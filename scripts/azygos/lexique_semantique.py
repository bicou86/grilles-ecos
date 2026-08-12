"""Colorisation sémantique des sections pédagogiques du corpus azygos.

La grille sémantique à huit couleurs est celle du dépôt (`case-styles.css`,
socle partagé) et du vault Obsidian (`skills-ecos.css`) :

    c-red    pathologie / danger        c-pink   symptôme / signe
    c-green  examen / normal / score    c-blue   commentaire
    c-amber  traitement / médicament    c-purple facteur de risque
    c-orange complication               c-yellow concept-clé (surligné)

Pourquoi un lexique et non un passage au fil de l'eau. Les grilles sont
**générées** : toute colorisation faite à la main serait écrasée à la
reconstruction suivante. Les règles vivent donc ici, elles sont relisibles,
corrigibles, et produisent le même résultat à chaque exécution.

Précision assumée. Ces règles reconnaissent des entités cliniques explicites,
pas le sens d'une phrase. Elles sont volontairement conservatrices : mieux vaut
ne pas colorer un terme que le ranger dans la mauvaise famille. Les faux amis
morphologiques (« nécessite », « réduite », « visite » pour le suffixe -ite)
sont exclus nommément.
"""

from __future__ import annotations

import html
import re

# --------------------------------------------------------------------------
# Faux amis : mots que la morphologie médicale attraperait à tort.
# --------------------------------------------------------------------------

EXCLUS = {
    # -ite qui ne sont pas des inflammations
    "nécessite", "réduite", "visite", "limite", "suite", "ensuite", "fuite",
    "conduite", "produite", "introduite", "gratuite", "petite", "gîte", "site",
    "gestuelle", "élite", "gîtes", "gratuité", "traite", "abrite", "excite",
    "invite", "évite", "irrite", "mérite", "hésite", "précipite", "licite",
    "décrite", "décrites", "induite", "induites", "prédite", "droite", "droites",
    "petites", "subite", "subites", "écrite", "écrites", "réécrite",
    # anatomie et résultats de laboratoire, pas des inflammations
    "orbite", "orbites", "nitrites",
    # -ose / -oses non pathologiques
    "chose", "choses", "cause", "causes", "dose", "doses", "pose", "propose",
    "repose", "expose", "suppose", "impose", "oppose", "glucose", "prose",
    "morose", "close", "dispose",
    # -ome / -omes non tumoraux
    "symptôme", "symptômes", "diplôme", "arôme", "royaume", "volume", "résume",
    # « syndrome » seul est un mot de catégorie ; nommé, il est capté plus haut
    "syndrome", "syndromes",
    # -émie / -algie faux positifs
    "académie",
}

# --------------------------------------------------------------------------
# Règles, de la plus spécifique à la plus générale. Chaque entrée est
# (classe, motif). Le moteur retient les correspondances les plus longues.
# --------------------------------------------------------------------------

def _mots(*termes: str) -> str:
    """Alternative regex sur des termes ENTIERS, pluriels tolérés.

    Les frontières `\\b` sont indispensables : sans elles, et avec `re.I`,
    « CT » se retrouve dans « conta**ct** » et « AINS » dans « cert**ains** ».
    """
    return r"\b(?:" + "|".join(termes) + r")\b"


