"""Capture l'etat de reference des 88 grilles German dans baseline.json."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_german as lib

# `section_counts` ne depend d'aucune particularite de corpus : il lit
# `window.caseConfig.sectionInfo`, dont les 88 grilles German portent
# exactement la meme forme que les 40 grilles AMBOSS. Reutilise tel quel.
section_counts = lib.amboss_module("snapshot_invariants").section_counts

OUT = Path(__file__).parent / "baseline.json"


def snapshot_one(path):
    html = path.read_text(encoding="utf-8")
    m = re.search(r"maxScores:\s*\{([^}]*)\}", html)
    max_scores = {}
    if m:
        for k, v in re.findall(r"(\w+):\s*(\d+)", m.group(1)):
            max_scores[k] = int(v)
    spans = dict(re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html))
    stripped = lib.strip_base64(html)
    return {
        "maxScores": max_scores,
        "scoreSpans": {k: int(v) for k, v in spans.items()},
        # `sectionInfo[].count` — le nombre de criteres que le calcul itere.
        # C'est ce champ, longtemps hors snapshot, qui rendait le bareme
        # d'AMBOSS-9 inatteignable sans qu'aucun controle puisse le voir.
        "sectionCounts": section_counts(html),
        # [nom, nombre de segments] : un bloc peut apparaitre plusieurs fois
        # (German-78 porte deux `annexe-dd`, 44 grilles portent 2 a 3
        # `therapy-section`). Geler le seul nom laisserait disparaitre un
        # segment sans trace.
        "blocks": lib.blocks_present(stripped),
        # Filet contre l'angle mort d'AMBOSS-34 : une fiche portee par une
        # classe non prevue serait invisible a tout le reste de l'outillage et
        # n'aurait pour symptome qu'un chiffre de redondance anormalement bas.
        # Ces deux champs doivent rester vides ; `check_invariants.py` le
        # verifie a chaque passage.
        "boundsAnomalies": lib.bounds_anomalies(stripped),
        "uncoveredContent": lib.uncovered_content(stripped),
        "criteriaCount": len(re.findall(r'class="criteria-text"', html)),
        "detailCount": len(re.findall(r'class="detail-text criteria-detail"', html)),
        "radioCount": len(re.findall(r'<input type="radio"', html)),
        "checkboxCount": len(re.findall(r'<input type="checkbox"', html)),
    }


def main():
    data = {p.name: snapshot_one(p) for p in lib.grids()}
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Snapshot de {len(data)} grilles ecrit dans {OUT.name}")


if __name__ == "__main__":
    main()
