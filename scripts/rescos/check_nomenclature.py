"""Detecte les termes non suisses dans les 41 grilles RESCOS. Sortie 1 si presents.

La table BANNED est celle de `scripts/amboss/check_nomenclature.py`, importee
et non recopiee. Elle ne decrit pas un corpus mais un referentiel — la
nomenclature de laboratoire et les usages suisses — et chacune de ses entrees
porte un commentaire acquis a l'usage : pourquoi `mg/mL` ne doit JAMAIS y
figurer (PC20 de la methacholine), pourquoi `CBC`/`BMP` sont tolerees en
position de cle de glossaire, pourquoi `/µL` n'est banni que precede d'un terme
d'hemogramme (une numeration de LCR se rend bien en /µL). Une seconde copie
divergerait au premier ajout.

Releve initial sur RESCOS (etat au moment du portage) : 111 termes sur 28
grilles — 104 `NFS`, 4 `mg/dL`, 2 `g/dL`, 1 `/mm³`. Aucun `ng/mL`, `pg/mL`,
`/µL`, `911`, `SAMU`, ni nom de marque americaine.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos as lib

BANNED = lib.amboss_module("check_nomenclature").BANNED


def main():
    total = 0
    for path in lib.grids():
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        for pattern, repl in BANNED.items():
            hits = re.findall(pattern, html)
            if hits:
                total += len(hits)
                print(f"  {path.name}: {len(hits)}x {pattern} -> attendu {repl}")
    if total:
        print(f"\nECHEC — {total} terme(s) non suisse(s) restant(s)")
        return 1
    print("OK — aucun terme non suisse detecte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
