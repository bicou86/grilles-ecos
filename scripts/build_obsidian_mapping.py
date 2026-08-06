# Construit docs/obsidian-mapping.yaml : chaque grille → page Obsidian + libellé.
# Encode la curation médicale validée (pilote 2026-07-23 + généralisation).
import json, re, unicodedata

SCRATCH = str(__import__("pathlib").Path(__file__).resolve().parent.parent / "docs" / "obsidian-data")
REPO = "/Users/damienfulliquet/Developer/GitHub/grilles-ecos"
cat = json.load(open(f"{SCRATCH}/catalog2.json"))
pages_meta = {p["name"]: p for p in json.load(open(f"{SCRATCH}/pages.json"))}

SSP = lambda n: f"SSP ECOS/SSP — {n}.md"
SK = lambda n: f"Skills ECOS/Skills — {n}.md"

def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", " ", s).strip()

# ---- mapping par motif (corpus amboss/german/rescos/usmle/triage) ----
M = {}
def add(page, *motifs):
    for m in motifs: M[norm(m)] = page

add(SSP("Douleur Abdominale"), "Douleurs abdominales", "Douleur abdominale",
    "Douleur Abdominale Feminine", "Douleur Abdominale Masculine")
add(SSP("Pyrosis (RGO)"), "Brûlures d'estomac")
add(SSP("Dysphagie"), "Dysphagie")
add(SSP("Céphalée"), "Céphalée", "Céphalées")
add(SSP("Douleur Thoracique"), "Douleur thoracique", "Douleur Thoracique")
add(SSP("Fatigue"), "Fatigue")
add(SSP("Hématurie"), "Hématurie")
add(SSP("Mal de Gorge (Angine)"), "Mal de gorge")
add(SSP("Nausées, Vomissements & Hématémèse"), "Nausées", "Nausées et Vomissements")
add(SSP("Toux Chronique"), "Toux chronique", "Toux", "Toux persistante", "Toux Chronique",
    "Symptômes Respiratoires")
add(SSP("Fièvre du Nourrisson"), "Toux et fièvre", "Fièvre nourrisson", "Fièvre enfant",
    "Convulsions enfant")
add(SSP("Troubles du Sommeil"), "Troubles du sommeil", "Problèmes de sommeil")
add(SSP("Vertiges"), "Vertiges")
add(SSP("Acouphènes"), "Acouphènes")
add(SSP("Constipation"), "Constipation")
add(SSP("Diarrhée"), "Diarrhée", "Diarrhées", "Diarrhée nourrisson", "Vomissements et diarrhée",
    "Diarrhées et constipation", "Troubles du transit")
add(SSP("Douleur au Poignet"), "Douleur au poignet", "Douleur au Poignet")
add(SSP("Dyspnée"), "Dyspnée")
add(SSP("Dysurie"), "Dysurie", "Fièvre pendant la grossesse")
add(SSP("Énurésie Nocturne"), "Enurésie", "Énurésie nocturne")
add(SSP("Éruption Cutanée"), "Eruption cutanée", "Changements cutanés", "Erythème")
add(SSP("Lombalgies"), "Lombalgie", "Douleur lombaire", "Douleur dorsale", "Douleurs dorsales",
    "Douleurs dorsales et raideur", "Lombalgie chez un patient âgé")
add(SSP("Malaise & Perte de Connaissance Brève"), "Malaise", "Perte de connaissance", "Epilepsie")
add(SSP("Ménopause"), "Ménopause", "Bouffées de chaleur")
add(SSP("Syndrome Métabolique"), "Obésité", "Prise de poids")
add(SSP("Palpitations"), "Palpitations", "Tachycardie", "Bradycardie")
add(SSP("Pollakiurie"), "Pollakiurie")
add(SSP("Saignement Vaginal Anormal"), "Saignement vaginal", "Saignements vaginaux",
    "Règles irrégulières")
add(SSP("Tremblement"), "Tremblement")
add(SSP("Adénopathie"), "Adénopathie sus-claviculaire")
add(SSP("Amaurose & Baisse d'Acuité Visuelle"), "Amaurose", "Perte de vision", "Perte de Vision")
add(SSP("Dépression"), "Dépression")
add(SSP("Diplopie"), "Diplopie")
add(SSP("Douleur au Mollet & TVP"), "Douleur au mollet", "Douleur mollet",
    "Douleur du membre inférieur")
add(SSP("Douleurs Articulaires"), "Douleurs articulaires", "Douleurs Articulaires",
    "Douleur au coude", "Douleur au talon", "Douleur talon")
add(SSP("Aménorrhée"), "Aménorrhée")
add(SSP("Dyspareunie"), "Dyspareunie")
add(SSP("Dysphonie"), "Dysphonie")
add(SSP("Fièvre"), "Fièvre", "Fièvre chez l'enfant", "Coup de Chaleur")
add(SSP("Fièvre au Retour de Voyage"), "Voyage au Brésil", "Voyage à Madagascar")
add(SSP("Ictère"), "Ictère")
add(SSP("Ictère Néonatal"), "Ictère néonatal")
add(SSP("Incontinence Urinaire"), "Incontinence")
add(SSP("Perte d'Audition"), "Perte auditive")
add(SSP("Perte de Poids Involontaire"), "Perte de poids et Fatigue")
add(SSP("Saignements & Ecchymoses"), "Fatigue et Ecchymoses")
add(SSP("Rectorragies & Hémorragie Digestive Basse"), "Selles noires", "Sang dans les selles")
add(SSP("Troubles de la Mémoire & Démences"), "Troubles de mémoire", "Troubles mémoire",
    "Troubles de Mémoire")
add(SSP("Capacité de Discernement & Éthique"), "Évaluation après chute", "Agression sexuelle")
add(SSP("AVP (Accident de la Voie Publique)"), "AVP")
add(SSP("Dépendance & Addictions (Alcool, Tabac, Drogues)"), "Abus d'alcool")
add(SSP("Prévention Pédiatrique (consultations & dépistages systématiques)"), "Allaitement")
add(SSP("Trouble Anxieux"), "Anxiété", "Crise de panique")
add(SSP("Chute & Évaluation Gériatrique"), "Chute")
add(SSP("Troubles du Développement & Croissance"), "Difficultés scolaires")
add(SSP("Douleur de Genou"), "Douleur au genou", "Douleur genou", "Douleur Antérieure du Genou")
add(SSP("Douleur d'Épaule"), "Douleur à l'épaule", "Douleur épaule")
add(SSP("Entorse de Cheville"), "Douleur à la cheville")
add(SSP("Otalgie"), "Douleur à l'oreille", "Otorrhée")
add(SSP("Douleur de Hanche"), "Douleur à la hanche")
add(SK("Entretien Motivationnel"), "EM Tabac", "EM Vaccinations")
add(SSP("Ballonnement (Météorisme)"), "Gonflement abdominal")
add(SSP("Syndrome Néphrotique"), "Gonflement du visage")
add(SSP("HTA (Suivi & Crise Hypertensive)"), "Hypertension", "Suivi hypertension")
add(SSP("Enfant Irritable & Pleurs Excessifs"), "Pleurs inconsolables")
add(SSP("Troubles de la Croissance (Retard - Grande taille)"), "Retard de croissance")
add(SSP("Dysfonction Érectile"), "Troubles de l'érection")
add(SSP("Neuropathie Périphérique"), "Troubles sensoriels aux pieds",
    "Diminution de sensation dans les extrémités")
