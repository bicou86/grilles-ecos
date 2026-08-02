"""Verifie que le bareme declare est ATTEIGNABLE par le calcul. Sortie 1 si ecart.

Usage :
    python3 scripts/casecos/check_reachability.py [GRILLE_FILTRE]

Exemples :
    python3 scripts/casecos/check_reachability.py             # les 198 grilles
    python3 scripts/casecos/check_reachability.py Migraine    # detail d'une grille

La simulation elle-meme (`section_max`, `orphan_criteria`, `check_one`) est
importee de `scripts/amboss/check_reachability.py`, sans copie : elle rejoue
`cases/scoring.js` et ne depend d'aucune particularite de corpus. Seules
l'enumeration des grilles, la LECTURE DE LA CONFIGURATION et les deux controles
propres a ce corpus (`empty_weighted_sections`, `engine_defects`) sont ici.

LE BAREME A ETE EMBARQUE, IL NE L'EST PLUS
------------------------------------------
Les 198 grilles n'avaient a l'origine ni `window.caseConfig` ni
`<script src="../scoring.js">` : chacune embarquait sa PROPRE copie complete du
moteur, ou la configuration etait un litteral local au corps de
`calculateScores()` :

    maxScores = {anamnese: 37, examen: 15, management: 14, communication: 20};
    coef = {anamnese: 0.25, examen: 0.25, management: 0.25, communication: 0.25};
    sectionInfo = [
        {key: "anamnese", prefix: "a", count: 8, label: "Anamnèse"},
        {key: "examen", prefix: "e", count: 4, label: "Examen clinique",
         scoreId: "statusScore"},
        ...
    ];

Ces litteraux sont PRECEDES d'une declaration vide (`let maxScores = {};`) que
`parse_config` doit ignorer — voir `snapshot_invariants._first_non_empty`.

`migrate_to_shared_engine.py` les a basculees vers `window.caseConfig` +
`cases/scoring.js`. `parse_config` lit les DEUX formes, la declarative d'abord :
une grille qui reviendrait a la forme embarquee doit rester lisible.

LES 198 COPIES ETAIENT SAINES, ET IDENTIQUES ENTRE ELLES
--------------------------------------------------------
C'est ce qui a rendu la bascule mecaniquement sure. Mesure d'alors : les 198
blocs `<script>` porteurs de `calculateScores()`, nombres et chaines neutralises,
rendaient UNE SEULE empreinte. Il n'y avait pas 198 moteurs mais un seul,
recopie 198 fois.

Ce moteur unique etait `cases/scoring.js` AMPUTE de six ajouts posterieurs :
chargement de `srs.js`, indirection `window.caseConfig`, gardes de nullite sur
`#missingItems` / `#missingList`, mode circuit, `createNavBar()` et
`saveToRegistry()`. Le CALCUL lui-meme — traitement des cases de detail, repli
sur les radios, table communication A=4..E=0, ponderation par `coef`,
`max > 0 ? (score/max)*100 : 0` — etait identique au caractere pres : la bascule
ne change donc aucune note, elle rebranche ce qui manquait autour du calcul.

Le moteur partage ne peut pas lever de `TypeError` sur ce corpus : les
deferencements DOM non gardes qu'il porte encore (`#totalScore` et les six du
minuteur — `#timerContainer`, `#timerStatus`, `#timerDisplay`, `#startBtn`,
`#stopBtn`, `#resetBtn`) sont presents dans les 198 grilles. `engine_defects()`
le reverifie a chaque passage, contre le moteur que chaque grille execute
REELLEMENT, plutot que de s'en remettre a la mesure d'un jour.

Le moteur EMBARQUE, lui, en levait une — sur les 198, a chaque recalcul. Il
deferencait `#missingItems` et `#missingList` sans garde, et ces deux
identifiants n'existent que dans un COMMENTAIRE HTML (« ELEMENTS MANQUANTS
(MASQUES) »). La premiere redaction de ce controle cherchait `id="..."` dans le
HTML BRUT : elle les trouvait dans le commentaire et rendait la porte verte.
Voir `live_dom()`. Le rebranchement sur `cases/scoring.js`, qui garde les deux,
supprime le defaut ; la neutralisation des commentaires supprime l'angle mort.

POURQUOI CE CONTROLE EST DISTINCT DE check_invariants.py
--------------------------------------------------------
`check_invariants.py` compare l'etat courant a un snapshot : il repond a « le
bareme est-il le meme qu'hier ? », jamais a « le bareme est-il juste ? ». Un
bareme faux depuis l'origine reste vert indefiniment — c'est ce qui s'est
produit sur AMBOSS-9, dont le defaut, present des le commit initial, n'a ete vu
qu'apres quinze taches.

Ce script ne compare rien a un passe : il simule le remplissage complet et
exige que le total tombe sur `maxScores[key]` ET sur le denominateur affiche au
candidat, et que le pourcentage global fasse 100 %.

QUATRE ECARTS CHERCHES, plus un cinquieme propre a ce corpus :

  * `count` trop grand — un critere promis par `count` mais absent de la page
    rapporte 0 (AMBOSS-9). Signale « ABSENT » ;
  * sous-item ORPHELIN — un critere hors de la sequence `prefix1..prefixN`,
    cochable a l'ecran mais jamais compte (`a12b`, AMBOSS-9) ;
  * `maxScores` et le `<span>` affiche qui divergent ;
  * section DECLAREE VIDE mais conservant son COEFFICIENT (RESCOS-12 et
    RESCOS-13) : son pourcentage vaut 0 quoi que fasse le candidat et sa part
    est perdue pour tout le monde. `empty_weighted_sections()` la nomme ;
  * moteur embarque INCALCULABLE — un deferencement DOM non garde vers un
    element que la grille ne porte pas (RESCOS-7 et RESCOS-9, `TypeError` a
    chaque clic). `engine_defects()` le cherche.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_casecos as lib
import snapshot_invariants as snap
from snapshot_invariants import engine_source

_amboss = lib.amboss_module("check_reachability")
section_max = _amboss.section_max
orphan_criteria = _amboss.orphan_criteria


def _first_non_empty(html, pattern):
    for m in re.finditer(pattern, html, re.S):
        if m.group(1).strip():
            return m.group(1)
    return ""


def _config_blob(html, declaratif, embarque):
    """Corps du litteral cherche : forme `caseConfig` d'abord, embarquee ensuite."""
    blob = _first_non_empty(html, declaratif)
    return blob if blob else _first_non_empty(html, embarque)


