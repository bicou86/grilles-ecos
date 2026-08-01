"""Liste les paires d'items quasi identiques entre blocs pedagogiques.

Usage :
    python3 scripts/amboss/report_redundancy.py [GRILLE_FILTRE] [--intra]

Par defaut, seules les paires INTER-BLOCS sont comptees (`if b1 == b2:
continue`). C'est la mesure de reference du projet — les 301 paires de depart,
tous les releves intermediaires et le chiffre final sont exprimes dans cette
unite. **Le comportement par defaut ne doit pas changer** : toute mesure du
projet cesserait d'etre comparable.

`--intra` ajoute les paires INTRA-BLOC — deux items du meme bloc qui disent la
meme chose. Cet angle mort n'a jamais ete mesure : il etait visible seulement
par ricochet, quand deux items d'un `resume` s'appariaient au meme item de la
`presentation` (observe sur AMBOSS-1, echographie, et AMBOSS-31, radiographie).
Les deux totaux restent affiches separement, jamais additionnes, pour que le
chiffre de reference reste lisible tel quel.
"""
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

THRESHOLD = 0.72


def pairs_for(path, intra=False):
    html = path.read_text(encoding="utf-8")
    items = []
    for name, _, _ in lib.BLOCKS:
        seg = lib.block_segment(html, name)
        if seg:
            items += [(name, t) for t in lib.list_items(seg)]
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
    positional = [a for a in args if not a.startswith("--")]
    only = positional[0] if positional else None

    grand = 0
    grand_intra = 0
    for path in lib.grids():
        if only and only not in path.name:
            continue
        found = pairs_for(path, intra=intra)
        inter = [p for p in found if p[1] != p[3]]
        same = [p for p in found if p[1] == p[3]]
        grand += len(inter)
        grand_intra += len(same)
        if found:
            label = f"{len(inter)} paire(s)"
            if intra:
                label += f" + {len(same)} intra-bloc"
            print(f"\n=== {path.name} — {label} ===")
            for ratio, b1, t1, b2, t2 in found:
                tag = "  [intra]" if b1 == b2 else ""
                print(f"  [{ratio}] {b1} <-> {b2}{tag}")
                print(f"      A: {t1[:100]}")
                print(f"      B: {t2[:100]}")
    print(f"\nTOTAL : {grand} paire(s) quasi identiques")
    if intra:
        print(f"TOTAL INTRA-BLOC : {grand_intra} paire(s) — mesure additionnelle, "
              f"hors du chiffre de reference du projet")


if __name__ == "__main__":
    main()
