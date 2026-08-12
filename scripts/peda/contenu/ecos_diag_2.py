# -*- coding: utf-8 -*-
"""Contenu pédagogique — ECOS Diag 2, « L'abdomen aigu aux urgences ».

Dérivé des critères notés de la grille. Aucune source externe.
"""

CONTENU = {
    "grille": "casecos/ECOS Diag 2 - Abdomen Aigu aux Urgences - Grille ECOS.html",
    "titre_resume": "Perforation d'ulcère gastro-duodénal – Résumé ECOS",
    "titre_cas": "Abdomen aigu avec contracture",

    "resume": [
        ("🔍 Anamnèse", [
            ("Le début, qui fait le diagnostic", [
                "Douleur survenue d'un coup il y a 2 heures, décrite comme un coup de couteau",
                "Immédiatement insupportable, cotée 9 sur 10 — pas de crescendo",
                "Débutée vers l'épigastre puis étendue à tout l'abdomen",
                "Un début brutal et d'emblée maximal oriente vers une perforation, une rupture ou une occlusion vasculaire",
            ]),
            ("Les facteurs de risque d'ulcère, tous présents", [
                "Ibuprofène depuis 2 semaines pour des douleurs du dos",
                "Antécédent de brûlures d'estomac, jamais explorées",
                "Tabagisme à un paquet par jour",
                "Ces trois éléments, réunis, transforment une hypothèse en probabilité",
            ]),
            ("Les signes de choc, à chercher explicitement", [
                "Vertiges au lever, soif intense, sueurs froides, sensation de malaise",
                "TA 95/60, FC 110, FR 22 superficielle : le tableau hémodynamique est déjà altéré",
            ]),
            ("Ce qui ne doit jamais être oublié", [
                "Chez une femme en âge de procréer : date des dernières règles, contraception, saignement — une grossesse extra-utérine rompue donne le même tableau",
                "Symptômes digestifs : un vomissement juste après le début, arrêt des gaz, dernier repas il y a 4 heures",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Ce qui se voit avant de toucher", [
                "Respiration exclusivement thoracique, l'abdomen ne bouge pas",
                "Patient immobile, recroquevillé sur le côté — l'immobilité est un signe péritonéal",
            ]),
            ("Les quatre temps, dans l'ordre", [
                "Palpation : contracture généralisée dès l'effleurement, ventre de bois — c'est LE signe",
                "Percussion : disparition de la matité hépatique, signant un pneumopéritoine ; tympanisme diffus",
                "Auscultation : silence auscultatoire, iléus réflexe",
                "La contracture n'est pas une défense : elle est permanente, involontaire, et ne se relâche pas",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Ce qui ne doit pas retarder le bloc", [
                "Le diagnostic est CLINIQUE : contracture plus disparition de la matité hépatique suffisent",
                "Radiographie thoracique debout ou scanner : pneumopéritoine — mais un cliché normal n'écarte rien",
                "Bilan préopératoire : formule, crase, groupe, ionogramme, fonction rénale, lactates",
                "Test de grossesse chez toute femme en âge de procréer, avant l'imagerie",
            ]),
            ("Ce que le scanner apporte quand il est possible", [
                "Localisation de la perforation et cartographie de l'épanchement",
                "Il ne se demande jamais chez un patient instable qu'on ne peut pas surveiller",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Les gestes immédiats, en parallèle", [
                "Deux voies veineuses de bon calibre, remplissage vasculaire",
                "À jeun strict, sonde nasogastrique en aspiration",
                "Antalgie — ne pas la retarder au prétexte de préserver l'examen, le diagnostic est déjà fait",
                "Antibiothérapie couvrant les germes digestifs, inhibiteur de la pompe à protons par voie veineuse",
            ]),
            ("La décision", [
                "Appel chirurgical SANS attendre les résultats : c'est une urgence chirurgicale",
                "Surveillance rapprochée : tension, fréquence, diurèse, conscience",
                "Information du patient et de sa famille sur l'intervention",
                "Le facteur pronostique principal est le délai entre la perforation et la chirurgie",
            ]),
        ]),
    ],

    "points_cles": [
        "Un ventre de bois est une contracture, pas une défense : permanent, involontaire, dès l'effleurement",
        "La disparition de la matité hépatique signe le pneumopéritoine — c'est le geste que tout le monde oublie",
        "Début brutal d'emblée maximal : penser perforation, rupture, occlusion vasculaire",
        "AINS depuis 2 semaines, brûlures d'estomac non explorées, tabac : les trois facteurs sont réunis",
        "Test de grossesse chez toute femme en âge de procréer — une GEU rompue donne le même tableau",
        "L'antalgie ne masque pas le diagnostic quand il est déjà posé : la retarder est une faute",
    ],

    "checklist": [
        ("Questions à poser", [
            "Comment cela a-t-il commencé ? En combien de temps ?",
            "Où avez-vous eu mal en premier ? Où avez-vous mal maintenant ?",
            "Prenez-vous des anti-inflammatoires ? Depuis quand ?",
            "Avez-vous déjà eu des brûlures d'estomac ?",
            "La tête tourne-t-elle quand vous vous levez ? Avez-vous soif ?",
            "Avez-vous vomi ? Émis des gaz depuis ?",
            "Quelle est la date de vos dernières règles ?",
        ]),
        ("Examens à faire", [
            "Inspection : respiration, position antalgique, mobilité abdominale",
            "Palpation douce en dernier, à la recherche d'une contracture",
            "PERCUSSION avec recherche de la matité hépatique",
            "Auscultation, constantes complètes",
        ]),
        ("Prise en charge en 3 points", [
            "Deux voies, remplissage, à jeun, sonde nasogastrique, antalgie",
            "Antibiothérapie digestive et IPP par voie veineuse, bilan préopératoire",
            "Appel chirurgical immédiat, sans attendre l'imagerie",
        ]),
    ],

    "theorie": [
        ("Contracture et défense : deux signes, deux gravités",
         "Le vocabulaire n'est pas interchangeable, et la grille le cote séparément.",
         [
             "La défense est une contraction volontaire, réflexe à la palpation, qui cède à la distraction",
             "La contracture est permanente, involontaire, présente dès l'effleurement et impossible à vaincre",
             "Le « ventre de bois » désigne une contracture généralisée : il signe une péritonite",
             "Dire « défense » devant une contracture, c'est sous-évaluer d'un cran une urgence chirurgicale",
         ]),
        ("La percussion, le temps qu'on saute",
         "Elle apporte ici le signe le plus spécifique du dossier.",
         [
             "La matité hépatique se percute normalement sur la ligne médio-claviculaire droite",
             "Sa disparition traduit l'interposition d'air entre le foie et la paroi : c'est un pneumopéritoine",
             "Le tympanisme diffus complète le tableau",
             "Percuter sans interpréter ne vaut rien : c'est la conclusion énoncée qui compte",
         ]),
        ("Pourquoi le début brutal oriente à lui seul",
         "La cinétique d'installation d'une douleur abdominale est une donnée diagnostique majeure.",
         [
             "Brutal et d'emblée maximal : perforation, rupture d'anévrisme, torsion, embolie mésentérique",
             "Rapidement progressif sur quelques heures : obstruction, colique, inflammation d'organe",
             "Lentement progressif sur des jours : inflammation, infection, tumeur",
             "Ici, « comme un coup de couteau », 9 sur 10 immédiatement : la première catégorie",
         ]),
        ("L'antalgie ne masque pas le diagnostic",
         "L'idée qu'il faudrait attendre l'avis chirurgical pour soulager est un réflexe ancien et faux.",
         [
             "Le diagnostic est ici clinique et déjà posé : contracture et disparition de la matité hépatique",
             "L'antalgie ne fait pas disparaître une contracture, qui est involontaire",
             "Un patient soulagé est un patient qu'on peut examiner et informer",
             "Retarder l'antalgie n'apporte aucune information et ajoute de la souffrance à une urgence",
         ]),
    ],

    "presentation": {
        "checklist_mentale": [
            "Intro : âge, contexte d'urgence, motif, délai",
            "Cinétique de la douleur : début, intensité initiale, migration",
            "Facteurs de risque d'ulcère : AINS, antécédents, tabac",
            "Signes de choc recherchés explicitement",
            "Cause gynécologique écartée chez la femme en âge de procréer",
            "Symptômes digestifs : vomissement, arrêt des gaz, dernier repas",
            "Examen dans l'ordre : inspection, auscultation, percussion, palpation",
            "Constantes et retentissement hémodynamique",
            "Diagnostic, différentiels, et ce qui ne doit pas retarder le bloc",
            "Mesures immédiates et appel chirurgical",
        ],
        "mnemo": ("« Trois signes, un bloc »", [
            "Début en coup de couteau, d'emblée maximal",
            "Ventre de bois dès l'effleurement",
            "Matité hépatique disparue",
            "→ appel chirurgical, sans attendre l'imagerie",
        ]),
        "version_longue": [
            "Il s'agit d'un patient de 35 à 45 ans, qui consulte aux urgences pour une douleur "
            "abdominale sévère apparue soudainement il y a deux heures.",

            "La douleur est survenue d'un coup, décrite comme un coup de couteau dans le ventre, "
            "immédiatement insupportable et cotée 9 sur 10. Elle a commencé au niveau de l'estomac puis "
            "s'est étendue à tout l'abdomen.",

            "L'interrogatoire retrouve trois facteurs de risque d'ulcère réunis : une prise d'ibuprofène "
            "depuis deux semaines pour des douleurs du dos, des brûlures d'estomac anciennes jamais "
            "explorées, et un tabagisme à un paquet par jour.",

            "Il présente des signes d'instabilité : vertiges au lever, soif intense, sueurs froides et "
            "sensation de malaise. Sur le plan digestif, il a vomi une fois juste après le début de la "
            "douleur, n'a plus émis de gaz depuis, et avait mangé quatre heures auparavant. Chez une "
            "patiente, j'ai vérifié la date des dernières règles, la contraception et l'absence de "
            "saignement vaginal.",

            "Les constantes confirment le retentissement : tension à 95/60, fréquence cardiaque à 110, "
            "fréquence respiratoire à 22 et superficielle, température à 37,8 °C, saturation à 97 %, "
            "douleur à 9 sur 10.",

            "À l'inspection, le patient respire uniquement avec le thorax, l'abdomen ne bouge pas ; il "
            "est immobile, recroquevillé sur le côté. À la palpation, dès l'effleurement, je retrouve "
            "une contracture généralisée, un ventre dur comme une planche de bois, avec blocage "
            "respiratoire et grimace. À la percussion, la matité hépatique a disparu, ce qui signe un "
            "pneumopéritoine, avec un tympanisme diffus. À l'auscultation, les bruits hydro-aériques "
            "sont absents, traduisant un iléus réflexe.",

            "Mon diagnostic est une péritonite par perforation d'ulcère gastro-duodénal, très "
            "probablement favorisée par la prise d'anti-inflammatoires. Les différentiels sont une "
            "pancréatite aiguë, une occlusion, une ischémie mésentérique, et chez une femme une "
            "grossesse extra-utérine rompue — que j'ai écartée par l'anamnèse et que je confirmerai par "
            "un test de grossesse.",

            "Le diagnostic est clinique et ne doit pas être retardé par l'imagerie. Je demande "
            "néanmoins une radiographie thoracique debout ou un scanner à la recherche du "
            "pneumopéritoine, en sachant qu'un cliché normal n'écarterait rien, ainsi qu'un bilan "
            "préopératoire complet : formule, crase, groupe, ionogramme, fonction rénale et lactates.",

            "En parallèle, je pose deux voies veineuses de bon calibre et je remplis, je mets le patient "
            "à jeun strict avec une sonde nasogastrique en aspiration, j'administre une antalgie — la "
            "retarder n'apporterait aucune information puisque le diagnostic est posé —, une "
            "antibiothérapie couvrant les germes digestifs et un inhibiteur de la pompe à protons par "
            "voie veineuse.",

            "Enfin, et c'est le point essentiel : j'appelle le chirurgien sans attendre les résultats. "
            "Le facteur pronostique principal d'une perforation est le délai entre la perforation et "
            "l'intervention.",
        ],
        "sbar": {
            "S": "Patient de 35-45 ans, douleur abdominale brutale depuis 2 heures, EVA 9/10.",
            "B": "Ibuprofène depuis 2 semaines, brûlures d'estomac anciennes non explorées, tabagisme à un paquet par jour.",
            "A": "Péritonite par perforation d'ulcère : début en coup de couteau d'emblée maximal, contracture généralisée, disparition de la matité hépatique, silence auscultatoire. TA 95/60, FC 110 — retentissement hémodynamique.",
            "R": "Deux voies et remplissage, à jeun avec sonde nasogastrique, antalgie, antibiothérapie digestive et IPP IV, bilan préopératoire, APPEL CHIRURGICAL immédiat sans attendre l'imagerie.",
        },
        "questions": [
            ("Qu'est-ce qui vous fait poser le diagnostic ?",
             "Trois éléments cliniques, et ils suffisent. Un début brutal d'emblée maximal, décrit comme "
             "un coup de couteau. Une contracture généralisée dès l'effleurement — un ventre de bois, "
             "qui n'est pas une défense mais une contraction permanente et involontaire. Et la "
             "disparition de la matité hépatique à la percussion, qui signe le pneumopéritoine. "
             "L'imagerie confirmera, elle ne décidera pas."),
            ("Quelle différence faites-vous entre défense et contracture ?",
             "La défense est une contraction volontaire, réflexe à la palpation, qui cède à la "
             "distraction. La contracture est permanente, involontaire, présente dès l'effleurement et "
             "impossible à vaincre. Le ventre de bois désigne une contracture généralisée et signe une "
             "péritonite. Dire « défense » ici reviendrait à sous-évaluer d'un cran une urgence "
             "chirurgicale."),
            ("Donnez-vous des antalgiques avant l'avis chirurgical ?",
             "Oui, sans hésiter. L'idée qu'il faudrait attendre pour ne pas masquer l'examen est un "
             "réflexe ancien et faux : le diagnostic est déjà posé, et l'antalgie ne fait pas "
             "disparaître une contracture, qui est involontaire. Un patient soulagé est un patient qu'on "
             "peut examiner et informer. Retarder l'antalgie n'apporte rien et ajoute de la souffrance."),
            ("Attendez-vous le scanner pour appeler le chirurgien ?",
             "Non. Le facteur pronostique principal d'une perforation est le délai entre la perforation "
             "et l'intervention. J'appelle en parallèle des examens, pas après. Et je ne demanderais pas "
             "de scanner chez un patient instable que je ne pourrais pas surveiller pendant l'examen."),
            ("Qu'auriez-vous fait de plus si la patiente était une femme jeune ?",
             "Exactement ce que j'ai fait : demander la date des dernières règles, la contraception et "
             "l'existence d'un saignement, puis réaliser un test de grossesse avant toute imagerie. Une "
             "grossesse extra-utérine rompue donne le même tableau de douleur brutale avec instabilité "
             "hémodynamique, et c'est une urgence chirurgicale d'une autre nature."),
        ],
    },

    "scenario": [
        ("Identité et cadre", [
            ("Patient", "35 à 45 ans, sexe indifférent"),
            ("Lieu", "service des urgences"),
            ("Motif", "douleur abdominale sévère apparue soudainement il y a 2 heures"),
            ("Position initiale", "allongé sur le côté, genoux repliés, immobile"),
        ]),
        ("Jeu de rôle", [
            ("Douleur", "intense en permanence ; grimacer, souffler court"),
            ("Respiration", "thoracique uniquement, superficielle"),
            ("Mobilité", "refuser de bouger ; se plaindre si on veut changer de position"),
            ("À la palpation", "bloquer la respiration et grimacer dès le contact"),
        ]),
        ("Phrases à dire telles quelles", [
            ("Début", "« C'est arrivé d'un coup il y a 2 heures, comme un coup de couteau dans le ventre. »"),
            ("Intensité", "« La douleur était immédiatement insupportable, 9 sur 10. »"),
            ("Migration", "« Ça a commencé vers l'estomac puis ça s'est étendu à tout le ventre. »"),
            ("Malaise", "« J'ai la tête qui tourne quand j'essaie de me lever », « J'ai très soif », « J'ai des sueurs froides »"),
            ("Digestif", "« J'ai vomi une fois juste après le début », « Je n'ai plus eu de gaz depuis »"),
        ]),
        ("Ce qui se donne si on le demande", [
            ("AINS", "« Je prends de l'ibuprofène depuis 2 semaines pour des douleurs au dos. »"),
            ("Antécédent digestif", "« J'ai déjà eu des brûlures d'estomac par le passé mais jamais exploré. »"),
            ("Tabac", "« Je fume un paquet par jour. »"),
            ("Dernier repas", "« J'ai mangé il y a 4 heures. »"),
            ("Gynécologique", "« Mes dernières règles datent d'il y a 3 semaines, elles étaient normales. Je prends la pilule. Pas de saignement vaginal. »"),
        ]),
        ("Inquiétudes et questions", [
            (None, "« Est-ce que vous pouvez me donner quelque chose contre la douleur ? »"),
            (None, "« Est-ce qu'il va falloir m'opérer ? »"),
            (None, "« C'est grave ? »"),
        ]),
    ],
}
