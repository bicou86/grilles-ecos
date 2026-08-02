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


def coefs(html):
    """`coef` par section, forme declarative ou imperative.

    Gele pour la meme raison que `sectionCounts`, et sur le defaut qu'a porte
    CE corpus : RESCOS-12 et RESCOS-13 laissaient coef 0.25 a une section vide,
    dont `scoring.js` calcule le pourcentage a 0 (`max > 0 ? ... : 0`) — une
    copie parfaite plafonnait a 75 % sans qu'aucun compte de criteres, de
    sous-items ou de cases ne bouge.

    Le filet existant est INCOMPLET : `check_reachability.py` exige que le
    total tombe sur 100 %, donc il rattrape toute valeur qui casse la SOMME des
    coefficients — mais pas une redistribution qui la conserve. Passer de trois
    tiers egaux a `{0.5, 0.25, 0.25}` changerait la note de toutes les copies
    et resterait vert. Le geler ferme ce trou ; verifier que la valeur est
    *juste* reste le role de `check_reachability.py`.

    Les valeurs sont des flottants : `json` les serialise et les relit au bit
    pres, l'egalite de `check_invariants.py` est donc exacte — y compris pour
    le `0.3333333333333333` de RESCOS-12 et RESCOS-13.
    """
    m = re.search(r"coef:\s*\{([^}]*)\}", html)
    if m:
        return {k: float(v) for k, v in re.findall(r"(\w+):\s*([\d.]+)", m.group(1))}
    return {k: float(v) for k, v in
            re.findall(r'coef\["(\w+)"\]\s*=\s*([\d.]+)', html)}


def snapshot_one(path):
    html = path.read_text(encoding="utf-8")
    spans = dict(re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html))
    stripped = lib.strip_base64(html)
    return {
        "maxScores": max_scores(html),
        # Le champ qui a produit le defaut de RESCOS-12 et RESCOS-13 : une
        # section vide gardant son quart de coefficient. Voir `coefs()`.
        "coef": coefs(html),
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
