"""Fonctions partagées pour le traitement des grilles AMBOSS."""
import re
import unicodedata
from pathlib import Path

CASES = Path(__file__).resolve().parents[2] / "cases" / "amboss"

# Bornes des quatre blocs pédagogiques. L'ordre reflète leur ordre dans le fichier.
BLOCKS = [
    ("resume", r'<div class="resume">', r'<div class="annexes">'),
    ("expert", r'<div class="annexe-item annexe-expert">',
     r'<div class="annexe-item annexe-theorie">'),
    ("theorie", r'<div class="annexe-item annexe-theorie">',
     r'<div class="presentation-patient">|<div class="annexe-item annexe-scenario">'),
    ("presentation", r'<div class="presentation-patient">',
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
    """Texte visible : sans balises, sans base64, espaces normalisés."""
    txt = re.sub(r"<[^>]+>", " ", strip_base64(html))
    txt = re.sub(r"&[a-z]+;", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def norm(s):
    """Minuscules, sans accents, sans ponctuation — pour comparer du texte."""
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s)).strip()


def list_items(segment, min_len=18):
    """Items <li> normalisés, filtrés sur une longueur minimale."""
    items = [norm(visible_text(x))
             for x in re.findall(r"<li[^>]*>(.*?)</li>", segment, re.S)]
    return [i for i in items if len(i) >= min_len]
