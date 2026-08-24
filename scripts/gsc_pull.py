#!/usr/bin/env python3
"""Descarga los datos de Google Search Console a CSV.

La API sirve los 16 meses de histórico en cualquier momento, así que cada
ejecución rehace los ficheros enteros en lugar de ir acumulando. Si un día no
se ejecuta, no se pierde nada.

Uso típico:
    venv/bin/python scripts/gsc_pull.py --list-sites
    venv/bin/python scripts/gsc_pull.py
"""

import argparse
import csv
import os
import sys
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import quote

from dotenv import load_dotenv
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "notas" / "stats" / "gsc"
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
BASE = "https://searchconsole.googleapis.com/webmasters/v3"
FILAS_POR_PAGINA = 25000
METRICAS = ["clicks", "impressions", "ctr", "position"]

# GSC omite las filas cuya consulta es demasiado rara para anonimizarla, así
# que la suma de "consultas" no cuadra con la de "totales". Los totales son los
# buenos; las otras series sirven para saber por qué términos y páginas entra.
SERIES = {
    "totales": ["date"],
    "consultas": ["date", "query"],
    "paginas": ["date", "page"],
    "segmentos": ["date", "country", "device"],
}


def abrir_sesion(ruta):
    if not ruta:
        sys.exit(
            "Falta el JSON de la service account.\n"
            "Pásalo con --credentials o define GSC_SERVICE_ACCOUNT_JSON en .env"
        )
    ruta = Path(ruta).expanduser()
    if not ruta.is_file():
        sys.exit(f"No existe el fichero de credenciales: {ruta}")
    credenciales = service_account.Credentials.from_service_account_file(
        str(ruta), scopes=[SCOPE]
    )
    return AuthorizedSession(credenciales)


def listar_sitios(sesion):
    respuesta = sesion.get(f"{BASE}/sites")
    respuesta.raise_for_status()
    return respuesta.json().get("siteEntry", [])


def consultar(sesion, sitio, inicio, fin, dimensiones, estado):
    url = f"{BASE}/sites/{quote(sitio, safe='')}/searchAnalytics/query"
    filas = []
    arranque = 0
    while True:
        respuesta = sesion.post(
            url,
            json={
                "startDate": inicio,
                "endDate": fin,
                "dimensions": dimensiones,
                "rowLimit": FILAS_POR_PAGINA,
                "startRow": arranque,
                "dataState": estado,
            },
        )
        if respuesta.status_code == 403:
            sys.exit(
                f"403 sobre '{sitio}'.\n"
                "La service account no tiene permiso sobre esa propiedad, o el\n"
                "identificador no es el correcto. Comprueba ambas cosas con:\n"
                f"    {sys.argv[0]} --list-sites"
            )
        respuesta.raise_for_status()
        lote = respuesta.json().get("rows", [])
        filas.extend(lote)
        if len(lote) < FILAS_POR_PAGINA:
            return filas
        arranque += FILAS_POR_PAGINA


def escribir_csv(ruta, dimensiones, filas):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", newline="", encoding="utf-8") as fichero:
        escritor = csv.writer(fichero)
        escritor.writerow(dimensiones + METRICAS)
        for fila in filas:
            escritor.writerow(
                list(fila.get("keys", []))
                + [
                    fila.get("clicks", 0),
                    fila.get("impressions", 0),
                    round(fila.get("ctr", 0.0), 6),
                    round(fila.get("position", 0.0), 2),
                ]
            )


def parsear_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", default=os.getenv("GSC_SITE_URL", "sc-domain:physicsofhobbies.com"))
    parser.add_argument("--credentials", default=os.getenv("GSC_SERVICE_ACCOUNT_JSON"))
    parser.add_argument("--start", help="YYYY-MM-DD (por defecto, 16 meses atrás)")
    parser.add_argument("--end", help="YYYY-MM-DD (por defecto, hoy menos 2 días)")
    parser.add_argument("--out", default=str(DESTINO))
    parser.add_argument(
        "--serie",
        action="append",
        choices=sorted(SERIES),
        help="Serie a descargar; repetible. Por defecto, todas.",
    )
    parser.add_argument(
        "--dimensions",
        help="Dimensiones sueltas separadas por comas, para una consulta ad-hoc. Ignora --serie.",
    )
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="Incluye los últimos días sin consolidar (dataState=ALL). Esas cifras cambian.",
    )
    parser.add_argument(
        "--list-sites",
        action="store_true",
        help="Lista las propiedades visibles para la service account y sale.",
    )
    return parser.parse_args()


def main():
    load_dotenv(RAIZ / ".env")
    args = parsear_args()
    sesion = abrir_sesion(args.credentials)

    if args.list_sites:
        for entrada in listar_sitios(sesion):
            print(f"{entrada.get('permissionLevel', '?'):<20} {entrada.get('siteUrl')}")
        return

    fin = args.end or (date.today() - timedelta(days=2)).isoformat()
    inicio = args.start or (date.fromisoformat(fin) - timedelta(days=480)).isoformat()
    estado = "ALL" if args.fresh else "FINAL"
    destino = Path(args.out).expanduser()

    if args.dimensions:
        series = {"adhoc": [d.strip() for d in args.dimensions.split(",") if d.strip()]}
    else:
        series = {n: SERIES[n] for n in (args.serie or sorted(SERIES))}

    print(f"{args.site}  {inicio} → {fin}  ({estado})\n")
    for nombre, dimensiones in series.items():
        filas = consultar(sesion, args.site, inicio, fin, dimensiones, estado)
        ruta = destino / f"{nombre}.csv"
        escribir_csv(ruta, dimensiones, filas)
        clics = sum(f.get("clicks", 0) for f in filas)
        impresiones = sum(f.get("impressions", 0) for f in filas)
        print(
            f"{nombre:<12} {len(filas):>6} filas  "
            f"{clics:>5} clics  {impresiones:>7} impresiones  →  {ruta.relative_to(RAIZ)}"
        )


if __name__ == "__main__":
    main()
