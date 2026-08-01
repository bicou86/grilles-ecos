"""Capture l'état de référence des 40 grilles dans baseline.json."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

OUT = Path(__file__).parent / "baseline.json"


def section_counts(html):
    """`sectionInfo[].count` par section — le nombre de criteres que le calcul itere.

    Champ longtemps absent du snapshot, et c'est precisement lui qui rendait le
    bareme d'AMBOSS-9 inatteignable : `count: 13` pour douze criteres presents,
    donc quatre points impossibles a obtenir. Aucun autre champ ne le refletait —
    `criteriaCount` compte les libelles presents dans la page, jamais ceux que
    `calculateScores()` va chercher — si bien que l'ecart n'apparaissait dans
    aucun diff de baseline. Le figer ici empeche toute derive future ; verifier
    qu'il est *juste* reste le role de `check_reachability.py`.
    """
    m = re.search(r"sectionInfo:\s*\[(.*?)\]", html, re.S)
    counts = {}
    for blob in re.findall(r"\{[^{}]*\}", m.group(1) if m else ""):
        key = re.search(r'key:\s*"(\w+)"', blob)
        count = re.search(r"count:\s*(\d+)", blob)
        if key and count:
            counts[key.group(1)] = int(count.group(1))
    return counts


def snapshot_one(path):
    html = path.read_text(encoding="utf-8")
    m = re.search(r"maxScores:\s*\{([^}]*)\}", html)
    max_scores = {}
    if m:
        for k, v in re.findall(r"(\w+):\s*(\d+)", m.group(1)):
            max_scores[k] = int(v)
    spans = dict(re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html))
    return {
        "maxScores": max_scores,
        "scoreSpans": {k: int(v) for k, v in spans.items()},
        "sectionCounts": section_counts(html),
        "blocks": lib.blocks_present(html),
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