add(SSP("Œil Rouge"), "Yeux rouges", "Douleur oculaire", "Œil Rouge")
add(SK("Annonce Mauvaise Nouvelle (SPIKES)"), "BBN")
add(SSP("Boiterie de l'Enfant"), "Boiterie pédiatrique")
add(SSP("Colique Néphrétique"), "Douleur au flanc", "Douleur au flanc et troubles mictionnels")
add(SSP("Claudication Intermittente & AOMI"), "Douleur aux jambes")
add(SSP("Douleur - Masse Pelvienne"), "Douleur pelviennes", "Douleurs pelviennes")
add(SSP("Œdème Scrotal"), "Masse Testiculaire")
add(SSP("Diabète (Suivi & Complications)"), "Diabète pédiatrique", "Suivi diabète")
add(SSP("Cervicalgies"), "Douleurs cervicales")
add(SSP("Visite médicale d'Embauche - Médecine du travail"), "Examen médical pré-embauche")
add(SSP("Troubles Psychotiques & Schizophrénie"), "Hallucinations visuelles")
add(SSP("Détresse Respiratoire (Adulte-Enfant non-néonatal)"), "Respiration bruyante enfant")
add(SSP("Grossesse  - Surveillance & Complications"), "Test de grossesse positif")
add(SSP("Leucorrhées"), "Lésion génitale")
add(SSP("Hémoptysie"), "Hémoptysie")
add(SSP("Syncope"), "Syncope")
add(SSP("Capacité de Discernement & Éthique"), "Fatigue et violence domestique")

