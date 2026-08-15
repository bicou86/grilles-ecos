"""Lecture d'une grille -> structure de cas pivot.

Les fonctions `propre`, `sections` et `items` viennent de
`scripts/build_obsidian_memento.py`, ou elles ont ete eprouvees sur les neuf
grilles officielles. Elles sont deplacees ici sans modification : le memento
officiel doit rester identique a l'octet pres.
"""
import html as H
import json
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# LIGNES DE SYNTHESE GLOBALE — du bareme, pas des items a couvrir : elles
# notent la MANIERE (« l'anamnese a-t-elle ete bien conduite ? »), pas un geste
# ou une question. Deux formulations coexistent dans le corpus :
#
#   « Anamnese en general », « Management en general »        (9 officielles)
#   « Évaluation globale de la qualite de l'anamnese »        (RESCOS/GERMAN…)
#
# La seconde branche est ANCREE EN DEBUT DE LIBELLE, et c'est essentiel :
# non ancree, elle emporterait des gestes legitimes. Releve exhaustif du
# corpus (4 665 libelles d'items distincts, 9 108 occurrences) — ce que la
# branche ancree fait tomber, et rien d'autre :
#
#     89x  Évaluation globale de la qualité de l'anamnèse
#     88x  Évaluation globale de la qualité de l'examen clinique
#     85x  Évaluation globale de la qualité de la prise en charge
#      4x  Évaluation globale de la prise en charge
#      1x  Évaluation globale de la démarche téléphonique
#
# et ce qu'elle laisse passer, alors qu'un motif plus gourmand les prendrait :
# « Inspection globale », « Inspection globale du pied en position debout »,
# « Sensibilite des membres inferieurs - evalue globalement la sensibilite... »
# (idem membres superieurs), « Impression generale et proportions », les
# quinze libelles en « Qualite... » et les quatre en « Synthese... ».
# « Appreciation globale » et « qualite globale de » n'existent nulle part.
#
# Les neuf grilles officielles ne portent aucun libelle en « Évaluation
# globale » : leur memento est inchange a l'octet pres (md5 epingle par
# check_fusion.py). Verifie.
SYNTHESE = re.compile(r"\ben g[ée]n[ée]ral|^[ée]valuation globale", re.I)

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

# REPONSES DU·DE LA PATIENT·E RENDUES EN SOUS-CRITERE. Le corpus AZYGOS separe
# les libelles des reponses par la structure de son JSON ; le HTML, lui, n'a
# pas de champ dedie hors du `patient-response` deja retire par `propre()`.
# Des reponses s'y glissent donc parmi les sous-criteres : « TA 138/85 mmHg »,
# « Pas de turgescence jugulaire », « Murmure vesiculaire normal ».
#
# LE CRITERE EST ADOSSE AU REFERENTIEL, pas invente : les neuf grilles
# officielles ne portent AUCUNE valeur chiffree avec unite et AUCUN « normal »,
# et leurs quatre negations sont soit des items de TETE (« Absence de
# symptomes entre les crises »), soit une ligne didactique qui ne COMMENCE pas
# par la negation (« Pour le zona : pas de contage… »). Trois consequences,
# toutes verifiees sur les neuf grilles — le memento officiel est inchange a
# l'octet pres :
#
#   1. la regle ne s'applique qu'aux SOUS-criteres, jamais aux items de tete ;
#   2. la negation doit etre EN DEBUT de libelle ;
#   3. un libelle qui porte un « : » est epargne — le deux-points introduit une
#      echelle, une plage ou un seuil (« Classe I: Activites quotidiennes
#      normales », « Normal: 0.9-1.3 », « Odeur : normale - tres malodorante »),
#      jamais un constat nu.
#
# La valeur chiffree n'est retenue que HORS PARENTHESES : entre parentheses,
# elle precise un libelle legitime (« Interpretation du test (chute ≥20/10
# mmHg) », « Betabloquant (bisoprolol 5mg/j) ») au lieu d'etre le constat.
#
# « Sans… » a ete ecarte du motif a dessein : il aurait emporte « Sans
# correction » (une modalite d'examen visuel) pour ne gagner qu'une reponse.
_REPONSE_NEGATION = re.compile(r"^(?:pas d[e’']|absence d[e’']|aucune?\b)", re.I)
_REPONSE_NORMAL = re.compile(r"\b(?:normale?s?|normaux)\b", re.I)
_REPONSE_VALEUR = re.compile(
    r"\d\s*(?:mmHg|kg/m²|kg|cm|mm|°C|bpm|mg|ml|mL|mmol|µmol|%|/min|/mn)\b")
_PARENTHESES = re.compile(r"\([^)]*\)")


