# Procédure de traitement d'une grille German

Corpus : `cases/german`, **88 grilles**. Outillage : `scripts/german/`.

Ce document est le pendant de `scripts/amboss/PROCEDURE.md` pour le second corpus.
Il ne le remplace pas : tout ce qui n'y est pas redit **reste valable tel quel**, en
particulier la hiérarchie à trois niveaux (§ 4 ci-dessous), la règle du format, et la
règle « le dédoublonnage ne perd jamais d'information ».

---

## 0. Ce qui change par rapport à AMBOSS, en une page

| | AMBOSS | German |
|---|---|---|
| Grilles | 40 | **88** |
| Blocs existants | `annexe-dd`, `resume`, `expert`, `theorie`, `presentation` | `annexe-dd`, `redflags`, `therapy`, `resume`, `presentation`, `annexe-image` |
| `annexe-expert` / `annexe-theorie` / `annexe-scenario` | 40/40 | **0/88 — n'existent pas** |
| Un bloc peut apparaître plusieurs fois | non | **oui** (78 `annexe-dd` en 77 grilles, 126 `therapy` en 44) |
| Fin de la zone pédagogique | `<div class="annexe-item annexe-scenario">` | `<!-- COMMENTAIRE GÉNÉRAL -->` (88/88) |
| Sections notées | 4 à 25 % | **identiques** |
| `window.caseConfig` | 40/40 | **88/88, même forme** |

Conséquence pratique : **`lib_amboss.BLOCKS` transposé tel quel ne verrait que trois
des six blocs**, et manquerait `therapy` (44 grilles), `redflags` (10) et
`annexe-image` (9).

---

## 1. Situer les blocs — lecture ciblée, jamais le fichier entier

```bash
python3 -c "
import sys; sys.path.insert(0,'scripts/german'); import lib_german as lib
p=[g for g in lib.grids() if 'German-N_' in g.name][0]
h=lib.strip_base64(p.read_text(encoding='utf-8'))
for nom,_,_ in lib.BLOCKS:
    for a,b in lib.block_spans(h,nom):
        print(f'{nom:14s} offset={h[:a].count(chr(10))+1:5d}  limit={h[:b].count(chr(10))-h[:a].count(chr(10))+1:4d}')
"
```

