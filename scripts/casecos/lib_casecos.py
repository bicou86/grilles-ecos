"""Fonctions partagees pour le traitement des grilles CasECOS (198 grilles).

ARCHITECTURE — ce qui est importe, ce qui est redefini
------------------------------------------------------
Meme etoile que `scripts/rescos/lib_rescos.py` et `scripts/german/lib_german.py`,
pour la meme raison : `scripts/amboss/lib_amboss.py` est la RACINE partagee, les
trois autres corpus en sont des FEUILLES. Rien n'est ecrit dans `scripts/amboss/`,
`scripts/german/` ni `scripts/rescos/` : leurs mesures publiees (AMBOSS 147 paires
inter-blocs, RESCOS 127) sont inchangees par construction.

Sont IMPORTEES de `scripts/amboss/lib_amboss.py`, par chemin explicite :
`strip_base64`, `visible_text`, `norm`, `BULLET`, `_bullet_items`. Elles ne
dependent d'aucune particularite de corpus — elles nettoient du HTML et
normalisent du francais — et chacune porte un correctif durement acquis, au
premier rang duquel le CHEVRON NU (`Hb < 70 g/L`) que `visible_text` ne consomme
plus. Sont egalement importees la table `BANNED` (`check_nomenclature`) et la
simulation de `cases/scoring.js` (`check_reachability`), voir ces scripts.

Est REDEFINI ici tout ce qui DECRIT le corpus : `CASES`, `BLOCKS`,
`CONTENT_CLASSES`, `grids()`, les bornes (`_balanced_end`, `block_spans`,
`peda_bounds`, `dd_bounds`, `bounds_anomalies`, `uncovered_content`) et
`list_items()`.

POURQUOI `_balanced_end` N'EST PAS RECOPIE DE `lib_rescos` : LE CHEVRON NU
--------------------------------------------------------------------------
C'est le seul ecart de fond avec le portage RESCOS, et il n'est pas cosmetique.
L'equilibrage de `<div>` de `lib_german` et `lib_rescos` repose sur le motif de
balise `<(/?)(\\w+)([^>]*)>`. Or `\\w` COMPREND LES CHIFFRES : sur un seuil ecrit
en clair juste avant une fermeture —

    ... cancers intra-muqueux (T1a) <2 cm, bien differencies</div>

— le motif reconnait une pseudo-balise nommee « 2 » qui s'etend jusqu'au `>` du
`</div>` suivant. La balise fermante est AVALEE, la profondeur ne redescend
jamais, et le bloc engloutit tout ce qui suit.

Mesure sur les 198 grilles CasECOS, motif naif contre motif corrige :

                                    `\\w+`      `[a-zA-Z][a-zA-Z0-9]*`
    segments debordant l'END_MARK       9                          0
    imbrications bloc-dans-bloc       244                          0
    queues distinctes (annexe-dd)       7                          3
    queues distinctes (therapy)        12                          3
    queues distinctes (redflags)        7                          1

Le motif corrige — celui de `visible_text`, un `<` suivi d'une LETTRE ASCII —
rend le corpus parfaitement regulier : zero debordement, zero imbrication, et
une poignee de queues stables par bloc. C'est exactement le meme correctif que
celui de `visible_text`, applique au meme piege, un etage plus bas.

Ce bug est LATENT dans `lib_german` et `lib_rescos`. Il n'y produit AUCUN effet
mesurable aujourd'hui, verifie et non suppose : sur les 41 grilles RESCOS, les
deux motifs rendent des bornes IDENTIQUES sur les 313 segments de `BLOCKS`. Le
corpus RESCOS porte pourtant 9 chevrons nus numeriques precedant un `</div>` (et
AMBOSS 8) — aucun ne tombe sur une frontiere de bloc. CasECOS en porte 364, et
c'est ce qui fait la difference. `lib_amboss` n'emploie d'ailleurs pas
d'equilibrage du tout : ses blocs sont bornes par motif de fin.

German n'a pas ete mesure : son outillage est en cours de modification par
ailleurs et ses chiffres bougent. Corriger l'un ou l'autre est un refactor a
part entiere ; il n'entrait pas dans le perimetre de cette tache. Le bon point
de chute reste un module partage (`scripts/lib_grilles.py`) d'ou les corpus
tireraient l'equilibrage.

DIFFERENCES STRUCTURELLES AVEC AMBOSS ET RESCOS (mesurees sur les 198 grilles)
------------------------------------------------------------------------------
* AUCUN bloc `resume` (0/198) — le corpus n'a pas de fiche de synthese. La
  source canonique du contrat des trois corpus precedents n'existe pas ici.
* AUCUN bloc `presentation-patient` (0/198). La quatrieme fiche de fin de page
  est `annexe-defi` (« Defi pedagogique », 195/195) : une situation qui derape
  — refus de soins, aggravation, question imprevue — suivie du « type de
  reponse attendue ». Ce n'est PAS l'homologue de `presentation-patient`
  d'AMBOSS, qui est un jeu de questions/reponses d'annonce au patient.
* `annexe-nu` — variante de classe INEDITE : AMC-Psy-P10 porte une CINQUIEME
  fiche sous `<div class="annexe-item">` nu (« Scenario Mere Standardisee », le
  script d'anamnese collaterale). Sans entree dans `BLOCKS`, cette fiche
  entiere serait invisible : c'est l'angle mort d'AMBOSS-34, retrouve ici.
* `exemples` — bloc INEDIT (`<div class="exemples-phrases">`, 383 segments sur
  190 grilles) : des phrases modeles d'annonce, entre guillemets. Il vit dans
  le `cloture-item` 371 fois sur 383 ; les 12 restantes sont posees directement
  dans un `criteria-row` de la section Management, donc HORS de tout autre
  bloc. Ce sont ces 12 orphelins qui imposent de le declarer comme bloc a part
  entiere — c'est `uncovered_content()` qui les a fait apparaitre.
* `cloture` (595 segments / 194 grilles) et `therapy` (759 / 190) sont ici la
  regle et non l'exception : RESCOS en comptait 40 et 47.
* Trois grilles (« ECOS Diag 1/2/3 ») n'ont AUCUNE fiche de fin de page :
  ni `annexes`, ni `expert`, ni `theorie`, ni `scenario`, ni `defi`.

Le corpus est globalement equilibre en `<div>` : 198 grilles sur 198, zero ecart
entre `<div` et `</div>`. C'est ce qui autorise le decoupage par equilibrage.
"""
import importlib.util
import re
import sys
import unicodedata
from pathlib import Path