REGLES: list[tuple[str, str]] = [
    # ---- concept-clé : ce que le cas veut faire retenir -------------------
    ("c-yellow", r"\bsignes? d[e’']alarme\b"),
    ("c-yellow", r"\bred flags?\b"),
    ("c-yellow", r"\bdiagnostic d[e’']emblée\b"),
    ("c-yellow", r"\bdiagnostics? différentiels?\b"),
    ("c-yellow", r"\burgence (?:vitale|absolue|chirurgicale|ophtalmologique|médicale)\b"),
    ("c-yellow", r"\bfilet de sécurité\b"),
    ("c-yellow", r"\bprise en charge immédiate\b"),
    ("c-yellow", r"\bcritères? de gravité\b"),
    ("c-yellow", r"\bdiagnostic d[e’']exclusion\b"),
    ("c-yellow", r"\blevée d[e’']inhibition\b"),
    ("c-yellow", r"\bplans? de sécurité\b"),
    ("c-yellow", r"\bcritères? (?:du )?DSM(?:-5)?\b"),
    ("c-yellow", r"\bplacement à des fins d[e’']assistance\b"),
    ("c-yellow", r"\bPAFA\b"),
    # Le verbe seul (« à écarter ») est un mouvement de raisonnement, pas un
    # concept à retenir : gardé uniquement quand il porte l'urgence.
    ("c-yellow", r"\bà (?:éliminer|écarter|exclure) (?:en priorité|d[e’']emblée)\b"),

    # ---- complication ----------------------------------------------------
    ("c-orange", r"\bcomplications? (?:graves?|sévères?|redoutables?|possibles?)\b"),
    ("c-orange", _mots(
        r"complications?", r"récidives?", r"chronicisation", r"séquelles?",
        r"perforations?", r"nécroses?", r"sepsis", r"septicémie",
        r"hémorragies?", r"embolies?", r"cécité", r"abcès", r"rupture[s]?",
        r"perte définitive de la vision", r"amputation", r"insuffisance rénale",
        r"choc (?:septique|hypovolémique|anaphylactique)",
    )),

    # ---- facteur de risque ----------------------------------------------
    ("c-purple", r"\bfacteurs? (?:de )?risques?\b"),
    ("c-purple", _mots(
        r"tabagisme", r"tabac", r"alcool(?:isme)?", r"obésité", r"surpoids",
        r"sédentarité", r"antécédents familiaux", r"hérédité", r"âge avancé",
        r"immunosuppression", r"immunodépression", r"diabète(?: sucré)?",
        r"hypertension(?: artérielle)?", r"contraception (?:orale|hormonale)",
        r"grossesse", r"exposition solaire", r"atopie",
    )),
    # `risque` nu est écarté pour la même raison que `symptôme` : 179
    # occurrences, et « facteur de risque » — le terme qui porte le sens — a
    # déjà sa règle, plus longue, donc prioritaire.
    ("c-purple", _mots(r"antécédents?", r"comorbidités?", r"prédispositions?")),

    # ---- traitement / médicament / geste --------------------------------
    ("c-amber", r"\b[a-zà-ÿ]{4,}thérapies?\b"),
    ("c-amber", _mots(
        r"AINS", r"corticostéroïdes?", r"corticoïdes?", r"antibiotiques?",
        r"antihistaminiques?", r"antalgiques?", r"analgésiques?", r"opioïdes?",
        r"bêtabloquants?", r"bétabloquants?", r"anticoagulants?",
        r"inhibiteurs? de l[e’'](?:ECA|anhydrase carbonique)",
        r"analogues? de la vitamine D", r"vaccinations?", r"vaccins?",
        r"chirurgie", r"opération", r"drainage", r"immobilisation",
        r"kératolyse", r"lavage nasal", r"inhalation", r"perfusion",
        r"traitement (?:topique|systémique|local|symptomatique|de fond)",
    )),
    ("c-amber", _mots(
        r"traitements?", r"thérapeutiques?", r"thérapies?", r"médicaments?",
        r"prise en charge", r"posologies?", r"prescriptions?",
    )),
    # Psychotropes et psychothérapies.
    ("c-amber", _mots(
        r"antidépresseurs?", r"ISRS", r"IRSN", r"thymorégulateurs?",
        r"psychothérapies?", r"TCC", r"thérapie cognitivo-comportementale",
        r"thérapie interpersonnelle", r"activation comportementale", r"MBCT",
        r"sertraline", r"escitalopram", r"venlafaxine", r"lévothyroxine",
        r"benzodiazépines?", r"luminothérapie", r"arrêts? de travail",
        r"neuroleptiques?", r"antipsychotiques?", r"lithium",
        r"électroconvulsivothérapie", r"ECT",
        r"exposition avec prévention de la réponse", r"thérapie de couple",
    )),

    # ---- examen / normal / score ----------------------------------------
    # Éponymes : « signe de Murphy », « test de Lachman ». L'initiale majuscule
    # est ce qui distingue l'éponyme de « indice d'une baisse… », d'où le
    # drapeau localisé `(?-i:…)` — `re.I` global annulerait la contrainte.
    ("c-green", r"\b(?:signe|test|manœuvre|score) d[eu’'] ?(?-i:[A-ZÀ-Ý])[A-Za-zÀ-ÿ-]+\b"),
    ("c-green", _mots(
        r"signe de la bougie", r"signe de la dernière lamelle",
        r"phénomène de Köbner", r"signes? de grattage",
    )),
    ("c-green", _mots(
        r"échographies?", r"radiographies?", r"scanner", r"tomodensitométrie",
        r"IRM", r"CT(?:-scan)?", r"dermatoscopie", r"otoscopie", r"rhinoscopie",
        r"ophtalmoscopie", r"laryngoscopie", r"spirométrie", r"ECG",
        r"palpations?", r"auscultations?", r"inspections?", r"percussions?",
        r"examen à l[e’']état frais", r"bilan (?:biologique|sanguin|de laboratoire)",
        r"tonométrie", r"acuité visuelle", r"champ visuel",
        r"status neurovasculaire", r"statut neurovasculaire",
    )),
    # Le registre de l'ORIENTATION, propre aux justifications d'azygos : ces
    # bulles disent pourquoi on cherche, avec le vocabulaire de la démarche
    # plutôt que celui des entités. Il est absent des règles réglées sur du
    # texte de résumé, d'où la moitié de densité manquante du corpus.
    ("c-green", r"\bexamens? (?:clinique|physique|neurologique|ophtalmologique"
                r"|au spéculum|complémentaires?)\b"),
    ("c-green", r"\b(?:status|statut) (?:neurologique|cardiaque|respiratoire"
                r"|abdominal|articulaire|cutané|local)\b"),
    ("c-green", r"\banamnèses?(?: ciblée| systématique| par systèmes?)?\b"),
    ("c-green", _mots(
        r"dépistages?", r"bilans?", r"laboratoire", r"paramètres? vitaux?",
        r"évaluations? clinique", r"examens? de laboratoire",
    )),
    # Échelles et instruments — l'équivalent psychiatrique d'un examen.
    ("c-green", _mots(
        r"PHQ-9", r"Hamilton", r"MDQ", r"échelles?", r"questionnaires?",
        r"TSH", r"FSC", r"ionogrammes?", r"entretiens? cliniques?",
        r"folates?", r"vitamines? [BD]\d*",
    )),

    # ---- symptôme / signe ------------------------------------------------
    ("c-pink", _mots(
        r"douleurs?", r"céphalées?", r"prurit", r"dyspnées?", r"fièvre",
        r"nausées?", r"vomissements?", r"vertiges?", r"asthénie", r"fatigue",
        r"toux", r"dysurie", r"hématurie", r"ictère", r"œdèmes?", r"oedèmes?",
        r"paresthésies?", r"photophobie", r"halos? (?:colorés?|lumineux)",
        r"baisse (?:de l[e’'])?(?:acuité visuelle|visus)", r"raideur matinale",
        r"perte de poids", r"sueurs nocturnes", r"palpitations?",
        r"saignements?", r"éruptions? cutanées?",
    )),
    # Les termes de la sémiologie et ses descripteurs. « signe de Murphy »
    # reste vert : l'éponyme est déclaré plus haut et il est plus long, donc
    # le moteur le retient d'abord.
    #
    # `symptôme` et `signe` NUS sont volontairement absents : 546 occurrences
    # dans le corpus, et les colorer porte la densité à 86,6 — au-dessus du
    # plafond de 80 — sans rien signaler. « Ces signes sont typiques » ne dit
    # pas plus en rose qu'en noir. Le mot qui compte est celui qui nomme le
    # signe, et il a déjà sa règle.
    ("c-pink", _mots(
        r"troubles?", r"atteintes?", r"lésions?",
        r"crises?", r"syncopes?", r"chutes?", r"malaises?",
        r"perte de (?:connaissance|vision|audition|force|équilibre)",
    )),
    # Sémiologie psychiatrique : ce que la patiente décrit et ce qui se voit.
    ("c-pink", r"\bhumeurs? dépressives?\b"),
    ("c-pink", r"\bralentissements? psychomoteurs?\b"),
    ("c-pink", r"\bsymptômes? (?:positifs?|négatifs?|psychotiques?|maniaques?|cardinaux)\b"),
    ("c-pink", _mots(
        r"anhédonies?", r"dévalorisations?", r"culpabilités?", r"ruminations?",
        r"insomnies?", r"hypersomnies?", r"anxiétés?", r"désespoirs?",
        r"labilités? émotionnelles?", r"retraits? sociaux?", r"apathies?",
        r"psychomoteur(?:s|e|es)?", r"hallucinations?", r"idées? délirantes?",
        # Sémiologie psychotique, obsessionnelle et de la personnalité :
        # le registre des dix vignettes « Psy » de rescos-locales.
        r"obsessions?", r"compulsions?", r"rituels", r"délires?",
        r"grandioses?", r"grandiosités?", r"désorganisations?",
        r"avolitions?", r"alogies?", r"émoussements?", r"méfiances?",
        r"volubilités?", r"logorrhées?", r"fuite des idées", r"distractibilités?",
        r"perplexités?", r"ambivalences?",
    )),
    ("c-pink", _mots(
        r"aigu[ëe]?s?", r"chroniques?", r"brutal(?:e|es|aux)?",
        r"progressi(?:f|ve|ves)", r"unilatéral(?:e|es|aux)?",
        r"bilatéral(?:e|es|aux)?", r"intermittent(?:e|es|s)?",
        r"irradiations?", r"prodromes?",
    )),

    # ---- pathologie / danger --------------------------------------------
    # Entités nommées d'abord : elles priment sur la morphologie.
    ("c-red", r"\bsyndromes? (?:de |du |d[e’']')?[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ-]{2,}\b"),
    ("c-red", _mots(
        r"glaucome(?: aigu| par fermeture de l[e’']angle)?", r"psoriasis(?: vulgaris)?",
        r"blocage angulaire(?: aigu)?", r"artérite à cellules géantes",
        r"appendicites?", r"cholécystites?", r"pancréatites?", r"pyélonéphrites?",
        r"méningites?", r"pneumonies?", r"embolie pulmonaire",
        r"infarctus(?: du myocarde)?", r"accident vasculaire cérébral", r"AVC",
        r"tendinopathies?(?: de la coiffe des rotateurs| calcifiante)?",
        r"carcinomes?", r"mélanomes?", r"lymphomes?", r"tumeurs? maligne[s]?",
        r"fractures?", r"luxations?", r"torsions? (?:testiculaire|ovarienne)",
        r"tinea corporis", r"eczémas?(?: atopique| séborrhéique)?",
    )),
    # PSYCHIATRIE. Le lexique a été réglé sur azygos, corpus somatique : rien
    # n'y couvrait le registre psychiatrique, et les dix vignettes « Psy » de
    # `rescos-locales` rendaient 31 spans pour 1000 mots contre 107 pour leur
    # corpus. Le danger vient en premier — c'est ce qui se cherche et se cote.
    ("c-red", r"\brisques? suicidaires?\b"),
    ("c-red", r"\bidéations? suicidaires?\b"),
    ("c-red", r"\bidées? de mort\b"),
    ("c-red", r"\bactes? préparatoires?\b"),
    ("c-red", r"\bépisodes? (?:dépressifs? majeurs?|maniaques?|mixtes?)\b"),
    ("c-red", r"\btroubles? de la personnalité(?: \w+)?\b"),
    ("c-red", r"\bpersonnalités? (?:narcissique|paranoïaque|borderline|antisociale|évitante|dépendante)\b"),
    ("c-red", r"\btroubles? obsessionnels?(?:[- ]compulsifs?)?\b"),
    ("c-red", r"\bpsychoses? (?:puerpérale|du post-partum)\b"),
    ("c-red", _mots(
        r"suicides?", r"suicidaires?", r"dépressions?", r"dépressi(?:f|ve|fs|ves)",
        r"troubles? bipolaires?", r"bipolarités?", r"manies?", r"hypomanies?",
        r"maniaques?", r"états? mixtes?", r"virages? maniaques?",
        r"psychoses?", r"troubles? psychotiques?", r"catatonies?", r"incuries?",
        r"hypothyroïdies?", r"hyperthyroïdies?",
        r"schizophrénies?", r"troubles? schizo-affectifs?", r"TOC",
        r"infanticides?", r"narcissiques?", r"paranoïaques?",
    )),
    # Éponymes de maladie, puis les génériques de la catégorie.
    ("c-red", r"\bmaladies? (?:de |du |d[e’'])[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ-]{2,}\b"),
    ("c-red", _mots(
        r"pathologies?", r"maladies?", r"infections?", r"traumatismes?",
        r"atteintes? (?:centrale|organique|systémique)",
    )),
    # Morphologie ensuite, avec garde sur les faux amis.
    ("c-red", r"\b[a-zà-ÿ]{3,}(?:ite|ites)\b"),
    ("c-red", r"\b[a-zà-ÿ]{5,}(?:ose|oses|osis)\b"),
    ("c-red", r"\b[a-zà-ÿ]{5,}(?:pathie|pathies)\b"),
    ("c-red", r"\b[a-zà-ÿ]{5,}(?:ome|omes)\b"),
    ("c-red", r"\b[a-zà-ÿ]{5,}(?:algie|algies)\b"),
    ("c-red", r"\b[a-zà-ÿ]{5,}(?:émie|émies)\b"),

    # ---- commentaire : le méta-discours d'examen -------------------------
    # Ces bulles alternent le clinique (« ce que la douleur oriente ») et le
    # docimologique (« ce qui est évalué ici »). Le second registre est un
    # commentaire sur l'épreuve, pas sur le patient : il mérite sa couleur.
    ("c-blue", r"\bSur AZYGOS[^.;]{0,160}[.;]"),
    ("c-blue", _mots(
        r"le candidat", r"la candidate", r"l[e’']examinateur",
        r"ce qui est évalué", r"pour l[e’']évaluation",
        r"patients? standardisés?", r"patiente standardisée",
    )),
]

