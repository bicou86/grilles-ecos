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
| `annexe-image` | 3 | Légender un schéma (base64, jamais modifié) | Contenu autonome — la légende doit rester lisible **avec** l'image |

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

Et deux propres à ce corpus :

- **Ne pas modifier `redflags` ni `therapy` pour résoudre un doublon** : ils sont du
  niveau 2, c'est le pédagogique qui cède.
- **Ne pas déplacer un `</div>` dans un `criteria-row`** — voir German-84.