_AMBOSS_DIR = Path(__file__).resolve().parents[1] / "amboss"


def amboss_module(name):
    """Charge un module de `scripts/amboss/` sous un alias `_casecos_amboss_<nom>`.

    Chargement par chemin explicite, jamais par `sys.path` : les quatre dossiers
    de corpus portent des scripts de meme nom (`check_nomenclature.py`,
    `check_reachability.py`, ...) et un import ordinaire resoudrait selon
    l'ordre du chemin, donc au hasard.

    L'alias porte un prefixe PROPRE a casecos, distinct du `_amboss_<nom>` de
    `lib_german` et du `_rescos_amboss_<nom>` de `lib_rescos`. Sans cela, les
    corpus partageraient la meme instance dans `sys.modules`, et le
    remplacement de `parse_config` opere par `check_reachability.py` (bareme
    embarque, propre a ce corpus) fuirait vers les autres s'ils s'executaient
    dans le meme processus.
    """
    path = _AMBOSS_DIR / (name + ".py")
    spec = importlib.util.spec_from_file_location("_casecos_amboss_" + name, path)
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

CASES = Path(__file__).resolve().parents[2] / "cases" / "casecos"

# Marqueur de fin de la zone pedagogique. Present dans les 198 grilles, une
# seule fois par grille, et toujours apres le dernier bloc de contenu.
END_MARK = "<!-- COMMENTAIRE GÉNÉRAL -->"

# Marqueur de fin de la section « Cloture de consultation », present 198/198
# (y compris dans les 4 grilles sans `cloture-item`, ou il borne la section
# Management). Toujours immediatement apres le dernier `cloture-item`.
COMM_MARK = "<!-- COMMUNICATION -->"

