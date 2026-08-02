# Journal CasECOS — août 2026

Branche `refonte-amboss-suisse`. Base de mesure `d0a89f4`. Rien n'a été lu,
écrit ni exécuté sous `cases/german/` ni `scripts/german/` — l'utilisateur y
travaillait en parallèle. Commits `path`-scopés.

**Cinq commits de l'utilisateur ont atterri pendant ce lot** (`260a903` →
`6cd583f`), sur `cases/german/`, `cases/img/`, `cases/rescos-locales/`,
`scripts/german/` et `scripts/rescos-locales/`. **Aucun chevauchement** avec
`cases/casecos/` ni `scripts/casecos/`, vérifié fichier par fichier. Et
`cases/scoring.js`, `cases/persistence.js`, `cases/srs.js` et `index.html` sont
**intacts depuis `d0a89f4`** — les mesures de ce lot restent donc valides telles
quelles.

⚠️ **Le contenu de ce lot est parti dans le commit `4bc9404` de l'utilisateur,
pas dans le mien** (`288894d`, qui ne porte que ce journal). J'avais indexé mes
chemins par `git add` ; **l'index est partagé entre les deux sessions**, et le
`git commit` que l'utilisateur a lancé entre-temps a emporté l'index entier. Mon
`git commit -- <chemins>`, qui n'emporte que les chemins nommés, ne trouvait donc
plus rien à commiter d'autre. **L'arbre est correct** : les 198 grilles de `HEAD`
sont identiques octet à octet à l'arbre de travail (vérifié une par une), les six
scripts y sont, et les portes repassent au vert après coup. L'historique n'a
**pas** été récrit — l'utilisateur commite sur la même branche.

**Règle pour les lots suivants : sur un dépôt travaillé à deux, ne pas indexer.
Commiter en un seul geste par `git commit -- <chemins>`**, qui ignore l'index et
ne peut rien emporter d'autre.

---

## k2 — Bascule des 198 grilles vers `cases/scoring.js`

### Ce qui a été fait

Les 198 grilles de `cases/casecos/` portaient chacune une copie complète du
moteur de calcul, ~726 lignes de JavaScript, avec `maxScores`, `coef` et
`sectionInfo` déclarés en variables locales à `calculateScores()`. Elles
déclarent aujourd'hui un `window.caseConfig` et chargent le moteur partagé.

Chaque grille portait **quatre** blocs `<script>`, dans un ordre invariable —
signature mesurée identique sur les 198. Après bascule :

| bloc | avant | après |
|---|---|---|
| 1 | `<script src="../theme-sync.js">` | inchangé |
| 2 | le moteur embarqué | `window.caseConfig` + `<script src="../scoring.js">` |
| 3 | rappel de `colorPatientResponses()` | **supprimé** |
| 4 | barre de navigation, IIFE | **supprimée** |
| — | — | `<script src="../persistence.js">` ajouté avant `</body>` |

Les blocs 3 et 4 ne sont pas des pertes. Le bloc 3 est la **queue exacte de
`cases/scoring.js`**, aux cinq mêmes lignes près : le garder l'aurait fait jouer
deux fois. Le bloc 4 est le substitut local de `createNavBar()`, que
`scoring.js` appelle désormais : le garder aurait affiché **deux barres de
navigation superposées**. Le `<style>` de `.case-nav-bar` qui le précède est
conservé — les grilles CasECOS ne chargent pas `cases/case-styles.css`, il est
leur seule source de mise en forme pour la barre.

`srs.js` ne reçoit aucune balise, et c'est l'alignement demandé : **aucune
grille du dépôt ne lui en donne** (0/40 AMBOSS, 0/88 German, 0/41 RESCOS, 0/40
triage, 0/44 USMLE). C'est `cases/scoring.js` qui l'injecte lui-même. Vérifié en
navigateur : `script[src$="srs.js"]` présent sur les 198 après bascule, absent
sur les 198 avant.

### Le geste, et pourquoi il était mécaniquement sûr

`scripts/casecos/migrate_to_shared_engine.py`, huit assertions par grille, une
seule qui tombe et la grille reste intacte. Zéro refus sur 198.

Trois mesures préalables ont fondé la sûreté du geste :

1. **Un seul moteur.** Les 198 blocs porteurs de `calculateScores()`, **une fois
   leur configuration retirée**, rendent **une seule empreinte SHA-1**
   (`1435807315a4…`). Ce n'est pas la mesure de K1 — qui neutralisait nombres et
   chaînes — mais une mesure plus forte : ici le texte restant est identique
   **caractère pour caractère** sur les 198.
2. **Ce moteur est `scoring.js` moins six ajouts.** `diff -u` du moteur
   canonicalisé contre `cases/scoring.js` : **205 lignes ajoutées, 6
   remplacées**, aucune supprimée. Les 6 sont les 4 lignes `#missingItems` sans
   garde et les 3 lignes du `DOMContentLoaded` déplacées dans la branche `else`
   du mode circuit.
