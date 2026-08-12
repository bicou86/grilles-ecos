# Colorisation sémantique — azygos et les 20 grilles sans pédagogie — Design

Date : 2026-08-12 · Statut : **implémenté le 2026-08-12** — lot 1 (azygos 39,1 → 79,6) et
lot 2 (20 grilles sur 20) terminés

Plan d'exécution : `docs/superpowers/plans/2026-08-12-colorisation-semantique.md`

## Résultat final

**Plus aucune grille du dépôt n'est sans contenu pédagogique** (hors les 9 feuilles porte, qui
n'en ont pas par nature). Densité par corpus après travaux :

| corpus | spans / 1000 mots |
|---|---:|
| usmle | 112,8 |
| rescos | 107,8 |
| rescos-locales | 107,3 |
| casecos | 106,9 |
| triage | 106,3 |
| amboss | 97,2 |
| german | 82,8 |
| azygos | **79,6** (était 39,1) |

Deux chantiers non prévus s'y sont ajoutés à la demande : la bascule des 166 grilles de
`rescos-locales` en thème sombre, et le rapatriement des 34 grilles RESCOS-41 à 70 depuis
`rescos-locales` vers `rescos`.

## Problème

La demande initiale était d'« appliquer le code couleur sémantique aux sections pédagogiques
et théoriques de toutes les grilles ». La mesure montre que le travail est déjà fait presque
partout, et que deux poches seulement le justifient.

### Le CSS est en place sur les 666 grilles

Les huit classes `c-red` … `c-yellow` sont définies pour toutes les grilles, par deux chemins :

| Chemin | Corpus | Grilles |
|---|---|---:|
| `<link>` vers `cases/case-styles.css` (socle sémantique, l. 3786) | amboss, azygos, german, rescos, triage, usmle | 302 |
| Bloc injecté dans le `<style>` en ligne par `scripts/inject_semantic_css.py` | casecos, rescos-locales | 364 |

Le bloc injecté porte aussi les variantes `[data-theme="dark"]`. Rien à faire de ce côté.

### La convention de balisage est mesurable, et déjà respectée

Elle n'est écrite nulle part, mais elle est appliquée sans exception :

- **0 span avant la zone pédagogique**, sur les quatre corpus vérifiés (german, amboss,
  triage, usmle). Les critères notés ne sont jamais colorés.
- Dans german, les 22 614 spans se répartissent sur **trois blocs seulement** : `resume`
  (8 788), `theorie` (7 975), `presentation` (5 851). `cloture`, `annexe-dd`, `redflags`,
  `therapy`, `expert` et `scenario` sont à zéro.

### Un seul corpus est en déficit

Densité mesurée sur le bloc `theorie` seul, à périmètre strictement comparable :

| corpus | spans / 1000 mots | grilles avec `theorie` |
|---|---:|---:|
| usmle | 112,8 | 44 |
| rescos | 108,8 | 37 |
| rescos-locales | 107,9 | 139 |
| casecos | 107,0 | 195 |
| triage | 106,3 | 40 |
| amboss | 97,2 | 40 |
| german | 82,8 | 88 |
| **azygos** | **39,1** | **49** |

Le nombre absolu de spans est trompeur et ne doit pas servir de critère : triage a 26 spans
par grille contre 252 pour german, mais ses sections pédagogiques font 228 mots contre 3 243.
Rapporté au texte, triage est **plus** dense que german.

### Le lexique automatique plafonne à ~55 spans / 1000 mots

`scripts/azygos/lexique_semantique.py` repassé sur le texte visible du bloc `theorie` :

| corpus | densité actuelle | ce que le lexique rendrait |
|---|---:|---:|
| azygos | 40,4 | 53,8 |
| usmle | 110,2 | 57,0 |
| german | 64,3 | 36,2 |

Les corpus à 100 et plus n'ont donc pas été colorisés par ce lexique : leur balisage est
éditorial. **Régénérer azygos avec le lexique actuel le porterait à ~54, pas à 107.** C'est la
raison pour laquelle la cible retenue est 70–80 et non l'alignement sur usmle.

### 29 grilles sans aucun span — et sans rien à coloriser

Vérifiées une par une : aucune ne possède `resume`, `theorie` ni `presentation`.

- **9 feuilles porte** — pas de contenu pédagogique par nature. Hors périmètre définitivement.
- **20 grilles** — il manque le contenu, pas le balisage.

| grille(s) | corpus | blocs déjà présents | mots |
|---|---|---|---:|
| Psy-Vignette 1 à 10 | rescos-locales | cloture, annexe-dd | 5 974 – 7 081 |
| Pédiatrie — Enfant 3 ans avec toux · Nourrisson 6 mois avec fièvre | rescos-locales | cloture, annexe-dd, redflags | 6 504 · 6 505 |
| Diabète — Patient avec hyperglycémie nouvelle | rescos-locales | cloture, annexe-dd | 6 985 |
| RESCOS-57 — Ralentissement | rescos-locales | expert, scenario, cloture, annexe-dd, redflags | 6 904 |
| RESCOS-64 — Toux, station double 2 | rescos-locales | — | 6 185 |
| ECOS Diag 1 · 2 · 3 | casecos | — | 5 783 – 5 952 |
| RESCOS-29 — Douleur à la jambe | rescos | expert, scenario, cloture, annexe-dd | 2 065 |
| RESCOS-11 — Chute | rescos | — | **805** |

