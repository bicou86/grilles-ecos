"""Capture l'etat de reference des 198 grilles CasECOS dans baseline.json.

DEUX FORMES DE DECLARATION DU BAREME, ET LA BASCULE DE L'UNE A L'AUTRE
----------------------------------------------------------------------
AMBOSS, German et RESCOS declarent leur bareme dans un `window.caseConfig`
(forme DECLARATIVE) que le `cases/scoring.js` partage vient lire.

Les 198 grilles CasECOS employaient a l'origine une forme qu'aucun autre corpus
ne portait : ni `window.caseConfig` (0/198) ni `<script src="../scoring.js">`
(0/198). Chacune embarquait sa propre copie complete du moteur, ou la
configuration etait un LITTERAL LOCAL au corps de `calculateScores()` :

    let maxScores = {};                                   <- declaration vide
    ...
    maxScores = {anamnese: 37, examen: 15, ...};          <- affectation reelle
    coef = {anamnese: 0.25, ...};
    sectionInfo = [
        {key: "anamnese", prefix: "a", count: 8, label: "Anamnèse"},
        ...
    ];

Les lecteurs de cette forme ignorent la PREMIERE affectation (`{}` et `[]`,
vides) et retiennent la premiere NON VIDE. Un motif `maxScores\\s*=\\s*\\{([^}]*)\\}`
naif rendrait la declaration vide et le snapshot serait uniformement nul.

Les 198 ont depuis bascule vers `window.caseConfig` + `cases/scoring.js`
(`migrate_to_shared_engine.py`). Les lecteurs essaient donc la forme
DECLARATIVE d'abord et retombent sur la forme embarquee — celle-ci reste lue,
et non supprimee, pour que le jour ou une grille reviendrait en arriere le
snapshot le dise au lieu de rendre un bareme vide.

LE MOTEUR EST GELE, EMBARQUE OU PARTAGE
---------------------------------------
Quand le bareme n'est pas seulement declare mais aussi CALCULE dans le fichier,
`engineHash` capte l'empreinte du bloc `<script>` qui porte `calculateScores()`,
NOMBRES ET CHAINES NEUTRALISES. Sans neutralisation chaque grille aurait une
empreinte unique (elle porte son propre bareme) et le champ ne dirait rien ;
avec elle, les 198 grilles rendaient UNE SEULE valeur — un moteur unique,
recopie 198 fois.

Depuis la bascule, le champ vaut `"shared:scoring.js"` : il n'y a plus de moteur
embarque a geler. Le champ garde sa fonction, et meme sa fonction d'origine —
c'etait, selon les termes de sa premiere redaction, « le pendant, pour un moteur
embarque, de ce qu'un `git diff` sur `cases/scoring.js` faisait deja pour un
moteur partage ». Le moteur etant redevenu partage, c'est `git diff` qui le
couvre, et `check_reachability.py` qui re-verifie a chaque passage que ce moteur
partage est calculable contre le DOM de chaque grille. Toute grille qui
re-embarquerait un moteur rendrait de nouveau une empreinte, et le champ le
signalerait des le premier passage.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_casecos as lib

OUT = Path(__file__).parent / "baseline.json"

# Bloc `<script>` inline (sans `src=`) — celui qui porte le moteur.
_INLINE_SCRIPT = re.compile(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', re.S)


def engine_source(html):
    """Corps du `<script>` inline qui definit `calculateScores()`, ou None.

    Les 198 grilles portent exactement trois blocs inline : le moteur, un rappel
    de coloration, et la barre de navigation. Un seul contient
    `function calculateScores`.
    """
    blocks = [b for b in _INLINE_SCRIPT.findall(html)
              if "function calculateScores" in b]
    return blocks[0] if len(blocks) == 1 else None


def neutralize(js):
    """Code JavaScript prive de ses commentaires, chaines et nombres.

    C'est ce qui distingue « deux grilles au meme moteur mais au bareme
    different » (attendu, 198 fois) de « deux moteurs differents » (une
    regression). Les chaines sont neutralisees au meme titre que les nombres :
    `label: "Anamnèse"` et `prefix: "a"` sont de la configuration, pas de la
    structure.
    """
    js = re.sub(r"/\*.*?\*/", " ", js, flags=re.S)
    js = re.sub(r"//[^\n]*", " ", js)
    js = re.sub(r'"(?:[^"\\]|\\.)*"', '"S"', js)
    js = re.sub(r"'(?:[^'\\]|\\.)*'", '"S"', js)
    js = re.sub(r"\b\d+(?:\.\d+)?\b", "N", js)
    return re.sub(r"\s+", " ", js).strip()


SHARED_ENGINE_TAG = '<script src="../scoring.js"></script>'


def loads_shared_engine(html):
    """La grille delegue-t-elle son calcul au `cases/scoring.js` partage ?"""
    return SHARED_ENGINE_TAG in html


def engine_hash(html):
    """Identite du moteur de calcul de la grille.

    `"shared:scoring.js"` quand elle charge le moteur partage ; sinon
    l'empreinte structurelle du moteur embarque ; `None` s'il n'y en a aucun —
    cas d'une grille sans moteur du tout, qui est un defaut.
    """
    if loads_shared_engine(html):
        return "shared:scoring.js"
    src = engine_source(html)
    if src is None:
        return None
    return hashlib.sha1(neutralize(src).encode("utf-8")).hexdigest()[:12]


def _first_non_empty(html, pattern):
    """Premier groupe non vide du motif — voir l'entete (`let maxScores = {}`)."""
    for m in re.finditer(pattern, html, re.S):
        if m.group(1).strip():
            return m.group(1)
    return ""


