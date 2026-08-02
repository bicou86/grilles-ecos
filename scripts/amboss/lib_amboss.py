"""Fonctions partagées pour le traitement des grilles AMBOSS."""
import re
import unicodedata
from pathlib import Path

CASES = Path(__file__).resolve().parents[2] / "cases" / "amboss"

# Bornes des cinq blocs pédagogiques. L'ordre reflète leur ordre dans le fichier.
# Le bloc "presentation" porte deux variantes de classe : la standard
# `presentation-patient` (24 grilles) et `annexe-item annexe-presentation`
# (AMBOSS-34 seule) — voir PROCEDURE.md § 6, « Angle mort : variante de classe
# non prévue ». Les deux alternatives figurent aussi dans le marqueur de fin de
# "theorie", sans quoi ce bloc engloutirait le contenu de la variante jusqu'à
# `annexe-scenario`.
#
# "annexe-dd" est le seul bloc situé *avant* la zone pédagogique : il est inséré
# dans la section Management, à l'intérieur du `criteria-row` du critère m1
# (« Hypothèses diagnostiques »), dont il commente les hypothèses sans rien
# noter lui-même. Sa fin est le `criteria-row` suivant : vérifié sur les 40
# grilles par équilibrage des `<div>` — la fermeture équilibrée du bloc tombe
# exactement sur `<div class="criteria-row" id="criteria-m2">`, 40 fois sur 40,
# et le bloc ne contient lui-même aucun `criteria-row`. Les deux alternatives
# `annexes` / `resume` ne servent jamais aujourd'hui ; elles bornent la casse si
# une grille future plaçait le bloc en fin de section, sans `criteria-row`
# derrière lui — sans elles, `block_segment` avalerait tout le reste du fichier.
BLOCKS = [
    ("annexe-dd", r'<div class="annexe-item annexe-dd">',
     r'<div class="criteria-row"|<div class="annexes">|<div class="resume">'),
    ("resume", r'<div class="resume">', r'<div class="annexes">'),
    ("expert", r'<div class="annexe-item annexe-expert">',
     r'<div class="annexe-item annexe-theorie">'),
    ("theorie", r'<div class="annexe-item annexe-theorie">',
     r'<div class="presentation-patient">|<div class="annexe-item annexe-presentation">'
     r'|<div class="annexe-item annexe-scenario">'),
    ("presentation", r'<div class="presentation-patient">|<div class="annexe-item annexe-presentation">',
     r'<div class="annexe-item annexe-scenario">'),
]


def grids():
    """Chemins des 40 grilles, triés par numéro."""
    return sorted(CASES.glob("AMBOSS-*.html"),
                  key=lambda p: int(re.search(r"AMBOSS-(\d+)", p.name).group(1)))


def grid_num(path):
    return int(re.search(r"AMBOSS-(\d+)", Path(path).name).group(1))


def strip_base64(html):
    """Remplace les URI de données par un marqueur — 95 % du poids des fichiers."""
    return re.sub(r'data:image[^"]*', "DATAURI", html)


def peda_bounds(html):
    """Index (début, fin) de la zone pédagogique.

    Début : <div class="resume"> si présent, sinon <div class="annexes">.
    Fin : <div class="annexe-item annexe-scenario">, sinon fin du fichier.
    Retourne (-1, -1) si aucune zone pédagogique n'est trouvée.
    """
    start = html.find('<div class="resume">')
    if start < 0:
        start = html.find('<div class="annexes">')
    if start < 0:
        return -1, -1
    end = html.find('<div class="annexe-item annexe-scenario">', start)
    return start, (end if end > 0 else len(html))


def dd_bounds(html):
    """Index (début, fin) du seul bloc `annexe-dd`, pour une lecture ciblée.

    Ce bloc vit dans la section Management, donc **avant** la zone rendue par
    `peda_bounds()` et sans recouvrement avec elle. Il lui faut ses propres
    bornes : élargir `peda_bounds()` jusqu'à l'englober ferait lire, à chaque
    fois, les centaines de lignes de section notée qui les séparent.

    Même convention que `peda_bounds()` — des index de caractères, à convertir
    en numéros de ligne pour `Read` (voir PROCEDURE.md § 1). Retourne (-1, -1)
    si le bloc est absent.
    """
    start = html.find('<div class="annexe-item annexe-dd">')
    if start < 0:
        return -1, -1
    _, end_pat = [(s, e) for n, s, e in BLOCKS if n == "annexe-dd"][0]
    m = re.search(end_pat, html[start + 1:])
    return start, (start + 1 + m.start() if m else len(html))


