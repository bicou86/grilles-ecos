#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrige dans le vault les extensions qui ne correspondent pas au format réel.

Pourquoi. `fetch_image.py` contrôle la signature du fichier avant de le livrer,
et refuse tout fichier dont l'en-tête contredit l'extension. Le contrôle est
juste — c'est la donnée qui est fausse. Conséquence : des images intactes et
pertinentes sont inaccessibles aux grilles, dont plusieurs documentent
littéralement un critère noté (score de Genève révisé, gradations de l'HSA,
équivalences de corticoïdes, algorithmes « fièvre sans foyer »).

Ce que fait ce script.

  1. Il détecte le format réel par la signature des premiers octets, jamais par
     le nom.
  2. Il renomme le fichier avec la bonne extension.
  3. Il met à jour **toutes** les citations du vault — `![[nom.ext]]`,
     `[[nom.ext]]`, `![](chemin/nom.ext)` — dans les 365 notes.
  4. Il écrit un **journal de réversibilité** : chaque ligne porte l'ancien et
     le nouveau chemin, plus la liste des notes modifiées. `--undo` rejoue le
     journal à l'envers.

Sécurités, vérifiées avant toute écriture :

  - **aucune collision** : si le nom corrigé existe déjà, le fichier est laissé
    tel quel et signalé (comparaison insensible à la casse, APFS l'étant) ;
  - **le vault n'est pas sous git** : rien n'est écrit sans que le journal ne
    soit d'abord ouvert en écriture ;
  - **comptage symétrique** : le nombre de citations réécrites doit égaler le
    nombre de citations trouvées, note par note.

Usage
-----
    fix_vault_extensions.py --check          diagnostique, n'écrit rien
    fix_vault_extensions.py                  applique et journalise
    fix_vault_extensions.py --undo JOURNAL   rejoue le journal à l'envers
"""
import argparse
import os
import re
import sys
from datetime import datetime

VAULT = os.environ.get(
    "ECOS_VAULT", "/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian")

#: Signatures reconnues. Un format non reconnu ne declenche aucun renommage :
#: mieux vaut ignorer un fichier exotique que de le renommer a tort.
def format_reel(chemin):
    with open(chemin, "rb") as fh:
        tete = fh.read(12)
    if tete.startswith(b"\x89PNG"):
        return "png"
    if tete.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if tete[:4] == b"RIFF" and tete[8:12] == b"WEBP":
        return "webp"
    if tete[:4] in (b"GIF8",):
        return "gif"
    return None


EXT_IMAGE = ("png", "jpg", "jpeg", "webp", "gif")


def parcourt(racine, suffixes):
    for dossier, _, fichiers in os.walk(racine):
        if "/." in dossier:
            continue
        for f in fichiers:
            if f.lower().endswith(suffixes):
                yield os.path.join(dossier, f)


def a_corriger():
    """Rend [(chemin, ancien_nom, nouveau_nom)] et la liste des collisions."""
    presents = {p.lower() for p in parcourt(VAULT, tuple("." + e for e in EXT_IMAGE))}
    plan, collisions = [], []
    for p in parcourt(VAULT, tuple("." + e for e in EXT_IMAGE)):
        nom = os.path.basename(p)
        ext = os.path.splitext(nom)[1].lower().lstrip(".")
        ext = "jpg" if ext == "jpeg" else ext
        reel = format_reel(p)
        if reel is None or reel == ext:
            continue
        neuf = os.path.splitext(nom)[0] + "." + reel
        chemin_neuf = os.path.join(os.path.dirname(p), neuf)
        if chemin_neuf.lower() in presents:
            collisions.append((nom, neuf))
        else:
            plan.append((p, nom, neuf))
    return plan, collisions


def applique(plan, ecrire, journal):
    notes = list(parcourt(VAULT, (".md",)))
    contenus = {n: open(n, encoding="utf-8", errors="replace").read() for n in notes}
    renommes = 0
    citations = 0
    for chemin, ancien, neuf in plan:
        touchees = []
        for n in notes:
            c = contenus[n]
            if ancien not in c:
                continue
            avant = c.count(ancien)
            c = c.replace(ancien, neuf)
            apres_reste = c.count(ancien)
            if apres_reste:                      # comptage symetrique
                raise SystemExit(
                    "ARRET — %s : %d citation(s) non reecrite(s) dans %s"
                    % (ancien, apres_reste, n))
            contenus[n] = c
            touchees.append((n, avant))
            citations += avant
        if ecrire:
            os.rename(chemin, os.path.join(os.path.dirname(chemin), neuf))
            journal.write("RENAME\t%s\t%s\n" % (chemin, neuf))
            for n, k in touchees:
                journal.write("CITE\t%s\t%s\t%s\t%d\n" % (n, ancien, neuf, k))
        renommes += 1
    if ecrire:
        for n, c in contenus.items():
            if c != open(n, encoding="utf-8", errors="replace").read():
                open(n, "w", encoding="utf-8").write(c)
    return renommes, citations


def annule(chemin_journal):
    lignes = open(chemin_journal, encoding="utf-8").read().rstrip("\n").split("\n")
    notes = {}
    for l in reversed(lignes):
        if l.startswith("#") or not l.strip():
            continue
        parts = l.split("\t")
        if parts[0] == "RENAME":
            _, ancien, neuf = parts
            actuel = os.path.join(os.path.dirname(ancien), neuf)
            if os.path.exists(actuel):
                os.rename(actuel, ancien)
        elif parts[0] == "CITE":
            _, note, ancien, neuf, _k = parts
            if note not in notes:
                notes[note] = open(note, encoding="utf-8", errors="replace").read()
            notes[note] = notes[note].replace(neuf, ancien)
    for n, c in notes.items():
        open(n, "w", encoding="utf-8").write(c)
    print("Annulation appliquee : %d note(s) restauree(s)" % len(notes))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="diagnostique sans ecrire")
    ap.add_argument("--undo", metavar="JOURNAL", help="rejoue un journal a l'envers")
    args = ap.parse_args()

    if args.undo:
        annule(args.undo)
        return 0

    plan, collisions = a_corriger()
    print("%d fichier(s) a renommer, %d collision(s)" % (len(plan), len(collisions)))
    for a, b in collisions:
        print("  COLLISION %s -> %s (existe deja, laisse tel quel)" % (a, b))

    if args.check:
        _, cit = applique(plan, False, None)
        print("%d citation(s) seraient mises a jour" % cit)
        return 0

    horo = datetime.now().strftime("%Y%m%d-%H%M%S")
    chemin_journal = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "vault-renommages-%s.tsv" % horo)
    with open(chemin_journal, "w", encoding="utf-8") as journal:
        journal.write("# Journal de reversibilite — %s\n" % horo)
        journal.write("# Rejouer a l'envers : fix_vault_extensions.py --undo %s\n"
                      % os.path.basename(chemin_journal))
        n, cit = applique(plan, True, journal)
    print("%d fichier(s) renomme(s), %d citation(s) mise(s) a jour" % (n, cit))
    print("Journal : %s" % chemin_journal)
    return 0


if __name__ == "__main__":
    sys.exit(main())