_COMPILEES = [(cls, re.compile(motif, re.I)) for cls, motif in REGLES]


def _valide(fragment: str) -> bool:
    """Écarte les correspondances qui tombent sur un faux ami."""
    return fragment.strip().lower().strip(".,;:()") not in EXCLUS


def colorise(texte: str) -> str:
    """Renvoie le texte échappé, entités cliniques enveloppées d'un `<span>`.

    L'échappement se fait segment par segment : coloriser après un
    `html.escape` global casserait les motifs, les apostrophes françaises
    devenant `&#x27;`.
    """
    if not texte:
        return ""

    # 1. Collecte de toutes les correspondances, avec leur classe.
    trouvees: list[tuple[int, int, str]] = []
    for cls, motif in _COMPILEES:
        for m in motif.finditer(texte):
            if m.end() > m.start() and _valide(m.group(0)):
                trouvees.append((m.start(), m.end(), cls))

    # 2. Résolution des chevauchements : la plus longue gagne, puis la
    #    première déclarée (les règles sont ordonnées du spécifique au
    #    général).
    trouvees.sort(key=lambda t: (t[0], -(t[1] - t[0])))
    retenues: list[tuple[int, int, str]] = []
    fin_precedente = -1
    for debut, fin, cls in trouvees:
        if debut >= fin_precedente:
            retenues.append((debut, fin, cls))
            fin_precedente = fin

    # 3. Reconstruction.
    morceaux: list[str] = []
    curseur = 0
    for debut, fin, cls in retenues:
        morceaux.append(html.escape(texte[curseur:debut], quote=True))
        morceaux.append(
            f'<span class="{cls}">{html.escape(texte[debut:fin], quote=True)}</span>'
        )
        curseur = fin
    morceaux.append(html.escape(texte[curseur:], quote=True))
    return "".join(morceaux)


def statistiques(textes: list[str]) -> dict[str, int]:
    """Compte les spans par classe — sert au réglage et aux contrôles."""
    from collections import Counter

    compte: Counter = Counter()
    for t in textes:
        for cls in re.findall(r'<span class="(c-[a-z]+)">', colorise(t)):
            compte[cls] += 1
    return dict(compte)