# Bornes des blocs de contenu, dans leur ordre d'apparition dans le fichier.
#
# Chaque entree est (nom, motif de debut, queue attendue). Le decoupage reel se
# fait par EQUILIBRAGE des `<div>` (`_balanced_end`), pas par le motif de fin.
# La « queue attendue » est ce qui doit suivre immediatement la fin equilibree ;
# `bounds_anomalies()` le verifie sur tout le corpus et `check_invariants.py` en
# fait un invariant. C'est ce controle qui signalerait qu'une grille future a
# change de gabarit.
#
# Releve de reference (188 + 181 + 759 + 595 + 383 + 195 x4 + 1 = 2887
# segments), queue par queue :
#   annexe-dd    -> `<div class="criteria-row"` 177,
#                   `<div class="criteria-description"` 9,
#                   `<div style="text-align: center` 2
#   redflags     -> `<div class="criterion-comment-section"` 181/181
#   therapy      -> `<div class="therapy-section">` 564,
#                   `<div class="criterion-comment-section"` 153,
#                   `<div class="redflags-section">` 42
#   cloture      -> `<div class="cloture-item">` 401,
#                   `</div>`* + COMM_MARK 194
#   exemples     -> `</div>`* + COMM_MARK 189,
#                   `</div>`* + `<div class="cloture-item">` 182,
#                   `<div class="criterion-comment-section"` 9,
#                   `<div class="scoring-rule">` 3
#   expert       -> `<div class="annexe-item annexe-theorie">` 195/195
#   theorie      -> `<div class="annexe-item annexe-scenario">` 195/195
#   scenario     -> `<div class="annexe-item annexe-defi">` 195/195
#   defi         -> `</div>`* + END_MARK 194,
#                   `<div class="annexe-item">` 1 (AMC-Psy-P10)
#   annexe-nu    -> `</div>`* + END_MARK 1/1
BLOCKS = [
    # --- blocs loges dans la section notee (niveau 2) ----------------------
    ("annexe-dd", r'<div class="annexe-item annexe-dd">',
     r'<div class="criteria-row"|<div class="criteria-description"'
     r'|<div style="text-align: center'),
    ("redflags", r'<div class="redflags-section">',
     r'<div class="criterion-comment-section"'),
    ("therapy", r'<div class="therapy-section">',
     r'<div class="therapy-section">|<div class="criterion-comment-section"'
     r'|<div class="redflags-section">'),
    # --- section « Cloture de consultation », non notee (niveau 2) ---------
    ("cloture", r'<div class="cloture-item">',
     r'<div class="cloture-item">|(?:</div>\s*)*' + re.escape(COMM_MARK)),
    # `exemples` est IMBRIQUE dans `cloture` 371 fois sur 383. Il est declare
    # comme bloc pour ses 12 occurrences ORPHELINES (posees dans un
    # `criteria-row`), que rien d'autre ne couvrirait. Les segments imbriques
    # sont donc comptes deux fois par `block_spans` — c'est voulu et sans
    # consequence : `all_items()` et `report_redundancy.py` passent par
    # `top_spans()`, qui ne retient que les segments NON contenus dans un autre.
    ("exemples", r'<div class="exemples-phrases">',
     r'<div class="criterion-comment-section"|<div class="scoring-rule">'
     r'|(?:</div>\s*)*(?:<div class="cloture-item">|' + re.escape(COMM_MARK) + r')'),
    # --- fiches pedagogiques de fin de page (niveau 3) ---------------------
    ("expert", r'<div class="annexe-item annexe-expert">',
     r'<div class="annexe-item annexe-theorie">'),
    ("theorie", r'<div class="annexe-item annexe-theorie">',
     r'<div class="annexe-item annexe-scenario">'),
    ("scenario", r'<div class="annexe-item annexe-scenario">',
     r'<div class="annexe-item annexe-defi">'),
    ("defi", r'<div class="annexe-item annexe-defi">',
     r'(?:</div>\s*)*(?:<div class="annexe-item">|' + re.escape(END_MARK) + r')'),
    # Variante de classe non standard — voir l'entete. Le motif exige la
    # fermeture immediate du `class=` : il ne peut pas attraper
    # `annexe-item annexe-dd` ni les quatre autres fiches.
    ("annexe-nu", r'<div class="annexe-item">',
     r'(?:</div>\s*)*' + re.escape(END_MARK)),
]

