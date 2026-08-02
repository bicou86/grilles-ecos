"""Capture l'etat de reference des 165 grilles rescos-locales dans baseline.json.

CE QUE CE SNAPSHOT AJOUTE AUX TROIS PRECEDENTS : `engineFingerprint`
=====================================================================
Les trois corpus precedents partageaient `cases/scoring.js` : un seul fichier,
suivi par `git` comme n'importe quel autre, dont toute modification apparait au
`diff`. Ici, chacune des 156 grilles notees embarque sa propre copie du moteur —
35 800 caracteres de JavaScript noyes dans un fichier de 170 000. Une
modification d'un de ces 156 moteurs ne se distinguerait, dans un `diff` de
grille, d'aucune retouche de contenu.

`engineFingerprint` est le SHA-256 de ce moteur, region de configuration
masquee. Il gele la LOGIQUE de calcul independamment des chiffres du bareme, qui
sont geles a part (`maxScores`, `coef`, `sectionCounts`). Les 156 grilles
portent aujourd'hui la MEME empreinte ; une divergence future, qu'elle vienne
d'une correction appliquee a une seule grille ou d'un import de gabarit
different, est signalee par `check_invariants.py` — et separement rejetee par
`check_reachability.py`, dont c'est une precondition.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib
from check_reachability import (_CFG_END, _CFG_START, engine_fingerprint,
                                engine_source, is_door_sheet, parse_config)

OUT = Path(__file__).parent / "baseline.json"


def config_form(html):
    """Forme de declaration du bareme, gelee parce qu'elle designe le lecteur.

    `declarative` : `maxScores = {…}` / `sectionInfo = [{…}]` — 154 grilles.
    `imperative`  : `maxScores["x"] = …` / `sectionInfo.push({…})` — 2 grilles.
    `feuille-porte` : aucun bareme, par nature.
    `aucune` : ni l'un ni l'autre — anomalie.

    Une grille qui basculerait d'une forme a l'autre changerait de branche de
    lecture dans `parse_config` sans qu'aucun autre champ ne bouge.

    La lecture est BORNEE a la region de configuration : hors d'elle, les 156
    moteurs portent tous la declaration `let maxScores = {};`, qu'un
    `re.search(r"maxScores\\s*=\\s*\\{")` sur tout le script prendrait pour la
    forme declarative — et les deux grilles imperatives seraient classees a
    tort avec les 154 autres.
    """
    if is_door_sheet(html):
        return "feuille-porte"
    js = engine_source(html)
    a = js.find(_CFG_START)
    b = js.find(_CFG_END, a) if a >= 0 else -1
    cfg = js[a:b] if a >= 0 and b > 0 else ""
    if re.search(r"maxScores\s*=\s*\{", cfg):
        return "declarative"
    if re.search(r'maxScores\["\w+"\]\s*=', cfg):
        return "imperative"
    return "aucune"


def snapshot_one(path):
    html = path.read_text(encoding="utf-8")
    stripped = lib.strip_base64(html)
    max_scores, coef, sections, spans = parse_config(stripped)
    return {
        "maxScores": max_scores,
        # Le champ qui a produit le defaut de RESCOS-12 et RESCOS-13 (section
        # vide gardant son quart) et celui de RESCOS-63 ici (somme = 0,5). Il
        # gouverne la note globale sans etre reflete par aucun autre.
        "coef": coef,
        "scoreSpans": spans,
        # `sectionInfo[].count` — le nombre de criteres que le calcul itere.
        # C'est ce champ, longtemps hors snapshot, qui rendait le bareme
        # d'AMBOSS-9 inatteignable sans qu'aucun controle puisse le voir.
        "sectionCounts": {s["key"]: s["count"] for s in sections},
        "sectionPrefixes": {s["key"]: s["prefix"] for s in sections},
        # Voir l'entete : le seul moyen de suivre 156 moteurs embarques.
        "engineFingerprint": engine_fingerprint(stripped),
        "configForm": config_form(stripped),
        # [nom, nombre de segments] : un bloc peut apparaitre plusieurs fois
        # (jusqu'a 8 `therapy-section` et 8 `cloture-item` par grille). Geler le
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
