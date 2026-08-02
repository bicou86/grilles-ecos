"""Fonctions partagees pour le traitement des grilles RESCOS.

ARCHITECTURE — ce qui est importe, ce qui est redefini
------------------------------------------------------
Meme partage que `scripts/german/lib_german.py`, pour la meme raison. Les
primitives de TEXTE viennent de `scripts/amboss/lib_amboss.py`, chargees par
chemin explicite : `strip_base64`, `visible_text`, `norm`, `BULLET`,
`_bullet_items`. Elles ne dependent d'aucune particularite de corpus — elles
nettoient du HTML et normalisent du francais — et chacune porte un correctif
durement acquis :

  * `visible_text` ne consomme pas le CHEVRON NU d'un seuil (`Hb < 70 g/L`).
    Ce corpus en porte 114 sur 30 grilles : un `re.sub(r'<[^>]+>', ...)` naif
    avalerait la clause qui suit chacun d'eux ;
  * `strip_base64` neutralise les data-URI avant tout controle ;
  * `_bullet_items` traite la puce « • » comme un separateur.

Sont egalement importees de `scripts/amboss/` la table `BANNED`
(`check_nomenclature`) et la simulation de `cases/scoring.js`
(`check_reachability`) — voir les scripts concernes.

Ce qui DECRIT le corpus est redefini ici, et rien n'est ecrit dans
`scripts/amboss/` ni dans `scripts/german/` : `CASES`, `BLOCKS`,
`CONTENT_CLASSES`, `grids()`, `grid_num()`, les bornes (`_balanced_end`,
`block_spans`, `peda_bounds`, `dd_bounds`, `bounds_anomalies`,
`uncovered_content`) et `list_items()`. Aucun fichier des deux corpus
precedents n'est modifie : leurs mesures publiees (AMBOSS 147 paires
inter-blocs, German 14) sont inchangees par construction.

POURQUOI `_balanced_end` EST RECOPIE PLUTOT QU'IMPORTE DE `lib_german`
----------------------------------------------------------------------
C'est le seul point ou ce module s'ecarte du precedent German. L'equilibrage de
`<div>` est quinze lignes de syntaxe pure : il ne porte aucun correctif acquis a
l'usage, contrairement a `visible_text`, dont le bug du chevron nu est
precisement la raison pour laquelle German l'importe. L'importer de `lib_german`
ferait de German une dependance porteuse d'un corpus qui n'a rien a voir avec
lui, et transformerait une etoile (amboss = racine partagee, german et rescos =
feuilles) en chaine. Surtout, une divergence entre les deux copies ne peut pas
passer inapercue : elle se manifeste par `bounds_anomalies()`, verifie a chaque
passage de `check_invariants.py`, corpus par corpus.

Le bon point de chute a terme est un module partage (`scripts/lib_grilles.py`)
d'ou les trois corpus tireraient l'equilibrage ; ce refactor touche `lib_german`
et n'entrait pas dans le perimetre de cette tache.

DIFFERENCES STRUCTURELLES AVEC AMBOSS (mesurees sur les 41 grilles)
-------------------------------------------------------------------
La structure est PROCHE d'AMBOSS, contrairement a German : les trois fiches de
fin de page existent (`expert` 39/41, `theorie` 37/41, `scenario` 39/41), la
zone pedagogique s'ouvre sur `resume`/`annexes` et le bloc `annexe-dd` vit dans
la section Management. S'y ajoutent quatre differences :

* `cloture` — bloc INEDIT, absent du `BLOCKS` d'AMBOSS comme de celui de
  German : 40 segments sur 13 grilles, loges dans une cinquieme section de page
  `<div class="section cloture-section">` (« Cloture de consultation »), placee
  entre Management et Communication. Cette section ne porte AUCUN critere note
  (0 `criteria-row`, 0 `criteria-text`, 0 `<input>`) : c'est du contenu
  redactionnel pur — explication au patient, questions du patient, reponses
  adaptees. Sans entree dans `BLOCKS`, ces 40 blocs seraient invisibles, ce qui
  est exactement l'angle mort d'AMBOSS-34.
* `therapy` (47 segments / 16 grilles) et `redflags` (6 / 6) : memes blocs que
  German, loges dans un `criteria-row` de la section notee.
  ATTENTION : `grep -l therapy-section` rend 18 grilles et non 16 — deux
  grilles ne portent la chaine que dans leur feuille de style. Le compte qui
  fait foi est celui des `class="therapy-section"`, soit 16.
* `annexe-dd` (22 / 22) : 20 grilles le placent dans la section Management
  (fin sur le `criteria-row` suivant, comme AMBOSS), mais RESCOS-14 et
  RESCOS-24 le placent en fin de page, DANS `annexes-grid`, apres la
  `presentation` — sa fin y tombe sur `annexe-scenario`. Les deux queues sont
  donc attendues.
* `annexe-image` (33 / 12) : items d'image et de laboratoire portes par un
  `<div class="annexe-item">` nu, comme dans German.

Le corpus est globalement equilibre en `<div>` : 41 grilles sur 41, zero ecart
entre `<div` et `</div>`. C'est ce qui autorise le decoupage par equilibrage.
"""
import importlib.util
import re
import sys
from pathlib import Path

