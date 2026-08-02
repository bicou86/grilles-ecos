"""Fonctions partagees pour le traitement des grilles German.

ARCHITECTURE — pourquoi ce module n'est pas une copie de `lib_amboss.py`
------------------------------------------------------------------------
Les primitives de TEXTE sont importees telles quelles de `lib_amboss` :
`strip_base64`, `visible_text`, `norm`, `_bullet_items`, `BULLET`. Elles ne
dependent d'aucune particularite de corpus — elles nettoient du HTML et
normalisent du francais — et chacune porte un correctif durement acquis :

  * `visible_text` ne consomme pas le CHEVRON NU d'un seuil (`Hb < 70 g/L`) ;
  * `strip_base64` neutralise les data-URI avant tout controle ;
  * `_bullet_items` traite la puce « • » comme un separateur.

Les dupliquer ici, c'est garantir qu'un correctif futur sera applique a un seul
des deux corpus. Les importer, c'est une implementation unique pour les deux.

Ce qui est PROPRE au corpus est redefini ici, et rien n'est ecrit dans
`scripts/amboss/` : `CASES`, `BLOCKS`, `grids()`, `grid_num()`, `peda_bounds()`,
`dd_bounds()`, `block_segments()`, `list_items()`. Aucun fichier d'AMBOSS n'est
modifie, donc les mesures publiees d'AMBOSS sont inchangees par construction.

DIFFERENCES STRUCTURELLES AVEC AMBOSS (mesurees sur les 88 grilles)
-------------------------------------------------------------------
* `annexe-expert`, `annexe-theorie`, `annexe-scenario` : 0/88 a l'import. Ces
  trois blocs n'existaient pas dans ce corpus ; il n'y a donc pas de marqueur de
  fin `annexe-scenario` sur lequel borner la zone pedagogique. `annexe-theorie`
  est desormais declare dans BLOCKS : le chantier des sections pedagogiques en
  cree, et sa classe interne `theorie-section` est une CONTENT_CLASSE — sans
  declaration, elle serait vue hors bloc. `annexe-expert` et `annexe-scenario`
  restent absents et non declares.
* `annexe-dd` : 77/88 grilles, **78 segments** — German-78 en porte deux. Tout
  bloc peut donc apparaitre plusieurs fois dans une meme grille : c'est
  `block_segments()` (pluriel) qui fait foi, et non `block_segment()`.
* deux blocs de contenu supplementaires, absents d'AMBOSS et loges DANS un
  `criteria-row` de la section notee : `therapy-section` (126 segments, 44
  grilles) et `redflags-section` (10 segments, 10 grilles). Ils portent la
  reponse attendue du critere qu'ils accompagnent. Les ignorer reproduirait
  exactement l'angle mort d'AMBOSS-34 — un bloc invisible, dont le seul
  symptome est un chiffre de redondance anormalement bas.
* `redflags-section` ne contient **ni `<li>` ni puce « • »** : ses items sont
  des `<div class="redflags-text">`. Sans l'extension de `list_items()`
  ci-dessous, ce bloc rendrait zero item — invisible a la redondance comme a
  `check_no_loss`.
* la zone pedagogique se termine sur le commentaire `<!-- COMMENTAIRE GENERAL
  -->` (present 88/88), pas sur `annexe-scenario`.
"""
import importlib.util
import re
import sys
from pathlib import Path

_AMBOSS_DIR = Path(__file__).resolve().parents[1] / "amboss"


def amboss_module(name):
    """Charge un module de `scripts/amboss/` sous un alias `_amboss_<nom>`.

    Chargement par chemin explicite, jamais par `sys.path` : les deux dossiers
    portent des scripts de meme nom (`check_nomenclature.py`, ...) et un import
    ordinaire resoudrait selon l'ordre du chemin, donc au hasard. Sert a
    reutiliser ce qui ne depend pas du corpus — la table de nomenclature, la
    simulation de `scoring.js` — sans en faire une seconde copie.
    """
    path = _AMBOSS_DIR / (name + ".py")
    spec = importlib.util.spec_from_file_location("_amboss_" + name, path)
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

CASES = Path(__file__).resolve().parents[2] / "cases" / "german"

# Marqueur de fin de la zone pedagogique. Present dans les 88 grilles, une seule
# fois par grille, et toujours apres le dernier bloc de contenu.
END_MARK = "<!-- COMMENTAIRE GÉNÉRAL -->"