`offset` et `limit` se passent directement à `Read`. **Ne jamais lire le fichier
entier** (jusqu'à 2,8 Mo, dont ~95 % de base64).

`peda_bounds()` et `dd_bounds()` existent aussi, avec la même convention d'index
qu'AMBOSS, mais ils ne couvrent que la fiche de fin de page et le premier
`annexe-dd`. **La commande ci-dessus est celle qui couvre tout**, y compris les
`therapy-section` dispersées au fil de la section Management.

---

## 2. Les six blocs, leurs bornes, leur rôle

Les bornes ne sont **pas** posées par un motif de fin : `block_spans()` procède par
**équilibrage strict des `<div>`**. Le corpus est globalement équilibré (0 écart
entre `<div>` et `</div>` sur les 88 grilles), et l'équilibrage ne peut pas se
tromper de borne quand un bloc en contient un autre — ce que le motif de fin
d'AMBOSS ne garantit pas. Le motif de fin est conservé dans `BLOCKS` comme **queue
attendue** : `bounds_anomalies()` vérifie qu'elle suit bien la fin équilibrée, et
`check_invariants.py` en fait un invariant. Relevé de référence, 251 segments,
**0 anomalie** :

| Bloc | Début | Fin équilibrée suivie de | Segments / grilles |
|---|---|---|---|
| `annexe-dd` | `<div class="annexe-item annexe-dd">` | `<div class="criteria-row"` (m3 ×74, m2 ×2, m4 ×2) | 78 / 77 |
| `redflags` | `<div class="redflags-section">` | `<div class="criterion-comment-section"` | 10 / 10 |
| `therapy` | `<div class="therapy-section">` | `therapy-section` suivante (82) ou `criterion-comment-section` (44) | 126 / 44 |
| `resume` | `<div class="resume">` | `<div class="annexes">` | 14 / 14 |
| `presentation` | `<div class="presentation-patient">` | `images-wrapper` (3) ou `<!-- COMMENTAIRE GÉNÉRAL -->` (10) | 13 / 13 |
| `annexe-image` | `<div class="annexe-item"` (+ `data-image-id`) | item suivant, ou `<!-- COMMENTAIRE GÉNÉRAL -->` | 10 / 9 |

**Où ils vivent.** `annexe-dd` est un **frère** du `criteria-row` qui le précède (et
non son contenu, comme dans AMBOSS). `redflags` et `therapy` sont **à l'intérieur**
du `criteria-row`, juste après le `criteria-text` du critère qu'ils documentent.
`resume`, `presentation` et `annexe-image` sont en fin de page ; `presentation` et
`annexe-image` vivent dans le conteneur `<div class="annexes">` (20 grilles, dont
German-24 où il est **vide** — coquille sans contenu).

### Contrat de rôle

| Bloc | Niveau | Rôle exclusif | Ne porte jamais |
|---|---|---|---|
| `redflags` | 2 — corrigé de la section notée | Énumérer les signaux d'alarme que le critère attend | Conduite thérapeutique, différentiel |
| `therapy` | 2 — corrigé de la section notée | Détailler la prise en charge que le critère attend | Différentiel, formulation orale |
| `annexe-dd` | 2/3 — commentaire du critère « diagnostics différentiels » | **Raisonner le différentiel** : hypothèses, arguments pour/contre, examen qui départage | Check-list actionnable, conduite de station, formulation orale |
| `resume` | 3 | Réviser vite — **source canonique** | Redites, formats oraux |
| `presentation` | 3 | Restituer à l'oral | Toute donnée clinique nouvelle |
| `annexe-image` | 3 | Légender un schéma (fichier référencé sous `cases/img/german/`, jamais modifié — § 8.6) | Contenu autonome — la légende doit rester lisible **avec** l'image |

**Deux rôles absents d'AMBOSS.** `redflags` et `therapy` sont le corrigé du critère
qui les héberge : ils font partie du **niveau 2** de la hiérarchie, pas du niveau 3.
Conséquence directe pour le dédoublonnage : quand un item de `resume` ou de
`presentation` double un item de `therapy` ou de `redflags`, **c'est le pédagogique
qui cède**, jamais le corrigé — même règle qu'une divergence avec un `criteria-text`.

**`annexe-dd` n'est pas noté.** Il ne contient aucune case à cocher ; le
`<input type="radio">` du `criteria-row` voisin appartient au critère, pas au bloc.
Y toucher ne peut pas déplacer le barème — mais les bornes doivent rester exactes,
sous peine d'emporter le critère voisin.

**Interdit spécifique : `redflags` et `therapy` sont dans un `criteria-row`.** Toute
édition doit rester à l'intérieur du bloc. Un `</div>` mal placé y déplacerait la
fermeture du `criteria-row` et casserait le rendu de tous les critères suivants —
défaut déjà présent en German-84 (§ 6).

---

## 3. La hiérarchie à trois niveaux reste applicable telle quelle

`scripts/amboss/PROCEDURE.md` § 4 :

| Niveau | Situation | Autorité |
|---|---|---|
| 1 | La page SSP tranche explicitement | **La page SSP fait foi** |
| 2 | La page SSP est générique **et** le pédagogique contredit la section notée | **La section notée fait foi** |
| 3 | Ni l'une ni l'autre ne tranche | Laisser inchangé, consigner. **Ne rien inventer** |

**Elle s'applique sans adaptation.** Elle départage des **sources** — page SSP,
section notée, pédagogique — et ne dit rien de la façon dont le pédagogique est
découpé en blocs. Que German ait six blocs au lieu de cinq, qu'ils portent d'autres
noms, qu'ils se répètent dans une même grille : rien de tout cela ne touche à
l'ordre des trois autorités. Le barème reste gelé dans les trois cas.

Le seul point à préciser pour ce corpus est celui du § 2 ci-dessus : `redflags` et
`therapy` **appartiennent au niveau 2**. Une divergence entre eux et le pédagogique
se tranche en leur faveur ; une divergence **à l'intérieur** d'eux se consigne, elle
ne se corrige pas — c'est de la section notée.

Rappel qui vaut ici aussi : la hiérarchie n'arbitre qu'entre **sources
divergentes**. Une erreur factuelle interne à un bloc, que rien d'autre ne
contredit, se corrige directement. Le niveau 3 protège une formulation défendable,
pas un fait faux.

---

## 4. Dédoublonner

```bash
python3 scripts/german/report_redundancy.py German-N_          # paires inter-blocs
python3 scripts/german/report_redundancy.py German-N_ --intra  # + paires intra-bloc
```

Seuil et unité identiques à AMBOSS (`SequenceMatcher(...).ratio() > 0.72`, paires
inter-blocs par défaut) : les deux corpus se lisent dans le même langage. **Le
comportement par défaut ne doit pas changer.**

Mesure initiale (HEAD `9382830`) : **83 paires inter-blocs**, concentrées sur les
15 grilles qui portent au moins deux blocs de fin de page ; 638 paires intra-bloc.

La redondance de ce corpus n'a **pas** le même moteur que celle d'AMBOSS : 62 des
83 paires sont `resume ↔ presentation`, c'est-à-dire le seul couple de blocs
pédagogiques qui existe ici. Les 14 grilles à `resume` sont donc l'essentiel du
travail de dédoublonnage ; les 63 grilles à `annexe-dd` seul n'ont aucun doublon
inter-blocs possible.

**Le dédoublonnage ne perd jamais d'information** (règle inchangée). Vérifier avant
commit :

```bash
python3 scripts/german/check_no_loss.py HEAD German-N_
```

Rapport, pas test : sortie 0 même quand il signale des disparitions. Ne jamais le
câbler comme porte bloquante.

---

## 5. Vérifier

```bash
python3 scripts/german/check_invariants.py     # doit sortir OK
python3 scripts/german/check_reachability.py   # doit sortir OK
python3 scripts/german/check_nomenclature.py   # 64 termes au départ, doit tomber à 0
python3 scripts/amboss/check_invariants.py     # AMBOSS ne doit jamais bouger
python3 scripts/amboss/check_reachability.py
python3 scripts/amboss/check_nomenclature.py
```

`snapshot_invariants.py` regénère `baseline.json`. **Ne le relancer qu'après avoir
constaté et justifié un changement voulu** : il efface la référence.

Ce que gèle `check_invariants.py` : `maxScores`, `scoreSpans`, `sectionCounts`
(`sectionInfo[].count`), `blocks` (**nom + nombre de segments**), `criteriaCount`,
`detailCount`, `radioCount`, `checkboxCount`. Et ce qu'il exige **vide** :
`boundsAnomalies`, `uncoveredContent` (§ 6).

`check_reachability.py` répond à l'autre question — le barème est-il *juste* ? Il ne
compare à aucun passé : il rejoue `cases/scoring.js` et simule le remplissage
complet. **Les 88 grilles passent à 100 % sur chacune des quatre sections** ; aucune
grille au barème inatteignable dans ce corpus (contrairement à AMBOSS-9).

---

## 6. Pièges — ceux d'AMBOSS, et ce que German y ajoute

**Le chevron nu.** `re.sub(r'<[^>]+>', ...)` avale le texte entre un `<` de seuil
(`Hb < 70 g/L`) et le `>` suivant. `visible_text()` est corrigé et **importé** de
`lib_amboss`, pas recopié — il n'y a qu'une implémentation pour les deux corpus.
German porte **28 chevrons nus dans 21 grilles** (`SpO2 < 94%`, `VEMS < 80%`,
`selles < 3/semaine`…) : le piège est bien réel ici. Le sous-cas résiduel non
traitable — un `<` collé à une lettre — est **absent des 88 grilles** (mesuré).
Le même piège produit aussi des **faux positifs** : avant de déclarer un texte
mutilé, vérifier qu'un chevron nu n'a pas simplement borné la recherche.

**Le base64.** Jamais de `grep` brut pour un contrôle, toujours `strip_base64`
d'abord. L'alphabet base64 fait apparaître par hasard n'importe quelle courte
séquence alphanumérique.

**Les puces textuelles.** `annexe-dd` emploie des `•` et non des `<li>` pour ses
arguments ; `therapy` n'a **ni `<li>` ni** autre structure que des `•` séparés par
des `<br>`. `list_items()` traite la puce comme un séparateur.

**Nouveau piège German : un bloc sans liste ni puce.** `redflags-section` porte ses
54 items dans des `<div class="redflags-text">` — ni `<li>`, ni `•`. Une
`list_items()` transposée telle quelle d'AMBOSS aurait rendu **zéro item** pour ce
bloc : invisible à la redondance comme à `check_no_loss`, avec pour seul symptôme
un chiffre de redondance anormalement bas. C'est exactement la forme qu'avait pris
l'angle mort d'AMBOSS-34. `lib_german.list_items()` reconnaît donc aussi
`redflags-text` et `annexe-description`.

**`sectionInfo[].count`.** Ce champ échappait à tout snapshot et rendait le barème
d'AMBOSS-9 inatteignable. Il est capté ici aussi (`sectionCounts`).

**L'angle mort du bloc invisible est désormais outillé.** `uncovered_content()`
cherche 43 classes porteuses de contenu rédactionnel **hors** de tout segment de
`BLOCKS` ; `check_invariants.py` échoue si l'ensemble n'est pas vide. C'est ce
contrôle qui a fait apparaître `therapy-section` et `redflags-section`, qu'une
transposition naïve de `BLOCKS` laissait invisibles. Il ne couvre que des classes
**connues** : une classe entièrement nouvelle lui échapperait encore. Relevé de
référence : **0 occurrence hors bloc sur les 88 grilles**.

**Angle mort assumé : les items courts.** `list_items(min_len=18)` écarte les items
de moins de 18 caractères normalisés — « 1. Âge > 50 ans » en fait 12. C'est le seuil
d'AMBOSS, conservé pour que les deux mesures soient comparables ; il implique qu'un
item court peut disparaître sans que `check_no_loss.py` le signale.

**Anomalie structurelle connue : German-84.** Le `criteria-row` du critère `m7`
englobe **quatre `criteria-row` suivants** — un `</div>` manquant localement,
compensé plus loin (le fichier reste globalement équilibré, et
`check_reachability.py` passe). Seule grille du corpus dans ce cas. Ne pas éditer
cette zone sans reconstruire l'imbrication ; le défaut est mesuré, pas corrigé.

---

## 7. Défauts d'import — mesurés, non corrigés

```bash
python3 scripts/german/report_import_defects.py [German-N_] [--quiet]
```

Rapport, sortie 0. Les détecteurs sont **validés** : rejoués sur `cases/amboss` au
commit qui a introduit les grilles, ils retrouvent les défauts documentés (13 plages
coupées, 2 fragments en `x`, 10 troncatures de molécule, 8 numérations en unité
implicite dont « GB 8500 » et « éosinophiles > 300 »). Leur silence sur German est
donc une information, pas une panne.

| Famille | AMBOSS (avant correction) | **German** |
|---|---|---|
| Plages / décimales coupées (`500-: 1000 mg`) | 13 | **0** |
| Fragment orphelin en `x` (`: ximale`) | 2 | **0** |
| Molécule tronquée (`Amo: 2g IV`) | 10 | **0** |
| Signe de comparaison manquant (`SpO2 92%`) | 29 (bruité) | **0** (2 faux positifs : `IMC 29 kg/m²`, valeurs de patient) |
| Numération en unité implicite (`GB 8500`) | 8 | **0** |
| Chevron nu (piège d'outillage, pas un défaut) | 132 | 28 / 21 grilles |
| Chevron nu collé à une lettre (angle mort résiduel) | 0 | **0** |

**German ne porte aucun des défauts d'import d'AMBOSS.** Les deux corpus n'ont pas
été produits par la même chaîne d'import.

---

## 8. Les images de la page SSP — règle de sélection

Établie sur la grille pilote **German-1 (Abus d'alcool)**, elle vaut pour les 87
grilles suivantes, et pour AMBOSS et RESCOS si le chantier s'y étend. Tous les
chiffres ci-dessous sont **mesurés**, sur les 53 pages SSP qui portent au moins
une des 88 grilles german.

### 8.1 La source : la page SSP, et rien d'autre

**Une image ne se choisit pas dans le vault, elle se prend parmi celles que la
page SSP de la grille cite en `![[nom-de-fichier.png]]`.** C'est la règle de
sourçage qui gouverne tout le projet — le niveau 1 de la hiérarchie (§ 3) dit que
la page SSP fait foi ; elle fait foi aussi pour l'iconographie. Aller chercher
une image ailleurs dans le vault, c'est décider soi-même de ce qui illustre la
station, sans source qui l'autorise.

La page de référence est donnée par `docs/obsidian-mapping.yaml`. Pour lister ce
qu'elle cite, avec la légende que la page pose elle-même sous chaque image :

```bash
python3 - <<'PY'
import re
from pathlib import Path
V = Path("/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian")
page = V / "SSP ECOS/SSP — <Titre exact>.md"
lignes = page.read_text(encoding="utf-8").split("\n")
for i, l in enumerate(lignes):
    m = re.search(r"!\[\[([^\]|#]+\.(?:png|jpe?g|svg))", l, re.I)
    if m:
        suite = lignes[i+1].strip(" >") if i+1 < len(lignes) else ""
        print("%-70s %s" % (m.group(1), suite[:90]))
PY
```

**Le cas « la page ne référence aucune image » n'existe pas dans ce corpus** :
les 53 pages en citent toutes au moins 3 (min 3, p25 8, médiane 12, p75 16,
max 57). La question est donc tranchée par la mesure et non par une préférence :
on ne va **jamais** chercher ailleurs, parce qu'on n'en a jamais besoin. Si une
page future n'en citait aucune, la grille reste **sans image** — et on le
consigne au journal. Une grille sans image n'est pas un défaut ; une image sans
source en est un.

### 8.2 Combien : 2 à 4, cible 3

| Page | Images citées |
|---|---|
| `SSP — Céphalée.md` | 57 |
| `SSP — Douleur Thoracique.md` | 47 |
| `SSP — Dyspnée.md` | 36 |
| médiane des 53 pages | **12** |
| `SSP — Dépendance & Addictions` (German-1) | 18 |

Tout embarquer est exclu (§ 8.6 : 57 images sur une grille, c'est ~6 Mo à servir
et une planche que personne ne lit). **Cible : 3 images par grille ; plancher 2 ;
plafond 4.** Le
plafond n'est pas un quota à remplir : une page dont une seule image passe les
tests du § 8.3 donne une grille à une image, et c'est le bon résultat.

### 8.3 Le critère : la vignette précise, jamais le thème

Une page SSP couvre un **motif de consultation** ; une grille couvre **une
vignette**. Les 57 images de « Céphalée » servent huit grilles différentes ; les
retenir toutes pour chacune reviendrait à recopier la page dans la grille.

Une image n'est retenue que si elle passe **au moins un** des trois tests
suivants, et l'ordre est un ordre de préférence :

| | Test | Ce qui l'ancre |
|---|---|---|
| 1 | **Barème** — l'image documente un critère **noté de cette grille-ci** | un score que l'anamnèse demande de calculer, une manœuvre que l'examen note, un traitement que le management note |
| 2 | **Différentiel** — l'image documente une hypothèse **nommée dans `annexe-dd` de cette grille** | les pages SSP sous-titrent `### Arguments clés — <Diagnostic>` : la sélection devient mécanique, on ne garde que les images logées sous les diagnostics que `annexe-dd` nomme |
| 3 | **Piège** — l'image documente la complication ou le drapeau rouge que la vignette expose | `redflags`, et les « À éviter ❌ » de la page |

Tout le reste est écarté, **même excellent**. Sur les 57 images de « Céphalée » :
les six réflexes ostéo-tendineux, Kernig et Brudzinski, les neuf coupes de TDM
d'hémorragie sous-arachnoïdienne ne sont retenus que par la grille dont
l'`annexe-dd` nomme l'HSA, ou dont l'examen note le méningisme. Pour les autres,
ce sont des images du thème, pas de la vignette.

**Corollaire vérifiable — deux grilles d'une même page ne portent pas la même
sélection**, à l'exception du message-clé (§ 8.4). Vingt-cinq des 53 pages
portent plusieurs grilles ; si les sélections convergent, c'est que le test de la
vignette n'a pas été appliqué et qu'on a sélectionné sur le thème. C'est le
contrôle le plus utile de tout ce paragraphe.

### 8.4 Le message-clé : obligatoire quand il porte sur la vignette, et **un seul**

Le vault porte **49 fichiers `*message-cle*`**, un par dossier thématique.
**24 des 53 pages german** en citent au moins un, ce qui couvre **52 des 88
grilles**. Beaucoup de pages les balisent en plus par `<!-- compas-message -->`
(34 pages, 41 occurrences) — signal secondaire fiable, mais c'est le **nom de
fichier** qui fait foi.

**Règle : quand la page en cite un qui porte sur la vignette, il est
obligatoire**, et il compte dans le budget de 2 à 4 — précision au texte
antérieur (« dès que la page en cite un »), qui omettait la condition et rendait
obligatoire un message-clé hors sujet. Voir German-19 au point 3 : la page en
cite deux, aucun ne porte sur la vignette, et aucun n'est embarqué.

Une page peut en citer plusieurs — mesuré : 19 pages en citent 1, **4 en citent
2**, et **1 en cite 3** (celle de German-1 : tabagisme, alcool, dépendances).
Dans ce cas :

1. Prendre celui dont le sujet est **l'entité de la vignette** — celle que le
   titre de la grille nomme et que l'hypothèse retenue d'`annexe-dd` confirme.
   German-1 s'intitule « Abus d'alcool » : c'est
   `general-message-cle-consommation-d-alcool.png`, pas celui du tabagisme ni
   celui des dépendances, qui appartiennent aux deux autres vignettes que la même
   page dessert.
2. **Jamais deux.** Deux panneaux de messages clés dans une même planche, c'est
   du texte long en image, non sélectionnable, non traduisible, et qui redit ce
   que `resume` porte déjà en HTML.
3. Si **aucun** ne porte sur l'entité de la vignette, n'en mettre aucun et le
   consigner. Un message-clé hors sujet est pire que pas de message-clé : il
   affirme, avec l'autorité du Compas, quelque chose que la station ne demande
   pas — cas rencontré sur **German-19** : la page « Douleur Abdominale » cite
   un message-clé sur le syndrome de l'intestin irritable, quand la vignette est
   une rectocolite ulcéro-hémorragique avec drapeaux rouges. Poser ce
   message-clé aurait affirmé, à tort, qu'aucun examen n'est nécessaire chez ce
   patient. Écarté, et consigné.

### 8.5 Ce qu'on n'embarque pas

**a) Les scans et les pages de PDF converties.** `Résumé-SSP_page-0065.jpg`,
`EM - Résumé-2024_page-0002.jpg`, `Dermato-Résumé.jpg` : **39 fichiers distincts,
41 occurrences** sur les 53 pages. **Écartés par défaut.** Ce n'est pas une
figure mais **une page d'un autre document** : elle apporte sa propre mise en
page, ses propres titres, sa propre hiérarchie, et une résolution calibrée pour
l'impression. Dans une grille, elle se lit comme une capture d'écran de manuel.
Surtout, elle **redit en image ce que `resume` porte en texte** — et le
dédoublonnage ne sait pas la voir : `list_items()` ne lit pas les pixels, donc
la redondance passerait sous le radar au lieu d'être arbitrée.

**Exception, une seule** : quand la page de PDF **est** le schéma, c'est-à-dire
qu'elle ne porte qu'une figure pleine page et rien d'autre — typiquement
`EM_Aide - Algorithme_tabac_1_Cornuz_JacotSadowski_page-0001.jpg`. Elle est alors
traitée comme un schéma ordinaire et légendée comme tel. Ouvrir l'image pour
trancher ; ne pas trancher sur le nom de fichier.

**b) Aucune photographie identifiante de patient — a fortiori mineur.** Même
quand la page SSP la cite et que le critère de pertinence du § 8.3 est rempli.
Un montage de portraits sans annotation n'apporte rien qu'un texte descriptif ne
rende mieux, et le sujet n'a pas consenti à figurer dans une grille pédagogique.
Cas réel : `general-syndrome-de-turner-stigmates-cliniques.jpg`, quinze
portraits face et profil de patientes mineures, cité par la page « Troubles de
la Croissance » et passant le test 3 du § 8.3 (red flag imposant le caryotype)
pour German-72 — écarté à raison malgré cela.

**c) Les références cassées.** **29 des 700 fichiers cités** par les 53 pages
n'existent nulle part dans le vault, dont **28** `Résumé-SSP_page-NNNN.jpg` — la
mesure remplace le chiffre de 36 publié précédemment (2026-08, vérification p4).
Une référence introuvable **arrête le traitement de la grille** ; elle ne se
remplace pas par une image approchante et elle ne s'embarque pas en substituant
un fichier au nom voisin.