_AMBOSS_DIR = Path(__file__).resolve().parents[1] / "amboss"


def amboss_module(name):
    """Charge un module de `scripts/amboss/` sous un alias `_rescos_amboss_<nom>`.

    Chargement par chemin explicite, jamais par `sys.path` : les trois dossiers
    de corpus portent des scripts de meme nom (`check_nomenclature.py`,
    `check_reachability.py`, ...) et un import ordinaire resoudrait selon
    l'ordre du chemin, donc au hasard.

    L'alias porte un prefixe PROPRE a rescos, distinct du `_amboss_<nom>` de
    `lib_german`. Sans cela, les deux corpus partageraient la meme instance
    dans `sys.modules`, et le remplacement de `parse_config` opere par
    `check_reachability.py` (forme imperative de RESCOS-7 et RESCOS-9)
    fuirait vers German s'ils s'executaient dans le meme processus.
    """
    path = _AMBOSS_DIR / (name + ".py")
    spec = importlib.util.spec_from_file_location("_rescos_amboss_" + name, path)
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

CASES = Path(__file__).resolve().parents[2] / "cases" / "rescos"

# Marqueur de fin de la zone pedagogique. Present dans les 41 grilles, une
# seule fois par grille, et toujours apres le dernier bloc de contenu.
END_MARK = "<!-- COMMENTAIRE GÉNÉRAL -->"

# Marqueur de fin de la section « Cloture de consultation », present dans les
# 13 grilles qui la portent, immediatement apres le dernier `cloture-item`.
COMM_MARK = "<!-- COMMUNICATION -->"

