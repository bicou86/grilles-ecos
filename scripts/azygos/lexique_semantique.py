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
