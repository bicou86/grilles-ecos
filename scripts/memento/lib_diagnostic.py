"""Resolution du diagnostic d'un cas, par cascade a cinq niveaux.

Aucun champ ne porte le diagnostic. On tente, du plus fiable au moins :

  1. explicite          — critere « Hypothese diagnostique : X » du management
  2. corrige            — bloc pedagogique <h4>Diagnostic</h4> de GERMAN,
                           le seul corpus qui porte une reponse dediee et
                           distincte du differentiel generique (niveau 4)
  3. dd-principal       — premiere entree d'une categorie dd-category que la
                           grille intitule elle-meme « Diagnostic principal »
                           (ou « Cause principale ») : la grille DIT que cette
                           entree est le diagnostic retenu, elle n'est pas
                           supposee telle
  4. premier-dd         — premiere entree du bloc pedagogique dd-category,
                           quelle que soit l'intitule de la categorie : REPLI
                           NON VERIFIE, cf. ci-dessous
  5. diagnostic-travail — label « Diagnostic de travail » du JSON AZYGOS

Deux niveaux ne sont pas produits par la cascade et se posent a la main :
  - deduit  — aucun niveau n'a rien donne, il a fallu lire la grille ;
  - enonce  — la grille NOMME son diagnostic ailleurs que dans les sources
              ci-dessus (presentation orale du cas, bloc « Diagnostic le plus
              probable »), et cette valeur-la a ete retenue apres relecture.
Le niveau confirme marque, lui, une valeur relue et validee par l'auteur.

POURQUOI premier-dd EST UN REPLI ET NON UNE REGLE. « S'il n'y a pas
d'hypothese explicite, c'est le premier diagnostic differentiel » a ete
valide sur AMBOSS-1, ou le bloc dd-category est personnalise par vignette.
Il est FAUX partout ou ce bloc liste le differentiel GENERIQUE de la plainte :
sur GERMAN il produit de vraies inversions (« Fibroadenome » pour un carcinome
mammaire, German-62 ; « Pheochromocytome » pour une perimenopause, German-6),
et sur RESCOS aussi (« Cholangite » pour une cholecystite, RESCOS-18 —
la vignette dit quatre fois « cholecystite »). Ce que la grille signale
elle-meme, en revanche, est fiable : quand le <h4> de la premiere categorie
annonce « Diagnostic principal », l'entree qui suit EST la reponse, et c'est
le niveau 3. Le niveau 4 ne subsiste que pour les grilles ou aucune source
dediee n'existe — et `hypotheses_enoncees()` sert a check_diagnostic.py pour
refuser toute valeur de niveau 3 ou 4 que la grille contredit.

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
# jamais s'y meler dans la VALEUR.
#
# Il porte en revanche l'information decisive sur la FIABILITE de cette
# valeur. Deux familles d'intitules, deux statuts :
#
#   « Diagnostic principal », « Cause principale », « Diagnostic principal -
#   Urgence chirurgicale » : la grille DESIGNE cette entree comme la reponse
#   retenue. Fiable (niveau dd-principal).
#
#   « Causes hepatobiliaires », « Origine uro-genitale »,
#   « Spondylarthropathies inflammatoires » : intitule THEMATIQUE. La premiere
#   entree n'est que la premiere d'une famille, pas la reponse — c'est la que
#   naissent les inversions (RESCOS-18 « Cholangite » alors que la vignette
#   dit quatre fois cholecystite). Repli non verifie (niveau premier-dd).
#
# Releve du corpus : les 1 485 dd-category des sept corpus HTML ont toutes un
# <h4> immediatement apres l'ouverture du div, sans exception — la capture ne
# peut pas rater et rendre un bloc muet.
DD_CATEGORIE = re.compile(r'<div class="dd-category">\s*<h4>(.*?)</h4>', re.S)
DD_PREMIER = re.compile(r'<li>\s*<strong[^>]*>(.*?)</strong>', re.S)

# Intitule de categorie qui DESIGNE la reponse au lieu de nommer une famille.
# Ancre en debut d'intitule : « Diagnostics differentiels a considerer » ne
# doit pas passer, « Diagnostic principal - Urgence chirurgicale » doit.
DD_PRINCIPALE = re.compile(r"^(?:diagnostic|cause|hypoth[èe]se)s?\s+principale?s?\b", re.I)

# GERMAN seulement : le bloc pedagogique <h4>Diagnostic</h4> nomme le
# diagnostic RETENU pour cette vignette precise (le « corrige »), dans le
# <p> qui suit immediatement. Le nom lui-meme est porte par un
# <span class="c-red"> de ce paragraphe — les spans qui precedent (c-pink :
# symptome/examen, c-purple : facteur de risque/demographie) ne sont jamais
# le diagnostic. Les 4 fichiers sans ce bloc sont des consultations de
# prevention/counseling sans maladie a nommer (tabac, vaccination, voyage x2).
#
# UN SEUL c-red (60/88 fichiers) : c'est lui, sans ambiguite.
#
# PLUSIEURS c-red (28/88 fichiers) : le premier n'est pas toujours le bon —
# ronde de correction 2/5, German-20 et German-52 avaient une comorbidite ou
# un antecedent etiquete c-red par erreur (fibrillation auriculaire, BPCO)
# AVANT le vrai diagnostic. Quand le paragraphe porte une formule assertive
# du corrige (« le corrige TRAITE/RETIENT/ORIENTE VERS X »), c'est le
# premier c-red qui SUIT cette formule qui est retenu, pas le premier du
# paragraphe. Verifie sur les 28 fichiers a c-red multiples : seuls
# German-18, 20 et 52 portent cette formule ; German-18 avait deja le bon
# diagnostic en premiere position (aucun changement), German-20 et
# German-52 sont corriges par cette regle. Les 25 autres, sans formule,
# gardent le premier c-red — comportement inchange, revalide un par un.
#
# Un verbe plus faible (« le corrige EVOQUE X ou Y », German-50) n'est PAS
# un marqueur : il introduit un differentiel non tranche, pas une reponse
# unique — German-50 garde deliberement son premier c-red (« Syndrome
# nephrotique »), choix explicite et non un effet de bord de la regle.
GERMAN_DIAGNOSTIC_H4 = re.compile(r"<h4>Diagnostic</h4>\s*<p>(.*?)</p>", re.S)
GERMAN_DIAGNOSTIC_SPAN = re.compile(r'<span class="c-red">(.*?)</span>', re.S)
GERMAN_MARQUEUR_CORRIGE = re.compile(r"corrig[ée]\s+(?:traite|retient|oriente\s+vers)", re.I)

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


def _diagnostic_corrige_german(paragraphe):
    """Choisit LE c-red du paragraphe <h4>Diagnostic</h4> de GERMAN.

    Un seul c-red : pas d'ambiguite, c'est lui. Plusieurs : le premier n'est
    pas toujours le bon (une comorbidite ou un antecedent peut y etre
    etiquete c-red par erreur) — si une formule assertive du corrige
    (« traite »/« retient »/« oriente vers ») est presente, le c-red qui la
    SUIT est retenu ; sinon repli sur le premier c-red du paragraphe.
    """
    spans = list(GERMAN_DIAGNOSTIC_SPAN.finditer(paragraphe))
    if not spans:
        return None
    marqueur = GERMAN_MARQUEUR_CORRIGE.search(paragraphe)
    if marqueur:
        for m in spans:
            if m.start() > marqueur.end():
                return m.group(1)
    return spans[0].group(1)


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
    """(diagnostic, confiance). `html_brut` est requis pour les niveaux 2 a 4.

    Renvoie (None, "absent") si aucun des cinq niveaux n'aboutit — a
    completer a la main dans la table avec la confiance « deduit ».

    Le niveau 1 (« explicite ») est reserve aux corpus HTML : AZYGOS nomme
    son diagnostic de travail dans le meme genre d'intitule (« Diagnostic
    presume », « Hypothese diagnostique »...) mais la confiance qui en
    resulte doit rester « diagnostic-travail », propre a ce corpus — cf.
    niveau 5.
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
        # 4) qui n'est PAS fiable sur ce corpus — cf. docstring du module.
        if html_brut and cas["corpus"] == "german":
            m0 = GERMAN_DIAGNOSTIC_H4.search(html_brut)
            if m0:
                brut_span = _diagnostic_corrige_german(m0.group(1))
                if brut_span:
                    nom = _texte(brut_span)
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
                        # Meme valeur, deux confiances : la grille designe
                        # elle-meme cette entree comme la reponse, ou bien
                        # elle ne fait que l'ouvrir une famille thematique.
                        principale = DD_PRINCIPALE.match(_texte(m0.group(1)))
                        return nom, "dd-principal" if principale else "premier-dd"

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


