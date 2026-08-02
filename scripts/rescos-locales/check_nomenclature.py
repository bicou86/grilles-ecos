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

RELEVE INITIAL — ce corpus n'a subi AUCUNE passe de nomenclature
================================================================
                          AMBOSS   German   RESCOS   rescos-locales
  \\bNFS\\b                  0        0        0        208 / 77
  /mm³                       0        0        0         17 / 11
  \\bpg/mL\\b                0        0        0          6 /  3
  \\bmg/dL\\b                0        0        0          6 /  4
  \\bg/dL\\b                 0        0        0          5 /  5
  \\bng/mL\\b                0        0        0          5 /  4
  gold standard             26        5        0         33 / 24
  \\bBMI\\b                  0        3        0         26 / 16
  \\bHIV\\b                  0        0        0         13 /  9
  \\bANA\\b                  0       10        0         13 /  4
  \\bMRSA\\b                 0        0        0         10 /  2
  \\bDMARDs?\\b              0        0        0          7 /  1
  \\bPCI\\b                  0        0        0          7 /  2
  \\bSCFE\\b                 0        0        0          3 /  1
  \\bMST\\b                  0        0        0          1 /  1
  numeration-implicite       0        0        0          8 /  6
  tous les autres            0        0        0          0

Total : **368 termes** a traiter, sur 103 grilles. Les trois corpus precedents
sont a zero — leur passe a ete faite. Celle-ci reste entierement a faire ; ce
volet MESURE et ne corrige pas.

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
_HEMO = (
    r"(?:hyperleucocytoses?|hypoleucocytoses?|leucocytoses?|leucop[ée]nies?|leucocytes?"
    r"|globules?\s+blancs?|\bGB\b|polynucl[ée]aires?|neutrophiles?|\bPNN\b|granulocytes?"
    r"|lymphocytes?|lymphop[ée]nies?|[ée]osinophiles?|[ée]osinophilies?|monocytes?"
    r"|basophiles?|thrombop[ée]nies?|thrombocytoses?|thrombocytes?|plaquettes?|\bPLT\b)"
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

# Numeration d'hemogramme sans unite : « plaquettes 422 » se lit 422 G/L.
# Seuil `\d{3,}` et NON `\d{2,}` : a deux chiffres le motif coupe
# « hyperleucocytose (> 12 000/mm³) » en deux et declare une numeration nue la
# ou l'unite est deux caracteres plus loin. Garde-fou d'ANNEE `(?!(?:19|20)\d\d)`
# : un motif numerique trop large finit par rencontrer « plaquettes en 2019 ».
_NUMERATION_IMPLICITE = (
    _HEMO
    + r"(?:[^<\n]|<(?![a-zA-Z/])){0,25}?\s(?!(?:19|20)\d\d\b)(\d{3,}(?:[  ]\d{3})?)"
    + r"(?![\d.,]*\s*" + _UNITS + r")"
)

# `/µL` precede d'un terme d'hemogramme, vocabulaire elargi.
_MICROLITRE_ETENDU = _HEMO + r"[^<]{0,30}/\s?[µμ]L"

EXTRA = {
    _NUMERATION_IMPLICITE: "numeration en G/L (unite explicite obligatoire)",
    _MICROLITRE_ETENDU: "G/L (x0,001)",
}

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
    r"gold standard": "examen (ou traitement) de reference",
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