## Référentiel

La grille de huit couleurs est celle du dépôt (`cases/case-styles.css`, socle partagé) et du
vault Obsidian (`~/Documents/Damien/Medecine/Obsidian/.obsidian/snippets/skills-ecos.css`) :

```
c-red    pathologie / danger        c-pink   symptôme / signe
c-green  examen / normal / score    c-blue   commentaire
c-amber  traitement / médicament    c-purple facteur de risque
c-orange complication               c-yellow concept-clé (fond surligné)
```

**Aucune source externe n'est consultée pour le lot 2.** Le contenu rédigé est dérivé de ce
que la grille porte déjà — critères notés, clôture, diagnostic différentiel — reformulé et
structuré, avec les seuls rappels physiopathologiques nécessaires à la cohérence du texte.
C'est ce qui garantit qu'aucune section pédagogique ne contredira les critères notés de sa
propre grille.

## Périmètre

### Inclus

- **Lot 1** — les 49 grilles `cases/azygos/`, par régénération.
- **Lot 2** — les 20 grilles listées ci-dessus, par rédaction des blocs `resume`, `theorie`
  et `presentation`.

### Exclu

- **german, amboss, rescos, casecos, rescos-locales, triage, usmle** : mesurés entre 82,8 et
  112,8 spans / 1000 mots, au-dessus de la référence. Une passe automatique les
  **appauvrirait** — mesuré : le lexique rendrait 57,0 sur usmle qui est à 110,2.
- **Les 9 feuilles porte** de `cases/rescos-locales/`.
- **Les critères notés**, dans tous les cas. Le balisage reste cantonné aux trois blocs
  pédagogiques, conformément à la convention mesurée.

## Lot 1 — azygos

### Causes du déficit

1. **11 % du texte** du bloc `theorie` est en labels `<strong>`, produits par
   `lib.echappe(label)` dans `rend_theorie` et jamais passés au lexique. Ce sont les intitulés
   cliniques, donc du vocabulaire à haute densité sémantique, écarté par construction.
2. Le texte des `infos` d'azygos est du **raisonnement clinique** (« pourquoi cette question »,
   « ce qu'oriente telle réponse »), moins dense en entités nommées que le texte de résumé
   pour lequel le lexique a été réglé.

### Changements

1. Dans `scripts/azygos/build_grid.py`, `rend_theorie` : passer le label par `lex.colorise()`
   à l'intérieur du `<strong>`, au lieu de `lib.echappe()`.
2. Dans `scripts/azygos/lexique_semantique.py`, ajouter les règles couvrant le vocabulaire du
   raisonnement clinique : verbes d'orientation diagnostique, gradations, seuils, familles
   d'examens. Les règles restent ordonnées du spécifique au général, et toute addition passe
   par la liste `EXCLUS` pour les faux amis.
3. Régénérer par `python3 scripts/azygos/build_all.py`.

### Cible

**70–80 spans / 1000 mots** sur le bloc `theorie`, soit le niveau de german (82,8) et non
celui d'usmle (112,8). Accordée explicitement le 2026-08-12.

Le lexique actuel rend 53,8. L'écart jusqu'à 70 doit être comblé par les labels récupérés et
par les règles ajoutées — c'est une cible, pas un acquis. Si elle n'est atteignable qu'en
colorant des termes que le reste du dépôt laisse en noir, **on s'arrête au niveau le plus haut
obtenu sans empâtement** et on consigne le chiffre. Une densité honnête à 62 vaut mieux qu'un
75 obtenu en colorant « patient » et « examen ».

## Lot 2 — les 20 grilles

### Principe d'architecture

Le contenu est rédigé **en texte brut, jamais en HTML**. Un script unique le passe par
`lex.colorise()`, fabrique le HTML des trois blocs et l'insère avant le marqueur
`<!-- COMMENTAIRE GÉNÉRAL -->`.

Trois conséquences voulues : le contenu se relit sans balises, le balisage sémantique est
produit par la même règle que le reste du dépôt, et une correction se fait dans le texte.

```
scripts/peda/
├── inject_peda_blocks.py     # générique, idempotent : lit, colorise, insère
└── contenu/
    ├── psy-vignette-10.py    # resume / theorie / presentation en texte brut
    └── …                     # un fichier par grille
```

`inject_peda_blocks.py` est idempotent : il porte un marqueur de début et de fin, et une
seconde exécution remplace le bloc au lieu de le dupliquer. Le contrôle de sortie vérifie que
retirer le bloc injecté redonne le fichier d'entrée à l'octet près — même contrat que
`scripts/inject_semantic_css.py`.

### Contrat de blocs

Chaque grille traitée reçoit les trois blocs, au gabarit de RESCOS-70 :

- **`resume`** — Anamnèse, Examen clinique, Examens diagnostiques, Prise en charge, Points
  clés ECOS, Check-list rapide.