# Blocs exclus de la mesure de redondance par defaut — voir report_redundancy.py.
# `scenario` est le SCRIPT DU PATIENT SIMULE : redire les symptomes deja listes
# dans les fiches est sa fonction meme. AMBOSS l'exclut de fait, RESCOS
# explicitement ; l'exclure ici garde les trois corpus dans la meme unite.
# `annexe-nu` n'est PAS exclu : c'est aujourd'hui un second scenario (celui de
# la mere, AMC-Psy-P10), mais la classe est generique et une grille future
# pourrait y loger tout autre chose. Exclure sur la foi d'un seul segment
# creerait un angle mort permanent ; ses paires avec `scenario` se lisent et se
# comprennent.
REDUNDANCY_EXCLUDED = {"scenario"}

# Classes porteuses de contenu redactionnel. Toute occurrence hors des segments
# de BLOCKS est une ANOMALIE : elle signale un bloc que l'outillage ne voit pas.
# C'est la traduction en controle automatique de l'angle mort d'AMBOSS-34, ou
# une fiche portee par une classe non prevue etait restee invisible et n'avait
# eu pour seul symptome qu'un chiffre de redondance anormalement bas.
#
# Liste etablie par MESURE et non a la main : les 105 valeurs de `class=` du
# corpus ont ete partagees entre celles qui tombent dans un segment de BLOCKS et
# celles qui n'y tombent jamais. C'est cette partition qui a fait apparaitre les
# 12 `exemples-phrases` orphelins.
#
# `annexe-item` EST inclus, contrairement au choix de `lib_rescos`. Le piege du
# `\b` qui l'y faisait ecarter (`\btext\b` matchant `detail-text criteria-detail`)
# ne joue pas pour ce jeton : aucune autre classe du corpus ne contient
# « annexe-item » comme sous-chaine bordee. L'inclure fait de `uncovered_content`
# un detecteur direct de fiche inedite : toute `<div class="annexe-item annexe-X">`
# nouvelle serait signalee des le premier passage.
CONTENT_CLASSES = [
    "annexe-item", "annexe-title", "annexe-content",
    "annexe-dd-content", "dd-category",
    "redflags-section", "redflags-title", "redflags-item", "redflags-text",
    "redflags-description",
    "therapy-section", "therapy-title", "therapy-items", "therapy-item",
    "cloture-item", "cloture-title", "cloture-details", "cloture-detail",
    "cloture-content", "cloture-content-green",
    "exemples-phrases", "exemple-phrase",
    "annexe-expert-content", "expert-section",
    "annexe-theorie-content", "theorie-section",
    "theorie-section-rappels", "theorie-section-examens",
    "annexe-scenario-content", "scenario-section", "scenario-info",
    "annexe-defi-content",
    "property-group", "nested-object",
]

# Deliberement ABSENTES de CONTENT_CLASSES :
#
# * `criteria-row`, `criteria-text`, `criteria-description`, `detail-row`,
#   `detail-text criteria-detail`, `detail-checkbox(es)`,
#   `details-with-checkboxes`, `checkbox-group`, `patient-response`,
#   `points-display`, `scoring-rule`, `sub-criteria`, `comment-*`,
#   `criterion-comment-section`, `communication-*` : c'est la SECTION NOTEE
#   elle-meme (niveau 2), pas un bloc de commentaire. `patient-response` en
#   particulier compte 8152 occurrences dans la section notee contre 773 dans
#   les blocs : c'est une classe de critere, pas de contenu.
# * `annexes`, `annexes-grid`, `section cloture-section`, `section`,
#   `section-header`, `section-content` : ce sont les CONTENEURS des blocs, pas
#   leur contenu — ils sont par construction hors des segments.
# * `vital-sign*`, `timer-*`, `mode-*`, `total-*`, `header*`, `container`,
#   `missing-items`, `print-button`, `revision-*`, `lacune-button`, `score`,
#   `pourcent-body` : charpente de page et panneau de score.