# ---------------------------------------------------------------------------
# TEMOINS : ce que la grille DIT d'elle-meme, hors de la cascade.
#
# Ces sources ne servent pas a produire une valeur (elles rendent la
# formulation de la vignette, pas le nom court d'une maladie : « BPCO
# severe » la ou la table porte « Bronchopneumopathie chronique obstructive
# (BPCO) »). Elles servent a CONTREDIRE une valeur tiree du differentiel —
# c'est le controle de check_diagnostic.py.
#
# CALIBRAGE, par temoin positif. Les 71 valeurs GERMAN de confiance
# « corrige » sont tirees d'une source dediee et ont ete relues ; on demande
# a l'extracteur, sur les 17 grilles GERMAN ou il repond et ou le niveau
# `explicite` ne le devance pas, de retrouver cette valeur : 17 sur 17, zero
# ecart (German-10 « accident vasculaire cerebral », German-52 « cancer
# broncho-pulmonaire », German-8 « cephalee du restaurant chinois »...). Le
# meme extracteur sans restriction de zone — cherchant la formule dans tout
# le document — descend a 16 bons sur 36 : il attrape les « si suspicion
# de… » des criteres de management. D'ou les DEUX zones delimitees
# ci-dessous, et la formule « suspicion de » admise dans la seule zone SBAR,
# ou elle est l'enonce meme de l'evaluation.
ZONE_SBAR = re.compile(r"<p>\s*A\s*\(Assessment\)\s*:(.*?)</p>", re.S | re.I)
ZONE_LONGUE = re.compile(
    r'<div class="presentation-section section-longue">(.*?)</div>\s*</div>', re.S)

