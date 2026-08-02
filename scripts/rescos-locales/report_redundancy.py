"""Liste les paires d'items quasi identiques entre blocs de contenu rescos-locales.

Usage :
    python3 scripts/rescos-locales/report_redundancy.py [GRILLE_FILTRE] [--intra]
                                                        [--quiet] [--with-scenario]

Par defaut, seules les paires INTER-BLOCS sont comptees (`if b1 == b2:
continue`) — meme convention, meme seuil (0.72) et meme unite que les trois
corpus precedents, pour qu'ils se lisent dans le meme langage. Le comportement
par defaut ne doit pas changer : toute mesure du projet cesserait d'etre
comparable.

`--intra` ajoute les paires INTRA-BLOC. Les deux totaux restent affiches
separement, jamais additionnes.

`--quiet` n'affiche que le tableau par grille et les totaux, sans le detail des
paires — utile pour un releve.

LE BLOC `scenario` EST EXCLU PAR DEFAUT
---------------------------------------
`annexe-scenario` est le SCRIPT DU PATIENT SIMULE : redire les symptomes deja
listes dans le `resume` ou la `presentation` est sa fonction meme. AMBOSS
l'exclut deja de fait (son `BLOCKS` ne le contient pas), RESCOS explicitement.
Le bloc reste dans `lib.BLOCKS` : il est borne, gele au snapshot, verifie par
`bounds_anomalies` et protege par `check_no_loss`. Ce n'est pas un angle mort,
c'est une exclusion documentee, et `--with-scenario` la leve.

ECHELLE — ce corpus n'est pas du meme ordre que les precedents
---------------------------------------------------------------
27,1 Mo hors base64 contre 3,8 pour RESCOS, 165 grilles contre 41, et jusqu'a
1 400 items dans une seule grille. Le cout est quadratique en items PAR GRILLE
(les grilles ne sont jamais comparees entre elles) : compter sur plusieurs
minutes pour un passage complet. `--quiet` ne change rien au calcul, seulement
a l'affichage.

Comme dans RESCOS, un bloc peut apparaitre plusieurs fois dans une meme grille
(jusqu'a 8 `therapy-section`, 8 `cloture-item`). Les segments d'un meme bloc
sont donc concatenes en une seule liste d'items sous le nom du bloc — deux
`therapy-section` de la meme grille comptent comme intra, ce qui est exact :
c'est bien le meme role editorial.
"""
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib

THRESHOLD = 0.72  # identique a AMBOSS, German et RESCOS — meme mesure.


def pairs_for(path, intra=False, with_scenario=False):
    html = lib.strip_base64(path.read_text(encoding="utf-8"))
    excluded = set() if with_scenario else lib.REDUNDANCY_EXCLUDED
    items = []
    for name, _, _ in lib.BLOCKS:
        if name in excluded:
            continue
        for segment in lib.block_segments(html, name):
            items += [(name, t) for t in lib.list_items(segment)]
    out = []
    for i in range(len(items)):
        b1, t1 = items[i]
        for j in range(i + 1, len(items)):
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
    with_scenario = "--with-scenario" in args
    positional = [a for a in args if not a.startswith("--")]
    only = positional[0] if positional else None

    grand = grand_intra = 0
    per_grid = []
    by_pair = Counter()
    for path in lib.grids():
        if only and only not in path.name:
            continue
        found = pairs_for(path, intra=intra, with_scenario=with_scenario)
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
    for name, n_inter, n_intra in sorted(per_grid, key=lambda x: -x[1]):
        if n_inter or (intra and n_intra):
            suffix = f"  (+{n_intra} intra)" if intra else ""
            print(f"  {n_inter:4d}{suffix}  {name}")
    print("\n--- paires inter-blocs par couple de blocs ---")
    for (b1, b2), n in by_pair.most_common():
        print(f"  {n:4d}  {b1} <-> {b2}")
    scope = "scenario INCLUS" if with_scenario else "scenario exclu"
    print(f"\nTOTAL : {grand} paire(s) quasi identiques  ({scope})")
    if intra:
        print(f"TOTAL INTRA-BLOC : {grand_intra} paire(s) — mesure additionnelle, "
              f"hors du chiffre de reference du projet")


if __name__ == "__main__":
    main()