# Motif de balise CORRIGE — un `<` suivi d'une LETTRE ASCII. Voir l'entete :
# le `\w+` de `lib_german` / `lib_rescos` reconnait « <2 cm ... </div> » comme
# une balise nommee « 2 » et avale la fermeture. 244 imbrications fantomes et 9
# segments emballes sur ce corpus.
_TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)((?:\s[^>]*?)?)/?>")


def grids():
    """Chemins des 198 grilles, tries par nom de fichier.

    Contrairement aux trois corpus precedents, les fichiers CasECOS ne portent
    AUCUN identifiant numerique (« AMC-Chir2-ECG3 ... », « UIDC-Mme Servier
    ... », « STEMI - Femme 55 ans ... »). Il n'y a donc pas de `grid_num()` :
    l'ordre est celui du nom, stable et reproductible. Le tri est un tri de
    chaines Python (par point de code), volontairement independant de la locale
    — un tri localise donnerait un ordre different d'une machine a l'autre et
    ferait diverger `baseline.json`.
    """
    return sorted(CASES.glob("*.html"), key=lambda p: p.name)


def grid_key(path):
    """Cle d'identification d'une grille : son nom de fichier.

    Existe pour donner aux scripts un point d'entree unique, la ou les autres
    corpus emploient `grid_num()`. Ne pas la remplacer par un index de position
    dans `grids()` : l'ajout d'une grille decalerait toutes les suivantes.
    """
    return Path(path).name


def matches(path, only):
    """Le filtre de ligne de commande `only` designe-t-il cette grille ?

    Comparaison en NFC des deux cotes. Les trois corpus precedents se filtraient
    par un identifiant ASCII (`RESCOS-12_`) ; ici le seul identifiant est le
    TITRE, qui porte des accents. Or macOS stocke les noms de fichiers en NFD
    (« e » + accent combinant) tandis qu'un shell ou un editeur envoie du NFC
    (« é » precompose) : `"Céphalées" in path.name` est FAUX sur ce systeme,
    alors que les deux chaines s'affichent a l'identique. Sans cette
    normalisation, tout filtre accentue rend « aucune grille ne correspond ».
    """
    if not only:
        return True
    return (unicodedata.normalize("NFC", only)
            in unicodedata.normalize("NFC", Path(path).name))


def _balanced_end(html, start):
    """Index de fin du `<div>` ouvert en `start`, par equilibrage strict.

    Plus sur qu'un motif de fin : un bloc qui en contient un autre du meme type,
    ou qui contient par accident le motif de fin d'un voisin, ne peut pas
    tromper l'equilibrage. Les 198 grilles sont globalement equilibrees ; en cas
    d'anomalie locale la fonction rend `len(html)`, ce que `bounds_anomalies()`
    signale.

    Le motif `_TAG` n'accepte que les balises a nom commencant par une LETTRE :
    c'est le correctif du chevron nu, sans lequel « (T1a) <2 cm ... </div> »
    fait disparaitre une fermeture. Voir l'entete du module.
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
    segments suivants (jusqu'a 14 `therapy-section` et 9 `cloture-item` dans une
    meme grille). Utiliser `block_segments()`.
    """
    segments = block_segments(html, name)
    return segments[0] if segments else None


def blocks_present(html):
    """Noms des blocs presents, avec leur nombre de segments : [[nom, n], ...]."""
    return [[name, len(block_spans(html, name))]
            for name, _, _ in BLOCKS if block_spans(html, name)]


def all_spans(html):
    """Tous les segments de tous les blocs, avec leur nom, tries."""
    spans = [(a, b, name) for name, _, _ in BLOCKS
             for a, b in block_spans(html, name)]
    return sorted(spans)