3. **Une seule forme de configuration.** Les 198 blocs de config, nombres et
   chaînes neutralisés, rendent **une seule forme** : quatre sections
   `anamnese / examen / management / communication`, `scoreId` sur `examen`,
   `isComm` sur `communication`.

Le piège signalé par K1 — `let maxScores = {};` vide précédant l'affectation
réelle — est contourné en cherchant la ligne-repère
`// Configuration pour le format traditionnel` et non `maxScores`.

`scores = {anamnese: 0, …}` n'est pas reporté dans `caseConfig` :
`cases/scoring.js` porte ce littéral en dur (ligne 110) et il est **inerte** —
la boucle affecte `scores[section.key]` avant toute lecture. Le script vérifie
tout de même que la grille porte bien ce littéral-là, et refuse sinon.

### Aucun octet de contenu n'a bougé

Preuve directe, sur les 198 : le fichier **privé de ses blocs `<script>`**,
comparé à sa version `d0a89f4` privée des siens, ne diffère que par
**`'\n    ' → '\n'`** — l'indentation qui précédait le bloc 3 supprimé. Rien
d'autre. Pas un caractère de contenu médical.

Le snapshot le dit champ par champ : `maxScores`, `coef`, `scoreSpans`,
`sectionCounts`, `blocks`, `boundsAnomalies`, `uncoveredContent`,
`criteriaCount`, `detailCount`, `radioCount`, `checkboxCount` — **inchangés sur
les 198**. Seuls trois champs bougent, et ce sont les trois attendus.

### Le défaut que K1 n'a pas vu : une `TypeError` sur les 198

**C'est le résultat le plus important de ce lot, et il n'était pas au mandat.**

K1 concluait : « Aucune ne peut lever de `TypeError`, contrairement à RESCOS-7 et
RESCOS-9. Les neuf identifiants déréférencés sans garde […] sont présents dans
les 198. » Le contrôle en navigateur du miroir de `d0a89f4` dit le contraire :
**les 198 grilles levaient
`TypeError: Cannot read properties of null (reading 'style')` dans
`calculateScores`**, à chaque recalcul — 341 à 503 fois par session de
remplissage complet.

La cause : `#missingItems` et `#missingList` n'existent **que dans un
commentaire HTML** :

```html
<!-- ÉLÉMENTS MANQUANTS (MASQUÉS) -->
<!-- <div class="missing-items" id="missingItems" style="display: none;">
    <h3>Éléments non évalués</h3>
    <div id="missingList"></div>
</div> -->
```

198 grilles sur 198. `engine_defects()` cherchait `id="missingItems"` dans le
**HTML brut** : il le trouvait dans le commentaire, concluait « présent » et
rendait la porte verte. Le navigateur, lui, ne construit pas les commentaires.

Conséquence en cascade, mesurée : la `TypeError` interrompait le gestionnaire
`DOMContentLoaded` **avant** `colorPatientResponses()` et avant l'enregistrement
du `setTimeout` de recoloration. Sur les 198 grilles, la coloration des crochets
ne devait son existence qu'au bloc 3 — le rappel de secours.

**Deux corrections, pas une :**

* le rebranchement sur `cases/scoring.js`, qui **garde** les deux
  déréférencements (`var missingEl = …; if (missingEl) …`), supprime la
  `TypeError` : **198 → 0** exceptions, mesuré en navigateur ;
* `check_reachability.live_dom()` neutralise les commentaires HTML avant toute
  recherche d'identifiant, pour que l'angle mort ne se reforme pas. Contrôle de
  morsure : le contrôle corrigé, appliqué au miroir de `d0a89f4`, rend
  **198/198 en échec** et nomme exactement les deux identifiants que le
  navigateur signalait.

### Outillage — quatre fichiers touchés, chacun pour une raison nommée

| fichier | changement |
|---|---|
| `migrate_to_shared_engine.py` | **nouveau** — le geste, idempotent, sous assertions |
| `snapshot_invariants.py` | lit les deux formes de config ; `engineHash` devient `"shared:scoring.js"` ; `savesToRegistry` cesse de mentir |
| `check_reachability.py` | lit les deux formes ; contrôle le moteur **réellement exécuté** ; `live_dom()` |
| `check_invariants.py` | commentaires des champs gelés remis à jour |
| `PROCEDURE-casecos.md` | §§ 5 et 6 récrits ; § 4 complété |

**`savesToRegistry` mentait des deux côtés.** Sa première rédaction cherchait la
chaîne `saveToRegistry` dans le HTML : elle rendait `false` **avant** la bascule
(moteur embarqué périmé) et aurait rendu `false` **après** (la fonction vit dans
un fichier séparé). Le champ existait pour voir un seul changement et l'aurait
manqué. Il vaut désormais `true` si la grille porte la fonction **ou** charge le
moteur qui la porte.

