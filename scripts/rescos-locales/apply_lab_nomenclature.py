"""Passe de nomenclature suisse sur les 165 grilles de `cases/rescos-locales`.

Usage :
    python3 scripts/rescos-locales/apply_lab_nomenclature.py --check   # a blanc
    python3 scripts/rescos-locales/apply_lab_nomenclature.py           # ecrit

DEUX REGISTRES, ET LA RAISON DE LES SEPARER
============================================
`CIBLES` — remplacement mecanique, applique a TOUTES les grilles. N'y figure
qu'un terme dont le VOISINAGE a ete releve occurrence par occurrence et dont le
remplacement est un DROP-IN : la phrase reste grammaticale et le sens intact,
quelle que soit l'occurrence. Le releve de voisinages est reproductible :

    python3 - <<'EOF'
    import re, sys; sys.path.insert(0, "scripts/rescos-locales")
    import lib_rescos_locales as lib
    from collections import Counter
    c = Counter()
    for p in lib.grids():
        h = lib.strip_base64(p.read_text(encoding="utf-8"))
        for m in re.finditer(r"\\bNFS\\b", h):
            c[h[m.start()-26:m.end()+26]] += 1
    EOF

`EDITS` — remplacement UNIQUE, ancre sur une grille et verifie au compte exact.
Tout ce dont le texte voisin bouge : conversion d'unite (le NOMBRE change), mot
grammatical a accorder, parenthese devenue redondante, faux positif francais.
Aucun `sed` uniforme ne peut faire ce travail — la campagne rescos l'avait paye
sur « Methotrexate = gold standard », qui serait devenu « = examen de reference ».

LES QUATRE PIEGES DE CE CORPUS, MESURES
========================================
1. PLUSIEURS VALEURS SUR UNE LIGNE. « Hb > 7-9 g/dL, plaquettes > 50 000 »
   (AMC Urgences 1) porte DEUX unites fausses de deux familles differentes ;
   « Leucocytes < 4000 ou > 20000 » (AMC Urgences 5C) en porte deux de la meme.
   Chaque edition couvre la LIGNE, jamais le premier nombre seul.
2. L'ANALYTE DECIDE DU FACTEUR. Les 6 `mg/dL` sont 1 creatinine (x88,4),
   4 glycemies (/18) et 1 bilirubine deja rendue en SI (parenthese a retirer).
   Un facteur unique aurait ecrit « creatinine 140 mmol/L » ou « glycemie
   17 700 µmol/L ». Les 14 `ng/mL`+`ng/ml` sont 8 D-dimeres (x1 -> µg/L),
   1 troponine (x1000 -> ng/L), 4 PCT et 1 PSA (x1 -> µg/L) : trois unites
   d'arrivee pour une seule unite de depart.
3. LE QUALIFICATIF VOISIN. Il sert de CONTROLE, pas seulement de decor :
   « CRP [17 mg/ml - legerement elevee] » ne peut pas etre du mg/mL (17 mg/mL
   = 17 000 mg/L, ni legere ni compatible avec la vie clinique du dossier).
   C'est le qualificatif qui prouve que l'unite voulue etait mg/L, et que la
   correction est une COQUILLE a redresser sans toucher au nombre.
4. LE BORDAGE. Trois motifs evidents ont ete ecartes sur un faux positif
   FRANCAIS mesure dans ce corpus meme — voir l'en-tete de
   `check_nomenclature.py`, section « ecartes apres mesure ».
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib  # noqa: E402

# --------------------------------------------------------------------------
# Regions INTOUCHABLES. Masquees avant toute substitution, restaurees apres.
#
# `<style>` : les 165 grilles portent leur mise en page EN LIGNE (0 `case-styles.css`).
#   Un motif de trois lettres y rencontre des noms de classe et des valeurs CSS —
#   mesure : `gb` de `rgba(...)` suivi de `z-index: 1000` matche le motif de
#   numeration implicite si on le rend insensible a la casse sans precaution.
# `<script>` : depuis le lot `l3`, 156 grilles portent `window.caseConfig` et
#   `<script src="../scoring.js">`. Le bareme ne doit pas bouger.
# `data:` : 11 images en base64. `\bNFS\b` a toutes les chances de tomber dans
#   une charge utile de 40 000 caracteres aleatoires.
_MASKED = [
    re.compile(r"<style[^>]*>.*?</style>", re.S | re.I),
    re.compile(r"<script[^>]*>.*?</script>", re.S | re.I),
    re.compile(r"data:[A-Za-z0-9+/;,=._-]{40,}"),
]


def _mask(html):
    store = []

    def keep(m):
        store.append(m.group(0))
        return f"\x00{len(store) - 1}\x00"

    for rx in _MASKED:
        html = rx.sub(keep, html)
    return html, store


def _unmask(html, store):
    return re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], html)


# --------------------------------------------------------------------------
# CIBLES — drop-in verifie sur la totalite des occurrences.
#
# Chaque ligne porte le compte releve AVANT la passe. Les exceptions sont
# traitees par `EDITS`, qui s'applique EN PREMIER : quand le mecanique passe,
# elles ont deja disparu du fichier.
CIBLES = [
    # 208 NFS - 3 exceptions traitees en EDITS = 205 mecaniques.
    # `FSC` est deja le terme du corpus : 36 occurrences sur 23 grilles.
    (r"\bNFS\b", "FSC"),
    # 26 BMI - 1 exception (mnemonique BODE) = 25. `IMC` : 64 occurrences.
    (r"\bBMI\b", "IMC"),
    # 13 HIV - 2 exceptions (hemorragie intraventriculaire ; nom de site) = 11.
    (r"\bHIV\b", "VIH"),
    # 13 ANA. Deux tombent dans le mnemonique anglais SOAP BRAIN MD (« A = ANA ») :
    # `AAN` commence aussi par A, la lettre du mnemonique est preservee.
    (r"\bANA\b", "AAN"),
    # 10 MRSA, dont 2 « anti-MRSA » -> « anti-SARM ».
    (r"\bMRSA\b", "SARM"),
    # 9 ERCP. `CPRE` est deja le terme du corpus : 14 occurrences sur 2 grilles.
    (r"\bERCP\b", "CPRE"),
    # 1 Doliprane. Prolonge l'entree `Tylenol -> Dafalgan` de la table AMBOSS :
    # meme molecule, meme geste, marque francaise au lieu de la marque US.
    (r"\bDoliprane\b", "Dafalgan"),
    # 41 « gold standard », dont 8 capitalises — la casse etait le tiers du
    # relevé manquant. 5 exceptions en EDITS (1 traitement, 1 echelle, 3
    # accords) = 36 mecaniques.
    (r"\bgold standard\b", "examen de référence"),
    (r"\bGold standard\b", "Examen de référence"),
]

# --------------------------------------------------------------------------
# EDITS — (fragment de nom de grille, motif, remplacement, compte attendu).
#
# Le compte attendu est VERIFIE : un motif qui ne trouve pas exactement ce
# nombre d'occurrences fait echouer la passe entiere, sans rien ecrire.
EDITS = [
    # === mg/dL : SIX occurrences, TROIS analytes, TROIS facteurs ============
    # Creatinine : x 88,4 -> µmol/L. 2,5 mg/dL = 221 µmol/L.
    ("AMC Urgences 3B", r"créat < 2\.5 mg/dL", "créat < 221 µmol/L", 1),
    # Glycemie : / 18 -> mmol/L. C'est le piege du mandat : ces quatre valeurs
    # passees au facteur 88,4 de la creatinine auraient donne « glycemie a jeun
    # >= 11 138 µmol/L ».
    ("AMC Urgences 5B", r"\[Cible 140-180 mg/dL\]", "[Cible 7.8-10 mmol/L]", 1),
    ("Diabète pédiatrique - Garçon de 9 ans - Grille", r"Glycémie aléatoire ≥ 200 mg/dL avec symptômes",
     "Glycémie aléatoire ≥ 11.1 mmol/L avec symptômes", 1),
    ("Diabète pédiatrique - Garçon de 9 ans - Grille", r"Glycémie à jeun ≥ 126 mg/dL à 2 reprises",
     "Glycémie à jeun ≥ 7.0 mmol/L à 2 reprises", 1),
    ("Diabète pédiatrique - Garçon de 9 ans - Grille", r"Glycémie ≥ 200 mg/dL après 2 h",
     "Glycémie ≥ 11.1 mmol/L après 2 h", 1),
    # Bilirubine : la valeur SI est DEJA la (50 µmol/L). Le mg/dL n'est qu'un
    # doublon US entre parentheses — on le retire, on ne le convertit pas.
    # Controle : 3 mg/dL x 17,1 = 51,3 µmol/L, coherent avec le « >50 » ecrit.
    ("RESCOS-47", r"bilirubine >50 μmol/L \(3 mg/dL\)", "bilirubine >50 μmol/L", 1),

    # === g/dL et g/dl : SEPT occurrences, toutes de l'hemoglobine, x 10 =====
    # PIEGE N° 1 : cette ligne porte AUSSI « plaquettes > 50 000 » (numeration
    # en unite implicite). Ne convertir que l'hemoglobine laisserait un seuil
    # de plaquettes muet a cote d'un seuil d'hemoglobine corrige.
    ("AMC Urgences 1 - Polytraumatisé",
     r"Hb > 7-9 g/dL, plaquettes > 50 000, INR < 1\.5",
     "Hb > 70-90 g/L, plaquettes > 50 G/L, INR < 1.5", 1),
    ("Choc septique pulmonaire", r"Transfusion si Hb < 7 g/dL",
     "Transfusion si Hb < 70 g/L", 1),
    ("USIT2 - Diarrhée", r"Hb < 7 g/dL", "Hb < 70 g/L", 1),
    # PIEGE N° 1, forme intervalle : les DEUX bornes doivent bouger.
    ("RESCOS-50", r"Hb < 7-8 g/dL", "Hb < 70-80 g/L", 1),
    ("SMIG-4", r"\[Hb 10\.5 g/dL,", "[Hb 105 g/L,", 1),
    ("RESCOS-58 - Rectorragies", r"Hémoglobine < 8 g/dl", "Hémoglobine < 80 g/L", 1),
    ("RESCOS-58 - Rectorragies", r"Hb < 7-8 g/dl", "Hb < 70-80 g/L", 1),

    # === ng/mL et ng/ml : QUATORZE occurrences, TROIS unites d'arrivee ======
    # D-dimeres : 1 ng/mL = 1 µg/L (x 1). Huit occurrences.
    ("AMC Urgences 2A", r"\[> 5000 ng/mL\]", "[> 5000 µg/L]", 1),
    ("AMC Urgences 3C", r"\(< 500 ng/mL exclut", "(< 500 µg/L exclut", 1),
    ("Dyspnée post-COVID", r"D-dimères élevés \(805 ng/ml\)",
     "D-dimères élevés (805 µg/L)", 1),
    ("Dyspnée post-COVID", r"\[805 ng/ml - élevés\]", "[805 µg/L - élevés]", 1),
    ("Dyspnée post-COVID", r"\[48 x 10 = 480 ng/ml\]", "[48 x 10 = 480 µg/L]", 1),
    ("Dyspnée post-COVID", r"\[805 ng/ml - au-dessus du seuil\]",
     "[805 µg/L - au-dessus du seuil]", 1),
    ("Dyspnée post-COVID", r"Si < 500 ng/ml \+ YEARS", "Si < 500 µg/L + YEARS", 1),
    ("Dyspnée post-COVID", r"D-dimères à 805 ng/ml \(N < 500\)",
     "D-dimères à 805 µg/L (N < 500)", 1),
    # Troponine : 1 ng/mL = 1000 ng/L (x 1000). SEULE occurrence du corpus, et
    # seule de la famille a changer d'ordre de grandeur. PIEGE N° 1 : la meme
    # ligne porte un BNP en pg/mL, autre analyte, autre facteur.
    ("AMC Urgences 2A", r"Troponine I > 0\.4 ng/mL, BNP > 100 pg/mL",
     "Troponine I > 400 ng/L, BNP > 100 ng/L", 1),
    # Procalcitonine : 1 ng/mL = 1 µg/L (x 1).
    ("AMC Urgences 2B", r"\[15 ng/mL\]", "[15 µg/L]", 1),
    ("RESCOS-46", r"PCT: >0\.5 ng/mL évocateur", "PCT: >0.5 µg/L évocateur", 1),
    ("Pédiatrie - État fébrile", r"PCT < 0\.5 ng/ml = 0 pt",
     "PCT < 0.5 µg/L = 0 pt", 1),
    ("Pédiatrie - État fébrile", r"PCT > 0\.5 ng/ml: meilleur",
     "PCT > 0.5 µg/L: meilleur", 1),
    # PSA : 1 ng/mL = 1 µg/L (x 1).
    ("Dépistage cancer prostate", r"\[< 4 ng/ml généralement\]",
     "[< 4 µg/L généralement]", 1),

    # === pg/mL et pg/ml : HUIT occurrences, toutes BNP/NT-proBNP, x 1 ======
    # ng/L, PAS pmol/L : le facteur 0,738 est celui de la vitamine B12, qui
    # n'est dosee nulle part dans ce corpus (verifie : 3 occurrences de « B12 »,
    # aucune avec une valeur).
    ("AMC Urgences 2A", r"\[850 pg/mL\]", "[850 ng/L]", 1),
    ("AMC Urgences 3B", r"BNP > 100 pg/mL ou NT-proBNP > 300 pg/mL",
     "BNP > 100 ng/L ou NT-proBNP > 300 ng/L", 1),
    ("SMIG-5", r"\[Élevé > 1000 pg/mL\]", "[Élevé > 1000 ng/L]", 1),
    ("SMIG-5", r"> 100/300 pg/mL diagnostic", "> 100/300 ng/L diagnostic", 1),
    ("Mal à l'épaule", r"\[110 pg/ml - normale\]", "[110 ng/L - normale]", 1),
    ("RESCOS-54", r"> 900 pg/ml significatif", "> 900 ng/L significatif", 1),

    # === mEq/L et mEq/l : QUATRE occurrences ===============================
    # Lactate et potassium sont monovalents : 1 mEq = 1 mmol, le nombre ne
    # bouge pas. Le qualificatif « normal » reste juste a 0,4 mmol/L.
    ("Baisse de l'état général", r"\[0\.4 mEq/l - normal\]", "[0.4 mmol/L - normal]", 1),
    ("Mal au dos - Syndrome de Guillain-Barré - Grille ECOS (1)", r"\[0\.4 mEq/l - normal\]",
     "[0.4 mmol/L - normal]", 1),
    ("Mal au dos 2 - Syndrome de Guillain", r"\[0\.4 mEq/l - normal\]",
     "[0.4 mmol/L - normal]", 1),
    ("Douleur abdominale et diarrhée fébrile", r"KCl 20-40 mEq/L",
     "KCl 20-40 mmol/L", 1),

    # === mg/mL sur la CRP : DEUX coquilles, pas des conversions =============
    # PIEGE N° 4 retourne : c'est le QUALIFICATIF qui identifie l'unite voulue.
    # 17 mg/mL vaudrait 17 000 mg/L ; « legerement elevee » ne peut designer
    # que 17 mg/L. Le nombre est juste, l'unite est fausse — on ne convertit
    # pas, on redresse. `mg/mL` n'est JAMAIS banni globalement : c'est l'unite
    # de la PC20 a la methacholine (2 occurrences legitimes sur AMBOSS-18).
    ("Baisse de l'état général", r"\[17 mg/ml - légèrement élevée\]",
     "[17 mg/L - légèrement élevée]", 1),
    ("Mal à l'épaule", r"\[46 mg/ml - élevée\]", "[46 mg/L - élevée]", 1),

    # === /mm³ : DIX-SEPT occurrences, DEUX destinations selon le liquide ====
    # LCR — 1/mm³ = 1/µL exactement, le nombre ne bouge pas. Le G/L y serait
    # faux d'usage : une cellularite de LCR se rend en /µL, jamais en G/L.
    ("AMC Urgences 5C", r"\[8500/mm³, 95% PNN\]", "[8500/µL, 95% PNN]", 1),
    ("Baisse de l'état général", r"\[15/mm³\]", "[15/µL]", 1),
    ("Céphalées - Vignette clinique", r"Cellules: <5/mm³ normal",
     "Cellules: <5/µL normal", 1),
    ("Mal au dos - Syndrome de Guillain-Barré - Grille ECOS (1)", r"\[15/mm³\]", "[15/µL]", 1),
    ("Mal au dos 2 - Syndrome de Guillain", r"\[15/mm³\]", "[15/µL]", 1),
    # « GB » est un terme d'hemogramme : « GB 1200/µL » retomberait dans le
    # motif `_MICROLITRE_ETENDU` de la porte. « elements » est le terme
    # consacre de la cellularite du LCR et leve l'ambiguite.
    ("Pédiatrie - Vomissements", r"\[GB 1200/mm³\]", "[1200 éléments/µL]", 1),
    ("Pédiatrie - Vomissements", r"Normal: < 5 GB/mm³,", "Normal: < 5 éléments/µL,", 1),
    # Sang et liquide articulaire — x 0,001 -> G/L.
    ("Enfant qui boîte", r"GB > 12000/mm³", "GB > 12 G/L", 3),
    ("Fièvre et douleurs articulaires - Infection",
     r"> 50'000 GB/mm³", "> 50 G/L", 1),
    ("Pédiatrie - Nouveau-né en détresse",
     r"GB 2800/mm³, neutrophiles 49%, thrombocytes 85000/mm³",
     "GB 2.8 G/L, neutrophiles 49%, thrombocytes 85 G/L", 1),
    ("Pédiatrie - Vomissements", r"\[366'000/mm³\]", "[366 G/L]", 1),
    ("RESCOS-63", r"\(>10 000/mm³\)", "(> 10 G/L)", 1),
    ("RESCOS-63", r"hyperlymphocytose > 10 000/mm³", "hyperlymphocytose > 10 G/L", 1),

    # === numeration en unite implicite : HUIT lignes, NEUF valeurs ==========
    # Le relevé annoncait 8 occurrences ; le motif d'origine en trouvait 8 dont
    # DEUX FAUSSES, et en manquait DEUX par sensibilite a la casse (voir
    # `check_nomenclature.py`). Vrai total : 8 lignes, 9 valeurs.
    # (« plaquettes > 50 000 » d'AMC Urgences 1 est traite avec son Hb ci-dessus.)
    ("AMC Urgences 2B", r"\[GB 18000, neutrophiles 85%\]",
     "[GB 18 G/L, neutrophiles 85%]", 1),
    ("AMC Urgences 2B", r"Plaquettes 180 000", "Plaquettes 180 G/L", 1),
    ("AMC Urgences 2B", r"plaquettes si < 20000", "plaquettes si < 20 G/L", 1),
    ("AMC Urgences 5C", r"thrombopénie < 50 000", "thrombopénie < 50 G/L", 1),
    # PIEGE N° 1 : DEUX valeurs sur la meme ligne, meme analyte.
    ("AMC Urgences 5C", r"Leucocytes < 4000 ou > 20000",
     "Leucocytes < 4 G/L ou > 20 G/L", 1),
    ("Enfant qui boîte", r"GB 8000 - normal", "GB 8 G/L - normal", 1),
    ("Enfant qui boîte", r"\(GB 8000, CRP 20 mg/l", "(GB 8 G/L, CRP 20 mg/l", 1),

    # === °F : une temperature en Fahrenheit, doublon du °C deja present =====
    ("RESCOS-46", r"température >38\.3°C ou >101°F", "température >38.3°C", 1),

    # === HIV : DEUX faux positifs FRANCAIS sur treize occurrences ===========
    # Classification de Fisher modifiee, grade 4 : « HSA + hematome
    # intraparenchymateux ou HIV ». Ici HIV = HEMORRAGIE INTRAVENTRICULAIRE.
    # Un `sed HIV -> VIH` aurait fait du virus une complication de l'hemorragie
    # meningee. L'abreviation est developpee : elle etait illisible de toute
    # facon dans une grille ou HIV designe partout ailleurs le virus.
    ("AMC Urgences 5A", r"intraparenchymateux ou HIV",
     "intraparenchymateux ou hémorragie intraventriculaire", 1),
    # Nom propre d'une ressource : le site hiv-druginteractions.org de
    # l'universite de Liverpool. « VIH drug interactions » ne designerait rien.
    # Rendu sous sa forme d'URL, comme le « drugs.com » qui le precede.
    ("Pharmacologie clinique 3", r"\[drugs\.com, HIV drug interactions\]",
     "[drugs.com, hiv-druginteractions.org]", 1),

    # === BMI : une exception, le mnemonique BODE ===========================
    # « B: BMI | O: Obstruction | D: Dyspnee | E: Exercise » — la lettre B du
    # score porte l'acronyme. « B: IMC » romprait le mnemonique ; le terme est
    # developpe et glose.
    ("AMC Urgences 4", r"B: BMI \| O: Obstruction",
     "B: Body mass index (IMC) | O: Obstruction", 1),

    # === NFS : trois occurrences ou « FSC » rendrait la phrase redondante ===
    # FSC = formule sanguine complete : « FSC complete » se lirait « formule
    # sanguine complete complete », et la FSC inclut deja les plaquettes.
    ("Lupus érythémateux systémique - Femme de 26 ans", r"NFS complète", "FSC", 1),
    ("Diverticulite sigmoidienne", r"NFS-plaquettes", "FSC", 1),
    ("Douleur non traumatique du membre inférieur", r"NFS-plaquettes", "FSC", 1),

    # === MST : elision =====================================================
    ("RESCOS-42", r"Antécédents de MST", "Antécédents d'IST", 1),

    # === SCFE : trois occurrences, dont une deja glosee ====================
    ("Enfant qui boîte", r"SCFE <span class=\"equals\">",
     "Épiphysiolyse fémorale supérieure <span class=\"equals\">", 1),
    ("Enfant qui boîte", r"Épiphysiolyse fémorale supérieure \(SCFE\), tumeurs",
     "Épiphysiolyse fémorale supérieure, tumeurs", 1),
    ("Enfant qui boîte", r"hospitalisation si SCFE,",
     "hospitalisation si épiphysiolyse fémorale supérieure,", 1),

    # === DMARD : sept occurrences, dont DEUX ou le mecanique produirait ====
    # « Traitement de fond (traitement de fond) ».
    ("Sémiologie MSQ - Polyarthrite", r"Traitement de fond \(DMARDs\)", "Traitement de fond", 2),
    ("Sémiologie MSQ - Polyarthrite", r"Traitement précoce par DMARDs pour éviter",
     "Traitement de fond précoce pour éviter", 1),
    ("Sémiologie MSQ - Polyarthrite", r"Introduire précocement un DMARD \(",
     "Introduire précocement un traitement de fond (", 1),
    ("Sémiologie MSQ - Polyarthrite", r"</span> DMARD \(méthotrexate en 1ère intention\)",
     "</span> traitement de fond (méthotrexate en 1ère intention)", 1),
    ("Sémiologie MSQ - Polyarthrite", r"<li>DMARDs précoces \(", "<li>Traitement de fond précoce (", 1),
    ("Sémiologie MSQ - Polyarthrite", r"<li>DMARD de 1ère intention",
     "<li>Traitement de fond de 1ère intention", 1),

    # === PCI : sept occurrences, phrase a reformuler a chaque fois ==========
    ("AMC Urgences 3A", r"Thrombolyse si PCI non disponible",
     "Thrombolyse si angioplastie non disponible", 1),
    ("AMC Urgences 3A", r"\(PCI vs thrombolyse\)", "(angioplastie vs thrombolyse)", 1),
    ("Douleurs thoraciques - DRS", r"Coronarographie \+ PCI immédiate",
     "Coronarographie + angioplastie immédiate", 1),
    ("Douleurs thoraciques - DRS", r"Si délai PCI >120 min",
     "Si délai d'angioplastie >120 min", 1),
    ("Douleurs thoraciques - DRS", r"Transfert secondaire pour PCI",
     "Transfert secondaire pour angioplastie", 1),
    ("Douleurs thoraciques - DRS", r"Door-to-balloon \(PCI\)",
     "Door-to-balloon (angioplastie)", 1),
    ("Douleurs thoraciques - DRS", r"Premier contact médical-PCI",
     "Premier contact médical-angioplastie", 1),

    # === MRCP : sept occurrences. `cholangio-IRM` est deja le terme du =====
    # corpus (6 occurrences sur 2 grilles), ce qui tranche la traduction.
    # EDITS passe AVANT CIBLES : `ERCP` est encore la a ce moment, et c'est le
    # remplacement mecanique qui en fera `CPRE` juste apres.
    ("RESCOS-47", r"ERCP/MRCP si indiqué", "ERCP/cholangio-IRM si indiqué", 1),
    ("RESCOS-47", r"IRM/MRCP: alternative", "Cholangio-IRM: alternative", 1),
    ("RESCOS-47", r"IRM abdominale \+ MRCP:", "IRM abdominale + cholangio-IRM:", 1),
    ("RESCOS-56", r"CT abdominal, MRCP, CA 19-9", "CT abdominal, cholangio-IRM, CA 19-9", 1),
    ("RESCOS-56", r"→ MRCP, anticorps", "→ Cholangio-IRM, anticorps", 1),
    ("RESCOS-56", r"MRCP \(cholangio-pancréatographie",
     "Cholangio-IRM (cholangio-pancréatographie", 1),
    ("RESCOS-56", r"MRCP: cartographie", "Cholangio-IRM: cartographie", 1),

    # === BSA : quatre occurrences ==========================================
    ("Psoriasis - Femme de 42 ans", r"% de surface corporelle atteinte \(BSA\)",
     "% de surface corporelle atteinte", 1),
    ("Psoriasis - Femme de 42 ans", r"Formes légères \(< 3–5 % BSA\)",
     "Formes légères (< 3–5 % de surface corporelle)", 1),
    ("Psoriasis - Femme de 42 ans", r"Formes modérées à sévères \(> 3–5 % BSA\)",
     "Formes modérées à sévères (> 3–5 % de surface corporelle)", 1),
    ("Psoriasis - Femme de 42 ans", r"Évaluer % surface atteinte \(BSA, PASI\)",
     "Évaluer % surface atteinte, score PASI", 1),

    # === COPD, SLE, QD : une occurrence chacun =============================
    # `BPCO` : 122 occurrences dans le corpus. `LES` : 16, dans cette grille meme.
    ("RESCOS-64 - Toux - Station double 2", r"confirmer le COPD", "confirmer la BPCO", 1),
    ("Lupus érythémateux systémique - Femme de 26 ans", r"\(x2 chez patient SLE\)",
     "(x2 chez patient avec LES)", 1),
    ("Dyspnée et insuffisance cardiaque", r"Nébivolol 5mg QD", "Nébivolol 5 mg 1x/j", 1),

    # === numero d'urgence : le 15 est FRANCAIS, la Suisse compose le 144 ====
    # Le corpus emploie deja le 144 (AMC Urgences 3A, script du patient).
    ("BPCO exacerbation - Femme de 65 ans - Grille", r"Appeler le 15 si urgence", "Appeler le 144 si urgence", 1),
    ("BPCO exacerbation - Femme de 65 ans - Grille", r"médecin traitant ou le 15\.",
     "médecin traitant ou le 144.", 1),

    # === gold standard : CINQ occurrences ou « examen » serait faux ========
    # PIEGE N° 3, celui que rescos avait paye. Ici c'est l'ANGIOPLASTIE
    # PRIMAIRE qui est designee : un traitement, pas un examen.
    ("Douleurs thoraciques - DRS", r"Gold standard:<br>", "Traitement de référence:<br>", 1),
    # Une echelle d'evaluation (HAM-D), ni examen ni traitement.
    ("Dépression majeure - Homme de 36 ans - Grille", r"gold standard clinique", "référence clinique", 1),
    # Accord : « les methodes … sont LE gold standard ».
    ("RESCOS-41", r"sont le gold standard\.", "sont la méthode de référence.", 1),
    # Elision : « qui est LE gold standard » -> « qui est L'examen de reference ».
    ("Lésion de la coiffe", r"qui est le gold standard",
     "qui est l'examen de référence", 1),
    # « examen de reference diagnostique » serait pleonastique.
    ("Épilepsie absence", r"gold standard diagnostique", "examen de référence", 1),
]


def apply_to(name, html):
    """Applique EDITS puis CIBLES a une grille. Rend (html, n_edits, n_cibles)."""
    html, store = _mask(html)
    n_edits = n_cibles = 0
    for grid, pattern, repl, want in EDITS:
        if grid not in name:
            continue
        got = len(re.findall(pattern, html))
        if got != want:
            raise SystemExit(
                f"ARRET — {name}\n  motif {pattern!r}\n"
                f"  attendu {want} occurrence(s), trouve {got}. Rien n'est ecrit.")
        html = re.sub(pattern, lambda _m, r=repl: r, html)
        n_edits += got
    for pattern, repl in CIBLES:
        html, n = re.subn(pattern, lambda _m, r=repl: r, html)
        n_cibles += n
    return _unmask(html, store), n_edits, n_cibles


def main():
    check = "--check" in sys.argv[1:]
    total_e = total_c = touched = 0
    unused = {(g, p) for g, p, _, _ in EDITS}
    for path in lib.grids():
        html = path.read_text(encoding="utf-8")
        new, n_e, n_c = apply_to(path.name, html)
        for grid, pattern, _, _ in EDITS:
            if grid in path.name:
                unused.discard((grid, pattern))
        if new != html:
            touched += 1
            total_e += n_e
            total_c += n_c
            print(f"  {path.name}: {n_e} edition(s) ciblee(s), {n_c} remplacement(s)")
            if not check:
                path.write_text(new, encoding="utf-8")
    if unused:
        raise SystemExit(f"ARRET — {len(unused)} edition(s) sans grille cible : {unused}")
    verb = "seraient appliques" if check else "appliques"
    print(f"\n{total_e + total_c} remplacement(s) {verb} sur {touched} grille(s) "
          f"({total_e} cibles, {total_c} mecaniques)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
