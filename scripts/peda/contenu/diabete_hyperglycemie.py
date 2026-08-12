# -*- coding: utf-8 -*-
"""Contenu pédagogique — « Diabète, patient avec hyperglycémie nouvelle ».

Dérivé des critères notés, du bloc `annexe-dd` et du bloc `cloture` de la grille.
Aucune source externe. Écrire en TEXTE BRUT : le balisage est posé à l'injection.
"""

CONTENU = {
    "grille": "rescos-locales/Diabète - Patient avec hyperglycémie nouvelle - Grille ECOS.html",
    "titre_resume": "Diabète de type 2 de découverte récente – Résumé ECOS",
    "titre_cas": "Diabète de type 2 de découverte récente",

    "resume": [
        ("🔍 Anamnèse", [
            ("Les circonstances de découverte", [
                "Bilan de santé annuel en entreprise, il y a deux semaines",
                "Glycémie à jeun de 1,8 g/L, confirmée à 1,9 g/L — deux valeurs au-delà du seuil suffisent au diagnostic",
                "Découverte présentée comme fortuite : le patient dit n'avoir eu aucun symptôme",
            ]),
            ("Les symptômes cardinaux, qui étaient là", [
                "Polyurie : il se lève 2 à 3 fois par nuit depuis 3 mois",
                "Polydipsie : 3 à 4 litres par jour",
                "Amaigrissement : 4 kg en 6 mois sans régime",
                "Pas de polyphagie, appétit normal",
                "Le patient les avait banalisés — c'est l'interrogatoire qui les fait apparaître, pas le patient qui les apporte",
            ]),
            ("Les complications déjà présentes à la découverte", [
                "Vision parfois floue — l'atteinte rétinienne se cherche d'emblée dans le type 2",
                "Fourmillements des pieds le soir : neuropathie débutante probable",
                "Mycose génitale il y a 2 mois : c'est une infection révélatrice classique",
                "Ni douleur thoracique, ni dyspnée d'effort, ni claudication",
            ]),
            ("Le risque cardiovasculaire global, qui fait le pronostic", [
                "Hypertension connue depuis 5 ans, traitée par amlodipine 5 mg",
                "Dyslipidémie limite, non traitée",
                "Ex-fumeur à 20 paquets-années, arrêt il y a 3 ans",
                "Sédentarité, stress professionnel important",
                "IMC 31 kg/m², tour de taille 108 cm : obésité abdominale",
                "Mère diabétique, père décédé d'infarctus à 65 ans, frère hypertendu, sœur obèse",
            ]),
            ("Le mode de vie, qui est le premier levier", [
                "Repas irréguliers, restauration rapide fréquente",
                "2 à 3 sodas par jour, 2 à 3 verres de vin par jour",
                "Activité physique limitée à 10 minutes de marche",
                "6 heures de sommeil et ronflements : penser au syndrome d'apnées du sommeil",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Ce qui se mesure", [
                "Surpoids abdominal visible, IMC 31, tour de taille 108 cm",
                "Tension artérielle 145/92 mmHg — au-dessus de la cible, sous traitement",
                "Fréquence cardiaque 78/min régulière, hydratation et coloration normales",
            ]),
            ("Ce qu'il faut chercher activement", [
                "Pouls périphériques aux quatre membres et recherche de souffles vasculaires",
                "Examen des pieds : sensibilité au monofilament, réflexes, état cutané, points d'appui, espaces interdigitaux",
                "Recherche d'acanthosis nigricans, marqueur d'insulinorésistance",
                "L'examen des pieds ne s'improvise pas à la première complication : il commence à la découverte",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Confirmer et graduer", [
                "Le diagnostic est déjà porté : deux glycémies à jeun au-delà du seuil",
                "HbA1c pour connaître l'exposition des trois derniers mois et fixer une cible",
                "Distinguer type 1 et type 2 : ici l'âge, l'IMC, l'hérédité et l'installation progressive plaident pour un type 2",
            ]),
            ("Le bilan des complications, dès la découverte", [
                "Rein : créatinine avec débit de filtration estimé, et rapport albuminurie/créatininurie",
                "Œil : fond d'œil ou rétinographie — dans le type 2, la rétinopathie peut précéder le diagnostic",
                "Cœur : ECG de repos, bilan lipidique complet",
                "Pieds : gradation du risque podologique",
                "Foie : transaminases, la stéatose est fréquente sur ce terrain",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Les mesures qui viennent en premier", [
                "Alimentation : supprimer les sodas est le geste au meilleur rapport effort/bénéfice",
                "Réduction de l'alcool : 2 à 3 verres par jour apportent des calories et compliquent le contrôle",
                "Activité physique progressive, à négocier en minutes par semaine, pas en principe",
                "Perte de poids de 5 à 10 % : objectif réaliste, bénéfice démontré",
            ]),
            ("Le traitement médicamenteux", [
                "Metformine en première intention, sauf contre-indication, introduite progressivement",
                "Le choix des associations tient compte du risque cardiovasculaire et rénal, élevé ici",
                "Optimiser l'antihypertenseur : 145/92 sous amlodipine n'est pas à la cible",
                "Statine à discuter selon le risque cardiovasculaire global, qui est majeur chez ce patient",
            ]),
            ("Ce qui structure le suivi", [
                "HbA1c tous les 3 mois jusqu'à l'objectif, puis tous les 6 mois",
                "Fond d'œil et bilan rénal annuels, examen des pieds à chaque consultation",
                "Éducation thérapeutique et vaccinations à jour",
                "Rechercher un syndrome d'apnées du sommeil : ronflements, 6 h de sommeil, obésité abdominale",
            ]),
        ]),
    ],

    "points_cles": [
        "« Découverte fortuite » est presque toujours faux : les symptômes cardinaux existaient depuis 3 mois et avaient été banalisés",
        "Dans le type 2, les complications peuvent précéder le diagnostic — le bilan se fait à la découverte, pas un an après",
        "Une mycose génitale chez un homme de 52 ans doit faire doser la glycémie",
        "Ce patient a six facteurs de risque cardiovasculaire en plus du diabète : c'est le risque global qu'on traite, pas seulement le sucre",
        "Supprimer 2 à 3 sodas par jour est la mesure au meilleur rapport effort/bénéfice de toute la consultation",
        "Ronflements, 6 h de sommeil et obésité abdominale : chercher un syndrome d'apnées du sommeil",
    ],

    "checklist": [
        ("Questions à poser", [
            "Vous levez-vous la nuit pour uriner ? Combien de fois, depuis quand ?",
            "Combien buvez-vous par jour ?",
            "Avez-vous perdu du poids sans le vouloir ?",
            "Votre vue est-elle parfois floue ? Avez-vous des fourmillements aux pieds ?",
            "Avez-vous eu des infections à répétition, une mycose ?",
            "Que mangez-vous, que buvez-vous — sodas, alcool ?",
            "Ronflez-vous ? Combien d'heures dormez-vous ?",
            "Qui est diabétique ou cardiaque dans votre famille ?",
        ]),
        ("Examens à faire", [
            "Poids, taille, IMC, tour de taille, tension artérielle",
            "Pouls périphériques, auscultation des trajets vasculaires",
            "Examen COMPLET des pieds : monofilament, réflexes, peau, points d'appui",
            "HbA1c, créatinine et débit de filtration, rapport albuminurie/créatininurie, bilan lipidique, transaminases, ECG, fond d'œil",
        ]),
        ("Prise en charge en 3 points", [
            "Mesures hygiéno-diététiques ciblées : sodas d'abord, puis alcool et activité physique",
            "Metformine en première intention, optimisation de l'antihypertenseur, statine selon le risque",
            "Bilan de complications à la découverte, éducation thérapeutique, suivi structuré",
        ]),
    ],

    "theorie": [
        ("La découverte n'est jamais aussi fortuite qu'on le dit",
         "Ce patient affirme n'avoir eu aucun symptôme avant le bilan. L'interrogatoire dirigé en "
         "retrouve trois.",
         [
             "Polyurie depuis trois mois, polydipsie à 3-4 litres, perte de 4 kg en six mois",
             "Chacun avait été attribué à autre chose : le travail, la chaleur, le stress",
             "La leçon est méthodologique : les symptômes cardinaux se demandent un par un, ils ne se rapportent pas spontanément",
             "Reconstituer cette chronologie permet aussi d'estimer depuis quand l'hyperglycémie évolue",
         ]),
        ("Pourquoi le bilan de complications se fait à la découverte",
         "Le diabète de type 2 évolue silencieusement pendant des années avant d'être diagnostiqué.",
         [
             "Une rétinopathie peut donc être présente le jour du diagnostic : le fond d'œil ne s'attend pas",
             "La néphropathie débute par une albuminurie, indolore et invisible sans dosage",
             "La neuropathie est déjà suggérée ici par les paresthésies des pieds",
             "Une infection révélatrice — la mycose génitale d'il y a deux mois — signale souvent une hyperglycémie ancienne",
         ]),
        ("Traiter le risque, pas seulement la glycémie",
         "Ce patient cumule les facteurs, et ce sont eux qui déterminent son pronostic.",
         [
             "Hypertension mal contrôlée à 145/92 sous amlodipine, dyslipidémie non traitée, tabagisme sevré à 20 paquets-années",
             "Obésité abdominale avec un tour de taille à 108 cm, sédentarité, antécédent d'infarctus paternel précoce",
             "La réduction du risque cardiovasculaire passe autant par la tension et les lipides que par la glycémie",
             "Un contrôle glycémique isolé, sans agir sur le reste, ne modifie pas l'essentiel du pronostic",
         ]),
        ("Négocier plutôt que prescrire un mode de vie",
         "Les conseils hygiéno-diététiques échouent quand ils sont énoncés comme une liste.",
         [
             "Deux à trois sodas par jour représentent un apport considérable et supprimable en une décision",
             "L'alcool à 2-3 verres quotidiens apporte des calories et complique le contrôle : le dire sans moraliser",
             "L'activité physique se négocie en minutes par semaine et en trajets réels, pas en recommandations générales",
             "Un objectif de perte de 5 à 10 % du poids est atteignable et suffisant pour un bénéfice mesurable",
         ]),
    ],

    "presentation": {
        "checklist_mentale": [
            "Intro : âge, circonstances de découverte, valeurs et délai",
            "Symptômes cardinaux, demandés un par un",
            "Complications déjà présentes : œil, pieds, infections, cœur, artères",
            "Facteurs de risque cardiovasculaire, tous",
            "Antécédents familiaux",
            "Mode de vie : alimentation, sodas, alcool, activité, sommeil et ronflements",
            "Traitement actuel, observance, allergies",
            "Anthropométrie : poids, IMC, tour de taille",
            "Examen : tension, pouls, pieds, peau",
            "Bilan de complications à la découverte, puis traitement et suivi structuré",
        ],
        "mnemo": ("Les trois « P » et ce qu'ils cachent", [
            "Polyurie : il se lève la nuit depuis 3 mois",
            "Polydipsie : 3 à 4 litres par jour",
            "Perte de poids : 4 kg en 6 mois",
            "Le patient dit « aucun symptôme » — c'est l'interrogatoire qui les fait apparaître",
        ]),
        "version_longue": [
            "Il s'agit d'un homme de 52 ans, adressé par son médecin traitant pour une hyperglycémie "
            "découverte lors d'un bilan de santé en entreprise il y a deux semaines : glycémie à jeun à "
            "1,8 g/L, confirmée à 1,9 g/L.",

            "Il présente la découverte comme fortuite, mais l'interrogatoire dirigé retrouve trois "
            "symptômes cardinaux : une polyurie avec deux à trois levers nocturnes depuis trois mois, "
            "une polydipsie à 3 ou 4 litres par jour, et une perte de 4 kg en six mois sans régime. Il "
            "n'a pas de polyphagie.",

            "Certaines complications sont déjà présentes : une vision parfois floue, des fourmillements "
            "des pieds le soir, et une mycose génitale il y a deux mois. Il n'a ni douleur thoracique, "
            "ni dyspnée d'effort, ni claudication.",

            "Son risque cardiovasculaire est élevé : hypertension connue depuis cinq ans traitée par "
            "amlodipine 5 mg, dyslipidémie limite non traitée, ex-tabagisme à 20 paquets-années sevré "
            "depuis trois ans, sédentarité avec un travail de bureau, et un stress professionnel "
            "important. Sa mère est diabétique de type 2, son père est décédé d'un infarctus à 65 ans, "
            "son frère est hypertendu et sa sœur obèse.",

            "Son mode de vie comporte des repas irréguliers avec de la restauration rapide, deux à trois "
            "sodas par jour, deux à trois verres de vin quotidiens, une activité physique limitée à dix "
            "minutes de marche, et six heures de sommeil avec des ronflements.",

            "À l'examen, le surpoids abdominal est visible, l'IMC à 31 kg/m² et le tour de taille à "
            "108 cm. La tension artérielle est à 145/92 mmHg, donc au-dessus de la cible malgré le "
            "traitement, la fréquence cardiaque à 78 régulière, l'hydratation et la coloration normales. "
            "Les bruits du cœur sont réguliers sans souffle et les pouls périphériques présents et "
            "symétriques.",

            "Mon diagnostic est un diabète de type 2 de découverte récente : l'âge, l'obésité "
            "abdominale, l'hérédité maternelle et l'installation progressive plaident pour ce type "
            "plutôt que pour un type 1. Le diagnostic est déjà établi par deux glycémies à jeun au-delà "
            "du seuil.",

            "Je demande une HbA1c pour connaître l'exposition des trois derniers mois et fixer une "
            "cible, et je lance le bilan de complications dès aujourd'hui : créatinine avec débit de "
            "filtration et rapport albuminurie/créatininurie, fond d'œil, ECG de repos, bilan lipidique "
            "complet, transaminases, et gradation du risque podologique. Dans le type 2, ces "
            "complications peuvent précéder le diagnostic : elles ne s'attendent pas.",

            "Pour la prise en charge, je commence par les mesures qui ont le meilleur rapport "
            "effort/bénéfice : supprimer les sodas, réduire l'alcool, négocier une activité physique en "
            "minutes par semaine, et viser une perte de 5 à 10 % du poids. J'introduis de la metformine "
            "en première intention, j'optimise l'antihypertenseur puisque 145/92 n'est pas à la cible, "
            "et je discute une statine au vu d'un risque cardiovasculaire global majeur.",

            "Enfin je structure le suivi : HbA1c tous les trois mois jusqu'à l'objectif, fond d'œil et "
            "bilan rénal annuels, examen des pieds à chaque consultation, éducation thérapeutique, "
            "vaccinations à jour. Et je recherche un syndrome d'apnées du sommeil, évoqué par les "
            "ronflements, les six heures de sommeil et l'obésité abdominale.",
        ],
        "sbar": {
            "S": "Homme de 52 ans adressé pour hyperglycémie découverte au bilan d'entreprise : 1,8 puis 1,9 g/L à jeun.",
            "B": "HTA traitée depuis 5 ans, dyslipidémie non traitée, ex-fumeur 20 PA, IMC 31, tour de taille 108 cm, mère diabétique, père décédé d'infarctus à 65 ans.",
            "A": "Diabète de type 2 de découverte récente, symptomatique depuis 3 mois — polyurie, polydipsie, perte de 4 kg — avec complications probablement déjà présentes : flou visuel, paresthésies des pieds, mycose génitale récente. Risque cardiovasculaire global majeur, TA à 145/92 non contrôlée.",
            "R": "HbA1c et bilan de complications d'emblée, metformine, optimisation de l'antihypertenseur, statine à discuter, mesures hygiéno-diététiques ciblées, recherche d'un SAOS, suivi structuré.",
        },
        "questions": [
            ("Le patient dit n'avoir eu aucun symptôme. Qu'en pensez-vous ?",
             "Qu'il faut les demander un par un, parce qu'ils ne se rapportent pas spontanément. En "
             "l'interrogeant, j'ai retrouvé une polyurie avec deux à trois levers nocturnes depuis trois "
             "mois, une polydipsie à trois ou quatre litres, et une perte de quatre kilos en six mois. "
             "Il les avait attribués au travail et au stress. Cette chronologie m'indique aussi que "
             "l'hyperglycémie évolue depuis plusieurs mois au moins."),
            ("Pourquoi faire le bilan de complications tout de suite ?",
             "Parce que le diabète de type 2 évolue silencieusement pendant des années avant d'être "
             "diagnostiqué : une rétinopathie peut être présente le jour du diagnostic. Et parce que ce "
             "patient a déjà des signes — un flou visuel, des paresthésies des pieds, et une mycose "
             "génitale il y a deux mois, qui est une infection révélatrice classique. Attendre un an "
             "serait perdre du temps sur des complications déjà installées."),
            ("Quelle est votre priorité thérapeutique ?",
             "Le risque cardiovasculaire global, pas la seule glycémie. Ce patient cumule hypertension "
             "mal contrôlée à 145/92, dyslipidémie non traitée, ex-tabagisme à 20 paquets-années, "
             "obésité abdominale, sédentarité et un père décédé d'infarctus à 65 ans. Un contrôle "
             "glycémique isolé ne modifierait pas l'essentiel de son pronostic."),
            ("Par quelle mesure hygiéno-diététique commencez-vous ?",
             "Par les sodas. Deux à trois par jour représentent un apport considérable, et c'est la "
             "seule mesure supprimable en une décision, sans effort d'organisation. Ensuite l'alcool, à "
             "deux ou trois verres quotidiens, que j'aborde sans moraliser. Et l'activité physique, que "
             "je négocie en minutes par semaine et en trajets réels plutôt qu'en recommandations "
             "générales. L'objectif de poids est une perte de 5 à 10 %, atteignable et suffisante."),
            ("Y a-t-il autre chose à chercher chez ce patient ?",
             "Un syndrome d'apnées du sommeil. Il ronfle, dort six heures et présente une obésité "
             "abdominale avec un tour de taille à 108 cm : la probabilité est forte. C'est important "
             "parce que le SAOS aggrave l'hypertension et le contrôle glycémique, et qu'il se traite."),
        ],
    },

    "scenario": [
        ("Identité et cadre", [
            ("Patient", "homme de 52 ans"),
            ("Motif", "adressé par son médecin traitant pour une glycémie élevée"),
            ("Profession", "travail de bureau, stress important"),
            ("Position initiale", "assis, détendu, un peu pressé"),
        ]),
        ("Jeu de rôle", [
            ("État d'esprit", "peu inquiet ; considère qu'il « n'a rien »"),
            ("Minimisation", "présenter la découverte comme fortuite et sans symptôme"),
            ("Si le candidat demande les symptômes un par un", "les reconnaître alors, comme si on n'y avait pas pensé"),
            ("Si le candidat moralise", "se braquer et répondre plus brièvement"),
        ]),
        ("Phrases à dire telles quelles", [
            ("Motif", "« Mon médecin traitant m'envoie car ma glycémie est élevée. »"),
            ("Contexte", "« C'était le bilan de santé annuel de l'entreprise. »"),
            ("Valeurs", "« 1,8 à jeun, et ils ont refait, c'était 1,9. »"),
            ("Déni initial", "« Je n'avais aucun symptôme, c'est tombé comme ça. »"),
            ("Polyurie", "« Oui, je me lève 2-3 fois la nuit depuis 3 mois. »"),
            ("Polydipsie", "« Je bois environ 3-4 litres par jour. »"),
            ("Poids", "« J'ai perdu 4 kg en 6 mois, sans régime. »"),
            ("Vision", "« Ma vision est un peu floue parfois. »"),
            ("Pieds", "« J'ai des fourmillements dans les pieds le soir. »"),
            ("Mycose", "« J'ai eu une mycose il y a 2 mois. »"),
        ]),
        ("Ce qui se donne si on le demande", [
            ("Tension", "« Je suis traité pour la tension depuis 5 ans, amlodipine 5 mg. »"),
            ("Cholestérol", "« On m'a dit qu'il était limite, mais rien de prescrit. »"),
            ("Tabac", "« J'ai arrêté il y a 3 ans, je fumais un paquet par jour pendant 20 ans. »"),
            ("Alimentation", "repas irréguliers, restauration rapide plusieurs fois par semaine"),
            ("Sodas", "« 2-3 par jour. »"),
            ("Alcool", "« 2-3 verres de vin par jour. »"),
            ("Activité", "« Je marche 10 minutes jusqu'au travail. »"),
            ("Sommeil", "« 6 heures », « ma femme dit que je ronfle »"),
            ("Famille", "mère diabétique, père décédé d'infarctus à 65 ans, frère hypertendu, sœur obèse"),
            ("Poids", "95 kg pour 175 cm ; maximum 98 kg il y a un an"),
        ]),
        ("Inquiétudes et questions", [
            (None, "« Est-ce que je vais devoir faire des piqûres ? »"),
            (None, "« Je peux continuer à boire mon verre de vin ? »"),
            (None, "« C'est grave, docteur ? Ma mère l'a et elle va bien. »"),
            (None, "« Est-ce que je vais devoir prendre des médicaments toute ma vie ? »"),
        ]),
    ],
}
