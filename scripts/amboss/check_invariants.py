"""Compare l'etat courant au snapshot. Sortie 1 si divergence."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib
from snapshot_invariants import snapshot_one

BASE = Path(__file__).parent / "baseline.json"

# Champs dont toute variation est une regression.
# `sectionCounts` (sectionInfo[].count) a ete ajoute apres coup : c'est le champ
# qui rendait le bareme d'AMBOSS-9 inatteignable sans qu'aucun controle puisse
# le voir. Le geler interdit toute derive ; verifier qu'il est *juste* — que le
# bareme declare est bien atteignable par le calcul — est le role distinct de
# `check_reachability.py`, qui ne compare a aucun passe.
FROZEN = ["maxScores", "scoreSpans", "sectionCounts", "blocks",
          "criteriaCount", "detailCount", "radioCount", "checkboxCount"]


def main():
    baseline = json.loads(BASE.read_text(encoding="utf-8"))
    problems = []
    for path in lib.grids():
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
    if problems:
        print(f"ECHEC — {len(problems)} invariant(s) rompu(s) :\n")
        for p in problems:
            print("  " + p)
        return 1
    print(f"OK — {len(baseline)} grilles, tous les invariants preserves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
