# Ecosysteme ECOS — Flux pedagogique complet

## Vue d'ensemble

L'ecosysteme ECOS integre trois outils pour un flux pedagogique en 4 etapes :

```
 grilles-ecos            ChatGPT                grilles-ecos           Claude
 +-----------+      +----------------+      +----------------+    +---------------+
 | 1. PREPARER| ---> | 2. SIMULER     | ---> | 3. TRANSCRIRE  | -> | 4. EVALUER    |
 | Consulter  |      | Jouer la       |      | Coller la      |    | Recevoir le   |
 | la grille  |      | station avec   |      | conversation   |    | rapport de    |
 | du cas     |      | Patient ECOS   |      | du GPT         |    | performance   |
 +-----+------+      +-------+--------+      +-------+--------+    +-------+-------+
       |                      |                       |                     |
   cases/*.html     chatgpt.com/g/...     simulation/transcript.html   claude.ai/project/...
```

## Outils externes

| Outil | URL | Role |
|-------|-----|------|
| **Patient ECOS** (GPT) | `https://chatgpt.com/g/g-699864f041888191b3f512be2e0e1834` | Simule le patient standardise |
| **Examinateur ECOS** (Projet Claude) | `https://claude.ai/project/019ca098-3dc7-70ce-b1f0-39244d852d52` | Genere le rapport de performance |

## Architecture des fichiers

```
grilles-ecos/
├── index.html                     # Page d'accueil avec grille de cas + historique
├── exam.html                      # Mode examen blanc
├── cases/
│   ├── case-styles.css            # Styles communs des grilles
│   ├── scoring.js                 # Logique d'evaluation
│   ├── persistence.js             # Sauvegarde auto des reponses
│   ├── srs.js                     # Repetition espacee (SM-2)
│   ├── amboss/                    # 40 cas AMBOSS
│   ├── german/                    # 88 cas German
│   ├── rescos/                    # 41 cas RESCOS
│   ├── usmle/                     # 44 cas USMLE
│   └── triage/                    # 40 cas Triage
├── simulation/
│   ├── launcher.html              # Page de lancement de simulation
│   └── transcript.html            # Soumission de transcription
├── report/
│   └── viewer.html                # Visualisation du rapport
├── js/
│   ├── simulation.js              # Utilitaires simulation (params URL, clipboard)
│   ├── transcript.js              # Construction du prompt evaluateur
│   └── report.js                  # Parsing/sauvegarde des rapports
├── scripts/
│   ├── inject-simulation-buttons.js  # Injection des boutons dans les cas
│   └── clean-injections.js           # Nettoyage d'injections de prompt
└── sw.js                          # Service Worker PWA
```

## Conventions de nommage des cas

Chaque cas suit le format : `{CORPUS}-{N}_-_{Titre}_-_{Description}_-_Grille_ECOS.html`

Exemples :
- `AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS.html`
- `German-42_-_Eruption_cutane_e_-_Grille_ECOS.html`
- `RESCOS-5_-_Douleur_thoracique_-_Femme_65_ans_-_Grille_ECOS.html`

Les corpus disponibles sont : `amboss`, `german`, `rescos`, `usmle`, `triage`

## Structure localStorage

| Cle | Format | Description |
|-----|--------|-------------|
| `ecos_sim_start_{CASE_ID}` | timestamp (ms) | Horodatage de debut de simulation |
| `ecos_transcript_{CASE_ID}_{timestamp}` | string | Transcription de la conversation |
| `ecos_report_{CASE_ID}_{timestamp}` | JSON `{caseId, corpus, caseTitle, report, score, timestamp}` | Rapport de performance sauvegarde |
| `ecos_theme` | `"light"` ou `"dark"` | Preference de theme |
| `ecos_registry` | JSON | Registre des scores par cas |
| `ecos_srs` | JSON | Donnees de repetition espacee |
| `ecos_circuit` | JSON | Etat du circuit d'examen en cours |

## Flux detaille

### Etape 1 — Preparer
L'etudiant consulte une grille dans `cases/{corpus}/{cas}.html`. Chaque grille contient un bouton **"Simuler cette station avec Patient ECOS"** qui mene vers `simulation/launcher.html`.

### Etape 2 — Simuler
`launcher.html` :
1. Affiche les instructions et copie `/start {nom du cas}` dans le clipboard
2. Ouvre Patient ECOS (ChatGPT) dans un nouvel onglet
3. L'etudiant joue la station

### Etape 3 — Transcrire
`transcript.html` :
1. L'etudiant colle la transcription de sa conversation
2. La grille du cas est chargee en panneau lateral pour reference
3. Un clic sur "Obtenir mon rapport" construit le prompt `/evaluer` complet (grille + transcription)
4. Le prompt est copie dans le clipboard et l'Examinateur ECOS (Claude) s'ouvre

### Etape 4 — Evaluer
L'etudiant colle le prompt dans le Projet Claude "Examinateur ECOS" qui genere un rapport en 7 sections avec scoring algorithmique. Le rapport peut ensuite etre colle dans `report/viewer.html` pour visualisation et sauvegarde.

## Ajouter un nouveau cas au flux

1. Creer le fichier HTML de la grille dans `cases/{corpus}/` en suivant la convention de nommage
2. Executer `node scripts/inject-simulation-buttons.js` (idempotent — ne modifie que les fichiers sans bouton)
3. Ajouter la carte correspondante dans `index.html` dans la section du corpus
4. Le cas sera automatiquement disponible dans le flux simulation

## Commandes utiles

```bash
# Injecter les boutons de simulation dans les cas
node scripts/inject-simulation-buttons.js

# Scanner et nettoyer les injections de prompt
node scripts/clean-injections.js
```
