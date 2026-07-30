"""Capture l'état de référence des 40 grilles dans baseline.json."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

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
    return {
        "maxScores": max_scores,
        "scoreSpans": {k: int(v) for k, v in spans.items()},
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