**d) Tout fichier de plus de 600 Ko** — § 8.6. **Deux exemptions, sans limite de
taille** : les message-clés que le § 8.4 rend obligatoires, et les images
**désignées nommément par un critère noté** de la grille (un `[Voir <image>]`
dans un `patient-response`, un renvoi explicite du corrigé). Ces deux catégories
sont sourcées par un texte de la grille elle-même, pas par une préférence
éditoriale — c'est ce qui les distingue de tout le reste, toujours plafonné.
**Ces deux exemptions valent aussi pour le budget par grille du § 8.6** : une
règle qui rend une image obligatoire ne peut pas être annulée par un budget qui
la refuse (arbitrage 2026-08, vérification p4 — voir § 8.6).

**e) Les photographies cliniques et les séries radiologiques** quand la vignette
ne note pas leur lecture. Elles pèsent le plus lourd du corpus (jusqu'à 13 Mo
pour un seul fichier) et le test 1 du § 8.3 les écarte presque toujours.

### 8.6 La livraison : fichiers référencés, jamais base64

**Décision arrêtée sur German-1 (2026-08-02) : les images sont servies en
fichiers, sous `cases/img/german/`, et citées par un chemin relatif.** Le base64
est abandonné. C'est déjà le mode des cartes SBAR/SNAPPS servies depuis
`cases/img/` (commit `06b189e`) ; le corpus german s'y aligne.