def parse_config(html):
    """maxScores, coef, sectionInfo et denominateurs affiches.

    Les deux formes sont lues : `window.caseConfig` (celle des 198 depuis la
    bascule, et des trois autres corpus) puis le litteral embarque (celle
    d'avant). L'ordre importe — la forme embarquee est precedee d'une
    declaration vide (`let maxScores = {};`) que `_first_non_empty` ecarte.
    Une grille qui reviendrait a la forme embarquee reste donc lue, au lieu de
    rendre un bareme vide qui se confondrait avec « pas de section ».
    """
    max_scores = {k: int(v) for k, v in re.findall(
        r"(\w+):\s*(\d+)", _config_blob(html, r"maxScores:\s*\{([^{}]*)\}",
                                        r"maxScores\s*=\s*\{([^{}]*)\}"))}
    coef = {k: float(v) for k, v in re.findall(
        r"(\w+):\s*([\d.]+)", _config_blob(html, r"coef:\s*\{([^{}]*)\}",
                                           r"coef\s*=\s*\{([^{}]*)\}"))}

    sections = []
    for chunk in re.findall(
            r"\{[^{}]*\}", _config_blob(html, r"sectionInfo:\s*\[(.*?)\]",
                                        r"sectionInfo\s*=\s*\[(.*?)\];")):
        key = re.search(r'key:\s*"(\w+)"', chunk)
        prefix = re.search(r'prefix:\s*"(\w+)"', chunk)
        count = re.search(r"count:\s*(\d+)", chunk)
        if not (key and prefix and count):
            continue
        score_id = re.search(r'scoreId:\s*"(\w+)"', chunk)
        sections.append({
            "key": key.group(1),
            "prefix": prefix.group(1),
            "count": int(count.group(1)),
            # scoreId: section.scoreId || section.key + "Score"
            "scoreId": score_id.group(1) if score_id else key.group(1) + "Score",
            "isComm": re.search(r"isComm:\s*true", chunk) is not None,
        })

    spans = {k: int(v) for k, v in re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html)}
    return max_scores, coef, sections, spans


# `check_one` appelle `parse_config` par son nom global : le remplacer dans le
# module AMBOSS suffit a lui faire lire la forme embarquee, sans en recopier la
# moindre ligne. L'alias du module est propre a casecos (`lib.amboss_module`,
# prefixe `_casecos_amboss_`) afin qu'il ne puisse pas fuir vers German ou
# RESCOS si plusieurs corpus tournaient dans le meme processus.
_amboss.parse_config = parse_config
check_one = _amboss.check_one


