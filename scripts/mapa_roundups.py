#!/usr/bin/env python3
"""Genera el mapa `Grupo búsqueda` → roundup que usa el nodo `Code` de Physics v3.

Lee el frontmatter de los roundups publicados y escupe el bloque `const ROUNDUPS`
listo para pegar. Antes de que los roundups llevaran `grupoBusqueda`, ese mapa se
mantenía a mano y el primero hubo que derivarlo cruzando ASIN contra Airtable.

Uso:
    venv/bin/python scripts/mapa_roundups.py            # el bloque para pegar
    venv/bin/python scripts/mapa_roundups.py --check    # solo avisa de huecos
"""

import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BLOG = RAIZ / "src" / "content" / "blog"


def campo(texto, nombre):
    m = re.search(rf'^{nombre}: "(.+)"$', texto, re.M)
    return m.group(1) if m else None


def roundups():
    for ruta in sorted(BLOG.glob("*.md")):
        texto = ruta.read_text(encoding="utf-8")
        if 'type: "roundup"' not in texto:
            continue
        yield ruta.stem, campo(texto, "grupoBusqueda"), campo(texto, "title")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Solo comprobar, sin imprimir el mapa.")
    args = parser.parse_args()

    encontrados, huerfanos = [], []
    for slug, grupo, titulo in roundups():
        (encontrados if grupo else huerfanos).append((slug, grupo, titulo))

    for slug, _, _ in huerfanos:
        print(f"AVISO: sin grupoBusqueda → {slug}", file=sys.stderr)

    # Dos roundups del mismo grupo romperían el mapa en silencio: el segundo
    # pisaría al primero y unos posts enlazarían a la comparativa equivocada.
    vistos = {}
    for slug, grupo, _ in encontrados:
        vistos.setdefault(grupo, []).append(slug)
    for grupo, slugs in vistos.items():
        if len(slugs) > 1:
            print(f"ERROR: el grupo '{grupo}' tiene {len(slugs)} roundups: {', '.join(slugs)}", file=sys.stderr)
            return 1

    print(f"{len(encontrados)} roundups con grupo, {len(huerfanos)} sin él", file=sys.stderr)
    if args.check:
        return 1 if huerfanos else 0

    print("const ROUNDUPS = {")
    for slug, grupo, titulo in sorted(encontrados, key=lambda r: r[1]):
        seguro = titulo.replace('"', "'")
        print(f'  "{grupo}": {{ slug: "{slug}", titulo: "{seguro}" }},')
    print("};")
    return 0


if __name__ == "__main__":
    sys.exit(main())
