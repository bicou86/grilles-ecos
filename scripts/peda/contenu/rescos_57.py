# -*- coding: utf-8 -*-
"""Contenu pédagogique — RESCOS-57, « Ralentissement, consultation téléphonique EMS ».

Dérivé des critères notés, du bloc `annexe-dd`, du bloc `cloture` et du bloc
`expert` de la grille. Aucune source externe.

Pas de bloc `scenario` : la grille en porte déjà un. Dans `cases/rescos/`, le
motif de fin de `presentation` accepte `images-wrapper`, donc le contrat de
découpage reste tenu.
"""

CONTENU = {
    "grille": "rescos/RESCOS-57 - Ralentissement - Consultation téléphonique EMS - Grille ECOS.html",
    "titre_resume": "Ralentissement aigu du sujet âgé en EMS – Résumé ECOS",
    "titre_cas": "Ralentissement aigu sur déshydratation, consultation téléphonique",

    "resume": [
        ("🔍 Anamnèse", [
            ("Poser le cadre de la consultation téléphonique", [
                "Identifier l'interlocuteur : infirmier·ère de nuit à l'EMS de la Croix",
                "Au téléphone, on n'examine pas : on demande à l'infirmier·ère de mesurer et de décrire",
                "Se nommer, préciser sa fonction, et annoncer ce qu'on cherche à décider",
                "Vérifier d'emblée les directives anticipées : réanimation OUI dans ce dossier",
            ]),
            ("Caractériser le ralentissement", [
                "Début ce soir, avec un temps de latence aux sollicitations",
                "Orienté aux quatre modes malgré le ralentissement",
                "Hier encore normal et souriant : c'est la RUPTURE avec l'état habituel qui compte",
                "Chez un résident d'EMS, l'état antérieur ne se suppose pas, il se demande",
            ]),
            ("Caractériser les diarrhées", [
                "Depuis 2 jours, 5 à 6 épisodes aujourd'hui",
                "Aqueuses, non sanglantes, pas de méléna",
                "Contage : un autre résident présente les mêmes symptômes",
                "Un vomissement alimentaire en début d'après-midi",
            ]),
            ("Ce qu'il faut chercher au téléphone", [
                "Douleurs abdominales : inconfort, mains sur le ventre",
                "Fièvre : 37,8 °C ce soir, apyrétique dans la journée",
                "Symptômes neurologiques : céphalées, vertiges, troubles visuels, déficit — tous absents",
                "Traitements en cours, et c'est là que se trouve la clé de ce cas",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Ce que l'infirmier·ère rapporte", [
                "FC 98/min, TA 120/78 mmHg, T° 37,8 °C auriculaire",
                "Ralenti mais orienté aux quatre modes, sans latéralisation ni parésie",
                "Pâleur des téguments, muqueuses et langue sèches, temps de recoloration à 4 secondes",
                "Abdomen diffusément sensible, sans défense ni détente, bruits intestinaux augmentés",
            ]),
            ("Comment lire ces chiffres chez un patient de 88 ans", [
                "Une TA à 120/78 n'est pas rassurante chez un hypertendu traité : elle est BASSE pour lui",
                "Un temps de recoloration à 4 secondes signe une hypoperfusion périphérique",
                "Une fréquence à 98/min sous traitement freinateur éventuel est déjà une tachycardie relative",
                "L'absence de défense écarte l'urgence chirurgicale, pas la gravité",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Ce qu'il faut demander, et pourquoi", [
                "Ionogramme : le losartan associé à l'hydrochlorothiazide expose à l'hyponatrémie et à l'hypokaliémie",
                "Créatinine et urée : insuffisance rénale aiguë fonctionnelle attendue",
                "FSC et CRP, glycémie",
                "Recherche de toxine de Clostridioides difficile et coproculture si contexte de collectivité",
            ]),
            ("Ce que le contexte impose", [
                "Un cas groupé en institution évoque une gastro-entérite virale épidémique",
                "Cela ne dispense pas de chercher la cause du ralentissement, qui n'est pas la diarrhée elle-même",
                "Antécédent de tuberculose traitée dans la jeunesse : à connaître, sans pertinence immédiate ici",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Ce qui se décide au téléphone", [
                "Suspendre le diurétique et l'antihypertenseur : chez un patient déshydraté, ils aggravent tout",
                "Réhydratation, orale si elle est possible, sinon par voie veineuse ou sous-cutanée",
                "Surveillance rapprochée : conscience, tension, diurèse, poids",
                "Mesures d'hygiène et isolement de contact, puisqu'un autre résident est atteint",
            ]),
            ("Décider du transfert, et sur quels critères", [
                "Transférer si : troubles de conscience progressifs, hypotension, oligo-anurie, vomissements incoercibles",
                "Ou si la voie veineuse est impossible sur place et la réhydratation orale inefficace",
                "Directives anticipées favorables à la réanimation : elles autorisent le transfert, elles ne l'imposent pas",
                "Décider AVEC l'équipe et la famille, pas contre elles — le fils vient une fois par mois, la fille vit en Allemagne",
            ]),
        ]),
    ],

    "points_cles": [
        "Au téléphone, on ne palpe pas : on fait mesurer, on fait décrire, et on donne des consignes de surveillance vérifiables",
        "Chez un résident d'EMS, la rupture avec l'état habituel vaut plus que n'importe quel chiffre — hier il était souriant",
        "Une TA à 120/78 chez un hypertendu traité de 88 ans est BASSE pour lui : les normes se lisent relativement",
        "Le losartan associé à l'hydrochlorothiazide plus une diarrhée : suspendre le traitement fait partie de la prescription",
        "Un temps de recoloration à 4 secondes est un signe d'hypoperfusion, pas un détail de l'examen",
        "Vérifier les directives anticipées AVANT de décider d'un transfert, pas après",
    ],

    "checklist": [
        ("Questions à poser à l'infirmier·ère", [
            "Depuis quand est-il ralenti ? Comment était-il hier ?",
            "Est-il orienté ? Répond-il, avec quel délai ?",
            "Combien de selles, depuis quand, quel aspect ?",
            "D'autres résidents sont-ils touchés ?",
            "Pouvez-vous me donner tension, pouls, température ?",
            "Ses muqueuses sont-elles sèches ? Combien de secondes pour la recoloration ?",
            "Quels sont ses traitements ? Y a-t-il un diurétique ?",
            "Que disent ses directives anticipées ?",
        ]),
        ("Examens à faire", [
            "Ionogramme, créatinine et urée",
            "FSC, CRP, glycémie",
            "Recherche de toxine de C. difficile et coproculture selon le contexte",
            "Bandelette urinaire et ECG selon l'évolution",
        ]),
        ("Prise en charge en 3 points", [
            "Suspendre diurétique et antihypertenseur, réhydrater",
            "Consignes de surveillance chiffrées : conscience, tension, diurèse",
            "Critères de transfert énoncés d'avance, avec les directives anticipées vérifiées",
        ]),
    ],

    "theorie": [
        ("La consultation téléphonique est un exercice à part",
         "On ne dispose que de ce que l'interlocuteur observe. La qualité de l'appel dépend de la "
         "qualité des questions.",
         [
             "S'identifier, identifier l'interlocuteur, et vérifier de qui l'on parle",
             "Demander des mesures, pas des impressions : « quelle tension ? » plutôt que « comment va-t-il ? »",
             "Faire décrire ce qu'on ne peut pas voir : couleur, sécheresse des muqueuses, temps de recoloration",
             "Terminer par des consignes vérifiables et un critère de rappel explicite",
         ]),
        ("Le ralentissement du sujet âgé n'est pas un symptôme mineur",
         "Chez un patient de 88 ans, un ralentissement d'apparition brutale est l'équivalent d'un "
         "signal d'alarme.",
         [
             "Il traduit souvent une cause organique aiguë : déshydratation, infection, trouble ionique, cause iatrogène",
             "La rupture avec l'état antérieur est le critère : hier normal et souriant, ce soir en latence",
             "L'orientation conservée aux quatre modes rassure sur la profondeur du trouble, pas sur sa cause",
             "Un état confusionnel constitué se serait accompagné de fluctuations et de désorientation",
         ]),
        ("Le piège médicamenteux de ce cas",
         "Le traitement habituel devient dangereux dès que la volémie baisse.",
         [
             "Le losartan bloque le système rénine-angiotensine et compromet l'adaptation rénale à l'hypovolémie",
             "L'hydrochlorothiazide majore les pertes hydrosodées et expose à l'hyponatrémie et à l'hypokaliémie",
             "L'association des deux, avec 5 à 6 selles liquides par jour, produit une insuffisance rénale aiguë fonctionnelle",
             "Suspendre ces traitements est une prescription à part entière, à formuler explicitement à l'infirmier·ère",
         ]),
        ("Lire les constantes relativement, pas absolument",
         "Chez un hypertendu traité de 88 ans, les seuils habituels induisent en erreur.",
         [
             "Une TA à 120/78 est basse pour lui : comparer à ses valeurs habituelles, disponibles au dossier de l'EMS",
             "Un temps de recoloration à 4 secondes signe une hypoperfusion périphérique",
             "Une fréquence à 98/min chez un sujet âgé traduit une tachycardie compensatrice",
             "Une température à 37,8 °C chez un patient de cet âge peut correspondre à une fièvre réelle : la réponse thermique est atténuée",
         ]),
    ],

    "presentation": {
        "checklist_mentale": [
            "S'identifier, identifier l'interlocuteur, situer le patient",
            "Motif de l'appel et ce qui a changé depuis hier",
            "Caractériser le ralentissement : début, profondeur, orientation",
            "Caractériser les diarrhées : durée, fréquence, aspect, contage",
            "Symptômes associés et recherche de signes neurologiques",
            "Antécédents et TRAITEMENTS — c'est là qu'est la clé",
            "Faire mesurer : tension, pouls, température, recoloration, muqueuses",
            "Vérifier les directives anticipées",
            "Prescrire : suspension des traitements, réhydratation, surveillance",
            "Énoncer les critères de transfert et le moment de rappeler",
        ],
        "mnemo": ("Au téléphone : « faire mesurer, faire décrire, faire rappeler »", [
            "Faire MESURER : tension, pouls, température, recoloration",
            "Faire DÉCRIRE : muqueuses, couleur, comportement, selles",
            "Faire RAPPELER : à quel moment, sur quel critère précis",
        ]),
        "version_longue": [
            "Il s'agit d'un appel de l'infirmier·ère de nuit de l'EMS de la Croix, concernant M. Michel "
            "Bertchi, 88 ans, résident depuis six ans, pour un ralentissement apparu ce soir.",

            "Le ralentissement se manifeste par un temps de latence aux sollicitations. Il reste orienté "
            "aux quatre modes. Hier encore, il était normal et souriant : c'est cette rupture avec son "
            "état habituel qui motive l'appel.",

            "Depuis deux jours, il présente des diarrhées, avec cinq à six épisodes aujourd'hui, "
            "aqueuses, non sanglantes, sans méléna. Un autre résident présente des symptômes similaires, "
            "ce qui évoque une épidémie de collectivité. Il a vomi une fois en début d'après-midi, de "
            "façon alimentaire.",

            "Il est inconfortable, les mains sur le ventre. Sa température est à 37,8 °C ce soir, alors "
            "qu'il était apyrétique dans la journée. Il est très fatigué, avec une faiblesse "
            "généralisée. Je n'ai retrouvé ni céphalées, ni vertiges, ni troubles visuels, ni déficit "
            "sensitivomoteur.",

            "Ses antécédents comportent une hypertension, une hypercholestérolémie, une hyperplasie "
            "bénigne de la prostate, des troubles du sommeil, un déclin cognitif léger et une "
            "tuberculose traitée dans sa jeunesse. Et surtout, son traitement comprend du losartan "
            "associé à de l'hydrochlorothiazide, de l'atorvastatine, de la tamsulosine, de la "
            "clométhiazole et du ginkgo.",

            "Il est veuf depuis huit ans, sa fille vit en Allemagne et son fils lui rend visite une fois "
            "par mois. Ses directives anticipées mentionnent une décision de réanimation favorable.",

            "Sur les constantes rapportées : fréquence cardiaque à 98, tension à 120/78, température "
            "auriculaire à 37,8 °C. Il est ralenti mais orienté, sans latéralisation ni parésie. Les "
            "téguments sont pâles, les muqueuses et la langue sèches, le temps de recoloration à quatre "
            "secondes. L'abdomen est diffusément sensible, sans défense ni détente, avec des bruits "
            "intestinaux augmentés.",

            "Mon hypothèse est un ralentissement sur déshydratation aiguë, secondaire à une "
            "gastro-entérite probablement virale en contexte épidémique, aggravée par son traitement "
            "antihypertenseur et diurétique. Je souligne que la tension à 120/78 est basse pour un "
            "hypertendu traité de 88 ans, et que le temps de recoloration à quatre secondes signe une "
            "hypoperfusion.",

            "Je demande un ionogramme, une créatinine et une urée, une FSC, une CRP et une glycémie, "
            "ainsi qu'une recherche de toxine de Clostridioides difficile et une coproculture au vu du "
            "contexte de collectivité.",

            "Je prescris la suspension immédiate du losartan et de l'hydrochlorothiazide, qui aggravent "
            "l'hypovolémie et exposent à l'insuffisance rénale aiguë fonctionnelle et aux troubles "
            "ioniques. J'organise une réhydratation, orale si elle est possible, sinon par voie "
            "veineuse ou sous-cutanée. Je donne des consignes de surveillance chiffrées : conscience, "
            "tension, diurèse, poids. Et je fais appliquer des mesures d'hygiène et un isolement de "
            "contact, puisqu'un autre résident est touché.",

            "Enfin, j'énonce à l'avance les critères de transfert : troubles de conscience progressifs, "
            "hypotension, oligo-anurie, vomissements incoercibles, ou impossibilité de réhydrater sur "
            "place. Ses directives anticipées autorisent le transfert et la réanimation, mais elles ne "
            "les imposent pas : la décision se prend avec l'équipe et avec la famille.",
        ],
        "sbar": {
            "S": "Appel de l'infirmier·ère de nuit de l'EMS pour M. Bertchi, 88 ans, ralenti depuis ce soir.",
            "B": "Résident depuis 6 ans. HTA, hypercholestérolémie, HBP, déclin cognitif léger. Traitement par losartan + hydrochlorothiazide. Diarrhées depuis 2 jours, un autre résident touché. Directives anticipées : réanimation OUI.",
            "A": "Ralentissement sur déshydratation aiguë par gastro-entérite épidémique, aggravée par le traitement diurétique et antihypertenseur. TA 120/78 basse pour lui, recoloration à 4 secondes, muqueuses sèches. Orienté, sans signe de localisation.",
            "R": "Suspendre losartan et hydrochlorothiazide, réhydrater, ionogramme et fonction rénale, isolement de contact, surveillance chiffrée, critères de transfert énoncés d'avance.",
        },
        "questions": [
            ("Qu'est-ce qui vous inquiète le plus dans cet appel ?",
             "La rupture avec l'état habituel. Hier il était normal et souriant, ce soir il présente un "
             "temps de latence aux sollicitations. Chez un patient de 88 ans, un ralentissement "
             "d'apparition brutale traduit presque toujours une cause organique aiguë. Le fait qu'il "
             "reste orienté aux quatre modes me rassure sur la profondeur du trouble, pas sur sa cause."),
            ("La tension est à 120/78. N'est-ce pas normal ?",
             "Pas pour lui. C'est un hypertendu de 88 ans, traité par losartan et hydrochlorothiazide : "
             "120/78 est une valeur basse dans son contexte, et elle doit être comparée à ses chiffres "
             "habituels, qui figurent au dossier de l'EMS. Le temps de recoloration à quatre secondes "
             "confirme d'ailleurs l'hypoperfusion périphérique."),
            ("Quel est le rôle de son traitement ?",
             "Central. Le losartan bloque le système rénine-angiotensine et compromet l'adaptation "
             "rénale à l'hypovolémie ; l'hydrochlorothiazide majore les pertes hydrosodées et expose à "
             "l'hyponatrémie et à l'hypokaliémie. Avec cinq à six selles liquides par jour, "
             "l'association produit une insuffisance rénale aiguë fonctionnelle. Suspendre ces deux "
             "traitements est une prescription à part entière, que je formule explicitement."),
            ("Comment procédez-vous, puisque vous ne pouvez pas examiner le patient ?",
             "Je fais mesurer et je fais décrire. Je demande des chiffres — tension, pouls, température, "
             "temps de recoloration — plutôt que des impressions. Je fais décrire ce que je ne peux pas "
             "voir : l'état des muqueuses, la couleur des téguments, l'aspect des selles, le "
             "comportement. Et je termine par des consignes de surveillance vérifiables et un critère "
             "de rappel explicite."),
            ("Le transféreriez-vous à l'hôpital ?",
             "Pas d'emblée dans l'état décrit : il est orienté, sa tension est encore correcte, et la "
             "réhydratation peut débuter sur place. Mais j'énonce les critères de transfert à l'avance — "
             "troubles de conscience progressifs, hypotension, oligo-anurie, vomissements incoercibles, "
             "ou impossibilité de réhydrater. Ses directives anticipées sont favorables à la "
             "réanimation, ce qui autorise le transfert sans l'imposer : la décision se prend avec "
             "l'équipe et avec la famille."),
        ],
    },
}