# Bornes des blocs de contenu, dans leur ordre d'apparition dans le fichier.
#
# Chaque entree est (nom, motif de debut, queue attendue). Le decoupage reel se
# fait par EQUILIBRAGE des `<div>` (`_balanced_end`), pas par le motif de fin :
# les 41 grilles sont globalement equilibrees (verifie : 0 ecart entre `<div`
# et `</div>`), et l'equilibrage ne peut pas se tromper de borne quand un bloc
# en contient un autre. La « queue attendue » est ce qui doit suivre
# immediatement la fin equilibree ; `bounds_anomalies()` le verifie sur tout le
# corpus et `check_invariants.py` en fait un invariant. C'est ce controle qui
# signalerait qu'une grille future a change de gabarit.
#
# Releve de reference (22 + 6 + 47 + 40 + 25 + 39 + 37 + 25 + 39 + 33 = 313
# segments), queue par queue :
#   annexe-dd    -> `<div class="criteria-row"` 20 (m2 x10, m3 x8, m4, m5)
#                   `<div class="annexe-item annexe-scenario">` 2 (RESCOS-14, 24)
#   redflags     -> `<div class="criterion-comment-section"` 6/6
#   therapy      -> `<div class="therapy-section">` 31, sinon
#                   `<div class="criterion-comment-section"` 16
#   cloture      -> `<div class="cloture-item">` 27, sinon `</div>`* + COMM_MARK 13
#   resume       -> `<div class="annexes">` 25/25
#   expert       -> `<div class="annexe-item annexe-theorie">` 37,
#                   `<div class="presentation-patient">` 1,
#                   `<div class="annexe-item annexe-scenario">` 1
#   theorie      -> `<div class="presentation-patient">` 23, sinon
#                   `<div class="annexe-item annexe-scenario">` 14
#   presentation -> `<div class="annexe-item annexe-scenario">` 22,
#                   `<div class="annexe-item annexe-dd">` 2 (RESCOS-14, 24),
#                   `</div>`* + END_MARK 1 (RESCOS-6, sans scenario)
#   scenario     -> `</div>`* + END_MARK 27, sinon `<div class="images-wrapper">` 12
#   annexe-image -> item d'image suivant 21, sinon `</div>`* + END_MARK 12
BLOCKS = [
    # --- blocs loges dans la section notee (niveau 2) ----------------------
    ("annexe-dd", r'<div class="annexe-item annexe-dd">',
     r'<div class="criteria-row"|<div class="annexe-item annexe-scenario">'),
    ("redflags", r'<div class="redflags-section">',
     r'<div class="criterion-comment-section"'),
    ("therapy", r'<div class="therapy-section">',
     r'<div class="therapy-section">|<div class="criterion-comment-section"'),
    # --- section « Cloture de consultation », non notee (niveau 2) ---------
    ("cloture", r'<div class="cloture-item">',
     r'<div class="cloture-item">|(?:</div>\s*)*' + re.escape(COMM_MARK)),
    # --- fiches pedagogiques de fin de page (niveau 3) ---------------------
    ("resume", r'<div class="resume">', r'<div class="annexes">'),
    ("expert", r'<div class="annexe-item annexe-expert">',
     r'<div class="annexe-item annexe-theorie">|<div class="presentation-patient">'
     r'|<div class="annexe-item annexe-scenario">'),
    ("theorie", r'<div class="annexe-item annexe-theorie">',
     r'<div class="presentation-patient">|<div class="annexe-item annexe-scenario">'),
    ("presentation", r'<div class="presentation-patient">',
     r'<div class="annexe-item annexe-scenario">|<div class="annexe-item annexe-dd">'
     r'|(?:</div>\s*)*' + re.escape(END_MARK)),
    ("scenario", r'<div class="annexe-item annexe-scenario">',
     r'(?:</div>\s*)*(?:<div class="images-wrapper">|' + re.escape(END_MARK) + r')'),
    ("annexe-image", r'<div class="annexe-item"(?=[ >])',
     r'(?:</div>\s*)*(?:<div class="annexe-item"(?=[ >])|'
     + re.escape(END_MARK) + r')'),
]

# Blocs exclus de la mesure de redondance par defaut — voir report_redundancy.py.
# `scenario` est le SCRIPT DU PATIENT SIMULE : redire les symptomes deja listes
# dans les fiches est sa fonction meme. AMBOSS l'exclut deja de fait (son
# `BLOCKS` ne le contient pas et `peda_bounds` s'arrete dessus) ; l'exclure ici
# aussi garde les deux corpus dans la meme unite. Il reste dans `BLOCKS`, donc
# borne, gele au snapshot et protege par `check_no_loss` : ce n'est pas un angle
# mort, c'est une exclusion documentee.
REDUNDANCY_EXCLUDED = {"scenario"}

