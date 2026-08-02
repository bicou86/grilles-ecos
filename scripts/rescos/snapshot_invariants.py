"""Capture l'etat de reference des 41 grilles RESCOS dans baseline.json."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos as lib

# `section_counts` ne depend d'aucune particularite de corpus : il lit
# `window.caseConfig.sectionInfo`, dont les 39 grilles RESCOS qui portent un
# `caseConfig` ont exactement la meme forme que les 40 grilles AMBOSS.
# Reutilise tel quel.
_section_counts_caseconfig = lib.amboss_module("snapshot_invariants").section_counts

OUT = Path(__file__).parent / "baseline.json"

# Forme IMPERATIVE du barème, propre a RESCOS-7 et RESCOS-9 : ces deux grilles
# n'ont pas de `window.caseConfig` et embarquent a la place leur PROPRE copie
# de `calculateScores()`, ou la configuration est construite ligne a ligne
# (`maxScores["anamnese"] = 41;` puis `sectionInfo.push({...})`). La logique de
# calcul y est identique au `cases/scoring.js` partage, au caractere pres :
# seule la maniere de declarer la configuration change. Sans ce second lecteur,
# `sectionCounts` serait vide pour ces deux grilles et le champ le plus
# sensible du snapshot — celui qui rendait AMBOSS-9 faux — ne serait pas gele.
_PUSH = re.compile(r"sectionInfo\.push\(\{([^}]*)\}\)")


def section_counts(html):
    """`sectionInfo[].count` par section, quelle que soit la forme de declaration."""
    counts = _section_counts_caseconfig(html)
    if counts:
        return counts
    for blob in _PUSH.findall(html):
        key = re.search(r'key:\s*"(\w+)"', blob)
        count = re.search(r"count:\s*(\d+)", blob)
        if key and count:
            counts[key.group(1)] = int(count.group(1))
    return counts


def max_scores(html):
    """`maxScores` par section, forme declarative ou imperative."""
    m = re.search(r"maxScores:\s*\{([^}]*)\}", html)
    if m:
        return {k: int(v) for k, v in re.findall(r"(\w+):\s*(\d+)", m.group(1))}
    return {k: int(v) for k, v in
            re.findall(r'maxScores\["(\w+)"\]\s*=\s*(\d+)', html)}


def snapshot_one(path):
    html = path.read_text(encoding="utf-8")
    spans = dict(re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html))
    stripped = lib.strip_base64(html)
    return {
        "maxScores": max_scores(html),
        "scoreSpans": {k: int(v) for k, v in spans.items()},
        # `sectionInfo[].count` — le nombre de criteres que le calcul itere.
        # C'est ce champ, longtemps hors snapshot, qui rendait le bareme
        # d'AMBOSS-9 inatteignable sans qu'aucun controle puisse le voir.
        "sectionCounts": section_counts(html),
        # Forme de declaration du bareme : "caseConfig" (39 grilles) ou
        # "inline" (RESCOS-7 et RESCOS-9). Gele parce qu'une grille qui
        # basculerait d'une forme a l'autre changerait de moteur de calcul.
        "configForm": "caseConfig" if "window.caseConfig" in html else (
            "inline" if _PUSH.search(html) else "aucune"),
        # [nom, nombre de segments] : un bloc peut apparaitre plusieurs fois
        # (jusqu'a 4 `therapy-section` et 4 `cloture-item` par grille). Geler le
        # seul nom laisserait disparaitre un segment sans trace.
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
