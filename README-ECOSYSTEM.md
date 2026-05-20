# Grilles ECOS — Application d'entraînement

## Vue d'ensemble

`grilles-ecos` est un site statique regroupant **451 grilles d'évaluation ECOS**
(Examens Cliniques Objectifs Structurés / OSCEs) réparties en 6 corpus. Chaque
grille est une fiche de notation interactive autonome : on consulte le cas, on
s'entraîne, puis on coche les critères pour obtenir un score.

Pour une mise en situation interactive, chaque grille propose un lien
**« Simuler cette station avec Patient ECOS »** qui ouvre la station
correspondante dans l'application de simulation externe.

## Simulateur externe

| Outil            | URL                            | Rôle                                                                                       |
| ---------------- | ------------------------------ | ------------------------------------------------------------------------------------------ |
| **Patient ECOS** | `https://ecos-sim.replit.app/` | Application de simulation de patient — dépôt : `https://github.com/bicou86/Simulated-OSCE` |

Le bouton de chaque grille pointe vers la station correspondante via
`https://ecos-sim.replit.app/simulation?station={ID}`. L'`{ID}` est le préfixe
du nom de fichier du cas :

- préfixe = partie avant le premier `_-_` (ex. `USMLE-10`, `RESCOS-9b`) ;
- pour le corpus `triage`, les `_` du préfixe deviennent des espaces
  (`USMLE_Triage_10` → `USMLE Triage 10`) ;
- l'identifiant est encodé en URL (`USMLE Triage 10` → `USMLE%20Triage%2010`).

## Architecture des fichiers

```
grilles-ecos/
├── index.html                     # Page d'accueil : cartes de cas, recherche, statistiques
├── exam.html                      # Mode examen blanc
├── about.html                     # Guide d'utilisation
├── cases/
│   ├── case-styles.css            # Styles communs des grilles
│   ├── scoring.js                 # Logique d'évaluation
│   ├── persistence.js             # Sauvegarde auto des réponses
│   ├── srs.js                     # Répétition espacée (SM-2)
│   ├── amboss/                    # 40 cas AMBOSS
│   ├── german/                    # 88 cas German
│   ├── rescos/                    # 41 cas RESCOS
│   ├── usmle/                     # 44 cas USMLE
│   ├── triage/                    # 40 cas Triage
│   └── casecos/                   # 198 cas CasECOS
├── manifest.json                  # Manifeste PWA
└── sw.js                          # Service Worker PWA
```

## Conventions de nommage des cas

Chaque cas suit le format : `{CORPUS}-{N}_-_{Titre}_-_{Description}_-_Grille_ECOS.html`

Exemples :

- `AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS.html`
- `German-42_-_Eruption_cutane_e_-_Grille_ECOS.html`
- `RESCOS-5_-_Douleur_thoracique_-_Femme_65_ans_-_Grille_ECOS.html`

Les corpus disponibles sont : `amboss`, `german`, `rescos`, `usmle`, `triage`, `casecos`

## Structure localStorage

| Clé              | Format                | Description                           |
| ---------------- | --------------------- | ------------------------------------- |
| `ecos_theme`     | `"light"` ou `"dark"` | Préférence de thème                   |
| `ecos_registry`  | JSON                  | Registre des scores par cas           |
| `ecos_srs`       | JSON                  | Données de répétition espacée (SM-2)  |
| `ecos_circuit`   | JSON                  | État du circuit d'examen en cours     |
| `ecos_case_meta` | JSON                  | Métadonnées des cas (système médical) |

## Ajouter un nouveau cas

1. Créer le fichier HTML de la grille dans `cases/{corpus}/` en suivant la
   convention de nommage.
2. Sous le `<h1>` de la grille, ajouter la barre de simulation :

   ```html
   <div class="simulation-bar">
     <a
       href="https://ecos-sim.replit.app/simulation?station={ID}"
       class="btn-simulate"
       target="_blank"
       rel="noopener"
     >
       &#x1FA7A; Simuler cette station avec Patient ECOS
     </a>
   </div>
   ```

3. Ajouter la carte correspondante dans `index.html`, dans la section du corpus.
