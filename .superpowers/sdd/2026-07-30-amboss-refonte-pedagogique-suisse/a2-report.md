# a2 — balisage sémantique et message-clé, AMBOSS-21 à 40

Branche `refonte-amboss-suisse`, base `856aa5d` (fin du lot a1).

## Statut

**Terminé.** Les 20 grilles sont balisées ; six message-clés ajoutés, sept
écartés. **Les quarante grilles AMBOSS sont désormais balisées.**

| Commit | Contenu |
|---|---|
| `2e10907` | AMBOSS-21 à 25 |
| `138fbc7` | AMBOSS-26 à 30, message-clé de pharyngite sur AMBOSS-30 |
| `af8de6b` | AMBOSS-31 à 35, message-clés sur AMBOSS-26, 32, 33 |
| `da3f452` | AMBOSS-36 à 40, message-clés sur AMBOSS-27, 29, 38, 39 |

## Volet A — balisage

Quatre conteneurs, et rien d'autre : `resume`, `annexe-item annexe-theorie`,
`presentation-section section-mnemo`, `presentation-section section-questions`.
`annexe-dd`, `annexe-expert`, `annexe-scenario` et les versions orales de
`presentation` sont laissés intacts.

**Densité : 1 918 spans pour 17 119 mots visibles, 1/8,93.** Aucune grille en
dehors de 1/8,8–1/9,0. Le lot a1 tenait 1/8,94 ; le corpus german entier 1/8,72,
même métrique.

Onze grilles sans `resume` ni `presentation` (état d'import) — 21, 23, 24, 25,
26, 27, 29, 32, 33, 36, 40 : seul `annexe-theorie` y est balisé, donc sans
dilution possible. AMBOSS-34 porte `resume` et `theorie`, sans `presentation`.

### Ce que la garantie de substitution a attrapé

L'outil refuse d'écrire si le dépouillement des `<span class="c-…">` du nouveau
segment ne redonne pas la chaîne d'origine octet pour octet. **Il a mordu deux
fois**, sur deux altérations muettes du texte :

| Grille | Écart | Nature |
|---|---|---|
| AMBOSS-31 | `NSCLC` → `CPNPC` | traduction spontanée d'un sigle, dans le `resume` |
| AMBOSS-38 | `PEACE & LOVE` → `PEACE &amp; LOVE` | échappement HTML d'une esperluette |

Ni l'une ni l'autre n'aurait été vue par une relecture déclarative ou par
l'assertion d'équilibre des balises. C'est l'argument entier en faveur d'un
contrôle mécanique : la première change un terme médical, la seconde change
l'affichage, et les deux se glissent dans une retranscription attentive.

Le **détecteur à pile** de spans colorés imbriqués n'a mordu **aucune fois** sur
ce lot (cinq fois sur a1). Zéro imbrication résiduelle.

### Deux points de méthode, mesurés

**Calibrage.** Un premier jet spontané sort à 1/6,7–1/7,9, soit environ 1,4 fois
la cible. Le dégonflage se fait par retraits nommément désignés (couleur +
contenu exact du span), sous la même preuve de texte inchangé. Marquer puis
retirer ce qui n'informe plus est plus fiable que viser juste d'emblée.

**Rééquilibrage par conteneur.** La moyenne d'une grille peut masquer deux
conteneurs hors bande : AMBOSS-30 sortait à 1/9,4 avec un `resume` à 1/7,4 et une
`theorie` à 1/11,4 ; AMBOSS-37 à 1/8,4 avec une `theorie` à 1/7,5 et un `resume`
à 1/10,0. Les deux ont été rééquilibrés conteneur par conteneur. Un cas résiste :
le `questions` d'AMBOSS-38 et 39 reste à 1/11,2–1/11,4, parce que c'est de la
prose orale pauvre en termes discrets — le densifier serait du remplissage.

## Volet B — message-clés

**Ajoutés (6 fichiers, 8 grilles)**, en dernier item de l'`images-wrapper`
existant, fichiers référencés sous `cases/img/amboss/` :

| Grille | Fichier | Motif |
|---|---|---|
| AMBOSS-26, 33 | `neuro-message-cle-cephalee-aigue-non-traumatique.png` | 33 : le message nomme l'HSA et impose la PL après imagerie normale. 26 : la vignette est une crise migraineuse, et les points du message (drapeaux rouges avant de conclure à une céphalée primaire, céphalées médicamenteuses, recours au neurologue) sont ceux que la grille note |
| AMBOSS-27, 29 | `general-message-cle-fatigue.png` | les deux grilles portent mot pour mot le « bilan minimal de toute fatigue : FSC, ferritine, TSH, glycémie, CRP/VS » que le message prescrit, et toutes deux une anémie |
| AMBOSS-30 | `orl-message-cle-pharyngite.png` | vignette = pharyngite à SGA ; SGA, critères cliniques, test rapide, indication à l'antibiotique |
| AMBOSS-32 | `nephro-message-cle-uretrite-et-cervicite-simples.png` | vignette = co-infection VPH + Chlamydia ; PCR, bithérapie, dépistage des autres IST |
| AMBOSS-38 | `pied-cheville-message-cle-entorse-de-cheville.png` | même entité ; Ottawa, radiographie, traitement conservateur fonctionnel |
| AMBOSS-39 | `epaule-message-cle-epaule-douloureuse.png` | s'ouvre et se clôt nommément sur la lésion de coiffe |

Deux fichiers servent chacun deux grilles d'une même page SSP : le § 8.3 exempte
explicitement le message-clé du corollaire de non-recouvrement.

**Écartés (7 grilles).** Détail au journal. Les trois cas les plus instructifs :

- **AMBOSS-25** (le plus net) : le message « Gonalgies » affirme qu'en cas de
  gonalgie non traumatique le traitement conservateur suffit, quand la vignette
  est une TVP dont la station note l'anticoagulation.
- **AMBOSS-35** : le message « Dyspepsie et maladie de reflux » cadrerait en
  reflux une brûlure rétrosternale que la station enseigne précisément à ne pas
  lire ainsi (« non soulagée par les IPP = alerte », vignette = angor d'effort).
- **AMBOSS-36** : **révision assumée en cours de lot.** Le commit `138fbc7`
  annonçait le message-clé de la fatigue retenu pour les trois grilles
  « Fatigue ». Vérification faite sur la grille, la station est un bilan
  hépatologique ciblé chez un usager de drogues IV et ne note aucun bilan de
  fatigue. Écarté. « Ni ne contredit » ne suffit pas — le § 8.4 point 3 écarte le
  message hors sujet, pas seulement le message faux.

L'arbitrage le plus discutable est **AMBOSS-40** (Ramsay Hunt vs message-clé
« Vertige ») : deux des trois points du message recoupent réellement le HINTS que
la grille note, et l'écart repose sur le sujet du panneau (le tri
périphérique/central du vertige) et non sur une contradiction. Écarté, consigné
comme tel.

