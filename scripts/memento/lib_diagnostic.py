"""Resolution du diagnostic d'un cas, par cascade a quatre niveaux.

Aucun champ ne porte le diagnostic. On tente, du plus fiable au moins :

  1. explicite          — critere « Hypothese diagnostique : X » du management
  2. corrige            — bloc pedagogique <h4>Diagnostic</h4> de GERMAN,
                           le seul corpus qui porte une reponse dediee et
                           distincte du differentiel generique (niveau 3)
  3. premier-dd         — premiere entree du bloc pedagogique dd-category
  4. diagnostic-travail — label « Diagnostic de travail » du JSON AZYGOS

Un cinquieme niveau, deduit, n'est pas produit par la cascade : c'est la
marque que l'utilisateur (ou l'auteur de la table) pose a la main quand
aucun des quatre niveaux ci-dessus n'a rien donne et qu'il a fallu lire la
grille pour proposer un diagnostic.

Pourquoi le niveau 2 est reserve a GERMAN : la regle « premier diagnostic du
bloc dd-category » (niveau 3) a ete validee sur AMBOSS-1, ou ce bloc est
personnalise pour chaque vignette. Sur GERMAN, ce bloc liste le differentiel
GENERIQUE de la plainte (motif de consultation), pas le diagnostic retenu
pour CETTE vignette — l'appliquer aveuglement y produit de vraies inversions
(« Fibroadenome » a la place d'un carcinome mammaire, German-62). GERMAN a en
revanche un bloc dedie, <h4>Diagnostic</h4>, qui n'existe dans aucun autre
corpus : verifie avant premier-dd, jamais apres, sinon le differentiel
generique gagnerait la course.

La table docs/ecos-diagnostics.yaml est CUREE : une valeur corrigee a la main
doit survivre a une reexecution. La cascade ne remplit que les entrees
absentes.
"""
import html as H
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml

REPO = Path(__file__).resolve().parents[2]
TABLE = REPO / "docs" / "ecos-diagnostics.yaml"

# Intitules de critere qui annoncent LE diagnostic (au singulier — un
# intitule au pluriel, « Diagnostics differentiels », introduit une liste de
# possibilites, pas une reponse unique, et n'est jamais retenu ici).
_TRIGGER = r"hypoth[èe]se diagnostique(?: principale)?|diagnostic principal|diagnostic de suspicion"

# Forme en ligne : « Hypothese diagnostique (principale) : X », « ... - X »,
# ou une formulation en prose « Evoque le diagnostic (principal) de/d'X ».
# Le dernier membre de l'alternative (« diagnostic » nu) ne doit jamais
# absorber « diagnostic differentiel(s) », ni — quand rien de plus ne suit —
# se replier sur le « de » de « diagnostic de suspicion » lui-meme : sans la
# seconde negation, un titre isole « Diagnostic de suspicion » (sans valeur)
# echoue sur l'alternative dediee (pas de separateur apres) puis retombe sur
# le « diagnostic » nu, dont le separateur "de\s+" reprend alors le "de" du
# trigger et capture le seul mot "suspicion" comme s'il etait le diagnostic.
EXPLICITE_LIGNE = re.compile(
    rf"(?:{_TRIGGER}|diagnostic(?!s?\s+diff[ée]rentiel)(?!\s+de\s+suspicion\b))"
    r"\s*(?:[:\-–]\s*|d['’]\s*|de\s+)(.+)", re.I)

# Forme en sous-item : le titre EST l'intitule, sans rien apres ; la valeur
# est le premier sous-item (les suivants sont des precisions du meme
# diagnostic, pas des alternatives — cf. « Fracture de l'humerus / Spiroide
# / De diaphyse... »).
EXPLICITE_TITRE = re.compile(rf"^(?:{_TRIGGER})$", re.I)

# Le premier diagnostic du bloc pedagogique « Diagnostics differentiels a
# considerer » est toujours porte par le <strong> du premier <li> d'une
# categorie dd-category — le <h4> qui precede est le nom de la CATEGORIE
# (« Spondylarthropathies inflammatoires »), pas un diagnostic, et ne doit
# jamais s'y meler.
DD_CATEGORIE = re.compile(r'<div class="dd-category">')
DD_PREMIER = re.compile(r'<li>\s*<strong[^>]*>(.*?)</strong>', re.S)