def _config_blob(html, declaratif, embarque):
    """Corps du litteral cherche : forme `caseConfig` d'abord, embarquee ensuite.

    Les deux motifs sont essayes dans cet ordre parce que la forme embarquee
    est celle d'avant la bascule : une grille qui y reviendrait doit rester
    lisible, plutot que de rendre un bareme vide qui passerait pour « pas de
    section » au lieu de « regression ».
    """
    blob = _first_non_empty(html, declaratif)
    return blob if blob else _first_non_empty(html, embarque)


def max_scores(html):
    """`maxScores` par section."""
    blob = _config_blob(html, r"maxScores:\s*\{([^{}]*)\}",
                        r"maxScores\s*=\s*\{([^{}]*)\}")
    return {k: int(v) for k, v in re.findall(r"(\w+):\s*(\d+)", blob)}


def coefs(html):
    """`coef` par section.

    Gele pour la raison qu'a montree RESCOS-12/13 : une section vide gardant son
    quart de coefficient plafonne la note globale a 75 % sans qu'aucun compte de
    criteres, de sous-items ou de cases ne bouge. `check_reachability.py` ne
    rattrape que les valeurs qui CASSENT la somme a 100 % — une redistribution
    qui la conserve (`0.5 / 0.25 / 0.25`) passerait sans bruit.

    Les valeurs sont des flottants : `json` les serialise et les relit au bit
    pres, l'egalite de `check_invariants.py` est donc exacte.
    """
    blob = _config_blob(html, r"coef:\s*\{([^{}]*)\}", r"coef\s*=\s*\{([^{}]*)\}")
    return {k: float(v) for k, v in re.findall(r"(\w+):\s*([\d.]+)", blob)}


def section_counts(html):
    """`sectionInfo[].count` par section.

    C'est ce champ, longtemps hors snapshot, qui rendait le bareme d'AMBOSS-9
    inatteignable sans qu'aucun controle puisse le voir : `calculateScores()`
    itere `prefix1..prefixN`, et un `count` trop grand promet des criteres que
    la page ne porte pas.
    """
    blob = _config_blob(html, r"sectionInfo:\s*\[(.*?)\]",
                        r"sectionInfo\s*=\s*\[(.*?)\];")
    counts = {}
    for chunk in re.findall(r"\{[^{}]*\}", blob):
        key = re.search(r'key:\s*"(\w+)"', chunk)
        count = re.search(r"count:\s*(\d+)", chunk)
        if key and count:
            counts[key.group(1)] = int(count.group(1))
    return counts


def config_form(html):
    """Forme de declaration du bareme — voir l'entete du module."""
    if "window.caseConfig" in html:
        return "caseConfig"
    if re.search(r"sectionInfo\.push\(\{", html):
        return "inline-push"
    if _first_non_empty(html, r"sectionInfo\s*=\s*\[(.*?)\];"):
        return "inline-literal"
    return "aucune"


def saves_to_registry(html):
    """La grille alimente-t-elle `ecos_registry`, que le tableau de bord lit ?

    `saveToRegistry()` n'est defini et appele qu'a UN endroit du depot :
    `cases/scoring.js`. Une grille l'atteint donc de deux facons — en chargeant
    ce fichier, ou en portant elle-meme une copie du moteur assez recente pour
    contenir la fonction. Aucune des 198 n'etait dans le second cas, et la
    bascule les a mises toutes dans le premier.

    Chercher la seule chaine `saveToRegistry` dans le HTML, comme le faisait la
    premiere redaction, rendait `false` AVANT la bascule (moteur embarque
    perime) et `false` APRES (la fonction vit dans un fichier separe) : le champ
    aurait manque le seul changement qu'il existait pour voir.
    """
    return "saveToRegistry" in html or loads_shared_engine(html)


def snapshot_one(path):
    html = path.read_text(encoding="utf-8")
    spans = dict(re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html))
    stripped = lib.strip_base64(html)
    return {
        "maxScores": max_scores(html),
        "coef": coefs(html),
        "scoreSpans": {k: int(v) for k, v in spans.items()},
        "sectionCounts": section_counts(html),
        # Forme de declaration du bareme : "caseConfig" pour les 198 depuis la
        # bascule ("inline-literal" avant). Gele parce qu'une grille qui
        # reviendrait a la forme embarquee changerait de moteur de calcul sans
        # qu'aucun autre champ ne bouge.
        "configForm": config_form(html),
        # Identite du moteur : "shared:scoring.js" depuis la bascule, une
        # empreinte structurelle tant qu'il etait embarque. Voir l'entete.
        "engineHash": engine_hash(stripped),
        # Alimentation du registre central : c'est ce que le tableau de bord
        # (`index.html`) lit pour afficher la pastille de score. Gele a `false`
        # avant la bascule — un DEFAUT constate, non un etat souhaitable — pour
        # que sa correction soit un changement vu et voulu. Il vaut `true`
        # depuis.
        "savesToRegistry": saves_to_registry(html),
        # [nom, nombre de segments] : un bloc peut apparaitre plusieurs fois
        # (jusqu'a 14 `therapy-section` et 9 `cloture-item` par grille). Geler
        # le seul nom laisserait disparaitre un segment sans trace.
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