Mesuré sur German-1, seule grille convertie à ce jour :

| | base64 | référencé |
|---|---|---|
| German-1 | 820 Ko | **132 Ko** (−84 %) |
| les 3 images | dans la grille | 516 Ko dans `cases/img/german/` |

Trois raisons, dans l'ordre où elles ont pesé :

1. **`.git` pèse déjà 435 Mo et `git gc` est interdit sur ce dépôt.** Le base64
   se delta-compresse mal : chaque réédition d'une grille chargée restocke le
   blob entier. En référencé, le texte de la grille et ses images sont deux
   objets distincts — retoucher une formulation ne réécrit plus 700 Ko d'image.
2. **Une image corrigée profite à toutes les grilles qui la citent.** Le
   message-clé d'une page desservant huit grilles est stocké **une fois**, pas
   huit. C'est la déduplication qui fait l'essentiel de l'économie.
3. **Des grilles qui s'ouvrent vite**, y compris en mobile, et un `git diff` de
   grille qui redevient lisible.

**La consigne « poser les images en dernier » est abrogée.** Elle existait pour
ménager `.git` : en base64, retoucher le texte d'une grille imagée réécrivait le
blob entier, images comprises, à chaque passe. En référencé, l'image est un objet
git à part, écrit **une fois** ; éditer la grille ne la retouche plus. Les images
peuvent donc être posées **quand on veut dans le traitement** — au moment où l'on
tient la sélection, sans attendre que le texte soit figé.