# ---- mapping/override par fichier (préfixe) — casecos + cas particuliers ----
F = {
    # overrides corpus plats
    "AMBOSS-15_": None,  # pédiatrique — page dédiée à créer
    "German-48_": SSP("Fièvre du Nourrisson"),
    "German-84_": SSP("Fièvre du Nourrisson"),
    "RESCOS-29_": SSP("Douleur au Mollet & TVP"),
    "RESCOS-30_": SSP("Neuropathie Périphérique"),
    "USMLE_Triage_33_": SSP("Troubles du Sommeil"),
    "USMLE_Triage_34_": SSP("Dépendance & Addictions (Alcool, Tabac, Drogues)"),
    "USMLE_Triage_35_": SSP("Pyrosis (RGO)"),
    "USMLE_Triage_36_": SSP("Douleur Abdominale"),
    "USMLE_Triage_37_": SSP("Chute & Évaluation Gériatrique"),
    "USMLE_Triage_38_": SSP("Grossesse  - Surveillance & Complications"),
    "USMLE_Triage_39_": SSP("Capacité de Discernement & Éthique"),
    "USMLE_Triage_40_": SSP("Intoxications Aiguës"),
    "German-62_": SSP("Masse Mammaire"),
    "USMLE_Triage_10_": SSP("Masse Mammaire"),
    # casecos
    "AMC-CasECOS Céphalées": SSP("Céphalée"),
    "AMC-CasECOS Gériatrie": SSP("Chute & Évaluation Gériatrique"),
    "AMC-Chir6-ARC1": SSP("Colique Néphrétique"),
    "ECOS Diag 1 - Dos douloureux": SSP("Lombalgies"),
    "ECOS Diag 3 - Dyspnée": SSP("Dyspnée"),
    "AMC-Chir1-ECG1": SSP("Urgences Abdominales Chirurgicales"),
    "AMC-Chir1-ECG2": SSP("Douleur de Hanche"),
    "AMC-Chir1-MedLeg": SSP("Capacité de Discernement & Éthique"),
    "AMC-Chir2-ARC1": SSP("Douleur Abdominale"),
    "AMC-Chir2-ECG1": SSP("Douleur Abdominale"),
    "AMC-Chir2-ECG2": SSP("Douleur Abdominale"),
    "AMC-Chir2-ECG3": SSP("Nausées, Vomissements & Hématémèse"),
    "AMC-Chir2-ECG4": SSP("Urgences Abdominales Chirurgicales"),
    "AMC-Chir2-ECG5": SSP("Ascite & Cirrhose"),
    "AMC-Chir2-Vignette1": SSP("Hernie Inguinale"),
    "AMC-Chir2-Vignette2": SSP("Douleur Abdominale"),
    "AMC-Chir2-Vignette3": SSP("Urgences Abdominales Chirurgicales"),
    "AMC-Chir2-Vignette4": SSP("Syndrome Métabolique"),
    "AMC-Chir2-Vignette5": SSP("Diabète (Suivi & Complications)"),
    "AMC-Chir3-ARC1": SSP("Douleur de Hanche"),
    "AMC-Chir3-ECG1": SSP("Polytraumatisme"),
    "AMC-Chir3-ECG2": SSP("Douleur de Genou"),
    "AMC-Chir3-ECG3": SSP("Douleurs Articulaires"),
    "AMC-Chir3-ECG4": SSP("Lombalgies"),
    "AMC-Chir3-ECG5": SSP("Diabète (Suivi & Complications)"),
    "AMC-Chir3-ECG6": SSP("Douleur au Poignet"),
    "AMC-Chir3-ECG7": SSP("Douleurs Articulaires"),
    "AMC-Chir3-Vignette1": SSP("Douleur de Hanche"),
    "AMC-Chir3-Vignette2": SSP("Douleur de Genou"),
    "AMC-Chir3-Vignette3": SSP("Entorse de Cheville"),
    "AMC-Chir3-Vignette4": SSP("Douleur au Poignet"),
    "AMC-Chir4-ARC1": SSP("Dyspnée"),
    "AMC-Chir4-ECG1": SSP("Claudication Intermittente & AOMI"),
    "AMC-Chir4-ECG2": SSP("Claudication Intermittente & AOMI"),
    "AMC-Chir4-ECG3": SSP("Urgences Abdominales Chirurgicales"),
    "AMC-Chir4-ECG4": SSP("Douleur Thoracique"),
    "AMC-Chir4-ECG5": SSP("Douleur Thoracique"),
    "AMC-Chir4-ECG6": SSP("Dyspnée"),
    "AMC-Chir4-Vignette1": SSP("Douleur au Mollet & TVP"),
    "AMC-Chir4-Vignette2": SSP("Parésie - AVC"),
    "AMC-Chir5-ECG1": SSP("Adénopathie"),
    "AMC-Chir5-ECG2": SSP("Douleur Thoracique"),
    "AMC-Chir5-ECG3": SSP("Troubles Thyroïdiens"),
    "AMC-Chir5-ECG4": SSP("Polytraumatisme"),
    "AMC-Chir5-ECG5": SSP("HTA (Suivi & Crise Hypertensive)"),
    "AMC-Chir5-Vignette1": SSP("Toux Chronique"),
    "AMC-Chir5-Vignette2": SSP("Troubles Thyroïdiens"),
    "AMC-Chir6-ECG1": SSP("Urgences Urologiques"),
    "AMC-Chir6-ECG2": SSP("SD Counselling Dépistages (cancer, CV, IST)"),
    "AMC-Chir6-ECG3": SSP("Incontinence Urinaire"),
    "AMC-Chir6-Vignette1": SSP("Hématurie"),
    "AMC-Chir6-Vignette2": SSP("Œdème Scrotal"),
    "AMC-Chir6-Vignette3": SSP("Troubles Mictionnels & HBP"),
    "AMC-ECOS1-S1": SSP("TCA (Troubles du Comportement Alimentaire)"),
    "AMC-ECOS1-S10": SSP("Douleur Thoracique"),
    "AMC-ECOS1-S2": SSP("Rectorragies & Hémorragie Digestive Basse"),
    "AMC-ECOS1-S3": SSP("Vertiges"),
    "AMC-ECOS1-S4": SSP("Fièvre du Nourrisson"),
    "AMC-ECOS1-S5": SSP("Céphalée"),
    "AMC-ECOS1-S6": SSP("Urgences Abdominales Chirurgicales"),
    "AMC-ECOS1-S7": SSP("HTA Gravidique - Pré-éclampsie"),
    "AMC-ECOS1-S8": SSP("Céphalée"),
    "AMC-ECOS1-S9": SSP("Lombalgies"),
    "AMC-ECOSDiag1": SSP("Lombalgies"),
    "AMC-ECOSDiag2": SSP("Urgences Abdominales Chirurgicales"),
    "AMC-ECOSDiag3": SSP("Dyspnée"),
    "AMC-EthiqueLegale-V1": SSP("Capacité de Discernement & Éthique"),
    "AMC-EthiqueLegale-V2": SSP("Capacité de Discernement & Éthique"),
    "AMC-EthiqueLegale-V3": SSP("Dépendance & Addictions (Alcool, Tabac, Drogues)"),
    "AMC-EthiqueLegale-V4": SSP("Capacité de Discernement & Éthique"),
    "AMC-EthiqueLegale-V5": SSP("Urgences Psychiatriques (Agitation, PAFA)"),
    "AMC-GynObs-V1 ": SSP("SD Counselling Dépistages (cancer, CV, IST)"),
    "AMC-GynObs-V10": SSP("Douleur - Masse Pelvienne"),
    "AMC-GynObs-V11": SSP("Contraception & Conseil"),
    "AMC-GynObs-V12": SSP("Diabète Gestationnel"),
    "AMC-GynObs-V2": SSP("Douleur - Masse Pelvienne"),
    "AMC-GynObs-V3": SSP("Masse Mammaire"),
    "AMC-GynObs-V4": SSP("Saignement Vaginal Anormal"),
    "AMC-GynObs-V5": SSP("HTA Gravidique - Pré-éclampsie"),
    "AMC-GynObs-V6": SSP("Grossesse  - Surveillance & Complications"),
    "AMC-GynObs-V7": SSP("Grossesse  - Surveillance & Complications"),
    "AMC-GynObs-V8": SSP("Grossesse  - Surveillance & Complications"),
    "AMC-GynObs-V9": SSP("Aménorrhée"),
    "AMC-MCPR-ARC1 ": SSP("Dépendance & Addictions (Alcool, Tabac, Drogues)"),
    "AMC-MCPR-ARC10": SSP("Mal de Gorge (Angine)"),
    "AMC-MCPR-ARC12": SSP("SD Counselling Dépistages (cancer, CV, IST)"),
    "AMC-MCPR-ARC13": SSP("Lombalgies"),
    "AMC-MCPR-ARC14": SSP("Contraception & Conseil"),
    "AMC-MCPR-ARC15": SSP("Entorse de Cheville"),
    "AMC-MCPR-ARC16": SSP("Diarrhée"),
    "AMC-MCPR-ARC17": SSP("Diabète (Suivi & Complications)"),
    "AMC-MCPR-ARC18": SSP("Dyspnée"),
    "AMC-MCPR-ARC19": SSP("Ronflement - SAOS"),
    "AMC-MCPR-ARC2 ": SSP("Douleur de Genou"),
    "AMC-MCPR-ARC20": SSP("Perte d'Appétit - Anorexie (Adulte & âgé)"),
    "AMC-MCPR-ARC21": None,  # évaluation préopératoire — page manquante
    "AMC-MCPR-ARC22": SSP("Fièvre au Retour de Voyage"),
    "AMC-MCPR-ARC23": SSP("Dyspnée"),
    "AMC-MCPR-ARC3 ": SSP("SD Counselling Dépistages (cancer, CV, IST)"),
    "AMC-MCPR-ARC4 ": SSP("Pyrosis (RGO)"),
    "AMC-MCPR-ARC5 ": SSP("Vertiges"),
    "AMC-MCPR-ARC6 ": SSP("Douleur Thoracique"),
    "AMC-MCPR-ARC7 ": SSP("Dysurie"),
    "AMC-MCPR-ARC8 ": SSP("SD Counselling Dépistages (cancer, CV, IST)"),
    "AMC-MCPR-ARC9 ": SSP("Lombalgies"),
    "AMC-MedInterne Embolie": SSP("Dyspnée"),
    "AMC-MedInterne-P1 ": SSP("Syncope"),
    "AMC-MedInterne-P10": SSP("Douleur Thoracique"),
    "AMC-MedInterne-P11": SSP("Lombalgies"),
    "AMC-MedInterne-P12": SSP("Fièvre"),
    "AMC-MedInterne-P13": SSP("Céphalée"),
    "AMC-MedInterne-P14": SSP("Douleurs Articulaires"),
    "AMC-MedInterne-P15": SSP("Diarrhée"),
    "AMC-MedInterne-P2 ": SSP("Dyspnée"),
    "AMC-MedInterne-P3 ": SSP("Dyspnée"),
    "AMC-MedInterne-P4 ": SSP("Diabète (Suivi & Complications)"),
    "AMC-MedInterne-P5 ": SSP("Ictère"),
    "AMC-MedInterne-P6 ": SSP("Fatigue"),
    "AMC-MedInterne-P7 ": SSP("Pâleur & Anémie"),
    "AMC-MedInterne-P8 ": SSP("Fièvre"),
    "AMC-MedInterne-P9 ": SSP("Confusion - État Confusionnel Aigu"),
    "AMC-Neuro-P1 ": SSP("Amaurose & Baisse d'Acuité Visuelle"),
    "AMC-Neuro-P2 ": SSP("Trouble de la Marche"),
    "AMC-Neuro-P3 ": SSP("Neuropathie Périphérique"),
    "AMC-Neuro-P4 ": SSP("Fatigue"),
    "AMC-Neuro-P5 ": SSP("Malaise & Perte de Connaissance Brève"),
    "AMC-Neuro-P6 ": SSP("Tremblement"),
    "AMC-Neuro-P7 ": SSP("Céphalée"),
    "AMC-Neuro-R1 ": SSP("Céphalée"),
    "AMC-Neuro-R2 ": SSP("Parésie - AVC"),
    "AMC-ORL-P1 ": SSP("Otalgie"),
    "AMC-ORL-P2 ": SSP("Vertiges"),
    "AMC-ORL-P3 ": SSP("Céphalée"),
    "AMC-ORL-P4 ": SSP("Épistaxis"),
    "AMC-ORL-P5 ": SSP("Masses Cervicales"),
    "AMC-ORL-P6 ": SSP("Dysphonie"),
    "AMC-ORL-P7 ": SSP("Masses Cervicales"),
    "AMC-ORL-P8 ": SSP("Mal de Gorge (Angine)"),
    "AMC-ORL-P9 ": SSP("Perte d'Audition"),
    "AMC-Pharmaco-S1": SSP("Dyspnée"),
    "AMC-Pharmaco-S2": SSP("Dyspnée"),
    "AMC-Pharmaco-S3": SSP("Fibrillation Auriculaire"),
    "AMC-Pharmaco-S4": SSP("Diabète (Suivi & Complications)"),
    "AMC-Psy-P1 ": SSP("Troubles Psychotiques & Schizophrénie"),
    "AMC-Psy-P10": SSP("TCA (Troubles du Comportement Alimentaire)"),
    "AMC-Psy-P12": None,  # TDAH adulte — page manquante
    "AMC-Psy-P13": SSP("Dépression"),
    "AMC-Psy-P2 ": None,  # trouble paraphilique — page manquante
    "AMC-Psy-P3 ": SSP("Trouble Anxieux"),
    "AMC-Psy-P4 ": None,  # autisme adulte — page manquante
    "AMC-Psy-P5 ": SSP("Urgences Psychiatriques (Agitation, PAFA)"),
    "AMC-Psy-P6 ": SSP("Trouble Anxieux"),
    "AMC-Psy-P7 ": SSP("Trouble Anxieux"),
    "AMC-Psy-P9 ": SSP("Troubles du Sommeil"),
    "AMC-Psy-S1 ": SSP("Troubles de l'Humeur"),
    "AMC-Psy-S2 ": SSP("Troubles Psychotiques & Schizophrénie"),
    "AMC-Psy-S3 ": SSP("Urgences Psychiatriques (Agitation, PAFA)"),
    "AMC-Psy-S4 ": SSP("Troubles de la Mémoire & Démences"),
    "Anorexie boulimie": SSP("TCA (Troubles du Comportement Alimentaire)"),
    "Céphalées - Homme 30": SSP("Céphalée"),
    "Constat de chute": SSP("Chute & Évaluation Gériatrique"),
    "Convulsion fébrile": SSP("Fièvre du Nourrisson"),
    "Dyspnée multifactorielle": SSP("Dyspnée"),
    "Examen physique lombalgie": SSP("Lombalgies"),
    "Fracture vertébrale ostéoporotique": SSP("Lombalgies"),
    "HSA avec convulsion": SSP("Céphalée"),
    "HSA et refus de soins": SSP("Capacité de Discernement & Éthique"),
    "L'Abdomen Aigu": SSP("Urgences Abdominales Chirurgicales"),
    "ECOS Diag 2 - Abdomen Aigu": SSP("Urgences Abdominales Chirurgicales"),
    "La Dyspnée": SSP("Dyspnée"),
    "Le Laborantin": SSP("Lombalgies"),
    "Méléna sous anticoagulant": SSP("Rectorragies & Hémorragie Digestive Basse"),
    "Prééclampsie - Femme": SSP("HTA Gravidique - Pré-éclampsie"),
    "Péritonite par perforation": SSP("Urgences Abdominales Chirurgicales"),
    "STEMI - Femme": SSP("Douleur Thoracique"),
    "Spondylarthrite axiale": SSP("Lombalgies"),
    "Tendinite coiffe": SSP("Douleur d'Épaule"),
    "Trauma abdominal pénétrant": SSP("Urgences Abdominales Chirurgicales"),
    "UIDC-Caroline": SSP("Polydipsie & Polyurie"),
    "UIDC-Lea": SSP("Troubles de la Croissance (Retard - Grande taille)"),
    "UIDC-Linda": SSP("Fièvre du Nourrisson"),
    "UIDC-Madame Kopf": SSP("Céphalée"),
    "UIDC-Madame Ondine": SSP("Incontinence Urinaire"),
    "UIDC-Madame Siaulat": SSP("Confusion - État Confusionnel Aigu"),
    "UIDC-Mlle Olivia Veyre": SSP("Douleur Abdominale"),
    "UIDC-Mme A. Parino": SSP("Fièvre"),
    "UIDC-Mme Ona F.": SSP("Douleur de Hanche"),
    "UIDC-Mme Servier": SSP("Dépression"),
    "UIDC-Mme Victoria": SSP("Chute & Évaluation Gériatrique"),
    "UIDC-Monsieur Arden": SSP("Capacité de Discernement & Éthique"),
    "UIDC-Monsieur Dupont": SSP("Rectorragies & Hémorragie Digestive Basse"),
    "UIDC-Monsieur H. Toinnes - Anévrisme": SSP("Urgences Abdominales Chirurgicales"),
    "UIDC-Monsieur H. Toinnes - Douleur thoracique": SSP("Douleur Thoracique"),
    "UIDC-Monsieur H. Toinnes - Hypertension": SSP("HTA (Suivi & Crise Hypertensive)"),
    "UIDC-Monsieur Marcel T.": SSP("Toux Chronique"),
    "UIDC-Monsieur Paretic": SSP("Parésie - AVC"),
    "UIDC-Monsieur Zimmer": SSP("Douleur de Hanche"),
    "UIDC-Thomas": SSP("Fièvre du Nourrisson"),
    "UIDC-Vertiges": SSP("Vertiges"),
    "Vertiges aigus": SSP("Vertiges"),
    "USIT2": SSP("Syndromes Gériatriques (Fragilité + Glissement)"),
}

