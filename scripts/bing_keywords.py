#!/usr/bin/env python3
"""Compara volumen de búsqueda entre términos con la API de Bing Webmaster.

Bing es ~3-5 % del mercado en España, así que las cifras absolutas no valen
para nada. Lo que se usa es la PROPORCIÓN entre términos del mismo grupo: si
un sinónimo tiene 4x las impresiones de otro, esa relación se sostiene
razonablemente en Google aunque el número crudo no.

Uso típico:
    venv/bin/python scripts/bing_keywords.py
    venv/bin/python scripts/bing_keywords.py --country es --country mx
    venv/bin/python scripts/bing_keywords.py --terms "sonómetro,medidor de ruido"
    venv/bin/python scripts/bing_keywords.py --related "linterna frontal"
"""

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "notas" / "stats" / "bing"
BASE = "https://ssl.bing.com/webmaster/api.svc/json"
IDIOMA_POR_PAIS = {"es": "es-ES", "mx": "es-MX", "ar": "es-AR", "co": "es-CO", "cl": "es-CL"}

# Los sinónimos que deciden el título de cada roundup. Se comparan dentro del
# grupo, nunca entre grupos.
GRUPOS = {
    "sonometro": ["medidor de decibelios", "sonómetro", "medidor de ruido"],
    "frontal": ["linterna frontal", "frontal led", "linterna de cabeza"],
    "prismaticos": ["prismáticos", "binoculares"],
    "termografica": ["cámara termográfica", "cámara térmica"],
    "termometro": ["termómetro infrarrojo", "termómetro láser"],
    "dinamometrica": ["llave dinamométrica", "llave de par"],
}


def llamar(clave, metodo, parametros):
    respuesta = requests.get(
        f"{BASE}/{metodo}", params={**parametros, "apikey": clave}, timeout=30
    )
    if respuesta.status_code == 401:
        sys.exit("401: la clave de BING_API_KEY no es válida o no tiene acceso a la API.")
    if respuesta.status_code != 200:
        sys.exit(f"{respuesta.status_code} en {metodo}: {respuesta.text[:400]}")
    try:
        return respuesta.json()
    except ValueError:
        sys.exit(f"{metodo} no devolvió JSON:\n{respuesta.text[:400]}")


def desenvolver(carga):
    """La API es WCF y envuelve el resultado en 'd'. No siempre, según el método."""
    if isinstance(carga, dict) and "d" in carga:
        return carga["d"]
    return carga


def a_epoch(valor):
    """WCF serializa fechas como /Date(1755820800000)/."""
    if isinstance(valor, str):
        encontrado = re.search(r"/Date\((-?\d+)", valor)
        if encontrado:
            return int(encontrado.group(1)) // 1000
    return valor


def impresiones(fila):
    """`Impressions` es la métrica de la fila; `BroadImpressions` incluye variantes."""
    if not isinstance(fila, dict):
        return 0
    valor = fila.get("Impressions", fila.get("BroadImpressions", 0))
    return valor if isinstance(valor, (int, float)) else 0


def estadisticas(clave, termino, pais, idioma, bruto):
    datos = desenvolver(llamar(clave, "GetKeywordStats", {
        "q": termino, "country": pais, "language": idioma,
    }))
    if bruto:
        print(json.dumps(datos[:2] if isinstance(datos, list) else datos, indent=2, ensure_ascii=False))
    if not isinstance(datos, list):
        return 0, 0
    return sum(impresiones(f) for f in datos), len(datos)


def relacionados(clave, termino, pais, idioma, bruto):
    datos = desenvolver(llamar(clave, "GetRelatedKeywords", {
        "q": termino, "country": pais, "language": idioma,
    }))
    if bruto:
        print(json.dumps(datos[:3] if isinstance(datos, list) else datos, indent=2, ensure_ascii=False))
    filas = []
    for fila in datos if isinstance(datos, list) else []:
        if isinstance(fila, dict):
            filas.append((fila.get("Query") or fila.get("Keyword") or "?", impresiones(fila)))
    return sorted(filas, key=lambda f: -f[1])


def parsear_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--country", action="append", help="Repetible. Por defecto es y mx.")
    parser.add_argument("--terms", help="Términos sueltos separados por comas. Ignora los grupos.")
    parser.add_argument("--related", help="Saca la constelación de términos alrededor de este.")
    parser.add_argument("--grupo", action="append", choices=sorted(GRUPOS))
    parser.add_argument("--out", default=str(DESTINO))
    parser.add_argument("--raw", action="store_true", help="Vuelca el JSON crudo de la primera respuesta.")
    return parser.parse_args()


def main():
    load_dotenv(RAIZ / ".env")
    clave = os.getenv("BING_API_KEY")
    if not clave:
        sys.exit("Falta BING_API_KEY en .env")
    args = parsear_args()
    paises = args.country or ["es", "mx"]
    destino = Path(args.out).expanduser()
    destino.mkdir(parents=True, exist_ok=True)

    if args.related:
        for pais in paises:
            idioma = IDIOMA_POR_PAIS.get(pais, "es-ES")
            filas = relacionados(clave, args.related, pais, idioma, args.raw)
            print(f"\n=== relacionados con '{args.related}' ({pais}) ===")
            for termino, imp in filas[:25]:
                print(f"{imp:>8}  {termino}")
            with (destino / f"relacionados-{pais}.csv").open("w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow(["query", "impressions"])
                escritor.writerows(filas)
        return

    if args.terms:
        grupos = {"adhoc": [t.strip() for t in args.terms.split(",") if t.strip()]}
    else:
        grupos = {n: GRUPOS[n] for n in (args.grupo or sorted(GRUPOS))}

    salida = []
    for pais in paises:
        idioma = IDIOMA_POR_PAIS.get(pais, "es-ES")
        print(f"\n### {pais.upper()} ({idioma})")
        for nombre, terminos in grupos.items():
            medidos = []
            for termino in terminos:
                total, semanas = estadisticas(clave, termino, pais, idioma, args.raw)
                medidos.append((termino, total, semanas))
                salida.append({"country": pais, "grupo": nombre, "query": termino,
                               "impressions": total, "weeks": semanas})
            # El ratio va sobre la media semanal: dos términos pueden volver con
            # distinto número de semanas y comparar totales mentiría.
            medidos.sort(key=lambda m: -(m[1] / m[2] if m[2] else 0))
            cabeza = (medidos[0][1] / medidos[0][2] if medidos[0][2] else 0) or 1
            print(f"\n  {nombre}")
            for termino, total, semanas in medidos:
                media = total / semanas if semanas else 0
                print(f"    {media:>7.0f}/sem  ({media / cabeza:>4.0%})  {total:>6} en {semanas:>2} sem   {termino}")

    ruta = destino / "volumen-terminos.csv"
    with ruta.open("w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["country", "grupo", "query", "impressions", "weeks"])
        escritor.writeheader()
        escritor.writerows(salida)
    print(f"\n→ {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