Poids des images citées par les 53 pages (664 fichiers trouvés) :

| médiane | p75 | p90 | p95 | max |
|---|---|---|---|---|
| 110 Ko | 208 Ko | 460 Ko | **3 196 Ko** | 13 008 Ko |

La queue est très lourde : **une règle sans plafond n'est pas bornée**. Les deux
garde-fous du § 8.5 d restent en vigueur — **plafond par image 600 Ko**,
**budget par grille 700 Ko de source**. **Le budget par grille s'entend hors
images exemptées** — message-clé rendu obligatoire par le § 8.4, et image
désignée nommément par un critère noté (§ 8.5 d) : les deux mêmes catégories
que celles qui échappent au plafond par image, et pour la même raison. Une
règle qui rend une image obligatoire ne peut pas être annulée par un budget qui
la refuse ; le § 8.5 d ne le disait que pour le plafond par image, ce qui
ouvrait une contradiction avec le budget par grille — tranché ici (2026-08,
vérification p4).

**Révision du plafond (2026-08-02) : 400 Ko → 600 Ko, plus deux exemptions.**
Sa justification d'origine — borner le poids d'un fichier HTML servi en base64
— a disparu avec le passage aux images référencées (ci-dessus) : le plafond ne
borne plus qu'un **stock partagé**, où une image citée par huit grilles ne
coûte qu'une fois, et il continue d'écarter les séries radiologiques et les
scans pleine page que le § 8.3 ne retient de toute façon presque jamais. Sa
valeur de 400 Ko n'avait donc plus de fondement propre ; elle est **portée à
600 Ko**, pour rester ce qu'il est en réalité — un filtre contre les fichiers
aberrants d'un vault dont le p95 est à 3,2 Mo et le maximum à 13 Mo (table
ci-dessus), pas une borne sur un budget de page. Un plafond, quelle que soit sa
valeur, entrait par ailleurs en contradiction avec le § 8.4 (message-clé rendu
obligatoire) et avec un critère noté qui désigne une image nommément : le
§ 8.5 d en exempte désormais ces deux catégories, sans limite de taille, parce
qu'elles sont sourcées par la grille elle-même et non par une préférence
éditoriale.