def blocks_present(html):
    """Noms des blocs pédagogiques présents dans ce fichier."""
    return [name for name, start, _ in BLOCKS if re.search(start, html)]


def block_segment(html, name):
    """Segment HTML d'un bloc, ou None s'il est absent."""
    for bname, start, end in BLOCKS:
        if bname != name:
            continue
        m = re.search(start, html)
        if not m:
            return None
        e = re.search(end, html[m.end():])
        return html[m.start(): m.end() + (e.start() if e else len(html))]
    return None


def visible_text(html):
    """Texte visible : sans balises, sans base64, espaces normalisés.

    Ne retire qu'une vraie balise HTML — un `<` suivi d'un nom de balise
    (lettre ASCII). Un `<[^>]+>` naïf traiterait tout `<` nu comme une
    ouverture de balise, y compris les seuils de laboratoire écrits
    `Hb < 70 g/L (< 90 si coronarien)` : le `<` de « < 70 » ouvrirait alors
    une pseudo-balise que le motif referme sur le prochain `>` réel (celui
    du `</li>`), avalant toute la clause. Voir PROCEDURE.md § 6.
    """
    txt = re.sub(r'</?[a-zA-Z][a-zA-Z0-9]*(?:\s[^>]*?)?/?>', " ", strip_base64(html))
    txt = re.sub(r"&[a-z]+;", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


LIGATURES = str.maketrans({"œ": "oe", "Œ": "oe", "æ": "ae", "Æ": "ae"})


def norm(s):
    """Minuscules, sans accents, sans ponctuation — pour comparer du texte.

    Les ligatures œ et æ n'ont AUCUNE décomposition Unicode : ni NFD ni NFKD
    ne les touchent, ce sont des lettres à part entière et non des ligatures
    de compatibilité comme ﬁ. Sans translittération explicite, le filtre
    [^a-z0-9 ] les remplace par une espace et « œdème » se compare comme
    « deme », « cœur » comme « c ur ». 4045 occurrences dans cases/.
    """
    s = unicodedata.normalize("NFD", s.lower().translate(LIGATURES))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s)).strip()


BULLET = "•"


def _bullet_items(text):
    """Fragments d'un texte à puces « • » : la puce est un séparateur, pas du contenu."""
    return [p for p in (norm(f) for f in text.split(BULLET)) if p]


def list_items(segment, min_len=18):
    """Items de liste normalisés, filtrés sur une longueur minimale.

    Le corpus emploie deux formats de liste, qui peuvent coexister dans un même
    segment :

    - le `<li>` classique — un item par élément ;
    - la **puce textuelle** « • », séparée par des `<br>` à l'intérieur d'un
      seul élément. C'est la forme du bloc `annexe-dd`, où chaque `<li>` porte
      un diagnostic différentiel entier (nom, puis un argument par puce) : ses
      995 puces du corpus sont toutes à l'intérieur d'un `<li>`.

    Un `<li>` qui contient des puces est donc rendu par ses puces **seules**,
    jamais aussi par son texte entier : sinon le même contenu serait compté
    deux fois, une fois groupé et une fois éclaté, et chaque doublon avec un
    autre bloc serait rapporté en double par `report_redundancy.py`.

    Hors `<li>`, seules les puces sont retenues — le texte qui *précède* la
    première puce est jeté, faute de borne gauche : il pourrait sinon s'étendre
    à tout le segment. À l'intérieur d'un `<li>`, cette tête est bornée par
    l'élément lui-même et porte le nom du diagnostic : elle est conservée.

    Rétro-compatible : l'extraction des quatre blocs préexistants est
    inchangée, vérifié item par item sur les 40 grilles. Un seul d'entre eux
    contient des puces (le `resume` d'AMBOSS-34, 6 puces), et chacune y ouvre
    son propre `<li>` — la découpe rend exactement ce que `norm()`, qui efface
    déjà le caractère « • », rendait auparavant.
    """
    items = []
    for m in re.finditer(r"<li[^>]*>(.*?)</li>", segment, re.S):
        text = visible_text(m.group(1))
        items += _bullet_items(text) if BULLET in text else [norm(text)]
    outside = visible_text(re.sub(r"<li[^>]*>.*?</li>", " ", segment, flags=re.S))
    if BULLET in outside:
        items += _bullet_items(outside)[1:]
    return [i for i in items if len(i) >= min_len]
