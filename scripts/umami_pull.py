#!/usr/bin/env python3
"""Saca de Umami de dónde viene el tráfico y quién pulsa los enlaces de afiliado.

La pregunta que motiva el script (2026-10-11): Amazon contó **31 clics de
afiliado** en 30 días mientras Search Console contaba **3 clics de búsqueda**.
Diez a uno. O hay tráfico que no viene de Google, o una parte de esos clics son
propios. Lo primero significa que el 3,23 % de conversión es real; lo segundo,
que el dato no vale.

Lo que saca, a `notas/stats/umami/`:

  resumen.csv      visitas, visitantes, páginas vistas y rebote por día
  referentes.csv   de dónde llegan (Google, Bing, directo, referidos)
  paginas.csv      qué se lee
  eventos.csv      `amazon-click` y `amazon-click-imagen`, que son los que
                   acaban en comisión

Uso:
    venv/bin/python scripts/umami_pull.py
    venv/bin/python scripts/umami_pull.py --dias 90

Credenciales en `.env` (no se piden por consola ni se imprimen nunca):

    UMAMI_PASSWORD=...        contraseña del usuario admin
    UMAMI_USER=admin          opcional, admin por defecto
    UMAMI_URL=https://stats.physicsofhobbies.com    opcional

Umami autoalojado v2 no tiene claves de API: se hace login contra
`/api/auth/login` y se usa el token devuelto durante la sesión.
"""

import argparse
import csv
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "notas" / "stats" / "umami"
URL_POR_DEFECTO = "https://stats.physicsofhobbies.com"
# De src/config/site.ts. Si algún día se crea otro sitio en la misma instancia,
# este es el valor que hay que tocar.
WEBSITE_ID = "499441fe-5423-4c87-816e-f2a635470022"


def iniciar_sesion(base, usuario, contrasena):
    r = requests.post(
        f"{base}/api/auth/login",
        json={"username": usuario, "password": contrasena},
        timeout=30,
    )
    if r.status_code == 401:
        sys.exit(
            "401: usuario o contraseña incorrectos.\n"
            "La contraseña del panel NO es UMAMI_DB_PASSWORD ni UMAMI_APP_SECRET: esas son la de\n"
            "Postgres y la de firma de sesiones. Si no la recuerdas hay que resetearla por SQL;\n"
            "está documentado en notas/umami-despliegue.md."
        )
    r.raise_for_status()
    token = r.json().get("token")
    if not token:
        sys.exit(f"El login respondió 200 pero sin token. Respuesta: {r.text[:200]}")
    return token


def pedir(base, token, ruta, parametros):
    r = requests.get(
        f"{base}{ruta}",
        params=parametros,
        headers={"Authorization": f"Bearer {token}"},
        timeout=60,
    )
    if r.status_code == 404:
        sys.exit(
            f"404 en {ruta}. Puede que esta versión de Umami use otra ruta; comprueba la versión\n"
            f"con: ssh oracle-altair 'sudo docker exec umami sh -c \"grep -m1 version /app/package.json\"'"
        )
    r.raise_for_status()
    return r.json()


def ms(fecha):
    """Umami cuenta el tiempo en milisegundos desde epoch, en UTC."""
    return int(fecha.replace(tzinfo=timezone.utc).timestamp() * 1000)


def escribir(nombre, cabeceras, filas, destino):
    destino.mkdir(parents=True, exist_ok=True)
    ruta = destino / nombre
    with open(ruta, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cabeceras)
        w.writerows(filas)
    print(f"  {len(filas):4d} filas  →  {ruta.relative_to(RAIZ)}")
    return ruta


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dias", type=int, default=30, help="ventana hacia atrás (30 por defecto)")
    p.add_argument("--out", default=str(DESTINO))
    args = p.parse_args()

    load_dotenv(RAIZ / ".env")
    contrasena = os.getenv("UMAMI_PASSWORD")
    if not contrasena:
        sys.exit(
            "Falta UMAMI_PASSWORD en .env. Añádela sin que pase por la consola:\n"
            "    echo 'UMAMI_PASSWORD=tu-contraseña' >> .env"
        )
    base = os.getenv("UMAMI_URL", URL_POR_DEFECTO).rstrip("/")
    usuario = os.getenv("UMAMI_USER", "admin")
    destino = Path(args.out)

    token = iniciar_sesion(base, usuario, contrasena)
    fin = datetime.now(timezone.utc)
    ini = fin - timedelta(days=args.dias)
    ventana = {"startAt": ms(ini), "endAt": ms(fin)}
    sitio = f"/api/websites/{WEBSITE_ID}"

    print(f"{base}  —  {ini:%Y-%m-%d} → {fin:%Y-%m-%d}  ({args.dias} días)\n")

    # ── Resumen por día ──────────────────────────────────────────────────
    serie = pedir(base, token, f"{sitio}/pageviews", {**ventana, "unit": "day", "timezone": "Europe/Madrid"})
    por_dia = {}
    for clave, campo in (("pageviews", "paginas_vistas"), ("sessions", "visitantes")):
        for punto in serie.get(clave, []):
            dia = str(punto.get("x", ""))[:10]
            por_dia.setdefault(dia, {})[campo] = punto.get("y", 0)
    filas = [[d, v.get("paginas_vistas", 0), v.get("visitantes", 0)] for d, v in sorted(por_dia.items())]
    escribir("resumen.csv", ["fecha", "paginas_vistas", "visitantes"], filas, destino)

    # ── De dónde llegan: ESTA es la pregunta ─────────────────────────────
    refs = pedir(base, token, f"{sitio}/metrics", {**ventana, "type": "referrer"})
    filas = [[r.get("x") or "(directo)", r.get("y", 0)] for r in refs]
    escribir("referentes.csv", ["referente", "visitas"], filas, destino)

    # ── Qué se lee ───────────────────────────────────────────────────────
    pags = pedir(base, token, f"{sitio}/metrics", {**ventana, "type": "url"})
    filas = [[r.get("x", ""), r.get("y", 0)] for r in pags]
    escribir("paginas.csv", ["ruta", "vistas"], filas, destino)

    # ── Clics de afiliado ────────────────────────────────────────────────
    evs = pedir(base, token, f"{sitio}/metrics", {**ventana, "type": "event"})
    eventos = [[r.get("x", ""), r.get("y", 0)] for r in evs]
    escribir("eventos.csv", ["evento", "veces"], eventos, destino)

    # ── Lectura rápida ───────────────────────────────────────────────────
    clics = sum(int(v) for nombre, v in eventos if str(nombre).startswith("amazon-click"))
    visitantes = sum(d.get("visitantes", 0) for d in por_dia.values())
    directo = next((int(v) for ref, v in
                    [[r.get("x") or "(directo)", r.get("y", 0)] for r in refs]
                    if ref == "(directo)"), 0)
    print(f"\n  clics de afiliado que ve Umami: {clics}")
    print(f"  visitantes en la ventana:       {visitantes}")
    print(f"  de ellos, tráfico directo:      {directo}")
    print(
        "\n  Compáralo con los 31 clics de Amazon y los clics de GSC. Si Umami ve bastantes menos\n"
        "  que Amazon, hay clics que no pasan por el sitio o el bloqueo de rastreadores se está\n"
        "  comiendo eventos. Si la mayoría de referentes son '(directo)', mira si son tuyos."
    )


if __name__ == "__main__":
    main()
