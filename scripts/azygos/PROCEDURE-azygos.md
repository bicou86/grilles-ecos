# Procédure de production du corpus azygos

Le corpus azygos ne s'enrichit pas depuis le vault Obsidian comme `amboss` ou
`german` : il est **produit intégralement** depuis le mode apprentissage
d'[azygos.ch](https://azygos.ch), plateforme suisse d'entraînement ECOS. La
chaîne va de l'extraction navigateur jusqu'à l'intégration dans `index.html`.

Droits d'usage : l'extraction se fait depuis un compte personnel, pour un usage
personnel. Vérifier que c'est toujours le cas avant toute reconstruction.

## Vue d'ensemble

```
navigateur authentifié
   └─ extract.js  ───────────────►  .azygos-extraction/<uuid>.json   (NON versionné)
                                         │
                     build_grid.py ◄─────┤  (+ téléchargement des images)
                                         │  │
                                         │  └─►  cases/azygos/AZYGOS-N_-_….html
                                         │       cases/img/azygos/*.jpg
                                         │
                  fige_azygos.py ◄───────┘
                        └─────────────►  docs/azygos-grilles/<uuid>.json  (VERSIONNÉ)
                                              └─► chaîne des mémentos
```

**Deux consommateurs, deux sources, et l'étape 6 est obligatoire.**
`scripts/azygos/` lit l'extraction brute, parce qu'il a besoin des images. La
chaîne des mémentos (`scripts/memento/`) lit `docs/azygos-grilles/`, le miroir
versionné : le dépôt ne doit pas dépendre d'un dossier que `.gitignore` exclut.
Une ré-extraction qui oublie l'étape 6 laisse les deux sources divergentes —
`check_azygos.py` le détecte, mais **seulement sur une machine qui a les deux**.

## 1. Session authentifiée

Le profil Chrome piloté par `chrome-devtools-mcp` est distinct du navigateur
quotidien : il faut s'y connecter une fois. Le cookie persiste ensuite.

```
navigate_page  https://azygos.ch/fr/app/library
```

Si la page redirige vers `/fr/login`, se connecter manuellement dans la fenêtre.

## 2. Rafraîchir l'inventaire

`scripts/azygos/inventaire.json` liste les 49 cas (id, titre, cadre, patient,
spécialité, format, difficulté). Il fixe aussi la **numérotation AZYGOS-N**,
qui suit l'ordre alphabétique de la collection en ligne. Ne pas réordonner ce
fichier : les numéros sont des identifiants stables, référencés par les liens
de simulation et par la progression enregistrée côté navigateur.

Pour le régénérer, parcourir `/fr/app/library` en mode « Tous » et relever les
liens `/app/library/<uuid>` sur les trois pages.

## 3. Extraire un cas

```
navigate_page    https://azygos.ch/fr/app/learning-mode/<uuid>
evaluate_script  extract.js          → .azygos-extraction/<uuid>.json
```

Trois pièges, tous traités dans `extract.js` :

- **dialogue d'accueil.** Une présentation du format du poste s'ouvre au
  chargement et intercepte les clics. Tant qu'il n'est pas refermé, certains
  onglets restent inatteignables — et l'échec est SILENCIEUX : on obtient
  simplement moins de données. C'est ce qui avait tronqué quatre cas lors de la
  première campagne d'extraction. `fermeIntro()` le referme d'emblée.

- **onglets à deux niveaux.** « Infos du cas », « Préparation » et « Tableau de
  bord » forment le niveau haut ; les onglets cliniques ne vivent que sous
  « Tableau de bord ». Il faut y repasser avant chacun d'eux.
- **libellés variables.** Selon le format du poste : « Statut clinique »,
  « Status clinique », « État clinique », « Examen clinique », ou préfixés
  « Partie 1 / … ». Le script découvre les onglets au lieu de les présupposer ;
  `lib_azygos.classe_onglet()` les range ensuite par mot-clé. 30 libellés
  distincts sont attestés sur les 49 cas.

### Informations complémentaires

Beaucoup d'items portent un bouton « Information complémentaire » dont la bulle
justifie l'item : pourquoi poser cette question, ce qu'oriente telle réponse.
Ce texte est présent dans la charge utile client mais n'est rendu qu'à
l'ouverture du popover — il faut donc les ouvrir un par un (≈ 40 par cas,
1 951 sur le corpus). 90 ms suffisent, avec une seconde passe à 300 ms pour les
retardataires.