# Classes porteuses de contenu redactionnel. Toute occurrence hors des segments
# de BLOCKS est une ANOMALIE : elle signale un bloc que l'outillage ne voit pas.
# C'est la traduction en controle automatique de l'angle mort d'AMBOSS-34, ou
# une fiche portee par une classe non prevue etait restee invisible et n'avait
# eu pour seul symptome qu'un chiffre de redondance anormalement bas.
#
# Liste etablie par MESURE et non a la main : toutes les valeurs de `class=` du
# corpus ont ete partagees entre celles qui tombent dans un segment de BLOCKS et
# celles qui n'y tombent jamais. La partition est nette — chacune des classes
# ci-dessous est a 100 % dans un bloc (zero occurrence dehors), et tout ce qui
# reste dehors est soit la charpente de page, soit la section notee.
CONTENT_CLASSES = [
    "annexe-dd-content", "dd-category",
    "arg-title", "arg-list", "reponse-pour", "reponse-contre", "reponse-section",
    "response-list",
    "therapy-section", "therapy-title",
    "redflags-section", "redflags-title", "redflags-item", "redflags-text",
    "redflags-description",
    "cloture-item", "cloture-title", "cloture-content", "cloture-content-green",
    "resume", "resume-content", "resume-main-title", "resume-section",
    "resume-subsection", "resume-subsection-points", "resume-bullet",
    "resume-points", "resume-table", "tableau-comparatif",
    "subsection-title", "section-title", "table-title", "first-col",
    "nested-object", "property-group",
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
    "annexe-image", "annexe-description", "lab-section", "lab-results",
    "highlight-important", "highlight-range", "highlight-percent",
    "arrow-updown", "with-arrow",
    "section-anamnese", "section-examen", "section-management",
    "section-keypoints", "section-diagnostic", "section-checklist",
    "section-longue", "section-express", "section-mnemo", "section-questions",
]

# Deliberement ABSENTES de CONTENT_CLASSES :
#
# * `criteria-text`, `detail-text criteria-detail`, `patient-response`,
#   `scoring-rule`, `sub-criteria`, `criteria-row`, `points-display`,
#   `criteria-subheader`, `communication-*` : c'est la SECTION NOTEE elle-meme
#   (niveau 2), pas un bloc de commentaire.
# * `vital-sign*` (panneau de constantes de l'en-tete), `missing-items`
#   (conteneur vide rempli par le JavaScript), `annexes`, `annexes-grid`,
#   `images-wrapper`, `section cloture-section` : ce sont les CONTENEURS des
#   blocs, pas leur contenu — ils sont par construction hors des segments.
# * `arrow`, `equals`, `highlight`, `list`, `text`, `structured`, `urgence`,
#   `annexe-item`, `annexe-title` : jetons trop generiques. Le motif de
#   `uncovered_content()` est `class="[^"]*\bCLS\b[^"]*"`, et le tiret est une
#   frontiere de mot : `\btext\b` matcherait `class="detail-text criteria-detail"`,
#   c'est-a-dire la section notee. Ces jetons sont tous portes par des classes
#   deja couvertes autrement (`resume-bullet highlight`, `presentation-reponse
#   list`, `annexe-item annexe-dd`, ...), leur absence ne cree donc pas d'angle
#   mort.

_TAG = re.compile(r"<(/?)(\w+)([^>]*)>")


def grids():
    """Chemins des 41 grilles, tries par numero.

    Le tri est un couple (numero, suffixe) et non un entier : le corpus porte
    une grille RESCOS-9b (« Boiterie pediatrique — Fillette de 2 ans »), qu'un
    `int()` sur la seule partie chiffree ferait passer pour une seconde
    RESCOS-9 et placerait avant ou apres elle au hasard.
    """
    return sorted(CASES.glob("RESCOS-*.html"), key=grid_num)


def grid_num(path):
    """(numero, suffixe) d'une grille — (9, '') pour RESCOS-9, (9, 'b') pour 9b."""
    m = re.search(r"RESCOS-(\d+)([a-z]*)", Path(path).name)
    return int(m.group(1)), m.group(2)