# GERMAN seulement : le bloc pedagogique <h4>Diagnostic</h4> nomme le
# diagnostic RETENU pour cette vignette precise (le « corrige »), dans le
# <p> qui suit immediatement. Le nom lui-meme est toujours porte par le
# premier <span class="c-red"> de ce paragraphe — les spans qui precedent
# (c-pink : symptome/examen, c-purple : facteur de risque/demographie) ne
# sont jamais le diagnostic ; verifie sur 84/88 fichiers GERMAN. Les 4
# fichiers sans ce bloc sont des consultations de prevention/counseling
# sans maladie a nommer (tabac, vaccination, voyage x2).
GERMAN_DIAGNOSTIC_H4 = re.compile(r"<h4>Diagnostic</h4>\s*<p>(.*?)</p>", re.S)
GERMAN_DIAGNOSTIC_SPAN = re.compile(r'<span class="c-red">(.*?)</span>', re.S)

# Qualificatif de raisonnement colle au nom dans le span (« carcinome
# vesical A EXCLURE ») : ce n'est pas le nom du diagnostic, a retirer.
_QUALIFICATIF_CORRIGE = re.compile(r"\s+(?:[àa]\s+exclure|[àa]\s+confirmer)\s*$", re.I)

# AZYGOS nomme son diagnostic de travail sous plusieurs intitules equivalents
# selon la station (« Diagnostic de travail », « Diagnostic presume »,
# « Hypothese diagnostique »...) : rechercher n'importe lequel, contrairement
# au niveau 1 qui exige un intitule EXACT (rien d'autre dans le titre).
AZYGOS_TRAVAIL = re.compile(rf"diagnostic de travail|diagnostic pr[ée]sum[ée]|{_TRIGGER}", re.I)


def _texte(fragment):
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", H.unescape(fragment)).strip()


def _raccourci(nom):
    """Retire un complement explicatif pour ne garder que le nom de maladie.

    Le <strong>/<span> du premier diagnostic porte parfois, en plus du nom,
    une explication qui allonge la phrase au-dela d'un intitule de
    diagnostic ( « Hypothyroidie : Fatigue, prise de poids, bradycardie... »,
    « Syndrome du rond pronateur [Compression du nerf median...] »,
    « Psoriasis : Plaques erythemato-squameuses bien delimitees, ... » ).

    Deux familles de separateur, deux regles :
    - « : », « — » (tiret cadratin) et « [ » introduisent TOUJOURS une
      explication, jamais une abreviation attachee au nom : on tronque a
      leur premiere occurrence sans condition de longueur — un nom deja
      court comme « Psoriasis : Plaques... » (huit mots au total) doit
      quand meme perdre son explication.
    - « ( » et « / » sont ambigus : une parenthese peut porter une
      abreviation qui fait partie du nom ( « Syndrome coronarien aigu
      (SCA) » ), un tiret cadratin place APRES elle doit rester prioritaire
      ( « Exantheme subit (HHV-6/7) — hypothese principale » -> tronque au
      tiret cadratin, la parenthese est conservee). Ces deux-la ne sont
      tronques que si le nom brut depasse le seuil de huit mots.
    """
    nom = nom.strip(" .:")
    for sep in (":", "—", "["):
        if sep in nom:
            court = nom.split(sep, 1)[0].strip(" .:—")
            if court:
                return court
    if len(nom.split()) <= 8:
        return nom
    for sep in ("(", "/"):
        if sep in nom:
            court = nom.split(sep, 1)[0].strip(" .:")
            if court and len(court.split()) <= 8:
                return court
    return nom