# Bornes des blocs de contenu, dans leur ordre d'apparition dans le fichier.
#
# Chaque entree est (nom, motif de debut, queue attendue). Le decoupage reel se
# fait par EQUILIBRAGE des `<div>` (`_balanced_end`), pas par le motif de fin :
# les 88 grilles sont globalement equilibrees (verifie : 0 ecart entre `<div>`
# et `</div>`), et l'equilibrage ne peut pas se tromper de borne quand un bloc
# en contient un autre. La « queue attendue » est ce qui doit suivre
# immediatement la fin equilibree ; `bounds_anomalies()` le verifie sur tout le
# corpus et `check_invariants.py` en fait un invariant. C'est ce controle qui
# signalerait qu'une grille future a change de gabarit.
#
# Releve de reference (78 + 10 + 126 + 14 + 13 + 10 segments) :
#   annexe-dd    -> `<div class="criteria-row"` 78/78 (m3 x74, m2 x2, m4 x2)
#   redflags     -> `<div class="criterion-comment-section"` 10/10
#   therapy      -> `<div class="therapy-section">` 82, sinon
#                   `<div class="criterion-comment-section"` 44
#   resume       -> `<div class="annexes">` 14/14
#   presentation -> `</div></div>` puis END_MARK (10) ou `<div class="images-wrapper">` (3)
#   annexe-image -> item d'image suivant, ou fin de `images-wrapper`/`annexes-grid`
BLOCKS = [
    # --- blocs loges dans la section notee (niveau 2) ---------------------
    ("annexe-dd", r'<div class="annexe-item annexe-dd">',
     r'<div class="criteria-row"'),
    ("redflags", r'<div class="redflags-section">',
     r'<div class="criterion-comment-section"'),
    ("therapy", r'<div class="therapy-section">',
     r'<div class="therapy-section">|<div class="criterion-comment-section"'),
    # --- fiches pedagogiques de fin de page (niveau 3) ---------------------
    ("resume", r'<div class="resume">', r'<div class="annexes">'),
    # `annexe-theorie` : bloc ABSENT du corpus d'origine (0/88), cree par le
    # chantier des sections pedagogiques. Il est declare ici — et non laisse de
    # cote — parce que sa classe interne `theorie-section` figure dans
    # CONTENT_CLASSES : sans cette entree, `uncovered_content()` la verrait hors
    # de tout bloc et signalerait a juste titre un bloc invisible. Motif de
    # debut et queue attendue repris de `lib_amboss.BLOCKS`, ou le bloc precede
    # toujours la fiche de presentation.
    ("annexe-theorie", r'<div class="annexe-item annexe-theorie">',
     r'<div class="presentation-patient">'),
    ("presentation", r'<div class="presentation-patient">',
     r'(?:</div>\s*)*(?:<div class="images-wrapper">|' + re.escape(END_MARK) + r')'),
    ("annexe-image", r'<div class="annexe-item"(?=[ >])',
     r'(?:</div>\s*)*(?:<div class="annexe-item"(?=[ >])|'
     + re.escape(END_MARK) + r')'),
]

# Classes porteuses de contenu redactionnel. Toute occurrence hors des segments
# de BLOCKS est une ANOMALIE : elle signale un bloc que l'outillage ne voit pas.
# C'est la traduction en controle automatique de l'angle mort d'AMBOSS-34, ou
# une fiche portee par une classe non prevue etait restee invisible et n'avait
# eu pour seul symptome qu'un chiffre de redondance anormalement bas.
CONTENT_CLASSES = [
    "annexe-dd-content", "dd-category",
    "therapy-section", "therapy-title",
    "redflags-section", "redflags-title", "redflags-item", "redflags-text",
    "resume-content", "resume-main-title", "resume-section", "resume-subsection",
    "resume-subsection-points", "resume-bullet", "resume-points", "resume-table",
    "subsection-title",
    "presentation-content", "presentation-main-title", "presentation-section",
    "presentation-section-title", "presentation-subsection", "presentation-points",
    "presentation-qa", "presentation-question", "presentation-reponse",
    "presentation-analyse", "presentation-astuce",
    "qa-container", "q-number", "q-text", "arg-title", "arg-list",
    "reponse-pour", "reponse-contre", "reponse-section", "response-list",
    "mnemo-box", "mnemo-title", "mnemo-items",
    "annexe-description", "annexe-image", "first-col",
]

# `criteria-text`, `detail-text criteria-detail`, `patient-response`,
# `scoring-rule`, `sub-criteria` et `communication-*` sont deliberement absents :
# ils constituent la SECTION NOTEE elle-meme (niveau 2 de la hierarchie), pas un
# bloc de commentaire. `vital-sign`, `missing-items` et `section-title` non plus :
# le premier est le panneau de constantes de l'en-tete, le deuxieme un conteneur
# vide rempli par le JavaScript, le troisieme sert a la fois dans `resume` et
# dans la charpente de page.

_TAG = re.compile(r"<(/?)(\w+)([^>]*)>")


def grids():
    """Chemins des 88 grilles, tries par numero."""
    return sorted(CASES.glob("German-*.html"),
                  key=lambda p: int(re.search(r"German-(\d+)", p.name).group(1)))


def grid_num(path):
    return int(re.search(r"German-(\d+)", Path(path).name).group(1))