**`engineHash`.** Sa justification d'origine était explicite : « le pendant, pour
un moteur embarqué, du `git diff` sur `cases/scoring.js` ; ici il n'y a rien à
diff. » Le moteur étant redevenu partagé, `git diff` le couvre de nouveau : le
champ vaut `"shared:scoring.js"` et garde la charge de signaler toute grille qui
en ré-embarquerait un. Contrôle de morsure n° 4 ci-dessous : il mord.

**Les lecteurs de la forme embarquée n'ont pas été supprimés**, ils sont passés
en repli après la forme déclarative. Une grille qui reviendrait en arrière reste
lue — sans quoi elle rendrait un barème vide, indiscernable de « pas de
section ».

### Quatre contrôles de morsure

Le silence d'une porte ne vaut que si elle mord. Chaque contrôle a été cassé
volontairement, puis le fichier restauré à l'octet près.

| perturbation | porte | verdict |
|---|---|---|
| `maxScores.anamnese` 37 → 36 | `check_reachability` | `ÉCHEC`, « global si tout est coché : 101 % » |
| `id="totalScore"` retiré | `check_reachability` | `ÉCHEC`, « déréférencement non gardé vers #totalScore » |
| `count` 8 → 9 | `check_invariants` | `ÉCHEC`, `sectionCounts a changé` |
| `scoring.js` retiré, moteur ré-embarqué | `check_invariants` | `ÉCHEC`, `engineHash` **et** `savesToRegistry` |

### Portes et témoins

| porte | avant | après |
|---|---|---|
| `casecos/check_invariants.py` | rc 0 | **rc 0**, baseline régénéré, 3 champs |
| `casecos/check_reachability.py` | rc 0, 198/198 | **rc 0, 198/198 à 100 %** |
| `casecos/check_nomenclature.py` | rc 1, **649** | rc 1, **649**, sortie **identique octet à octet** |
| `casecos/report_redundancy.py --quiet` | **830** | **830**, sortie **identique octet à octet** |
| `casecos/check_no_loss.py d0a89f4` | — | **0 item disparu** sur 198 grilles modifiées |
| `casecos/report_import_defects.py` | 6 familles | 5 identiques, `chevron-nu` 2414 → 1622 (§ ci-dessous) |
| AMBOSS — 3 portes + redondance | rc 0, **147** | **identiques octet à octet** |
| RESCOS — 3 portes + redondance | rc 0, **127** | **identiques octet à octet** |

**`chevron-nu` : 2414 → 1622, et ce n'est pas du contenu.** Ce rapport balaie le
HTML brut, `<script>` compris. Les 792 disparus sont **exactement 4 par grille ×
198**, mesurés sur une grille témoin (4 → 0) : ce sont les opérateurs `<=` du
moteur supprimé — `for (let i = 1; i <= section.count; i++)` deux fois,
`window.currentSeconds <= 30`, `window.currentSeconds <= 0`. Même phénomène
qu'au lot r7 sur RESCOS (96 → 88). Les cinq autres familles ne bougent pas :
2/2, 5/4, 0/0, 128/56, 26/18.

### Contrôle navigateur — 198 grilles, avant et après, dans la même unité

Chrome piloté par le protocole DevTools, WebSocket natif de Node 22, serveur
statique sur `127.0.0.1`, `--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE
127.0.0.1`. Aucun paquet installé. Le même harnais a été passé sur un **miroir de
`d0a89f4`** servi depuis le scratchpad.

**Contexte de navigation isolé par grille** (`Target.createBrowserContext`) :
aucune course entre ouvriers sur `ecos_registry`, et `registryKeys === 1` prouve
que c'est bien cette grille-là qui a écrit son entrée.

**Navigation par les URL d'`index.html`, jamais par le disque.** C'est le point
qui décide de la validité de la preuve : `saveToRegistry()` indexe par
`location.pathname.split("/").pop()` et `index.html` par
`href.split("/").pop()`. macOS stocke ces noms accentués en **NFD**, `index.html`
les porte percent-encodés en **NFC**. Une énumération du système de fichiers
aurait produit la clé `…Ce%CC%81phale%CC%81es…` là où le tableau de bord attend
`…C%C3%A9phal%C3%A9es…` : la pastille ne serait jamais apparue, et le harnais
aurait mesuré un chemin que l'utilisateur n'emprunte pas.

