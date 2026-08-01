"""Verifie que le bareme declare est ATTEIGNABLE par le calcul. Sortie 1 si ecart.

Usage :
    python3 scripts/german/check_reachability.py [GRILLE_FILTRE]

Exemples :
    python3 scripts/german/check_reachability.py            # les 88 grilles
    python3 scripts/german/check_reachability.py German-9_  # detail d'une grille

La simulation elle-meme (`parse_config`, `section_max`, `orphan_criteria`,
`check_one`) est importee de `scripts/amboss/check_reachability.py`, sans copie.
Elle ne depend d'aucune particularite de corpus : elle rejoue
`cases/scoring.js` sur `window.caseConfig`, dont les 88 grilles German portent
exactement la meme forme que les 40 grilles AMBOSS (`maxScores`, `coef`,
`sectionInfo[{key, prefix, count, scoreId, isComm}]`, memes quatre sections a
0.25 chacune, meme gabarit de `<span class="score">`). Seule l'enumeration des
grilles change, et c'est tout ce que ce fichier redefinit.

POURQUOI CE CONTROLE EST DISTINCT DE check_invariants.py
--------------------------------------------------------
`check_invariants.py` compare l'etat courant a un snapshot : il repond a « le
bareme est-il le meme qu'hier ? », jamais a « le bareme est-il juste ? ». Un
bareme faux depuis l'origine reste vert indefiniment — c'est ce qui s'est
produit sur AMBOSS-9, dont le defaut, present des le commit initial, n'a ete vu
qu'apres quinze taches.

Ce script ne compare rien a un passe : il simule le remplissage complet (chaque
case de detail cochee, chaque radio au maximum, chaque item de communication au
niveau A) et exige que le total tombe sur `maxScores[key]` ET sur le
denominateur affiche au candidat, et que le pourcentage global fasse 100 %.
Trois ecarts sont detectes ici et par rien d'autre : un `count` trop grand
(critere promis, absent de la page), un sous-item ORPHELIN hors de la sequence
`prefix1..prefixN` (cochable mais jamais compte), et un `maxScores` qui diverge
du `<span>` affiche.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_german as lib

_amboss = lib.amboss_module("check_reachability")
parse_config = _amboss.parse_config
section_max = _amboss.section_max
orphan_criteria = _amboss.orphan_criteria
check_one = _amboss.check_one


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    checked, bad = 0, 0
    for path in lib.grids():
        if only and only not in path.name:
            continue
        checked += 1
        ok, lines = check_one(path)
        if not ok:
            bad += 1
        if not ok or only:
            print(f'{path.name}  {"OK" if ok else "ECART"}')
            print("\n".join(lines))

    if only and checked == 0:
        print(f"Aucune grille ne correspond au filtre {only!r}.")
        return 1
    if bad:
        print(f"\nECHEC — {bad} grille(s) sur {checked} au bareme inatteignable")
        return 1
    print(f"\nOK — {checked} grille(s), bareme atteignable a 100 % sur chaque section")
    return 0


if __name__ == "__main__":
    sys.exit(main())