def _balanced_end(html, start):
    """Index de fin du `<div>` ouvert en `start`, par equilibrage strict.

    Plus sur qu'un motif de fin : un bloc qui en contient un autre du meme type,
    ou qui contient par accident le motif de fin d'un voisin, ne peut pas
    tromper l'equilibrage. Les 41 grilles sont globalement equilibrees ; en cas
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
    segments suivants (jusqu'a 4 `therapy-section` et 4 `cloture-item` dans une
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
    Fin : le commentaire `<!-- COMMENTAIRE GENERAL -->`, present 41/41.
    Retourne (-1, -1) pour RESCOS-11, seule grille sans `resume` ni `annexes`.

    Ne couvre NI `annexe-dd` (section Management, voir `dd_bounds()`), NI
    `therapy`, `redflags` et `cloture`, disperses dans la page en amont. Pour
    lire tout le contenu d'une grille, passer par `block_spans()`.
    """
    start = html.find('<div class="resume">')
    if start < 0:
        start = html.find('<div class="annexes">')
    if start < 0:
        return -1, -1
    end = html.find(END_MARK, start)
    return start, (end if end > 0 else len(html))


def dd_bounds(html):
    """Index (debut, fin) du bloc `annexe-dd`, pour une lecture ciblee.

    Dans 20 grilles sur 22 ce bloc vit dans la section Management, donc avant
    la zone rendue par `peda_bounds()`. Dans RESCOS-14 et RESCOS-24 il est au
    contraire DANS `annexes-grid`, donc a l'interieur de cette zone : les deux
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
    `redflags-section` dans German, et `cloture-item` ici : trois blocs entiers
    qu'une transposition naive du `BLOCKS` d'AMBOSS aurait laisses invisibles.
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
# `redflags-text` (30) et `annexe-description` (33) sont les memes que dans
# German. `cloture-content` (40) est propre a ce corpus : le bloc `cloture` ne
# contient ni `<li>` ni puce « • » dans 12 de ses 13 grilles, il rendrait donc
# zero item sans cette extension.
_DIV_ITEM = re.compile(
    r'<div class="(?:redflags-text|annexe-description|cloture-content[^"]*)">(.*?)</div>',
    re.S)


def list_items(segment, min_len=18):
    """Items normalises d'un segment, filtres sur une longueur minimale.

    Reprend la regle d'AMBOSS — `<li>`, puces « • » a l'interieur d'un `<li>`,
    puces hors `<li>` en jetant la tete sans borne gauche — et y ajoute, comme
    German, les items portes par un `<div>` de classe dediee.

    Trois formats coexistent dans ce corpus :

    - `<li>` : `resume`, `presentation`, `theorie`, `expert`, `scenario`, et
      `annexe-dd` (chaque `<li>` portant un diagnostic entier, decoupe ensuite
      par ses puces) ;
    - puce « • » separee par des `<br>` hors de tout `<li>` : `therapy-section`,
      comme dans German. La tete jetee est le `therapy-title`, un intitule ;
    - `<div class="redflags-text">`, `<div class="annexe-description">` et
      `<div class="cloture-content ...">` : ni liste ni puce.

    Aucun double comptage : les `<div>` d'item sont retires du reste avant le
    decoupage par puces, et ne sont jamais dans un `<li>`.

    `min_len` vaut 18 comme dans AMBOSS et German, pour que le chiffre de
    redondance des trois corpus se lise dans la meme unite.
    """
    items = []
    for m in re.finditer(r"<li[^>]*>(.*?)</li>", segment, re.S):
        text = visible_text(m.group(1))
        items += _bullet_items(text) if BULLET in text else [norm(text)]
    for m in _DIV_ITEM.finditer(segment):
        text = visible_text(m.group(1))
        items += _bullet_items(text) if BULLET in text else [norm(text)]
    rest = re.sub(r"<li[^>]*>.*?</li>", " ", segment, flags=re.S)
    rest = _DIV_ITEM.sub(" ", rest)
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