def top_spans(html, excluded=()):
    """Segments de PREMIER NIVEAU : ceux qui ne sont contenus dans aucun autre.

    Le bloc `exemples` vit 371 fois sur 383 a l'interieur d'un `cloture-item`.
    Compter ses items a la fois sous son propre nom et sous celui de `cloture`
    doublerait 1514 phrases modeles, et `report_redundancy.py` rapporterait
    chaque doublon deux fois. Cette fonction rend le decoupage NON RECOUVRANT
    du contenu : chaque caractere appartient a exactement un segment, sous le
    nom du bloc le plus exterieur.

    `excluded` retire des blocs AVANT le calcul du premier niveau, et non
    apres : sinon exclure `cloture` ferait remonter ses `exemples` imbriques,
    et l'exclusion changerait le total au lieu de le reduire.
    """
    spans = [s for s in all_spans(html) if s[2] not in excluded]
    return [(a, b, n) for a, b, n in spans
            if not any(a2 <= a and b <= b2 and (a2, b2) != (a, b)
                       for a2, b2, _ in spans)]


def peda_bounds(html):
    """Index (debut, fin) de la zone pedagogique de fin de page.

    Debut : `<div class="annexes">` — il n'y a pas de `resume` dans ce corpus.
    Fin : le commentaire `<!-- COMMENTAIRE GENERAL -->`, present 198/198.
    Retourne (-1, -1) pour les 3 grilles « ECOS Diag », seules sans `annexes`.

    Ne couvre NI `annexe-dd`, NI `therapy`, `redflags`, `cloture` et `exemples`,
    tous loges en amont dans les sections notees. Pour lire tout le contenu
    d'une grille, passer par `block_spans()` ou `top_spans()`.
    """
    start = html.find('<div class="annexes">')
    if start < 0:
        return -1, -1
    end = html.find(END_MARK, start)
    return start, (end if end > 0 else len(html))


def dd_bounds(html):
    """Index (debut, fin) du premier bloc `annexe-dd`, pour une lecture ciblee.

    Ce bloc vit dans la section Management (188 segments / 186 grilles, deux
    grilles en portent deux), donc AVANT la zone rendue par `peda_bounds()` et
    sans recouvrement avec elle — contrairement a RESCOS-14 et RESCOS-24. Meme
    convention d'index que `peda_bounds()` : des caracteres, a convertir en
    numeros de ligne pour `Read`. Retourne (-1, -1) si absent.
    """
    spans = block_spans(html, "annexe-dd")
    return spans[0] if spans else (-1, -1)


def bounds_anomalies(html):
    """Blocs dont la fin equilibree ne tombe pas sur la queue attendue.

    Filet contre une derive de gabarit : si une grille future deplace un bloc,
    l'equilibrage rendra toujours une borne juste mais ce qui la suit changera,
    et l'ecart sera signale ici plutot que de passer inapercu. C'est aussi ce
    controle qui a mis au jour le bug du chevron nu dans l'equilibrage : neuf
    segments dont la fin tombait sur `<script>` ou sur la fin du fichier.
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
    `redflags-section` dans German, `cloture-item` dans RESCOS, et ici les 12
    `exemples-phrases` orphelins : quatre blocs entiers qu'une transposition
    naive du `BLOCKS` d'AMBOSS aurait laisses invisibles.
    """
    spans = [(a, b) for a, b, _ in all_spans(html)]
    out = {}
    for cls in CONTENT_CLASSES:
        pattern = r'class="[^"]*\b' + re.escape(cls) + r'\b[^"]*"'
        for m in re.finditer(pattern, html):
            if not any(a <= m.start() < b for a, b in spans):
                out[cls] = out.get(cls, 0) + 1
    return out


# Items portes par un `<div>` de classe dediee plutot que par un `<li>` ou une
# puce. Sans cette regle, quatre blocs entiers rendraient ZERO item :
# `therapy` (1986 `therapy-item`, ni `<li>` ni puce dans 190 grilles),
# `redflags` (1249 paires texte/description), `cloture` (773 `cloture-detail`
# et 97 `cloture-content`) et `exemples` (1572 `exemple-phrase`).
#
# L'extraction se fait par EQUILIBRAGE et non par un `(.*?)</div>` non gourmand :
# un `therapy-item` contient deux `<div>` internes (« Traitement : ... » et
# « Details : ... »), qu'un motif non gourmand couperait au premier `</div>`.
_DIV_ITEM_CLASSES = (
    "therapy-item", "redflags-text", "redflags-description",
    "cloture-detail", "cloture-content", "exemple-phrase",
)
_DIV_ITEM_START = re.compile(
    r'<div class="(?:' + "|".join(_DIV_ITEM_CLASSES) + r')(?:[ "])[^>]*>')


