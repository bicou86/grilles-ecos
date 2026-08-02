"""Detecte les termes non suisses dans les 41 grilles RESCOS. Sortie 1 si presents.

La table BANNED d'AMBOSS (`scripts/amboss/check_nomenclature.py`) est importee
et non recopiee. Elle ne decrit pas un corpus mais un referentiel — la
nomenclature de laboratoire et les usages suisses — et chacune de ses entrees
porte un commentaire acquis a l'usage : pourquoi `mg/mL` ne doit JAMAIS y
figurer (PC20 de la methacholine), pourquoi `CBC`/`BMP` sont tolerees en
position de cle de glossaire, pourquoi `/µL` n'est banni que precede d'un terme
d'hemogramme (une numeration de LCR se rend bien en /µL). Une seconde copie
divergerait au premier ajout.

Releve initial sur RESCOS (etat au moment du portage) : 111 termes sur 28
grilles — 104 `NFS`, 4 `mg/dL`, 2 `g/dL`, 1 `/mm³`. Aucun `ng/mL`, `pg/mL`,
`/µL`, `911`, `SAMU`, ni nom de marque americaine. Tous traites par
`apply_lab_nomenclature.py` ; la table est depuis a zero.

CE QUE CE FICHIER AJOUTE — `EXTRA`
===================================
Deux regles que la table d'AMBOSS ne porte pas, ajoutees APRES la passe et
bordees avant activation. Elles vivent ici et non dans `scripts/amboss/` :
c'est ce corpus qui a fait apparaitre les deux manques, et le volet RESCOS
s'interdit d'ecrire dans les dossiers des corpus precedents.

Les deux se fondent sur une meme liste de TERMES D'HEMOGRAMME (`_HEMO`), plus
large que celle d'AMBOSS. Elle y ajoute les FORMES CLINIQUES du resultat —
`hyperleucocytose`, `leucocytose`, `leucopenie`, `thrombopenie`,
`thrombocytose`, `eosinophilie` — et les synonymes `polynucleaires`, `PNN`,
`granulocytes`, `PLT`. C'est exactement le manque qui avait laisse passer
« eosinophiles > 300/µL » dans AMBOSS-19 : la recherche initiale ne couvrait
pas la variante employee par la grille.

BORDAGE — mesure, pas intention
-------------------------------
Les deux motifs ont ete passes sur les TROIS corpus avant d'etre actives.

1. `numeration-implicite` : 1 seul hit avant la passe (RESCOS-3,
   « plaquettes 422 »), 0 sur AMBOSS, 0 sur German, 0 sur RESCOS apres.

   * Le seuil est `\\d{3,}` et NON `\\d{2,}`, par mesure : a deux chiffres, le
     motif attrape « CRP > 20 mg/L, hyperleucocytose (> 12 000/mm³) » de
     RESCOS-9b — il capture « 12 », recule devant « 000/mm³ » et declare une
     numeration nue la ou l'unite est presente deux caracteres plus loin. Un
     faux positif dans une porte BLOQUANTE coute plus cher que la detection
     d'un « plaquettes 45 » hypothetique, que le corpus ne contient pas.
     C'est aussi le seuil de la famille `numeration-implicite` de
     `scripts/german/report_import_defects.py` : les deux mesures restent
     comparables.
   * Le garde-fou d'ANNEE `(?!(?:19|20)\\d\\d\\b)` a ete ajoute apres avoir vu
     « plaquettes en 2019 » declenchee par le motif nu. C'est la lecon du
     `\\b112\\b` d'AMBOSS transposee : un motif numerique trop large finit par
     rencontrer un nombre qui n'est pas une valeur de laboratoire.
   * La liste d'unites du lookahead negatif (`_UNITS`) borne l'autre cote :
     sans elle, « leucocytes (norme 4-10 G/L), CRP 120 mg/L » comptait pour
     une numeration nue parce que le nombre suivant portait une unite absente
     de la liste.

2. `/µL` a termes etendus : 0 hit sur RESCOS (le corpus n'emploie pas cette
   graphie), et — controle essentiel — la numeration de LCR
   « PL : GR 50 000 /µL », seule ecriture CORRECTE de ce cas, n'est PAS
   attrapee : `GR` ne figure pas dans `_HEMO`, deliberement. La regle
   d'AMBOSS reste en place ; celle-ci n'en est qu'un elargissement de
   vocabulaire.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos as lib

# Termes d'hemogramme — resultats ET formes cliniques du resultat.
# `GR`, `globules rouges`, `hematies` en sont ABSENTS a dessein : une
# numeration de LCR se rend justement en /µL (PROCEDURE.md § 6).
_HEMO = (
    r"(?:hyperleucocytoses?|hypoleucocytoses?|leucocytoses?|leucop[ée]nies?|leucocytes?"
    r"|globules?\s+blancs?|\bGB\b|polynucl[ée]aires?|neutrophiles?|\bPNN\b|granulocytes?"
    r"|lymphocytes?|lymphop[ée]nies?|[ée]osinophiles?|[ée]osinophilies?|monocytes?"
    r"|basophiles?|thrombop[ée]nies?|thrombocytoses?|thrombocytes?|plaquettes?|\bPLT\b)"
)

# Unites qui, si elles suivent le nombre, prouvent qu'il n'est PAS nu.
# Volontairement large : chaque entree manquante est un faux positif dans une
# porte bloquante.
_UNITS = (
    r"(?:G/L|g/L|/mm|/\s?[µμ]L|%|10|mg|µg|mcg|ng|pg|mmol|µmol|umol|U/L|UI|kg|cm|mm"
    r"|ml|mL|bpm|°|/j|/h|ans?\b|mois\b|min\b|jours?\b|semaines?\b)"
)

# Numeration d'hemogramme sans unite : « plaquettes 422 » se lit 422 G/L.
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

# ---------------------------------------------------------------------------
# MICROBIO — abreviations microbiologiques et infectiologiques anglophones
# ---------------------------------------------------------------------------
# Angle mort constate au lot r4a : `MRSA` figurait dans RESCOS-9b et a ete
# corrige en `SARM` a l'occasion d'un alignement de niveau 1, sans qu'AUCUN
# controle ne le signale — la table d'AMBOSS porte les unites de laboratoire et
# les numeros d'urgence, pas la nomenclature microbiologique.
#
# BORDAGE (mesure, pas intention) — les onze motifs ci-dessous rendent 0 hit sur
# les 41 grilles RESCOS apres la passe du lot r4b, et 0 sur les 40 grilles
# AMBOSS, a une exception mesuree et documentee :
#
#   * `\bTB\b` : 0 sur RESCOS (l'unique occurrence, RESCOS-34
#     « etiologie specifique (TB, purulente, neoplasique) », est devenue
#     « tuberculeuse »), mais **22 sur AMBOSS-31**, ou le token est employe
#     systematiquement. La table ne tourne que sur RESCOS, donc l'ajout est sans
#     effet la-bas ; consigne ici pour qui voudrait un jour la promouvoir.
#
# DEUX MOTIFS DELIBEREMENT ECARTES, et pourquoi :
#
#   * `\bVRE\b` (enterocoque resistant a la vancomycine) — **faux positif
#     francais avere** : AMBOSS-19 ecrit « VRE = volume de reserve
#     expiratoire », abreviation standard de spirometrie. Dans une porte
#     BLOQUANTE, ce motif casserait toute grille portant des volumes
#     pulmonaires. C'est la lecon du `\b112\b` d'AMBOSS et du seuil `\d{3,}`
#     ci-dessus : un token court finit par rencontrer un homographe legitime.
#   * `\bCRE\b` (enterobacterie resistante aux carbapenemes) — trois lettres,
#     aucun besoin demontre (0 occurrence sur les deux corpus), meme famille de
#     risque que `VRE`. On n'ajoute pas un motif court sans besoin mesure.
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
    r"\bTB\b": "tuberculose (ou TBC)",
}

# ---------------------------------------------------------------------------
# ANGLICISMES — acronymes anglophones hors microbiologie
# ---------------------------------------------------------------------------
# Le lot r4b avait traite les abreviations MICROBIOLOGIQUES et signale que le
# recensement etait fait a moitie. Recensement complet mene au lot r4c : tous
# les tokens majuscules de 2 a 8 caracteres du TEXTE VISIBLE des 41 grilles ont
# ete extraits et tries, puis chaque candidat a ete compte sur les TROIS corpus
# avant d'etre retenu ou ecarte.
#
# Les seize motifs ci-dessous rendent 0 hit sur les 41 grilles RESCOS apres la
# passe. Chacun etait, avant elle, en CONTRADICTION INTERNE avec une graphie
# francaise deja employee ailleurs dans le corpus — ce n'est pas une preference
# de style mais une incoherence mesuree :
#
#   ANA (RESCOS-3) contre AAN (RESCOS-38)     DMARDs contre « traitement de
#   fond » (RESCOS-38, dans le MEME bloc)     PCI/CABG contre « angioplastie »
#   et « pontage » (RESCOS-36, dans la MEME grille)     MST (RESCOS-1) contre
#   IST (RESCOS-14, 33)     BMI (10 grilles) contre IMC (6 grilles, dont deux
#   qui ecrivaient les DEUX)     ESR (RESCOS-3) contre « VS », donnee dans la
#   parenthese suivante     SCFE (RESCOS-9b) contre « epiphysiolyse femorale
#   superieure », en toutes lettres deux lignes plus bas.
#
# `gold standard` : 15 occurrences sur 14 grilles, contre « examen de
# reference » deja employe 7 fois sur 5 grilles. Le lot r4b l'avait laisse
# intact faute de pouvoir le traiter sur tout le corpus ; il l'est ici en une
# passe. ATTENTION : une des 15 qualifiait un TRAITEMENT et non un examen
# (« Methotrexate = gold standard »), d'ou « traitement de fond de reference ».
# Un `sed` uniforme aurait produit une phrase fausse — le remplacement s'est
# fait occurrence par occurrence.
#
# MESURE SUR LES DEUX AUTRES CORPUS (la table ne tourne que sur RESCOS ; ces
# chiffres sont consignes pour qui voudrait un jour la promouvoir) :
#   `gold standard` 26 sur AMBOSS (19 grilles), 5 sur German (3 grilles)
#   `\bANA\b`       9 sur German-44   `\bBMI\b` 3 sur German   `\bFIT\b` 1
#   tous les autres : 0 / 0.
#
# SEPT MOTIFS DELIBEREMENT ECARTES, chacun sur un faux positif MESURE :
#
#   * `\bVRE\b` — AMBOSS-19 ecrit « VRE = volume de reserve expiratoire ».
#     Confirme au lot r4c (1 hit). Ecarte, comme au lot r4b.
#   * `\bQID\b` — cas neuf et exemplaire : RESCOS-22 ecrit « 4 quadrants :
#     QSD, QSG, QID, QIG » (quadrant inferieur droit, FRANCAIS) tandis
#     qu'AMBOSS-13 et AMBOSS-8 ecrivent « paracetamol 1g QID » (quater in die,
#     posologie). Meme token, deux sens legitimes, un par corpus : dans une
#     porte BLOQUANTE, ce motif casserait RESCOS-22 pour un usage correct.
#   * `\bASA\b` — RESCOS-14 ecrit « 5-ASA » (aminosalicylate), 8 hits ; aussi
#     6 sur AMBOSS et 10 sur German. Nom de molecule, pas un acronyme d'usage.
#   * `\bRx\b` — « Rx thorax » est la graphie SUISSE de la radiographie
#     (6 RESCOS, 10 AMBOSS). Faux ami parfait : en anglais `Rx` designe
#     l'ordonnance. Bannir le sigle francais parce qu'il ressemble a un sigle
#     anglais serait l'erreur exactement inverse de celle qu'on corrige.
#   * `\bAF\b` — RESCOS-19 ecrit « Anamnese familiale (AF) ».
#   * `\bAAA\b` — anevrisme de l'aorte abdominale : le sigle francais et le
#     sigle anglais coincident (3 hits RESCOS, tous corrects).
#   * `\bMI\b` (membres inferieurs, 8 RESCOS / 16 AMBOSS), `\bCT\b` (90),
#     `\bUS\b` (41), `\bPR\b` (polyarthrite rhumatoide) et `borderline`
#     (terme diagnostique du DSM/CIM employe tel quel en francais) : usages
#     installes, mesures, non corriges.
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
    r"\bFIT\b": "test immunologique fecal",
    r"\bN/V\b": "nausees et vomissements",
    r"\bDM\b": "diabete",
    r"\bMST\b": "IST",
    r"\bBMI\b": "IMC",
}

# Copie, jamais la reference : muter la table d'AMBOSS en place ferait
# dependre son contenu de l'ordre des imports si les deux corpus tournaient
# dans le meme processus.
BANNED = dict(lib.amboss_module("check_nomenclature").BANNED)
BANNED.update(EXTRA)
BANNED.update(MICROBIO)
BANNED.update(ANGLICISMES)


def main():
    total = 0
    for path in lib.grids():
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        for pattern, repl in BANNED.items():
            hits = re.findall(pattern, html)
            if hits:
                total += len(hits)
                print(f"  {path.name}: {len(hits)}x {pattern} -> attendu {repl}")
    if total:
        print(f"\nECHEC — {total} terme(s) non suisse(s) restant(s)")
        return 1
    print("OK — aucun terme non suisse detecte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
