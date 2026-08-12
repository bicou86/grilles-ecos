# -*- coding: utf-8 -*-
"""Contenu pédagogique — Pédiatrie, « Enfant 3 ans avec toux ».

Dérivé des critères notés, du bloc `annexe-dd` et du bloc `cloture` de la grille.
Aucune source externe. Écrire en TEXTE BRUT : le balisage est posé à l'injection.
"""

CONTENU = {
    "grille": "rescos-locales/Pédiatrie - Enfant 3 ans avec toux - Grille ECOS.html",
    "titre_resume": "Toux aiguë du jeune enfant – Résumé ECOS",
    "titre_cas": "Toux aiguë de l'enfant de 3 ans",

    "resume": [
        ("🔍 Anamnèse", [
            ("Caractériser la toux", [
                "Début il y a 5 jours, progressif",
                "Toux grasse et productive, expectorations claires à jaunâtres — la couleur ne signe pas une infection bactérienne",
                "Présente toute la journée, pire le matin, déclenchée par l'effort et le rire",
                "Toux nocturne qui réveille l'enfant 2 à 3 fois : c'est ce qui inquiète le père et ce qui mesure la gêne",
            ]),
            ("Les symptômes associés, et surtout ceux qui manquent", [
                "Fièvre à 38,5 °C les deux premiers jours, 37,8 °C aujourd'hui",
                "Rhinorrhée depuis une semaine : l'atteinte des voies aériennes supérieures a précédé",
                "PAS de dyspnée, PAS de sifflements, PAS de douleur thoracique — ces absences sont le cœur du raisonnement",
                "Appétit diminué, fatigue, un vomissement après une quinte",
            ]),
            ("Le terrain atopique, qui change la lecture", [
                "2 à 3 bronchites par hiver, une bronchiolite hospitalisée à 8 mois",
                "Eczéma atopique personnel",
                "Mère asthmatique, père allergique aux pollens",
                "Ce terrain n'explique pas l'épisode actuel, mais il fait poser la question de l'asthme du nourrisson",
            ]),
            ("Le contexte, qui oriente vers le viral", [
                "École maternelle, plusieurs enfants toussent dans la classe",
                "Pas de tabagisme passif",
                "Un chat depuis six mois — pertinent pour l'allergologie, pas pour cet épisode",
                "Vaccinations à jour, coqueluche comprise : cela rend une coqueluche peu probable sans l'exclure formellement",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Ce qui rassure, et qu'il faut dire", [
                "État général conservé, enfant éveillé et coopératif, coloration normale, hydratation correcte",
                "Température 37,8 °C, fréquence cardiaque 110/min, fréquence respiratoire 28/min, saturation 97 % en air ambiant",
                "Pas de tirage, pas de cyanose : l'absence de signe de lutte est le point le plus important de cet examen",
            ]),
            ("Ce qu'on trouve", [
                "Rhinorrhée antérieure mucopurulente, pharynx légèrement érythémateux, tympans normaux",
                "Quelques adénopathies cervicales",
                "Râles bronchiques diffus, SANS sibilants — la distinction commande la conduite",
                "Percussion normale, examen cardiaque, abdominal et cutané sans particularité en dehors de l'eczéma des plis",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Ce qu'il ne faut PAS demander", [
                "Aucune radiographie thoracique : état général conservé, pas de signe de lutte, saturation normale, auscultation symétrique",
                "Aucun bilan sanguin, aucun prélèvement microbiologique dans ce tableau",
                "Demander des examens ici, c'est irradier et inquiéter sans rien changer",
            ]),
            ("Quand la radiographie deviendrait justifiée", [
                "Fièvre élevée persistante au-delà de 3 à 5 jours ou réascension thermique",
                "Signes de lutte, tachypnée, désaturation",
                "Asymétrie auscultatoire, matité à la percussion",
                "Altération de l'état général, mauvaise tolérance",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Ce qui se prescrit", [
                "Rien d'antibiotique : le tableau est viral",
                "Désobstruction rhinopharyngée au sérum physiologique, qui a déjà montré un effet",
                "Antipyrétique si la fièvre gêne, pas systématiquement",
                "Hydratation, position surélevée pour la nuit, aération",
            ]),
            ("Ce qui ne se prescrit pas chez l'enfant", [
                "Antitussifs : contre-indiqués chez le jeune enfant, et la toux grasse est utile",
                "Mucolytiques et fluidifiants : contre-indiqués avant 2 ans, sans bénéfice démontré ensuite",
                "Antibiotiques sur la couleur des expectorations : elle ne distingue pas viral de bactérien",
            ]),
            ("Le filet de sécurité, à donner par écrit", [
                "Reconsulter si : difficulté à respirer, tirage, respiration rapide, lèvres bleutées",
                "Si l'enfant boit moins, mouille moins de couches, devient somnolent ou geignard",
                "Si la fièvre dure plus de 3 jours ou remonte après amélioration",
                "Revoir à distance pour poser la question de l'asthme du nourrisson : trois épisodes obstructifs feraient basculer le diagnostic",
            ]),
        ]),
    ],

    "points_cles": [
        "Absence de signes de lutte, saturation normale, état général conservé : ces trois éléments autorisent à ne demander AUCUN examen",
        "La couleur des expectorations ne distingue pas une infection virale d'une bactérienne — elle ne justifie jamais une antibiothérapie",
        "Râles bronchiques SANS sibilants : pas de bronchodilatateur, pas d'argument pour une crise d'asthme",
        "Antitussifs et mucolytiques sont contre-indiqués chez le jeune enfant : la toux grasse évacue",
        "Le terrain atopique — eczéma, mère asthmatique, bronchites répétées — fait poser la question de l'asthme du nourrisson À DISTANCE, pas aujourd'hui",
        "Le filet de sécurité se donne par écrit et se vérifie : c'est le vrai traitement de cette consultation",
    ],

    "checklist": [
        ("Questions à poser", [
            "Depuis quand, comment a-t-elle commencé ?",
            "Toux grasse ou sèche ? Ramène-t-il quelque chose ?",
            "Le réveille-t-elle la nuit ? Combien de fois ?",
            "A-t-il du mal à respirer, siffle-t-il ?",
            "Comment mange-t-il, comment boit-il, combien de couches ?",
            "Est-il déjà passé par des épisodes semblables ? Combien par hiver ?",
            "Y a-t-il de l'asthme ou des allergies dans la famille ?",
            "Ses vaccins sont-ils à jour ?",
        ]),
        ("Examens à faire", [
            "État général, coloration, hydratation",
            "Paramètres vitaux avec SATURATION",
            "Recherche des signes de lutte : tirage, battement des ailes du nez, geignement",
            "Auscultation à la recherche de sibilants et d'une asymétrie ; percussion ; examen ORL",
        ]),
        ("Prise en charge en 3 points", [
            "Aucun examen complémentaire, aucun antibiotique",
            "Désobstruction rhinopharyngée, antipyrétique si gêne, hydratation",
            "Filet de sécurité écrit et contrôle à distance pour la question de l'asthme",
        ]),
    ],

    "theorie": [
        ("Ce qui autorise à ne rien demander",
         "Décider de ne pas prescrire d'examen est une décision clinique, qui s'argumente sur des "
         "éléments précis.",
         [
             "État général conservé : l'enfant est éveillé, coopératif, bien coloré, correctement hydraté",
             "Absence de signes de lutte : ni tirage, ni battement des ailes du nez, ni geignement",
             "Saturation à 97 % et fréquence respiratoire à 28/min, normales pour l'âge",
             "Auscultation symétrique sans foyer, percussion normale",
             "Chacun de ces éléments doit être énoncé : c'est leur ensemble qui remplace la radiographie",
         ]),
        ("Râles bronchiques ou sibilants : la distinction qui décide",
         "Les deux s'entendent à l'auscultation d'un enfant qui tousse, et n'appellent pas la même "
         "conduite.",
         [
             "Les râles bronchiques traduisent l'encombrement des grosses voies aériennes : ils se mobilisent avec la toux",
             "Les sibilants traduisent une obstruction bronchique : ils feraient discuter un bronchodilatateur",
             "Ici il n'y a pas de sibilant, et pas de dyspnée : aucun argument pour une crise d'asthme aujourd'hui",
             "Cette absence doit être notée explicitement, car c'est elle qui écarte la principale alternative",
         ]),
        ("La couleur des expectorations, un faux ami tenace",
         "« Des glaires jaunâtres » est la phrase qui déclenche le plus d'antibiothérapies injustifiées.",
         [
             "La coloration vient des polynucléaires dégradés, présents dans les infections virales comme bactériennes",
             "Elle n'a aucune valeur discriminante et ne doit jamais motiver une prescription",
             "Ce qui oriente vers une surinfection : fièvre élevée persistante ou qui remonte, altération de l'état général, foyer auscultatoire",
             "Le dire au parent fait partie du soin : sans explication, l'antibiotique sera demandé ailleurs",
         ]),
        ("L'asthme du nourrisson : la question se pose, mais pas aujourd'hui",
         "Le terrain est évocateur, et c'est précisément pourquoi il ne faut pas conclure dans "
         "l'urgence.",
         [
             "Eczéma atopique personnel, mère asthmatique, père allergique : le terrain atopique est constitué",
             "Deux à trois bronchites par hiver et une bronchiolite hospitalisée à 8 mois",
             "La définition classique retient trois épisodes d'obstruction bronchique avant l'âge de 3 ans",
             "Or l'épisode actuel n'est pas obstructif : ni sibilant, ni dyspnée. Il ne compte pas comme tel",
             "La question se reprend à distance, au calme, avec l'historique complet — et c'est ce qu'on annonce au père",
         ]),
    ],

    "presentation": {
        "checklist_mentale": [
            "Intro : âge, qui accompagne, motif et durée",
            "Caractériser la toux : début, type, horaire, déclencheurs, retentissement nocturne",
            "Symptômes associés — et énoncer les absences : dyspnée, sifflements, douleur",
            "Alimentation, hydratation, couches, état général vu par le parent",
            "Antécédents respiratoires et terrain atopique personnel et familial",
            "Contexte : collectivité, tabagisme passif, animaux, vaccinations",
            "Examen : état général, paramètres avec saturation, signes de lutte, auscultation, ORL",
            "Argumenter l'absence d'examen complémentaire",
            "Prise en charge symptomatique, ce qu'on ne prescrit pas et pourquoi",
            "Filet de sécurité écrit et contrôle à distance pour l'asthme",
        ],
        "mnemo": ("Les quatre « pas » qui autorisent à ne rien demander", [
            "Pas de tirage",
            "Pas de désaturation",
            "Pas d'asymétrie auscultatoire",
            "Pas d'altération de l'état général",
        ]),
        "version_longue": [
            "Il s'agit d'un enfant de 3 ans, amené par son père pour une toux persistante depuis cinq "
            "jours.",

            "La toux a débuté progressivement, elle est grasse et productive, avec des glaires claires à "
            "jaunâtres. Elle est présente toute la journée, pire le matin, déclenchée par l'effort et le "
            "rire, et le réveille deux à trois fois par nuit.",

            "Il a eu de la fièvre à 38,5 °C les deux premiers jours, aujourd'hui à 37,8 °C. Une "
            "rhinorrhée précède la toux depuis une semaine. Il n'a pas d'essoufflement, pas de "
            "sifflement, pas de douleur thoracique. Son appétit est diminué, il est plus fatigué que "
            "d'habitude, et il a vomi une fois après une quinte.",

            "Dans ses antécédents, deux à trois bronchites par hiver, une bronchiolite hospitalisée à "
            "huit mois, un eczéma atopique. Sa mère est asthmatique et son père allergique aux pollens. "
            "Aucun diagnostic d'asthme n'a été posé.",

            "Il est en petite section de maternelle où plusieurs enfants toussent, les parents ne fument "
            "pas, et la famille a un chat depuis six mois. Ses vaccinations sont à jour, coqueluche "
            "comprise. Le père a donné du paracétamol pour la fièvre et fait des inhalations de sérum "
            "physiologique, avec une amélioration temporaire.",

            "À l'examen, l'état général est conservé : l'enfant est éveillé, coopératif, bien coloré et "
            "correctement hydraté. La température est à 37,8 °C, la fréquence cardiaque à 110, la "
            "fréquence respiratoire à 28 par minute et la saturation à 97 % en air ambiant. Il n'y a ni "
            "tirage ni cyanose. L'examen ORL retrouve une rhinorrhée antérieure mucopurulente, un "
            "pharynx légèrement érythémateux, des tympans normaux et quelques adénopathies cervicales. "
            "À l'auscultation pulmonaire, j'entends des râles bronchiques diffus, sans sibilant, avec "
            "une percussion normale. Les examens cardiaque, abdominal et cutané sont sans particularité "
            "en dehors de l'eczéma des plis.",

            "Mon hypothèse est une infection virale des voies aériennes avec atteinte bronchique, dans "
            "un contexte de collectivité et sur un terrain atopique. Les diagnostics différentiels sont "
            "une pneumonie, écartée par l'absence de fièvre élevée persistante, de signes de lutte, "
            "d'asymétrie auscultatoire et de désaturation ; une crise d'asthme, écartée par l'absence de "
            "sibilants et de dyspnée ; et une coqueluche, peu probable au vu de la vaccination à jour et "
            "de l'absence de quintes émétisantes répétées.",

            "Je ne demande aucun examen complémentaire, et je peux le justifier : état général "
            "conservé, absence de signes de lutte, saturation normale, auscultation symétrique. Une "
            "radiographie deviendrait justifiée en cas de fièvre élevée persistante ou de réascension, "
            "de signes de lutte, de désaturation, d'asymétrie ou d'altération de l'état général.",

            "Pour le traitement, je ne prescris pas d'antibiotique : la couleur des expectorations ne "
            "distingue pas viral de bactérien. Je propose une désobstruction rhinopharyngée au sérum "
            "physiologique, qui a déjà aidé, un antipyrétique si la fièvre gêne, une bonne hydratation "
            "et une position surélevée la nuit. Je ne prescris ni antitussif ni mucolytique, "
            "contre-indiqués à cet âge — et la toux grasse est utile.",

            "Enfin je remets un filet de sécurité par écrit : reconsulter en cas de difficulté "
            "respiratoire, de tirage, de respiration rapide, de lèvres bleutées, si l'enfant boit moins "
            "ou mouille moins de couches, devient somnolent, ou si la fièvre dure plus de trois jours ou "
            "remonte. Et je propose un contrôle à distance pour reprendre au calme la question de "
            "l'asthme du nourrisson, que son terrain et ses bronchites répétées justifient de poser — "
            "mais pas aujourd'hui, puisque cet épisode n'est pas obstructif.",
        ],
        "sbar": {
            "S": "Enfant de 3 ans, amené par son père pour toux grasse depuis 5 jours.",
            "B": "Terrain atopique — eczéma, mère asthmatique, père allergique, 2-3 bronchites par hiver, bronchiolite hospitalisée à 8 mois. Petite section, plusieurs enfants malades. Vaccins à jour.",
            "A": "Infection virale des voies aériennes avec atteinte bronchique. État général conservé, pas de signe de lutte, saturation 97 %, râles bronchiques sans sibilant. Pneumonie, asthme et coqueluche écartés cliniquement.",
            "R": "Aucun examen, aucun antibiotique. Désobstruction rhinopharyngée, antipyrétique si gêne, hydratation. Filet de sécurité écrit et contrôle à distance pour la question de l'asthme.",
        },
        "questions": [
            ("Demandez-vous une radiographie ?",
             "Non, et je peux l'argumenter point par point : l'état général est conservé, il n'y a aucun "
             "signe de lutte, la saturation est à 97 %, la fréquence respiratoire est normale pour "
             "l'âge, l'auscultation est symétrique et la percussion normale. Une radiographie ici "
             "irradierait et inquiéterait sans rien changer. Elle deviendrait justifiée en cas de fièvre "
             "élevée persistante ou qui remonte, de signes de lutte, de désaturation, d'asymétrie "
             "auscultatoire ou d'altération de l'état général."),
            ("Le père insiste : les glaires sont jaunes, il veut un antibiotique.",
             "Je lui explique que la couleur vient des cellules de défense dégradées, et qu'on la "
             "retrouve dans les infections virales comme bactériennes : elle n'a aucune valeur pour "
             "trancher. Ce qui m'orienterait vers une surinfection serait une fièvre élevée qui "
             "persiste ou qui remonte, une altération de l'état général, ou un foyer à l'auscultation — "
             "et rien de tout cela n'est présent. Prendre le temps de cette explication évite que "
             "l'antibiotique soit demandé ailleurs."),
            ("Pourquoi ne prescrivez-vous pas de sirop contre la toux ?",
             "Parce que les antitussifs sont contre-indiqués chez le jeune enfant, et que les "
             "mucolytiques le sont avant deux ans sans bénéfice démontré ensuite. Et parce que cette "
             "toux est grasse : elle sert à évacuer les sécrétions. La supprimer serait "
             "contre-productif. Ce qui aide réellement, c'est la désobstruction rhinopharyngée, qui a "
             "d'ailleurs déjà montré un effet."),
            ("Ce terrain atopique ne vous fait-il pas penser à un asthme ?",
             "Il fait poser la question, mais pas la trancher aujourd'hui. La définition classique "
             "retient trois épisodes d'obstruction bronchique avant trois ans — or l'épisode actuel "
             "n'est pas obstructif : ni sibilant, ni dyspnée. Il ne compte pas comme tel. En revanche, "
             "l'eczéma, l'asthme maternel, l'allergie paternelle, les bronchites répétées et la "
             "bronchiolite à huit mois justifient de reprendre cet historique au calme lors d'un "
             "contrôle à distance."),
            ("Que dites-vous au père avant qu'il reparte ?",
             "Je lui remets un filet de sécurité par écrit, et je vérifie qu'il l'a compris. Reconsulter "
             "en urgence si l'enfant a du mal à respirer, si l'on voit sa peau se creuser entre les "
             "côtes, s'il respire vite, si ses lèvres bleuissent. Reconsulter aussi s'il boit moins, "
             "mouille moins de couches, devient somnolent ou geignard, ou si la fièvre dure plus de "
             "trois jours ou remonte après amélioration."),
        ],
    },

    "scenario": [
        ("Identité et cadre", [
            ("Patient", "garçon de 3 ans"),
            ("Accompagnant", "son père, qui répond pour lui"),
            ("Motif", "toux persistante depuis 5 jours"),
            ("Enfant", "éveillé, joue avec un jouet, tousse à quelques reprises pendant l'entretien"),
        ]),
        ("Jeu de rôle — le père", [
            ("État d'esprit", "inquiet mais posé ; fatigué par les réveils nocturnes"),
            ("Demande implicite", "veut un antibiotique, sans le dire d'emblée"),
            ("Insistance", "amener la couleur des glaires si le candidat ne parle pas de traitement"),
            ("Si le candidat explique", "accepter l'absence d'antibiotique et poser des questions sur la surveillance"),
        ]),
        ("Phrases à dire telles quelles", [
            ("Motif", "« Mon fils tousse beaucoup depuis 5 jours. »"),
            ("Toux", "« Elle est grasse », « C'est pire le matin », « Ça le réveille 2 à 3 fois la nuit »"),
            ("Déclencheurs", "« Quand il court ou quand il rit. »"),
            ("Expectorations", "« Des glaires claires, parfois jaunâtres. »"),
            ("Fièvre", "« 38,5 les deux premiers jours, maintenant ça baisse. »"),
            ("Nez", "« Il a le nez qui coule depuis une semaine. »"),
            ("Absences", "« Non, il ne siffle pas », « Non, il n'est pas essoufflé »"),
            ("Vomissement", "« Il a vomi une fois après une quinte. »"),
            ("Traitement essayé", "« Du paracétamol, et du sérum physiologique — ça le soulage un moment. »"),
        ]),
        ("Ce qui se donne si on le demande", [
            ("Antécédents", "« 2 à 3 bronchites par hiver », « Une bronchiolite à 8 mois, il avait été hospitalisé »"),
            ("Eczéma", "« Il fait de l'eczéma dans les plis. »"),
            ("Famille", "« Sa mère est asthmatique », « Moi je suis allergique aux pollens »"),
            ("École", "« Il est en petite section », « Plusieurs enfants toussent dans sa classe »"),
            ("Tabac", "« Non, on ne fume pas. »"),
            ("Animaux", "« On a un chat depuis 6 mois. »"),
            ("Vaccins", "« À jour, il a eu tous ses rappels. »"),
            ("Alimentation", "mange moins mais boit normalement ; couches normales"),
        ]),
        ("Inquiétudes et questions", [
            (None, "« Est-ce qu'il ne faudrait pas un antibiotique ? Les glaires sont jaunes. »"),
            (None, "« Est-ce qu'il faut faire une radio ? »"),
            (None, "« Est-ce qu'il va devenir asthmatique comme sa mère ? »"),
            (None, "« Est-ce qu'il peut retourner à l'école ? »"),
        ]),
    ],
}