UNMAPPED_REASONS = {
    "AMBOSS-15_": "douleur abdominale pédiatrique — page pédiatrique à créer",
    "German-62_": "masse mammaire — pas de page « sein » dans le vault",
    "USMLE_Triage_10_": "masse mammaire — pas de page « sein » dans le vault",
    "AMC-GynObs-V3": "masse du sein — pas de page « sein » dans le vault",
    "AMC-MCPR-ARC21": "évaluation préopératoire — page manquante",
    "AMC-Psy-P12": "TDAH de l'adulte — page manquante",
    "AMC-Psy-P2 ": "trouble paraphilique — page manquante",
    "AMC-Psy-P4 ": "autisme de l'adulte — page manquante",
}

# ---- libellés ----
LIEU_MAP = [
    ("téléphon", "Cas téléphonique 📞"), ("urgence", "Urgences"), ("domicile", "Domicile"),
    ("premier recours", "Cabinet MG"), ("médecine générale", "Cabinet MG"),
    ("généraliste", "Cabinet MG"), ("médecine de famille", "Cabinet MG"),
    ("pédiatrie", "Pédiatrie"), ("gynécolog", "Gynécologie"), ("obstétrique", "Obstétrique"),
    ("neurochirurgie", "Neurochirurgie"), ("neurologie", "Neurologie"),
    ("gastro", "Gastro-entérologie"), ("clinique", "Clinique médicale"),
    ("cabinet", "Cabinet médical"),
]
def short_lieu(lieu):
    l = lieu.lower()
    for k, v in LIEU_MAP:
        if k in l: return v
    return lieu.strip() if 0 < len(lieu.strip()) <= 28 else ""

SEX = {"femme":"Femme","madame":"Femme","mme":"Femme","mlle":"Femme","jeune fille":"Femme",
       "fillette":"Fille","fille":"Fille","petite fille":"Fille",
       "homme":"Homme","monsieur":"Homme","m.":"Homme",
       "garçon":"Garçon","nourrisson":"Nourrisson","nouveau-né":"Nouveau-né","nouveau-née":"Nouveau-née"}
def parse_patient(p):
    m = re.search(r"(fils|fille(?:tte)?|garçon|bébé|nourrisson|enfant)[^,;.]{0,40}?,?\s*(?:âgée? de |de )?(\d+)\s*(ans|mois|jours|semaines)", p, re.I)
    if not m:
        m = re.search(r"(jeune fille|petite fille|femme|homme|monsieur|madame|mme|mlle|m\.|garçon|fillette|fille|nouveau-née?|nourrisson)[^,;.]{0,32}?(?:de |âgée? de |,\s*)?(\d+)\s*(ans|mois|jours|semaines)", p, re.I)
    if not m: return ""
    sex = SEX.get(m.group(1).lower(), m.group(1).capitalize())
    if sex == "Fils": sex = "Garçon"
    if sex == "Enfant" and "fille" in p.lower(): sex = "Fille"
    return f"{sex} {m.group(2)} {m.group(3)}"

def parse_complaint(p, fallback):
    m = re.search(r"(?:consultant pour|consulte(?: ce jour)?(?: à [^ ]+ cabinet)? pour|s(?:e|'est) présentée?[^.]{0,25}? (?:pour|avec)|en se plaignant (?:de|que)|avec des plaintes de|en raison d[e']|appelle pour|présentant|car (?:il|elle)?)\s*(.{4,90})", p, re.I)
    s = m.group(1).strip() if m else fallback
    s = re.sub(r"^avec\s+", "", s)
    s = re.split(r"\s+depuis\b|\s+évoluant\b|\s*\(|(?<=[a-zà-ü])\.\s|$", s)[0]
    s = re.sub(r"^(?:(?:son|sa|leur)\s+)?(?:fils|fille|enfant|bébé)\s+(?:continue de\s+|a\s+|présente\s+)?", "", s.strip())
    s = re.sub(r"^(?:plaintes? (?:de|concernant)\s+)", "", s)
    s = re.sub(r"^(des|de la|de l'|du|une|un|d')\s*", "", s.strip())
    s = s.rstrip(" .,;")
    return (s[:72].rsplit(" ", 1)[0] if len(s) > 72 else s) or fallback

