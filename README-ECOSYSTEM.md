# Grilles ECOS — Application d'entraînement

## Vue d'ensemble

`grilles-ecos` est un site statique regroupant **666 grilles d'évaluation ECOS**
(Examens Cliniques Objectifs Structurés / OSCEs) réparties en 8 corpus. Chaque
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
│   ├── casecos/                   # 198 cas CasECOS
│   ├── azygos/                    # 49 cas Azygos (suisses, OFSP)
│   └── rescos-locales/            # 166 cas locaux (dont 9 feuilles porte)
├── manifest.json                  # Manifeste PWA
└── sw.js                          # Service Worker PWA
```

## Conventions de nommage des cas

Chaque cas suit le format : `{CORPUS}-{N}_-_{Titre}_-_{Description}_-_Grille_ECOS.html`

Exemples :

- `AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS.html`
- `German-42_-_Eruption_cutane_e_-_Grille_ECOS.html`
- `RESCOS-5_-_Douleur_thoracique_-_Femme_65_ans_-_Grille_ECOS.html`

Les corpus disponibles sont : `amboss`, `german`, `rescos`, `usmle`, `triage`,
`casecos`, `azygos`, `rescos-locales`

Le corpus `rescos-locales` ne suit pas cette convention de nommage : ses grilles
ont été importées avec leur nom d'origine, en clair et accentué (`Céphalées -
Vignette clinique - Grille ECOS.html`). Seules 33 d'entre elles portent un
préfixe `RESCOS-41` à `RESCOS-70`. Son injection dans `index.html` est
reproductible par `python3 scripts/rescos-locales/inject_index.py`.

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

Pour un corpus **entier**, l'ajout à `index.html` ne se limite pas aux cartes :
le JavaScript doit connaître le corpus, sinon les cartes existent dans le DOM
mais aucun filtre ni compteur ne les voit. Trois points sont concernés —
`getCat()`, le tableau `cats` et l'objet `catLabels`. Le corpus `azygos` les
traite dans `scripts/azygos/inject_index.py`, qui est idempotent.

## Corpus azygos

49 cas suisses extraits du mode apprentissage d'[azygos.ch](https://azygos.ch),
traduits de l'allemand. Particularités :

- la section communication reprend les **4 dimensions de l'Examen fédéral
  (OFSP)**, notées de 0 à 4 — l'échelle A–E du gabarit leur correspond
  exactement ;
- les postes ont des formats variés (poste standard, avec mannequin, de
  communication, consultation téléphonique, raisonnement clinique, présentation
  de cas, double poste) ; certains n'ont pas d'examen physique, ce qui est
  attendu et non un défaut d'extraction ;
- 43 images cliniques (photos, échographies, radiographies, CT) sont embarquées
  en base64 et tracées dans `cases/img/azygos/MANIFEST.tsv` ;
- **2 191 justifications cliniques** (« pourquoi cet item ») sont rendues deux
  fois : en vignette ⓘ au survol, et en annexe « Raisonnement clinique ». 270
  d'entre elles portent sur un sous-chapitre entier (« Dynamique temporelle »)
  plutôt que sur un item isolé, et s'affichent collées à son nom. Les classes
  `.info-vignette*` et `.detail-sous-groupe` sont propres à ce corpus mais
  vivent dans les feuilles partagées, sans JavaScript ;
- les annexes portent la **grille sémantique à huit couleurs** commune aux sept
  corpus (3 667 termes colorés), posée par `scripts/azygos/lexique_semantique.py`
  à la génération — jamais à la main.

Voir `scripts/azygos/PROCEDURE-azygos.md`.
