"""Detecte les termes non suisses dans les 198 grilles CasECOS. Sortie 1 si presents.

La table BANNED d'AMBOSS (`scripts/amboss/check_nomenclature.py`) est importee
et non recopiee. Elle ne decrit pas un corpus mais un REFERENTIEL — la
nomenclature de laboratoire et les usages suisses — et chacune de ses entrees
porte un commentaire acquis a l'usage : pourquoi `mg/mL` ne doit JAMAIS y
figurer (PC20 de la methacholine), pourquoi `CBC`/`BMP` sont tolerees en
position de cle de glossaire, pourquoi `/µL` n'est banni que precede d'un terme
d'hemogramme (une numeration de LCR se rend bien en /µL).

POURQUOI LES TABLES DE RESCOS NE SONT PAS IMPORTEES
====================================================
`scripts/rescos/check_nomenclature.py` porte trois tables supplementaires
(`EXTRA`, `MICROBIO`, `ANGLICISMES`). Elles ne sont PAS importees ici, et ce
n'est pas un oubli : deux de leurs entrees produisent, sur CE corpus, des faux
positifs averes dans une porte BLOQUANTE.

  * `\\bTB\\b` — 19 occurrences, toutes legitimes : « Quantiferon (TB latente) »,
    « TB-MDR », « MDR-TB », graphies internationales standard de la
    tuberculose multiresistante. S'y ajoute l'homographe psychiatrique
    « trouble bipolaire (TB) ». Deux sens corrects, un motif : ecarte.
  * `\\bMST\\b` — 4 occurrences, dont **« Morphine PO (Sevredol® 10 mg q4h,
    MST Continus®) »**. `MST Continus®` est la morphine a liberation prolongee,
    un nom de specialite. Bannir ce sigle corromprait une prescription. Meme
    famille que le `\\bVRE\\b` d'AMBOSS-19 (volume de reserve expiratoire) et le
    `\\bQID\\b` de RESCOS-22 (quadrant inferieur droit) : ecarte.

Une table qu'il faut amputer corpus par corpus n'est pas une table partagee.
Les motifs communs sont donc redefinis ici, chacun re-borde par MESURE sur les
198 grilles CasECOS. Le referentiel reellement universel — unites SI, marques,
numeros d'urgence — reste celui d'AMBOSS, importe.

RELEVE INITIAL CasECOS (etat au moment du portage, avant toute passe)
======================================================================
Le corpus n'a jamais ete traite : la table sort donc ROUGE, et c'est sa
fonction — elle est la liste de travail du lot suivant, pas un echec de
l'outillage.

ETAT APRES LA PASSE k3 : VERTE
================================
Les 649 termes du releve k1 ont ete traites, plus 200 que k1 ne voyait pas et
qu'un releve INDEPENDANT a fait apparaitre — tous les acronymes MAJUSCULES de 2
a 8 caracteres du texte visible des 198 grilles (script et style retires),
3563 jetons distincts, juges un par un :

    DOAC 40   ERCP 25   MCV  22   pPCI 20   ARDS 12   MCHC 11   ALT  10
    AST   8   SNRI  8   LDCT  8   SSRI  7   EUS   7   MCH   2   g%    2
    NPO   2   MRI   2   WHO   1   TTE   1   TEE   1   OTC   1   HCT   1

plus 9 numerations sanguines en unite implicite hors du vocabulaire de
`report_import_defects.py` (« leucocytose 18'000 », « hyperleucocytose »,
« Plq 150 », « GR », « Ht », « Hb 15.8 » sans unite).

`pPCI` est le plus instructif : il etait invisible au releve k1 parce que le
`p` minuscule de `pPCI` est un caractere de mot et que `\\bPCI\\b` n'y trouve
donc pas de frontiere gauche. 20 occurrences dans une seule grille, a cote des
31 `PCI` qui, elles, etaient comptees.

Le releve k3 a aussi ECARTE onze jetons d'apparence anglophone qui sont des
homographes francais ou suisses — `MI` (membres inferieurs), `IU` (infection
urinaire), `PTT` (la crase suisse), `OAC` (l'ordonnance federale), `IBS`
(infection bacterienne serieuse), `HIT` (Head Impulse Test), `EGFR` (le gene)
— tous consignes dans SANS_MOTIF avec leur chiffre.

DEUX FAUX POSITIFS MESURES QUI ONT FAIT ECARTER UN MOTIF
---------------------------------------------------------
  * `\\b112\\b` — **593 occurrences sur les 198 grilles**, toutes dans la
    feuille de style : `rgb(112, 188, 123)`, la couleur des phrases modeles.
    La regle « pas de motif sur 112 » heritee d'AMBOSS (« Score Global 0/112 »)
    se verifie ici a une echelle inedite. Ne jamais l'ajouter.
  * `\\blivres?\\b` nu — 3 occurrences, dont « Associations de patients
    (TDAH Suisse), **livres**, groupes de soutien » : des ouvrages, pas des
    pounds. Le motif retenu exige un NOMBRE devant (`\\b\\d+\\s+livres?\\b`), ce
    qui rend 2 occurrences, les deux reelles (« j'ai perdu environ 20 livres…
    Je pesais 140 livres »).

TROIS MARQUES QUI RESSEMBLENT A DES ANGLICISMES ET N'EN SONT PAS
-----------------------------------------------------------------
Mesurees, puis deliberement NON bannies :
  * `Lopressor®` (13 occ) — metoprolol, specialite NOVARTIS, enregistree en
    Suisse. Le nom sonne americain ; il ne l'est pas.
  * `Lasix®` (3 occ) et `Zofran®` (2 occ) — furosemide et ondansetron, tous
    deux enregistres par Swissmedic.
  * `Glucophage®` (9 occ) — metformine, enregistree en Suisse.
Bannir une specialite disponible en Suisse au motif qu'elle est aussi vendue
aux Etats-Unis serait l'erreur exactement inverse de celle qu'on corrige.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_casecos as lib

# ---------------------------------------------------------------------------
# UNITES — la meme regle qu'AMBOSS, dans les graphies que sa table ne voit pas
# ---------------------------------------------------------------------------
# ANGLE MORT DE LA TABLE AMBOSS, mis au jour ici : ses motifs d'unites sont
# SENSIBLES A LA CASSE (`\bg/dL\b`, `\bng/mL\b`). Or CasECOS ecrit trois fois
# sur quatre la graphie minuscule. Releve comparatif :
#
#                  graphie AMBOSS      graphie minuscule     total reel
#     mg/dL              2                     5                  7
#     g/dL               1                    24                 25
#     ng/mL             17                    39                 56
#     pg/mL              6                     4                 10
#     /mm³              19                     4 (`/mm3`)        23
#
# Sans ces cinq motifs, 76 des 121 valeurs a convertir seraient invisibles.
# Meme bordage que la table d'origine : dans « mg/dl » comme dans « ng/dl » il
# n'y a pas de frontiere de mot entre la lettre de prefixe et le « g », donc
# `\bg/dl\b` ne peut pas attraper `mg/dl`.
#
# NE PAS y ajouter `mmol/l`, `mg/l`, `U/l`, `G/l` : ce sont les unites SI
# CORRECTES, ecrites avec un « l » minuscule. 223 + 27 + 15 occurrences dans ce
# corpus. Le « l » minuscule est une variante typographique, pas une erreur de
# nomenclature ; les bannir signalerait comme faux ce qui est juste.
UNITES = {
    r"\bmg/dl\b": "unites SI",
    r"\bg/dl\b": "g/L (x10)",
    r"\bng/ml\b": "ng/L ou µg/L selon l'analyte",
    r"\bpg/ml\b": "pmol/L ou ng/L selon l'analyte",
    # `/mm3` : meme unite que `/mm³`, exposant non typographie. La frontiere de
    # mot a droite empeche d'attraper un volume ecrit « 5 mm30 ».
    r"/mm3\b": "G/L (x0,001)",
    # mEq : milliequivalent, unite anglo-saxonne. Pour le potassium 1 mEq =
    # 1 mmol ; les laboratoires suisses rendent en mmol/L.
    r"\bmEq\b": "mmol/L",
    # Livres et pounds — poids en unites imperiales. Voir l'entete pour le
    # bordage numerique, indispensable (« livres » = ouvrages).
    r"\blbs?\b": "kg (1 lb = 0,4536 kg)",
    r"\b\d+\s+livres?\b": "kg (1 livre = 0,4536 kg)",
    # `g%` — gramme pour 100 mL, graphie ARCHAIQUE du g/dL. Deux occurrences
    # trouvees par le releve k3 (« Hb 16 g% », deux versions du meme cas d'AVC)
    # qu'aucun motif d'unite existant ne voyait : ni `g/dL` ni `g/dl` n'en est
    # sous-chaine. 16 g% = 16 g/dL = 160 g/L. Le `\b` de gauche empeche
    # d'attraper « mg% » ou « µg% », qui appelleraient un autre facteur.
    r"\bg%": "g/L (1 g% = 1 g/dL = 10 g/L)",
}

# ---------------------------------------------------------------------------
# MARQUES — specialites americaines absentes du marche suisse
# ---------------------------------------------------------------------------
# Chacune est en CONTRADICTION INTERNE avec une specialite suisse deja employee
# ailleurs dans le meme corpus — ce n'est pas une preference de style mais une
# incoherence mesuree :
#
#   Coumadin (47 occ / 2 grilles)  contre  Sintrom® et Marcoumar® (4 + 4)
#   Ativan   (13 occ / 4 grilles)  contre  Temesta®  (12 occ / 6 grilles)
#   Versed   ( 7 occ / 2 grilles)  contre  Dormicum® (13 occ / 4 grilles)
#
# `Coumadin` est le cas le plus net : la warfarine n'est pas commercialisee en
# Suisse. Un candidat suisse ne rencontrera jamais ce nom, et la conduite a
# tenir devant un surdosage differe (phenprocoumon et acenocoumarol ont des
# demi-vies tres differentes de la warfarine).
MARQUES = {
    r"\bCoumadin\b": "Sintrom® (acenocoumarol) ou Marcoumar® (phenprocoumon)",
    r"\bAtivan\b": "Temesta® (lorazepam)",
    r"\bVersed\b": "Dormicum® (midazolam)",
    r"\bDilantin\b": "phenytoine (Phenhydan®)",
    r"\bPepto-?Bismol\b": "sous-salicylate de bismuth (non commercialise en Suisse)",
}

# ---------------------------------------------------------------------------
# ANGLICISMES — acronymes anglophones, microbiologie comprise
# ---------------------------------------------------------------------------
# Les douze premiers ont un hit non nul sur ce corpus ; les quatorze suivants
# sont a zero et servent de prophylaxie (ils viennent du releve RESCOS, ou ils
# etaient eux aussi a zero apres passe). Aucun n'a d'homographe francais connu
# — c'est ce qui les distingue de `TB`, `MST`, `VRE`, `QID`, `ASA`, `Rx`,
# `AAA`, `AF`, `CHF`, `OR` et `PE`, tous ecartes (voir SANS_MOTIF ci-dessous).
ANGLICISMES = {
    r"\bBMI\b": "IMC",                                              # 86 / 30
    r"gold standard": "examen (ou traitement) de reference",        # 76 / 34
    r"\bHIV\b": "VIH",                                              # 35 / 11
    r"\bMRSA\b": "SARM",                                            # 33 /  4
    r"\bPCI\b": "angioplastie coronarienne",                        # 31 /  2
    r"\bFIT\b": "test immunologique fecal",                         # 16 /  4
    r"\bANA\b": "AAN (anticorps anti-nucleaires)",                  #  9 /  4
    r"\bCABG\b": "pontage (aorto-)coronarien",                      #  8 /  1
    r"\bPID\b": "salpingite / infection genitale haute",            #  3 /  2
    r"\bDMARDs?\b": "traitement de fond",                           #  3 /  1
    r"\bBUN\b": "uree",                                             #  2 /  1
    r"\bCOPD\b": "BPCO",                                            #  1 /  1
    # --- termes institutionnels FRANCAIS (et non anglophones) --------------
    # Meme critere que les marques : contradiction interne mesuree.
    #   EHPAD (4 occ / 1 grille) contre EMS (73 occ / 10 grilles), le terme
    #   suisse, employe par le corpus lui-meme y compris dans une reponse de
    #   patient (« je vais devoir aller en EMS ? »).
    #   IDE (4 occ / 1 grille) — infirmier diplome d'Etat, titre francais ;
    #   la Suisse dit « infirmier/ere ». Aucun homographe dans le corpus.
    r"\bEHPAD\b": "EMS (etablissement medico-social)",              #  4 /  1
    r"\bIDE\b": "infirmier/ere",                                    #  4 /  1
    # --- AJOUTS DU RELEVE k3 -----------------------------------------------
    # Releve independant : tous les acronymes MAJUSCULES de 2 a 8 caracteres du
    # TEXTE VISIBLE des 198 grilles (script/style retires), 3563 jetons
    # distincts, juges un par un. Les huit retenus ci-dessous ont le meme
    # critere que les marques : CONTRADICTION INTERNE MESUREE — la forme suisse
    # est deja employee ailleurs dans le meme corpus, parfois dans la meme
    # grille. Aucun n'a d'homographe francais (voir SANS_MOTIF pour les onze
    # qui en ont un et qui ont ete ecartes a ce titre).
    #
    #   DOAC 36/5   contre AOD 22/8 et ACOD 15/4
    #   ERCP 25/3   contre CPRE  6/2 — et glose par le corpus lui-meme
    #   MCV  22/5   contre VGM  16/5
    #   ARDS 12/5   contre SDRA  2/2 — glose « (Syndrome de Detresse Resp. Aigue) »
    #   MCHC 11/2   contre CCMH  1/1
    #   ALT  10/2   contre ALAT 85/33
    #   AST   8/1   contre ASAT 83/33
    #   MCH   2/1   contre TCMH  0    (seule sans temoin interne ; suit MCV/MCHC)
    #
    # `\bMCH\b` ne peut pas attraper `MCHC` : le `\b` de droite exige une
    # frontiere apres le « H », que le « C » suivant interdit. Les deux motifs
    # coexistent donc sans se recouvrir.
    r"\bDOACs?\b": "AOD (anticoagulant oral direct)",               # 36 /  5
    r"\bERCP\b": "CPRE (cholangio-pancreatographie retrograde endoscopique)",
    r"\bMCV\b": "VGM (volume globulaire moyen)",                    # 22 /  5
    r"\bARDS\b": "SDRA (syndrome de detresse respiratoire aigue)",  # 12 /  5
    r"\bMCHC\b": "CCMH (concentration corpusculaire moyenne en Hb)", # 11 /  2
    r"\bALT\b": "ALAT",                                             # 10 /  2
    r"\bAST\b": "ASAT",                                             #  8 /  1
    r"\bMCH\b": "TCMH (teneur corpusculaire moyenne en Hb)",        #  2 /  1
    # `WHO` — une seule occurrence (« definition WHO : Hb <13 g/dl homme »),
    # dans une grille qui ecrit OMS partout ailleurs. Le corpus emploie `OMS`
    # 55 fois. Aucun homographe : `WHO` n'est pas un mot francais.
    r"\bWHO\b": "OMS",                                              #  1 /  1
    # `pPCI` — angioplastie primaire. N'etait PAS compte dans les 31 `\bPCI\b`
    # du releve k1 : dans « pPCI » le « p » minuscule est un caractere de mot,
    # donc `\bPCI\b` n'y trouve pas de frontiere gauche. 20 occurrences dans la
    # grille STEMI, restees invisibles jusqu'au releve k3. Motif distinct plutot
    # que `\bp?PCI\b`, pour que le recapitulatif les compte separement.
    r"pPCI": "angioplastie primaire",                               # 20 /  1
    # --- second balayage k3 : la QUEUE du releve (moins de 9 occurrences) ---
    # Le premier balayage s'etait arrete aux jetons frequents. La queue en
    # portait neuf de plus, tous en contradiction interne mesuree :
    #   SNRI  8/2  contre IRSN 11/3   — et « ISRS, SNRI » dans la MEME phrase
    #   SSRI  7/2  contre ISRS 63/17
    #   EUS   7/2  contre « echo-endoscopie », employe partout ailleurs
    #   LDCT  8/1  contre « CT thoracique faible dose », glose de la meme ligne
    #   NPO   2/2  contre « a jeun », 5 fois dans les memes deux grilles
    #   MRI   2/1  contre IRM 879/115 — c'etait « IRM ... (mp-MRI) »
    #   TTE   1/1  contre ETT 145/29
    #   TEE   1/1  contre ETO  23/7
    #   OTC   1/1  contre « en vente libre »
    r"\bSSRI\b": "ISRS",                                             #  7 /  2
    r"\bSNRI\b": "IRSN",                                             #  8 /  2
    r"\bEUS\b": "echo-endoscopie",                                   #  7 /  2
    r"\bLDCT\b": "CT thoracique faible dose",                        #  8 /  1
    r"\bNPO\b": "a jeun",                                            #  2 /  2
    r"\bMRI\b": "IRM",                                               #  2 /  1
    r"\bTTE\b": "ETT",                                               #  1 /  1
    r"\bTEE\b": "ETO",                                               #  1 /  1
    r"\bOTC\b": "en vente libre",                                    #  1 /  1
    # --- a zero sur les 198 grilles, gardes en prophylaxie ------------------
    r"\bMSSA\b": "SASM",
    r"\bESBL\b": "BLSE",
    r"\bMDRO\b": "BMR (bacterie multiresistante)",
    r"\bUTI\b": "IVU (infection des voies urinaires)",
    r"\bSTD\b": "IST",
    r"\bSTI\b": "IST",
    r"\bESR\b": "VS (vitesse de sedimentation)",
    r"anti-DNA": "anti-ADN natif",
    r"\bSCFE\b": "epiphysiolyse femorale superieure",
    r"\bIVDU\b": "usage de drogues par voie intraveineuse",
    r"\bPRN\b": "a la demande / si besoin",
    r"[Gg]iant cells?": "cellules geantes",
    r"\bN/V\b": "nausees et vomissements",
    r"\bDM\b": "diabete",
}

# ---------------------------------------------------------------------------
# SANS_MOTIF — mesures, puis deliberement NON bannis
# ---------------------------------------------------------------------------
# Consigne ici plutot qu'en commentaire libre, pour qu'un lot futur qui
# voudrait « completer la table » retrouve la raison du refus avec son chiffre.
# Chaque ligne est (jeton, occurrences sur CasECOS, raison).
SANS_MOTIF = [
    ("112", 593, "toutes dans la CSS : rgb(112, 188, 123)"),
    ("AAA", 124, "anevrisme de l'aorte abdominale — sigle francais et anglais confondus"),
    ("ASA", 89, "score ASA (American Society of Anesthesiologists) et 5-ASA — "
                "deux usages corrects, aucun n'est un anglicisme a corriger"),
    ("Rx", 51, "graphie SUISSE de la radiographie (« Rx thorax ») — faux ami parfait"),
    ("CHF", 20, "FRANC SUISSE (« coût 27-40 CHF »), pas congestive heart failure"),
    ("TB", 19, "TB-MDR / MDR-TB (tuberculose multiresistante) et « trouble bipolaire (TB) »"),
    ("guidelines", 18, "usage installe en francais medical (« selon les guidelines ESC 2021 »)"),
    ("check-up", 11, "glose par la grille elle-meme : « check-up (examen medical periodique) »"),
    ("Lopressor", 13, "metoprolol, specialite Novartis enregistree en Suisse"),
    ("Glucophage", 9, "metformine, enregistree en Suisse"),
    ("MST", 4, "« MST Continus® » = morphine a liberation prolongee"),
    ("livres", 3, "« Associations de patients, livres, groupes de soutien » = ouvrages"),
    ("Lasix", 3, "furosemide, enregistre par Swissmedic"),
    ("OR", 3, "odds ratio (« Facteurs forts (OR >10) »)"),
    ("VRE", 2, "ici enterocoque resistant, mais volume de reserve expiratoire sur AMBOSS-19"),
    ("AF", 2, "antecedents familiaux, et tenofovir-AF"),
    ("Zofran", 2, "ondansetron, enregistre par Swissmedic"),
    ("screening", 2, "meme famille que `guidelines` — style, pas nomenclature"),
    ("PE", 1, "preeclampsie"),
    ("mmol/l, mg/l, U/l, G/l", 265, "unites SI correctes, « l » minuscule — "
                                    "variante typographique, pas une erreur"),
    # --- termes institutionnels mesures et ecartes -------------------------
    ("HAS", 15, "Haute Autorite de Sante, citee comme source de criteres "
                "(« criteres GLIM 2018 / HAS 2021 ») — et surtout homographe "
                "du verbe anglais « has »"),
    ("LAMal", 18, "loi suisse — a conserver"),
    ("OFSP", 13, "office federal suisse — a conserver"),
    ("Swissmedic", 10, "agence suisse — a conserver"),
    ("AMM", 4, "« hors AMM en Suisse » : usage installe, meme si l'autorisation "
               "suisse est delivree par Swissmedic"),
    ("SMUR", 3, "service mobile d'urgence et de reanimation — existe bel et bien "
                "en Suisse romande (« Contacter le SMUR ou le 144 »)"),
    ("CHU", 3, "dont « CHU Ste-Justine », nom propre d'un hopital montrealais "
               "cite comme source d'algorithme"),
    # --- releve k3 : jetons anglophones D'APPARENCE, tous ecartes -----------
    # Onze homographes francais qu'une table « acronymes anglais » naive aurait
    # bannis. Chacun a ete lu en contexte avant d'etre ecarte ; c'est la moitie
    # la plus utile du releve k3.
    ("MI", 113, "MEMBRES INFERIEURS (« Doppler veineux MI », « œdemes des MI ») "
                "et non myocardial infarction — le corpus ecrit IDM (107 occ)"),
    ("IU", 36, "INFECTION URINAIRE (« les IU simples », « ECBU : elimination IU ») "
               "et non international units — le corpus ecrit UI (84 occ)"),
    ("PTT", 36, "graphie SUISSE de la crase (« TP 60%, PTT 30s », « TP/PTT/plaquettes ») : "
                "les laboratoires suisses rendent TP + PTT la ou la France ecrit "
                "TP + TCA. Ce n'est PAS le purpura thrombotique thrombocytopenique"),
    ("DAPT", 35, "double antiagregation plaquettaire — sigle des recommandations ESC, "
                 "installe en francais de cardiologie"),
    ("NIPT", 34, "test prenatal non invasif : usage suisse installe (OFSP, FMH), "
                 "et glose par la grille elle-meme « NIPT / DPNI »"),
    ("EGFR", 21, "RECEPTEUR du facteur de croissance epidermique (« mutations EGFR, "
                 "ALK, ROS1 ») — un gene, pas le debit de filtration glomerulaire"),
    ("HIT", 19, "HEAD IMPULSE TEST du protocole HINTS (« HIT pathologique gauche ») "
                "et non heparin-induced thrombocytopenia"),
    ("PCC", 19, "concentre de complexe prothrombinique (« vitamine K + PCC "
                "(Beriplex/Octaplex) ») — sigle installe des protocoles suisses"),
    ("OAC", 18, "Ordonnance reglant l'Admission a la Circulation routiere, "
                "ORDONNANCE FEDERALE SUISSE (« OAC art. 27 ») — a conserver"),
    ("IBS", 16, "INFECTION BACTERIENNE SERIEUSE du nourrisson (« risque d'IBS tres "
                "eleve ») et non irritable bowel syndrome — le corpus ecrit SII"),
    ("ADHD", 7, "toutes dans des NOMS PROPRES d'echelles : « Adult ADHD Self-Report "
                "Scale (ASRS) », « Conners Adult ADHD Rating Scale », « Diagnostic "
                "Interview for ADHD in adults (DIVA 2.0) ». La grille ecrit TDAH "
                "(59 occ) pour le trouble lui-meme"),
    ("PTSD", 3, "meme raison : « PCL-5 (PTSD Checklist for DSM-5) » et « CAPS-5 "
                "(Clinician-Administered PTSD Scale for DSM-5) ». Le corpus ecrit "
                "TSPT (49 occ) et ESPT"),
    ("HCT", 1, "corrigee en `Ht` a la main, mais PAS ajoutee a BANNED : `HCT` est "
               "aussi l'abreviation courante de l'HYDROCHLOROTHIAZIDE. Un motif "
               "ici ferait signaler une prescription comme faute d'unite"),
    ("CD4", 2, "un taux de CD4 se rend en /µL partout, y compris en Suisse ; "
               "0,014 G/L n'a pas de sens clinique. FAUX POSITIF du motif "
               "hemogramme+/µL importe d'AMBOSS, evite par reformulation"),
    # --- releve k3 : anglicismes reels, mesures et NON traites -------------
    # Ils ne sont pas dans BANNED : chacun demanderait plus qu'une substitution
    # de nomenclature. Consignes ici pour qu'un lot futur les retrouve.
    ("HBV / HCV", 57, "VHB (50) et VHC (22) coexistent avec HBV (15) et HCV (42) : "
                      "contradiction interne REELLE, non traitee parce que « Cirrhose "
                      "HCV et CHC » est dans le NOM DE FICHIER d'une grille et dans "
                      "index.html, tous deux hors du perimetre de ce lot"),
    ("SCLC / NSCLC", 30, "CBPC (5) et CBNPC (7) presents dans la MEME grille : "
                         "contradiction reelle, mais les sigles y sont gloses en "
                         "anglais (« SCLC (Small Cell Lung Cancer) ») — la correction "
                         "est une reecriture, pas une substitution"),
    ("Gold Standards Framework", 3, "nom propre d'un outil britannique d'identification "
                                    "des patients palliatifs. C'est pour lui que le motif "
                                    "`gold standard` doit rester SENSIBLE A LA CASSE"),
    ("bleuets", 8, "quebecisme pour myrtilles, dans la liste des causes factices de "
                   "melena — vocabulaire, pas nomenclature medicale"),
]

# Copie, jamais la reference : muter la table d'AMBOSS en place ferait dependre
# son contenu de l'ordre des imports si plusieurs corpus tournaient dans le meme
# processus.
BANNED = dict(lib.amboss_module("check_nomenclature").BANNED)
BANNED.update(UNITES)
BANNED.update(MARQUES)
BANNED.update(ANGLICISMES)


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    total = 0
    per_pattern = {}
    for path in lib.grids():
        if not lib.matches(path, only):
            continue
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        for pattern, repl in BANNED.items():
            hits = re.findall(pattern, html)
            if hits:
                total += len(hits)
                per_pattern[pattern] = per_pattern.get(pattern, 0) + len(hits)
                print(f"  {path.name}: {len(hits)}x {pattern} -> attendu {repl}")
    if total:
        print("\n--- recapitulatif par motif ---")
        for pattern, n in sorted(per_pattern.items(), key=lambda kv: -kv[1]):
            print(f"  {n:6d}  {pattern}  -> {BANNED[pattern]}")
        print(f"\nECHEC — {total} terme(s) non suisse(s) restant(s)")
        return 1
    print("OK — aucun terme non suisse detecte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
