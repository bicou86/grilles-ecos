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
