"""Liste les paires d'items quasi identiques entre blocs de contenu CasECOS.

Usage :
    python3 scripts/casecos/report_redundancy.py [GRILLE_FILTRE] [--intra]
                                                 [--quiet] [--with-scenario]

Par defaut, seules les paires INTER-BLOCS sont comptees (`if b1 == b2:
continue`) — meme convention, meme seuil (0.72) et meme unite que
`scripts/amboss/report_redundancy.py` (147 paires) et ses homologues German et
RESCOS (127). Le comportement par defaut ne doit pas changer : toute mesure du
projet cesserait d'etre comparable.

`--intra` ajoute les paires INTRA-BLOC. Les deux totaux restent affiches
separement, jamais additionnes.

`--quiet` n'affiche que le tableau par grille et les totaux, sans le detail des
paires — utile pour un releve. Recommande sur ce corpus : le detail complet
depasse le million de lignes.

LE BLOC `scenario` EST EXCLU PAR DEFAUT
---------------------------------------
`annexe-scenario` est le SCRIPT DU PATIENT SIMULE : redire les symptomes deja
listes dans les fiches est sa fonction meme, et l'y apparier compterait comme
redondance ce qui est en realite la coherence exigee du scenario. AMBOSS
l'exclut de fait (son `BLOCKS` ne le contient pas), RESCOS explicitement ;
l'exclure ici garde les quatre corpus dans la meme unite. Le bloc reste dans
`lib.BLOCKS` : il est borne, gele au snapshot, verifie par `bounds_anomalies` et
protege par `check_no_loss`. Ce n'est pas un angle mort, c'est une exclusion
documentee, et `--with-scenario` la leve pour qui veut la mesure elargie.

`annexe-nu` n'est PAS exclu bien qu'il porte aujourd'hui, dans AMC-Psy-P10, un
second scenario (celui de la mere) : la classe est generique et rien ne garantit
qu'une grille future y logera encore un scenario. Ses paires avec `scenario`
sont attendues et se lisent comme telles.

DEUX DIFFERENCES AVEC LES CORPUS PRECEDENTS
--------------------------------------------
1. Un bloc peut apparaitre BEAUCOUP de fois dans une meme grille (jusqu'a 14
   `therapy-section`, 9 `cloture-item`). Les segments d'un meme bloc sont
   concatenes en une seule liste sous le nom du bloc — deux `therapy-section`
   de la meme grille comptent donc comme intra, ce qui est exact : c'est bien
   le meme role editorial.
2. Le decoupage passe par `lib.top_spans()` et non par `lib.block_spans()`.
   Le bloc `exemples` vit 371 fois sur 383 A L'INTERIEUR d'un `cloture-item` ;
   sans ce passage, ses 1514 phrases modeles seraient comptees deux fois — une
   fois sous `exemples`, une fois sous `cloture` — et chaque doublon serait
   rapporte en double.
"""
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_casecos as lib

THRESHOLD = 0.72  # identique a AMBOSS, German et RESCOS — meme mesure.


def pairs_for(path, intra=False, with_scenario=False):
    html = lib.strip_base64(path.read_text(encoding="utf-8"))
    excluded = set() if with_scenario else lib.REDUNDANCY_EXCLUDED
    items = [(name, t)
             for a, b, name in lib.top_spans(html, excluded=excluded)
             for t in lib.list_items(html[a:b])]
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
        if not lib.matches(path, only):
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
    for name, n_inter, n_intra in sorted(per_grid, key=lambda r: -r[1]):
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
