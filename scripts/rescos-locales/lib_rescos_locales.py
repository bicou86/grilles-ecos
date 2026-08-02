"""Fonctions partagees pour le traitement des grilles de `cases/rescos-locales`.

ARCHITECTURE — ce qui est importe, ce qui est redefini
------------------------------------------------------
Meme partage que `scripts/german/lib_german.py` et `scripts/rescos/lib_rescos.py`,
pour la meme raison. Les primitives de TEXTE viennent de
`scripts/amboss/lib_amboss.py`, chargees par chemin explicite : `strip_base64`,
`visible_text`, `norm`, `BULLET`, `_bullet_items`. Elles ne dependent d'aucune
particularite de corpus — elles nettoient du HTML et normalisent du francais — et
chacune porte un correctif durement acquis :

  * `visible_text` ne consomme pas le CHEVRON NU d'un seuil (`Hb < 70 g/L`) ;
  * `strip_base64` neutralise les data-URI avant tout controle — ce corpus pese
    27,9 Mo brut pour 27,1 Mo hors data-URI, la difference est faible mais le
    principe reste : jamais de `grep` brut pour un controle ;
  * `_bullet_items` traite la puce « • » comme un separateur.

Sont egalement importees de `scripts/amboss/` la table `BANNED`
(`check_nomenclature`) et la simulation du moteur de calcul
(`check_reachability`) — voir les scripts concernes.

Ce qui DECRIT le corpus est redefini ici, et rien n'est ecrit dans
`scripts/amboss/`, `scripts/german/` ni `scripts/rescos/` : `CASES`, `BLOCKS`,
`CONTENT_CLASSES`, `grids()`, `grid_key()`, les bornes (`_balanced_end`,
`block_spans`, `peda_bounds`, `dd_bounds`, `bounds_anomalies`,
`uncovered_content`) et `list_items()`. Les mesures publiees des corpus
precedents (AMBOSS 147 paires inter-blocs, RESCOS 127) sont inchangees par
construction — verifie par comparaison de sorties avant/apres.

`_balanced_end` est RECOPIE plutot qu'importe de `lib_rescos`, pour la raison
exposee dans l'entete de ce dernier : quinze lignes de syntaxe pure, sans
correctif acquis, dont une divergence eventuelle se manifesterait immediatement
par `bounds_anomalies()`. Importer ferait de rescos une dependance de
rescos-locales et transformerait l'etoile (amboss = racine) en chaine.

CE QUE CE CORPUS A DE RADICALEMENT DIFFERENT : LES GRILLES SONT AUTONOMES
=========================================================================
Mesure sur les 165 fichiers :

    caseConfig        0/165        <style> en ligne       165/165
    scoring.js        0/165        calculateScores        156/165
    case-styles.css   0/165        maxScores              156/165

Les trois corpus precedents partageaient `cases/scoring.js` — un seul fichier,
dont `check_reachability` simule la logique. Ici il y en a 156, un par grille
notee. Le resultat de leur audit conditionne toute la suite ; il est expose dans
l'entete de `check_reachability.py`, dont c'est le sujet. En resume :

  * les 156 moteurs sont OCTET POUR OCTET IDENTIQUES entre eux hors du bloc de
    configuration — une seule variante, verifiee par empreinte SHA-1 apres
    masquage de la config et de `isNewFormat` ;
  * ils sont une FOURCHE PERIMEE de `cases/scoring.js`, a laquelle manquent
    exactement les six corrections que r7 avait relevees sur RESCOS-7 et
    RESCOS-9 ;
  * ils levent une exception `TypeError` a CHAQUE calcul, dans les 156 grilles,
    parce que le `<div id="missingItems">` qu'ils adressent sans garde est
    commente dans le HTML (156/165). Mesure en navigateur — voir
    `browser_probe.js`.

Les 9 grilles sans `calculateScores` sont les 9 FEUILLES PORTE
(`<div class="feuille-porte">`) : consigne remise au candidat devant la station.
Elles ne portent aucun critere (0 `criteria-row`, 0 `<input>`, 0 `<script>`) et
n'ont donc pas de bareme — ce n'est pas un defaut, c'est leur nature. Elles ont
malgre tout une entree dans `BLOCKS`, faute de quoi leur contenu redactionnel
serait invisible a tout l'outillage.

STRUCTURE DES BLOCS — mesuree sur les 165 grilles
==================================================
Proche d'AMBOSS et de RESCOS. Les trois fiches de fin de page existent
(`expert` 127, `theorie` 138, `scenario` 118), la zone pedagogique s'ouvre sur
`resume`/`annexes`, `annexe-dd` vit dans la section notee, et la section
« Cloture de consultation » inauguree par RESCOS est ici MAJORITAIRE (134/165
grilles, 398 segments, contre 13/41 dans RESCOS).

Deux blocs sont INEDITS, absents des `BLOCKS` des trois corpus precedents :

  * `feuille-porte` — 9 segments sur 9 grilles (voir ci-dessus) ;
  * `annexe-qr` — 1 segment, « Pediatrie — Etat febrile sans foyer ». Fiche
    questions/reponses portee par `<div class="annexe-item annexe-qr">`, logee
    dans `annexes-grid` apres `scenario`. C'est exactement l'angle mort
    d'AMBOSS-34 : une fiche sous une classe non standard, invisible sans entree
    dedidee, dont le seul symptome aurait ete un chiffre de redondance
    anormalement bas sur une grille.

Le corpus est globalement equilibre en `<div>` : 165 grilles sur 165, zero ecart
entre `<div` et `</div>`. C'est ce qui autorise le decoupage par equilibrage.
"""
import importlib.util
import re
import sys
from pathlib import Path

