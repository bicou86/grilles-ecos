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

---

## k4 — Grille pilote `AMC-MedInterne-P13 Méningite — Mme S.` et contrat de blocs

Base `b6f83f6`. **Une seule grille modifiée**, trois ajouts, aucune suppression.
Le livrable principal n'est pas la grille : c'est le **contrat de blocs**, écrit
au § 2 de `scripts/casecos/PROCEDURE-casecos.md`.

### Le contrat, en une phrase

`theorie` est le canonique ; la frontière `expert ↔ theorie` — 405 des 830
paires du corpus — se trace sur le **référent** et non sur le caractère
actionnable : *changez le patient, l'item survit-il ?* Il survit → `theorie`,
il meurt → `expert`. Deux sections de `theorie` échappent au test (« Diagnostic »
et « Résumé du cas clinique ») : elles y restent, car elles sont le logement
CasECOS du `resume` manquant, et aucun autre bloc ne restitue le cas en
narration synthétique.

Corollaire assumé : **l'interdit d'AMBOSS « `theorie` ne porte jamais de
protocole » ne se transpose pas.** Chez AMBOSS il avait un bénéficiaire, le
`resume`. Ici il n'y en a aucun, et la section « Algorithme de prise en charge
empirique (HUG) » du pilote n'a aucune autre destination licite : la supprimer
serait une perte, `expert` casserait le référent, `therapy` est une section
notée.

### Les trois modifications, toutes des ajouts

Trouvées par l'**usage inversé** de la mesure de redondance (une paire notée qui
s'accorde avec un bloc de restitution sans passer par le canonique = un trou du
canonique), puis confirmées par comptage du texte visible bloc par bloc.

| # | ajout | où | pourquoi |
|---|---|---|---|
| 1 | fond d'œil / évaluation clinique de l'HTIC, risque de cône de pression | `expert`/Pièges | présent dans `redflags` n° 4 et le `detail-text` e4-detail-1, **absent du canonique des pièges** — or « Oublier le fond d'œil » est le **piège n° 1 de la page SSP** (niveau 1) |
| 2 | « Devant un purpura fulminans, la première dose de 2 g s'administre sans délai, IV ou IM, y compris en préhospitalier » | `theorie`/Rappels, item ceftriaxone | **cible chiffrée de la page SSP** absente de toute la grille (0 occurrence de « préhospitalier ») |
| 3 | « Rationnel : réduction de la mortalité et des séquelles neurologiques, bénéfice principalement démontré dans les méningites à S. pneumoniae » | `theorie`/Rappels, item dexaméthasone | le *pourquoi* vivait dans `therapy` m3 **et** `redflags` n° 5 — deux sections notées — et nulle part dans le canonique du rationnel thérapeutique. 0 occurrence de « séquelle » dans `theorie` avant |

Page SSP : `SSP ECOS/SSP — Céphalée.md` (elle dessert 22 grilles). **L'indicateur
se vérifie** : son rendement n'est pas venu de sa largeur mais de ses trois
cibles chiffrées sur la méningite. Les deux qui portaient un nombre déjà présent
dans la grille (ceftriaxone 2 g × 2/j, dexaméthasone 10 mg × 4/j) n'ont rien
donné — la grille était déjà juste ; celle qui portait un nombre **absent**
(2 g IV/IM en préhospitalier) a donné la modification n° 2.

### Ce qui a été vu et NON corrigé

* **`therapy` m3 (noté) omet la grossesse** parmi les facteurs de risque Listeria
  (« âge >50 ans, diabète, immunosuppression, néoplasie, contexte
  épidémiologique »), là où la page SSP et `theorie` la nomment. C'est une
  **divergence dans une section notée** : elle se consigne, elle ne se corrige
  pas.
* **1 paire intra-`expert` à 0,77** (Points clés « Gérer la dimension
  épidémiologique… » ↔ Pièges « Ne pas penser à la dimension épidémiologique… »).
  Plancher structurel : la polarité est la raison d'être des trois sections
  d'`expert`. Jugement d'auteur, documenté, non corrigé.
* Les 3 grilles « ECOS Diag » et les 12 sans `annexe-dd` restent en l'état
  (arbitrages k1 toujours ouverts).

### La découverte qui change la méthode des 197 suivantes

**Le pilote mesure 0 paire inter-blocs**, et porte pourtant les cinq mêmes
molécules aux mêmes posologies dans `therapy` et dans `theorie`/Rappels. Ces cinq
couples marquent **0,15 à 0,48**. La cause est arithmétique : un `therapy-item`
empaquette « Traitement : X » et un long « Détails : » (308 caractères en
moyenne) quand un `<li>` de `theorie` en fait 145 ; `SequenceMatcher.ratio()`
valant `2M/T`, un item court **entièrement contenu** dans le long plafonne à
`2×145/453 = 0,64` — **sous le seuil de 0,72**.

Le seuil n'a pas été touché : c'est la mesure publiée du projet, elle garde les
quatre corpus comparables. Mais sur ce corpus **c'est le contrat qui trouve le
travail, et la mesure qui le confirme** — jamais l'inverse. Les 135 paires
`theorie ↔ therapy` du relevé k1 sont un plancher, pas un total. Le couple
`expert ↔ theorie` (405 paires) n'a pas ce biais : items de longueur voisine
(121 et 145 caractères au pilote).

### Portes

| porte | avant | après |
|---|---|---|
| `check_invariants.py` | rc 0 | **rc 0** |
| `check_nomenclature.py` | rc 0 | **rc 0** |
| `check_reachability.py` | 198/198 | **198/198 à 100 %** |
| `report_redundancy.py "AMC-MedInterne-P13"` | **0 inter, 1 intra** | **0 inter, 1 intra** |
| `check_no_loss.py b6f83f6 "AMC-MedInterne-P13"` | — | **2 disparitions, 2 verdictées** |
| `scripts/amboss/report_redundancy.py --quiet` | **147** | **147** |
| `scripts/rescos/report_redundancy.py --quiet` | **127** | **127** |

**Contrôle anti-perte indépendant**, parce qu'une disparition appariée reste une
affirmation : **175 items avant, 175 après**. 3 disparus, 3 apparus, appariés un
à un (0,69 / 0,70 / 0,73) — les trois sont des **allongements** des items
modifiés, aucun texte retiré. `check_no_loss` n'en signale que 2 : le troisième
(ceftriaxone) reste au-dessus de son seuil d'appariement.

**Barème intact** : aucun `maxScores`, aucun `coef`, aucun `sectionInfo[].count`,
aucun `<span class="score">`, aucun libellé `N.` de `.criteria-text` touché.
Les trois modifications sont dans des `<li>` de blocs pédagogiques non notés —
règle 1 du barème (correction sans changement de structure).

### Contraintes respectées

* Rien écrit hors de `cases/casecos/`, `scripts/casecos/PROCEDURE-casecos.md` et
  ce journal (plus le rapport k4).
* **Aucun `git add`** — commit par `git commit -- <chemins>` exclusivement.
  Rien touché sous `cases/german/`, `cases/rescos-locales/`, `scripts/german/`,
  `scripts/rescos-locales/`, où l'utilisateur travaillait en parallèle (109
  fichiers modifiés dans son arbre au début du lot, aucun chevauchement).
* **Aucune grille lue en entier avec `Read`** : bornes situées par
  `lib.top_spans()`, lecture par fenêtres `offset`/`limit`.
* **Aucun `grep` brut employé comme contrôle** : tous les chiffres viennent des
  scripts de `scripts/casecos/` ou de mesures Python explicites (stdlib seule).
* Aucune commande réseau, aucun `git push`, aucun `git gc`, aucun `git prune`,
  aucun `timeout`.

---

## Lot k5a — 25 premières grilles CasECOS par ordre alphabétique

Branche `refonte-amboss-suisse`, base `42aa4e0`. Premier lot de production après
le pilote k4 : les 25 premières grilles de `cases/casecos/` par ordre
alphabétique. Le pilote (`AMC-MedInterne-P13 Méningite`) n'y figure pas — il est
au-delà du rang 25 — le lot est donc exactement `lib.grids()[:25]`.