# libellés du pilote — conservés à l'identique
OVR = {
"AMBOSS-1_": "AMBOSS-1 — Femme 47 ans, douleurs abdominales — Urgences",
"AMBOSS-2_": "AMBOSS-2 — Femme 23 ans, douleurs abdominales — Urgences",
"AMBOSS-3_": "AMBOSS-3 — Femme 34 ans, douleurs abdominales — Cabinet médical",
"German-15_": "German-15 — Femme 73 ans, douleurs abdominales — Cabinet MG",
"German-16_": "German-16 — Jeune fille 16 ans, douleurs abdominales — Cabinet MG",
"German-17_": "German-17 — Femme 27 ans, douleurs abdominales — Cabinet de gynécologie",
"German-18_": "German-18 — Femme 28 ans, douleurs abdominales aiguës — Urgences",
"German-19_": "German-19 — Homme 21 ans, douleurs abdominales + diarrhée — Service médical",
"German-20_": "German-20 — Homme 72 ans, se tord de douleur — Urgences",
"German-21_": "German-21 — Femme 57 ans, douleurs épigastriques — Urgences",
"RESCOS-17_": "RESCOS-17 — Homme 39 ans, douleurs abdominales — Urgences",
"RESCOS-18_": "RESCOS-18 — Femme 39 ans, douleurs abdominales, surpoids — Cabinet MG",
"RESCOS-19_": "RESCOS-19 — Homme 64 ans, urines foncées — Cabinet MG",
"RESCOS-20_": "RESCOS-20 — Femme 30 ans, douleur abdominale, obésité — Urgences",
"RESCOS-21_": "RESCOS-21 — Homme 35 ans, douleur épigastrique en coup de poignard — Urgences",
"RESCOS-22_": "RESCOS-22 — 24 ans, douleurs abdominales, retour du Sénégal — Urgences · ECC Digestion",
"RESCOS-23_": "RESCOS-23 — Femme 45 ans, douleur biliaire — Gastro-entérologie · ECC Digestion",
"USMLE-13_": "USMLE-13 — Femme 48 ans, douleurs abdominales — Clinique médicale",
"USMLE-31_": "USMLE-31 — Femme 21 ans, douleurs abdominales — Urgences",
"USMLE_Triage_16_": "Triage 16 — Homme 47 ans, nausées et vomissements — Clinique médicale",
"USMLE_Triage_19_": "Triage 19 — Femme 36 ans, douleurs abdominales depuis 3 jours — Urgences",
"USMLE_Triage_36_": "Triage 36 — Homme 22 ans, douleurs abdominales sévères — Cas téléphonique 📞",
"AMC-Chir2-ECG1": "AMC-Chir2-ECG1 — Fièvre + douleurs abdominales — Maladie de Crohn",
"AMC-Chir2-ECG2 ": "AMC-Chir2-ECG2 — Douleurs épigastriques tenaces — Cancer gastrique",
"UIDC-Mlle Olivia Veyre": "UIDC — Olivia Veyre, douleurs abdominales aiguës FID — Appendicite",
}

def make_label(c):
    for pref, lab in OVR.items():
        if c["file"].startswith(pref): return lab
    t = re.sub(r"\s*-\s*Grille ECOS$", "", c["title"]).strip()
    if c["corpus"] == "casecos":
        lab = re.sub(r"\s+-\s+", " — ", t)
        return lab[:110].rstrip(" —")
    parts = re.split(r"\s+-\s+", t)
    cid = parts[0].replace("USMLE Triage", "Triage")
    motif = parts[1] if len(parts) > 1 else ""
    motif_fb = motif if (motif.isupper() or len(motif) <= 4) else motif.lower()
    pat = parse_patient(c["patient"])
    comp = parse_complaint(c["patient"], motif_fb)
    lieu = short_lieu(c["lieu"])
    core = f"{pat}, {comp}" if pat else (comp or motif)
    lab = f"{cid} — {core}"
    if lieu: lab += f" — {lieu}"
    return lab

# ---- grilles locales (_bibliotheque/rescos-grilles-locales) : cible + libellé manuels ----
LOCAL_DIR = "_bibliotheque/ECOS/rescos-grilles-locales"
LOCAL = {
 "RESCOS-41 - Dysurie - Grille ECOS.html":
    (SSP("Dysurie"), "RESCOS-41 — Femme 19 ans, douleurs en urinant — Gynécologie 📁"),
 "RESCOS-42 - Dysurie - Grille ECOS.html":
    (SSP("Dysurie"), "RESCOS-42 — Femme 29 ans, brûlures mictionnelles — Cabinet MG 📁"),
 "RESCOS-43 - EM tabac - Grille ECOS.html":
    (SK("Entretien Motivationnel"), "RESCOS-43 — EM tabac : fumeur 30 ans, demande de dépistage — Cabinet MG 📁"),
 "RESCOS-44 - Fatigue - Grille ECOS.html":
    (SSP("Fatigue"), "RESCOS-44 — 42 ans, fatigue persistante, obésité — Policlinique 📁"),
 "RESCOS-45 - Fatigue - Grille ECOS.html":
    (SSP("Fatigue"), "RESCOS-45 — Femme 87 ans, fatigue — Cabinet MG 📁"),
 "RESCOS-46 - Fièvre - Grille ECOS.html":
    (SSP("Fièvre"), "RESCOS-46 — Homme 26 ans, fièvre élevée depuis 5 jours — Urgences 📁"),
 "RESCOS-47 - Ictère - Grille ECOS.html":
    (SSP("Ictère"), "RESCOS-47 — Femme 58 ans, jaunisse depuis une semaine — Cabinet MG 📁"),
 "RESCOS-48 - Lombalgie - Grille ECOS.html":
    (SSP("Lombalgies"), "RESCOS-48 — Homme 75 ans, douleurs dorsales — Cabinet MG 📁"),
 "RESCOS-49 - Malaise - Grille ECOS.html":
    (SSP("Malaise & Perte de Connaissance Brève"), "RESCOS-49 — Homme 62 ans, troubles de conscience sur hypoglycémie — Urgences 📁"),
 "RESCOS-50 - Malaise - Grille ECOS.html":
    (SSP("Malaise & Perte de Connaissance Brève"), "RESCOS-50 — Homme 30 ans, perte de connaissance, anémie ferriprive — Urgences 📁"),
 "RESCOS-51 - Oedèmes des MI - Grille ECOS.html":
    (SSP("Œdèmes des Membres Inférieurs"), "RESCOS-51 — Femme 30 ans, œdèmes des membres inférieurs — Cabinet MG 📁"),
 "RESCOS-52 - Paralysie - Grille ECOS.html":
    (SSP("Parésie - AVC"), "RESCOS-52 — 52 ans, paralysie brutale transitoire (30 min) — Urgences 📁"),
 "RESCOS-53 - Parésie facio-brachiale - ECC Neurologie - Grille ECOS.html":
    (SSP("Parésie - AVC"), "RESCOS-53 — Homme 79 ans, parésie facio-brachiale brutale + dysarthrie — Neurologie 📁"),
 "RESCOS-54 - Présentation au CDC - Grille ECOS.html":
    (SK("Présentation de Cas"), "RESCOS-54 — Présentation au CDC : femme 92 ans, œdèmes MI + plaie — Médecine interne 📁"),
 "RESCOS-55 - Présentation au Colloque social - Grille ECOS.html":
    (SK("Présentation de Cas"), "RESCOS-55 — Colloque social : femme 89 ans, retour à domicile — Médecine interne 📁"),
 "RESCOS-56 - Prurit - Grille ECOS.html":
    (SSP("Prurit"), "RESCOS-56 — Homme 61 ans, prurit généralisé + ictère — Cabinet MG 📁"),
 "RESCOS-57 - Ralentissement - Consultation téléphonique EMS - Grille ECOS.html":
    (SSP("Confusion - État Confusionnel Aigu"), "RESCOS-57 — Homme 88 ans (EMS), ralentissement + déshydratation — Cas téléphonique 📞 📁"),
 "RESCOS-57b - Ralentissement - Consultation téléphonique - Grille ECOS.html":
    (SSP("Confusion - État Confusionnel Aigu"), "RESCOS-57b — Homme 88 ans (EMS), ralentissement + diarrhées — Cas téléphonique 📞 📁"),
 "RESCOS-58 - Rectorragies - Grille ECOS.html":
    (SSP("Rectorragies & Hémorragie Digestive Basse"), "RESCOS-58 — 52 ans, sang dans les selles depuis 3 jours — Urgences 📁"),
 "RESCOS-58b - Rectorragies - Grille ECOS.html":
    (SSP("Rectorragies & Hémorragie Digestive Basse"), "RESCOS-58b — 52 ans, sang dans les selles (variante) — Urgences 📁"),
 "RESCOS-59 - SD - Cholestérol - Grille ECOS.html":
    (SSP("SD Counselling Dépistages (cancer, CV, IST)"), "RESCOS-59 — Décision partagée : cholestérol élevé — Cabinet MG 📁"),
 "RESCOS-60 - SD - Iléus palliatif - Grille ECOS.html":
    (SK("Décision Partagée"), "RESCOS-60 — Décision partagée : iléus palliatif, cancer ovarien — Médecine interne 📁"),
 "RESCOS-61 - Suivi de grossesse - ECC Obstétrique - Grille ECOS.html":
    (SSP("Grossesse  - Surveillance & Complications"), "RESCOS-61 — Suivi de grossesse — Obstétrique · ECC 📁"),
 "RESCOS-62 - Toux - ECC Poumon - Grille ECOS.html":
    (SSP("Toux Chronique"), "RESCOS-62 — Homme 65 ans, toux fébrile + dyspnée — Cabinet MG · ECC Poumon 📁"),
 "RESCOS-63 - Toux - Pédiatrie - Grille ECOS.html":
    (SSP("Toux Chronique"), "RESCOS-63 — Bébé 5 mois, toux — Urgences · Pédiatrie 📁"),
 "RESCOS-64 - Toux - Station double 1 - Grille ECOS.html":
    (SSP("Hémoptysie"), "RESCOS-64 — Femme 61 ans, toux chronique + crachats sanglants — Station double 1/2 📁"),
 "RESCOS-64 - Toux - Station double 2 - Grille ECOS.html":
    (SK("Présentation de Cas"), "RESCOS-64 — Présentation de la patiente au pneumologue — Station double 2/2 📁"),
 "RESCOS-65 - Tremblements - ECC Neurologie - Grille ECOS.html":
    (SSP("Tremblement"), "RESCOS-65 — Homme 64 ans, tremblement de repos unilatéral — Neurologie 📁"),
 "RESCOS-66 - Troubles de l'équilibre - ECC Neurologie - Grille ECOS.html":
    (SSP("Trouble de la Marche"), "RESCOS-66 — Femme 74 ans, troubles de l'équilibre + amaigrissement — Neurologie 📁"),
 "RESCOS-67 - Fatigue - Grille ECOS.html":
    (SSP("Fatigue"), "RESCOS-67 — Femme 38 ans, baisse d'énergie — Cabinet MG 📁"),
 "RESCOS-68 - Eruption cutanée - Grille ECOS.html":
    (SSP("Éruption Cutanée"), "RESCOS-68 — 31 ans, éruption cutanée — Cabinet MG 📁"),
 "RESCOS-69 - Traumatisme MS - Basketteur 25 ans - Grille ECOS.html":
    (SSP("Douleur d'Épaule"), "RESCOS-69 — 25 ans, douleur du bras droit post-basketball — Urgences 📁"),
 "RESCOS-69 - Traumatisme MS - Grille ECOS.html":
    (SSP("Douleur d'Épaule"), "RESCOS-69 — 25 ans, douleur du bras droit post-basketball (annexes Rx) — Urgences 📁"),
}