Estimation du corpus complet à 88 grilles, faite au moment de la décision avec
le plafond alors en vigueur (400 Ko, non révisé depuis) — modèle « message-clé
de la page + (k−1) schémas distincts par grille », k=3 — **220 images
distinctes** pour les 88 grilles :

| sélection | images | poids images | corpus german (8,1 Mo de HTML) |
|---|---|---|---|
| biais bas | 220 | 14,2 Mo | 22,3 Mo |
| **neutre** | **220** | **21,0 Mo** | **29,1 Mo** |
| biais haut | 220 | 41,8 Mo | 49,9 Mo |

**Attendu : ~26 à 29 Mo**, contre ~44 Mo qu'aurait coûtés le base64. La cible de
25,9 Mo retenue au moment de la décision tombe dans cette fourchette.

**Convention de nommage : le nom du vault, normalisé ASCII-minuscules-tirets.**

On **ne préfixe pas** et on **ne renomme pas sur le fond**. Deux mesures le
justifient, sur les 664 images citées par les 53 pages german :

- **Aucun homonyme.** Zéro collision de nom, y compris hors de
  `Skills ECOS/img/` (75 des 664 viennent de `_bibliotheque/`). Un préfixe de
  dossier n'écarterait donc aucun risque réel, alors qu'il allongerait des noms
  qui atteignent déjà 119 caractères — et les noms du vault portent **déjà** leur
  thème (`general-`, `abdo-`, `neuro-`…).