def empty_weighted_sections(html):
    """Sections declarees vides mais conservant un coefficient non nul.

    Retourne [(key, coef), ...]. Leur pourcentage vaut 0 quoi qu'il arrive et
    leur part de coefficient est definitivement perdue : c'est la cause exacte
    d'un « global < 100 % » sans aucun ecart de section (RESCOS-12, RESCOS-13).
    """
    max_scores, coef, sections, _ = parse_config(html)
    return [(s["key"], coef.get(s["key"], 0)) for s in sections
            if s["count"] == 0 and not max_scores.get(s["key"])
            and coef.get(s["key"], 0)]


# Deferencement DOM sans garde : `document.getElementById("x").prop`. Si `x`
# n'existe pas dans la page, le premier clic leve une `TypeError` et le score
# n'est jamais calcule — c'etait le defaut des copies perimees de RESCOS-7 et
# RESCOS-9. Ici le moteur est embarque : le controle doit se faire grille par
# grille, contre le DOM de CETTE grille.
_UNGUARDED = re.compile(
    r"document\.getElementById\(\s*['\"]([^'\"]+)['\"]\s*\)\s*\.\s*\w+")

# Un `id=` ecrit dans un COMMENTAIRE HTML n'est pas dans le DOM.
#
# C'est le piege qui a fait manquer, a la premiere redaction de ce controle, un
# defaut present sur les 198 grilles : le bloc
#
#     <!-- ELEMENTS MANQUANTS (MASQUES) -->
#     <!-- <div class="missing-items" id="missingItems" ...>
#              <div id="missingList"></div>
#          </div> -->
#
# porte les deux identifiants QUE le moteur embarque deferencait sans garde. La
# recherche se faisait sur le HTML brut : elle trouvait `id="missingItems"`,
# concluait « present dans les 198 » et rendait la porte verte. Le navigateur,
# lui, levait une `TypeError` a CHAQUE recalcul de score, sur les 198 grilles —
# exactement le defaut de RESCOS-7 et RESCOS-9 que ce controle existe pour
# attraper.
#
# Les commentaires sont donc neutralises avant toute recherche d'identifiant.
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)


def live_dom(html):
    """HTML prive de ses commentaires — ce que le navigateur construit vraiment."""
    return _HTML_COMMENT.sub(" ", html)


SHARED_ENGINE = Path(__file__).resolve().parents[2] / "cases" / "scoring.js"


def engine_defects(html):
    """Defauts rendant le moteur de la grille incalculable. Liste vide si sain.

    Le moteur controle est celui que la grille EXECUTE reellement : le
    `cases/scoring.js` partage si elle le charge, sinon sa copie embarquee. Le
    controle reste grille par grille dans les deux cas — c'est le DOM de CETTE
    grille qui decide si un deferencement est sur, et deux grilles chargeant le
    meme moteur peuvent parfaitement diverger sur ce point.

    Trois causes possibles :
      * ni balise `../scoring.js`, ni bloc `<script>` portant
        `calculateScores()` — la grille n'a aucun moteur ;
      * un identifiant deference sans garde et absent du DOM de la grille ;
      * la grille charge `../scoring.js` mais le fichier est introuvable.
    """
    if snap.loads_shared_engine(html):
        if not SHARED_ENGINE.exists():
            return [f"charge {SHARED_ENGINE.name} mais le fichier est introuvable"]
        src = SHARED_ENGINE.read_text(encoding="utf-8")
    else:
        src = engine_source(html)
        if src is None:
            return ["moteur introuvable : ni <script src=\"../scoring.js\">, "
                    "ni <script> definissant calculateScores()"]
    dom = live_dom(html)
    missing = sorted({i for i in _UNGUARDED.findall(src)
                      if not re.search(r'id=["\']' + re.escape(i) + r'["\']', dom)})
    return [f"deferencement non garde vers #{i}, absent du DOM — TypeError au "
            f"premier calcul" for i in missing]


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    checked, bad = 0, 0
    for path in lib.grids():
        if not lib.matches(path, only):
            continue
        checked += 1
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        ok, lines = check_one(path)

        defects = engine_defects(html)
        if defects:
            ok = False
            lines += ["    " + d for d in defects]
        if not ok:
            bad += 1
            for key, c in empty_weighted_sections(html):
                lines.append(
                    f"    section VIDE mais PONDEREE : {key} (count=0, maxScores=0) "
                    f"garde coef={c} — {round(c * 100)} % du score global sont "
                    f"inatteignables par construction")
        if not ok or only:
            print(f'{path.name}  {"OK" if ok else "ECART"}')
            print("\n".join(lines))

    if only and checked == 0:
        print(f"Aucune grille ne correspond au filtre {only!r}.")
        return 1
    if bad:
        print(f"\nECHEC — {bad} grille(s) sur {checked} au bareme inatteignable "
              f"ou incalculable")
        return 1
    print(f"\nOK — {checked} grille(s), bareme atteignable a 100 % sur chaque "
          f"section et moteur calculable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