# ---- résolution ----
def motif_of(c):
    t = re.sub(r"\s*-\s*Grille ECOS$", "", c["title"])
    parts = re.split(r"\s+-\s+", t)
    return parts[1] if len(parts) > 1 else t

F = {unicodedata.normalize("NFD", k): v for k, v in F.items()}
UNMAPPED_REASONS = {unicodedata.normalize("NFD", k): v for k, v in UNMAPPED_REASONS.items()}
mapping, unmapped = {}, []
for c in cat:
    page, why = None, None
    hit = [p for p in F if unicodedata.normalize("NFD", c["file"]).startswith(p)]
    if hit:
        page = F[max(hit, key=len)]
        if page is None:
            why = next((r for k, r in UNMAPPED_REASONS.items() if c["file"].startswith(k)),
                       "curation : cible incertaine")
    elif c["corpus"] != "casecos":
        page = M.get(norm(motif_of(c)))
        if page is None: why = f"motif non mappé : {motif_of(c)}"
    else:
        why = "casecos sans règle"
    if page:
        mapping.setdefault(page, []).append(c)
    else:
        unmapped.append((c, why))


# ---- nouvelles grilles locales (lot 2026-07-29) : cible explicite, libellé auto ----
LOCAL2 = {
 "AMC Urgences 1 - Polytraumatisé - Grille ECOS.html": SSP("Polytraumatisme"),
 "AMC Urgences 2A - Embolie pulmonaire massive - Grille ECOS.html": SSP("États de Choc"),
 "AMC Urgences 2B - Choc septique sur péritonite - Grille ECOS.html": SSP("États de Choc"),
 "AMC Urgences 3A - Douleur thoracique aiguë - STEMI - Grille ECOS.html": SSP("Douleur Thoracique"),
 "AMC Urgences 3B - Douleur thoracique aiguë - NSTEMI - Grille ECOS.html": SSP("Douleur Thoracique"),
 "AMC Urgences 3C - Douleur thoracique aiguë - Dissection aortique - Grille ECOS.html": SSP("Douleur Thoracique"),
 "AMC Urgences 4 - Insuffisance respiratoire aiguë sur BPCO - Grille ECOS.html": SSP("Détresse Respiratoire (Adulte-Enfant non-néonatal)"),
 "AMC Urgences 5A - Hémorragie sous-arachnoïdienne - Grille ECOS.html": SSP("Céphalée"),
 "AMC Urgences 5B - AVC ischémique avec transformation maligne - Grille ECOS.html": SSP("Parésie - AVC"),
 "AMC Urgences 5C - Méningite bactérienne avec sepsis - Grille ECOS.html": SSP("Céphalée"),
 "Acné vulgaire - Adolescente de 16 ans - Grille ECOS.html": SSP("Éruption Cutanée"),
 "BBN - Cancer du sein - Grille ECOS.html": SK("Annonce Mauvaise Nouvelle (SPIKES)"),
 "BBN - Limitation thérapeutique cancer - Grille ECOS.html": SK("Annonce Mauvaise Nouvelle (SPIKES)"),
 "BBN - Sclérose en plaques - Grille ECOS.html": SK("Annonce Mauvaise Nouvelle (SPIKES)"),
 "BPCO exacerbation - Femme de 65 ans - Feuille porte.html": SSP("Dyspnée"),
 "BPCO exacerbation - Femme de 65 ans - Grille ECOS.html": SSP("Dyspnée"),
 "Baisse de l'état général et mal au dos - Syndrome de Guillain-Barré - Grille ECOS.html": SSP("Lombalgies"),
 "Choc anaphylactique - Femme de 28 ans - Grille ECOS.html": SSP("Détresse Respiratoire & Anaphylaxie"),
 "Choc septique pulmonaire - Homme de 46 ans - Grille ECOS.html": SSP("États de Choc"),
 "Claudication intermittente - Homme de 64 ans - Grille ECOS.html": SSP("Claudication Intermittente & AOMI"),
 "Contraception - Femme de 28 ans - Grille ECOS.html": SSP("Contraception & Conseil"),
 "Contraception adolescente - Fille de 16 ans - Grille ECOS.html": SSP("Contraception & Conseil"),
 "Crise convulsive - Homme de 77 ans - Grille ECOS.html": SSP("Malaise & Perte de Connaissance Brève"),
 "Céphalées - Exemple station ECOS B3 - Grille ECOS.html": SSP("Céphalée"),
 "Céphalées - Vignette clinique - Grille ECOS.html": SSP("Céphalée"),
 "Diabète - Patient avec hyperglycémie nouvelle - Grille ECOS.html": SSP("Diabète (Suivi & Complications)"),
 "Diabète pédiatrique - Garçon de 9 ans - Feuille porte.html": SSP("Diabète (Suivi & Complications)"),
 "Diabète pédiatrique - Garçon de 9 ans - Grille ECOS.html": SSP("Diabète (Suivi & Complications)"),
 "Diarrhées - Vignettes cliniques - Grille ECOS.html": SSP("Diarrhée"),
 "Diverticulite sigmoidienne - Homme de 58 ans - Grille ECOS.html": SSP("Douleur Abdominale"),
 "Douleur abdominale - Vignette clinique - Grille ECOS.html": SSP("Douleur Abdominale"),
 "Douleur abdominale - Vignettes cliniques - Grille ECOS.html": SSP("Douleur Abdominale"),
 "Douleur abdominale et diarrhée fébrile - Grille ECOS.html": SSP("Douleur Abdominale"),
 "Douleur non traumatique du membre inférieur - Grille ECOS.html": SSP("Douleur au Mollet & TVP"),
 "Douleur thoracique - Vignette clinique - Grille ECOS.html": SSP("Douleur Thoracique"),
 "Douleurs thoraciques - DRS - Grille ECOS.html": SSP("Douleur Thoracique"),
 "Dyspnée aigue - Grille ECOS.html": SSP("Dyspnée"),
 "Dyspnée dans un contexte de polymorbidité - Grille ECOS.html": SSP("Dyspnée"),
 "Dyspnée dans un contexte infectieux - Grille ECOS.html": SSP("Dyspnée"),
 "Dyspnée et insuffisance cardiaque - Grille ECOS.html": SSP("Dyspnée"),
 "Dyspnée et mal au cou - Grille ECOS.html": SSP("Dyspnée"),
 "Dyspnée post-COVID - Grille ECOS.html": SSP("Dyspnée"),
 "Dépression majeure - Homme de 36 ans - Feuille porte.html": SSP("Dépression"),
 "Dépression majeure - Homme de 36 ans - Grille ECOS.html": SSP("Dépression"),
 "Dépression post-partum - Femme de 29 ans - Feuille porte.html": SSP("Dépression"),
 "Dépression post-partum - Femme de 29 ans - Grille ECOS.html": SSP("Dépression"),
 "Enfant qui boîte - Synovite aiguë transitoire de la hanche - Grille ECOS.html": SSP("Boiterie de l'Enfant"),
 "Entretien motivationnel - Activité physique - Grille ECOS.html": SK("Entretien Motivationnel"),
 "Entretien motivationnel - Compliance thérapeutique - Grille ECOS.html": SK("Entretien Motivationnel"),
 "Entretien motivationnel - Consommation d'alcool - Grille ECOS.html": SK("Entretien Motivationnel"),
 "Entretien motivationnel - Sevrage tabagique - Grille ECOS.html": SK("Entretien Motivationnel"),
 "Entretien motivationnel - Tabac - Grille ECOS.html": SK("Entretien Motivationnel"),
 "Fatigue - Vignettes cliniques - Grille ECOS.html": SSP("Fatigue"),
 "Fatigue TBL - Grille ECOS.html": SSP("Fatigue"),
 "Fatigue et maladies chroniques - Grille ECOS.html": SSP("Fatigue"),
 "Fièvre et douleurs articulaires - Infection gonococcique disséminée - Grille ECOS.html": SSP("Douleurs Articulaires"),
 "Goutte - Accès aigu - Grille ECOS.html": SSP("Douleurs Articulaires"),
 "Grille ECOS USIT2 - Diarrhée Hématochézie - Grille ECOS.html": SSP("Rectorragies & Hémorragie Digestive Basse"),
 "Grille ECOS USIT2 - Hernie discale - Canal étroit - Grille ECOS.html": SSP("Lombalgies"),
 "Intoxication - Arrêt cardio-respiratoire sur intoxication aux opioïdes - Grille ECOS.html": SSP("Intoxications Aiguës"),
 "Intoxication - Syndrome anticholinergique - Intoxication à la Belladone - Grille ECOS.html": SSP("Intoxications Aiguës"),
 "Intoxication - Syndrome malin des neuroleptiques - Grille ECOS.html": SSP("Syndromes Iatrogènes Psychiatriques (SMN + Sd Sérotoninergique)"),
 "Intoxication médicamenteuse - Paracétamol et benzodiazépines - Grille ECOS.html": SSP("Intoxications Aiguës"),
 "Lupus érythémateux systémique - Femme de 26 ans - Grille ECOS.html": SSP("Douleurs Articulaires"),
 "Lupus érythémateux systémique - Feuille porte.html": SSP("Douleurs Articulaires"),
 "Lésion de la coiffe des rotateurs - Grille ECOS.html": SSP("Douleur d'Épaule"),
 "Mal au dos - Syndrome de Guillain-Barré - Grille ECOS.html": SSP("Lombalgies"),
 "Mal au dos 2 - Syndrome de Guillain-Barré - Grille ECOS.html": SSP("Lombalgies"),
 "Mal à l'épaule - Douleur thoracique - Grille ECOS.html": SSP("Douleur Thoracique"),
 "Ménopause - Femme de 53 ans - Grille ECOS.html": SSP("Ménopause"),
 "Ostéoporose prévention - Femme de 56 ans - Feuille porte.html": SSP("Ménopause"),
 "Ostéoporose prévention - Femme de 56 ans - Grille ECOS.html": SSP("Ménopause"),
 "Otosclérose - Femme de 33 ans - Grille ECOS.html": SSP("Perte d'Audition"),
 "Pemphigoïde bulleuse - Femme de 81 ans - Grille ECOS.html": SSP("Éruption Cutanée"),
 "Pharmacologie clinique 1 - Traitement de la douleur - Grille ECOS.html": SK("Réflexes Médicamenteux & Antidotes"),
 "Pharmacologie clinique 3 - Interactions médicamenteuses - Grille ECOS.html": SK("Réflexes Médicamenteux & Antidotes"),
 "Pityriasis versicolor - Homme de 24 ans - Grille ECOS.html": SSP("Éruption Cutanée"),
 "Polymyalgia Rheumatica - Femme de 72 ans - Grille ECOS.html": SSP("Douleurs Articulaires"),
 "Psoriasis - Femme de 42 ans - Grille ECOS.html": SSP("Éruption Cutanée"),
 "Psoriasis - Feuille porte.html": SSP("Éruption Cutanée"),
 "Psy-Vignette 10 - Une femme triste - Grille ECOS.html": SSP("Dépression"),
 "Psy-Vignette 2 - Un jardinier euphorique - Grille ECOS.html": SSP("Troubles de l'Humeur"),
 "Psy-Vignette 3 - Un homme qui vérifie - Grille ECOS.html": SSP("Trouble Anxieux"),
 "Psy-Vignette 4 - Un jeune homme qui se renferme - Grille ECOS.html": SSP("Troubles Psychotiques & Schizophrénie"),
 "Psy-Vignette 5 - Une jeune mère - Grille ECOS.html": SSP("Urgences Psychiatriques (Agitation, PAFA)"),
 "Psy-Vignette 6 - Un pompier qui tremble - Grille ECOS.html": SSP("Trouble Anxieux"),
 "Psy-Vignette 7 - Une jeune femme en colère - Grille ECOS.html": SSP("Urgences Psychiatriques (Agitation, PAFA)"),
 "Psy-Vignette 8 - Une jeune femme qui va se marier - Grille ECOS.html": SSP("Trouble Anxieux"),
 "Psy-Vignette 9 - Un homme qui crie la nuit - Grille ECOS.html": SSP("Troubles Psychotiques & Schizophrénie"),
 "Pédiatrie - Cardiopathie congénitale CIV - Grille ECOS.html": SSP("Troubles de la Croissance (Retard - Grande taille)"),
 "Pédiatrie - Détresse respiratoire bronchiolite et asthme - Grille ECOS.html": SSP("Détresse Respiratoire (Adulte-Enfant non-néonatal)"),
 "Pédiatrie - Enfant 3 ans avec toux - Grille ECOS.html": SSP("Toux Chronique"),
 "Pédiatrie - Nourrisson 6 mois avec fièvre - Grille ECOS.html": SSP("Fièvre du Nourrisson"),
 "Pédiatrie - Nouveau-né en détresse respiratoire - Grille ECOS.html": SSP("Détresse Respiratoire Néonatale"),
 "Pédiatrie - Nouveau-né normal et suivi - Grille ECOS.html": SSP("Prévention Pédiatrique (consultations & dépistages systématiques)"),
 "Pédiatrie - Occlusion sur bride - Grille ECOS.html": SSP("Urgences Abdominales Chirurgicales"),
 "Pédiatrie - Torsion testiculaire - Grille ECOS.html": SSP("Douleur Testiculaire"),
 "Pédiatrie - Vomissements et état fébrile - Méningite bactérienne - Grille ECOS.html": SSP("Fièvre du Nourrisson"),
 "Pédiatrie - État fébrile sans foyer - Bactériémie occulte - Grille ECOS.html": SSP("Fièvre du Nourrisson"),
 "SD - Dépistage cancer colorectal - Grille ECOS.html": SSP("SD Counselling Dépistages (cancer, CV, IST)"),
 "SD - Dépistage cancer du sein - Grille ECOS.html": SSP("SD Counselling Dépistages (cancer, CV, IST)"),
 "SD - Dépistage cancer prostate - Grille ECOS.html": SSP("SD Counselling Dépistages (cancer, CV, IST)"),
 "SMIG-1 - Syncope - Grille ECOS.html": SSP("Syncope"),
 "SMIG-2 - Situation 1 - Crise convulsive - Hyponatrémie sur thiazides - Grille ECOS.html": SSP("Malaise & Perte de Connaissance Brève"),
 "SMIG-2 - Situation 2 - Masse pulmonaire - SIADH sur cancer pulmonaire - Grille ECOS.html": SSP("Toux Chronique"),
 "SMIG-2 - Situation 3 - OMI - Hyponatrémie sur insuffisance cardiaque - Grille ECOS.html": SSP("Œdèmes des Membres Inférieurs"),
 "SMIG-3 - Douleurs abdominales et nausées - Acidocétose diabétique - Grille ECOS.html": SSP("Polydipsie & Polyurie"),
 "SMIG-4 - Fièvre prolongée et amaigrissement - Tuberculose - Grille ECOS.html": SSP("Fièvre"),
 "SMIG-5 - Examen clinique ciblé par hypothèses - Grille ECOS.html": SSP("Dyspnée"),
 "Sclérose en plaques - Femme de 32 ans - Grille ECOS.html": SSP("Amaurose & Baisse d'Acuité Visuelle"),
 "Syndrome de Guillain-Barré - Homme de 42 ans - Grille ECOS.html": SSP("Neuropathie Périphérique"),
 "Syndrome de Stevens-Johnson - Homme de 32 ans - Grille ECOS.html": SSP("Éruption Cutanée"),
 "Syndrome du canal carpien - Grille ECOS.html": SSP("Douleur au Poignet"),
 "Syphilis secondaire - Homme de 50 ans - Grille ECOS.html": SSP("Éruption Cutanée"),
 "Sémiologie MSQ - Coxarthrose - Grille ECOS.html": SSP("Douleur de Hanche"),
 "Sémiologie MSQ - Polyarthrite rhumatoïde - Grille ECOS.html": SSP("Douleurs Articulaires"),
 "TDAH pédiatrique - Garçon de 9 ans - Feuille porte.html": SSP("Troubles du Développement & Croissance"),
 "TDAH pédiatrique - Garçon de 9 ans - Grille ECOS.html": SSP("Troubles du Développement & Croissance"),
 "Toux et maux de ventre - Pédiatrie - Grille ECOS.html": SSP("Toux Chronique"),
 "Transaminases élevées - Homme de 50 ans - Feuille porte.html": SSP("Ictère"),
 "Transaminases élevées - Homme de 50 ans - Grille ECOS.html": SSP("Ictère"),
 "Trouble panique - Femme de 42 ans - Grille ECOS.html": SSP("Trouble Anxieux"),
 "Urticaire allergique aux crevettes - Homme de 27 ans - Grille ECOS.html": SSP("Éruption Cutanée"),
 "Voyage au Brésil - Femme de 22 ans - Grille ECOS.html": SSP("Fièvre au Retour de Voyage"),
 "Voyage à Madagascar - Père et enfant - Grille ECOS.html": SSP("Fièvre au Retour de Voyage"),
 "Épilepsie absence - Fille de 7 ans - Grille ECOS.html": SSP("Malaise & Perte de Connaissance Brève"),
 "Épisode dépressif majeur - Femme de 35 ans - Grille ECOS.html": SSP("Dépression"),
 "Épisode maniaque - Homme de 28 ans - Grille ECOS.html": SSP("Troubles de l'Humeur"),
 "Érythème cutané avec douleur - Homme de 56 ans - Grille ECOS.html": SSP("Éruption Cutanée"),
}