- **La normalisation est l'identité pour 573 d'entre elles (86 %)**, et ne
  produit **aucune collision**. Elle ne réécrit que les 91 noms hérités de
  `_bibliotheque/`, ceux qui portent espaces, accents et majuscules.

Elle n'est donc pas cosmétique, elle règle deux pannes concrètes : un espace ou
un accent dans un `src=` impose le percent-encoding (`%20`, `%C3%A9`), illisible
pour qui édite la grille à la main ; et 7 fichiers sont stockés en NFD par macOS
alors que la page SSP les cite en NFC — même chaîne à l'œil, octets différents,
404 sur tout serveur qui ne normalise pas. Passer en ASCII supprime le piège
définitivement.

Le nom livré et sa provenance sont consignés dans `cases/img/german/MANIFEST.tsv`
(nom, sha256, octets, dimensions, chemin dans le vault) : le renommage reste donc
**traçable**, et l'identité des octets vérifiable après coup.

### 8.7 Comment on l'écrit dans la grille

**L'outil fait la reprise — on ne copie pas une image à la main.**

```bash
python3 scripts/german/fetch_image.py '![[general-score-audit-c.png]]'
# ../img/german/general-score-audit-c.png
#     copie  519x639  Skills ECOS/img/general/13-…/general-score-audit-c.png  112912 octets
```

Il retrouve le fichier dans le vault, contrôle qu'il n'est ni vide ni tronqué, le
copie sous `cases/img/german/` au nom normalisé, met à jour le manifeste, et rend
**le chemin à coller dans la grille**. Il est **idempotent** : une image déjà
reprise est reconnue au sha256 et n'est pas réécrite — deux grilles citant le même
message-clé ne la copient qu'une fois, et aucun blob git nouveau n'est créé.

Il **s'arrête bruyamment** au lieu de livrer quelque chose de faux :

| Cas | Ce qu'il fait |
|---|---|
| référence introuvable (§ 8.5 c) | `ÉCHEC [cassee]`, code de sortie 1, rien n'est copié |
| fichier vide, tronqué, en-tête incohérent | `ÉCHEC [corrompu]` — jamais de fichier vide livré |
| homonyme ambigu | `ÉCHEC [ambigu]` avec la liste des candidats |
| nom déjà pris par un contenu différent | `ÉCHEC [collision]` |
| appariement non exact (NFD/NFC, casse) | copie, mais **avertit** que la page et le disque n'écrivent pas le nom pareil |
| source > 600 Ko | copie, mais rappelle le plafond du § 8.5 d — sauf message-clé ou image désignée par un critère noté (exemptés) |

`--check` diagnostique sans rien copier ; `--verify` vérifie que tous les `src`
des 88 grilles pointent vers un fichier existant, et signale les orphelines.

**Une seule `<div class="annexe-item">` par grille — une « planche » — dans
l'`images-wrapper` existant**, portant N triplets `annexe-title` +
`annexe-description` + `annexe-image` :

```html
<div class="images-wrapper">
<div class="annexe-item">
    <div class="annexe-title">…</div>
    <div class="annexe-description">…</div>
    <div class="annexe-image">
        <img src="../img/german/general-score-audit-c.png" alt="…" />
    </div>
    <div class="annexe-title">…</div>   <!-- image 2, même item -->
    …
</div>
</div>
</div>
```

**Le chemin est `../img/german/<nom>`** — les grilles sont dans `cases/german/`,
les images dans `cases/img/german/` : un seul niveau à remonter, comme
`../img/commcard-sbar.jpg` des cartes de communication.