| | avant (`d0a89f4`) | après k2 |
|---|---|---|
| total = 100 % | 198 | **198** |
| note = A | 198 | **198** |
| **`ecos_registry` renseigné** | **0** | **198** |
| dont `pct: 100, grade: "A"` | 0 | **198** |
| clé du registre = `fileKey` d'`index.html` | — | **198 / 198** |
| réponses restituées après rechargement | 0 | **198** |
| `persistence.js` chargé | 0 | **198** |
| `srs.js` chargé | 0 | **198** |
| **sans exception ni erreur console** | **0** | **198** |
| une seule barre de navigation | 198 | **198** |
| position « N / 451 » affichée | 198 | **198** |
| minuteur 13:00 → 12:5x | 198 | **198** |
| grilles dont le **total** diffère | — | **0** |
| grilles dont la **note** diffère | — | **0** |

**Ce qui rend la preuve du registre concluante** : `ecos_registry` n'est écrit
qu'à **un seul endroit du dépôt**, `cases/scoring.js`, dans `saveToRegistry()`.
Ni `persistence.js`, ni `srs.js`, ni `theme-sync.js` n'y touchent. L'apparition
des 198 entrées ne peut venir que du chargement du moteur partagé.

**Deux relevés ont demandé un verdict, aucun n'est un défaut.**

* **33 grilles perdaient un radio au rechargement** — et gardaient 100 %. Le
  radio perdu est `(sans nom) = on` : une **cale de mise en page**,
  `<div class="checkbox-group" style="visibility: hidden;"><input type="radio"
  disabled />`, sans `name`, sans `value`, sans point. 68 occurrences sur 33
  grilles. Elle n'était cochée que parce que `switchMode()` appelle
  `toggleCheckboxes(false)`, qui met `radio.disabled = false` sur **tous** les
  radios, cale comprise — un candidat, lui, ne peut pas cliquer un élément
  `visibility: hidden`. Remplissage restreint aux éléments **visibles**, les 33
  repassent : **33/33**, donc **198/198**. Défaut du harnais, pas des grilles.
* **3 grilles rendent zéro crochet coloré** — `AMC-Chir5-ECG5 Tumeur
  surrénalienne`, `AMC-Chir5-Vignette2 Goitre de croissance rapide`,
  `Examen physique lombalgie`. **C'est correct** : leurs seuls `[…]` sont des
  sélecteurs d'attribut CSS dans `<style>` (`input[type="radio"]`,
  `.annexe-item[data-image-id]`). Vérifié des deux côtés : **0 avant, 0 après**.
  Même cas que RESCOS-7 au lot r7.

### Un effet de bord assumé : les crochets colorés sont désormais imbriqués ×4

Mesure : 18 crochets → **18 spans avant, 72 après**, en 4 niveaux imbriqués
(`n1=72 n2=54 n3=36 n4=18`). Cause exacte, et elle est instructive :
`colorPatientResponses()` réécrit `element.innerHTML` et son motif
`\[([^\]]+)\]` retrouve le crochet **déjà enveloppé**, donc l'enveloppe à
nouveau. Avant la bascule la fonction ne tournait **qu'une fois** — la
`TypeError` de `calculateScores()` tuait le gestionnaire `DOMContentLoaded`
avant les deux autres appels. Elle tourne maintenant quatre fois, comme prévu.

**Ce n'est pas une régression de ce lot mais le comportement du dépôt entier** :
mesuré sur les témoins, `AMBOSS-1` rend `n1=244 n2=183 n3=122 n4=61` (61
crochets × 4) et `RESCOS-1` `n1=300 n2=225 n3=150 n4=75`. Les 253 grilles qui
chargeaient déjà `scoring.js` empilent les mêmes quatre couches. Le rendu est
identique — même couleur, même graisse — et corriger le motif toucherait
`cases/scoring.js`, donc les quatre corpus. Hors mandat, consigné.

### Ce qui n'a pas été fait

* **Rien sous `cases/german/` ni `scripts/german/`** — ni lu, ni écrit, ni
  exécuté. Les familles de `report_import_defects` y sont importées par le
  mécanisme que K1 a posé, sans ouvrir le fichier.
* **Aucune modification de `cases/scoring.js`**, `persistence.js`, `srs.js`,
  `theme-sync.js`, `index.html` ni d'aucun script partagé.
* **Aucun contenu médical touché** — prouvé octet à octet ci-dessus.
* **Aucune lecture de grille entière avec `Read`** : uniquement des fenêtres de
  lignes ciblées et des extractions programmatiques.
* **Aucun `grep` brut employé comme contrôle** : les chiffres viennent des
  scripts de `scripts/casecos/` ou de mesures Python explicites.
* **Aucune commande réseau, aucun `git push`, aucun `git gc`, aucun `git prune`.**

### Une leçon d'outillage, pour les lots suivants