def _balanced_end(html, start):
    """Index de fin du `<div>` ouvert en `start`, par equilibrage strict.

    Plus sur qu'un motif de fin : un bloc qui en contient un autre du meme type
    (German-78 porte deux `annexe-dd`) ou qui contient par accident le motif de
    fin d'un voisin ne peut pas tromper l'equilibrage. Les 88 grilles sont
    globalement equilibrees ; en cas d'anomalie locale la fonction rend
    `len(html)`, ce que `bounds_anomalies()` signale.
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
    segments suivants (German-78 et ses deux `annexe-dd`, les 126 `therapy` de
    44 grilles). Utiliser `block_segments()`.
    """
    segments = block_segments(html, name)
    return segments[0] if segments else None


def blocks_present(html):
    """Noms des blocs presents, avec leur nombre de segments : [(nom, n), ...]."""
    return [[name, len(block_spans(html, name))]
            for name, _, _ in BLOCKS if block_spans(html, name)]


def all_spans(html):
    """Tous les segments de tous les blocs, fusionnes et tries."""
    spans = [s for name, _, _ in BLOCKS for s in block_spans(html, name)]
    return sorted(spans)


def peda_bounds(html):
    """Index (debut, fin) de la zone pedagogique de fin de page.

    Debut : `<div class="resume">` si present, sinon `<div class="annexes">`.
    Fin : le commentaire `<!-- COMMENTAIRE GENERAL -->`, present 88/88.
    Retourne (-1, -1) pour les 63 grilles qui n'ont aucune fiche de fin de page
    (leur seul contenu est `annexe-dd`, lu par `dd_bounds()`), ainsi que pour
    les 11 grilles depourvues de tout bloc.
    """
    start = html.find('<div class="resume">')
    if start < 0:
        start = html.find('<div class="annexes">')
    if start < 0:
        return -1, -1
    end = html.find(END_MARK, start)
    return start, (end if end > 0 else len(html))


def dd_bounds(html):
    """Index (debut, fin) du PREMIER bloc `annexe-dd`, pour une lecture ciblee.

    Ce bloc vit dans la section Management, donc avant la zone rendue par
    `peda_bounds()` et sans recouvrement avec elle. Meme convention d'index que
    `peda_bounds()` — des caracteres, a convertir en numeros de ligne pour
    `Read`. Retourne (-1, -1) si le bloc est absent (11 grilles).
    Voir `block_spans(html, "annexe-dd")` pour les obtenir tous.
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
    `redflags-section`, invisibles a une transposition naive de `BLOCKS`.
    """
    spans = all_spans(html)
    out = {}
    for cls in CONTENT_CLASSES:
        pattern = r'class="[^"]*\b' + re.escape(cls) + r'\b[^"]*"'
        for m in re.finditer(pattern, html):
            if not any(a <= m.start() < b for a, b in spans):
                out[cls] = out.get(cls, 0) + 1
    return out


# Items portes par un `<div>` plutot que par un `<li>` ou une puce. Sans cette
# extension, `redflags-section` rendrait zero item : ni `<li>` ni « • ».
_DIV_ITEM = re.compile(
    r'<div class="(?:redflags-text|annexe-description)">(.*?)</div>', re.S)


def list_items(segment, min_len=18):
    """Items normalises d'un segment, filtres sur une longueur minimale.

    Reprend la regle d'AMBOSS — `<li>`, puces « • » a l'interieur d'un `<li>`,
    puces hors `<li>` en jetant la tete sans borne gauche — et y ajoute les
    items portes par un `<div>` de classe dediee.

    Trois formats coexistent dans ce corpus :

    - `<li>` : `resume` (586), `presentation` (710), `annexe-dd` (484, chaque
      `<li>` portant un diagnostic entier decoupe ensuite par ses puces) ;
    - puce « • » separee par des `<br>` hors de tout `<li>` : `therapy-section`
      (499 puces, zero `<li>`). La tete jetee est le `therapy-title`, un
      intitule — coherent avec les `<h5 class="subsection-title">` du `resume`,
      egalement hors item ;
    - `<div class="redflags-text">` (54) et `<div class="annexe-description">`
      (10) : ni liste ni puce.

    Aucun double comptage : les `<div>` d'item ne sont jamais dans un `<li>` et
    ne contiennent pas de puce, les trois sources sont donc disjointes.

    `min_len` vaut 18 comme dans AMBOSS, pour que le chiffre de redondance des
    deux corpus se lise dans la meme unite. Effet de bord assume : un item
    court (« 1. Age > 50 ans », 12 caracteres apres normalisation) sort de la
    mesure — c'est deja le cas dans AMBOSS.
    """
    items = []
    for m in re.finditer(r"<li[^>]*>(.*?)</li>", segment, re.S):
        text = visible_text(m.group(1))
        items += _bullet_items(text) if BULLET in text else [norm(text)]
    for m in _DIV_ITEM.finditer(segment):
        items.append(norm(visible_text(m.group(1))))
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