**24 grilles sur 25 modifiées.** Seule `AMC-Chir3-ECG2 Entorse grave du genou`
ressort intacte : sa paire mesurée (`annexe-dd ↔ expert`, triade d'O'Donoghue)
est déjà couverte par `theorie`, et son usage inversé ne signale aucun trou.

### Redondance : 66 → 27 paires inter-blocs (−59 %)

| couple | avant | après |
|---|---|---|
| **`expert ↔ theorie`** | **36** | **4** (−89 %) |
| `theorie ↔ theorie` (intra) | 58 | 57 |
| `annexe-dd ↔ annexe-dd` (intra) | 16 | 16 |
| `therapy ↔ theorie` | 10 | 11 |
| `expert ↔ expert` (intra) | 9 | 8 |
| autres inter | 20 | 12 |
| **TOTAL inter** | **66** | **27** |
| TOTAL intra | 90 | 88 |

`expert ↔ theorie` était bien la cible : 36 des 66 paires du lot, 55 %, contre
49 % annoncés sur le corpus. Le test du référent — *changez le patient, l'item
survit-il ?* — la tranche sans ambiguïté sur ce lot, parce que le motif y est
constant : **`expert`/Points clés est, dans ce corpus, un cours en réduction**.
Épidémiologie, classifications, posologies détaillées, résultats d'études — tout
y survit au changement de patient, et `theorie` le porte déjà, presque toujours
plus richement. `expert`/Rôles et `expert`/Pièges, eux, tiennent leur rôle.

### La règle appliquée, et sa limite volontaire

Un item d'`expert` n'a été **retiré** que si (a) le test du référent l'attribue à
`theorie`, (b) `theorie` porte déjà son contenu **intégral** — vérifié terme à
terme avant chaque suppression, en portant d'abord dans `theorie` ce qui lui
manquait — et (c) `expert` garde le comportement observable correspondant dans
Rôles ou Pièges. Sinon l'item est **spécialisé** (le générique part dans
`theorie`, la formulation d'`expert` redevient une action) ou **laissé**.

**Limite assumée** : l'opération n'a porté que sur les paires *mesurées*. Le
reste des Points clés déclaratifs d'`expert` — largement majoritaire — n'a pas
été touché. Le convertir serait une réécriture de masse, non mesurable, et
excède le mandat d'un lot. **C'est une question de style éditorial à trancher
pour le corpus entier, pas grille par grille.** Voir « Ce qui reste ouvert ».

### Les 4 paires `expert ↔ theorie` laissées, et pourquoi

| grille | paire | raison |
|---|---|---|
| Constat de chute | « Prescrire un CT cérébral… » (Points clés) ↔ règle + rationnel (`theorie`) | action ↔ règle : le format change, le contrat protège |
| TFCC | « Connaissance de l'arthroscopie… » (**Rôles**) ↔ « arthroscopie = référence… » | `Rôles` est la liste de ce que l'évaluateur vérifie : ce n'est pas un énoncé de savoir |
| Épicondylite | « Indications chirurgicales : échec conservateur 6 mois » (**Rôles**) ↔ idem | idem |
| Fémur proximal | « Fractures du col chez le sujet jeune… » ↔ « toutes Garden… » | forme avec l'item « sujet âgé » un contraste jeune/âgé dont l'amputation d'une moitié serait une perte pédagogique — **règle 3** |

Supprimer un item de `Rôles` pour satisfaire une comparaison de chaînes
reviendrait à laisser l'outil dicter le contrat. Sur `AMC-Chir3-Vignette1`, la
paire à **1,00** entre `Rôles` (« Approche multidisciplinaire (orthogériatrie) »)
et `theorie` a été résolue autrement : l'item de `Rôles` a été rendu à sa
fonction — « Évaluer l'inscription du cas dans une filière orthogériatrique et
l'appel des intervenants utiles ». C'est le geste de spécialisation, pas la
suppression.

### 3 paires `annexe-dd ↔ theorie` sont un ARTEFACT DE MESURE, pas une redondance

Sur `AMC-Chir2-ARC1`, trois paires (1,00 · 0,75 · 0,73) apparient un item
d'`annexe-dd` — « migration cholédocienne (arguments POUR) », « pancréatite
biliaire (arguments POUR) » — à un **sous-titre** de `theorie` porté par un `<li>`
(« MIGRATION CHOLÉDOCIENNE : », « PANCRÉATITE BILIAIRE : »). Ce sont des
étiquettes de structure des deux côtés, pas du contenu. **Ne pas les poursuivre**,
et se souvenir qu'`annexe-dd` ne se nettoie pas (§ 8 de la procédure).

### L'usage inversé : 8 trous du canonique sur 25 grilles

Instrument du pilote rejoué grille par grille — appariement à seuil abaissé
(0,45) des items de `therapy`/`redflags` contre les blocs de restitution, en
retenant ceux dont le meilleur appariement est **ailleurs que dans `theorie`** —
puis confirmation par comptage du terme dans le texte visible, bloc par bloc.

