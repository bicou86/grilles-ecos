#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fait basculer les grilles `rescos-locales` en thème sombre, comme les autres corpus.

Le constat. Les 166 grilles portent bien les règles `[data-theme="dark"]` que
`inject_semantic_css.py` leur a injectées — mais l'attribut n'est jamais posé :
elles ne chargent ni `theme-sync.js`, ni `mobile-responsive.css`. Mesuré en
navigateur : azygos, german et casecos rendent la palette sombre ; ces 166-là
restent en clair, seules de leur espèce.

Ce que le script ajoute, et pourquoi ces deux fichiers exactement :

    <script src="../theme-sync.js"></script>       pose `data-theme` sur <html>
    <link rel="stylesheet" href="../mobile-responsive.css">   les 133 règles sombres

Le second n'est pas optionnel. `theme-sync.js` seul poserait l'attribut sans
que rien ne suive, sauf les huit classes sémantiques : on obtiendrait des
couleurs vives sur fond blanc, c'est-à-dire pire qu'avant.

Le modèle est `cases/casecos/`, qui a exactement le même profil — mise en page
locale dans un `<style>` en ligne, pas de `case-styles.css` — et charge ces
deux fichiers juste après son `</style>`. On copie cet emplacement : après la
feuille locale, donc en mesure de la surcharger.

`case-styles.css` n'est PAS ajouté. La procédure du corpus est explicite : les
165 `<style>` en ligne *sont* la mise en page de ce volet, et c'est délibéré.

Idempotent : une grille déjà traitée est laissée telle quelle, à l'octet près.

Usage
-----
    apply_theme_sync.py [--check]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib  # noqa: E402

MARQUE = '<script src="../theme-sync.js"></script>'
BLOC = ('    ' + MARQUE + "\n"
        '    <link rel="stylesheet" href="../mobile-responsive.css">\n')

#: Le point d'insertion est la fermeture du `<head>`, comme dans `casecos` :
#: après la feuille locale, donc en mesure de la surcharger, et avant le corps.
#:
#: Viser `</style>` suivi de `<body>` ne marche PAS — il y a un `</head>` entre
#: les deux, et les 166 grilles ont échoué là-dessus. `</head>` est à la fois
#: plus simple et plus sûr : une seule occurrence par fichier.
FIN_STYLE = re.compile(r"(?=</head>)")


def applique(html: str) -> tuple[str, str]:
    """Rend (html_modifié, état) — 'deja', 'ok', ou un motif d'échec."""
    if MARQUE in html:
        return html, "deja"
    m = FIN_STYLE.search(html)
    if not m:
        return html, "pas de </style> de tête avant <body>"

    sortie = html[:m.end()] + BLOC + html[m.end():]
    # Contrôle d'inversibilité : retirer le bloc doit redonner l'entrée exacte.
    if sortie.replace(BLOC, "", 1) != html:
        return html, "strip-back non inversible"
    return sortie, "ok"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="diagnostique sans écrire")
    args = ap.parse_args()

    faits, deja, echecs = 0, 0, []
    for grille in lib.grids():
        html = grille.read_text(encoding="utf-8")
        sortie, etat = applique(html)
        if etat == "deja":
            deja += 1
        elif etat == "ok":
            faits += 1
            if not args.check:
                grille.write_text(sortie, encoding="utf-8")
        else:
            echecs.append(f"{grille.name}: {etat}")

    verbe = "à traiter" if args.check else "traitées"
    print(f"{faits} grille(s) {verbe}, {deja} déjà en place, {len(echecs)} échec(s)")
    for e in echecs:
        print("   ", e)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