# Bloc theorique dedie : 35 grilles AMBOSS et 3 CASECOS portent une reponse
# par vignette sous ce titre exact ; aucune autre grille du corpus ne
# l'emploie. A ne pas confondre avec le <h4>Diagnostic</h4> nu de RESCOS, qui
# introduit une prose generique (« Le diagnostic repose sur la clinique… »).
BLOC_PROBABLE = re.compile(
    r'<div class="theorie-section">\s*<h4>\s*'
    r'Diagnostic(?: le plus probable| principal| final| retenu)\s*</h4>\s*<p>(.*?)</p>', re.S)

_ARTICLE = (r"(?:d['’]\s*|de\s+la\s+|de\s+l['’]\s*|de\s+|du\s+|des\s+"
            r"|une?\s+|le\s+|la\s+|l['’]\s*)?")
_FORMULES = [
    ("hypothèse principale est",
     re.compile(rf"hypoth[èe]se\s+(?:diagnostique\s+)?principale\s+(?:est|serait)\s+{_ARTICLE}", re.I)),
    ("hypothèse principale :",
     re.compile(rf"hypoth[èe]se\s+(?:diagnostique\s+)?principale\s*:\s*{_ARTICLE}", re.I)),
    ("diagnostic principal est",
     re.compile(rf"diagnostic\s+principal\s+est\s+{_ARTICLE}", re.I)),
    ("diagnostic le plus probable",
     re.compile(rf"diagnostic\s+le\s+plus\s+probable\s*(?::|est)\s*{_ARTICLE}", re.I)),
    ("diagnostic final",
     re.compile(rf"diagnostic\s+final\s*:\s*{_ARTICLE}", re.I)),
    ("diagnostic retenu",
     re.compile(rf"diagnostic\s+retenu\s*(?::|est)\s*{_ARTICLE}", re.I)),
]
# « Suspicion de X » est l'enonce meme du A de SBAR (« A (Assessment) :
# Suspicion de cholecystite aigue »). Ailleurs c'est une CONDITION
# (« Scanner thoracique si forte suspicion »), d'ou la restriction.
_FORMULE_SBAR = ("suspicion de", re.compile(rf"\bsuspicion\s+(?:d['’]\s*|de\s+){_ARTICLE}", re.I))

_FIN_ENONCE = re.compile(r"[.;,]|\s+DD\b|\s+avec\b|\s+devant\b|\s+chez\b|\s+sur\s+|\s+mais\b")


def hypotheses_enoncees(html_brut, corpus=None):
    """Ce que la grille nomme elle-meme comme diagnostic retenu.

    Renvoie une liste de (source, enonce), vide si la grille ne dit rien.
    Une liste vide n'est PAS un feu vert : c'est l'absence de temoin, et
    check_diagnostic.py la compte pour ne pas se declarer satisfait d'un
    controle qui n'a rien examine.

    `corpus` conditionne le seul temoin qui ne vaut que pour GERMAN : le
    <h4>Diagnostic</h4> nu. RESCOS (7 grilles) et CASECOS (47) portent le meme
    titre au-dessus d'une prose GENERIQUE (« Le diagnostic repose sur la
    clinique et la confirmation bacteriologique. ») ou l'admettre reviendrait
    a opposer a la valeur retenue un texte qui ne nomme aucun diagnostic.
    """
    out = []
    for nom_zone, rx_zone in (("présentation SBAR", ZONE_SBAR),
                              ("présentation longue", ZONE_LONGUE)):
        m = rx_zone.search(html_brut)
        if not m:
            continue
        zone = _texte(m.group(1))
        formules = list(_FORMULES)
        if rx_zone is ZONE_SBAR:
            formules.insert(0, _FORMULE_SBAR)
        for nom_formule, rx in formules:
            mm = rx.search(zone)
            if not mm:
                continue
            val = _FIN_ENONCE.split(zone[mm.end():])[0].strip(" -–—:()")
            # « X ou Y » n'est pas une reponse unique : un differentiel non
            # tranche ne peut ni confirmer ni contredire (cf. German-50).
            if val and not re.search(r"\bou\b", val, re.I) and len(val.split()) <= 10:
                out.append((f"{nom_zone} « {nom_formule} »", val))
                break
    m = BLOC_PROBABLE.search(html_brut)
    if m:
        out.append(("bloc « Diagnostic le plus probable »", _texte(m.group(1))))
    if corpus == "german":
        m = GERMAN_DIAGNOSTIC_H4.search(html_brut)
        if m:
            out.append(("bloc corrigé <h4>Diagnostic</h4>", _texte(m.group(1))))
    return out