- **`theorie`** — sections de fond, une par notion structurante du cas.
- **`presentation`** — checklist mentale, version longue (2–3 min), version express SBAR,
  mnémos, questions probables de l'examinateur avec réponses.

### Déroulé

1. **Pilote** : Psy-Vignette 10 — « Une femme triste ». Choisie parce qu'elle a déjà sa
   clôture et son diagnostic différentiel, donc l'ossature factuelle existe. Validation du
   format **et** du fond par le relecteur avant toute suite.
2. **Les 19 restantes par lots de 5**, avec relecture entre chaque — soit quatre lots de
   5, 5, 5 et 4. RESCOS-11 (805 mots, aucun bloc) ferme la marche : c'est le cas le plus
   pauvre du dépôt, donc le plus exposé à l'invention.

## Invariants techniques

- Le **texte visible des sections notées** est inchangé dans les deux lots.
- Le **barème** est inchangé : ni `maxScores`, ni `coef`, ni `sectionInfo`, ni aucun
  `criteria-row`.
- Le balisage n'ajoute que des `<span class="c-*">` : il **enveloppe** du texte, il n'en
  retire ni n'en modifie aucun.
- Aucun span n'est **retiré**. Les passes sont additives.
- Les trois blocs injectés au lot 2 modifient le champ `blocks` du snapshot des corpus
  concernés (rescos, casecos, rescos-locales). Le snapshot est donc **régénéré**, et son diff
  doit être limité aux grilles effectivement traitées — toute autre ligne modifiée est une
  régression à instruire.

## Vérification

À chaque lot, sur le corpus concerné :

| Contrôle | Attendu |
|---|---|
| `check_reachability.py` | 100 % sur chaque section, aucune grille perdue |
| `check_nomenclature.py` | 0 terme non suisse |
| `check_no_loss.py` | 0 item disparu |
| `check_invariants.py` | vert après régénération du snapshot ; diff limité aux grilles traitées |
| `browser_probe.js --deep` | 0 exception, 100 % après remplissage, registre écrit |
| Mesure de densité avant/après | lot 1 : 39,1 → 70–80 sur `theorie` |

La mesure de densité est réalisée par le même script pour les deux passes, afin que le chiffre
avant et le chiffre après soient comparables.

### Résultat du lot 1 — 2026-08-12

| Contrôle | Résultat |
|---|---|
| Densité `theorie` azygos | **39,1 → 76,6** spans / 1000 mots (2 999 → 6 204 spans) |
| Autres corpus | inchangés, au chiffre près |
| Texte visible | identique sur les 49 grilles |
| Spans imbriqués | 0 |
| `check_invariants.py` azygos | vert |
| Couleurs rendues en navigateur | 837 spans contrôlés sur 5 grilles de 4 corpus, 100 % conformes |

**Deux constats faits en passant, hors périmètre :**

1. `browser_probe.js` rend `0/49` sur azygos — mais il rendait déjà `0/1` sur la version
   d'avant la régénération (commit `56c48f5`). Ce n'est pas une régression du lot. La page se
   charge sans exception ; c'est la lecture du score par le harnais qui échoue sur ce corpus.
2. **Les 166 grilles de `rescos-locales` ne suivent pas le thème sombre.** Elles portent bien
   les règles `[data-theme="dark"]` injectées, mais ne chargent ni `theme-sync.js` ni
   `mobile-responsive.css` : l'attribut n'est jamais posé. Vérifié en navigateur — azygos,
   german et casecos rendent la palette sombre, `rescos-locales` reste en clair.

## Séquencement

1. Lot 1 — azygos : labels, lexique, régénération, portes, mesure. Un commit.
2. Lot 2 — `inject_peda_blocks.py` et le pilote Psy-Vignette 10. Un commit après validation.
3. Lot 2 — les 19 grilles restantes en quatre lots (5, 5, 5, 4), un commit et une relecture
   par lot. RESCOS-11 en dernier.

## Risques

- **Sur-colorisation d'azygos.** Enrichir le lexique pour monter de 40 à 75 double le nombre
  de termes colorés. Le risque est l'empâtement : un texte où tout est coloré ne signale plus
  rien. Atténuation — la mesure de densité est faite après chaque ajout de règle, et la cible
  est un plafond, pas un objectif à dépasser.
- **Effet de bord du lexique sur les autres corpus.** Le lexique est partagé avec la
  génération d'azygos uniquement ; aucun autre corpus n'est régénéré. Mais si un corpus
  l'était un jour, les règles ajoutées s'y appliqueraient. Atténuation — les règles ajoutées
  visent du vocabulaire clinique général, pas des tournures propres à azygos.
- **Invention médicale au lot 2.** C'est le risque principal, et aucun script ne le détecte.
  Atténuation — contenu dérivé de la grille, relecture humaine obligatoire par lot de 5, et
  RESCOS-11 traitée en dernier, quand le format est stabilisé.
- **Contradiction entre pédagogie et critères notés.** Une section qui recommanderait autre
  chose que ce que la grille note est pire que pas de section du tout. Atténuation — la
  rédaction part des critères notés et de la clôture existante, jamais d'une source externe.