_AMBOSS_DIR = Path(__file__).resolve().parents[1] / "amboss"


def amboss_module(name):
    """Charge un module de `scripts/amboss/` sous un alias `_locales_amboss_<nom>`.

    Chargement par chemin explicite, jamais par `sys.path` : les quatre dossiers
    de corpus portent des scripts de meme nom (`check_nomenclature.py`,
    `check_reachability.py`, ...) et un import ordinaire resoudrait selon
    l'ordre du chemin, donc au hasard.

    L'alias porte un prefixe PROPRE a ce corpus, distinct du `_amboss_<nom>` de
    `lib_german` et du `_rescos_amboss_<nom>` de `lib_rescos`. Sans cela, les
    corpus partageraient la meme instance dans `sys.modules`, et le
    remplacement de `parse_config` opere par `check_reachability.py` fuirait
    vers eux s'ils s'executaient dans le meme processus.
    """
    path = _AMBOSS_DIR / (name + ".py")
    spec = importlib.util.spec_from_file_location("_locales_amboss_" + name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sys.path.append(str(_AMBOSS_DIR))
import lib_amboss as _base  # noqa: E402

# Primitives de texte partagees — implementation unique, voir l'entete.
strip_base64 = _base.strip_base64
visible_text = _base.visible_text
norm = _base.norm
BULLET = _base.BULLET
_bullet_items = _base._bullet_items

CASES = Path(__file__).resolve().parents[2] / "cases" / "rescos-locales"

# Marqueur de fin de la zone pedagogique. Present dans les 156 grilles notees,
# une seule fois par grille, et toujours apres le dernier bloc de contenu.
# ABSENT des 9 feuilles porte, qui n'ont pas de zone pedagogique.
END_MARK = "<!-- COMMENTAIRE GÉNÉRAL -->"

# Marqueur de fin de la section « Cloture de consultation », present dans les
# 154 grilles qui portent une section Communication — donc dans les 134 qui
# portent une cloture.
COMM_MARK = "<!-- COMMUNICATION -->"

# Marqueur d'ouverture de la section « Cloture de consultation ». Sert de queue
# a l'`annexe-dd` d'une grille (« Fatigue — Vignettes cliniques »), seule du
# corpus a placer ce bloc en DERNIER critere de sa section notee : il n'y a
# alors aucun `criteria-row` derriere lui, et sans cette alternative
# `bounds_anomalies()` crierait sur une grille parfaitement saine.
CLOTURE_MARK = "<!-- CLÔTURE -->"

# Bornes des blocs de contenu, dans leur ordre d'apparition dans le fichier.
#
# Chaque entree est (nom, motif de debut, queue attendue). Le decoupage reel se
# fait par EQUILIBRAGE des `<div>` (`_balanced_end`), pas par le motif de fin :
# les 165 grilles sont globalement equilibrees (verifie : 0 ecart entre `<div`
# et `</div>`), et l'equilibrage ne peut pas se tromper de borne quand un bloc
# en contient un autre. La « queue attendue » est ce qui doit suivre
# immediatement la fin equilibree ; `bounds_anomalies()` le verifie sur tout le
# corpus et `check_invariants.py` en fait un invariant. C'est ce controle qui
# signalerait qu'une grille future a change de gabarit.
#
# Releve de reference (132 + 58 + 260 + 398 + 59 + 127 + 138 + 57 + 118 + 1 +
# 109 + 9 = 1466 segments), queue par queue :
#   annexe-dd     -> `<div class="criteria-row"` 122, `<div style=` 7,
#                    `<div class="criteria-description"` 1,
#                    `</div>` + CLOTURE_MARK 1 (« Fatigue — Vignettes cliniques »,
#                    seule grille a placer le bloc en dernier critere de section),
#                    `<div class="annexe-item annexe-scenario">` 1 (RESCOS-48,
#                    seule grille a le loger dans `annexes-grid`)
#   redflags      -> `<div class="criterion-comment-section"` 57,
#                    `<div class="checkbox-group">` 1
#   therapy       -> `<div class="therapy-section">` 137,
#                    `<div class="criterion-comment-section"` 121,
#                    `<div class="checkbox-group"` 2
#   cloture       -> `<div class="cloture-item">` 262, sinon `</div>`* + COMM_MARK 136
#   resume        -> `<div class="annexes">` 59/59
#   expert        -> `<div class="annexe-item annexe-theorie">` 124,
#                    `<div class="presentation-patient">` 2,
#                    `<div class="annexe-item annexe-scenario">` 1
#   theorie       -> `<div class="annexe-item annexe-scenario">` 59,
#                    `<div class="presentation-patient">` 54,
#                    `</div>`* + END_MARK 17, `<div class="images-wrapper">` 7,
#                    `<div class="annexe-item annexe-dd">` 1
#   presentation  -> `<div class="annexe-item annexe-scenario">` 57/57
#   scenario      -> `</div>`* + END_MARK 81, `<div class="images-wrapper">` 30,
#                    `<div class="annexe-item"` 6, `<div class="annexe-item annexe-qr">` 1
#   annexe-qr     -> `<div class="images-wrapper">` 1
#   annexe-image  -> item d'annexe suivant 62, `</div>`* + END_MARK 46,
#                    `<div class="images-wrapper">` 1
#   feuille-porte -> `</body>` 9/9
BLOCKS = [
    # --- blocs loges dans la section notee (niveau 2) ----------------------
    ("annexe-dd", r'<div class="annexe-item annexe-dd">',
     r'<div class="criteria-row"|<div class="criteria-description"|<div style=|<h4'
     r'|<div class="annexe-item annexe-scenario">'
     r'|(?:</div>\s*)*' + re.escape(CLOTURE_MARK)),
    ("redflags", r'<div class="redflags-section">',
     r'<div class="criterion-comment-section"|<div class="checkbox-group"'),
    ("therapy", r'<div class="therapy-section">',
     r'<div class="therapy-section">|<div class="criterion-comment-section"'
     r'|<div class="checkbox-group"'),
    # --- section « Cloture de consultation », non notee (niveau 2) ---------
    ("cloture", r'<div class="cloture-item">',
     r'<div class="cloture-item">|(?:</div>\s*)*' + re.escape(COMM_MARK)),
    # --- fiches pedagogiques de fin de page (niveau 3) ---------------------
    ("resume", r'<div class="resume">', r'<div class="annexes">'),
    ("expert", r'<div class="annexe-item annexe-expert">',
     r'<div class="annexe-item annexe-theorie">|<div class="presentation-patient">'
     r'|<div class="annexe-item annexe-scenario">'),
    ("theorie", r'<div class="annexe-item annexe-theorie">',
     r'<div class="annexe-item annexe-scenario">|<div class="presentation-patient">'
     r'|<div class="annexe-item annexe-dd">'
     r'|(?:</div>\s*)*(?:<div class="images-wrapper">|' + re.escape(END_MARK) + r')'),
    ("presentation", r'<div class="presentation-patient">',
     r'<div class="annexe-item annexe-scenario">'),
    ("scenario", r'<div class="annexe-item annexe-scenario">',
     r'<div class="annexe-item"(?=[ >])|<div class="annexe-item annexe-qr">'
     r'|(?:</div>\s*)*(?:<div class="images-wrapper">|' + re.escape(END_MARK) + r')'),
    # --- fiche questions/reponses, INEDITE : une seule grille --------------
    ("annexe-qr", r'<div class="annexe-item annexe-qr">',
     r'(?:</div>\s*)*(?:<div class="images-wrapper">|' + re.escape(END_MARK) + r')'),
    ("annexe-image", r'<div class="annexe-item"(?=[ >])',
     r'(?:</div>\s*)*(?:<div class="annexe-item"(?=[ >])|<div class="images-wrapper">|'
     + re.escape(END_MARK) + r')'),
    # --- feuille porte : la grille ENTIERE, 9 fichiers sans bareme ---------
    ("feuille-porte", r'<div class="feuille-porte">', r"</body>"),
]

# Blocs exclus de la mesure de redondance par defaut — voir report_redundancy.py.
# `scenario` est le SCRIPT DU PATIENT SIMULE : redire les symptomes deja listes
# dans les fiches est sa fonction meme. Meme convention qu'AMBOSS (dont le
# `BLOCKS` ne le contient pas) et que RESCOS. Il reste dans `BLOCKS`, donc
# borne, gele au snapshot et protege par `check_no_loss` : ce n'est pas un angle
# mort, c'est une exclusion documentee.
REDUNDANCY_EXCLUDED = {"scenario"}

# Classes porteuses de contenu redactionnel. Toute occurrence hors des segments
# de BLOCKS est une ANOMALIE : elle signale un bloc que l'outillage ne voit pas.
# C'est la traduction en controle automatique de l'angle mort d'AMBOSS-34.
#
# Liste etablie par MESURE, avec DEUX criteres verifies programmatiquement sur
# les 165 grilles (voir `_selftest_content_classes()` en fin de module) :
#
#   1. la classe est a 100 % DANS un segment de BLOCKS — zero occurrence dehors ;
#   2. son motif `class="[^"]*\bCLS\b[^"]*"` ne matche AUCUN attribut `class`
#      situe hors bloc. Ce second critere ecarte les jetons generiques : le
#      tiret est une frontiere de mot, donc `\btext\b` matcherait
#      `class="detail-text criteria-detail"`, c'est-a-dire la SECTION NOTEE.
CONTENT_CLASSES = [
    "annexe-dd-content", "dd-category",
    "arg-title", "arg-list", "reponse-pour", "reponse-contre", "reponse-section",
    "response-list",
    "therapy-section", "therapy-title", "therapy-items", "therapy-item",
    "redflags-section", "redflags-title", "redflags-item", "redflags-text",
    "redflags-description",
    "cloture-item", "cloture-title", "cloture-content", "cloture-content-green",
    "cloture-details", "cloture-detail", "cloture-question", "cloture-response",
    "resume", "resume-content", "resume-main-title", "resume-section",
    "resume-subsection", "resume-subsection-points", "resume-bullet",
    "resume-points", "resume-table", "resume-category", "tableau-comparatif",
    "subsection-title", "section-title", "table-title",
    "presentation-patient", "presentation-content", "presentation-main-title",
    "presentation-section", "presentation-section-title", "presentation-subsection",
    "presentation-points", "presentation-qa", "presentation-question",
    "presentation-reponse", "presentation-analyse", "presentation-astuce",
    "analyse-icon", "analyse-text", "astuce-icon", "astuce-text",
    "q-number", "q-text", "qa-container",
    "mnemo-box", "mnemo-title", "mnemo-items",
    "annexe-expert-content", "expert-section",
    "annexe-theorie-content", "theorie-section",
    "theorie-section-rappels", "theorie-section-examens",
    "annexe-scenario-content", "scenario-section", "scenario-info",
    "annexe-qr-content", "qr-item",
    "annexe-image", "annexe-description",
    "highlight-important", "highlight-range", "highlight-percent",
    "arrow-updown",
    "section-anamnese", "section-examen", "section-management",
    "section-keypoints", "section-diagnostic", "section-checklist",
    "section-longue", "section-express", "section-mnemo", "section-questions",
    "feuille-porte", "titre-station", "contexte-label", "taches",
    "property-group", "nested-object", "signes-vitaux",
]

# Deliberement ABSENTES de CONTENT_CLASSES :
#
# * `criteria-text`, `detail-text criteria-detail`, `patient-response`,
#   `scoring-rule`, `sub-criteria`, `criteria-row`, `points-display`,
#   `criteria-subheader`, `criteria-description`, `communication-*` : c'est la
#   SECTION NOTEE elle-meme (niveau 2), pas un bloc de commentaire.
# * `exemple-phrase` / `exemples-phrases` : jeton MIXTE, mesure — 537
#   occurrences dans un bloc (`cloture` pour l'essentiel) et 222 DEHORS, sur 29
#   grilles, ou elles sont logees dans un `criteria-row` juste apres le
#   `details-with-checkboxes` d'un critere note. Ce n'est pas un bloc autonome
#   mais une FEUILLE : une annotation du critere, au meme titre que
#   `patient-response`. La compter comme classe de contenu ferait crier
#   `uncovered_content()` sur 29 grilles saines. Ses items sont neanmoins
#   extraits par `list_items()` la ou elle tombe dans un bloc — voir
#   `_DIV_ITEM_CLASSES`.
# * `vital-sign*`, `missing-items` (conteneur COMMENTE dans le HTML, voir
#   l'entete), `annexes`, `annexes-grid`, `images-wrapper`,
#   `section cloture-section` : ce sont les CONTENEURS des blocs, pas leur
#   contenu — ils sont par construction hors des segments.
# * `arrow`, `equals`, `highlight`, `list`, `text`, `structured`, `urgence`,
#   `contexte`, `description`, `question`, `answer`, `first-col`, `with-arrow`,
#   `with-data`, `annexe-item`, `annexe-title`, `annexe-content` : jetons trop
#   generiques, ecartes par le critere n° 2 ci-dessus ou par prudence. Tous sont
#   portes par des classes deja couvertes autrement (`resume-bullet highlight`,
#   `presentation-reponse list`, `annexe-item annexe-dd`, ...), leur absence ne
#   cree donc pas d'angle mort.

_TAG = re.compile(r"<(/?)(\w+)([^>]*)>")
_DIGITS = re.compile(r"(\d+)")


def grid_key(path):
    """Cle de tri NATURELLE d'une grille.

    Ce corpus n'a pas de numerotation uniforme : 33 fichiers portent un numero
    (`RESCOS-41` a `RESCOS-69`), les 132 autres un intitule thematique. Un tri
    purement alphabetique placerait `RESCOS-41` apres `RESCOS-4` mais aussi
    apres `RESCOS-100` si une telle grille apparaissait. La cle decoupe le nom
    en suites de chiffres et de non-chiffres et compare les premieres comme des
    entiers : `RESCOS-9` < `RESCOS-41` < `RESCOS-69`, et l'ordre reste
    l'ordre du repertoire pour tout le reste.
    """
    return tuple(int(p) if p.isdigit() else p.lower()
                 for p in _DIGITS.split(Path(path).name))


def grids():
    """Chemins des 165 grilles, en ordre naturel."""
    return sorted(CASES.glob("*.html"), key=grid_key)


def _balanced_end(html, start):
    """Index de fin du `<div>` ouvert en `start`, par equilibrage strict.

    Plus sur qu'un motif de fin : un bloc qui en contient un autre du meme type,
    ou qui contient par accident le motif de fin d'un voisin, ne peut pas
    tromper l'equilibrage. Les 165 grilles sont globalement equilibrees ; en cas
    d'anomalie locale la fonction rend `len(html)`, ce que `bounds_anomalies()`
    signale.
    """
    depth = 0
    for m in _TAG.finditer(html, start):
        if m.group(2).lower() != "div":
            continue
        if m.group(1) == "/":
            depth -= 1
            if depth == 0:
                return m.end()
        elif not m.group(3).rstrip().endswith("/"):
            depth += 1
    return len(html)


def block_spans(html, name):
    """Tous les couples (debut, fin) d'un bloc — liste vide s'il est absent."""
    pattern = next((s for n, s, _ in BLOCKS if n == name), None)
    if pattern is None:
        return []
    return [(m.start(), _balanced_end(html, m.start()))
            for m in re.finditer(pattern, html)]


def block_segments(html, name):
    """Tous les segments HTML d'un bloc. Un bloc peut apparaitre plusieurs fois."""
    return [html[a:b] for a, b in block_spans(html, name)]


def block_segment(html, name):
    """Premier segment d'un bloc, ou None — compatibilite de signature avec AMBOSS.

    A ne pas employer pour compter ou pour dedoublonner : elle perd les
    segments suivants (jusqu'a 8 `therapy-section` et 8 `cloture-item` dans une
    meme grille). Utiliser `block_segments()`.
    """
    segments = block_segments(html, name)
    return segments[0] if segments else None


def blocks_present(html):
    """Noms des blocs presents, avec leur nombre de segments : [[nom, n], ...]."""
    return [[name, len(block_spans(html, name))]
            for name, _, _ in BLOCKS if block_spans(html, name)]


def all_spans(html):
    """Tous les segments de tous les blocs, fusionnes et tries."""
    spans = [s for name, _, _ in BLOCKS for s in block_spans(html, name)]
    return sorted(spans)


def peda_bounds(html):
    """Index (debut, fin) de la zone pedagogique de fin de page.

    Debut : `<div class="resume">` si present, sinon `<div class="annexes">`.
    Fin : le commentaire `<!-- COMMENTAIRE GENERAL -->`, present 156/156 sur
    les grilles notees. Retourne (-1, -1) pour les 21 grilles sans zone
    pedagogique (les 9 feuilles porte et 12 grilles notees sans `annexes`).

    Ne couvre NI `annexe-dd` (section notee, voir `dd_bounds()`), NI `therapy`,
    `redflags` et `cloture`, disperses dans la page en amont. Pour lire tout le
    contenu d'une grille, passer par `block_spans()`.
    """
    start = html.find('<div class="resume">')
    if start < 0:
        start = html.find('<div class="annexes">')
    if start < 0:
        return -1, -1
    end = html.find(END_MARK, start)
    return start, (end if end > 0 else len(html))


def dd_bounds(html):
    """Index (debut, fin) du premier bloc `annexe-dd`, pour une lecture ciblee.

    Dans 122 grilles sur 123 ce bloc vit dans la section notee, donc avant la
    zone rendue par `peda_bounds()`. Une grille le place au contraire DANS
    `annexes-grid` (sa queue tombe alors sur le `theorie` suivant) : les deux
    plages s'y recouvrent, et tout appelant qui les concatene doit dedoublonner
    (c'est ce que fait `all_items()`, qui passe par les blocs et non par les
    zones). Meme convention d'index que `peda_bounds()` — des caracteres, a
    convertir en numeros de ligne pour `Read`. Retourne (-1, -1) si absent.
    """
    spans = block_spans(html, "annexe-dd")
    return spans[0] if spans else (-1, -1)


def bounds_anomalies(html):
    """Blocs dont la fin equilibree ne tombe pas sur la queue attendue.

    Filet contre une derive de gabarit : si une grille future deplace un bloc,
    l'equilibrage rendra toujours une borne juste mais ce qui la suit changera,
    et l'ecart sera signale ici plutot que de passer inapercu.
    """
    out = []
    for name, _, tail in BLOCKS:
        for a, b in block_spans(html, name):
            if b >= len(html) or not re.match(r"\s*(?:" + tail + ")", html[b:b + 400]):
                out.append(f"{name}@{a}: fin sur {html[b:b + 48]!r}")
    return out


def uncovered_content(html):
    """Classes de contenu presentes HORS de tout bloc — doit rester vide.

    C'est le controle qui a fait apparaitre `therapy-section` et
    `redflags-section` dans German, `cloture-item` dans RESCOS, et ici les deux
    blocs inedits `feuille-porte` et `annexe-qr` : sans eux, neuf grilles
    entieres et une fiche auraient ete invisibles a tout l'outillage.
    """
    spans = all_spans(html)
    out = {}
    for cls in CONTENT_CLASSES:
        pattern = r'class="[^"]*\b' + re.escape(cls) + r'\b[^"]*"'
        for m in re.finditer(pattern, html):
            if not any(a <= m.start() < b for a, b in spans):
                out[cls] = out.get(cls, 0) + 1
    return out


# Items portes par un `<div>` plutot que par un `<li>` ou une puce.
#
# `redflags-text` (264) et `annexe-description` (103) sont les memes que dans
# German et RESCOS. `cloture-content*` (354) vient de RESCOS. S'y ajoutent, pour
# ce corpus :
#   * `therapy-item` (188) — le bloc `therapy` n'emploie la puce « • » que dans
#     73 de ses 260 segments ; les 187 autres portent leurs items dans ce div ;
#   * `exemple-phrase` (537 en bloc) — phrases-types de cloture et de
#     communication, ni liste ni puce ;
#   * `cloture-detail`, `cloture-question`, `cloture-response` (34/21/21) —
#     variante structuree de la cloture ;
#   * `qr-item` (3) — la fiche questions/reponses inedite.
#
# L'extraction se fait par EQUILIBRAGE et non par `(.*?)</div>` : `therapy-item`
# contient un `<div>` interne dans ses 188 occurrences, qu'un motif non gourmand
# tronquerait a la premiere fermeture. Les classes retenues sont toutes des
# FEUILLES au sens de cette famille — aucune n'en contient une autre — donc
# aucun double comptage. `cloture-details` et `therapy-items`, qui sont leurs
# conteneurs, en sont deliberement absentes.
_DIV_ITEM_CLASSES = (
    "redflags-text", "annexe-description", "therapy-item", "exemple-phrase",
    "cloture-content", "cloture-detail", "cloture-question", "cloture-response",
    "qr-item",
)
_DIV_ITEM_OPEN = re.compile(
    r'<div class="(?:' + "|".join(
        # `cloture-content` couvre aussi `cloture-content-green`.
        re.escape(c) + ("[^\"]*" if c == "cloture-content" else "")
        for c in _DIV_ITEM_CLASSES) + r')"[^>]*>')


def _div_items(segment):
    """(items, segment ampute) — items portes par un `<div>` de classe dediee.

    Rend aussi le segment prive de ces `<div>`, pour que le decoupage par puces
    qui suit ne les recompte pas.
    """
    items, cuts, pos = [], [], 0
    for m in _DIV_ITEM_OPEN.finditer(segment):
        if m.start() < pos:          # deja consomme par un item precedent
            continue
        end = _balanced_end(segment, m.start())
        items.append(segment[m.end():max(m.end(), end - len("</div>"))])
        cuts.append((m.start(), end))
        pos = end
    rest, last = [], 0
    for a, b in cuts:
        rest.append(segment[last:a])
        last = b
    rest.append(segment[last:])
    return items, " ".join(rest)


def list_items(segment, min_len=18):
    """Items normalises d'un segment, filtres sur une longueur minimale.

    Reprend la regle d'AMBOSS — `<li>`, puces « • » a l'interieur d'un `<li>`,
    puces hors `<li>` en jetant la tete sans borne gauche — et y ajoute, comme
    German et RESCOS, les items portes par un `<div>` de classe dediee.

    Trois formats coexistent dans ce corpus :

    - `<li>` : `resume` (2822), `presentation` (3323), `theorie` (4046),
      `expert` (2006), `scenario` (3625), `feuille-porte` (32), et `annexe-dd`
      (589 `<li>` portant chacun un diagnostic entier, decoupe ensuite par ses
      1941 puces) ;
    - puce « • » separee par des `<br>` hors de tout `<li>` : `therapy` (323) et
      `cloture` (281). La tete jetee est le `therapy-title` / `cloture-title`,
      un intitule ;
    - `<div>` de classe dediee : voir `_DIV_ITEM_CLASSES`. `redflags` (58
      segments) et `annexe-image` (103) n'ont AUCUN `<li>` ni puce et
      rendraient zero item sans cette extension.

    Aucun double comptage : les `<div>` d'item sont retires du reste avant le
    decoupage par puces, et ne sont jamais dans un `<li>`.

    `min_len` vaut 18 comme dans AMBOSS, German et RESCOS, pour que le chiffre
    de redondance des quatre corpus se lise dans la meme unite.
    """
    items = []
    for m in re.finditer(r"<li[^>]*>(.*?)</li>", segment, re.S):
        text = visible_text(m.group(1))
        items += _bullet_items(text) if BULLET in text else [norm(text)]
    div_html, rest = _div_items(re.sub(r"<li[^>]*>.*?</li>", " ", segment, flags=re.S))
    for chunk in div_html:
        text = visible_text(chunk)
        items += _bullet_items(text) if BULLET in text else [norm(text)]
    outside = visible_text(rest)
    if BULLET in outside:
        items += _bullet_items(outside)[1:]
    return [i for i in items if len(i) >= min_len]


def all_items(html):
    """Items de TOUS les blocs d'une grille, fusionnes.

    Fusionnes et non compares bloc par bloc : un item deplace d'un bloc a un
    autre est un deplacement legitime, pas une disparition.
    """
    items = []
    for name, _, _ in BLOCKS:
        for segment in block_segments(html, name):
            items += list_items(segment)
    return items


def _selftest_content_classes():
    """Verifie les deux criteres de selection de CONTENT_CLASSES sur le corpus.

    Rend la liste des manquements. Utilise pour ETABLIR la liste, et rejouable
    a tout moment :  `python3 -c "import lib_rescos_locales as l;
    print(l._selftest_content_classes())"`. Ce n'est pas une porte — c'est
    `check_invariants.py`, via `uncovered_content`, qui l'est.
    """
    problems = []
    for path in grids():
        html = strip_base64(path.read_text(encoding="utf-8"))
        left = uncovered_content(html)
        if left:
            problems.append(f"{path.name}: {left}")
    return problems
