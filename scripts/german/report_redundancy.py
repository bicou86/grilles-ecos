"""Liste les paires d'items quasi identiques entre blocs de contenu German.

Usage :
    python3 scripts/german/report_redundancy.py [GRILLE_FILTRE] [--intra] [--quiet]

Par defaut, seules les paires INTER-BLOCS sont comptees (`if b1 == b2:
continue`) — meme convention, meme seuil (0.72) et meme unite que
`scripts/amboss/report_redundancy.py`, pour que les deux corpus se lisent dans
le meme langage. Le comportement par defaut ne doit pas changer : toute mesure
du projet cesserait d'etre comparable.

`--intra` ajoute les paires INTRA-BLOC. Les deux totaux restent affiches
separement, jamais additionnes.

`--quiet` n'affiche que le tableau par grille et les totaux, sans le detail des
paires — utile pour un releve.

DIFFERENCE AVEC AMBOSS : un bloc peut apparaitre plusieurs fois dans une meme
grille (deux `annexe-dd` en German-78, jusqu'a trois `therapy-section`). Les
segments d'un meme bloc sont donc concatenes en une seule liste d'items sous le
nom du bloc — deux `therapy-section` de la meme grille comptent comme intra, ce
qui est exact : c'est bien le meme role editorial.
"""
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_german as lib

THRESHOLD = 0.72  # identique a AMBOSS — meme mesure.


def pairs_for(path, intra=False):
    html = lib.strip_base64(path.read_text(encoding="utf-8"))
    items = []
    for name, _, _ in lib.BLOCKS:
        for segment in lib.block_segments(html, name):
            items += [(name, t) for t in lib.list_items(segment)]
    out = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            b1, t1 = items[i]
            b2, t2 = items[j]
            if b1 == b2 and not intra:
                continue
            ratio = SequenceMatcher(None, t1, t2).ratio()
            if ratio > THRESHOLD:
                out.append((round(ratio, 2), b1, t1, b2, t2))
    return sorted(out, reverse=True)


def main():
    args = sys.argv[1:]
    intra = "--intra" in args
    quiet = "--quiet" in args
    positional = [a for a in args if not a.startswith("--")]
    only = positional[0] if positional else None

    grand = grand_intra = 0
    per_grid = []
    by_pair = Counter()
    for path in lib.grids():
        if only and only not in path.name:
            continue
        found = pairs_for(path, intra=intra)
        inter = [p for p in found if p[1] != p[3]]
        same = [p for p in found if p[1] == p[3]]
        grand += len(inter)
        grand_intra += len(same)
        per_grid.append((path.name, len(inter), len(same)))
        for _, b1, _, b2, _ in inter:
            by_pair[tuple(sorted((b1, b2)))] += 1
        if found and not quiet:
            label = f"{len(inter)} paire(s)"
            if intra:
                label += f" + {len(same)} intra-bloc"
            print(f"\n=== {path.name} — {label} ===")
            for ratio, b1, t1, b2, t2 in found:
                tag = "  [intra]" if b1 == b2 else ""
                print(f"  [{ratio}] {b1} <-> {b2}{tag}")
                print(f"      A: {t1[:100]}")
                print(f"      B: {t2[:100]}")

    print("\n--- paires inter-blocs par grille (grilles a 0 omises) ---")
    for name, n_inter, n_intra in per_grid:
        if n_inter or (intra and n_intra):
            suffix = f"  (+{n_intra} intra)" if intra else ""
            print(f"  {n_inter:4d}{suffix}  {name}")
    print("\n--- paires inter-blocs par couple de blocs ---")
    for (b1, b2), n in by_pair.most_common():
        print(f"  {n:4d}  {b1} <-> {b2}")
    print(f"\nTOTAL : {grand} paire(s) quasi identiques")
    if intra:
        print(f"TOTAL INTRA-BLOC : {grand_intra} paire(s) — mesure additionnelle, "
              f"hors du chiffre de reference du projet")


if __name__ == "__main__":
    main()