def charger_table():
    return lib_yaml.lire_plat(TABLE)


def signalements_multi_cred():
    """Grilles GERMAN a plusieurs c-red dans <h4>Diagnostic</h4> sans marqueur.

    Recalcule a chaque appel depuis les fichiers HTML (pas une liste figee) :
    detecte a l'avenir tout fichier GERMAN, nouveau ou modifie, ou le
    diagnostic depend d'un choix entre plusieurs c-red que la formule
    assertive du corrige (« traite »/« retient »/« oriente vers ») ne
    tranche pas. Repli mecanique sur le premier c-red pour ces cas-la — pas
    une erreur en soi (souvent correct, cf. ronde de correction 2/5), mais
    une liste a relire plutot qu'un choix silencieux.

    Renvoie une liste triee de (identifiant, nombre de c-red).
    """
    import glob
    import lib_extraction as L

    out = []
    for f in sorted(glob.glob(str(REPO / "cases" / "german" / "*.html"))):
        brut = Path(f).read_text(encoding="utf8", errors="replace")
        m0 = GERMAN_DIAGNOSTIC_H4.search(brut)
        if not m0:
            continue
        spans = list(GERMAN_DIAGNOSTIC_SPAN.finditer(m0.group(1)))
        if len(spans) <= 1:
            continue
        marqueur = GERMAN_MARQUEUR_CORRIGE.search(m0.group(1))
        tranche = marqueur and any(m.start() > marqueur.end() for m in spans)
        if not tranche:
            out.append((L.identifiant(f), len(spans)))
    return sorted(out, key=lambda x: int(re.search(r"\d+", x[0]).group()))


def ecrire_table():
    """Complete la table sans jamais ecraser une valeur deja presente."""
    import glob
    import lib_extraction as L
    import lib_ssp
    from check_couverture import HORS_PERIMETRE

    existant = charger_table()
    out = dict(existant)
    for corpus in lib_ssp.CORPUS:
        motif = L.motif(corpus)
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
              "# confiance : explicite | corrige | dd-principal | premier-dd |",
              "#             diagnostic-travail | enonce | confirme | deduit | absent",
              "# corrige = bloc <h4>Diagnostic</h4> de GERMAN (reponse dediee par vignette).",
              "# dd-principal = 1re entree d'une categorie que la grille intitule",
              "#                elle-meme « Diagnostic principal » / « Cause principale ».",
              "# premier-dd = 1re entree d'une categorie THEMATIQUE : repli non verifie.",
              "# enonce = valeur lue dans ce que la grille enonce elle-meme (presentation",
              "#          orale du cas, bloc « Diagnostic le plus probable », bloc corrige),",
              "#          posee a la main apres relecture — la cascade ne la produit pas.",
              "# Une valeur corrigee a la main n'est jamais ecrasee par une reexecution.",
              "# Cinq grilles sont hors perimetre (cf. HORS_PERIMETRE) et n'apparaissent pas ici.",
              ""]
    # L'identifiant complet ferme la cle de tri : sans lui, « RESCOS-57 » et
    # « RESCOS-57b » sont ex aequo et leur ordre relatif est celui du dict,
    # donc celui du fichier precedent — une entree retiree puis recalculee
    # ressortait ailleurs, et le diff d'une reexecution montrait des
    # deplacements qui n'etaient pas des changements.
    for cid in sorted(out, key=lambda x: (x.split("-")[0],
                                          int(re.search(r"\d+", x).group()), x)):
        lignes.append(f"{cid}: {out[cid]}")
    TABLE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{len(out)} entrées -> {TABLE.relative_to(REPO)}")


if __name__ == "__main__":
    ecrire_table()
