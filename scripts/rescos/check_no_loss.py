"""Signale les items de contenu presents dans BASE_REF et disparus dans l'etat
courant du disque, pour les grilles RESCOS.

Usage :
    python3 scripts/rescos/check_no_loss.py BASE_REF [GRILLE_FILTRE]

Exemples :
    python3 scripts/rescos/check_no_loss.py 383ade6
    python3 scripts/rescos/check_no_loss.py 383ade6 RESCOS-12_

Pour chaque grille modifiee entre BASE_REF et le disque (comparaison via
`git diff`, donc les modifications non commitees comptent aussi), les items de
TOUS les blocs de contenu (`lib.all_items` : annexe-dd, redflags, therapy,
cloture, resume, expert, theorie, presentation, scenario, annexe-image) sont
extraits avant et apres, puis compares avec le meme seuil de ressemblance que
`report_redundancy.py` (SequenceMatcher(...).ratio() > 0.72) : les deux scripts
mesurent la meme chose, cote disparition plutot que cote doublon restant.

La comparaison porte sur l'ensemble des blocs et non bloc par bloc : un item
deplace d'un bloc a l'autre — d'`annexe-dd` vers `resume`, de `therapy` vers
`presentation` — est un deplacement legitime, pas une disparition.

DIFFERENCE AVEC AMBOSS : la version AMBOSS lit deux ZONES (`peda_bounds` et
`dd_bounds`). Ici on lit les BLOCS eux-memes, comme dans German, parce que
quatre d'entre eux (`therapy`, `redflags`, `cloture`, et l'`annexe-dd` de 20
grilles sur 22) vivent en amont de la zone pedagogique, disperses au fil de la
page, et qu'aucune zone continue ne les englobe sans avaler aussi les criteres
notes. Passer par les blocs regle du meme coup le recouvrement des deux zones
sur RESCOS-14 et RESCOS-24, dont l'`annexe-dd` est justement DANS `annexes-grid`.

Le bloc `scenario` est ici INCLUS, alors que `report_redundancy.py` l'exclut de
son total : les deux scripts n'ont pas le meme objet. Exclure le scenario d'une
mesure de doublons est un choix editorial ; l'exclure d'un controle de perte
laisserait reecrire le script du patient sans trace.

Ceci est un RAPPORT, pas un test. Un item signale « disparu » n'est pas
forcement une perte : il peut avoir ete fusionne, reformule au point de passer
sous le seuil, ou legitimement supprime comme doublon strict. C'EST POURQUOI CE
SCRIPT SORT TOUJOURS AVEC LE CODE 0. Ne jamais le cabler comme porte bloquante :
ce serait bloquer le projet sur des suppressions parfaitement legitimes.
"""
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos as lib

ROOT = Path(__file__).resolve().parents[2]
THRESHOLD = 0.72  # identique a report_redundancy.py — meme mesure, face opposee.


def changed_grid_names(base_ref):
    """Noms des fichiers de grilles modifies entre base_ref et le disque courant."""
    result = subprocess.run(
        ["git", "diff", "--name-only", base_ref, "--", "cases/rescos"],
        cwd=ROOT, capture_output=True, encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"git diff a echoue pour {base_ref!r} : {result.stderr.strip()}")
        return set()
    return {Path(line).name for line in result.stdout.splitlines() if line.strip()}


def read_old(base_ref, path):
    """Contenu du fichier a base_ref, ou None s'il n'existait pas a cette reference."""
    rel = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{base_ref}:{rel}"],
        cwd=ROOT, capture_output=True, encoding="utf-8",
    )
    return result.stdout if result.returncode == 0 else None


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
    grids_checked = total_missing = 0
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

        missing = disappeared(lib.all_items(lib.strip_base64(old_html)),
                              lib.all_items(lib.strip_base64(
                                  path.read_text(encoding="utf-8"))))
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

    print(f"\nTOTAL : {total_missing} item(s) disparu(s) sur {grids_checked} grille(s) "
          f"modifiee(s) — a relire, une disparition n'est pas forcement une perte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