def reponse_patient(libelle):
    """Vrai si ce SOUS-critere enonce une reponse et non un geste a couvrir."""
    if ":" in libelle:
        return False
    if _REPONSE_NEGATION.match(libelle) or _REPONSE_NORMAL.search(libelle):
        return True
    return bool(_REPONSE_VALEUR.search(_PARENTHESES.sub(" ", libelle)))


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
        cid = m.group(2)
        # Le filtre des reponses ne vaut QUE pour l'anamnese et le status. La
        # section management dit la meme chose avec les memes mots sans que ce
        # soit une reponse : « Ceftriaxone 500mg IM » est une prescription,
        # « U - Uree > 7 mmol/L » un critere de CURB-65, « Pas d'indication
        # antibiotique » et « Pas d'imagerie en urgence si le tableau est
        # typique » des decisions — cette derniere figure d'ailleurs, presque
        # mot pour mot, en item de TETE du memento officiel (RESCOS-70b).
        # Mesure a l'appui : le filtre non restreint coutait 25 libelles
        # legitimes, dont 24 en management.
        sous = [x for x in sous
                if x and not (cid[:1] in "ae" and reponse_patient(x))]
        lignes.append(("item", cid, titre, harmonise(sous)))
    return lignes


# Une station double porte le meme numero sur ses deux grilles : sans le rang,
# « RESCOS-64 - Toux - Station double 1 » et « ... Station double 2 » rendent
# le meme identifiant. Les deux grilles restent alors indiscernables partout
# ou un cas est designe par son identifiant — et comme l'appariement retient
# les cas dans un `set`, un item present dans les deux ne serait compte qu'une
# fois (« 13/14 » pour une SSP qui porte bien 14 grilles). Le rang est donc
# repris dans l'identifiant : RESCOS-64-1 et RESCOS-64-2.
_STATION_DOUBLE = re.compile(r"Station double (\d+)", re.I)


def identifiant(chemin):
    """« AMBOSS-1 », « German-45 » ou « RESCOS-64-2 » depuis un nom de fichier.

    Ancre en debut de nom : le prefixe de corpus (une majuscule initiale,
    puis des lettres quelconques — AMBOSS, German, RESCOS, AZYGOS...) suivi
    d'un numero et, pour certains corpus, d'un suffixe d'une lettre. Le rang
    de station double, quand il est present, est ajoute en fin (voir
    _STATION_DOUBLE).
    """
    nom = Path(chemin).name
    m = re.match(r"([A-Z][A-Za-z]*-\d+[a-z]?)", nom)
    if not m:
        return Path(chemin).stem[:40]
    rang = _STATION_DOUBLE.search(nom)
    return f"{m.group(1)}-{rang.group(1)}" if rang else m.group(1)


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


# Les onglets AZYGOS, ramenes aux trois sections du memento. « Diagnostic »,
# « Prise en charge », « Conduite (a tenir) », « Raisonnement clinique » et
# leurs variantes portent les examens complementaires et le raisonnement :
# tous alimentent le management. Certains cas sont des stations en deux
# parties dont les onglets portent un prefixe "Partie 1\n"/"Partie 2\n" et
# nomment l'examen clinique autrement ("Statut clinique", "Status clinique",
# "Etat clinique") : on normalise ce prefixe avant de chercher.
#
# Un onglet du JSON qui n'est ni dans cette table, ni dans les exclusions
# ci-dessous, est un onglet inconnu : check_azygos.py doit echouer plutot
# que de le laisser disparaitre silencieusement.
ONGLETS_AZYGOS = {
    "Anamnèse": "a",
    "Examen clinique": "e", "Statut clinique": "e", "Status clinique": "e",
    "État clinique": "e",
    "Diagnostic": "m", "Diagnostics": "m", "Diagnostique": "m",
    "Procédure": "m", "Prise en charge": "m",
    "Conduite": "m", "Conduite à tenir": "m", "Conseil & Procédure": "m",
    "Raisonnement clinique": "m", "Clinical Reasoning": "m",
}

# Onglets qui ne portent ni anamnese, ni examen, ni management — presentation
# orale du cas et communication avec l'examinateur, ou pur habillage
# (infos du cas, preparation). Volontairement hors des trois sections.
ONGLETS_AZYGOS_EXCLUS = {
    "Infos du cas", "Préparation", "Présentation de cas",
    "Communication", "Communication Poste 1", "Communication poste 1",
    "Communication Poste 2", "Communication poste 2",
}

_PREFIXE_PARTIE = re.compile(r"^Partie \d+\n")


def normalise_onglet(nom):
    """Nom d'onglet AZYGOS sans son prefixe de partie ("Partie 1\\n...")."""
    return _PREFIXE_PARTIE.sub("", nom)


