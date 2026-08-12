# -*- coding: utf-8 -*-
"""Contenu pédagogique — ECOS Diag 1, « Le laborantin au dos douloureux ».

Dérivé des critères notés de la grille. Aucune source externe.
Grille du corpus casecos : `resume` et `presentation` y sont deux blocs
nouvellement déclarés dans `lib_casecos.BLOCKS`.
"""

CONTENU = {
    "grille": "casecos/ECOS Diag 1 - Dos douloureux - Grille ECOS.html",
    "titre_resume": "Spondyloarthrite axiale – Résumé ECOS",
    "titre_cas": "Lombalgie inflammatoire du sujet jeune",

    "resume": [
        ("🔍 Anamnèse", [
            ("Le rythme de la douleur, qui fait tout le diagnostic", [
                "Réveil vers 4 h du matin à cause de la douleur, obligeant à se lever et à marcher",
                "Raideur matinale, améliorée par la douche chaude et par le mouvement",
                "Début progressif il y a environ 2 mois, chez un homme de 30 ans",
                "Ce rythme est l'inverse de celui d'une lombalgie commune : c'est lui qui doit alerter",
            ]),
            ("Les signes extra-axiaux à chercher activement", [
                "Enthésite : douleur du talon droit, surtout au réveil quand le pied se pose",
                "Dactylite, arthrite périphérique, à demander même si le patient n'en parle pas",
            ]),
            ("Les antécédents évocateurs", [
                "Épisode d'œil rouge très douloureux avec vision floue il y a 2 ans, qualifié d'inflammation par l'ophtalmologue — c'est une uvéite antérieure",
                "Oncle paternel atteint d'une maladie rhumatismale du dos",
                "À chercher aussi : psoriasis, maladie inflammatoire de l'intestin, infection urinaire ou digestive précédant les symptômes",
            ]),
            ("Les red flags, à écarter explicitement", [
                "Pas de faiblesse des jambes, pas de paresthésies",
                "Pas de trouble sphinctérien urinaire ni fécal",
                "Pas de fièvre, poids stable",
                "Les anti-inflammatoires soulagent bien — cette réponse est en elle-même un argument",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Les manœuvres qui comptent", [
                "Test de Schober : la distance passe de 10 à 13 cm, soit un gain de 3 cm quand la norme est d'au moins 5 — mobilité lombaire diminuée",
                "Test de Patrick et pression directe sur la sacro-iliaque : douleur reproduite à droite",
                "Mobilité rachidienne globalement limitée",
            ]),
            ("Ce qui doit être normal, et qui l'est", [
                "Examen neurologique des membres inférieurs strictement normal : réflexes symétriques, force 5/5, sensibilité conservée",
                "Lasègue négatif des deux côtés",
                "Cette normalité écarte la radiculopathie et confirme qu'on est sur un tableau axial inflammatoire",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Biologie", [
                "CRP et vitesse de sédimentation : souvent élevées, mais leur normalité n'écarte rien",
                "HLA-B27 : fortement associé, mais ce n'est ni un test diagnostique ni un test d'exclusion",
                "Le diagnostic reste clinique et radiologique",
            ]),
            ("Imagerie", [
                "Radiographie du bassin de face, à la recherche d'une sacro-iliite",
                "IRM des sacro-iliaques si la radiographie est normale : elle montre l'œdème osseux avant les lésions structurales",
                "C'est ce qui permet de diagnostiquer une forme non radiographique, fréquente chez le sujet jeune",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Première ligne", [
                "Anti-inflammatoires non stéroïdiens, en continu et à dose efficace",
                "Kinésithérapie et exercices d'assouplissement quotidiens : ce n'est pas un complément, c'est un traitement",
                "Maintien de l'activité physique — le repos aggrave l'enraidissement",
            ]),
            ("Ensuite", [
                "En cas d'échec, biothérapie après avis rhumatologique",
                "Suivi de la mobilité rachidienne, mesurée et notée",
                "Dépistage des atteintes associées : uvéite, psoriasis, maladie inflammatoire de l'intestin",
                "Sevrage tabagique s'il y a lieu : il aggrave l'évolution structurale",
            ]),
        ]),
    ],

    "points_cles": [
        "Réveil nocturne en deuxième partie de nuit et amélioration par le mouvement : c'est l'inverse de la lombalgie commune",
        "Une raideur matinale de plus de 30 minutes chez un adulte jeune impose de penser inflammatoire",
        "L'uvéite antérieure il y a 2 ans n'était pas un épisode isolé : c'est une manifestation extra-articulaire",
        "Un examen neurologique normal et un Lasègue négatif écartent la radiculopathie et confirment le tableau axial",
        "Une radiographie normale n'écarte pas le diagnostic : l'IRM des sacro-iliaques montre l'œdème avant les lésions",
        "HLA-B27 n'est ni un test diagnostique ni un test d'exclusion",
    ],

    "checklist": [
        ("Questions à poser", [
            "À quel moment de la nuit la douleur vous réveille-t-elle ?",
            "Devez-vous vous lever ? Qu'est-ce qui vous soulage ?",
            "Combien de temps dure la raideur du matin ?",
            "Avez-vous mal aux talons, aux fesses, à d'autres articulations ?",
            "Avez-vous déjà eu un œil rouge et douloureux ?",
            "Du psoriasis ? Des troubles digestifs chroniques ?",
            "Quelqu'un dans la famille a-t-il une maladie du dos ?",
            "Faiblesse, fourmillements, troubles pour uriner, fièvre, perte de poids ?",
        ]),
        ("Examens à faire", [
            "Test de Schober avec interprétation chiffrée",
            "Test de Patrick et pression directe des sacro-iliaques",
            "Examen neurologique complet des membres inférieurs, Lasègue",
            "Mobilité rachidienne dans les trois plans, recherche d'enthésites",
        ]),
        ("Prise en charge en 3 points", [
            "AINS en continu à dose efficace",
            "Kinésithérapie et exercices quotidiens, maintien de l'activité",
            "Radiographie du bassin puis IRM des sacro-iliaques si besoin, avis rhumatologique",
        ]),
    ],

    "theorie": [
        ("Inflammatoire ou mécanique : cinq questions suffisent",
         "La distinction se fait à l'interrogatoire, avant tout examen.",
         [
             "Âge de début avant 40 ans, installation progressive",
             "Réveil en deuxième partie de nuit, obligeant à se lever",
             "Raideur matinale prolongée, au-delà de 30 minutes",
             "Amélioration par l'exercice, PAS par le repos",
             "Réponse franche aux anti-inflammatoires",
             "Ce patient réunit les cinq : c'est un tableau inflammatoire typique",
         ]),
        ("Ce que l'uvéite d'il y a deux ans voulait dire",
         "Un œil rouge douloureux avec vision floue, qualifié d'inflammation, est une uvéite antérieure.",
         [
             "Elle est la manifestation extra-articulaire la plus fréquente des spondyloarthrites",
             "Elle précède souvent le diagnostic rhumatologique de plusieurs années",
             "L'interroger explicitement fait partie de l'anamnèse : le patient ne fait pas le lien",
             "Sa récidive impose un avis ophtalmologique en urgence, ce qui doit être dit au patient",
         ]),
        ("Le test de Schober, et comment ne pas le rater",
         "Il mesure la mobilité en flexion du rachis lombaire.",
         [
             "Repère au niveau de L5, puis 10 cm au-dessus ; on mesure l'écart en flexion maximale",
             "Normalement la distance passe de 10 à au moins 15 cm, soit un gain d'au moins 5 cm",
             "Ici elle passe à 13 cm : le gain n'est que de 3 cm, la mobilité est diminuée",
             "Réaliser le test sans en énoncer l'interprétation ne vaut que la moitié des points — et cliniquement, rien",
         ]),
        ("Pourquoi l'IRM change le diagnostic chez le sujet jeune",
         "Les lésions visibles à la radiographie mettent des années à apparaître.",
         [
             "Une sacro-iliite radiographique traduit une atteinte structurale déjà installée",
             "L'IRM montre l'œdème osseux, qui est le signe précoce et réversible",
             "C'est ce qui permet de reconnaître les formes non radiographiques, majoritaires chez l'adulte jeune",
             "Attendre l'apparition des signes radiographiques revient à diagnostiquer avec plusieurs années de retard",
         ]),
    ],

    "presentation": {
        "checklist_mentale": [
            "Intro : âge, profession, motif, durée",
            "Rythme de la douleur : horaire nocturne, raideur matinale, ce qui soulage",
            "Signes extra-axiaux : enthésites, arthrites périphériques, dactylite",
            "Antécédents évocateurs : uvéite, psoriasis, intestin, famille",
            "Red flags écartés un par un",
            "Examen : Schober chiffré, sacro-iliaques, neurologique, mobilité",
            "Synthèse : tableau axial inflammatoire du sujet jeune",
            "Diagnostic, différentiels et ce qui les écarte",
            "Biologie et imagerie, avec le rôle de l'IRM",
            "AINS, kinésithérapie, avis rhumatologique",
        ],
        "mnemo": ("« La douleur qui réveille et que le mouvement calme »", [
            "Mécanique : mal le soir, soulagée par le repos",
            "Inflammatoire : mal la nuit, soulagée par le mouvement",
            "Raideur matinale longue : inflammatoire",
            "Moins de 40 ans, début progressif : inflammatoire",
        ]),
        "version_longue": [
            "Il s'agit de M. Martin, 30 ans, laborantin, qui consulte pour des douleurs du bas du dos "
            "évoluant depuis environ deux mois, d'installation progressive.",

            "Le rythme de la douleur est caractéristique : elle le réveille vers 4 h du matin et "
            "l'oblige à se lever et à marcher pour qu'elle passe. Il décrit une raideur matinale, "
            "améliorée par la douche chaude et par le mouvement. Les anti-inflammatoires de type "
            "ibuprofène le soulagent bien. Il dort mal du fait des réveils nocturnes.",

            "À la recherche de signes extra-axiaux, il rapporte des douleurs du talon droit, surtout le "
            "matin au réveil lorsqu'il pose le pied — ce qui correspond à une enthésite.",

            "Dans ses antécédents, un épisode d'œil rouge très douloureux avec vision floue il y a deux "
            "ans, que l'ophtalmologue avait qualifié d'inflammation : il s'agissait très probablement "
            "d'une uvéite antérieure. Son oncle paternel est atteint d'une maladie rhumatismale du dos.",

            "J'ai écarté les signaux d'alarme : pas de faiblesse des membres inférieurs, pas de "
            "paresthésies, pas de trouble sphinctérien urinaire ou fécal, pas de fièvre, poids stable.",

            "À l'examen, le test de Schober montre une distance passant de 10 à 13 cm, soit un gain de "
            "3 cm alors que la norme est d'au moins 5 : la mobilité lombaire est diminuée. Le test de "
            "Patrick et la pression directe sur l'articulation sacro-iliaque reproduisent la douleur à "
            "droite. La mobilité rachidienne est globalement limitée. L'examen neurologique des membres "
            "inférieurs est strictement normal — réflexes symétriques et présents, force 5/5 "
            "bilatérale, sensibilité conservée — et le Lasègue est négatif des deux côtés.",

            "En synthèse, il s'agit d'un homme jeune présentant une lombalgie de rythme inflammatoire "
            "évoluant depuis deux mois, avec enthésite du talon, antécédent d'uvéite antérieure, "
            "antécédent familial de rhumatisme axial, mobilité lombaire diminuée et douleur "
            "sacro-iliaque reproduite. Mon hypothèse est une spondyloarthrite axiale.",

            "Les différentiels sont une lombalgie commune, écartée par le rythme nocturne et "
            "l'amélioration par le mouvement ; une hernie discale, écartée par l'examen neurologique "
            "normal et le Lasègue négatif ; et une cause infectieuse ou tumorale, écartée par l'absence "
            "de fièvre, la stabilité pondérale et l'évolution.",

            "Je demande une CRP et une vitesse de sédimentation, en sachant que leur normalité "
            "n'écarterait rien, ainsi qu'un HLA-B27, qui est fortement associé mais qui n'est ni un test "
            "diagnostique ni un test d'exclusion. Pour l'imagerie, une radiographie du bassin de face à "
            "la recherche d'une sacro-iliite, et une IRM des sacro-iliaques si elle est normale : chez "
            "un homme de 30 ans, la forme non radiographique est la plus fréquente, et l'IRM montre "
            "l'œdème osseux avant les lésions structurales.",

            "Pour la prise en charge, je propose des anti-inflammatoires non stéroïdiens en continu et à "
            "dose efficace, une kinésithérapie avec exercices d'assouplissement quotidiens, et le "
            "maintien de l'activité physique — le repos aggraverait l'enraidissement. J'oriente vers un "
            "rhumatologue, qui discutera une biothérapie en cas d'échec. Je préviens le patient qu'une "
            "récidive d'œil rouge douloureux impose une consultation ophtalmologique en urgence, et je "
            "dépiste les atteintes associées : psoriasis, maladie inflammatoire de l'intestin.",
        ],
        "sbar": {
            "S": "M. Martin, 30 ans, laborantin, lombalgie basse depuis 2 mois.",
            "B": "Uvéite antérieure il y a 2 ans, oncle paternel avec rhumatisme axial. Bonne réponse aux AINS.",
            "A": "Spondyloarthrite axiale : rythme inflammatoire avec réveil à 4 h et amélioration par le mouvement, enthésite du talon, Schober à 3 cm de gain, douleur sacro-iliaque reproduite, examen neurologique normal.",
            "R": "CRP, VS, HLA-B27, radiographie du bassin puis IRM des sacro-iliaques. AINS en continu, kinésithérapie, avis rhumatologique, information sur l'uvéite.",
        },
        "questions": [
            ("Qu'est-ce qui vous fait dire inflammatoire plutôt que mécanique ?",
             "Cinq éléments, tous présents : un début avant 40 ans et progressif, un réveil en deuxième "
             "partie de nuit qui l'oblige à se lever, une raideur matinale prolongée, une amélioration "
             "par le mouvement et non par le repos, et une réponse franche aux anti-inflammatoires. "
             "C'est l'exact inverse du profil d'une lombalgie commune."),
            ("Que retenez-vous de l'épisode oculaire d'il y a deux ans ?",
             "Qu'il s'agissait très probablement d'une uvéite antérieure, et que ce n'était pas un "
             "événement isolé : c'est la manifestation extra-articulaire la plus fréquente des "
             "spondyloarthrites, et elle précède souvent le diagnostic rhumatologique de plusieurs "
             "années. Le patient ne fait pas le lien spontanément — c'est à nous de poser la question."),
            ("Le test de Schober est à 13 cm. Qu'en concluez-vous ?",
             "Que la mobilité lombaire en flexion est diminuée. La distance doit passer de 10 à au moins "
             "15 cm, soit un gain d'au moins 5 cm ; ici le gain n'est que de 3. Et je précise que "
             "réaliser le test sans énoncer son interprétation ne sert à rien : c'est le chiffre "
             "rapporté à la norme qui constitue l'information."),
            ("La radiographie du bassin est normale. Que faites-vous ?",
             "Une IRM des sacro-iliaques. Une radiographie normale n'écarte pas le diagnostic : les "
             "lésions structurales mettent des années à apparaître, alors que l'IRM montre l'œdème "
             "osseux, qui est le signe précoce. Chez un homme de 30 ans, la forme non radiographique "
             "est la plus fréquente — attendre les signes radiographiques reviendrait à diagnostiquer "
             "avec plusieurs années de retard."),
            ("Que vaut le HLA-B27 dans votre raisonnement ?",
             "C'est un argument, pas une preuve. Il est fortement associé aux spondyloarthrites, mais il "
             "est présent chez une part non négligeable de la population générale, et son absence "
             "n'écarte pas le diagnostic. Je le demande pour compléter le faisceau, jamais pour trancher "
             "à lui seul."),
        ],
    },

    "scenario": [
        ("Identité et cadre", [
            ("Nom", "M. Martin"),
            ("Âge", "30 ans"),
            ("Profession", "laborantin"),
            ("Motif", "douleurs du bas du dos depuis 2 mois"),
            ("Position initiale", "assis, se relève et s'étire une fois pendant l'entretien"),
        ]),
        ("Jeu de rôle", [
            ("État", "gêné par la douleur, fatigué par les réveils nocturnes"),
            ("Attitude", "coopérant, un peu inquiet de « ne pas être pris au sérieux »"),
            ("Spontanéité", "ne pas mentionner le talon ni l'œil sans qu'on le demande"),
        ]),
        ("Phrases à dire telles quelles", [
            ("Rythme", "« Je me réveille vers 4 h du matin à cause de la douleur, je dois me lever et marcher pour que ça passe. »"),
            ("Raideur", "« Je suis plus raide le matin, ça va mieux après la douche chaude et en bougeant. »"),
            ("Début", "« Ça a commencé progressivement il y a environ 2 mois. »"),
            ("AINS", "« Les anti-douleurs type ibuprofène soulagent bien quand j'en prends. »"),
            ("Sommeil", "« Je dors mal à cause des réveils nocturnes. »"),
        ]),
        ("Ce qui se donne si on le demande", [
            ("Talon", "« Oui, j'ai parfois mal au talon droit, surtout le matin au réveil quand je pose le pied par terre. »"),
            ("Œil", "« Il y a 2 ans, j'ai eu un épisode d'œil rouge très douloureux avec vision floue, l'ophtalmologue a parlé d'inflammation. »"),
            ("Famille", "« Mon oncle paternel a une maladie rhumatismale du dos. »"),
            ("Red flags", "« Non, pas de faiblesse dans les jambes, pas de fourmillements, pas de problème pour uriner ou aller à la selle, pas de fièvre, poids stable. »"),
            ("Psoriasis", "non"),
            ("Digestif", "pas de diarrhées chroniques ni de sang dans les selles"),
        ]),
        ("Inquiétudes et questions", [
            (None, "« Est-ce que je vais finir plié en deux comme mon oncle ? »"),
            (None, "« Est-ce que je peux continuer le sport ? »"),
            (None, "« Est-ce que c'est à cause de mon travail ? »"),
        ]),
    ],
}
