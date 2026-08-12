# -*- coding: utf-8 -*-
"""Contenu pédagogique — Psy-Vignette 10, « Une femme triste ».

Tout ce qui suit est dérivé de la grille elle-même : critères notés des quatre
sections, bloc `annexe-dd` (critères DSM-5, sévérité, différentiels, sécurité du
traitement, virage maniaque, critères d'hospitalisation) et bloc `cloture`
(clôture type, questions difficiles, réponses types). Aucune source externe.

Écrire en TEXTE BRUT. Le balisage sémantique est posé par
`lexique_semantique.colorise()` à l'injection — ne pas mettre de `<span>` ici.
"""

CONTENU = {
    "grille": "rescos-locales/Psy-Vignette 10 - Une femme triste - Grille ECOS.html",
    "titre_resume": "Épisode dépressif majeur – Résumé ECOS",
    "titre_cas": "Épisode dépressif majeur",

    # ------------------------------------------------------------------ résumé
    "resume": [
        ("🔍 Anamnèse", [
            ("Les neuf critères, et il en faut cinq", [
                "Humeur dépressive presque toute la journée, presque tous les jours — ici depuis 3 mois",
                "Anhédonie : plus rien ne procure de plaisir. Avec l'humeur, c'est l'un des deux critères obligatoires",
                "Troubles du sommeil : réveil précoce à 4 h du matin, typique de la dépression mélancolique",
                "Perte d'appétit et perte de poids — 8 kg en 3 mois, une perte significative à objectiser",
                "Ralentissement psychomoteur, visible à l'entretien avant même d'être rapporté",
                "Fatigue et perte d'énergie dès le réveil",
                "Dévalorisation et culpabilité excessive : « je ne vaux rien », « tout est de ma faute »",
                "Troubles de la concentration, indécision, ruminations",
                "Idées de mort : « j'aimerais ne plus me réveiller »",
            ]),
            ("Ce qu'il faut avoir demandé en plus", [
                "Le risque suicidaire, en détail : idées de mort, idéation, plan, moyens, actes préparatoires, tentatives antérieures",
                "Les facteurs protecteurs — ici ses enfants, qu'elle cite spontanément",
                "Un antécédent d'hypomanie ou de manie, avant toute prescription d'antidépresseur",
                "Les antécédents personnels et familiaux : un épisode il y a 10 ans, une mère dépressive",
                "Le traitement qui avait fonctionné à l'époque : c'est le meilleur prédicteur de réponse",
                "Une cause organique traitable : hypothyroïdie connue, sous lévothyroxine",
                "L'impact fonctionnel : arrêts maladie répétés, retrait social, difficulté à se lever",
                "Le contexte déclenchant : surcharge de travail, divorce il y a 6 mois",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Ce qui se voit sans rien demander", [
                "Ralentissement psychomoteur, faciès triste, contact visuel pauvre, voix monocorde et lente",
                "Affect restreint, labilité émotionnelle avec pleurs, anxiété associée",
                "Attention et concentration diminuées, mémoire de travail affectée — sans confusion",
            ]),
            ("Ce qu'il faut chercher activement", [
                "Symptômes psychotiques : hallucinations, idées délirantes, culpabilité délirante — absents ici, et leur présence changerait la prise en charge",
                "Perte de poids objectivée à la pesée, et non seulement rapportée",
                "Paramètres vitaux et palpation thyroïdienne, pour ne pas manquer une cause organique",
                "Capacité de jugement et de discernement, qui conditionne la décision partagée",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Pour étayer et graduer", [
                "Le diagnostic est clinique : échelle PHQ-9 ou Hamilton pour graduer, pas pour diagnostiquer",
                "Score PHQ-9 attendu ici entre 15 et 20, soit une dépression modérée à sévère",
                "Questionnaire de dépistage de la bipolarité avant toute prescription",
            ]),
            ("Pour éliminer une cause organique", [
                "TSH de contrôle : l'hypothyroïdie est connue et traitée, encore faut-il qu'elle soit équilibrée",
                "FSC, ionogramme, fonction rénale et hépatique",
                "Vitamine D, vitamine B12, folates",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Traitement", [
                "Antidépresseur de première ligne : sertraline 50 à 200 mg/j, escitalopram 10 à 20 mg/j ou venlafaxine XR 75 à 225 mg/j",
                "Reprendre en priorité la molécule qui avait fonctionné il y a 10 ans",
                "Introduction progressive, pour limiter l'aggravation initiale de l'anxiété",
                "Poursuivre 6 à 12 mois après la rémission ; traitement au long cours en cas de récidive",
                "Psychothérapie, efficace seule ou en association : TCC, thérapie interpersonnelle, activation comportementale, MBCT — 12 à 20 séances, hebdomadaires au début",
                "Arrêt de travail thérapeutique temporaire, puis reprise progressive avec aménagements",
                "Activité physique régulière, hygiène du sommeil, réactivation sociale progressive, implication des proches",
            ]),
            ("Sécurité — le point qui décide de la station", [
                "Les premières semaines d'antidépresseur sont les plus à risque, par levée d'inhibition",
                "Revoir à une semaine, puis à deux ; prescrire en petites quantités",
                "Restreindre l'accès aux moyens létaux, avec l'accord de la patiente et de son entourage",
                "Remettre un filet de sécurité par écrit : La Main Tendue 143, disponible 24 h/24, et le 144 en cas de danger imminent",
                "Prévenir du délai d'action de 2 à 4 semaines — sans cet avertissement, la patiente arrête le traitement en le croyant inefficace",
            ]),
        ]),
    ],

    "points_cles": [
        "Deux critères sont obligatoires : humeur dépressive ou anhédonie. Sans l'un des deux, ce n'est pas un épisode dépressif majeur, quel que soit le nombre des autres",
        "L'évaluation du risque suicidaire n'est pas une question, c'est une séquence : idées de mort, idéation, plan, moyens, actes préparatoires, antécédents, facteurs protecteurs",
        "La levée d'inhibition précède l'effet sur l'humeur : la patiente retrouve l'énergie d'agir avant de perdre l'envie de mourir. Le risque suicidaire peut donc augmenter au début du traitement",
        "Dépister la bipolarité avant de prescrire : un antidépresseur seul peut faire virer un trouble bipolaire non diagnostiqué vers un épisode maniaque ou mixte",
        "L'antécédent de bonne réponse à une molécule est le meilleur argument pour la reprendre",
        "Une hypothyroïdie traitée n'exclut pas une hypothyroïdie déséquilibrée : demander la TSH de contrôle",
        "Nommer la maladie et déculpabiliser fait partie du traitement — « ce n'est ni votre faute ni un signe de faiblesse »",
    ],

    "checklist": [
        ("Questions à poser", [
            "Depuis quand, tous les jours, toute la journée ?",
            "Qu'est-ce qui vous faisait plaisir avant, et qu'est-ce qui vous en procure encore ?",
            "Comment dort-elle, à quelle heure se réveille-t-elle, combien a-t-elle perdu ?",
            "Vous arrive-t-il de penser que la vie ne vaut plus la peine ? Y avez-vous pensé pour vous ? Avez-vous imaginé comment ?",
            "Qu'est-ce qui vous retient ?",
            "Avez-vous déjà connu des périodes où vous dormiez peu sans être fatiguée, avec beaucoup d'énergie et d'idées ?",
            "Avez-vous déjà eu un épisode comme celui-ci, et qu'est-ce qui avait aidé ?",
        ]),
        ("Examens à faire", [
            "Entretien clinique structuré sur les neuf critères",
            "PHQ-9 ou Hamilton pour graduer la sévérité",
            "Questionnaire de dépistage de la bipolarité",
            "TSH de contrôle, FSC, ionogramme, fonction rénale et hépatique",
            "Vitamine D, vitamine B12, folates",
            "Pesée, paramètres vitaux, palpation thyroïdienne",
        ]),
        ("Prise en charge en 3 points", [
            "Antidépresseur de première ligne, de préférence celui qui avait fonctionné, introduit progressivement",
            "Psychothérapie et arrêt de travail temporaire",
            "Plan de sécurité écrit, contrôle à une semaine, numéros d'urgence remis en main propre",
        ]),
    ],

    # ----------------------------------------------------------------- théorie
    "theorie": [
        ("Compter les critères, et pourquoi cela compte",
         "Le diagnostic d'épisode dépressif majeur repose sur un décompte, pas sur une impression : "
         "au moins cinq symptômes présents pendant deux semaines, dont obligatoirement une humeur "
         "dépressive ou une anhédonie.",
         [
             "Madame D remplit les neuf critères, ce qui est rare et oriente d'emblée vers une forme sévère",
             "S'y ajoutent le critère B, une détresse ou une altération du fonctionnement, et le critère C, qui écarte une substance ou une affection médicale",
             "La sévérité se juge sur le nombre de symptômes, l'altération fonctionnelle, la présence d'une idéation suicidaire et la perte de poids",
             "Une échelle comme le PHQ-9 gradue et permet de suivre l'évolution ; elle ne remplace jamais l'entretien",
         ]),
        ("La levée d'inhibition, ou pourquoi le début du traitement est le moment le plus dangereux",
         "L'effet de l'antidépresseur sur le ralentissement psychomoteur précède son effet sur l'humeur. "
         "La patiente retrouve l'énergie d'agir avant de perdre l'envie de mourir.",
         [
             "Le risque suicidaire peut donc augmenter dans les premières semaines, alors même que le traitement agit",
             "Le sur-risque est établi chez le sujet de moins de 25 ans, et impose une surveillance rapprochée à tout âge",
             "Conduite pratique : revoir à une semaine puis à deux, prescrire en petites quantités, restreindre l'accès aux moyens létaux avec l'accord de la patiente et de son entourage",
             "Prévenir aussi de l'aggravation initiale possible de l'anxiété et du délai d'action de 2 à 4 semaines",
             "Le filet de sécurité se remet par écrit : La Main Tendue 143, 24 h/24, et le 144 si le danger est imminent",
         ]),
        ("Dépister la bipolarité avant de prescrire",
         "Le dépistage d'un trouble bipolaire n'est pas facultatif : c'est une condition préalable à "
         "la prescription.",
         [
             "Tout antidépresseur peut faire virer un trouble bipolaire non diagnostiqué vers un épisode maniaque ou mixte",
             "L'état mixte est la phase la plus à risque suicidaire de la maladie bipolaire",
             "D'où la recherche d'antécédents d'hypomanie ou de manie avant toute ordonnance, et le recours à un questionnaire de dépistage",
             "En cas d'antécédent avéré, l'antidépresseur ne se prescrit pas seul : un thymorégulateur l'accompagne, et l'avis psychiatrique est requis",
             "Réévaluer si l'amélioration est trop rapide ou franchement euphorique",
         ]),
        ("Quand hospitaliser, et sous quel régime",
         "L'hospitalisation se discute sur des critères précis, et la contrainte n'intervient qu'en "
         "dernier recours.",
         [
             "Idées suicidaires avec plan, moyens accessibles ou actes préparatoires ; tentative récente ; désespoir massif",
             "Dépression avec caractéristiques psychotiques, incurie, refus alimentaire, catatonie",
             "Isolement social ou absence d'entourage capable d'assurer la surveillance ; échec du traitement ambulatoire",
             "En cas de refus de soins avec danger, le placement à des fins d'assistance (art. 426 CC) suppose un trouble psychique, la nécessité d'un traitement et l'absence de mesure moins restrictive",
             "Sa durée est de 6 semaines au maximum (art. 429 CC), et le recours au juge est ouvert dans les 10 jours (art. 439 CC)",
             "Décision partagée quand elle est possible, contrainte seulement quand elle ne l'est pas — et toujours expliquée",
         ]),
        ("Ce que le contexte apporte, et ce qu'il n'excuse pas",
         "Une surcharge de travail et un divorce six mois plus tôt expliquent le déclenchement. Ils ne "
         "font pas basculer le diagnostic vers un trouble de l'adaptation.",
         [
             "Le trouble de l'adaptation se discute quand les critères complets de l'épisode dépressif majeur ne sont pas remplis — ce n'est pas le cas ici",
             "L'hypothyroïdie est connue et traitée : elle reste à vérifier par une TSH, mais elle n'explique pas un tableau complet à neuf critères",
             "Un épisode antérieur il y a 10 ans et une mère dépressive constituent des antécédents à valeur pronostique, pas des diagnostics alternatifs",
             "Attribuer la dépression aux circonstances est aussi ce que fait la patiente quand elle se croit responsable : le corriger fait partie du soin",
         ]),
    ],

    # ------------------------------------------------------------ présentation
    "presentation": {
        "checklist_mentale": [
            "Intro : âge, contexte, motif de consultation",
            "Les deux critères obligatoires : humeur dépressive, anhédonie",
            "Les sept autres, comptés un à un : sommeil, appétit et poids, psychomoteur, énergie, culpabilité, concentration, idées de mort",
            "Risque suicidaire en séquence : idées, idéation, plan, moyens, antécédents, facteurs protecteurs",
            "Impact fonctionnel : travail, vie sociale, quotidien",
            "Antécédents personnels et familiaux, et le traitement qui avait marché",
            "Dépistage de la bipolarité, avant de parler traitement",
            "Cause organique : hypothyroïdie connue, TSH à contrôler",
            "Résumé, diagnostic, sévérité, différentiels",
            "Traitement, sécurité des premières semaines, suivi rapproché",
        ],
        "mnemo": ("SIG E CAPS — les huit critères qui accompagnent l'humeur dépressive", [
            "S = Sommeil, perturbé dans un sens ou dans l'autre",
            "I = Intérêt perdu, l'anhédonie",
            "G = Guilt, culpabilité et dévalorisation",
            "E = Énergie effondrée",
            "C = Concentration diminuée",
            "A = Appétit et poids",
            "P = Psychomoteur, ralenti ou agité",
            "S = Suicide, les idées de mort",
        ]),
        "version_longue": [
            "Il s'agit de Madame D, 45 ans, qui consulte au cabinet pour une fatigue et des symptômes "
            "dépressifs évoluant depuis 3 mois.",

            "Elle décrit une humeur dépressive présente tous les jours, toute la journée, et une "
            "anhédonie complète : plus rien ne lui procure de plaisir. S'y associent un réveil précoce "
            "à 4 h du matin, une perte d'appétit avec une perte de 8 kg en 3 mois, un ralentissement "
            "psychomoteur, une fatigue dès le réveil, des troubles de la concentration avec indécision "
            "et ruminations, un sentiment de dévalorisation et une culpabilité excessive.",

            "Elle rapporte des idées de mort — « j'aimerais ne plus me réveiller » — et une idéation "
            "suicidaire occasionnelle, sans plan constitué, sans moyens envisagés et sans antécédent "
            "de tentative. Elle cite spontanément ses enfants comme ce qui la retient.",

            "L'impact fonctionnel est marqué : arrêts maladie répétés, performance professionnelle "
            "effondrée, retrait social, difficulté à se lever le matin.",

            "Le contexte associe une surcharge de travail et un divorce il y a 6 mois. Dans ses "
            "antécédents, un épisode dépressif il y a 10 ans, traité efficacement par un "
            "antidépresseur, une mère dépressive, et une hypothyroïdie traitée par lévothyroxine.",

            "À l'examen, le ralentissement psychomoteur est visible, le faciès est triste, le contact "
            "visuel pauvre et la voix monocorde. L'affect est restreint, avec des pleurs et une "
            "anxiété associée. L'attention et la concentration sont diminuées, sans confusion. Il n'y "
            "a aucun symptôme psychotique et le contact avec la réalité est préservé. La perte de "
            "poids est objectivée, les paramètres vitaux sont normaux et l'examen thyroïdien est sans "
            "particularité. Le jugement est préservé et le risque suicidaire est évalué comme modéré.",

            "Mon diagnostic est un épisode dépressif majeur d'intensité modérée à sévère : les neuf "
            "critères du DSM-5 sont remplis, l'altération fonctionnelle est marquée, une idéation "
            "suicidaire est présente et la perte de poids est significative — le score PHQ-9 attendu "
            "se situe entre 15 et 20.",

            "Comme différentiels, je retiens d'abord un trouble bipolaire, qui reste à écarter par la "
            "recherche d'antécédents d'hypomanie ou de manie avant toute prescription. Une "
            "hypothyroïdie déséquilibrée est peu probable puisqu'elle est traitée, mais je demande une "
            "TSH de contrôle. Un trouble de l'adaptation ne tient pas, les critères complets de "
            "l'épisode dépressif majeur étant remplis.",

            "Je propose un antidépresseur de première ligne, en reprenant si possible la molécule qui "
            "avait fonctionné il y a 10 ans, introduite progressivement, associé à une psychothérapie "
            "et à un arrêt de travail temporaire. Je poursuivrai 6 à 12 mois après la rémission.",

            "Le point critique est la sécurité des premières semaines : par levée d'inhibition, le "
            "risque suicidaire peut augmenter avant que l'humeur ne s'améliore. Je la revois à une "
            "semaine puis à deux, je prescris en petites quantités, je restreins l'accès aux moyens "
            "létaux avec son accord et celui de son entourage, et je lui remets par écrit La Main "
            "Tendue 143 et le 144. Je la préviens du délai d'action de 2 à 4 semaines et d'une "
            "possible majoration initiale de l'anxiété.",
        ],
        "sbar": {
            "S": "Madame D, 45 ans, consulte pour fatigue et symptômes dépressifs depuis 3 mois.",
            "B": "Épisode dépressif il y a 10 ans, bien traité ; mère dépressive ; hypothyroïdie sous lévothyroxine ; divorce il y a 6 mois et surcharge de travail.",
            "A": "Épisode dépressif majeur modéré à sévère, neuf critères sur neuf, perte de 8 kg, idéation suicidaire sans plan, PHQ-9 estimé 15-20. Différentiels : trouble bipolaire à écarter, hypothyroïdie déséquilibrée, trouble de l'adaptation.",
            "R": "Antidépresseur de première ligne après dépistage de la bipolarité, psychothérapie, arrêt de travail, plan de sécurité écrit et contrôle à une semaine.",
        },
        "questions": [
            ("Sur quoi posez-vous le diagnostic ?",
             "Sur un décompte, pas sur une impression : au moins cinq critères pendant deux semaines, "
             "dont obligatoirement une humeur dépressive ou une anhédonie. Ici les neuf sont présents, "
             "avec une altération fonctionnelle marquée et une idéation suicidaire, ce qui situe la "
             "sévérité entre modérée et sévère."),
            ("Comment évaluez-vous le risque suicidaire ?",
             "En séquence, sans jamais présumer de la réponse : idées de mort, puis idéation pour "
             "soi-même, puis plan, puis moyens accessibles, puis actes préparatoires, puis antécédents "
             "de tentative — et enfin les facteurs protecteurs. Madame D a des idées de mort et une "
             "idéation occasionnelle, sans plan ni moyens, et cite ses enfants comme ce qui la retient. "
             "Le risque est modéré, ce qui autorise une prise en charge ambulatoire à condition de la "
             "revoir vite."),
            ("Qu'est-ce qui doit être fait avant de prescrire un antidépresseur ?",
             "Dépister un trouble bipolaire. Un antidépresseur seul peut faire virer une bipolarité non "
             "diagnostiquée vers un épisode maniaque ou mixte, et l'état mixte est la phase la plus à "
             "risque suicidaire. Je cherche donc des antécédents d'hypomanie ou de manie et j'utilise un "
             "questionnaire de dépistage. En cas d'antécédent avéré, l'antidépresseur ne se prescrit pas "
             "seul : un thymorégulateur l'accompagne et l'avis psychiatrique est requis."),
            ("Pourquoi la revoir à une semaine plutôt qu'à un mois ?",
             "À cause de la levée d'inhibition. L'effet sur le ralentissement psychomoteur précède "
             "l'effet sur l'humeur : elle retrouvera l'énergie d'agir avant de perdre l'envie de mourir. "
             "Le risque suicidaire peut donc augmenter dans les premières semaines. Je la revois à une "
             "semaine puis à deux, je prescris en petites quantités et je lui remets par écrit La Main "
             "Tendue 143 et le 144."),
            ("Quels examens complémentaires demandez-vous ?",
             "Une TSH de contrôle en premier lieu : son hypothyroïdie est traitée, encore faut-il "
             "qu'elle soit équilibrée. J'y associe une FSC, un ionogramme, la fonction rénale et "
             "hépatique, ainsi que vitamine D, vitamine B12 et folates. Le diagnostic reste clinique — "
             "ces examens écartent une cause organique, ils ne le posent pas."),
            ("Quand hospitaliseriez-vous cette patiente ?",
             "Devant une idéation suicidaire avec plan, moyens accessibles ou actes préparatoires, une "
             "tentative récente, un désespoir massif, des caractéristiques psychotiques, une incurie, un "
             "refus alimentaire, un isolement sans entourage capable de surveiller, ou un échec du "
             "traitement ambulatoire. Aucun de ces éléments n'est présent ici. En cas de refus de soins "
             "avec danger, le placement à des fins d'assistance suppose un trouble psychique, la "
             "nécessité d'un traitement et l'absence de mesure moins restrictive ; il dure 6 semaines au "
             "maximum et le recours au juge est ouvert dans les 10 jours."),
            ("Elle vous demande si c'est de sa faute. Que répondez-vous ?",
             "Que la dépression est une maladie médicale réelle, avec des causes biologiques et "
             "environnementales, et qu'elle n'est ni sa faute ni un signe de faiblesse. Le dire "
             "explicitement fait partie du traitement : la culpabilité excessive est un symptôme de la "
             "maladie, et la laisser sans réponse revient à laisser un symptôme se retourner contre le "
             "soin."),
        ],
    },

    # --------------------------------------------------------------- scénario
    # Les répliques sont celles des critères notés, entre crochets. Elles sont
    # reprises telles quelles : c'est ce que la grille attend d'entendre.
    "scenario": [
        ("Identité et cadre", [
            ("Nom", "Madame D"),
            ("Âge", "45 ans"),
            ("Lieu", "cabinet de médecine générale"),
            ("Motif", "fatigue et symptômes dépressifs depuis 3 mois"),
            ("Situation", "divorcée depuis 6 mois, mère de plusieurs enfants, en emploi avec une surcharge de travail"),
            ("Position initiale", "assise, épaules basses, mains immobiles sur les genoux"),
        ]),
        ("Jeu de rôle", [
            ("État général", "ralentissement psychomoteur visible, faciès triste, contact visuel pauvre"),
            ("Voix", "monocorde et lente ; laisser des silences avant de répondre"),
            ("Affect", "restreint, avec des pleurs faciles — pleurer si le candidat aborde les enfants ou le divorce"),
            ("Comportement", "répondre par phrases courtes ; ne rien livrer spontanément, sauf si le candidat se montre chaleureux"),
            ("Anxiété", "présente mais discrète, sans agitation"),
        ]),
        ("Phrases à dire telles quelles", [
            ("Humeur", "« Je me sens triste tout le temps »"),
            ("Anhédonie", "« Plus rien ne me fait plaisir »"),
            ("Fatigue", "« Je suis épuisée dès le matin »"),
            ("Ralentissement", "« Tout est au ralenti »"),
            ("Concentration", "« Je n'arrive plus à me concentrer », « J'oublie tout », « Je rumine sans arrêt »"),
            ("Décisions", "« Je n'arrive plus à prendre de décisions »"),
            ("Estime de soi", "« Je ne vaux rien », « Tout est de ma faute », « Je ne sers à rien »"),
            ("Désespoir", "« Rien ne s'améliorera »"),
            ("Pleurs", "« Je pleure pour rien »"),
        ]),
        ("Symptômes somatiques", [
            ("Sommeil", "réveil à 4 h du matin, sans pouvoir se rendormir"),
            ("Appétit", "« Je n'ai plus faim »"),
            ("Poids", "8 kg perdus en 3 mois"),
            ("Libido", "aucun désir"),
            ("Douleurs", "« J'ai mal partout », sans localisation précise"),
        ]),
        ("Risque suicidaire — ce qui se dit, et à quelle condition", [
            ("Idées de mort", "« J'aimerais ne plus me réveiller » — à dire si le candidat pose la question ouvertement"),
            ("Idéation", "« J'y pense parfois » — seulement si le candidat insiste avec tact"),
            ("Plan", "non, pas de plan, aucun moyen envisagé"),
            ("Tentatives", "aucune, jamais"),
            ("Ce qui retient", "« Mes enfants ont besoin de moi »"),
            (None, "Ne jamais livrer ces éléments spontanément : la station évalue la capacité du candidat à les chercher."),
        ]),
        ("Impact et contexte", [
            ("Travail", "plusieurs arrêts maladie, « Je n'y arrive plus »"),
            ("Vie sociale", "« Je ne vois plus personne »"),
            ("Quotidien", "« Je laisse tout tomber », « Même me lever est difficile »"),
            ("Déclencheurs", "surcharge de travail, divorce il y a 6 mois"),
        ]),
        ("Antécédents à donner si on les demande", [
            ("Personnels", "un épisode dépressif il y a 10 ans"),
            ("Traitement d'alors", "un antidépresseur dont elle a oublié le nom, qui avait bien marché"),
            ("Familiaux", "mère dépressive"),
            ("Médicaux", "hypothyroïdie traitée, sous lévothyroxine"),
            ("Hypomanie ou manie", "aucune période d'euphorie, d'hyperactivité ou de sommeil réduit sans fatigue"),
        ]),
        ("Inquiétudes et questions", [
            (None, "« Je vais devoir prendre des médicaments toute ma vie ? »"),
            (None, "« C'est ma faute si je suis déprimée ? »"),
            (None, "« Je vais perdre mon travail ? »"),
            (None, "« Les antidépresseurs changent la personnalité ? »"),
            (None, "« Combien de temps avant d'aller mieux ? »"),
        ]),
    ],
}