EXCLUDE_LOCAL = {
 "RCI-Fièvre et douleurs articulaires - Infection gonococcique disséminée - Grille ECOS.html":
    "doublon (82 % de recouvrement avec la version sans préfixe RCI)",
 "Mal au dos - Syndrome de Guillain-Barré - Grille ECOS (1).html":
    "doublon (même patient Z.T. que « Mal au dos 2 », version moins complète)",
 "Psy-Vignette 1 - Un chirurgien énervé - Grille ECOS.html":
    "trouble de la personnalité narcissique — page manquante",
}

def auto_local_label(fn):
    stem = re.sub(r"\.html$", "", fn)
    porte = stem.endswith("Feuille porte")
    stem = re.sub(r"\s*-\s*(Grille ECOS( \(\d+\))?|Feuille porte)$", "", stem)
    lab = re.sub(r"\s+-\s+", " — ", stem)
    if porte:
        lab += " — 🚪 feuille de porte"
    return lab + " 📁"


# grilles locales
cat_local = json.load(open(f"{SCRATCH}/catalog_local.json"))
LOCAL = {unicodedata.normalize("NFC", k): v for k, v in LOCAL.items()}
LOCAL2 = {unicodedata.normalize("NFC", k): v for k, v in LOCAL2.items()}
EXCLUDE_LOCAL = {unicodedata.normalize("NFC", k): v for k, v in EXCLUDE_LOCAL.items()}
for c in cat_local:
    key = unicodedata.normalize("NFC", c["file"])
    if key in LOCAL:
        page, label, corpus = *LOCAL[key], "rescos"
    elif key in LOCAL2:
        page, label, corpus = LOCAL2[key], auto_local_label(key), "locales"
    elif key in EXCLUDE_LOCAL:
        unmapped.append((dict(c, corpus="local"), EXCLUDE_LOCAL[key]))
        continue
    else:
        unmapped.append((dict(c, corpus="local"), "grille locale sans règle"))
        continue
    entry = dict(c, corpus=corpus, _label=label, _relfile=f"{LOCAL_DIR}/{c['file']}")
    mapping.setdefault(page, []).append(entry)