`git checkout -- cases/casecos/` a **renommé** un fichier de NFD vers NFC
(`core.precomposeunicode` rend les chemins précomposés, APFS les conserve tels
qu'écrits). Le corpus est passé de 138 NFD / 60 ASCII à 137 / 1 / 60 en un
geste, et `baseline.json` a cessé de retrouver la grille par son nom. Restauré,
et vérifié après la bascule complète : **138 NFD + 60 ASCII, 0 NFC**, comme au
départ.

**Sur ce corpus, ne jamais annuler une modification par `git checkout` sur un
chemin accentué.** Sauvegarder les octets et les réécrire.

---

## k3 — Suissification de la nomenclature des 198 grilles

**Statut : terminé, `check_nomenclature.py` au vert.** 132 grilles réécrites,
**889 occurrences** traitées. Aucun contenu médical touché au-delà de la
nomenclature ; le barème n'a pas bougé.

| porte | avant | après |
|---|---|---|
| `check_nomenclature.py` | **649 termes / 123 grilles** | **OK, rc 0** |
| `check_invariants.py` | rc 0 | rc 0 |
| `check_reachability.py` | 198/198 | **198/198 à 100 %** |
| `report_redundancy.py --quiet` | 830 | **832** (+2, expliqué § 5) |
| `check_no_loss.py 566f38d` | — | 17 disparitions, **17 verdictées** (§ 6) |
| AMBOSS 147 / RESCOS 127 | 147 / 127 | **147 / 127, inchangés** |

### 1. Le relevé de k1 était juste, et incomplet

Les **649** termes annoncés par k1 ont tous été traités. Un relevé **indépendant**
— tous les acronymes MAJUSCULES de 2 à 8 caractères du **texte visible** des 198
grilles, `<script>` et `<style>` retirés, **3 563 jetons distincts** jugés un par
un — en a trouvé **220 de plus**, et la substitution de `Coumadin` en a entraîné
**20** autres (`warfarine`). Total **889**.

**Ce que k1 ne pouvait pas voir, et pourquoi :**

* **`pPCI` — 20 occurrences.** Le motif de k1 est `\bPCI\b`. Dans `pPCI`, le
  `p` minuscule est un caractère de mot : il n'y a **pas de frontière** avant le
  `P`. Les 31 `PCI` d'une grille étaient comptés, les 20 `pPCI` de la grille
  voisine ne l'étaient pas. Même famille d'angle mort que la casse des unités
  qui avait déjà doublé le relevé — un motif qui décrit *une* graphie ne voit
  pas les autres.
* **`gold standard` — 20 occurrences de plus que les 76 annoncées.** Le motif
  est sensible à la casse : `GOLD STANDARD` (8), `Gold standard` (4) et
  `gold-standard` (8) passaient au travers. **96 au total.** La sensibilité à la
  casse doit pourtant être **conservée** : c'est elle qui épargne les 3
  `Gold Standards Framework`, nom propre d'un outil britannique d'identification
  des patients palliatifs.
* **`g%` — 2 occurrences.** Graphie archaïque du g/dL (`Hb 16 g%`), dont ni
  `\bg/dL\b` ni `\bg/dl\b` n'est sous-chaîne. Aucun motif d'unité ne la voyait.
* **Neuf numérations sanguines** hors du vocabulaire de
  `report_import_defects.py` : « leucocytose 18'000 », « hyperleucocytose »,
  « Plq 150 », « GR », « Ht », et surtout **`Hb 15.8` sans unité** — un g/dL
  implicite qu'aucune liste de termes hématologiques n'attrape, parce que c'est
  la *valeur* qui trahit l'unité, pas le mot.

### 2. Décompte par famille

**Relevé k1 — 649, tous traités**

| famille | détail | n |
|---|---|---|
| laboratoire et unités | `NFS` 106 · `ng/ml` 39 + `ng/mL` 17 · `g/dl` 24 + `g/dL` 1 · `/mm³` 19 + `/mm3` 4 · `pg/mL` 6 + `pg/ml` 4 · `mg/dl` 5 + `mg/dL` 2 · hémogramme+`/µL` 3 · `mEq` 3 · `lbs` 9 + `livres` 2 | **244** |
| spécialités américaines | `Coumadin` 47 · `Ativan` 13 · `Dilantin` 8 · `Pepto-Bismol` 8 · `Versed` 7 · `Tylenol` 5 | **88** |
| acronymes et institutions | `BMI` 86 · `gold standard` 76 · `HIV` 35 · `MRSA` 33 · `PCI` 31 · `FIT` 16 · `ANA` 9 · `CABG` 8 · `EHPAD` 4 · `IDE` 4 · `PID` 3 · `DMARDs` 3 · `BUN` 2 · `COPD` 1 | **311** |
| urgences | `911` 3 · `SAMU` 3 → **144** | **6** |

**Relevé k3 — 220 de plus**

| famille | détail | n |
|---|---|---|
| acronymes anglophones | `DOAC` 40 · `ERCP` 25 · `MCV` 22 · `pPCI` 20 · `ARDS` 12 · `MCHC` 11 · `ALT` 10 · `AST` 8 · `SNRI` 8 · `LDCT` 8 · `SSRI` 7 · `EUS` 7 · `MCH` 2 · `NPO` 2 · `MRI` 2 · `WHO` 1 · `TTE` 1 · `TEE` 1 · `OTC` 1 · `HCT` 1 | **189** |
| graphies de casse non couvertes | `GOLD STANDARD` 8 · `gold-standard` 8 · `Gold standard` 4 | **20** |
| unités | `g%` 2 | **2** |
| numérations implicites | hors vocabulaire de l'outil | **9** |

**Conséquence d'une substitution : `warfarine` 20**, dans les deux seules
grilles où la molécule était nommée — voir § 3.

### 3. `Coumadin` → `Sintrom®`, et pourquoi pas `Marcoumar®`

Les 47 occurrences sont dans **deux grilles qui sont le même cas** : méléna sous
AVK, FA, INR 3,8 potentialisé par l'alcool. Le choix entre les deux AVK suisses
n'est pas indifférent : ce ne sont pas les mêmes molécules et leurs demi-vies
diffèrent d'un ordre de grandeur.

**`Sintrom®` (acénocoumarol), tranché sur la chronologie du cas lui-même :**

* la grille écrit « **son INR est revenu à 1,8 après arrêt** » et « on arrête le
  Sintrom® **quelques jours seulement**, le temps de faire la gastroscopie » ;
* l'acénocoumarol a une demi-vie de **8 à 11 h** : l'INR se normalise en 2–3
  jours, ce que le récit décrit exactement ;
* la phenprocoumone (`Marcoumar®`) a une demi-vie de **120 à 160 h** : l'INR
  resterait supra-thérapeutique **une à deux semaines**, et la phrase « quelques
  jours seulement » deviendrait cliniquement fausse. Substituer `Marcoumar®`
  aurait rendu la grille incohérente avec son propre déroulé.

S'y ajoute que `Sintrom®` est l'AVK très majoritairement prescrit en Suisse.
Le CYP2C9 cité comme voie du métabolisme reste juste pour l'acénocoumarol.

**Corollaire assumé :** dans ces deux grilles, les 20 `warfarine` deviennent
`acénocoumarol`. Laisser « interaction alcool–warfarine » à côté de
« Sintrom® » aurait créé une contradiction que la passe elle-même aurait
introduite. Ailleurs dans le corpus, `warfarine` reste — il y figure dans des
énumérations pharmacologiques génériques (« AVK (warfarine, acénocoumarol) »),
qui sont exactes.

**Une conséquence hors périmètre**, signalée et non traitée : la grille
`AMC-ECOS1-S2` s'appelle « … **Surdosage de Coumadin** — Grille ECOS.html ».
Le `<title>` et le `<h1>` disent désormais « Surdosage de Sintrom® », mais **le
nom de fichier et le libellé d'`index.html` disent toujours Coumadin** :
renommer le fichier et corriger `index.html` sort de `cases/casecos/`.

### 4. Les conversions d'unités, analyte par analyte

Chaque valeur a été recalculée après identification de l'analyte. Les facteurs
ne sont pas interchangeables :

| analyte | de | vers | facteur |
|---|---|---|---|
| hémoglobine | g/dL, `g%` | g/L | ×10 |
| numérations **sanguines** | /mm³ | G/L | ×0,001 |
| AFP, PSA, prolactine, ferritine, fibronectine, digoxine, procalcitonine | ng/mL | µg/L | ×1 |
| BNP / NT-proBNP | pg/mL | ng/L | ×1 |
| 17-β-œstradiol | pg/mL | pmol/L | ×3,671 |
| potassium | mEq | mmol | ×1 |
| poids | lb | kg | ×0,4536 |

**Les numérations de LIQUIDES BIOLOGIQUES ne suivent pas la règle du sang.**
Onze occurrences — PNN de l'ascite (seuil 250 de la PBS), cellularité du liquide
synovial, du LBA, du LCR, du liquide pleural — ont été rendues en **/µL**, pas
en G/L : c'est l'écriture correcte, et c'est la même raison qui fait qu'AMBOSS
ne bannit `/µL` que précédé d'un terme d'hémogramme. Trois d'entre elles ont dû
être reformulées (« 12'400 **éléments**/µL », « <50 **éléments**/µL ») parce que
la forme littérale « leucocytes/µL » ou « GB/µL », pourtant juste, déclenche ce
motif hérité.

**Quatre pièges de conversion payés, dont trois inédits :**

1. **« Hb >7 g/dl (ou >8 g/dl si cardiopathie ischémique) »** — deux valeurs sur
   une ligne, exactement le piège annoncé. Trois lignes de ce type dans la même
   grille, plus « Hb <13 g/dl homme, <12 g/dl femme » et « Plaquettes > 50'000
   (100'000 si hémorragie active) ».
2. **La formule de Ganzoni** — « déficit en fer (mg) = poids × (Hb normale − Hb
   patient) **(g/dl) × 2,4** ». Convertir l'unité sans toucher au **coefficient**
   aurait multiplié la dose de fer par dix. Écrite désormais `(g/L) × 0,24`.
   Deux occurrences.
3. **Deux seuils écrits mille fois trop grands à la source** : « NT-proBNP >
   300 **ng/ml** » et « troponines T ultrasensibles > 14 **ng/ml** ». La règle
   « ng/mL → ng/L, ×1000 » aurait donné 300 000 et 14 000 ng/L. Ce sont des
   **ng/L** : l'unité a été corrigée, la valeur gardée.
4. **Deux CRP en mg/dL** (« CRP 32 mg/dl — modérée », « CRP 45 mg/dL ») : 320 et
   450 mg/L seraient massives et contrediraient le qualificatif. La même grille
   écrit « CRP > 40 mg/L » ailleurs. Unité corrigée, valeur gardée.

**Une valeur, et une seule, a été changée** : `AMC-Chir2-ECG3` portait
« hémorragie digestive grave (**Hb 7,5 g/L**, choc compensé) » — présent dans
`566f38d`, vérifié. C'est une magnitude de g/dL sous une unité de g/L, et elle
contredit d'un facteur dix le seuil transfusionnel « Hb > 70 g/L » énoncé trois
lignes plus haut dans la même grille. Écrit **75 g/L**. C'est le seul endroit où
la nomenclature a imposé de toucher un chiffre plutôt qu'une unité.

Le qualificatif voisin a été relu après chaque conversion (« abaissé »,
« normal », « élevé », « anémie exclue », « leucopénie », « thrombopénie »).

### 5. La redondance monte de 2, et on sait lesquelles

**830 → 832.** Mesuré des deux côtés : le corpus de `566f38d` a été extrait par
`git archive` dans un répertoire de travail et `report_redundancy.py` relancé
dessus avec `lib.CASES` redirigé. Quatre grilles bougent, aucune autre :

| grille | Δ | couple | cause |
|---|---|---|---|
| `AMC-Chir3-ECG6` | **+1** | `expert ↔ theorie` | « ARTHROSCOPIE = gold standard diagnostique ET thérapeutique » et « ARTHROSCOPIE : gold standard … » disaient déjà la même chose ; réécrites toutes deux en « référence diagnostique ET thérapeutique », elles franchissent le seuil à **0,73** |
| `Péritonite` | **+1** | `expert ↔ theorie` | « Biopsies peropératoires (gold standard) » ×2 → « (examen de référence) », **0,93** |
| `UIDC-Monsieur Marcel T.` | **+1** | `expert ↔ theorie` | idem, **0,85** |
| `STEMI` | **−1** | `redflags ↔ theorie` | l'expansion de `pPCI` en « angioplastie primaire » **allonge** les deux items de façon inégale et fait **retomber** la paire sous 0,72 |

C'est bien l'effet annoncé — deux items qui disaient la même chose la disent
maintenant dans les mêmes mots — et il se concentre sur `expert ↔ theorie`,
le couple que k1 avait déjà désigné comme la frontière à tracer (405 paires sur
830). **Aucun contenu n'a été ajouté ni dupliqué.**

### 6. `check_no_loss` : 17 disparitions, 17 verdicts

**Aucune n'est une perte.** Les 17 sont le texte *normalisé* d'items renommés :
`check_no_loss` compare des chaînes normalisées, et un item dont un terme change
disparaît de l'ensemble d'avant. Chacune a été appariée à sa substitution —
`gold standard` (7), `Coumadin`/`warfarine` (2), `PCI`/`CABG` (2), `FIT` (2),
`911` (1), `DOACs` (1), unités implicites (1), `ng/mL` de la digoxine (1).

**Contrôle indépendant :** le nombre d'items extraits, grille par grille, sur les
13 grilles concernées — **2 816 avant, 2 817 après**. Douze sont strictement
égales. La treizième, `AMC-Chir4-ECG4`, gagne **un** item : le paragraphe
`<p>PCI vs CABG :</p>` normalisait en `pci vs cabg`, **11 caractères**, sous le
seuil `min_len = 18` de `list_items()` ; réécrit `Angioplastie vs pontage`, il
en fait 23 et devient visible. Effet de seuil de l'extracteur, pas de contenu
ajouté.

### 7. Onze faux positifs évités — la moitié utile du relevé

Chaque jeton d'apparence anglophone a été **lu en contexte** avant d'être jugé.
Onze sont des homographes français ou suisses, tous consignés dans `SANS_MOTIF`
avec leur chiffre :

| jeton | occ. | ce que c'est vraiment |
|---|---|---|
| `MI` | 113 | **membres inférieurs** (« Doppler veineux MI ») — le corpus écrit `IDM` 108 fois pour l'infarctus |
| `PTT` | 36 | **la crase suisse** : les laboratoires suisses rendent `TP + PTT` là où la France écrit `TP + TCA`. Ni purpura, ni faute |
| `IU` | 36 | **infection urinaire** (« les IU simples ») — `UI` pour les unités internationales est ailleurs, 84 fois |
| `DAPT` | 35 | double antiagrégation, sigle ESC installé en français |
| `NIPT` | 34 | usage suisse installé (OFSP, FMH), glosé « NIPT / DPNI » par la grille |
| `EGFR` | 21 | le **récepteur** en oncologie (« mutations EGFR, ALK, ROS1 »), pas le DFG |
| `HIT` | 19 | **Head Impulse Test** du protocole HINTS |
| `PCC` | 19 | concentré de complexe prothrombinique (Beriplex®/Octaplex®) |
| `OAC` | 18 | l'**Ordonnance réglant l'admission à la circulation routière** — texte fédéral suisse cité par article |
| `IBS` | 16 | **infection bactérienne sérieuse** du nourrisson — le corpus écrit `SII` pour le côlon irritable |
| `CD4` | 2 | un taux de CD4 se rend en /µL partout : `0,014 G/L` n'a aucun sens. Faux positif du motif hémogramme+`/µL` d'AMBOSS |

`HCT` mérite une mention à part : l'occurrence unique était bien un hématocrite
et a été corrigée en `Ht`, **mais le motif n'a pas été ajouté à `BANNED`** —
`HCT` est aussi l'abréviation courante de l'hydrochlorothiazide, et un motif ici
ferait un jour signaler une prescription comme une faute d'unité.

### 8. Ce qui reste ouvert

1. **Le nom de fichier `… Surdosage de Coumadin …`** et son libellé dans
   `index.html` — hors `cases/casecos/`.
2. **`HBV` 15 / `HCV` 42 contre `VHB` 50 / `VHC` 22.** Contradiction interne
   réelle, non traitée : « Cirrhose HCV et CHC » est dans un **nom de fichier**.
3. **`SCLC` 16 / `NSCLC` 14 contre `CBPC` 5 / `CBNPC` 7**, dans la même grille.
   Les sigles y sont glosés en anglais (« SCLC (Small Cell Lung Cancer) ») :
   la correction est une réécriture, pas une substitution.
4. **`AOD` 62 et `ACOD` 15 coexistent** — deux formes françaises correctes,
   aucune n'est un anglicisme ; à harmoniser si on veut une seule graphie.
5. **« bleuets »** 8 occurrences — québécisme pour myrtilles, dans la liste des
   causes factices de méléna. Vocabulaire, pas nomenclature.

### 9. Ce qui n'a pas été fait

* **Rien hors de `cases/casecos/`, `scripts/casecos/` et de ce journal.** Ni
  `cases/german/`, ni `cases/rescos-locales/`, ni `index.html`, ni
  `cases/scoring.js`, ni aucun script partagé.
* **Aucun `git add`** — l'index est resté intact. Commit par
  `git commit -- <chemins>` exclusivement.
* **Le barème n'a pas été touché** : `check_invariants.py` au vert, aucun
  `coef`, aucun `maxScores`, aucun libellé `N.` de `.criteria-text` modifié.
* **Aucune grille lue en entier avec `Read`** : uniquement des fenêtres de
  contexte extraites par script.
* **Aucun `grep` brut employé comme contrôle** — tous les chiffres viennent des
  scripts de `scripts/casecos/` ou de mesures Python explicites.
* **Aucune commande réseau, aucun `git push`, aucun `git gc`, aucun
  `git prune`.**

### 10. L'incident d'index, une troisième fois

Au moment de committer, l'historique avait été **réécrit** : `288894d` (bascule
des 198 grilles sur le moteur partagé) et `566f38d` (ce journal) **ne sont plus
des ancêtres de `HEAD`**. Le travail de k2 n'existait plus que dans l'arbre de
travail — d'où 198 grilles et 6 scripts signalés « modifiés » alors que je n'en
avais touché que 132 et un seul.

`git commit -- <chemins>` valide l'état de l'arbre de travail : ce commit
**restitue donc aussi le lot k2**, et c'est la seule issue sûre — l'alternative
était de le perdre. Une pièce n'a pas pu être récupérée :
`scripts/casecos/migrate_to_shared_engine.py`, que la réécriture a dé-suivi et
qui est aujourd'hui **non suivi sur le disque** ; le restaurer demanderait un
`git add`, interdit sur cet index partagé.
