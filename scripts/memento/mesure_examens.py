#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mesure ce que couterait de DEVINER le partage 🔬 / 💊 du management.

    python3 scripts/memento/mesure_examens.py

POURQUOI CE SCRIPT EXISTE. Le memento des neuf grilles officielles partage le
management en deux encadres — 🔬 examens complementaires et 💊 prise en charge.
Ce partage n'existe pas dans les grilles : il est declare A LA MAIN, critere
par critere, dans la table `EXAMENS` de scripts/build_obsidian_memento.py. Les
mementos par SSP couvrent 252 grilles et pres de 2 000 items de management ; la
declaration manuelle y est hors d'atteinte, et build_memento.py n'imprime donc
qu'un seul encadre 💊.

CE SCRIPT EST LA JUSTIFICATION CHIFFREE DE CE CHOIX, et il est verse au depot
pour qu'elle soit refaisable plutot que citee. Il confronte un motif lexical au
SEUL echantillon etiquete qui existe — ces neuf grilles — et imprime chaque
desaccord, ligne par ligne, pour qu'ils se relisent au lieu de se resumer.

CE N'EST PAS UN VERIFICATEUR : il ne garde aucun invariant et sort toujours 0.
Il mesure, il n'echoue pas. D'ou le nom `mesure_*` et non `check_*`.

Ce que la mesure a montre (2026-08-16) : 5 desaccords sur 57 lignes. Le motif
n'est pas optimise, mais les cinq desaccords ne sont PAS des artefacts de
frontiere de mot — ils tiennent au SENS de la ligne, et aucune liste de
mots-cles ne les tranche :

    RESCOS-67b m6  « Propose un dosage des anticorps anti-TPO »        🔬 -> 💊
    RESCOS-67b m8  « Suivi : prevoir un controle biologique... »       💊 -> 🔬
    RESCOS-67b m3  « Interprete correctement les resultats de labo »   💊 -> 🔬
    RESCOS-58b m4  « Propose une hospitalisation (suivi Hb et inv.) »  💊 -> 🔬
    RESCOS-57b m1  « Questionne sur l'examen clinique realise »        💊 -> 🔬

Une erreur de rangement ne se voit pas a la lecture, contrairement a un suffixe
faux : le lecteur croit l'encadre 🔬 exhaustif et ne cherche pas l'examen
ailleurs. Voir le commentaire au-dessus de LEGENDE dans lib_rendu.py.
"""
import importlib.util
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L                                # noqa: E402

REPO = Path(__file__).resolve().parents[2]
OFFICIEL = REPO / "scripts" / "build_obsidian_memento.py"

# Le motif le plus genereux qu'on puisse ecrire sans etudier le corpus. Les
# bornes \b sur les sigles courts sont INDISPENSABLES : sans elles, « ct »
# repond dans « Protection », « victimes » et « directives », et « irm » dans
# « infirmier·ere » — huit faux positifs qui n'apprennent rien sur la
# faisabilite du partage, seulement sur la redaction du motif.
MOTIF = re.compile(
    r"examen|investigation|laborat|imagerie|bilan|radiograph|scanner|"
    r"\bct\b|\birm\b|echograph|ultrason|prise de sang|frottis|"
    r"serolog|depistage|biolog|analys|\becg\b|\bfsc\b|test", re.I)


def memento_officiel():
    """Le module du memento officiel, importe sans executer son bloc principal."""
    spec = importlib.util.spec_from_file_location("build_obsidian_memento", OFFICIEL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)          # le corps utile est sous __main__
    return module


def lignes_de_management(fichier):
    """(identifiant de critere, libelle) des items de management d'une grille."""
    chemin = REPO / "cases" / "rescos" / fichier
    html = unicodedata.normalize("NFC", chemin.read_text(encoding="utf8"))
    secs = L.sections(html[html.index("<body"):])
    return [(cid, titre) for genre, cid, titre, _ in L.items(secs.get("m", ""))
            if genre == "item"]


def main():
    officiel = memento_officiel()
    total, desaccords = 0, []
    for fichier, _, _, _, _ in officiel.CAS:
        grille = fichier.split(" -")[0].split("_-_")[0]
        declares = officiel.EXAMENS[grille]
        for cid, titre in lignes_de_management(fichier):
            total += 1
            humain = cid in declares
            motif = bool(MOTIF.search(L.sans_accent(titre)))
            if humain != motif:
                desaccords.append((grille, cid, humain, titre))

    print(f"{len(officiel.CAS)} grilles officielles · {total} lignes de management "
          f"étiquetées à la main · {len(desaccords)} désaccord(s) du motif lexical\n")
    for grille, cid, humain, titre in desaccords:
        sens = "🔬 attendu, 💊 deviné" if humain else "💊 attendu, 🔬 deviné"
        print(f"  {grille:<12} {cid:<4} {sens}")
        print(f"               {titre[:96]}")
    print(f"\nUn motif lexical se tromperait sur {len(desaccords)} ligne(s) sur {total} "
          f"({100 * len(desaccords) / total:.0f} %) là où le partage est vérifiable.")
    print("Le corpus par SSP en compte près de 2 000, sans aucune étiquette.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