| grille | point | vivait dans | `theorie` |
|---|---|---|---|
| Migraine | **fond d'œil** (piège n° 1 de la page SSP) | `redflags` n° 5 seul | 0 occurrence de « œil » |
| Constat de chute | **station au sol > 1 h** : rhabdomyolyse, hypothermie, escarres, CK | `redflags` n° 6 seul | 0 « rhabdomyolyse », 0 « hypothermie », 0 « escarre », 0 CK |
| Cancer gastrique | **complications post-gastrectomie** : anémie ~50 %, dumping précoce/tardif, rationnel de la B12 | `redflags` n° 6-8 + `expert`/Pièges | aucune section complications |
| Hémorragie digestive | **seuil du score de Glasgow-Blatchford** | `expert`/Pièges seul, **et faux** (voir ci-dessous) | scores nommés sans seuil |
| Épicondylite | **complications de la chirurgie** | `therapy` + `cloture` (paire 0,73) | 0 |
| Fémur proximal | **mortalité 5-8 % à 1 mois, 20-30 % à 1 an** et **délai < 24-48 h** | `redflags` + `expert` (paire 0,80) | 0 « mortalité », 0 « 48h » |
| IRC du diabétique | **rationnel de la cible HbA1c** (DCCT, risque d'hypoglycémie ×3) | `therapy` + `expert` | 0 « DCCT », 0 « hypoglycémie » |
| Coxarthrose | **foyers infectieux pré-op / avis urologique** (sondage → infection prothétique) | `expert` + `therapy` + `defi` + `cloture` | 0 « urolog », 0 « sondage » |

**Deux de ces grilles mesuraient 0 paire inter-blocs** — `AMC-Chir2-Vignette5`
et `AMC-Chir3-ARC1`. C'est la démonstration directe de l'avertissement du
pilote : un `report_redundancy.py` vide ne dit rien du travail à faire. **C'est
le contrat qui le trouve.**

Un trou de plus, non listé parce que le canonique le portait déjà : le TFCC —
`cloture` et `expert` s'accordaient sur « 70-80 % de bons résultats » sans passer
par `theorie` ; le pronostic y a été ajouté.

### Niveau 1 — ce que les pages SSP ont donné

16 pages SSP desservent le lot, toutes lues. **L'indicateur du pilote se vérifie
une seconde fois** : le rendement suit les **cibles chiffrées**, pas la largeur
de la page.

Rendement (cible chiffrée absente de la grille, portée dans `theorie`) :

* **Céphalée** (22 grilles) — piège n° 1 « Oublier le fond d'œil » ; posologies de
  crise (paracétamol 1 g, ibuprofène 400-600 mg, sumatriptan 50-100 mg PO / 6 mg
  SC, ± métoclopramide 10 mg) : **la grille ne portait aucune dose** ; seuil du
  traitement de fond (≥ 3 crises invalidantes/mois) ; seuils de la céphalée par
  abus (≥ 15 j/mois antalgiques simples, ≥ 10 j/mois triptans) ; céphalée
  inaugurale après 50 ans → Horton, **absent de toute la grille**.
* **Chute & Évaluation gériatrique** (7) — station au sol > 1 h et son bilan.
* **Hernie inguinale** (1 seule grille, et la plus rentable du lot) — chirurgie
  **< 6 h**, absent de toute la page ; hernie crurale, risque d'étranglement
  **15-20 %** ; distinction **incarcération / étranglement**, 0 occurrence de
  « incarcér- » ; piège de la **réduction en masse**, 0 occurrence.
* **Douleur de Hanche** (8) — délai opératoire **24-48 h** (SSO/SGO).
* **Diabète** (10) — individualisation de la cible HbA1c (< 7 %, < 8 % chez
  l'âgé, jamais < 6,5 % chez le fragile).
* **Nausées / Hématémèse** (4) — seuil de Glasgow-Blatchford (**correction**).
* **Capacité de discernement** (10) — ordre de la cascade des représentants
  (**correction**).

Rendement **nul**, et c'est un résultat : **Lombalgies** (24 grilles) et
**Douleurs articulaires** (14) — les deux pages les plus larges du lot — ne
portent **aucun contenu** sur la scoliose idiopathique, la tendinopathie du
tibial postérieur ni l'épicondylite ; elles ne citent ces entités que par le
titre de la grille. **Douleur au Poignet** ne porte pas la classification de
Palmer, **Polytraumatisme** ne porte pas celle de Gustilo. Sur ces cinq points,
la hiérarchie tombe au **niveau 3** — ni SSP explicite, ni SSP générique
contradictoire : laisser, consigner. C'est fait ici.

### Deux corrections factuelles

1. **`AMC-Chir2-ECG3`, score de Glasgow-Blatchford.** `expert`/Pièges portait
   « Score de Glasgow-Blatchford > 0 = nécessite endoscopie hospitalière ». La
   page SSP est explicite et chiffrée : « GBS = 0-1 → prise en charge ambulatoire
   envisageable », « identifie les bas risques (0-1) → ambulatoire ». **SSP
   explicite → elle fait foi** (niveau 1). L'item devient un vrai piège, et le
   seuil est porté dans `theorie`/Évaluation de la sévérité, qui ne nommait les
   scores que sans leurs bornes.
2. **`AMC-Chir1-MedLeg`, cascade des représentants.** `theorie` plaçait le
   curateur (rang 2) **avant** le mandat pour cause d'inaptitude (rang 3). L'art.
   378 al. 1 CC met les directives anticipées et le mandat pour cause
   d'inaptitude au **même chiffre 1**, le curateur au chiffre 2 ; la page SSP dit
   la même chose. Les rangs 2 et 3 sont inversés, et la référence du curateur
   passe de l'art. 401 CC aux art. 394-396 CC, graphie de la page SSP.

Un troisième point relevé et **non corrigé** : `expert` de `AMC-Chir2-ECG5`
portait « score MELD (allocation **graphique** des greffons) », mot sans
signification ici. L'item ayant été supprimé comme doublon de `theorie` — qui
écrit correctement « allocation des greffons » — la coquille disparaît par le
même geste, sans arbitrage à porter.

### ⚠️ Le couple `theorie ↔ therapy` : la mesure est PIRE que ne le disait le pilote

Le pilote annonçait un plafond de 0,64 sur inclusion parfaite. **Sur ce lot il
est de 0,60**, mesuré : item de `theorie` **70 caractères** en moyenne (n = 1 622),
item de `therapy` **164** (n = 300), soit `2×70/(70+164) = 0,60`.

Mesure directe de ce que cela cache, par recouvrement de vocabulaire (jetons de
plus de 2 lettres, mots-outils retirés) :

| mesure | valeur |
|---|---|
| items de `theorie` dont **≥ 90 % du vocabulaire** se retrouve dans **un seul** item de `therapy` | **30** |
| … dont le ratio reste **≤ 0,72**, donc invisibles | **24 (80 %)** |
| paires `theorie ↔ therapy` effectivement mesurées sur le lot | **11** |

**La mesure voit environ un tiers du recouvrement réel.** Exemples chiffrés,
tous sous le seuil : `AMC-CasECOS Gériatrie` « surveillance neurologique
rapprochée » à **0,24** ; `AMC-Chir2-ECG4` « iléostomie de protection » à
**0,26** ; `AMC-Chir2-ECG5` « radiofréquence pour nodules < 3 cm » à **0,55** ;
`AMC-Chir2-Vignette1` « réparation pariétale, filet de Lichtenstein » à **0,56**.

Le seuil n'a pas été touché — c'est la mesure publiée du projet, elle garde
AMBOSS (147), RESCOS (127) et CasECOS comparables.

**La conséquence annoncée au § 3.3 du pilote est confirmée** : la structure
`Traitement : X` / `Détails : …` invite bien à loger le rationnel dans une
section notée. Cinq des huit trous du canonique ci-dessus sont exactement cela —
mortalité du fémur proximal, rationnel de la cible HbA1c, complications de la
chirurgie de l'épicondylite, complications post-gastrectomie, avis urologique
avant PTH. **Le repérage ne vient jamais de la mesure de redondance ; il vient
de l'usage inversé au seuil abaissé, puis d'un comptage bloc par bloc.**

### Portes

| porte | avant | après |
|---|---|---|
| `check_invariants.py` | rc 0 | **rc 0 — 198 grilles** |
| `check_nomenclature.py` | rc 0 | **rc 0** |
| `check_reachability.py` | 198/198 | **198/198 à 100 %** |
| `report_redundancy.py` (lot de 25) | **66 inter, 90 intra** | **27 inter, 88 intra** |
| `check_no_loss.py 42aa4e0` | — | **10 disparitions, 10 verdictées** |
| `scripts/amboss/report_redundancy.py --quiet` | **147** | **147** |
| `scripts/rescos/report_redundancy.py --quiet` | **127** | **127** |
| `scripts/amboss/check_invariants.py` · `scripts/rescos/check_invariants.py` | rc 0 | **rc 0** |

**Contrôle anti-perte indépendant**, parce qu'une disparition appariée reste une
affirmation. Ensembles d'items normalisés extraits de `git show 42aa4e0:…` et de
l'arbre de travail, sur les 25 grilles : **3 875 items avant, 3 863 après**,
soit **53 retirés et 41 ajoutés**, delta net **−12**.

Les 10 disparitions signalées par `check_no_loss` se répartissent en deux
familles, aucune n'étant une perte :

* **6 reformulations en place** — l'item existe toujours, enrichi : art. 16 CC et
  les deux rangs de la cascade (`MedLeg`), supplémentation post-gastrectomie
  (`ECG2`), les deux items du score de Glasgow-Blatchford (`ECG3`), engouement /
  incarcération (`Vignette1`).
* **4 suppressions dans `expert`** dont le contenu avait été **porté dans
  `theorie` au préalable** : art. 16 CC, laparoscopie de stadification et son
  chiffre de 20-30 %, bornes A/B/C du Child-Pugh.

Les 43 autres suppressions ne sont pas signalées parce que `theorie` en porte
déjà un appariement au-dessus du seuil — ce qui est précisément la condition
qu'on s'était donnée pour supprimer.

**Barème intact.** Toutes les modifications sont dans des `<li>` de blocs
pédagogiques non notés (`expert`, `theorie`). Aucun `maxScores`, aucun `coef`,
aucun `sectionInfo[].count`, aucun `<span class="score">`, aucun libellé `N.` de
`.criteria-text` touché ; aucune section notée (`therapy`, `redflags`, `cloture`,
`exemples`) modifiée. **Règle 1** du barème — pas de régénération du baseline,
`check_invariants.py` et `check_reachability.py` le confirment. `window.caseConfig`
et les chargements de `cases/scoring.js` / `cases/persistence.js` intacts.

### Non corrigé, documenté (règle 3)

* **88 paires intra-bloc** conservées. Les 57 paires intra-`theorie` sont
  massivement des **séries parallèles** dont le parallélisme est la raison d'être
  (« acidose / alcalose », « Garden I-II / III-IV », « sleeve / bypass », « stade
  3a / 3b », « fille 11-13 ans / garçon 13-15 ans »). Les 8 paires intra-`expert`
  sont le **plancher structurel de RESCOS** — polarité Points clés / Pièges.
  L'intra est une mesure additionnelle, hors du chiffre de référence : le noter,
  ne pas le poursuivre.
* **`AMC-CasECOS Migraine`** : `theorie` porte la prise en charge deux fois, en
  section « Prise en charge de la migraine » (synthèse) et en « Rappels
  thérapeutiques » (formulaire). Granularités différentes, même bloc : arbitrage
  d'auteur.
* **`AMC-Chir1-ECG1`** : `expert` et `theorie` rattachent tous deux l'ASA III à
  ce patient (« multiples comorbidités cardiopulmonaires » / « cas de
  M. Asaquatre »). Aucun des deux n'est le générique de l'autre.

### Ce qui reste ouvert

1. **Le style d'`expert`/Points clés, pour les 173 grilles restantes.** Le motif
   est corpus-large et non local : `Points clés` y est un cours en réduction là
   où le contrat le veut à l'infinitif. Ce lot n'a traité que les items *mesurés*
   comme doublons. Trancher globalement — réécriture à l'infinitif, ou
   assouplissement du contrat pour `Points clés` — est une décision d'auteur qui
   doit précéder les lots suivants, sous peine de traitements divergents.
2. **Instrument séparé pour `theorie ↔ therapy`.** Le § 7 du rapport k4 le
   proposait ; les chiffres ci-dessus le rendent nécessaire. Appariement du seul
   segment « Traitement : » d'un `therapy-item`, ou recouvrement de vocabulaire
   comme ici (30 recouvrements dont 24 invisibles). **Publié à part**, jamais en
   modifiant le seuil de 0,72.
3. **Sous-titres de `theorie` portés par des `<li>`.** Ils polluent
   `list_items()` et fabriquent des paires vides de contenu (3 sur ce lot).
   Un jour, les passer en `<h5>` ou les exclure de `list_items()` — mais cela
   déplacerait les chiffres publiés.
4. Les arbitrages k1 restent ouverts : 3 « ECOS Diag » obsolètes, 26
   `numeration-implicite`, nom de fichier « Surdosage de Coumadin », bug
   d'équilibrage latent de `lib_german` / `lib_rescos`.

### Contraintes respectées

* Rien écrit hors de `cases/casecos/`, de ce journal et du rapport k5a.
  **`scripts/casecos/` non modifié** — la procédure n'avait pas à changer, le
  contrat de blocs de k4 a tenu sur les 25 grilles.
* **Aucun `git add`** — commit par `git commit -- <chemins>` exclusivement.
  Rien touché sous `cases/german/`, `cases/rescos-locales/`, `scripts/german/`,
  `scripts/rescos-locales/`, où l'utilisateur travaillait en parallèle.
* **Aucune grille lue en entier avec `Read`** : bornes situées par
  `lib.top_spans()`, lecture par fenêtres `offset`/`limit`, édition par
  remplacement exact.
* **Aucun `grep` brut employé comme contrôle** : tous les chiffres viennent des
  scripts de `scripts/casecos/` ou de mesures Python passant par
  `lib.visible_text()` / `lib.top_spans()` / `lib.matches()` (stdlib seule).
* Aucune commande réseau, aucun `git push`, aucun `git gc`, aucun `git prune`,
  aucun `timeout`, aucun `snapshot_invariants.py`.

---

## Lot k5b — grilles 26 à 60 de `lib.grids()`

Branche `refonte-amboss-suisse`, base **`e54b127`**. Deuxième lot de production,
35 grilles, dans la continuité de k5a.

**28 grilles sur 35 modifiées, 60 ajouts, 106 suppressions de lignes.**
Redondance inter-blocs du lot **149 → 58 (−61 %)**, dont
`expert ↔ theorie` **81 → 2 (−97,5 %)**.

| porte | avant | après |
|---|---|---|
| `check_invariants.py` | rc 0 | **rc 0 — 198 grilles** |
| `check_nomenclature.py` | rc 0 | **rc 0** |
| `check_reachability.py` | 198/198 | **198/198 à 100 %** |
| `report_redundancy.py` (lot de 35) | **149 inter** | **58 inter** |
| `check_no_loss.py e54b127` | — | **19 disparitions, 19 verdictées** |
| `scripts/amboss/report_redundancy.py --quiet` | 147 | **147** |
| `scripts/rescos/report_redundancy.py --quiet` | 127 | **127** |
| `scripts/amboss/check_invariants.py` · `scripts/rescos/check_invariants.py` | rc 0 | **rc 0** |

### Le lot

`lib.grids()[25:60]`. Sept grilles ressortent intactes ; **`AMC-Chir5-Vignette1`
(nodule pulmonaire) est la seule à mesurer 0 paire ET 0 signal d'usage inversé** —
deuxième cas après `AMC-Chir3-ECG2` du lot k5a.

### Où sont passées les 91 paires

| couple | avant | après | pourquoi |
|---|---|---|---|
| `expert ↔ theorie` | 81 | **2** | le test du référent tranche |
| `annexe-dd ↔ expert` | 9 | **0** | spécialisation de l'item d'`expert` |
| `expert ↔ redflags` · `expert ↔ therapy` · `cloture ↔ expert` | 1 + 1 + 1 | **0** | idem |
| `annexe-dd ↔ theorie` | 18 | 18 | `annexe-dd` ne se nettoie pas |
| `theorie ↔ therapy` | 14 | 14 | le canonique doit porter le champ ; la section notée ne se dédoublonne pas |
| `redflags ↔ theorie` | 12 | 12 | idem |
| `annexe-dd ↔ redflags` | 11 | 11 | deux blocs non nettoyables |
| `cloture ↔ theorie` | 1 | 1 | phrase modèle de « Réponses types du candidat » |

**Les 58 paires restantes sont toutes entre blocs que le contrat interdit de
dédoublonner**, à deux exceptions assumées (voir plus bas).

### Les deux `expert ↔ theorie` laissées, et pourquoi

Toutes deux sur `AMC-ECOS1-S4 Convulsion fébrile` :

1. `expert`/Rôles, « Question 3 — Indication d'une PL dans ce cas précis : Non… ».
   C'est le **script de révélation** : l'expert gère cinq questions écrites et
   livre la réponse attendue. Supprimer là serait laisser la comparaison de
   chaînes dicter le contrat. Précédent k5a explicite.
2. `expert`/Pièges, « Prescrire un traitement antiépileptique de fond… — non
   recommandé » ↔ `theorie` « Ne pas prescrire d'antiépileptique de fond… ».
   **Action ↔ règle** : le format change, la polarité est la raison d'être de
   `Pièges`. Précédent k5a explicite.

### Trois artefacts de mesure, mesurés

1. **L'artefact des étiquettes numérotées.** `redflags` titre ses items
   « 1. », « 2. »… ; `theorie` numérote ses classifications de la même façon.
   D'où « 2. Retard de consolidation » (redflags) ↔ « C : retard de
   consolidation » (Herbert, `theorie`) à **0,96** — deux étiquettes, aucun
   contenu. Trois occurrences sur `AMC-Chir5-ECG4` seule.
2. **L'artefact « X — arguments POUR » de k5a se confirme**, et il est
   massif ici : `AMC-Chir5-ECG1` (masse médiastinale) rend **4 paires sur 5**
   par appariement de « 2. Thymome et autres tumeurs thymiques — arguments POUR »
   avec « 2. Thymomes et autres tumeurs thymiques (35-50%, le plus fréquent) ».
3. **L'artefact de négation, inédit.** Sur `AMC-ECOS1-S3` (vertiges), `annexe-dd`
   écrit ses arguments CONTRE en niant le libellé du `redflags` correspondant :
   « absence de facteurs de risque cardiovasculaire évidents » ↔ « 5. Facteurs
   de risque cardiovasculaire élevés » à **0,83**. `SequenceMatcher` ne voit pas
   la négation. Cinq occurrences sur cette grille, sept sur `AMC-ECOS1-S5`.
   **Ne jamais résoudre une telle paire : les deux items disent le contraire.**

### Les onze trous du canonique

Instrument de k4/k5a rejoué : appariement à seuil abaissé (0,45) de
`therapy`/`redflags` contre les blocs de restitution, en retenant ceux dont le
meilleur appariement est **ailleurs que dans `theorie`**, puis comptage du terme
bloc par bloc dans le texte visible.

| grille | point absent du canonique | vivait dans |
|---|---|---|
| Ostéosarcome | **pronostic 5 ans 60-70 / 20-30 %**, récidive locale, complications de l'allogreffe | `redflags` seul |
| Entorse de cheville | **5-10 % d'instabilité chronique** : le *pourquoi* de la rééducation proprioceptive | `therapy`/Détails + `redflags` |
| Scaphoïde | **retard de consolidation**, **3 mois** pour le 1/3 moyen, signal T2 de la nécrose, **humpback deformity** | `therapy`/Détails + `redflags` |
| Ischémie aiguë MI | **syndrome de revascularisation** : hyperkaliémie, acidose, IRA myoglobinurique, Volkmann | `redflags` seul |
| AOMI | **75 %/25 % à 5 ans**, 25 %/25 % de l'ischémie critique, −50 % / −25 % / +50-200 % | `expert` + `therapy` |
| AAA | **fistule aorto-duodénale**, dépistage familial des fratries > 55 ans | `expert` + `redflags` |
| STEMI | **90 min / 120 min**, cinétique des troponines, complications mécaniques J3-J7 et Dressler | `therapy` + `redflags` + `expert` |
| Dissection aortique | composants de la **triade de Beck**, fenestration sur malperfusion réfractaire | `annexe-dd` + `therapy` |
| Sténose aortique | **l'auscultation entière** : aucune section clinique dans `theorie` | `annexe-dd` + `expert` |
| TVP | **syndrome post-thrombotique** (0 occurrence dans `theorie`), filtre cave | `expert` + `redflags` + `therapy` |
| Carotide | **syndrome optico-pyramidal**, 10-20 % à 90 j, **syndrome d'hyperperfusion** | `expert` + `redflags` |

Plus quatre points de moindre portée : morbidité propre de la thyroïdectomie et
récidive du kyste après ponction (goitre), triade céphalées-palpitations-sueurs
et son caractère paroxystique (phéochromocytome), lung sliding / lung point et
récidive 30-50 % / 50-70 % (pneumothorax), mortalité la plus élevée des maladies
psychiatriques (anorexie).

**Aucun de ces quinze points n'est venu de `report_redundancy.py`.** Trois sont
sur des grilles qui mesuraient 0 ou 1 paire.

### ⚠️ Ce que la mesure ne voit pas — chiffré sur 35 grilles

Recouvrement de vocabulaire (jetons > 2 lettres, mots-outils retirés), état
`e54b127` :

| couple | items inclus à ≥ 90 % dans **un seul** item cible | dont **invisibles** (ratio ≤ 0,72) | paires effectivement mesurées |
|---|---|---|---|
| `theorie → therapy` | **97** | **91 (94 %)** | 14 |
| `expert → theorie` | **40** | **10 (25 %)** | 81 |

**Sur `theorie ↔ therapy`, la mesure voit environ une inclusion sur dix** — pire
encore que le tiers annoncé par k5a. Longueurs moyennes du lot : `theorie` 79
caractères (n = 2 022), `expert` 80 (n = 1 051) — **k4 avait raison sur
`expert ↔ theorie`**, dont les deux blocs ont le même grain, mais **25 % des
inclusions intégrales y restent tout de même invisibles** : un item d'`expert`
peut être un extrait exact d'un item de `theorie` deux fois plus long
(« IRM = examen de référence pour l'extension », inclusion 1,00, ratio 0,65).
Ces 10 items n'ont **pas** été traités : la consigne était de ne traiter que les
doublons mesurés.

### Deux corrections factuelles

1. **Souffle de la sténose aortique** (`AMC-Chir4-ECG6`). La grille écrivait
   « souffle HOLOSYSTOLIQUE 4/6 au 2e EIC droit » dans `annexe-dd`, `expert` et
   `defi`. Le souffle du rétrécissement aortique est **mésosystolique
   éjectionnel** ; « holosystolique » désigne l'insuffisance mitrale, la CIV,
   l'insuffisance tricuspide — c'est-à-dire exactement les diagnostics dont il
   fallait le distinguer. Corrigé aux trois endroits (aucun dans une section
   notée), et l'auscultation complète portée dans `theorie`, qui n'en disait
   rien du tout.
2. **Seuil fébrile de la pyélonéphrite obstructive** (`AMC-Chir6-ARC1`). La
   grille écrivait « fièvre + colique = pyélonéphrite obstructive » sans seuil ;
   la page SSP est explicite et chiffrée (« > 38,5 °C + frissons »).
   **SSP explicite → elle fait foi** ; le seuil est porté dans `theorie`.

### Niveau 1 — 27 pages SSP, cinq rendements

Les 35 grilles sont couvertes par **27 pages SSP** (couverture 35/35). Extraction
automatique des lignes chiffrées de chaque page, comparaison à l'ensemble du
texte visible de la grille desservie, puis lecture des candidats.

**Rendement.** *Colique néphrétique* : le seuil de 38,5 °C (§ ci-dessus).
*Entorse de cheville* : la **lésion de Maisonneuve** — 0 occurrence dans toute la
grille, alors que la page SSP la porte en image dédiée et que les critères
d'Ottawa ne couvrent pas le péroné proximal. *TCA* : les seuils de gravité
chiffrés (IMC < 14, bradycardie < 40/min, K⁺ < 2,5 mmol/L, Na⁺ < 125 mmol/L,
QTc > 500 ms) et le **syndrome de renutrition** (phosphore < 0,3 mmol/L), là où
la grille n'avait que « hypophosphatémie » ; plus la mortalité **5-10 %**.
*HBP* : le clampage **par paliers de 500 mL**, absent d'une grille qui ne disait
que « drainage progressif ». *TVP* : le piège SSP de la dermohypodermite qui ne
s'améliore pas à **48 h**.

**Rendement nul, et c'est un résultat.** Les 22 autres pages n'ont produit aucun
ajout. Deux causes distinctes, à ne pas confondre :

* les pages **larges et partagées** (*Douleur Thoracique* dessert 4 de mes
  grilles, *Dyspnée* 2) sont déjà concordantes sur leurs cibles chiffrées ;
* les pages **hors sujet de la grille** : *Douleur de Genou* ne traite pas
  l'ostéosarcome, *Adénopathie* ne traite pas la masse médiastinale,
  *Toux Chronique* ne traite pas le nodule pulmonaire solitaire. Comme les trois
  pages du lot k5a, elles ne citent la grille que par son titre. Le mapping les
  relie par le **motif de plainte**, pas par le diagnostic.

L'indicateur du pilote se vérifie une troisième fois : le rendement suit les
**cibles chiffrées**, jamais la largeur de la page.

### Non corrigé, documenté (règle 3)

* **Trois grilles de la série `AMC-ECOS1-*` citent le droit québécois.**
  `AMC-ECOS1-S5` (HSA) construit toute sa section de capacité de discernement sur
  la **garde préventive** et la *Loi sur la protection des personnes dont l'état
  mental présente un danger* — 9 occurrences, dont **3 dans la section notée**.
  `AMC-ECOS1-S1` cite le Québec dans `theorie` et `defi`, `AMC-ECOS1-S4` dans
  `scenario` ; « civière » apparaît dans `AMC-ECOS1-S10` et dans une grille hors
  lot. L'équivalent suisse est le **placement à des fins d'assistance
  (art. 426 ss CC)**. `check_nomenclature.py` ne voit rien : sa table porte sur
  les unités, les médicaments et les sigles, pas sur les institutions. **Le
  barème étant concerné, la correction est un arbitrage, pas une réécriture.**
* **`AMC-Chir5-ECG4`** garde 3 paires `redflags ↔ theorie` qui sont l'artefact
  d'étiquettes numérotées (§ ci-dessus) et 3 paires `theorie ↔ therapy` où
  `theorie`/Rappels décalque `therapy`. Le contrat interdit de toucher la section
  notée et exige que le canonique porte le champ : la paire est irréductible.
* **`AMC-Chir6-ARC1`** garde une paire `cloture ↔ theorie` à 0,73. Vérification
  faite, l'item de `cloture` est un `exemple-phrase` de « Réponses types du
  candidat » : c'est bien de l'oral, à sa place.

### Barème

**Intact.** Vérifié par mesure sur le diff complet : **0 ligne** touchant
`criteria-text`, `detail-text`, `maxScores`, `sectionInfo`, `coef`,
`<span class="score">`, `therapy-item`, `redflags-*`, `cloture-detail`,
`exemple-phrase`, `caseConfig`, `scoring.js` ou `persistence.js`. Sur 166 lignes
modifiées, **162 sont des `<li>`** de `expert` ou `theorie` ; les 4 autres sont
les deux corrections « holosystolique » (dans `annexe-dd` et `defi`).
**Règle 1** — pas de régénération du baseline, et `check_invariants.py` le
confirme.

### Anti-perte

`check_no_loss.py e54b127` signale **19 disparitions sur 28 grilles**, toutes
verdictées : **9 reformulations en place** (l'item existe, allongé pour recevoir
ce qui lui manquait) et **10 suppressions dans `expert` dont le contenu avait été
porté dans `theorie` au préalable**. Contrôle indépendant par ensembles d'items
normalisés extraits de `git show e54b127:…` : **6 108 items avant, 6 066 après**,
delta net **−42**. Les autres suppressions ne sont pas signalées parce que
`theorie` en porte déjà un appariement au-dessus du seuil — la condition même
qu'on s'était donnée pour supprimer. **Aucune perte.**

### Contraintes respectées

* Rien écrit hors de `cases/casecos/`, de ce journal et du rapport k5b.
  **`scripts/casecos/` non modifié** : le contrat de k4 a tenu sur 35 grilles de
  plus, sans amendement.
* **Aucun `git add`** — commit par `git commit -- <chemins>` exclusivement.
  Rien touché sous `cases/german/`, `cases/rescos-locales/`, `scripts/german/`,
  `scripts/rescos-locales/`, où l'utilisateur travaillait en parallèle.
* **Aucune grille lue en entier avec `Read`** : bornes par `lib.top_spans()`,
  lecture par fenêtres `offset`/`limit`, édition par remplacement exact.
* **Aucun `grep` brut employé comme contrôle** : tous les chiffres publiés
  viennent des scripts de `scripts/casecos/` ou de mesures Python passant par
  `lib.visible_text()` / `lib.top_spans()` / `lib.matches()` (stdlib seule).
* Vault Obsidian lu en **lecture seule** (27 pages SSP), rien écrit hors du dépôt.
* Aucune commande réseau, aucun `git push`, aucun `git gc`, aucun `git prune`,
  aucun `timeout`, aucun `snapshot_invariants.py`.

---

## Lot k5c — grilles 61 à 100, plus la correction transversale de droit

Base `741cd86`, branche `refonte-amboss-suisse`. Troisième lot de production
CasECOS (`lib.grids()[60:100]`), assorti d'un balayage juridique sur les 198.

**27 des 40 grilles du lot modifiées, plus 7 grilles hors lot au titre du droit.
Redondance inter-blocs du lot 94 → 41 (−56 %), dont `expert ↔ theorie`
46 → 0 (−100 %).** Sept trous du canonique comblés, quatre corrections
factuelles ou institutionnelles, un typo.

| porte | avant | après |
|---|---|---|
| `check_invariants.py` | rc 0 | **rc 0 — 198 grilles** |
| `check_nomenclature.py` | rc 0 | **rc 0** |
| `check_reachability.py` | 198/198 | **198/198 à 100 %** |
| `report_redundancy.py` (lot de 40) | **94 inter** | **41 inter** |
| `check_no_loss.py 741cd86` | — | **11 disparitions, 11 verdictées** |
| `scripts/amboss/report_redundancy.py --quiet` | **147** | **147** |
| `scripts/rescos/report_redundancy.py --quiet` | **127** | **127** |
| `scripts/amboss` · `scripts/rescos` `check_invariants` | rc 0 | **rc 0** |

### Volet A — le droit québécois corrigé, section notée comprise

L'arbitrage rendu par l'utilisateur après k5b : **c'est une erreur factuelle**,
au même titre que la « tutelle » abolie corrigée sur AMBOSS-17. Un étudiant
suisse ne doit pas apprendre une procédure qui n'existe pas chez lui.

**Source vérifiée avant écriture** : `SSP — Capacité de Discernement & Éthique`
et `SSP — Urgences Psychiatriques (Agitation, PAFA)` du vault. Éléments retenus :
PAFA art. 426-439 CC ; trois conditions cumulatives (trouble psychique,
déficience mentale ou grave état d'abandon · assistance impossible autrement ·
nécessité d'un placement en institution adaptée) ; décision par l'**APEA/KESB**
(art. 428 CC) **ou par un médecin habilité par le canton** en urgence
(art. 429 CC) ; **6 semaines** au maximum pour le PAFA médical ; **recours au
tribunal cantonal dans les 10 jours** (art. 439 CC) ; traitement sans
consentement art. 434 CC ; contention art. 383-385 CC ; cascade des
représentants art. 377-378 CC ; urgence vitale art. 379 CC ; mineur capable de
discernement art. 19c CC, **sans âge minimum fixe**.

**Six corrections, sur sept grilles :**

1. **`AMC-ECOS1-S5`** (HSA, 9 occurrences). Les **3 de la section notée** —
   `criteria-description` de `m5`, `detail-text` de `m5-detail-2`,
   `scoring-rule` de `m5` — corrigées en PAFA sans toucher à la structure
   (4 sous-items avant, 4 après) : **règle 1**. Les 6 autres, dans `expert`,
   `theorie` et `defi`, corrigées de même. Le canonique reçoit en outre la
   cascade art. 377-378, l'urgence vitale art. 379 et les droits du patient sous
   PAFA (recours 10 jours) : la grille disait « faire intervenir le représentant
   légal ou le mandataire désigné », formule qui n'est celle d'aucun droit.
2. **`AMC-ECOS1-S1`** (anorexie, mineure de 16 ans). « Au Québec, à 14 ans et
   plus, un mineur peut consentir seul » → art. 19c CC, capacité appréciée au
   cas par cas et pour chaque décision (présumée absente avant 12 ans, évaluée
   de 12 à 15, présumée de 16 à 18). Corrigé dans `theorie` et dans `defi`.
   « Élève de **secondaire 4** » → « 3ᵉ année du gymnase », gloss que la grille
   jumelle `Anorexie boulimie - Adolescente 16 ans` portait déjà.
3. **`AMC-ECOS1-S4`** : « vaccins à jour selon le **calendrier québécois** » →
   « plan de vaccination suisse (OFSP) ».
4. **`PLAFA` → `PAFA`, 11 occurrences sur 2 grilles**
   (`AMC-Chir1-MedLeg` 4, `HSA et refus de soins` 7). **PLAFA** =
   *privation de liberté à des fins d'assistance*, terme de l'ancien droit
   (art. 397a ss aCC) **abrogé le 1er janvier 2013**. Les deux grilles écrivaient
   déjà « PLAFA (**Placement** à des fins d'assistance, art. 426-439 CC) » :
   l'acronyme de l'ancien régime collé au développé et aux articles du nouveau.
   Univoque.
5. **`APAE` → `APEA`, 2 grilles** (`AMC-Chir1-MedLeg`, `HSA et refus de soins`).
   Inversion de lettres ; l'autorité est l'**Autorité de protection de l'enfant
   et de l'adulte**. Univoque. Une occurrence était dans un `criteria-text`
   (« 3. Rôle de l'autorité de protection de l'adulte (APAE / KESB) — Genève ») :
   correction en place, format `N. Libellé` préservé.
6. **La tutelle de l'adulte, abolie en 2013, subsistait sur 2 grilles.**
   `AMC-Psy-P1` écrivait « Qui peut décider : médecin habilité (selon canton),
   tribunal, **tuteur légal** » — doublement faux, puisqu'un curateur n'a pas non
   plus compétence pour ordonner un PAFA. Remplacé par APEA (art. 428 CC) /
   médecin habilité (art. 429 CC), avec la mention explicite de l'abolition. La
   même grille nommait l'instrument « hospitalisation non volontaire (HNV) »
   sans jamais écrire *PAFA* : le nom suisse a été porté dans le chapeau, et le
   délai de recours de 10 jours ajouté aux droits du patient. `AMC-Psy-P4`
   écrivait « le représentant légal (**tuteur ou curateur**) » deux fois, et
   « [tuteur, curateur ou parents] » dans un `patient-response` de la section
   notée, alors que la même grille dit ailleurs « curatelle de représentation ou
   de portée générale selon la législation suisse ». Corrigé.

### Volet A — ce que le balayage a trouvé d'autre, et qui n'est pas corrigé

Balayage des 198 grilles sur 46 motifs (lois cantonales et étrangères, garde
préventive, P-38, curateur public, majeur protégé, tutelle, sauvegarde de
justice, directives anticipées, numéros d'urgence, organismes nationaux), par
`lib.visible_text()` et `lib.top_spans()`.

**Le corpus est très majoritairement conforme.** Les 86 occurrences de
« directives anticipées » sur 11 grilles sont toutes rattachées aux
art. 370-373 CC ; les 44 « représentant thérapeutique » à l'art. 378 CC ; les
80 numéros d'urgence sont **144 / 117 / 143 / 145**, jamais 911, 15, 18 ni SAMU.
`P-38`, `curateur public`, `majeur protégé`, `sauvegarde de justice`,
`habilitation familiale`, `CLSC`, `CHSLD`, `RAMQ` : **0 occurrence**. `EHPAD`,
`SAMU` et `911`, présents au relevé k1, ont disparu avec la passe de
nomenclature.

**Consigné, non corrigé** (arbitrage d'auteur, hors périmètre du lot) :

* **Associations de patients françaises proposées à des patients suisses**, 4
  grilles hors lot : *Association Française contre les Myopathies (AFM)*
  (`AMC-Neuro-P4`), *France Alzheimer* ×2 (`AMC-Psy-S4`), *AFDIAG* (`UIDC-Lea`),
  *France Lynch* (`UIDC-Monsieur Dupont`). Les équivalents suisses existent
  (Alzheimer Suisse, ASRIMC, Ligue suisse contre le cancer) mais le choix d'une
  ressource associative est éditorial, pas factuel.
* **`HAS` (agence française), 7 occurrences sur 3 grilles.** Deux sont
  correctement étiquetées comme françaises ou internationales
  (`Anorexie boulimie` : « critères suisses SSPP / françaises HAS /
  internationales MARSIPAN » ; `AMC-Psy-P3` : « recommandations HAS, NICE,
  APA »). La troisième, `AMC-MCPR-ARC20` (dans le lot), écrivait « critères
  GLIM 2018 / HAS 2021 » sans attribution : **corrigée** en « critères
  internationaux GLIM 2018, repris par la HAS française en 2021 — la Suisse ne
  publiant pas de critères propres ». C'est une qualification de source, pas un
  changement de contenu.
* **« civière », 2 occurrences** (`AMC-ECOS1-S10`, `HSA avec convulsion`) : mot
  du français standard, employé aussi en Suisse ; « brancard » y est plus
  courant sans que « civière » soit fautif. Non corrigé.
* **`UIDC-Monsieur H. Toinnes`** situe sa vignette « en vacances dans le
  Sud-Ouest de la France » et cite l'art. 5 al. 3 K 1 30 (loi genevoise sur la
  santé) : le décor est étranger mais le droit cité est suisse. Incohérence de
  mise en scène, pas d'enseignement faux.
* **`Anorexie boulimie - Adolescente 16 ans`** garde « Secondaire 4 » sans gloss
  dans un `criteria-detail`, alors que son en-tête porte déjà « (3e année du
  gymnase) ». Hors lot, section notée : laissé.

### Volet B — `expert ↔ theorie` : 46 → 0

Le motif de k5a et k5b se reproduit une troisième fois sans exception :
`expert`/Points clés est un **cours en réduction** dont `theorie` porte déjà,
plus richement, la totalité. Règle appliquée, inchangée : un item d'`expert`
n'est retiré que si (a) le test du référent l'attribue à `theorie`, (b) `theorie`
porte son contenu **intégral** — vérifié terme à terme, en portant d'abord dans
`theorie` ce qui lui manquait — et (c) `expert` garde le comportement observable
correspondant dans `Rôles` ou `Pièges`.

**23 items retirés de `expert`, 15 spécialisés, 2 ports préalables dans
`theorie`** (« droit de communiquer avec un avocat » sur `AMC-EthiqueLegale-V5`,
« et le désir de la patiente » sur `AMC-GynObs-V3`).

Une figure de spécialisation s'est imposée ici plus qu'aux lots précédents : le
**piège qui nie le canonique**. `AMC-GynObs-V5` portait, en Points clés, « La
corticothérapie fœtale est PRIORITAIRE avant tout accouchement prématuré » et,
en Pièges, « Oublier la corticothérapie de maturation pulmonaire fœtale » — les
deux mesurés contre la même ligne de `theorie`/Conclusion. Retirer le premier ne
suffit pas : le second reste un décalque nié. La sortie est de le rendre
**observable dans cette station** : « Laisser partir la patiente en salle de
naissance sans avoir prescrit la bétaméthasone ». Onze pièges ont été traités
ainsi.

`AMC-EthiqueLegale-V5` est le cas extrême : sa `theorie`/Conclusion recopiait
**mot pour mot** quatre des huit Points clés d'`expert` (deux paires à **1,00**).

**Les 41 paires restantes n'appartiennent plus qu'à des couples structurels** :
`annexe-dd ↔ theorie` 17 (le bloc ne se nettoie pas — 97,5 % de formulations
distinctes au relevé k1), `theorie ↔ therapy` 7 et `redflags ↔ theorie` 5 (le
barème ne se dédoublonne pas), `annexe-dd ↔ expert` 6,
`annexe-dd ↔ redflags` 6 (artefact de négation).

### Volet B — sept trous du canonique

Instrument de k4/k5a/k5b : appariement à seuil abaissé (0,45) entre
`therapy`/`redflags` et les blocs de restitution, en retenant ceux dont le
meilleur appariement est **ailleurs que dans `theorie`**, puis comptage du terme
bloc par bloc sur le texte visible.

| grille | point absent du canonique | vivait dans |
|---|---|---|
| `AMC-ECOS1-S9` Fracture vertébrale | **syndrome de la queue de cheval** (0 occ. dans `theorie`) et **spondylodiscite** (0 occ.) — les deux drapeaux rouges de la dorsalgie | `redflags` + `expert` / `annexe-dd` |
| `AMC-MCPR-ARC6` Douleur thoracique | **dissection aortique** (0 occ.) et **score de Wells** (0 occ.) : `theorie` enseignait la probabilité pré-test sans jamais nommer l'urgence à écarter d'abord | `annexe-dd` + `redflags` |
| `AMC-MCPR-ARC15` Entorse de cheville | **lésion de Maisonneuve** — 0 occurrence dans **toute** la grille | nulle part |
| `AMC-MCPR-ARC17` Diabète | **pied diabétique** (0 occ. dans `theorie`) et le message « contrôler tous les FRCV compte autant que la glycémie » | `redflags` seul |
| `AMC-MCPR-ARC14` Claire, 15 ans | **infirmière scolaire** (0 occ. dans `theorie`) : le seul relais que l'adolescente peut atteindre seule | `therapy` + `expert` |
| `AMC-MCPR-ARC2` Arthrite goutteuse | seuil fébrile **38,5 °C** de la monoarthrite septique (0 occ. dans la grille) | page SSP |
| `AMC-MCPR-ARC6` Douleur thoracique | épidémiologie **dépendante du lieu** : pariétale 1 fois sur 2 et CV 16 % en premier recours, CV 54 % aux urgences — dans une station intitulée « au cabinet médical » | page SSP |

**Aucun n'est venu de `report_redundancy.py`.** Trois sont sur des grilles qui
mesuraient **0 paire** (`AMC-ECOS1-S9`, `AMC-MCPR-ARC14`, `AMC-MCPR-ARC17`).
Deux — le pied diabétique et l'infirmière scolaire — sont **du rationnel logé
dans un « Détails : »** de `therapy-item` : le motif du § 3.3 de k4 se confirme
pour la quatrième fois.

**La lésion de Maisonneuve est trouvée pour la deuxième fois.** k5b l'avait
comblée sur `AMC-Chir3-Vignette3` ; `AMC-MCPR-ARC15` est **la même station
dupliquée dans la série MCPR** et portait le même trou. La page SSP
*Entorse de Cheville* lui consacre une image dédiée
(`pied-cheville-lesion-de-maisonneuve.png`). Les limites d'application des
critères d'Ottawa (moins de 18 ans, intoxication, polytraumatisme, déficit
sensitif, traumatisme de plus de 10 jours) étaient absentes de la même grille et
ont été portées dans le même geste.

### Volet B — la mesure d'inclusion, reconduite

Recouvrement de vocabulaire (jetons > 2 lettres, mots-outils retirés) sur les
40 grilles, avant et après :

| couple | inclusions ≥ 90 % | dont **invisibles** (ratio ≤ 0,72) | paires mesurées |
|---|---|---|---|
| `theorie → therapy` avant | 64 | **60 (93 %)** | 7 |
| `theorie → therapy` après | 64 | **60 (93 %)** | 7 |
| `expert → theorie` avant | 10 | 6 (60 %) | 46 |
| `expert → theorie` après | **6** | **6 (100 %)** | **0** |

Deux lectures. La première confirme k5b au chiffre près : **la mesure ne voit
qu'une inclusion `theorie ↔ therapy` sur dix** (93 % ici, 94 % chez k5b).
La seconde est nouvelle : après traitement, **la totalité du résiduel
`expert → theorie` est invisible**. Le seuil de 0,72 a été poussé jusqu'à son
plancher sur ce couple ; ce qui reste ne peut plus être atteint que par la mesure
d'inclusion. Six items, à publier **à part** du chiffre de redondance.

### Niveau 1 — 26 pages SSP, deux rendements

39 des 40 grilles sont desservies par **26 pages SSP** ; `AMC-MCPR-ARC21`
(bilan préopératoire) n'a **aucune page** — c'est le premier trou de couverture
rencontré sur ce corpus. Méthode inchangée : extraction des lignes chiffrées,
comparaison au texte visible complet, lecture des candidats survivants.

**Rendement : deux pages.** *Douleur de Genou* → le seuil de 38,5 °C.
*Douleur Thoracique* → l'épidémiologie dépendante du lieu (16 % / 54 %).
*Entorse de Cheville* a confirmé la lésion de Maisonneuve déjà trouvée par
l'usage inversé.

**Deux quasi-rendements écartés, et c'est le point de méthode.** La page
*Diarrhée* donne un seuil de calprotectine de **150-250 µg/g** ; la grille
`AMC-MCPR-ARC16` en donne un autre, articulé (< 50 VPN, 50-200 zone grise,
> 200 endoscopie), plus fin et non contradictoire. La page
*Diabète Gestationnel* donne « césarienne si EPF > **4250-4500 g** » ; la grille
`AMC-GynObs-V12` écrit « > 4 000-4 500 g », intervalle plus large qui contient
le premier. **Divergence n'est pas contradiction** : rien n'a été forcé.

**Rendement nul sur 23 pages.** Les causes de k5a et k5b se reproduisent :
pages larges déjà concordantes (*Capacité de Discernement* dessert 3 grilles,
*Dyspnée* 3, *Grossesse* 3, *Counselling Dépistages* 3), et pages reliées par le
**motif de plainte et non par le diagnostic** (*Douleur - Masse Pelvienne* pour
une GEU, *Dyspnée* pour une anémie ferriprive sur AINS). L'indicateur tient une
quatrième fois : le rendement suit les **cibles chiffrées**, pas la largeur.

### Correction typographique

`AMC-MCPR-ARC12` portait « (risque de rash**))** » — parenthèse fermante
doublée, dans un `<li>` d'`expert`. Corrigé.

### Barème

**Intact, et cette fois des sections notées ont été touchées.** Cinq grilles ont
reçu une correction dans leur zone notée — `AMC-ECOS1-S5` (3 sites :
`criteria-description`, `detail-text`, `scoring-rule`), `AMC-Chir1-MedLeg`
(1 `criteria-text` + 6 `criteria-detail`), `HSA et refus de soins`
(`therapy-section`, `criteria-detail`, `scoring-rule`), `AMC-Psy-P4`
(`patient-response` d'un `criteria-detail` + `therapy`/Détails),
`AMC-MCPR-ARC20` (une `criteria-description`).

**Aucune n'a changé de structure**, et c'est mécaniquement prouvé :
`check_invariants.py` compare `criteriaCount`, `detailCount`, `radioCount`,
`checkboxCount`, `maxScores`, `coef`, `scoreSpans`, `sectionCounts` et `blocks`
au baseline gelé, et il est **vert sur les 198**. Le format
`N. Libellé [réponse]` exigé par `cases/scoring.js:159` est préservé sur les
2 `criteria-text` touchés. **Règle 1 partout — pas de régénération du baseline.**
Sur 175 lignes de diff : 0 touchant `maxScores`, `sectionInfo`, `coef`,
`<span class="score">`, `caseConfig`, `scoring.js`, `persistence.js`,
`therapy-item`, `redflags-text`, `redflags-description`, `cloture-detail` ou
`exemple-phrase`.

### Anti-perte

`check_no_loss.py 741cd86` signale **11 disparitions sur 34 grilles modifiées**,
toutes verdictées et **toutes des reformulations en place** : l'item existe
toujours, corrigé (Québec → PAFA, tuteur → curateur, calendrier québécois → OFSP)
ou allongé pour recevoir ce qui lui manquait (macro-angiopathie + FRCV, arthrite
septique + 38,5 °C, droits du patient + 10 jours).

Contrôle indépendant par comptage d'items normalisés extraits de
`git show 741cd86:…` et de l'arbre de travail : **5 418 items avant, 5 403
après**, delta net **−15**, qui s'explique exactement : **−23** retraits dans
`expert`, **+8** ajouts dans `theorie` (7 trous du canonique + les limites
d'Ottawa). Les 23 retraits ne sont pas signalés par `check_no_loss` parce que
`theorie` en porte déjà un appariement au-dessus du seuil — la condition même
qu'on s'était donnée pour les autoriser. **Aucune perte.**

### Contraintes respectées

* Rien écrit hors de `cases/casecos/`, de ce journal et du rapport k5c.
  **`scripts/casecos/` non modifié** : le contrat de k4 a tenu sur 40 grilles de
  plus, et sur une correction en section notée, sans amendement.
* **Aucun `git add`** — commit par `git commit -- <chemins>` exclusivement.
  Rien touché sous `cases/german/`, `cases/rescos-locales/`, `scripts/german/`,
  `scripts/rescos/`, où l'utilisateur travaillait en parallèle.
* **Aucune grille lue en entier avec `Read`** : bornage par `lib.top_spans()`,
  lecture par fenêtres `offset`/`limit`, édition par remplacement exact.
* **Aucun `grep` brut employé comme contrôle** : tous les chiffres publiés
  viennent de `scripts/casecos/` ou de mesures Python passant par
  `lib.visible_text()`, `lib.top_spans()`, `lib.matches()` (stdlib seule).
* Vault Obsidian lu en **lecture seule** (26 pages SSP + 2 pages de droit),
  rien écrit hors du dépôt.
* Aucune commande réseau, aucun `git push`, aucun `git gc`, aucun `git prune`,
  aucun `timeout`, aucun `snapshot_invariants.py`.