def _div_items(segment):
    """(items, reste) — textes des `<div>` d'item, et le segment sans eux.

    Le reste est rendu pour que le decoupage par puces qui suit ne recompte pas
    ce qui a deja ete extrait ici.
    """
    items, rest, cursor = [], [], 0
    for m in _DIV_ITEM_START.finditer(segment):
        if m.start() < cursor:
            continue  # deja avale par un item precedent (imbrication)
        end = _balanced_end(segment, m.start())
        rest.append(segment[cursor:m.start()])
        items.append(segment[m.start():end])
        cursor = end
    rest.append(segment[cursor:])
    return items, " ".join(rest)


# Paragraphes de prose. `defi` (390 `<p>`), `theorie` (1119) et `scenario`
# (1503) n'emploient NI `<li>` ni puce pour une partie de leur contenu : sans
# cette regle, la fiche `defi` entiere — 195 segments, une par grille — ne
# rendrait aucun item et pourrait etre reecrite sans que `check_no_loss.py` ne
# voie rien. C'est l'extension propre a ce corpus, comme `_DIV_ITEM` l'etait
# pour German et RESCOS.
_PARA = re.compile(r"<p[^>]*>(.*?)</p>", re.S)


def list_items(segment, min_len=18):
    """Items normalises d'un segment, filtres sur une longueur minimale.

    Reprend la regle d'AMBOSS — `<li>`, puces « • » a l'interieur d'un `<li>`,
    puces hors `<li>` en jetant la tete sans borne gauche — et y ajoute, comme
    German et RESCOS, les items portes par un `<div>` de classe dediee, plus les
    paragraphes `<p>`.

    Quatre formats coexistent dans ce corpus :

    - `<li>` : `annexe-dd` (chaque `<li>` portant un diagnostic entier, decoupe
      ensuite par ses puces), `expert`, `theorie`, `scenario`, `annexe-nu` ;
    - puce « • » : 4734 dans `annexe-dd`, 919 dans `therapy`, 210 dans `expert` ;
    - `<div>` de classe dediee : `therapy-item`, `redflags-text`,
      `redflags-description`, `cloture-detail`, `cloture-content`,
      `exemple-phrase` (voir `_DIV_ITEM_CLASSES`) ;
    - `<p>` : `defi`, `theorie`, `scenario`.

    Aucun double comptage : les `<div>` d'item sont retires du reste avant le
    decoupage par puces et avant l'extraction des `<p>`, et le `<li>` prime sur
    le `<p>` (un `<p>` dans un `<li>` n'existe pas dans ce corpus, verifie).

    `min_len` vaut 18 comme dans AMBOSS, German et RESCOS, pour que le chiffre
    de redondance des quatre corpus se lise dans la meme unite.
    """
    items = []
    for m in re.finditer(r"<li[^>]*>(.*?)</li>", segment, re.S):
        text = visible_text(m.group(1))
        items += _bullet_items(text) if BULLET in text else [norm(text)]
    rest = re.sub(r"<li[^>]*>.*?</li>", " ", segment, flags=re.S)

    div_items, rest = _div_items(rest)
    for raw in div_items:
        text = visible_text(raw)
        items += _bullet_items(text) if BULLET in text else [norm(text)]

    for m in _PARA.finditer(rest):
        text = visible_text(m.group(1))
        items += _bullet_items(text) if BULLET in text else [norm(text)]
    rest = _PARA.sub(" ", rest)

    outside = visible_text(rest)
    if BULLET in outside:
        items += _bullet_items(outside)[1:]
    return [i for i in items if len(i) >= min_len]


def all_items(html):
    """Items de TOUS les blocs d'une grille, fusionnes, sans recouvrement.

    Fusionnes et non compares bloc par bloc : un item deplace d'un bloc a un
    autre est un deplacement legitime, pas une disparition. Le decoupage passe
    par `top_spans()`, donc les `exemples` imbriques dans un `cloture-item` ne
    sont comptes qu'une fois.
    """
    return [t for a, b, _ in top_spans(html) for t in list_items(html[a:b])]