Le déclencheur est un **frère** du bloc de texte de l'item, pas un enfant :
`extract.js` remonte d'un cran, avec une garde sur le nombre de libellés pour ne
pas happer l'item voisin.

**Les en-têtes de sous-groupe ont leur propre bouton**, distinct de ceux de
leurs enfants : il justifie le bloc entier (pourquoi explorer la dynamique
temporelle) là où celui d'un enfant justifie un item précis (pourquoi demander
la date de début). Sur 2 191 justifications, 270 sont de ce niveau, réparties
sur 45 des 49 cas. Ne pas les confondre avec les enfants : un en-tête dont la
justification manque signale un défaut de rattachement, pas une absence.

Ces textes alimentent deux rendus. **Vignette** ⓘ : collée au critère pour un
item, collée au nom du sous-chapitre — et affichée sur son seul premier enfant —
pour un en-tête. **Annexe** « Raisonnement clinique — pourquoi chaque item
compte » : les justifications de sous-chapitre y précèdent celles de leurs
items, marquées d'un filet à gauche. La duplication vignette/annexe est voulue :
la première sert pendant la cotation, la seconde à la relecture et à
l'impression (la vignette est masquée à l'impression).

### Colorisation sémantique

Les sections pédagogiques portent la grille à huit couleurs du dépôt
(`c-red` pathologie · `c-pink` symptôme · `c-green` examen · `c-blue`
commentaire · `c-amber` traitement · `c-purple` facteur de risque ·
`c-orange` complication · `c-yellow` concept-clé surligné), comme les six
autres corpus. Les classes sont déjà définies dans les feuilles partagées et
les grilles azygos les chargent : **rien à injecter**, contrairement à
`rescos-locales` et `casecos` qui passent par `scripts/inject_semantic_css.py`.

Les règles vivent dans `scripts/azygos/lexique_semantique.py`. Un lexique, et
non une passe manuelle, parce que les grilles sont régénérées : toute couleur
posée à la main serait écrasée à la reconstruction suivante.

Trois pièges du lexique, tous traités :

- **frontières de mot.** Sans `\b`, et avec `re.I`, « CT » se retrouve dans
  « conta**ct** » et « AINS » dans « cert**ains** ».
- **faux amis morphologiques.** Le suffixe `-ite` attrape « nécessite »,
  « réduite », « décrite », « orbite » ; `-ose` attrape « chose », « dose ».
  Ils sont exclus nommément dans `EXCLUS` — élargir cette liste est le premier
  réflexe si une couleur paraît absurde.
- **`re.I` annule les contraintes de casse.** La règle des éponymes
  (« signe de Murphy ») exige une initiale majuscule pour se distinguer de
  « indice d'une baisse… » ; il faut le drapeau localisé `(?-i:[A-ZÀ-Ý])`.

La colorisation ne touche QUE les annexes. Dans la grille notée elle
parasiterait le codage couleur du score (`score-0/1/2`, `lacune-*`) posé par
`scoring.js` — `check_invariants.py` échoue si un span fuit hors des annexes.
Les bulles de vignette restent en texte simple : sur leur fond violet foncé,
un rouge #ff6369 serait illisible.

### Images

Les URL d'images sont **signées et expirent en une heure**. Elles ne figurent ni
dans le HTML rendu par le serveur ni dans la charge utile RSC : seule
l'ouverture de l'aperçu révèle l'original pleine résolution. Construire la
grille sans tarder après l'extraction — passé le délai, `build_grid.py` se
rabat sur le fichier local s'il existe, sinon l'image est perdue et il faut
réextraire.

## 4. Construire

```bash
python3 scripts/azygos/build_grid.py <uuid> <numero>   # un cas
python3 scripts/azygos/build_all.py                    # tout ce qui est extrait
python3 scripts/azygos/build_all.py --liste            # état d'avancement
```

Contrat de conversion : **un groupe Azygos devient un critère noté, un item
devient un détail à 1 point.** Les quatre sections sont à 25 %. Les dimensions
OFSP alimentent la section communication, notées A–E ; `scoring.js` mappe
`{A:4, B:3, C:2, D:1, E:0}`, ce qui reproduit exactement l'échelle 0–4
d'Azygos.