**Pourquoi une seule et non N.** `BLOCKS` compte les segments `annexe-image` à
partir de `<div class="annexe-item"` : **N items feraient N segments**, donc
`blocks` changerait, donc `baseline.json` serait à re-snapshoter — sur les 88
grilles. L'invariant qui protège les bornes pendant tout le chantier perdrait sa
valeur au moment précis où on en a le plus besoin. Une planche unique le laisse
gelé : German-1 passe de 1 à 3 images avec `annexe-image` toujours à **1
segment**, `check_invariants.py` OK, `baseline.json` non touché. (German-68 porte
deux `annexe-item` — c'est l'état d'import, pas le gabarit.)

**Ne pas poser `data-image-id`** : l'attribut déclenche `width: 49% !important`
et écraserait un panneau de texte de 2040 px dans ~380 px, illisible.

**Octets recopiés tels quels du vault, jamais ré-encodés ni recompressés** — le
sha256 du fichier livré doit être celui du fichier du vault. C'est ce qui rend la
provenance vérifiable après coup ; `fetch_image.py` le vérifie après copie et
l'inscrit au manifeste. Seul le **nom** est normalisé (§ 8.6), et le manifeste
garde le lien avec le nom d'origine.

**La légende décrit ce que l'image montre, pas le titre du fichier.** Elle nomme
le contenu : les colonnes du tableau, les items du questionnaire, les
équivalences de la planche. Elle peut se clore en rattachant l'image à la page
SSP. Elle **n'invente aucun seuil que l'image ne porte pas** — l'AUDIT-C affiche
un score sur 12 et aucun cut-off, la légende n'en cite donc aucun. `alt` reprend
le titre mot pour mot.

**Deux règles CSS posées par le pilote**, dans le socle et non dans la grille :
`.images-wrapper .annexe-image + .annexe-title` (filet de séparation entre deux
légendes de la planche) et `[data-theme="dark"] .images-wrapper .annexe-title`
(le bleu #2c5aa0 tombait à 1,8:1 de contraste sur le fond sombre #273449 ;
#93c5fd le remonte à 7,0:1). Les deux sélecteurs sont restreints à
`.images-wrapper` : 0 collision mesurée sur les six corpus.

### 8.8 L'ordre : la chronologie de la station, synthèse en dernier

Dépistage et quantification → complication à reconnaître → **message-clé en
dernier**. Il est une synthèse, il se lit après ; et c'est le fichier le plus
large (2040 px contre ~520 px pour les schémas), donc le placer en tête
déséquilibrerait la planche. German-1 : AUDIT-C → syndrome de sevrage →
messages clés.

### 8.9 Vérifier

```bash
python3 scripts/german/check_invariants.py    # blocks INCHANGÉ, pas de re-snapshot
python3 scripts/german/check_no_loss.py HEAD German-N_
python3 scripts/german/report_redundancy.py German-N_
python3 scripts/german/fetch_image.py --verify  # aucun src ne pointe dans le vide
```

`--verify` est le contrôle propre au mode référencé : un `src` cassé ne se voit
pas dans le HTML, seulement à l'affichage. Il signale aussi les images
**orphelines** — présentes dans `cases/img/german/` mais citées par aucune grille,
donc du poids mort à retirer — et les grilles restées en base64.

Et au navigateur, thèmes sombre et clair, 1200 px et 500 px : chaque `<img>` doit
avoir `complete === true`, des `naturalWidth`/`naturalHeight` égaux à ceux du
fichier du vault (un fichier tronqué ou un chemin faux rend 0×0), un rapport
largeur/hauteur conservé, et `document.documentElement.scrollWidth` égal à la
largeur de la fenêtre — aucun débordement horizontal.

Chrome sait le faire sans dépendance : injecter une sonde dans une **copie** de la
grille placée dans `cases/german/` (pour que `../img/german/` résolve pareil),
puis `--headless=new --dump-dom`, et supprimer la copie. C'est ainsi que German-1
a été validé : les trois images rendent **au pixel près** ce qu'elles rendaient en
base64 (519×639, 520×368, 2040×1455), aux deux largeurs et dans les deux thèmes.

---

## Interdits

Ceux de `scripts/amboss/PROCEDURE.md`, sans changement :

- Lire un fichier de grille en entier.
- Réécrire un fichier complet — remplacement exact de chaîne uniquement.
- Modifier `.criteria-text` : le format `N. Libellé [réponse]` est requis par
  `cases/scoring.js:159`.
- Retirer les crochets `[...]` des réponses patient (`cases/scoring.js:290`).
- Ajouter ou retirer un sous-item noté.
- Créer un bloc `resume` ou `presentation` absent.
- Supprimer une section sans l'avoir comparée item par item au bloc canonique.

Et quatre propres à ce corpus :

- **Ne pas modifier `redflags` ni `therapy` pour résoudre un doublon** : ils sont du
  niveau 2, c'est le pédagogique qui cède.
- **Ne pas déplacer un `</div>` dans un `criteria-row`** — voir German-84.
- **Ne pas embarquer une image que la page SSP ne cite pas** (§ 8.1), ni
  recompresser ni redimensionner celle qu'elle cite (§ 8.7). Le **nom** est la
  seule chose qui change, par la normalisation du § 8.6, appliquée
  mécaniquement par `fetch_image.py` et consignée au manifeste — jamais un nom
  choisi à la main.
- **Ne pas livrer une image en base64** : mode référencé exclusivement (§ 8.6).
- **Ne pas copier une image à la main** dans `cases/img/german/` : passer par
  `fetch_image.py`, qui seul contrôle l'intégrité et tient le manifeste.
- **Ne pas ouvrir un second `annexe-item` dans l'`images-wrapper`** : `blocks`
  changerait et `baseline.json` serait à refaire sur les 88 grilles (§ 8.7).
