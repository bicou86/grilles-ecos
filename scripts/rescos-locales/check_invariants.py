"""Compare l'etat courant au snapshot rescos-locales. Sortie 1 si divergence."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib
from snapshot_invariants import snapshot_one

BASE = Path(__file__).parent / "baseline.json"

# Champs dont toute variation est une regression.
#
# `sectionCounts` (sectionInfo[].count) : le champ qui rendait le bareme
# d'AMBOSS-9 inatteignable sans qu'aucun controle puisse le voir. Le geler
# interdit toute derive ; verifier qu'il est *juste* est le role distinct de
# `check_reachability.py`, qui ne compare a aucun passe.
# `coef` : le champ qui a produit le defaut de RESCOS-12/13 et celui de
# RESCOS-63 ici. `check_reachability.py` ne rattrape que les valeurs qui CASSENT
# la somme a 100 % — une redistribution qui la conserve (`0.5 / 0.25 / 0.25`)
# passerait sans bruit. Le geler ferme ce trou.
# `engineFingerprint` : les 156 moteurs embarques. Voir snapshot_invariants.py.
# `configForm` : une grille qui passerait d'une forme de declaration a l'autre
# changerait de branche de lecture sans qu'aucun autre champ ne bouge.
# `blocks` porte ici le NOMBRE de segments par bloc, pas seulement leur nom.
FROZEN = ["maxScores", "coef", "scoreSpans", "sectionCounts", "sectionPrefixes",
          "engineFingerprint", "configForm", "blocks", "criteriaCount",
          "detailCount", "radioCount", "checkboxCount"]

# Champs qui doivent rester VIDES quoi qu'il arrive — ils ne sont pas compares
# au passe mais a zero. Un bloc dont la fin equilibree ne tombe plus sur la
# queue attendue, ou une classe de contenu apparue hors de tout bloc, est un
# bloc que l'outillage ne voit plus : exactement l'angle mort d'AMBOSS-34.
MUST_BE_EMPTY = ["boundsAnomalies", "uncoveredContent"]


def main():
    baseline = json.loads(BASE.read_text(encoding="utf-8"))
    seen, problems = set(), []
    for path in lib.grids():
        seen.add(path.name)
        want = baseline.get(path.name)
        if want is None:
            problems.append(f"{path.name}: absent du snapshot")
            continue
        got = snapshot_one(path)
        for field in FROZEN:
            if got[field] != want[field]:
                problems.append(
                    f"{path.name}: {field} a change\n"
                    f"    attendu : {want[field]}\n"
                    f"    obtenu  : {got[field]}")
        for field in MUST_BE_EMPTY:
            if got[field]:
                problems.append(
                    f"{path.name}: {field} non vide — bloc devenu invisible ?\n"
                    f"    {got[field]}")
    # Une grille RETIREE du disque doit crier aussi fort qu'une grille modifiee.
    for name in sorted(set(baseline) - seen):
        problems.append(f"{name}: presente au snapshot, absente du disque")
    if problems:
        print(f"ECHEC — {len(problems)} invariant(s) rompu(s) :\n")
        for p in problems:
            print("  " + p)
        return 1
    print(f"OK — {len(baseline)} grilles, tous les invariants preserves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
