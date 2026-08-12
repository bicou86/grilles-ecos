# -*- coding: utf-8 -*-
"""Contenu pédagogique — RESCOS-29, « Douleur à la jambe ».

Dérivé des critères notés, du bloc `annexe-dd`, du bloc `cloture` et du bloc
`expert` de la grille. Aucune source externe.

Pas de bloc `scenario` : la grille en porte déjà un.
"""

CONTENU = {
    "grille": "rescos/RESCOS-29_-_Douleur_a__la_jambe_-_Grille_ECOS.html",
    "titre_resume": "Thrombose veineuse profonde et embolie pulmonaire – Résumé ECOS",
    "titre_cas": "Œdème unilatéral du membre inférieur avec dyspnée",

    "resume": [
        ("🔍 Anamnèse", [
            ("L'histoire, dans l'ordre où elle s'est déroulée", [
                "Début à la cheville gauche au milieu du voyage, puis extension à la jambe",
                "Gonflement progressif et douloureux, jambe gauche nettement plus grosse que la droite",
                "Alitement de 2 jours, avec amélioration transitoire",
                "Varices anciennes, opérées il y a 4 ans",
            ]),
            ("Le contexte déclenchant", [
                "Tour d'Italie en car, 16 heures d'une seule traite",
                "Retour il y a 4 jours",
                "Position assise prolongée : c'est le facteur déclenchant, et il se date",
            ]),
            ("Le symptôme qui change tout", [
                "Dyspnée d'effort modérée, présente en parlant",
                "Tachypnée à 22/min",
                "Pas de douleur thoracique, pas d'hémoptysie — leur absence n'écarte rien",
                "Devant une thrombose, chercher la dyspnée n'est pas facultatif : c'est chercher l'embolie",
            ]),
            ("Les facteurs de risque, à énumérer un par un", [
                "Cancer actif : cancer du sein droit avec mastectomie il y a 4 ans, récidive locale avec envahissement ganglionnaire il y a 6 mois, chimiothérapie il y a un mois",
                "Voyage prolongé en position assise, immobilisation relative de 2 jours",
                "Obésité : 93 kg pour 1,68 m, IMC supérieur à 30",
                "Âge de 68 ans, varices opérées",
                "Antécédent familial : mère décédée d'une embolie pulmonaire",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Ce qui se mesure", [
                "Circonférence comparée des deux mollets — chiffrée, pas estimée",
                "Œdème prenant le godet, veines superficielles collatérales dilatées",
                "Chaleur, rougeur, douleur au ballottement du mollet",
            ]),
            ("Ce qui cherche l'embolie", [
                "État général conservé, pas de cyanose, dyspnée modérée en parlant",
                "Fréquence respiratoire, fréquence cardiaque, saturation",
                "Auscultation cardio-pulmonaire, recherche de signes de cœur droit",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Calculer avant de prescrire", [
                "Score de Wells pour la thrombose : cancer actif +1, immobilisation ou voyage +1, gonflement unilatéral +1, œdème prenant le godet +1, veines collatérales +1, diagnostic alternatif moins probable +2",
                "Un score supérieur ou égal à 2 signe une probabilité élevée",
                "À probabilité élevée, les D-dimères ne servent plus : on va directement à l'imagerie",
            ]),
            ("L'imagerie", [
                "Échographie-doppler veineux des membres inférieurs, en urgence",
                "Angioscanner thoracique devant la dyspnée et la tachypnée : la question de l'embolie se pose",
                "Bilan avant anticoagulation : formule, crase, créatinine",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Le traitement", [
                "Anticoagulation à dose curative, débutée sans attendre la confirmation si la probabilité est forte",
                "Chez une patiente atteinte d'un cancer actif, le choix de la molécule et la durée obéissent à des règles propres",
                "Contention veineuse et mobilisation précoce — l'alitement n'est plus recommandé",
                "Antalgie",
            ]),
            ("Ce qui se décide ensuite", [
                "La durée du traitement dépend du caractère provoqué ou non de l'épisode, et de l'activité du cancer",
                "Ici l'épisode est provoqué par le voyage, mais le cancer actif est un facteur persistant",
                "Information sur les signes d'embolie devant conduire aux urgences",
                "Prévention lors des futurs voyages : mobilisation, hydratation, contention",
            ]),
        ]),
    ],

    "points_cles": [
        "Devant une thrombose veineuse, chercher la dyspnée revient à chercher l'embolie pulmonaire",
        "L'absence de douleur thoracique et d'hémoptysie n'écarte pas l'embolie : la dyspnée seule suffit à la faire évoquer",
        "Le score de Wells se CALCULE, item par item — ici il est largement supérieur à 2",
        "À probabilité clinique élevée, les D-dimères ne servent plus : on demande l'imagerie",
        "Un cancer actif avec chimiothérapie récente est le facteur de risque le plus lourd de ce dossier",
        "L'alitement n'est plus recommandé : contention et mobilisation précoce",
    ],

    "checklist": [
        ("Questions à poser", [
            "Quand cela a-t-il commencé, et où exactement ?",
            "Avez-vous voyagé ? Combien de temps assise ?",
            "Êtes-vous essoufflée ? À quel effort ?",
            "Avez-vous mal dans la poitrine ? Craché du sang ?",
            "Où en est votre cancer ? Quand a eu lieu la dernière chimiothérapie ?",
            "Êtes-vous restée alitée ? Combien de temps ?",
            "Quelqu'un dans votre famille a-t-il fait une phlébite ou une embolie ?",
        ]),
        ("Examens à faire", [
            "Circonférence comparée des mollets, chiffrée",
            "Godet, veines collatérales, chaleur, ballottement",
            "Fréquence respiratoire, fréquence cardiaque, saturation",
            "Calcul explicite du score de Wells",
        ]),
        ("Prise en charge en 3 points", [
            "Échographie-doppler veineux en urgence, angioscanner devant la dyspnée",
            "Anticoagulation curative sans attendre si la probabilité est forte",
            "Contention, mobilisation précoce, information sur les signes d'alerte",
        ]),
    ],

    "theorie": [
        ("Pourquoi la dyspnée change la consultation",
         "Une thrombose isolée et une thrombose compliquée d'embolie n'ont ni le même bilan ni la même "
         "urgence.",
         [
             "La dyspnée d'effort et la tachypnée à 22/min sont les deux seuls signes présents ici",
             "L'absence de douleur thoracique et d'hémoptysie est fréquente : ces signes manquent dans une majorité d'embolies",
             "Ne pas poser la question de l'essoufflement devant un œdème unilatéral, c'est accepter de manquer l'embolie",
             "La saturation et la fréquence respiratoire se mesurent systématiquement dans ce contexte",
         ]),
        ("Le score de Wells, et ce qu'il commande",
         "Il ne sert pas à faire joli : il détermine la stratégie diagnostique.",
         [
             "Cancer actif, immobilisation ou voyage récent, gonflement unilatéral, godet, veines collatérales, absence de diagnostic alternatif plus probable",
             "Un score supérieur ou égal à 2 place la patiente en probabilité élevée",
             "À probabilité faible, les D-dimères permettent d'exclure ; à probabilité élevée, ils ne servent plus",
             "Demander des D-dimères ici serait perdre du temps sur un résultat qui ne changerait aucune décision",
         ]),
        ("Le cancer, facteur de risque et facteur de décision",
         "Il pèse sur le diagnostic, sur le traitement et sur sa durée.",
         [
             "Un cancer actif multiplie le risque thromboembolique, d'autant plus sous chimiothérapie récente",
             "Ici : récidive locale avec envahissement ganglionnaire il y a 6 mois, chimiothérapie il y a un mois",
             "Le choix de l'anticoagulant et la durée du traitement obéissent à des règles propres à ce terrain",
             "L'épisode est provoqué par le voyage, mais le cancer reste un facteur persistant : la durée ne se décide pas comme pour un épisode provoqué simple",
         ]),
        ("Ce qui a changé dans la prise en charge",
         "Deux réflexes anciens sont aujourd'hui abandonnés.",
         [
             "L'alitement : il n'améliore rien et majore le risque. Mobilisation précoce et contention sont recommandées",
             "L'attente de la confirmation avant d'anticoaguler : à probabilité forte, le traitement se débute d'emblée",
             "La patiente a d'ailleurs constaté une amélioration après deux jours de lit — ce qui n'a rien traité",
             "L'information sur les signes d'embolie devant conduire aux urgences fait partie du traitement",
         ]),
    ],

    "presentation": {
        "checklist_mentale": [
            "Intro : âge, motif, latéralité, ancienneté",
            "Histoire : début, extension, alitement, évolution",
            "Contexte : voyage, durée assise, date du retour",
            "LA question : essoufflement, et à quel effort",
            "Douleur thoracique et hémoptysie, présentes ou absentes",
            "Facteurs de risque, tous, cancer actif en premier",
            "Antécédents personnels et familiaux thromboemboliques",
            "Examen : mollets chiffrés, godet, collatérales, constantes respiratoires",
            "Calcul explicite du score de Wells",
            "Doppler, angioscanner, anticoagulation sans attendre",
        ],
        "mnemo": ("« Une jambe, deux questions »", [
            "La jambe : circonférence, godet, collatérales",
            "Le poumon : essoufflée ? à quel effort ?",
            "Le score : Wells calculé, item par item",
            "La décision : probabilité forte → imagerie, pas D-dimères",
        ]),
        "version_longue": [
            "Il s'agit d'une femme de 68 ans, retraitée, qui consulte pour un œdème et une douleur de la "
            "cheville et de la jambe gauche, associés à une dyspnée d'effort.",

            "Les symptômes ont débuté à la cheville gauche au milieu d'un voyage, puis se sont étendus à "
            "la jambe, avec un gonflement progressif et douloureux. Sa jambe gauche est nettement plus "
            "grosse que la droite. Elle est restée alitée deux jours, avec une amélioration transitoire. "
            "Elle a des varices anciennes, opérées il y a quatre ans, et elle est inquiète parce qu'un "
            "médecin a parlé de phlébite et qu'elle craint une gangrène.",

            "Le contexte est déterminant : elle rentre d'un tour d'Italie en car, avec un trajet de "
            "seize heures d'une seule traite, en position assise prolongée. Le retour date de quatre "
            "jours.",

            "Et surtout, elle décrit une dyspnée d'effort modérée, présente en parlant, avec une "
            "tachypnée à 22 par minute. Elle n'a ni douleur thoracique ni hémoptysie — mais leur absence "
            "n'écarte rien, ces signes manquant dans la majorité des embolies pulmonaires.",

            "Ses facteurs de risque thromboembolique sont nombreux et lourds. Au premier rang, un cancer "
            "actif : cancer du sein droit avec mastectomie il y a quatre ans, récidive locale avec "
            "envahissement ganglionnaire il y a six mois, et quatre cures de chimiothérapie dont la "
            "dernière il y a un mois. S'y ajoutent le voyage prolongé, l'immobilisation relative de deux "
            "jours, une obésité à 93 kg pour 1,68 m, l'âge de 68 ans et des varices opérées. Sa mère est "
            "décédée d'une embolie pulmonaire.",

            "À l'examen, l'état général est conservé, il n'y a pas de cyanose, la dyspnée est modérée en "
            "parlant et il existe une tachypnée. La jambe gauche est augmentée de volume, avec un œdème "
            "prenant le godet et des veines superficielles collatérales.",

            "Je calcule le score de Wells pour la thrombose veineuse profonde : cancer actif un point, "
            "immobilisation et voyage un point, gonflement unilatéral un point, œdème prenant le godet "
            "un point, veines superficielles collatérales un point, et diagnostic alternatif moins "
            "probable deux points. Le score est largement supérieur à 2, ce qui place la patiente en "
            "probabilité élevée.",

            "En conséquence, je ne demande pas de D-dimères : à probabilité élevée, ils ne modifient "
            "aucune décision. Je demande une échographie-doppler veineuse des membres inférieurs en "
            "urgence, et un angioscanner thoracique devant la dyspnée et la tachypnée, car la question "
            "de l'embolie pulmonaire est posée. J'y associe une formule sanguine, une crase et une "
            "créatinine avant anticoagulation.",

            "Mon diagnostic est une thrombose veineuse profonde du membre inférieur gauche, probablement "
            "compliquée d'une embolie pulmonaire, survenue sur un terrain de cancer actif sous "
            "chimiothérapie et déclenchée par un voyage prolongé en position assise.",

            "Je débute une anticoagulation à dose curative sans attendre la confirmation, la probabilité "
            "étant forte. Chez une patiente atteinte d'un cancer actif, le choix de la molécule et la "
            "durée du traitement obéissent à des règles propres. Je prescris une contention veineuse et "
            "je recommande une mobilisation précoce — l'alitement n'est plus recommandé et n'a rien "
            "traité chez elle. J'informe la patiente des signes d'embolie devant la conduire aux "
            "urgences, et je lui donne les mesures de prévention pour ses futurs voyages.",
        ],
        "sbar": {
            "S": "Femme de 68 ans, œdème et douleur de la jambe gauche avec dyspnée d'effort, au retour d'un voyage en car de 16 heures.",
            "B": "Cancer du sein avec récidive ganglionnaire il y a 6 mois, chimiothérapie il y a un mois. Obésité, varices opérées, alitement de 2 jours. Mère décédée d'embolie pulmonaire.",
            "A": "Thrombose veineuse profonde gauche probablement compliquée d'embolie pulmonaire. Score de Wells largement supérieur à 2 : probabilité élevée. Tachypnée à 22/min, dyspnée en parlant, sans douleur thoracique ni hémoptysie.",
            "R": "Doppler veineux en urgence et angioscanner thoracique, sans D-dimères. Anticoagulation curative débutée sans attendre. Contention, mobilisation précoce, information sur les signes d'alerte.",
        },
        "questions": [
            ("Demandez-vous des D-dimères ?",
             "Non. Le score de Wells place cette patiente en probabilité élevée : cancer actif, "
             "immobilisation et voyage, gonflement unilatéral, godet, veines collatérales, et aucun "
             "diagnostic alternatif plus probable. À probabilité élevée, les D-dimères ne permettent "
             "plus d'exclure et ne modifieraient aucune décision. Je vais directement à l'imagerie."),
            ("Pourquoi demandez-vous un angioscanner alors qu'elle n'a pas mal à la poitrine ?",
             "Parce qu'elle est essoufflée en parlant et tachypnéique à 22 par minute, et que ces deux "
             "signes suffisent à poser la question de l'embolie. L'absence de douleur thoracique et "
             "d'hémoptysie n'écarte rien : ces signes manquent dans la majorité des embolies. Devant une "
             "thrombose, chercher la dyspnée revient à chercher l'embolie."),
            ("Quel facteur de risque vous paraît le plus lourd ?",
             "Le cancer actif. Mastectomie il y a quatre ans, mais surtout une récidive locale avec "
             "envahissement ganglionnaire il y a six mois et une chimiothérapie il y a un mois. Un "
             "cancer actif multiplie le risque thromboembolique, et il pèse aussi sur le choix de "
             "l'anticoagulant et sur la durée du traitement, qui obéissent à des règles propres à ce "
             "terrain."),
            ("Attendez-vous l'imagerie pour anticoaguler ?",
             "Non, pas à cette probabilité clinique. Le traitement se débute d'emblée, après avoir "
             "vérifié la formule, la crase et la fonction rénale. Attendre exposerait à une extension "
             "ou à une embolie pendant le délai d'examen, sans bénéfice."),
            ("Que lui dites-vous sur l'alitement, qu'elle a pratiqué deux jours ?",
             "Qu'il ne l'a pas soignée, même s'il l'a momentanément soulagée, et qu'il n'est plus "
             "recommandé : il majore le risque. Je prescris une contention veineuse et je recommande une "
             "mobilisation précoce. Je l'informe aussi des signes qui doivent la conduire aux urgences, "
             "et des mesures de prévention pour ses prochains voyages — se lever régulièrement, "
             "s'hydrater, porter une contention."),
        ],
    },
}