## Défauts du vault — signalés, ni contournés ni corrigés

**Cinq fichiers à extension mensongère** (PNG nommés `.jpg`) parmi les 290 images
citées par les 17 pages SSP de ces grilles : `general-fatigue-examens-paracliniques.jpg`,
`neuro-tableau-hsa-fischer-grades.jpg`, `neuro-tableau-hsa-wfns-grades.jpg`,
`pulmo-rx-thorax-nodules-bilateraux.jpg`,
`pulmo-rx-thorax-opacite-lobe-superieur-droit.jpg`. Le script les arrête ; aucun
n'est un message-clé, donc aucun n'a bloqué ce lot. Rien touché dans le vault.

**Dix-neuf références cassées**, toutes `Résumé-SSP_page-NNNN.jpg` — catégorie
connue, écartée de toute façon par le § 8.5 a.

## Vérifications

| Contrôle | Résultat |
|---|---|
| `check_invariants.py` | OK, 40 grilles — **`blocks` inchangé** |
| `check_nomenclature.py` | OK |
| `check_reachability.py` | OK, **40/40 à 100 %** |
| `report_redundancy.py` | **147 paires**, inchangé |
| `check_no_loss.py` | **0 item disparu**, contre chaque commit de base |
| `verify_all.py` | **0 anomalie** : texte visible identique hors balisage, 0 span imbriqué ; les six ajouts de message-clé apparaissent comme une insertion unique de 7 lignes |
| `fetch_image.py --corpus amboss --verify` | 8 images, 8 référencées, aucun lien cassé, aucune orpheline |
| german | invariants 88/88, nomenclature, atteignabilité, `--verify` : au vert |
| rescos | invariants 41/41, nomenclature, atteignabilité : au vert |

**Contrôle visuel** — Chrome `--headless=new`, AMBOSS-39 et AMBOSS-33, sombre et
clair, 1200 px et 500 px. Le bootstrap de `cases/theme-sync.js` est **substitué**
avant rendu : il réécrit sinon `data-theme` en `dark` et les deux rendus sortent
identiques. Empreintes des couleurs calculées et **différentes** entre les deux
thèmes sur les deux grilles — la substitution est donc effective, et l'on ne
valide pas un faux. `scrollWidth == innerWidth` aux quatre combinaisons.
Message-clés `complete === true`, aux dimensions du vault (2400×1485 et
2190×1689), affichés pleine largeur de la planche : 1046 px à 1200, 402 px à 500.

## Préoccupations

1. **Le `questions` de deux grilles reste à 1/11,2–1/11,4.** C'est de la prose
   orale, pauvre en termes discrets ; le densifier reviendrait à colorer des
   articulations de phrase. La cible de densité est un bon garde-fou par grille,
   mais elle n'a pas de sens uniforme conteneur par conteneur — un `resume` en
   listes et un `questions` en réponses parlées ne portent pas la même densité de
   termes marquables. Si la métrique devient un critère de recette, il faudra
   la déclarer par type de conteneur, pas par grille.
2. **L'arbitrage AMBOSS-40 mérite une relecture humaine.** Deux points sur trois
   du message-clé « Vertige » correspondent à ce que la grille note ; l'écart
   tient au sujet du panneau. C'est le seul des sept écarts qui ne soit pas
   tranché par le contenu seul.
3. **`annexe-dd` reste sans balisage** sur les 40 grilles, par alignement sur
   german. C'est le bloc le plus long de plusieurs grilles ; l'arbitrage, s'il
   s'ouvre, doit s'ouvrir sur les six corpus à la fois.
4. **Les images préexistantes restent en base64** (37 grilles AMBOSS) — décision
   de l'utilisateur, non touchée. Seuls les six message-clés ajoutés par a1 et a2
   sont en mode référencé. Le corpus est donc durablement mixte, ce que
   `fetch_image.py --verify` signale à chaque passage.
5. **Aucun contrôle visuel n'a été fait sur les grilles sans message-clé du lot**
   au-delà des deux échantillons. Les vingt grilles ne diffèrent des originales
   que par des `<span>` sur des classes CSS déjà exercées par les 88 grilles
   german, mais le contrôle reste un échantillon.
6. **Les cinq fichiers du vault à extension mensongère bloqueront** tout lot qui
   voudra reprendre ces schémas (tableaux de grades HSA de Fisher et WFNS,
   radiographies thoraciques, examens paracliniques de la fatigue). Le total
   distinct sur les 31 pages des 40 grilles n'a pas été mesuré.