# ---- YAML ----
def yq(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
CORPUS_ORDER = {"amboss": 0, "german": 1, "rescos": 2, "usmle": 3, "triage": 4, "casecos": 5, "locales": 6}
def sort_key(c): return (CORPUS_ORDER[c["corpus"]], natkey(c["file"]))
def natkey(s): return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", s)]

lines = [
    "# Mapping grilles ECOS → pages Obsidian (généré le 2026-07-23, curation validée)",
    "# Éditez librement pages/labels puis relancez scripts/inject_obsidian_blocks.py",
    "app_base: https://grilles-ecos.replit.app",
    "vault: /Users/damienfulliquet/Documents/Damien/Medecine/Obsidian",
    "pages:",
]
for page in sorted(mapping):
    lines.append(f"  {yq(page)}:")
    for c in sorted(mapping[page], key=sort_key):
        rel = c.get("_relfile") or ('cases/' + c['corpus'] + '/' + c['file'])
        lines.append(f"    - file: {yq(rel)}")
        lines.append(f"      label: {yq(c.get('_label') or make_label(c))}")
lines.append("unmapped:")
for c, why in sorted(unmapped, key=lambda x: x[0]["file"]):
    lines.append(f"  - file: {yq('cases/' + c['corpus'] + '/' + c['file'])}")
    lines.append(f"    raison: {yq(why)}")
open(f"{REPO}/docs/obsidian-mapping.yaml", "w").write("\n".join(lines) + "\n")

# ---- rapport ----
n_mapped = sum(len(v) for v in mapping.values())
print(f"grilles mappées : {n_mapped}/{len(cat)} — pages cibles : {len(mapping)} — non mappées : {len(unmapped)}")
missing_pages = [p for p in mapping if p.split("/")[-1][:-3] not in pages_meta]
if missing_pages: print("⚠️ PAGES INEXISTANTES :", missing_pages)
print("\n--- non mappées ---")
for c, why in unmapped: print(f"  {c['file'][:60]} | {why}")
print("\n--- répartition (top 25) ---")
for p, v in sorted(mapping.items(), key=lambda kv: -len(kv[1]))[:25]:
    print(f"  {len(v):3d}  {p.split('/')[-1][:-3]}")
print("\n--- échantillon de libellés générés ---")
import random; random.seed(7)
sample = random.sample([c for v in mapping.values() for c in v], 18)
for c in sample: print("  ", (c.get("_label") or make_label(c))[:112])
