# -*- coding: utf-8 -*-
"""Contenu pédagogique — ECOS Diag 3, « La dyspnée aux multiples visages ».

Dérivé des critères notés de la grille. Aucune source externe.
"""

CONTENU = {
    "grille": "casecos/ECOS Diag 3 - Dyspnée - Grille ECOS.html",
    "titre_resume": "Dyspnée multifactorielle du sujet âgé – Résumé ECOS",
    "titre_cas": "Dyspnée d'effort progressive du fumeur",

    "resume": [
        ("🔍 Anamnèse", [
            ("Graduer la dyspnée, pas seulement la constater", [
                "Essoufflé en montant un étage, alors qu'il en montait deux sans peine : c'est une gradation NYHA",
                "Aggravation progressive depuis 2 semaines",
                "Dort avec 2 oreillers, sinon il tousse : orthopnée débutante",
                "Le stade ET l'évolution temporelle sont deux informations distinctes, toutes deux cotées",
            ]),
            ("Le risque thromboembolique, à relier explicitement", [
                "Prothèse totale de genou droit il y a un mois",
                "Immobilité relative les premières semaines",
                "Une chirurgie orthopédique majeure récente est un facteur de risque MAJEUR — le mentionner sans le relier ne suffit pas",
            ]),
            ("Le lien AINS – saignement – anémie", [
                "Ibuprofène 3 fois par jour depuis 3 semaines pour une entorse de cheville",
                "Selles peut-être plus foncées que d'habitude — élément obtenu seulement en le demandant",
                "C'est la chaîne complète qu'il faut énoncer : AINS → saignement occulte → anémie → dyspnée",
            ]),
            ("Le terrain cardiovasculaire et le dépistage oncologique", [
                "Hypertension traitée depuis 10 ans, cœur battant parfois irrégulièrement — une fibrillation auriculaire est probable",
                "Tabagisme à un paquet par jour pendant 40 ans, arrêté il y a 5 ans",
                "Pas de perte de poids, pas de sueurs nocturnes, pas d'hémoptysie : les red flags oncologiques sont écartés, et cela se dit",
                "Pas de douleur thoracique franche, toux sèche occasionnelle, mollet opéré un peu sensible sans œdème net",
            ]),
        ]),
        ("👀 Examen clinique", [
            ("Les signes d'anémie, souvent les plus rentables", [
                "Pâleur conjonctivale marquée, pâleur palmaire",
                "Souffle systolique éjectionnel au foyer aortique — souffle fonctionnel de l'anémie",
            ]),
            ("Ce que les constantes annoncent", [
                "TA 145/85, FC 92 IRRÉGULIER, FR 18, saturation 94 % en air ambiant",
                "L'irrégularité du pouls est une donnée, pas un détail : elle oriente vers la fibrillation auriculaire",
            ]),
            ("Ce qu'il faut chercher activement", [
                "Signes de thrombose du membre opéré : circonférence comparée, douleur, chaleur",
                "Signes d'insuffisance cardiaque : crépitants, turgescence jugulaire, œdèmes, reflux hépato-jugulaire",
                "Toucher rectal à la recherche d'un méléna, cohérent avec l'hypothèse de saignement digestif",
            ]),
        ]),
        ("🧪 Examens diagnostiques", [
            ("Ce qui tranche entre les trois pistes", [
                "Formule sanguine : l'anémie se confirme ou s'écarte en une ligne",
                "ECG : fibrillation auriculaire, signes de cœur droit",
                "D-dimères et angioscanner selon la probabilité clinique — la prothèse récente la rend forte",
                "BNP ou NT-proBNP si l'insuffisance cardiaque reste discutée",
            ]),
            ("Le reste du bilan", [
                "Ionogramme, créatinine, ferritine et bilan martial",
                "Radiographie thoracique",
                "Recherche de sang dans les selles, gastroscopie selon le résultat",
            ]),
        ]),
        ("⚙️ Prise en charge", [
            ("Ce qui se décide selon la cause retrouvée", [
                "Anémie sur saignement digestif : arrêt IMMÉDIAT des AINS, protection gastrique, correction martiale, exploration endoscopique",
                "Embolie pulmonaire : anticoagulation, à débuter avant confirmation si la probabilité est forte",
                "Fibrillation auriculaire : contrôle de la fréquence et évaluation du risque embolique",
                "Ces causes ne s'excluent pas : elles peuvent coexister, et c'est le sens du titre de la station",
            ]),
            ("Ce qui se fait dans tous les cas", [
                "Arrêter l'ibuprofène, quelle que soit l'hypothèse retenue",
                "Réévaluer l'antalgie de son entorse par un autre moyen",
                "Expliquer au patient le lien entre son traitement et son essoufflement",
            ]),
        ]),
    ],

    "points_cles": [
        "Trois causes plausibles coexistent : anémie sur AINS, embolie pulmonaire post-prothèse, fibrillation auriculaire",
        "Une prothèse de genou il y a un mois est un facteur de risque thromboembolique MAJEUR — le relier explicitement",
        "AINS trois fois par jour depuis trois semaines plus des selles foncées : la chaîne complète doit être énoncée",
        "Un pouls irrégulier noté aux constantes est une donnée diagnostique, pas une imprécision de mesure",
        "La pâleur conjonctivale et un souffle systolique fonctionnel orientent vers l'anémie avant tout examen",
        "Chercher les red flags oncologiques ET dire qu'ils sont absents : l'absence documentée est une information",
    ],

    "checklist": [
        ("Questions à poser", [
            "Combien d'étages montiez-vous avant ? Et maintenant ?",
            "Depuis quand cela s'aggrave-t-il ?",
            "Dormez-vous à plat ? Avec combien d'oreillers ?",
            "Avez-vous été opéré ou immobilisé récemment ?",
            "Quels médicaments prenez-vous, et depuis quand ?",
            "Vos selles ont-elles changé de couleur ?",
            "Avez-vous maigri, transpiré la nuit, craché du sang ?",
            "Votre cœur bat-il parfois irrégulièrement ?",
        ]),
        ("Examens à faire", [
            "Conjonctives et paumes, auscultation cardiaque à la recherche d'un souffle",
            "Prise du pouls avec appréciation de la RÉGULARITÉ",
            "Mollets : circonférence comparée, douleur, chaleur",
            "Signes d'insuffisance cardiaque, toucher rectal",
        ]),
        ("Prise en charge en 3 points", [
            "Formule sanguine, ECG, D-dimères ou angioscanner selon la probabilité",
            "Arrêt immédiat des AINS quelle que soit l'hypothèse",
            "Traitement selon la cause, en gardant à l'esprit qu'elles peuvent coexister",
        ]),
    ],

    "theorie": [
        ("Une dyspnée, trois causes, et elles s'additionnent",
         "Le piège de ce cas est de s'arrêter à la première hypothèse trouvée.",
         [
             "Anémie par saignement digestif occulte sous AINS : elle explique la dyspnée d'effort progressive et la pâleur",
             "Embolie pulmonaire après prothèse totale de genou : elle explique la désaturation à 94 % et la sensibilité du mollet",
             "Fibrillation auriculaire : elle explique le pouls irrégulier et peut décompenser une fonction cardiaque limite",
             "Chacune est plausible seule ; leur coexistence est fréquente chez un homme de 65 ans, et c'est le sens du titre de la station",
         ]),
        ("Graduer une dyspnée avant de l'expliquer",
         "« Essoufflé » ne veut rien dire tant qu'on ne l'a pas rapporté à un effort et à une date.",
         [
             "La classification NYHA gradue l'effort qui déclenche : marche en terrain plat, montée d'un étage, repos",
             "Ici le patient est passé de deux étages sans peine à un étage avec essoufflement, en deux semaines",
             "Cette CINÉTIQUE est aussi informative que le stade : deux semaines évoquent un processus aigu ou subaigu",
             "L'orthopnée — deux oreillers pour ne pas tousser — ajoute une orientation cardiaque",
         ]),
        ("La chaîne AINS, et pourquoi il faut l'énoncer entière",
         "La grille cote le raisonnement complet, pas la simple mention du médicament.",
         [
             "Les AINS provoquent des lésions gastro-duodénales, souvent silencieuses",
             "Le saignement chronique est occulte : pas d'hématémèse, seulement des selles plus foncées",
             "L'anémie s'installe progressivement, ce qui permet une tolérance apparente jusqu'à un seuil",
             "La dyspnée d'effort est alors le symptôme révélateur — trois semaines de traitement suffisent",
             "Identifier les AINS sans faire ce lien ne vaut que la moitié des points, et cliniquement rien",
         ]),
        ("Le pouls irrégulier, une donnée qu'on note et qu'on suit",
         "Il figure dans les constantes, et il oriente.",
         [
             "Chez un hypertendu de 65 ans, une irrégularité fait évoquer une fibrillation auriculaire",
             "Le patient rapporte lui-même qu'on lui a dit que son cœur battait parfois irrégulièrement",
             "La fibrillation peut décompenser une fonction cardiaque limite et expliquer une part de la dyspnée",
             "Elle impose une évaluation du risque embolique — d'autant plus chez un patient déjà à risque thrombotique",
         ]),
    ],

    "presentation": {
        "checklist_mentale": [
            "Intro : âge, motif, ancienneté, inquiétude exprimée",
            "Graduer la dyspnée : stade et cinétique, orthopnée",
            "Risque thromboembolique : chirurgie, immobilisation, signes de thrombose",
            "Traitements : AINS, durée, posologie, et la chaîne jusqu'à l'anémie",
            "Red flags oncologiques recherchés et énoncés comme absents",
            "Terrain cardiovasculaire : HTA, rythme, tabac",
            "Examen : pâleur, souffle, régularité du pouls, mollets, signes d'insuffisance cardiaque",
            "Constantes avec saturation",
            "Les trois hypothèses, avec arguments, et le fait qu'elles peuvent coexister",
            "Examens ciblés et arrêt immédiat des AINS",
        ],
        "mnemo": ("« Trois visages d'une même dyspnée »", [
            "Le sang qui manque : AINS → saignement → anémie",
            "Le caillot : prothèse de genou il y a un mois",
            "Le rythme : pouls irrégulier chez un hypertendu",
            "Et rien n'oblige à choisir : elles s'additionnent",
        ]),
        "version_longue": [
            "Il s'agit de M. Simon, 65 ans, qui consulte pour une dyspnée d'effort progressive évoluant "
            "depuis deux semaines. Il est inquiet parce qu'il a beaucoup fumé.",

            "Sur la sévérité : il est essoufflé en montant un étage, alors qu'il en montait deux sans "
            "problème auparavant, et cela s'aggrave progressivement depuis deux semaines. Il dort "
            "désormais avec deux oreillers, faute de quoi il tousse.",

            "Trois éléments de son histoire récente orientent le raisonnement. D'abord une prothèse "
            "totale du genou droit il y a un mois, avec une immobilité relative les premières semaines : "
            "c'est un facteur de risque thromboembolique majeur. Ensuite une prise d'ibuprofène trois "
            "fois par jour depuis trois semaines pour une entorse de cheville — et lorsque je "
            "l'interroge, il remarque que ses selles sont peut-être un peu plus foncées que "
            "d'habitude. Enfin, une hypertension traitée depuis dix ans, et un cœur dont on lui a dit "
            "qu'il battait parfois irrégulièrement.",

            "Il a fumé un paquet par jour pendant quarante ans et a arrêté il y a cinq ans. J'ai "
            "recherché les signaux d'alarme oncologiques : pas de perte de poids, pas de sueurs "
            "nocturnes, pas d'hémoptysie ; sa fatigue est attribuée à l'essoufflement. Il n'a pas de "
            "douleur thoracique franche, une petite toux sèche occasionnelle, un mollet opéré un peu "
            "sensible mais sans œdème net, pas de fièvre, et des vertiges au lever rapide.",

            "À l'examen, les conjonctives sont nettement pâles, les paumes également, et j'ausculte un "
            "discret souffle systolique éjectionnel au foyer aortique, compatible avec un souffle "
            "fonctionnel d'anémie. Les constantes montrent une tension à 145/85, une fréquence "
            "cardiaque à 92 et irrégulière, une fréquence respiratoire à 18 et une saturation à 94 % en "
            "air ambiant.",

            "Je retiens trois hypothèses, et je souligne qu'elles peuvent coexister. La première est "
            "une anémie par saignement digestif occulte sous anti-inflammatoires : la chaîne est "
            "complète, AINS pendant trois semaines, selles plus foncées, pâleur conjonctivale et "
            "palmaire, souffle fonctionnel, dyspnée d'effort progressive. La deuxième est une embolie "
            "pulmonaire après prothèse de genou récente, soutenue par la désaturation à 94 % et la "
            "sensibilité du mollet opéré. La troisième est une fibrillation auriculaire, évoquée par "
            "l'irrégularité du pouls et par ce que son médecin lui a dit.",

            "Je demande donc une formule sanguine, qui tranchera la question de l'anémie en une ligne, "
            "un ECG, des D-dimères et un angioscanner selon la probabilité clinique — que la prothèse "
            "récente rend forte —, un ionogramme, une créatinine, un bilan martial avec ferritine, une "
            "radiographie thoracique, une recherche de sang dans les selles et un BNP si l'insuffisance "
            "cardiaque reste discutée.",

            "Quelle que soit l'hypothèse retenue, j'arrête immédiatement l'ibuprofène et je réévalue "
            "l'antalgie de son entorse par un autre moyen. Selon les résultats : correction martiale et "
            "exploration endoscopique en cas d'anémie sur saignement ; anticoagulation, débutée avant "
            "confirmation si la probabilité d'embolie est forte ; contrôle de la fréquence et évaluation "
            "du risque embolique en cas de fibrillation. Et j'explique au patient le lien entre son "
            "traitement anti-inflammatoire et son essoufflement.",
        ],
        "sbar": {
            "S": "M. Simon, 65 ans, dyspnée d'effort progressive depuis 2 semaines, inquiet de son passé tabagique.",
            "B": "Prothèse totale de genou il y a un mois, ibuprofène 3x/j depuis 3 semaines, HTA traitée, rythme parfois irrégulier, ex-fumeur 40 paquets-années sevré depuis 5 ans.",
            "A": "Dyspnée multifactorielle : anémie par saignement digestif sous AINS (pâleur conjonctivale et palmaire, souffle fonctionnel, selles foncées), embolie pulmonaire post-prothèse (saturation 94 %, mollet sensible), fibrillation auriculaire (pouls irrégulier). Red flags oncologiques absents.",
            "R": "Formule sanguine, ECG, D-dimères et angioscanner selon probabilité, bilan martial, recherche de sang dans les selles. ARRÊT IMMÉDIAT des AINS. Traitement selon la cause, en gardant à l'esprit qu'elles coexistent.",
        },
        "questions": [
            ("Quelle est votre première hypothèse ?",
             "L'anémie par saignement digestif occulte sous anti-inflammatoires — parce que la chaîne "
             "est complète et vérifiable en une ligne de biologie. Ibuprofène trois fois par jour depuis "
             "trois semaines, selles plus foncées, pâleur conjonctivale et palmaire marquée, souffle "
             "systolique fonctionnel, dyspnée d'effort progressive. Mais je ne m'y arrête pas : deux "
             "autres causes sont plausibles et peuvent s'y ajouter."),
            ("Pourquoi insistez-vous sur la prothèse de genou ?",
             "Parce qu'une chirurgie orthopédique majeure il y a un mois, avec immobilité relative, est "
             "un facteur de risque thromboembolique majeur. Mentionner la chirurgie sans faire ce lien "
             "ne suffit pas. Avec une saturation à 94 % et un mollet opéré sensible, la probabilité "
             "clinique d'embolie pulmonaire est suffisamment forte pour orienter directement vers "
             "l'angioscanner, et pour envisager d'anticoaguler avant confirmation."),
            ("Que faites-vous du pouls irrégulier ?",
             "Je le traite comme une donnée diagnostique, pas comme une imprécision de mesure. Chez un "
             "hypertendu de 65 ans, une irrégularité fait évoquer une fibrillation auriculaire — et le "
             "patient rapporte lui-même qu'on lui a dit que son cœur battait parfois irrégulièrement. "
             "Un ECG le confirmera. La fibrillation peut décompenser une fonction cardiaque limite et "
             "expliquer une part de la dyspnée, et elle impose une évaluation du risque embolique."),
            ("Faut-il choisir entre ces trois causes ?",
             "Non, et c'est le sens du titre de la station. Chez un homme de 65 ans, ces mécanismes "
             "coexistent fréquemment : une anémie décompense une fibrillation, une fibrillation majore "
             "le retentissement d'une embolie. S'arrêter à la première hypothèse trouvée serait le "
             "piège. Je demande donc les examens des trois pistes, sans les hiérarchiser au point d'en "
             "abandonner une."),
            ("Qu'arrêtez-vous aujourd'hui ?",
             "L'ibuprofène, quelle que soit l'hypothèse retenue. Il est en cause dans l'une d'elles, "
             "inutile dans les deux autres, et dangereux dans toutes — chez un patient possiblement "
             "anémié et possiblement candidat à une anticoagulation. Je réévalue l'antalgie de son "
             "entorse par un autre moyen, et je lui explique le lien entre ce traitement et son "
             "essoufflement."),
        ],
    },

    "scenario": [
        ("Identité et cadre", [
            ("Nom", "M. Simon"),
            ("Âge", "65 ans"),
            ("Lieu", "cabinet de médecine générale"),
            ("Motif", "dyspnée d'effort progressive depuis 2 semaines"),
            ("État d'esprit", "inquiet à cause de son passé tabagique — le dire spontanément"),
        ]),
        ("Jeu de rôle", [
            ("Aspect", "pâle ; s'assoit lentement"),
            ("Souffle", "s'essouffler légèrement en parlant longtemps"),
            ("Attribution", "mettre tout sur le compte du tabac ; revenir sur « j'ai beaucoup fumé »"),
            ("Selles", "n'y penser que si le candidat pose la question — répondre alors « maintenant que vous le dites »"),
        ]),
        ("Phrases à dire telles quelles", [
            ("Sévérité", "« Je suis essoufflé quand je monte un étage, alors qu'avant je pouvais en monter deux sans problème. »"),
            ("Évolution", "« Ça s'aggrave progressivement depuis 2 semaines. »"),
            ("Orthopnée", "« Je dors avec 2 oreillers maintenant, sinon je tousse. »"),
            ("Chirurgie", "« J'ai été opéré du genou droit il y a un mois, une prothèse. J'ai été assez immobile les premières semaines. »"),
            ("AINS", "« Pour mon entorse à la cheville, le médecin m'a donné de l'ibuprofène. J'en prends depuis 3 semaines, 3 fois par jour. »"),
            ("Selles", "« Maintenant que vous le dites, mes selles sont peut-être un peu plus foncées que d'habitude. »"),
            ("Cœur", "« Le médecin m'a dit que mon cœur battait parfois irrégulièrement. »"),
            ("Tabac", "« J'ai fumé un paquet par jour pendant 40 ans, j'ai arrêté il y a 5 ans. »"),
        ]),
        ("Ce qui se donne si on le demande", [
            ("Red flags", "« Non, je n'ai pas perdu de poids. Pas de sueurs la nuit. Pas de sang quand je tousse. »"),
            ("Fatigue", "« Je suis fatigué mais c'est surtout à cause de l'essoufflement. »"),
            ("Thorax", "« Pas de vraie douleur dans la poitrine. Une petite toux sèche parfois. »"),
            ("Mollet", "« Le mollet opéré est un peu sensible mais pas vraiment gonflé. »"),
            ("Vertiges", "« Parfois la tête qui tourne quand je me lève vite. »"),
            ("Œdèmes", "« Pas vraiment d'œdème aux jambes. »"),
            ("Tension", "traitée depuis 10 ans, suivie par son médecin"),
        ]),
        ("Inquiétudes et questions", [
            (None, "« C'est le tabac, docteur ? J'ai un cancer ? »"),
            (None, "« Est-ce que c'est le cœur ? »"),
            (None, "« Je peux continuer l'ibuprofène pour ma cheville ? »"),
        ]),
    ],
}
