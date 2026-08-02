"""Detecte les termes non suisses dans les 165 grilles rescos-locales. Sortie 1 si presents.

Usage :
    python3 scripts/rescos-locales/check_nomenclature.py [--quiet]

La table BANNED d'AMBOSS (`scripts/amboss/check_nomenclature.py`) est IMPORTEE
et non recopiee. Elle ne decrit pas un corpus mais un referentiel — la
nomenclature de laboratoire et les usages suisses — et chacune de ses entrees
porte un commentaire acquis a l'usage : pourquoi `mg/mL` ne doit JAMAIS y
figurer (PC20 de la methacholine), pourquoi `CBC`/`BMP` sont tolerees en
position de cle de glossaire, pourquoi `/µL` n'est banni que precede d'un terme
d'hemogramme. Une seconde copie divergerait au premier ajout.

Les trois tables complementaires (`EXTRA`, `MICROBIO`, `ANGLICISMES`) sont
COPIEES depuis `scripts/rescos/check_nomenclature.py`, ou elles ont ete
etablies, et non importees. Meme argument que celui qui a fait recopier
`_balanced_end` dans `lib_rescos` : importer ferait de RESCOS une dependance de
ce volet et transformerait l'etoile (amboss = racine partagee, les corpus =
feuilles) en chaine. Le bon point de chute a terme est un module partage
(`scripts/lib_nomenclature.py`) d'ou les quatre corpus tireraient ces tables ;
ce refactor touche `scripts/rescos/` et n'entrait pas dans le perimetre.

ETAT — passe faite au lot l4 : 0 terme restant
==============================================
                          AMBOSS   German   RESCOS   rescos-locales
                                                     l2        l4
  \\bNFS\\b                  0        0        0     208 / 77     0
  /mm³                       0        0        0      17 / 11     0
  \\bpg/mL\\b                0        0        0       6 /  3     0
  \\bmg/dL\\b                0        0        0       6 /  4     0
  \\bg/dL\\b                 0        0        0       5 /  5     0
  \\bng/mL\\b                0        0        0       5 /  4     0
  [Gg]old standard          29       9        2      41 / 30     0
  \\bBMI\\b                  0        3        0      26 / 16     0
  \\bHIV\\b                  0        0        0      13 /  9     0
  \\bANA\\b                  0       10        0      13 /  4     0
  \\bMRSA\\b                 0        0        0      10 /  2     0
  \\bDMARDs?\\b              0        0        0       7 /  1     0
  \\bPCI\\b                  0        0        0       7 /  2     0
  \\bSCFE\\b                 0        0        0       3 /  1     0
  \\bMST\\b                  0        0        0       1 /  1     0
  numeration-implicite       0        0        0       8 /  6     0
  tous les autres            0        0        0       0

CE QUE LE RELEVE INITIAL NE VOYAIT PAS — 56 TERMES SUR 424
===========================================================
Le constat de l2 portait 368 termes. La passe en a traite 424. Les 56 ecarts ne
formaient AUCUNE famille nouvelle : chacun est un defaut de BORDAGE du motif.

  * `[Gg]old standard` — 41 et non 33. Le motif etait borne en MINUSCULES ;
    8 occurrences capitalisees, un cinquieme de la famille, etaient invisibles.
    La casse reste bornee explicitement (pas de `re.I`) pour que « GOLD » seul
    demeure hors de portee : c'est la classification GOLD de la BPCO,
    25 occurrences legitimes sur 3 grilles.
  * `\\bng/ml\\b` 9, `\\bpg/ml\\b` 2, `\\bg/dl\\b` 2, `\\bmEq/[lL]\\b` 4 — la table
    d'AMBOSS borne la graphie CANONIQUE. Ce corpus ecrit surtout la minuscule :
    9 `ng/ml` contre 5 `ng/mL`, la variante NON BORNEE etait la plus frequente.
  * `\\bERCP\\b` 9, `\\bMRCP\\b` 7, `\\bCOPD\\b` 1, `\\bSLE\\b` 1, `\\bBSA\\b` 4,
    `\\bQD\\b` 1 — familles entieres absentes de la table.
  * `Plaquettes 180 000` et `Leucocytes < 4000 ou > 20000` — `_HEMO` etait
    sensible a la casse et manquait toute numeration ouvrant une phrase. Trois
    valeurs sur les neuf de la famille.
  * `°F` 1, `Doliprane` 1, « Appeler le 15 » 2, CRP en `mg/mL` 2 — non couverts.

Et DEUX des 8 occurrences annoncees en numeration implicite etaient FAUSSES
(un ratio, une borne de norme) : la famille vaut 8 lignes / 9 valeurs, pas 8.

LE CRITERE QUI TRANCHE UNE TRADUCTION, ET QUI EST MESURABLE
============================================================
Une famille n'est activee que si son equivalent francais est DEJA employe par
ce corpus. Le fait remplace l'avis :

  ERCP -> CPRE (14 occurrences)        SLE  -> LES  (16)
  MRCP -> cholangio-IRM (6)            BSA  -> surface corporelle (11)
  COPD -> BPCO (122)                   QD   -> 1x/j (`x/j` 37, `x/jour` 44)

Le meme critere ECARTE `PTSD` (7 occurrences), `DKA` et `HHS` (5 chacun) : ni
`TSPT`, ni `ESPT`, ni `SHH` n'apparaissent nulle part dans les quatre corpus, et
les traduire aurait introduit un terme que rien n'atteste. Ecartes aussi `MCV`,
`MCH`, `MCHC`, `CEA`, `HBV`, `IGRA`, `DEXA` : ce sont les graphies des RAPPORTS
DE LABORATOIRE SUISSES, pas des anglicismes.

BORDAGE l4 — CINQ FAUX POSITIFS FRANCAIS DE PLUS, MESURES ICI
==============================================================
  * `\\bHIV\\b` — 1 des 13 occurrences est une HEMORRAGIE INTRAVENTRICULAIRE
    (classification de Fisher modifiee, grade 4 : « HSA + hematome
    intraparenchymateux ou HIV »). Le motif reste ACTIF : l'occurrence a ete
    developpee en toutes lettres, elle se lisait « virus » pour tout lecteur.
  * `\\bACE\\b` — ANTIGENE CARCINO-EMBRYONNAIRE (« ACE [metastases hepatiques] »,
    « scanner TAP, ACE »), pas l'enzyme de conversion. Le corpus ecrit d'ailleurs
    `IEC` 30 fois. JAMAIS ACTIVE.
  * `\\bEMS\\b` — 34 occurrences : ETABLISSEMENT MEDICO-SOCIAL, terme SUISSE. Une
    grille entiere s'intitule « Consultation telephonique EMS ». JAMAIS ACTIVE.
  * `\\bHR\\b` — « CT thoracique HR » (haute resolution) et « HR bitherapie »
    (isoniazide + rifampicine). Deux lectures, aucune anglaise. JAMAIS ACTIVE.
  * `\\bLP\\b` — « Tramadol LP » : liberation prolongee. JAMAIS ACTIVE.

Trois autres ecartes sans jamais avoir ete actives : `\\bSMUR\\b` (le service
existe en Suisse romande — SMUR Lausanne, Geneve), `\\bAugmentin\\b` (enregistre
en Suisse), et `\\bSpasfon\\b` pour une raison plus forte que l'usage : son
equivalent suisse, le Buscopan, est UNE AUTRE MOLECULE. Le substituer changerait
le medicament, pas son nom.

Enfin, ecartes comme ANGLICISMES DE REGISTRE et non de nomenclature, sur le
precedent des trois corpus deja a zero qui les portent encore : `screening` (4
ici, 1 sur AMBOSS), `timing` (2 ici, 3 sur AMBOSS), `pattern`, `follow-up`,
`guidelines`, `red flags` (17 ici, 14 sur AMBOSS), `management` (1683 — c'est le
NOM D'UNE SECTION DU BAREME).

BORDAGE — cinq motifs de RESCOS DESACTIVES ici, chacun sur un faux positif MESURE
=================================================================================
Le mandat impose de tester tout motif sur les quatre corpus avant activation.
Deux des seize anglicismes de RESCOS et un des dix motifs microbiologiques ont
ete retires apres mesure sur CE corpus :

  * `\\bFIT\\b` — **24 occurrences sur 2 grilles, TOUTES legitimes.** Le corpus
    ecrit « test FIT (immunologique) », « Test FIT : depistage, pas indique si
    symptomes » : c'est le nom courant du test immunologique fecal dans les
    recommandations francophones, et le corpus le GLOSE lui-meme en francais a
    sa premiere occurrence. RESCOS pouvait l'activer sans risque (0 occurrence
    la-bas) ; ici, dans une porte BLOQUANTE, il casserait deux grilles saines.
  * `\\bTB\\b` — **17 occurrences sur 3 grilles**, dont « TB-spot », nom propre
    du test T-SPOT.TB. RESCOS le notait deja : 22 occurrences sur AMBOSS-31,
    ou le token est employe systematiquement. Un motif de trois lettres qui
    rencontre un nom de produit n'est pas bordable.
  * `\\bVRE\\b` — faux positif francais AVERE (AMBOSS-19 : « VRE = volume de
    reserve expiratoire »). 0 ici, mais la lecon vaut d'un corpus a l'autre.
  * `\\bQID\\b` — **1 occurrence ici, francaise** : « Pas de douleur a la
    palpation QID » (quadrant inferieur droit, « Diverticulite sigmoidienne »).
    C'est EXACTEMENT le cas RESCOS-22 : meme token, deux sens legitimes selon
    le corpus (« quater in die » sur AMBOSS-8 et AMBOSS-13).
  * `\\bCRE\\b` — trois lettres, 0 occurrence sur les quatre corpus, aucun
    besoin demontre.

Restent egalement ecartes, comme dans RESCOS et pour les memes raisons mesurees :
`\\bASA\\b` (5-ASA, aminosalicylate), `\\bRx\\b` (graphie SUISSE de la
radiographie), `\\bAF\\b`, `\\bAAA\\b`, `\\bMI\\b`, `\\bCT\\b`, `\\bUS\\b`,
`\\bPR\\b`, `borderline`.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib

# --- EXTRA : deux regles que la table d'AMBOSS ne porte pas -----------------
# Etablies dans `scripts/rescos/check_nomenclature.py`, copiees ici (voir
# l'entete). Elles se fondent sur une liste de TERMES D'HEMOGRAMME plus large
# que celle d'AMBOSS : elle y ajoute les FORMES CLINIQUES du resultat
# (`hyperleucocytose`, `thrombopenie`, ...) et les synonymes (`PNN`, `PLT`).
# `GR`, `globules rouges`, `hematies` en sont ABSENTS a dessein : une numeration
# de LCR se rend justement en /µL.
# La CASSE des formes en toutes lettres est tolérée, celle des ACRONYMES ne
# l'est pas. Mesure qui l'impose : « Coagulation : Plaquettes 180 000 » et
# « Leucocytes < 4000 ou > 20000 » — deux numerations nues d'AMC Urgences 2B et
# 5C — echappaient au motif parce qu'elles ouvrent une phrase. Elles portaient a
# elles seules TROIS des neuf valeurs de la famille.
# Rendre le motif entier insensible a la casse serait au contraire desastreux :
# les 165 grilles portent leur CSS EN LIGNE, `\bGB\b` y matcherait le `gb` de
# `rgba(0,0,0,0.2)` et le `z-index: 1000` deux lignes plus bas ferait le reste —
# 165 grilles rouges sur une feuille de style. D'ou l'alternance explicite
# lettre par lettre sur les mots, et la casse stricte sur `GB`, `PNN`, `PLT`.
#
# `GR`, `globules rouges`, `hematies` restent ABSENTS a dessein : une numeration
# de LCR se rend justement en /µL.
_HEMO = (
    r"(?:[Hh]yperleucocytoses?|[Hh]ypoleucocytoses?|[Ll]eucocytoses?|[Ll]eucop[ée]nies?"
    r"|[Ll]eucocytes?|[Gg]lobules?\s+blancs?|\bGB\b|[Pp]olynucl[ée]aires?|[Nn]eutrophiles?"
    r"|\bPNN\b|[Gg]ranulocytes?|[Ll]ymphocytes?|[Ll]ymphop[ée]nies?|[ÉéEe]osinophiles?"
    r"|[ÉéEe]osinophilies?|[Mm]onocytes?|[Bb]asophiles?|[Tt]hrombop[ée]nies?"
    r"|[Tt]hrombocytoses?|[Tt]hrombocytes?|[Pp]laquettes?|\bPLT\b"
    r"|[Hh]yperlymphocytoses?)"
)

# Unites qui, si elles suivent le nombre, prouvent qu'il n'est PAS nu.
# Volontairement large : chaque entree manquante est un faux positif dans une
# porte bloquante. `G/l` et `g/l` (l minuscule) sont ajoutes par rapport a
# RESCOS — CasECOS avait mesure que leur absence rendait faux les
# « plaquettes 91000 G/l ».
_UNITS = (
    r"(?:G/L|g/L|G/l|g/l|/mm|/\s?[µμ]L|%|10|mg|µg|mcg|ng|pg|mmol|µmol|umol|U/L|UI"
    r"|kg|cm|mm|ml|mL|bpm|°|/j|/h|ans?\b|mois\b|min\b|jours?\b|semaines?\b)"
)

# Unite EXPLICITE : si elle apparait entre le terme d'hemogramme et le nombre,
# c'est que le nombre est une BORNE DE NORME et non une numeration nue.
# Faux positif mesure, RESCOS-58b : « plaquettes 450 G/L (N: 150-400) ». Le
# motif s'accrochait au 150 de l'intervalle de reference — l'unite du resultat
# le precede de douze caracteres. Un `[\d.,]*` elargi au tiret ne suffit PAS :
# « 150-400) » n'est suivi d'aucune unite, la norme herite de celle du resultat.
_UNITE_EXPLICITE = r"(?:G/[Ll]|g/[Ll]|/mm|/\s?[µμ]L)"

# Numeration d'hemogramme sans unite : « plaquettes 422 » se lit 422 G/L.
# Seuil `\d{3,}` et NON `\d{2,}` : a deux chiffres le motif coupe
# « hyperleucocytose (> 12 000/mm³) » en deux et declare une numeration nue la
# ou l'unite est deux caracteres plus loin. Garde-fou d'ANNEE `(?!(?:19|20)\d\d)`
# : un motif numerique trop large finit par rencontrer « plaquettes en 2019 ».
#
# DEUX GARDES ajoutees apres mesure sur ce corpus, chacune sur un faux positif :
#
#   * `(?!\s*pour\b)` — RATIO. « PL traumatique: 1 GB pour 500-1000 GR »
#     (« Pediatrie — Vomissements et etat febrile ») enonce un RAPPORT entre
#     deux lignees, pas un compte : le 500 n'a pas d'unite et n'en veut pas.
#     Le convertir en « 500 G/L » aurait invente une numeration.
#   * `_UNITE_EXPLICITE` — BORNE DE NORME, voir ci-dessus.
#
# Les deux gardes ne peuvent que RETIRER des correspondances : les trois corpus
# precedents restent a zero par construction. Verifie : amboss 0, german 0,
# rescos 0, ici 8 lignes (9 valeurs), 0 fausse.
_NUMERATION_IMPLICITE = (
    _HEMO + r"(?!\s*pour\b)"
    + r"(?:(?!" + _UNITE_EXPLICITE + r")(?:[^<\n]|<(?![a-zA-Z/]))){0,25}?"
    + r"\s(?!(?:19|20)\d\d\b)(\d{3,}(?:[  ']\d{3})?)"
    + r"(?![\d.,]*\s*" + _UNITS + r")"
)

# `/µL` precede d'un terme d'hemogramme, vocabulaire elargi.
_MICROLITRE_ETENDU = _HEMO + r"[^<]{0,30}/\s?[µμ]L"

# --- UNITES : les variantes de CASSE que la table d'AMBOSS ne porte pas -----
# AMBOSS borne `\bg/dL\b`, `\bng/mL\b`, `\bpg/mL\b` a la graphie canonique. Ce
# corpus ecrit AUSSI la minuscule, et pas marginalement : 9 `ng/ml` contre
# 5 `ng/mL`, la variante non bornee etait la PLUS frequente des deux. Meme
# constat pour `mEq/l` (3) contre `mEq/L` (1). Ces motifs sont volontairement
# ecrits a part plutot que rendus insensibles a la casse : `(?i)g/dL` matcherait
# aussi `G/DL`, forme qui n'existe nulle part, et surtout la table doit rester
# lisible entree par entree.
_UNITES_CASSE = {
    r"\bg/dl\b": "g/L (x10)",
    r"\bng/ml\b": "ng/L ou µg/L selon l'analyte",
    r"\bpg/ml\b": "pmol/L ou ng/L selon l'analyte",
    r"\bmEq/[lL]\b": "mmol/L (x1 pour un ion monovalent)",
    # Fahrenheit. Une seule occurrence, doublon d'un °C deja present.
    r"°F\b": "°C",
}

# `mg/mL` sur la CRP UNIQUEMENT, et jamais en general.
#
# La table d'AMBOSS documente pourquoi `mg/mL` ne doit JAMAIS y figurer : c'est
# l'unite de la PC20 a la methacholine (2 occurrences legitimes sur AMBOSS-18).
# Sur la CRP en revanche c'est une COQUILLE mesurable : 17 mg/mL vaudrait
# 17 000 mg/L, et le qualificatif voisin — « legerement elevee » — prouve que
# l'unite voulue etait mg/L. Le motif traverse les balises (`<span
# class="patient-response">`) parce que la valeur en est separee dans les deux
# occurrences.
_CRP_MG_ML = r"CRP(?:[^<]|<[^>]*>){0,60}?\bmg\s?/\s?m[lL]\b"

EXTRA = {
    _NUMERATION_IMPLICITE: "numeration en G/L (unite explicite obligatoire)",
    _MICROLITRE_ETENDU: "G/L (x0,001)",
    _CRP_MG_ML: "CRP en mg/L (coquille : mg/mL vaudrait x1000)",
}
EXTRA.update(_UNITES_CASSE)

# --- MICROBIO : abreviations microbiologiques anglophones -------------------
# `\bTB\b` RETIRE apres mesure (17 occurrences ici, dont « TB-spot ») — voir
# l'entete. `\bVRE\b` et `\bCRE\b` n'y ont jamais figure, pour la meme raison.
MICROBIO = {
    r"\bMRSA\b": "SARM",
    r"\bMSSA\b": "SASM",
    r"\bESBL\b": "BLSE",
    r"\bMDRO\b": "BMR (bacterie multiresistante)",
    r"\bHIV\b": "VIH",
    r"\bPID\b": "salpingite / infection genitale haute",
    r"\bUTI\b": "IVU (infection des voies urinaires)",
    r"\bSTD\b": "IST",
    r"\bSTI\b": "IST",
}

# --- ANGLICISMES : acronymes anglophones hors microbiologie -----------------
# `\bFIT\b` RETIRE apres mesure (24 occurrences legitimes ici) — voir l'entete.
# ATTENTION pour la passe a venir : une des occurrences de `gold standard`
# qualifie parfois un TRAITEMENT et non un examen — le remplacement se fait
# occurrence par occurrence, jamais par `sed` uniforme.
ANGLICISMES = {
    # `[Gg]old` et non `gold` : 8 des 41 occurrences de ce corpus etaient
    # capitalisees, soit un cinquieme de la famille invisible au motif d'origine.
    # La casse est bornee explicitement (et non par `re.I`) pour que « GOLD »
    # seul reste hors de portee : c'est la classification GOLD de la BPCO,
    # 25 occurrences legitimes sur 3 grilles.
    r"[Gg]old standard": "examen (ou traitement) de reference",
    r"\bESR\b": "VS (vitesse de sedimentation)",
    r"\bANA\b": "AAN (anticorps anti-nucleaires)",
    r"anti-DNA": "anti-ADN natif",
    r"\bSCFE\b": "epiphysiolyse femorale superieure",
    r"\bDMARDs?\b": "traitement de fond",
    r"\bCABG\b": "pontage (aorto-)coronarien",
    r"\bPCI\b": "angioplastie coronarienne",
    r"\bIVDU\b": "usage de drogues par voie intraveineuse",
    r"\bPRN\b": "a la demande / si besoin",
    r"[Gg]iant cells?": "cellules geantes",
    r"\bN/V\b": "nausees et vomissements",
    r"\bDM\b": "diabete",
    r"\bMST\b": "IST",
    r"\bBMI\b": "IMC",
    # --- ajouts de la passe l4, chacun borde sur les quatre corpus ---------
    # Regle d'admission appliquee : (a) acronyme ou unite ANGLOPHONE, (b) AUCUNE
    # lecture francaise possible dans les quatre corpus, (c) l'equivalent
    # francais est DEJA employe par ce corpus meme — c'est ce troisieme critere,
    # mesurable, qui tranche la traduction plutot qu'un avis.
    r"\bERCP\b": "CPRE (deja 14 occurrences dans le corpus)",
    r"\bMRCP\b": "cholangio-IRM (deja 6 occurrences dans le corpus)",
    r"\bCOPD\b": "BPCO (deja 122 occurrences dans le corpus)",
    r"\bSLE\b": "LES (deja 16 occurrences dans le corpus)",
    r"\bBSA\b": "surface corporelle (deja 11 occurrences dans le corpus)",
    # « quaque die ». A ne pas confondre avec `\bQID\b`, ECARTE : il vaut
    # « quadrant inferieur droit » dans ce corpus (voir l'entete).
    r"\bQD\b": "1x/j",
    # Marque francaise du paracetamol. Prolonge `Tylenol -> Dafalgan` de la
    # table AMBOSS : meme molecule, meme geste. `Augmentin` a ete ECARTE apres
    # verification — il est enregistre en Suisse. `Spasfon` aussi, mais pour une
    # raison plus forte : son equivalent suisse (Buscopan) est une AUTRE
    # MOLECULE, et le substituer changerait le medicament, pas son nom.
    r"\bDoliprane\b": "Dafalgan",
    # Numero d'urgence francais. Borde a l'ACTE d'appeler : « le 15 » nu
    # rencontrerait « le 15 mars », « le 15e jour », « le 15 % ». La Suisse
    # compose le 144 — que le corpus emploie deja (AMC Urgences 3A).
    # `\b911\b` et `\bSAMU\b` sont deja dans la table AMBOSS importee ; `SMUR`
    # a ete ECARTE : ce service existe en Suisse romande (SMUR Lausanne, Geneve).
    r"(?:[Aa]ppeler|[Cc]omposer)[^<.]{0,30}\ble 15\b": "144",
    # Decide par les campagnes precedentes, 0 occurrence ici : la porte le
    # garde pour l'avenir plutot que de le redecouvrir.
    r"\bNPO\b": "a jeun",
}

# Copie, jamais la reference : muter la table d'AMBOSS en place ferait dependre
# son contenu de l'ordre des imports si plusieurs corpus tournaient dans le
# meme processus.
BANNED = dict(lib.amboss_module("check_nomenclature").BANNED)
BANNED.update(EXTRA)
BANNED.update(MICROBIO)
BANNED.update(ANGLICISMES)


def main():
    quiet = "--quiet" in sys.argv[1:]
    total, grids_hit = 0, set()
    for path in lib.grids():
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        for pattern, repl in BANNED.items():
            hits = re.findall(pattern, html)
            if hits:
                total += len(hits)
                grids_hit.add(path.name)
                if not quiet:
                    print(f"  {path.name}: {len(hits)}x {pattern} -> attendu {repl}")
    if total:
        print(f"\nECHEC — {total} terme(s) non suisse(s) restant(s) "
              f"sur {len(grids_hit)} grille(s)")
        return 1
    print("OK — aucun terme non suisse detecte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