Les items porteurs de `nbEnfants > 0` sont des en-têtes de sous-groupe : leur
valeur n'est que la concaténation des items suivants. `lib_azygos.aplatit()`
les retire et préfixe leurs enfants, pour ne compter aucun point deux fois — en
reportant au passage leur justification sur le premier enfant.

`nbEnfants` est déduit du nombre de libellés présents dans le conteneur : sur
des sous-groupes imbriqués il **surestime** (un cas déclare 13 enfants pour un
seul item suivant). L'aplatissement s'arrête donc au premier en-tête rencontré
plutôt que de l'avaler, et rend un en-tête sans enfant exploitable comme un item
ordinaire. Sans cette prudence, la justification de l'en-tête avalé disparaît
sans le moindre message.

## 5. Contrôler

```bash
python3 scripts/azygos/check_invariants.py
```

Vérifie que chaque cas a une anamnèse et une communication, que la somme des
coefficients vaut 1, que le maximum de communication vaut bien 4 × le nombre de
dimensions, qu'aucun détail n'est orphelin de son critère et que la chaîne
`scoring.js` / `persistence.js` est complète.

Trois contrôles portent sur les justifications et leur colorisation : **toute information extraite
doit être rendue** quelque part (le compte des clés non rendues doit être nul),
le nombre de vignettes doit égaler celui des entrées d'annexe, et aucun span
`c-*` ne doit apparaître hors des annexes. Ce sont les seuls garde-fous contre
une perte silencieuse à l'aplatissement et contre une couleur qui déborderait
sur le barème.

Les cas signalés « pas d'examen clinique » sont informatifs : certains postes
standards sont de purs entretiens (anxiété, troubles du sommeil), et les postes
de communication comme les téléconsultations n'ont par construction pas
d'examen physique.

## 6. Manifeste et intégration

```bash
python3 scripts/azygos/build_manifest.py   # cases/img/azygos/MANIFEST.tsv
python3 scripts/azygos/inject_index.py     # onglet, styles, cartes, JS
```

`inject_index.py` est idempotent : le bloc HTML est délimité par
`<!-- azygos:début -->` / `<!-- azygos:fin -->` et remplacé à chaque exécution ;
les trois ajouts JavaScript sont gardés par un test de présence.

## 7. Rafraîchir la source versionnée des mémentos

**Obligatoire après toute ré-extraction**, sans quoi les mémentos continuent de
se construire sur l'ancien contenu :

```
python3 scripts/memento/fige_azygos.py     # → docs/azygos-grilles/<uuid>.json
python3 scripts/memento/check_azygos.py    # fidélité brut ↔ miroir
python3 scripts/memento/build_memento.py   # les 88 mémentos
```

`fige_azygos.py` ne recopie pas le JSON brut : il en **projette** `meta` et,
par onglet, le nom de groupe et le `label` de chaque item — tout ce que
`lire_azygos()` lit, et rien d'autre. Sont laissés dehors les URL signées
(elles portent un JWT, qu'on ne commite pas, et qui change à chaque
extraction), les pavés didactiques, et les `valeurs` — les réponses du patient.

## Interdits

- Ne pas éditer une grille à la main : elle serait écrasée à la reconstruction
  suivante. Corriger le générateur.
- Ne pas renuméroter les cas.
- Ne pas éditer `MANIFEST.tsv` à la main.
- Ne pas ajouter de JavaScript pour les vignettes : le CSS (`:hover` +
  `:focus-within` sur un élément focusable) couvre pointeur, tactile et
  clavier. Le socle clair est dans `cases/case-styles.css`, les surcharges
  sombres dans `cases/mobile-responsive.css` — seul fichier autorisé à porter
  des règles `[data-theme="dark"]`.
- Ne pas colorer à la main : corriger `lexique_semantique.py`, qui s'applique à
  la reconstruction. Une couleur fausse se répare en ajoutant le terme à
  `EXCLUS` ou en précisant la règle, jamais dans le HTML.
- Ne pas recompresser les images déjà présentes : `build_grid.py` traite le
  fichier local comme la source de vérité, une seconde passe dégraderait la
  qualité sans nécessité.
