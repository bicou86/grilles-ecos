# -*- coding: utf-8 -*-
"""Contenu pédagogique — RESCOS-11, « Chute ».

Dérivé des critères notés de la grille. Aucune source externe.

C'est la grille la plus courte du chantier — 743 mots visibles, aucun bloc
pédagogique, ni clôture ni diagnostic différentiel. Mais ses critères notés
sont détaillés et suffisent : mécanisme, caractérisation de la douleur, examen
neurovasculaire territoire par territoire, incidences radiologiques, lésions à
identifier, conduite. Le contenu ci-dessous n'ajoute aucun fait clinique
absent de la grille.
"""

CONTENU = {
    "grille": "rescos/RESCOS-11_-_Chute_-_Grille_ECOS.html",
    "titre_resume": "Traumatisme du coude aux urgences – Résumé ECOS",
    "titre_cas": "Traumatisme du coude après chute sur la main",

    "resume": [
        ("🔍 Anamnèse", [
            ("Le mécanisme, qui prédit la lésion", [
                "Chute avec réception bras tendu, coude en extension",
                "Énergie du traumatisme à préciser : faible, moyenne ou haute",
                "Absence d'autres blessures que le coude — à vérifier, pas à supposer",
                "Une réception sur la main coude tendu transmet la force à la tête radiale : c'est le mécanisme classique de sa fracture",
            ]),
            ("Caractériser la douleur", [
                "Localisation au coude gauche, intensité 7 à 8 sur 10",
                "Douleur aiguë et lancinante, constante depuis la chute",
                "Irradiation vers l'avant-bras",
                "Aggravée par le mouvement, soulagée au repos",
            ]),
            ("Ce qui ne doit jamais manquer", [
                "Impotence fonctionnelle : elle ne peut pas mobiliser le coude",
                "Symptômes neurovasculaires : paresthésies, perte de sensibilité, faiblesse distale",
                "Ces questions se posent AVANT l'examen, et elles orientent ce qu'on cherchera",
            ]),
            ("Le terrain et le retentissement", [
                "Aucun antécédent médical ni chirurgical, aucun traitement, aucune allergie",
                "Membre dominant : droitière ou gauchère — cela change tout le retentissement",
                "Activités affectées : travail, loisirs, gestes quotidiens",
                "Chez une femme de 24 ans : la possibilité d'une grossesse se demande avant toute radiographie",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Toujours comparer les deux côtés", [
                "Observation comparative des deux membres supérieurs",
                "Palpation des deux coudes : douleur, déformation, crépitations",
                "Palpation des bras, épaules, avant-bras et poignets, pour écarter les lésions associées",
                "Une lésion du poignet ou de l'épaule passe inaperçue si l'attention reste sur le coude douloureux",
            ]),
            ("La perfusion distale, comparée", [
                "Pouls radial et ulnaire des deux côtés",
                "Temps de recoloration ou gradient thermique",
                "Un déficit vasculaire transforme la consultation en urgence",
            ]),
            ("Les trois nerfs, sensibilité ET motricité", [
                "Radial : sensibilité de la tabatière anatomique, extension du pouce et du poignet",
                "Médian : sensibilité de la pulpe de l'index, opposition du pouce",
                "Ulnaire : sensibilité de la pulpe de l'auriculaire, écartement des doigts",
                "Six tests, trois nerfs, deux fonctions chacun — et chacun se documente avant l'immobilisation",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Avant de demander l'imagerie", [
                "Évaluer le risque de grossesse chez une patiente de 24 ans : c'est un critère noté, et c'est une obligation",
            ]),
            ("La radiographie et sa lecture", [
                "Radiographie du coude gauche, incidences de FACE et de PROFIL — préciser les deux",
                "Rechercher une luxation, une fracture de la tête radiale, une fracture du processus coronoïde",
                "Le scanner se discute pour préciser une fracture articulaire ou devant une radiographie non concluante",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Ce qui se fait aux urgences", [
                "Antalgie, sans attendre le résultat de l'imagerie",
                "Immobilisation par attelle et écharpe",
                "Documentation de l'examen neurovasculaire AVANT immobilisation, et contrôle après",
                "Référence orthopédique",
            ]),
            ("Ce qu'il faut annoncer", [
                "Une prise en charge chirurgicale est possible selon le type et le déplacement de la fracture",
                "Le retentissement fonctionnel dépend du membre dominant et de l'activité",
                "Consignes de surveillance : douleur croissante, doigts froids, pâles, insensibles, ou impossibilité de les bouger",
            ]),
        ]),
    ],

    "points_cles": [
        "Réception bras tendu coude en extension : le mécanisme prédit la fracture de la tête radiale",
        "L'examen neurovasculaire se fait AVANT l'immobilisation et se documente — sinon on ne saura jamais ce que le plâtre a causé",
        "Trois nerfs, deux fonctions chacun : radial, médian, ulnaire, sensibilité et motricité",
        "Toujours comparer les deux côtés, et palper au-dessus et en dessous : l'épaule et le poignet se lèsent aussi",
        "Chez une femme en âge de procréer, évaluer le risque de grossesse avant toute radiographie",
        "Préciser les incidences demandées : face ET profil — une seule incidence manque les fractures",
    ],

    "checklist": [
        ("Questions à poser", [
            "Comment êtes-vous tombée ? Sur quoi avez-vous atterri ?",
            "Le bras était-il tendu ? Le coude plié ou droit ?",
            "De quelle hauteur, à quelle vitesse ?",
            "Vous êtes-vous fait mal ailleurs ?",
            "Pouvez-vous bouger le coude ? Les doigts ?",
            "Avez-vous des fourmillements, une zone insensible, une faiblesse ?",
            "Êtes-vous droitière ou gauchère ?",
            "Y a-t-il une possibilité que vous soyez enceinte ?",
        ]),
        ("Examens à faire", [
            "Observation et palpation comparatives des deux membres, coude, bras, épaule, avant-bras, poignet",
            "Pouls radial et ulnaire, recoloration, gradient thermique, des deux côtés",
            "Sensibilité : tabatière anatomique, pulpe de l'index, pulpe de l'auriculaire",
            "Motricité : extension du pouce et du poignet, opposition du pouce, écartement des doigts",
        ]),
        ("Prise en charge en 3 points", [
            "Antalgie, puis radiographie face et profil après évaluation du risque de grossesse",
            "Immobilisation attelle et écharpe, examen neurovasculaire documenté avant et après",
            "Référence orthopédique, information sur la possibilité d'une chirurgie",
        ]),
    ],

    "theorie": [
        ("Le mécanisme prédit la lésion",
         "En traumatologie, la question « comment êtes-vous tombée ? » vaut un examen.",
         [
             "Réception sur la main, coude en extension : la force remonte l'avant-bras et se concentre sur la tête radiale",
             "C'est le mécanisme le plus fréquent de fracture de la tête radiale chez l'adulte jeune",
             "Une chute sur le coude fléchi transmet différemment et lèse plutôt l'olécrane",
             "L'énergie du traumatisme oriente la recherche de lésions associées : haute énergie impose d'élargir l'examen",
         ]),
        ("L'examen neurovasculaire avant l'immobilisation",
         "C'est le point où une station de traumatologie se gagne ou se perd.",
         [
             "Il se réalise AVANT toute immobilisation et se consigne par écrit",
             "Sans trace initiale, un déficit constaté après le plâtre devient impossible à situer dans le temps",
             "Il se répète APRÈS l'immobilisation, pour vérifier qu'elle n'a rien compromis",
             "Trois nerfs à tester, chacun en sensibilité et en motricité — six gestes qui prennent une minute",
         ]),
        ("Comparer, et ne pas s'arrêter à l'endroit qui fait mal",
         "L'attention se fixe naturellement sur la zone douloureuse ; c'est ainsi que les lésions associées se manquent.",
         [
             "Comparer systématiquement au côté sain, pour l'observation, la palpation et la perfusion",
             "Palper l'articulation sus-jacente et sous-jacente : épaule et poignet",
             "Une fracture du poignet associée est fréquente après une réception sur la main",
             "L'absence d'autres blessures se vérifie, elle ne se déduit pas de ce que dit la patiente",
         ]),
        ("Ce que la radiographie doit montrer, et comment la demander",
         "Une demande imprécise donne une image inexploitable.",
         [
             "Préciser le côté et les incidences : coude gauche, face et profil",
             "Chercher trois choses : luxation, fracture de la tête radiale, fracture du processus coronoïde",
             "Le scanner précise les fractures articulaires et guide la décision chirurgicale",
             "Chez une femme en âge de procréer, l'évaluation du risque de grossesse précède la demande — la grille le cote explicitement",
         ]),
    ],

    "presentation": {
        "checklist_mentale": [
            "Intro : âge, contexte d'urgence, motif, côté",
            "Mécanisme : type de chute, position de réception, énergie",
            "Douleur : localisation, intensité, qualité, irradiation, facteurs",
            "Impotence et symptômes neurovasculaires",
            "Antécédents, traitements, allergies",
            "Latéralité dominante et retentissement",
            "Examen comparatif : observation, palpation étendue, perfusion",
            "Six tests neurologiques : trois nerfs, sensibilité et motricité",
            "Risque de grossesse, puis radiographie face et profil",
            "Antalgie, immobilisation, contrôle neurovasculaire, référence orthopédique",
        ],
        "mnemo": ("« Trois nerfs, deux fois »", [
            "Radial : tabatière anatomique / extension pouce et poignet",
            "Médian : pulpe de l'index / opposition du pouce",
            "Ulnaire : pulpe de l'auriculaire / écartement des doigts",
            "Avant l'attelle, et après l'attelle",
        ]),
        "version_longue": [
            "Il s'agit de Mme Frascarolo, 24 ans, qui se présente aux urgences pour une douleur et une "
            "impotence du membre supérieur gauche à la suite d'une chute.",

            "Le mécanisme est celui d'une chute avec réception bras tendu, coude en extension. Je "
            "précise l'énergie du traumatisme et je vérifie l'absence d'autres blessures.",

            "La douleur siège au coude gauche, cotée 7 à 8 sur 10, de type aigu et lancinant, constante "
            "depuis la chute, irradiant vers l'avant-bras, aggravée par le mouvement et soulagée au "
            "repos. Elle ne peut pas mobiliser le coude.",

            "Je recherche systématiquement des symptômes neurovasculaires : paresthésies, perte de "
            "sensibilité, faiblesse distale.",

            "Elle n'a aucun antécédent médical ni chirurgical, ne prend aucun médicament et n'a aucune "
            "allergie. Je précise sa latéralité dominante et les activités affectées, qui déterminent le "
            "retentissement réel.",

            "À l'examen, je procède par comparaison des deux membres supérieurs : observation, puis "
            "palpation des deux coudes à la recherche d'une douleur, d'une déformation ou de "
            "crépitations, et palpation des bras, épaules, avant-bras et poignets pour écarter des "
            "lésions associées — une réception sur la main lèse fréquemment le poignet.",

            "J'évalue la perfusion distale des deux côtés : pouls radial et ulnaire, temps de "
            "recoloration et gradient thermique.",

            "Puis je teste les trois nerfs, en sensibilité et en motricité. Le radial : sensibilité de "
            "la tabatière anatomique et extension du pouce et du poignet. Le médian : sensibilité de la "
            "pulpe de l'index et opposition du pouce. L'ulnaire : sensibilité de la pulpe de "
            "l'auriculaire et écartement des doigts. Cet examen est réalisé et documenté AVANT toute "
            "immobilisation, et je le répéterai après.",

            "Avant de demander l'imagerie, j'évalue le risque de grossesse chez cette patiente de "
            "24 ans. Je demande ensuite une radiographie du coude gauche, de face et de profil, à la "
            "recherche d'une luxation, d'une fracture de la tête radiale et d'une fracture du processus "
            "coronoïde. Un scanner se discutera pour préciser une fracture articulaire ou devant une "
            "radiographie non concluante.",

            "Pour la prise en charge, je propose une antalgie sans attendre l'imagerie, une "
            "immobilisation par attelle et écharpe avec contrôle neurovasculaire après la pose, et une "
            "référence orthopédique. J'annonce à la patiente qu'une prise en charge chirurgicale est "
            "possible selon le type de fracture et son déplacement, et je lui donne les consignes de "
            "surveillance : douleur croissante, doigts froids, pâles, insensibles, ou impossibles à "
            "bouger.",
        ],
        "sbar": {
            "S": "Mme Frascarolo, 24 ans, douleur et impotence du membre supérieur gauche après une chute, aux urgences.",
            "B": "Aucun antécédent, aucun traitement, aucune allergie. Réception bras tendu, coude en extension.",
            "A": "Traumatisme du coude gauche avec impotence fonctionnelle, douleur 7-8/10 irradiant à l'avant-bras. Examen neurovasculaire à documenter. Suspicion de fracture de la tête radiale au vu du mécanisme.",
            "R": "Antalgie, évaluation du risque de grossesse puis radiographie face et profil, immobilisation attelle et écharpe avec contrôle neurovasculaire, référence orthopédique.",
        },
        "questions": [
            ("Qu'attendez-vous du mécanisme de la chute ?",
             "Il prédit la lésion. Une réception sur la main, coude en extension, transmet la force le "
             "long de l'avant-bras et la concentre sur la tête radiale : c'est le mécanisme le plus "
             "fréquent de sa fracture chez l'adulte jeune. Une chute sur le coude fléchi léserait plutôt "
             "l'olécrane. L'énergie du traumatisme, elle, détermine jusqu'où j'élargis l'examen."),
            ("Quand faites-vous l'examen neurovasculaire ?",
             "Avant l'immobilisation, et je le consigne. C'est le point décisif : sans trace initiale, "
             "un déficit constaté après la pose de l'attelle devient impossible à situer dans le temps. "
             "Je le répète après l'immobilisation pour vérifier qu'elle n'a rien compromis. Trois nerfs, "
             "sensibilité et motricité pour chacun — six gestes, une minute."),
            ("Que palpez-vous en dehors du coude ?",
             "L'épaule, le bras, l'avant-bras et le poignet, des deux côtés. L'attention se fixe "
             "naturellement sur la zone douloureuse, et c'est ainsi qu'on manque les lésions associées. "
             "Après une réception sur la main, une fracture du poignet est fréquente. L'absence "
             "d'autres blessures se vérifie, elle ne se déduit pas."),
            ("Comment formulez-vous votre demande de radiographie ?",
             "En précisant le côté et les incidences : coude gauche, face et profil. Une seule "
             "incidence manque des fractures. Et je précise ce que je cherche : luxation, fracture de la "
             "tête radiale, fracture du processus coronoïde. Un scanner se discutera pour préciser une "
             "fracture articulaire ou si la radiographie n'est pas concluante."),
            ("Quelque chose précède la radiographie chez cette patiente ?",
             "Oui, l'évaluation du risque de grossesse. Elle a 24 ans, et la grille cote ce point "
             "explicitement. C'est une obligation avant toute exposition radiologique chez une femme en "
             "âge de procréer."),
        ],
    },
}
