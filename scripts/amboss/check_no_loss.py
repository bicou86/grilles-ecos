"""Signale les items <li> de la zone pedagogique presents dans BASE_REF et
disparus (sans equivalent suffisamment proche) dans l'etat courant du disque.

Usage :
    python3 scripts/amboss/check_no_loss.py BASE_REF [GRILLE_FILTRE]

Exemples :
    python3 scripts/amboss/check_no_loss.py 1873649
    python3 scripts/amboss/check_no_loss.py 1873649 AMBOSS-2_

Pour chaque grille modifiee entre BASE_REF et le disque (comparaison via
`git diff`, donc les modifications non commitees comptent aussi), les items
de la zone pedagogique entiere (lib.peda_bounds — resume/annexes jusqu'a
annexe-scenario, tous blocs confondus) **et ceux du bloc `annexe-dd`**
(lib.dd_bounds, situe en amont, dans la section Management) sont extraits
avant et apres, puis
compares avec le meme seuil de ressemblance que report_redundancy.py
(SequenceMatcher(...).ratio() > 0.72) : les deux scripts mesurent la meme
chose, cote disparition plutot que cote doublon restant — meme langage, memes
chiffres. La comparaison porte sur la zone entiere et non bloc par bloc : un
item deplace d'un bloc a l'autre (ex. le precedent beta-hCG, deplace de
`presentation` vers `expert`) n'est donc pas signale a tort.

Ceci est un RAPPORT, pas un test. Un item signale « disparu » n'est pas
forcement une perte : il peut avoir ete fusionne, reformule au point de
passer sous le seuil de ressemblance, ou legitimement supprime comme doublon
strict. Chaque signalement est fait pour relecture humaine (ou agent), il
n'est pas juge automatiquement. C'EST POURQUOI CE SCRIPT SORT TOUJOURS AVEC
LE CODE 0, y compris quand il signale des disparitions. Ne jamais le cabler
comme porte bloquante dans une chaine de verification : ce serait bloquer le
projet sur des suppressions parfaitement legitimes.
"""
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

ROOT = Path(__file__).resolve().parents[2]
THRESHOLD = 0.72  # identique a report_redundancy.py — meme mesure, face opposee.


def changed_grid_names(base_ref):
    """Noms des fichiers de grilles modifies entre base_ref et le disque courant."""
    result = subprocess.run(
        ["git", "diff", "--name-only", base_ref, "--", "cases/amboss"],
        cwd=ROOT, capture_output=True, encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"git diff a echoue pour {base_ref!r} : {result.stderr.strip()}")
        return set()
    return {Path(line).name for line in result.stdout.splitlines() if line.strip()}


def read_old(base_ref, path):
    """Contenu du fichier a base_ref, ou None s'il n'existait pas encore a cette reference."""
    rel = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{base_ref}:{rel}"],
        cwd=ROOT, capture_output=True, encoding="utf-8",
    )
    return result.stdout if result.returncode == 0 else None


def peda_items(html):
    """Items normalises de la zone pedagogique entiere, plus le bloc `annexe-dd`.

    `annexe-dd` vit dans la section Management, donc hors de `peda_bounds`, et se
    lit par ses propres bornes (`lib.dd_bounds`). Sans cet ajout, le bloc serait
    le seul contenu pedagogique du corpus qu'on pourrait reecrire sans qu'aucun
    controle ne signale une perte. Les deux zones sont disjointes : aucun item
    n'est compte deux fois. Elles sont fusionnees en une seule liste, et non
    comparees separement, pour la meme raison que les blocs le sont deja entre
    eux — un item deplace de `annexe-dd` vers `resume` est un deplacement
    legitime, pas une disparition.
    """
    items = []
    for start, end in (lib.peda_bounds(html), lib.dd_bounds(html)):
        if start >= 0:
            items += lib.list_items(html[start:end])
    return items


def disappeared(before, after):
    """Items de `before` sans equivalent (ratio > THRESHOLD) dans `after`."""
    return [item for item in before
            if not any(SequenceMatcher(None, item, other).ratio() > THRESHOLD
                       for other in after)]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    base_ref = sys.argv[1]
    only = sys.argv[2] if len(sys.argv) > 2 else None

    changed = changed_grid_names(base_ref)
    grids_checked = 0
    total_missing = 0
    for path in lib.grids():
        if only and only not in path.name:
            continue
        if path.name not in changed:
            continue
        grids_checked += 1

        old_html = read_old(base_ref, path)
        if old_html is None:
            print(f"\n=== {path.name} — absente de {base_ref}, ignoree ===")
            continue

        missing = disappeared(peda_items(old_html),
                               peda_items(path.read_text(encoding="utf-8")))
        if missing:
            total_missing += len(missing)
            print(f"\n=== {path.name} — {len(missing)} item(s) disparu(s) ===")
            for item in missing:
                print(f"  - {item[:100]}")
        else:
            print(f"\n=== {path.name} — aucun item disparu ===")

    if grids_checked == 0:
        suffix = f" (filtre : {only})" if only else ""
        print(f"Aucune grille modifiee entre {base_ref} et l'etat courant du disque{suffix}.")

    print(f"\nTOTAL : {total_missing} item(s) disparu(s) sur {grids_checked} grille(s) modifiee(s) "
          f"— a relire, une disparition n'est pas forcement une perte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