_FICHIERS_AZYGOS = None


def _numero_azygos(nom_fichier):
    """Identifiant AZYGOS d'un JSON, depuis la table docs/azygos-fichiers.yaml.

    Les JSON sont nommes par UUID ; `meta` ne porte pas le numero de grille.
    La table a ete construite une fois pour toutes en appariant les titres.
    """
    global _FICHIERS_AZYGOS
    if _FICHIERS_AZYGOS is None:
        import lib_yaml
        _FICHIERS_AZYGOS = lib_yaml.lire_plat(REPO / "docs" / "azygos-fichiers.yaml")
    return _FICHIERS_AZYGOS.get(nom_fichier)


def classifie_onglets(chemin):
    """Classe les onglets bruts d'un JSON AZYGOS.

    Sert de garde-fou a check_azygos.py : renvoie `candidats`, qui associe
    chaque section (a/e/m) presente aux noms d'onglets qui l'alimentent, et
    `inconnus`, la liste des noms d'onglets qui ne sont ni dans
    ONGLETS_AZYGOS ni dans ONGLETS_AZYGOS_EXCLUS — un onglet inconnu doit
    faire echouer le checker plutot que de disparaitre en silence.
    """
    chemin = Path(chemin)
    donnees = json.loads(chemin.read_text(encoding="utf8"))
    candidats, inconnus = {}, []
    for onglet in donnees["onglets"]:
        nom = normalise_onglet(onglet)
        prefixe = ONGLETS_AZYGOS.get(nom)
        if prefixe is not None:
            candidats.setdefault(prefixe, []).append(onglet)
        elif nom not in ONGLETS_AZYGOS_EXCLUS:
            inconnus.append(onglet)
    return candidats, inconnus


def lire_azygos(chemin):
    """Extraction JSON AZYGOS -> structure de cas pivot.

    Le HTML d'AZYGOS fond le libelle court et le paragraphe didactique dans un
    meme `detail-text` de 100 a 250 mots. Le JSON garde la separation : les
    `label` sont les items, les paragraphes vivent a part dans `infos` et ne
    sont pas repris.

    LES `valeurs` NE SONT PAS DES SOUS-CRITERES — ce sont les reponses du·de
    la patient·e, et elles ne sont donc pas reprises non plus. Le JSON separe
    les deux natures par la structure, pas par une heuristique de longueur :
    scripts/azygos/extract.js prend le libelle dans `span.font-medium` et les
    `valeurs` dans les `<p>` du meme conteneur, qui portent le texte de la
    reponse (« Aucune allergie connue. », « 5/10 au repos, 8/10 a la
    marche. »). Verifie sur le corpus : 2 valeurs sur 4 973 coincident avec
    un libelle d'item existant ailleurs, et les deux se lisent comme des
    reponses en contexte.

    Les vrais sous-criteres ne sont pas perdus pour autant : ils sont deja
    des items a part entiere de la meme liste. `nbEnfants` compte les
    libelles imbriques dans le conteneur, et ces enfants suivent le parent
    comme freres — « Noxes » (nbEnfants=3) est suivi de « Tabac », « Alcool »
    et « Drogues », dont il ne fait qu'agreger les reponses (verifie : 442
    parents sur 492 ont exactement pour `valeurs` la concatenation de celles
    de leurs n suivants). Aucune reconstruction de hierarchie n'est tentee
    ici : `nbEnfants` deborde du groupe pour 46 parents sur 538, ce qui en
    fait un compteur d'affichage, pas un compte d'enfants fiable.
    """
    chemin = Path(chemin)
    donnees = json.loads(chemin.read_text(encoding="utf8"))
    ident = _numero_azygos(chemin.name) or donnees["meta"]["id"][:8]
    sections_out = {}
    for onglet, groupes in donnees["onglets"].items():
        prefixe = ONGLETS_AZYGOS.get(normalise_onglet(onglet))
        if prefixe is None:
            continue
        lignes = sections_out.setdefault(prefixe, [])
        for groupe in groupes:
            if not isinstance(groupe, dict):
                continue
            nom = (groupe.get("groupe") or "").strip()
            if nom:
                lignes.append(("titre", None, nom, None))
            for rang, item in enumerate(groupe.get("items", [])):
                titre = (item.get("label") or "").strip()
                if not titre:
                    continue
                cid = f"{prefixe}{len(lignes) + 1}"
                lignes.append(("item", cid, titre, []))
    return {
        "id": ident,
        "corpus": "azygos",
        "fichier": str(chemin.relative_to(REPO)),
        "ssp": None,
        "diagnostic": None,
        "confiance": "absent",
        "sections": {k: v for k, v in sections_out.items() if v},
    }
