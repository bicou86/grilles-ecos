# -*- coding: utf-8 -*-
"""Contenu pédagogique — RESCOS-64, « Toux, station double 2 ».

Dérivé des critères notés de la grille. Aucune source externe.

Ni `presentation` ni `scenario` : la station EST un exercice de présentation de
cas devant un examinateur, et il n'y a pas de patient simulé. Une fiche de
présentation ferait doublon avec l'épreuve elle-même.
"""

CONTENU = {
    "grille": "rescos/RESCOS-64 - Toux - Station double 2 - Grille ECOS.html",
    "titre_resume": "Hémoptysie du fumeur — présentation de cas – Résumé ECOS",
    "titre_cas": "Hémoptysie chez une fumeuse de 35 UPA",

    "resume": [
        ("🔍 Ce qu'il faut avoir dit de l'anamnèse", [
            ("Identité et motif", [
                "Nom, prénom, âge de la patiente — une présentation commence toujours par là",
                "Motif principal : hémoptysie",
                "Aggravation de la toux ET de la dyspnée : les deux se citent, ils comptent séparément",
            ]),
            ("Les éléments qui font le diagnostic", [
                "Tabagisme actif à 35 unités paquets-années",
                "Douleur thoracique respiro-dépendante et augmentée à la toux",
                "Possible BPCO non investiguée, la patiente ayant refusé les explorations",
                "Perte pondérale de 4 kg en quelques mois",
                "Afébrile, sans sudations : deux absences qui orientent contre l'infection",
            ]),
        ]),
        ("👀 Ce qu'il faut avoir dit de l'examen", [
            ("Les cinq éléments cotés", [
                "Fréquence respiratoire normale",
                "Auscultation pulmonaire : sibilances diffuses",
                "Percussion pulmonaire normale",
                "Auscultation cardiaque normale",
                "Palpation thoracique sous le sein droit normale",
            ]),
            ("Ce que l'exercice évalue en plus", [
                "L'évaluation globale de la présentation : ordre, concision, hiérarchie de l'information",
                "La réflexivité — reconnaître ce qu'on n'a pas cherché et le dire",
                "Cette dernière compétence est notée à part : l'omettre coûte un point qu'aucune connaissance ne rattrape",
            ]),
        ]),
        ("🧪 Raisonnement diagnostique", [
            ("Le diagnostic le plus probable : cancer pulmonaire", [
                "POUR : tabagisme à 35 UPA, toux, dyspnée, douleur thoracique, perte pondérale",
                "CONTRE : absence de fatigue",
                "L'hémoptysie chez un fumeur de plus de 40 ans impose d'évoquer le cancer en premier, quel que soit le reste",
            ]),
            ("Les différentiels à énoncer", [
                "Exacerbation de BPCO : les sibilances diffuses et le tabagisme y renvoient, mais l'hémoptysie et la perte pondérale n'en font pas partie",
                "Embolie pulmonaire : la douleur respiro-dépendante et l'hémoptysie s'y retrouvent — l'absence de tachypnée joue contre",
                "Tuberculose : la perte pondérale l'évoque, mais l'apyrexie et l'absence de sudations nocturnes jouent contre",
                "Pneumonie : l'apyrexie et la percussion normale l'écartent largement",
            ]),
        ]),
        ("⚙️ Ce qu'il faut proposer", [
            ("Les examens", [
                "Radiographie thoracique en première intention",
                "Scanner thoracique injecté, qui explore le parenchyme et l'arbre vasculaire",
                "Bilan sanguin avec formule et crase, avant tout geste",
                "Exploration fonctionnelle respiratoire, que la patiente avait refusée",
            ]),
            ("La suite", [
                "Confirmation histologique par bronchoscopie ou biopsie guidée",
                "Bilan d'extension si la lésion se confirme",
                "Arrêt du tabac, à proposer même dans ce contexte — et surtout dans ce contexte",
                "Annonce et orientation en pneumologie, ce que cette station met précisément en scène",
            ]),
        ]),
    ],

    "points_cles": [
        "Une hémoptysie chez un fumeur de 35 UPA évoque un cancer pulmonaire jusqu'à preuve du contraire",
        "Une présentation de cas se juge autant sur l'ORDRE et la concision que sur l'exhaustivité",
        "La réflexivité est notée : dire ce qu'on n'a pas cherché vaut mieux que de laisser croire qu'on a tout fait",
        "Les absences se présentent comme des éléments à part entière : afébrile, pas de sudations, ce sont des arguments",
        "Des sibilances diffuses n'excluent pas un cancer : elles peuvent traduire une BPCO associée ou une obstruction",
        "Toujours donner les arguments POUR et CONTRE — c'est ce que l'examinateur demande explicitement",
    ],

    "checklist": [
        ("Structure de la présentation", [
            "Identité, âge, motif principal",
            "Anamnèse : facteurs de risque, symptômes, chronologie, éléments négatifs pertinents",
            "Examen : constantes, puis appareil par appareil",
            "Synthèse en une phrase",
            "Hypothèse principale avec arguments pour et contre",
            "Différentiels hiérarchisés",
            "Examens proposés et conduite",
            "Ce que je n'ai pas cherché et que j'aurais dû",
        ]),
        ("Les arguments à ne pas oublier", [
            "Tabagisme quantifié en unités paquets-années",
            "Perte pondérale chiffrée et datée",
            "Caractère respiro-dépendant de la douleur",
            "Apyrexie et absence de sudations nocturnes",
        ]),
        ("Examens à proposer", [
            "Radiographie puis scanner thoracique injecté",
            "Formule sanguine et crase",
            "Bronchoscopie ou biopsie guidée pour l'histologie",
            "Exploration fonctionnelle respiratoire",
        ]),
    ],

    "theorie": [
        ("Ce qu'une présentation de cas doit contenir, et dans quel ordre",
         "L'exercice n'évalue pas la quantité d'informations mais leur hiérarchie.",
         [
             "Commencer par identifier : nom, âge, motif — l'auditeur doit savoir de qui l'on parle avant d'entendre les détails",
             "Regrouper l'anamnèse par pertinence décroissante, pas par ordre chronologique de recueil",
             "Énoncer les éléments négatifs qui comptent : « afébrile, sans sudations » est une information, pas un vide",
             "Terminer par une synthèse en une phrase avant d'annoncer l'hypothèse",
         ]),
        ("Pourquoi l'hémoptysie du fumeur est une urgence diagnostique",
         "Elle impose une exploration, même isolée, même minime.",
         [
             "Chez un fumeur de plus de 40 ans, elle fait évoquer un cancer bronchique jusqu'à preuve du contraire",
             "Une radiographie normale n'écarte pas le diagnostic : le scanner est nécessaire",
             "La quantifier — filets, crachats striés, hémoptysie franche — oriente sur l'urgence, pas sur la cause",
             "Une hémoptysie massive est une urgence vitale par asphyxie, non par déglobulisation",
         ]),
        ("Les arguments pour ET contre : ce que l'exercice demande",
         "L'examinateur ne demande pas une liste de diagnostics, mais un raisonnement contradictoire.",
         [
             "Pour chaque hypothèse, un argument qui la soutient et un qui la fragilise",
             "L'absence de fatigue est ici l'argument contre le cancer — et il vaut d'être cité",
             "Un différentiel énoncé sans argument ne rapporte rien : c'est l'argumentation qui est notée",
             "Hiérarchiser : le plus probable d'abord, puis ce qui doit être écarté par gravité",
         ]),
        ("La réflexivité, compétence notée à part",
         "Reconnaître ce qu'on n'a pas fait est une compétence clinique, pas un aveu de faiblesse.",
         [
             "La grille attribue explicitement un point à cette reconnaissance",
             "Dans ce cas : a-t-on demandé les sudations nocturnes, la dysphonie, les adénopathies, le statut vaccinal, l'exposition professionnelle ?",
             "Le dire spontanément vaut mieux que de se le voir signaler",
             "En pratique clinique, c'est ce qui déclenche le rappel du patient plutôt que l'erreur silencieuse",
         ]),
    ],
}
