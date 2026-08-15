"""Lecture d'une grille -> structure de cas pivot.

Les fonctions `propre`, `sections` et `items` viennent de
`scripts/build_obsidian_memento.py`, ou elles ont ete eprouvees sur les neuf
grilles officielles. Elles sont deplacees ici sans modification : le memento
officiel doit rester identique a l'octet pres.
"""
import html as H
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

SYNTHESE = re.compile(r"en g[ée]n[ée]ral", re.I)

# HARMONISATION DE NOMENCLATURE. Les neuf grilles nomment les memes examens
# de trois facons ; un memento qui les compare a besoin d'un vocabulaire
# constant. Ces reecritures ne touchent QUE le memento : les grilles gardent
# le libelle de leur document officiel.
NOMENCLATURE = [
    (r"^Param[èe]tres inflammatoires \(VS ou CRP\)$", "VS / CRP"),
    (r"^Formule sanguine compl[èe]te$", "FSC"),
]

# Sous-items consecutifs a fondre en un seul (meme raison).
FUSIONS = [(["CRP", "VS"], "VS / CRP"), (["VS", "CRP"], "VS / CRP")]

# Un sous-titre qui repete le nom de son encadre n'apporte rien.
REDONDANTS = {"anamnese", "status", "management", "examen clinique"}


def sans_accent(t):
    t = unicodedata.normalize("NFD", t.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def harmonise(libelles):
    """Applique la table de nomenclature puis les fusions."""
    out = []
    for x in libelles:
        for motif, remplacement in NOMENCLATURE:
            x = re.sub(motif, remplacement, x)
        out.append(x)
    for suite, fusion in FUSIONS:
        i = 0
        while i <= len(out) - len(suite):
            if out[i:i + len(suite)] == suite:
                out[i:i + len(suite)] = [fusion]
            else:
                i += 1
    return out


def propre(frag):
    """Texte visible d'un fragment HTML, reponses du patient retirees.

    Deux formes coexistent : la reponse est le plus souvent dans un
    `<span class="patient-response">`, mais quelques lignes la portent en
    clair entre crochets dans le titre — RESCOS-63b, « Contage [2 grandes
    soeurs...] ». Les crochets sont la convention maison pour une reponse :
    les retirer dans les deux cas.
    """
    frag = re.sub(r'<span class="patient-response">.*?</span>', "", frag, flags=re.S)
    frag = re.sub(r"<[^>]+>", " ", frag)
    txt = re.sub(r"\s+", " ", H.unescape(frag)).strip()
    txt = re.sub(r"\s*\[[^\]]*\]", "", txt)
    return re.sub(r"\s+", " ", txt).strip(" :;·-").strip()


def sections(html):
    """Contenu de chaque section notee, indexe par prefixe de critere."""
    out = {}
    for m in re.finditer(r'<div class="section(?: [^"]*)?">(.*?)(?=<!--|\Z)', html, re.S):
        bloc = m.group(1)
        cids = re.findall(r'id="criteria-([aem])\d+"', bloc)
        if cids:
            out.setdefault(cids[0], bloc)
    return out


def items(bloc):
    """(sous-titre | critere) d'une section, dans l'ordre d'affichage."""
    lignes = []
    motif = re.compile(
        r'<div class="criteria-subheader">(.*?)</div>\s*(?=<div class="criteria-(?:row|subheader)")'
        r'|<div class="criteria-row" id="criteria-(\w+)">')
    positions = [(m.start(), m) for m in motif.finditer(bloc)]
    for i, (pos, m) in enumerate(positions):
        if m.group(1) is not None:
            # un sous-titre peut porter une precision imbriquee (la regle de
            # notation) : seul son intitule interesse le memento
            titre = propre(m.group(1).split("<div")[0])
            if (titre and not titre.lower().startswith("consigne")
                    and sans_accent(titre) not in REDONDANTS):
                lignes.append(("titre", None, titre, None))
            continue
        fin = positions[i + 1][0] if i + 1 < len(positions) else len(bloc)
        corps = bloc[pos:fin]
        t = re.search(r'class="criteria-text">(.*?)<button', corps, re.S)
        if not t:
            continue
        titre = propre(t.group(1))
        titre = re.sub(r"^\d+\.\s*", "", titre)
        if SYNTHESE.search(titre):
            continue
        sous = []
        s = re.search(r'class="sub-criteria">(.*?)</div>', corps, re.S)
        if s and propre(s.group(1)):
            sous.append(propre(s.group(1)))
        sous += [propre(d) for d in
                 re.findall(r'class="detail-text criteria-detail">(.*?)</div>', corps, re.S)]
        titre = harmonise([titre])[0]
        lignes.append(("item", m.group(2), titre, harmonise([x for x in sous if x])))
    return lignes


def identifiant(chemin):
    """« AMBOSS-1 » depuis un nom de fichier de grille."""
    nom = Path(chemin).name
    m = re.match(r"([A-Z]+-\d+[a-z]?)", nom)
    return m.group(1) if m else Path(chemin).stem[:40]


def lire_html(chemin):
    """Grille HTML -> structure de cas pivot (ssp et diagnostic a None)."""
    chemin = Path(chemin).resolve()
    texte = unicodedata.normalize("NFC", chemin.read_text(encoding="utf8", errors="replace"))
    corps = texte[texte.index("<body"):]
    return {
        "id": identifiant(chemin),
        "corpus": chemin.parent.name,
        "fichier": str(chemin.relative_to(REPO)),
        "ssp": None,
        "diagnostic": None,
        "confiance": "absent",
        "sections": {p: items(b) for p, b in sections(corps).items()},
    }