def resoudre(cas, html_brut=None):
    """(diagnostic, confiance). `html_brut` est requis pour les niveaux 2 et 3.

    Renvoie (None, "absent") si aucun des quatre niveaux n'aboutit — a
    completer a la main dans la table avec la confiance « deduit ».

    Le niveau 1 (« explicite ») est reserve aux corpus HTML : AZYGOS nomme
    son diagnostic de travail dans le meme genre d'intitule (« Diagnostic
    presume », « Hypothese diagnostique »...) mais la confiance qui en
    resulte doit rester « diagnostic-travail », propre a ce corpus — cf.
    niveau 4.
    """
    if cas["corpus"] != "azygos":
        for lignes in cas["sections"].values():
            for genre, _, titre, sous in lignes:
                if genre != "item":
                    continue
                m = EXPLICITE_LIGNE.search(titre)
                if m:
                    diag = _raccourci(m.group(1))
                    if len(diag.split()) <= 8:
                        return diag, "explicite"
                if sous and EXPLICITE_TITRE.match(titre.strip()):
                    diag = _raccourci(sous[0])
                    if diag and len(diag.split()) <= 8:
                        return diag, "explicite"

        # Niveau 2 : GERMAN seulement, avant le premier-dd generique (niveau
        # 3) qui n'est PAS fiable sur ce corpus — cf. docstring du module.
        if html_brut and cas["corpus"] == "german":
            m0 = GERMAN_DIAGNOSTIC_H4.search(html_brut)
            if m0:
                m1 = GERMAN_DIAGNOSTIC_SPAN.search(m0.group(1))
                if m1:
                    nom = _texte(m1.group(1))
                    nom = _QUALIFICATIF_CORRIGE.sub("", nom)
                    nom = _raccourci(nom)
                    if nom and len(nom.split()) <= 8:
                        return nom, "corrige"

        if html_brut:
            m0 = DD_CATEGORIE.search(html_brut)
            if m0:
                bloc = html_brut[m0.end():m0.end() + 4000]
                m = DD_PREMIER.search(bloc)
                if m:
                    nom = _raccourci(_texte(m.group(1)))
                    if nom and len(nom.split()) <= 8:
                        return nom, "premier-dd"

    if cas["corpus"] == "azygos":
        for lignes in cas["sections"].values():
            for genre, _, titre, sous in lignes:
                if genre == "item" and sous and AZYGOS_TRAVAIL.search(titre):
                    # Champ dedie, pas une extraction fragile : contrairement
                    # aux niveaux precedents, on ne rejette pas une valeur
                    # de plus de huit mots — ce champ EST la reponse, quitte
                    # a rester long (ex. « Colique nephretique due a un
                    # calcul ureteral distal gauche, non compliquee »).
                    diag = sous[0].strip(" .")
                    if diag:
                        return diag, "diagnostic-travail"

    return None, "absent"


def charger_table():
    return lib_yaml.lire_plat(TABLE)


def ecrire_table():
    """Complete la table sans jamais ecraser une valeur deja presente."""
    import glob
    import lib_extraction as L
    import lib_ssp
    from check_couverture import HORS_PERIMETRE

    existant = charger_table()
    out = dict(existant)
    for corpus in lib_ssp.CORPUS:
        motif = (str(REPO / ".azygos-extraction" / "*.json") if corpus == "azygos"
                 else str(REPO / "cases" / corpus / "*.html"))
        for f in sorted(glob.glob(motif)):
            if corpus == "azygos":
                cas, brut = L.lire_azygos(f), None
            else:
                cas = L.lire_html(f)
                brut = Path(f).read_text(encoding="utf8", errors="replace")
            if cas["id"] in HORS_PERIMETRE or cas["id"] in existant:
                continue
            diag, confiance = resoudre(cas, brut)
            out[cas["id"]] = f"{diag or ''} | {confiance}"

    lignes = ["# Diagnostic de chaque cas — TABLE CUREE.",
              "# Forme : IDENTIFIANT: Diagnostic | confiance",
              "# confiance : explicite | corrige | premier-dd | diagnostic-travail | deduit | absent",
              "# corrige = bloc <h4>Diagnostic</h4> de GERMAN (reponse dediee par vignette).",
              "# Une valeur corrigee a la main n'est jamais ecrasee par une reexecution.",
              "# RESCOS-7 et RESCOS-4 sont hors perimetre (cf. HORS_PERIMETRE) et n'apparaissent pas ici.",
              ""]
    for cid in sorted(out, key=lambda x: (x.split("-")[0], int(re.search(r"\d+", x).group()))):
        lignes.append(f"{cid}: {out[cid]}")
    TABLE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{len(out)} entrées -> {TABLE.relative_to(REPO)}")


if __name__ == "__main__":
    ecrire_table()
