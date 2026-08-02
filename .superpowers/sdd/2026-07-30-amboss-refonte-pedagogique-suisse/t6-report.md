# t6 — Vérification finale du corpus `cases/rescos-locales` (165 grilles)

Branche `refonte-amboss-suisse`, base d'import `7c77e3e`, état vérifié
`45e0986`. **Aucun fichier sous `cases/` n'a été modifié** — vérifié :
`git status --porcelain -- cases/rescos-locales` rend zéro ligne. Rien lu, écrit
ni exécuté sous `cases/german/`, `scripts/german/`, `cases/casecos/` ni
`scripts/casecos/`. Aucun `git add` : validation par
`git commit -F <fichier> -- <chemins>`. `core.quotepath=false` partout.

Livrable : `docs/superpowers/rapport-rescos-locales-2026-08.md`.

---

## Résultat des six vérifications

**Aucune n'échoue.**

| # | vérification | résultat |
|---|---|---|
| 1 | les sept vérificateurs sur les 165 | **code 0** — invariants, nomenclature, atteignabilité (156/156 notées à 100 %, 9 feuilles porte) ; `bounds_anomalies` / `uncovered_content` **[] / {}** recalculés sur les 165 |
| 2 | barème, 14 champs × 165 vs `7c77e3e` | **313 divergences sur 2310, toutes admises** : 156 `engineFingerprint`, 156 `configForm`, 1 `coef` (RESCOS-63). **Les 11 autres champs : 0 divergence sur les 165** |
| 3 | intégrité structurelle | **0 problème** — `<!DOCTYPE>`/`<html>`/`</body>`/`</html>` 165/165 · 19 balises à conteneur appariées, 0 déséquilibre · blocs et segments conformes au snapshot (1466 segments) · `.criteria-text` format « N. Libellé » 0 écart · **crochets `[…]` de `cloture` : 464 à `7c77e3e`, 464 sur disque, 0 grille ne bouge** |
| 4 | redondance | **1258 → 1003** (−255, −20,3 %). Le 1258 a été **remesuré avec l'outillage courant** sur les blobs de `7c77e3e` : identique au chiffre publié par `l2`. Témoins **AMBOSS 147**, **RESCOS 127** |
| 5 | non-perte, `check_no_loss 7c77e3e` | 423 items / 87 grilles ; **0 perte réelle** après verdict. 0 item de la famille « protection » |
| 6 | navigateur `--deep`, 165 grilles | **0 exception**, 165/165 sans erreur, **156/165 à 100 %**, **`ecos_registry` 156/165**, minuteur 156/165, barre nav 156/165, **recouvrement 0/165**, crochets colorés 155/165. **RESCOS-63 sondée seule : 100 %, note A, registre écrit** |

Chaque témoin a été relevé dans **son propre interpréteur**. Le piège signalé par
`t5` s'est présenté : un `sys.path.insert(0, …)` mal ordonné a fait charger le
module AMBOSS pour une mesure RESCOS. **L'assertion sur `report_redundancy.__file__`
l'a arrêté net** ; sans elle le chiffre publié aurait été faux et cohérent.

### Détail des chiffres de la vérification 6

```
grilles sondées               : 165        sans exception ni erreur   : 165/165
à 100 % après remplissage     : 156/165    écrivant ecos_registry     : 156/165
minuteur 13:00 -> autre       : 156/165    barre nav présente + fixed : 156/165
recouvrement barre/minuteur   : 0/165      exceptions phase --deep    : 0/165
sans aucun crochet coloré     : 10/165  = 9 feuilles porte + RESCOS-64 station double 2
```

Les 9 grilles hors barème sont **exactement** les 9 feuilles porte, nommées dans
le rapport. `RESCOS-64 station double 2` n'a aucun critère portant de
`patient-response` : état antérieur, pas une régression.

---

## Défauts trouvés — cinq, aucun réparé

Le mandat était de vérifier. Aucun de ces constats n'invalide une vérification.

1. **`Enfant qui boîte` qualifie une CRP à 20 mg/l de « normale » en cinq
   endroits, dont un sous-item noté.** Le lot `t3` a corrigé **un seul** de ces
   endroits, dans l'`annexe-dd`, en y écrivant « elle n'est pas normale (norme
   5-10 mg/l) ». Les quatre autres subsistent : `criteria-detail` noté
   « CRP [20 mg/l - normale] » · `annexe-dd`/Ostéomyélite « CONTRE : … CRP
   normale » · récit « une biologie normale (GB 8 G/L, CRP 20 mg/l, VS
   normale) » · différentiel « arthrite septique (mais CRP normale…) » · carte
   SBAR « (déjà faits : épanchement, CRP normale) ». **La grille se contredit
   avec elle-même et la version fausse est majoritaire.** Défaut le plus net du
   balayage.
2. **`AMC Urgences 3B` — nitrés sans la réserve du ventricule droit, dans deux
   sous-items notés.** « Dérivés nitrés IV si TA le permet » et « Vasodilatateurs
   (nitrés IV) si TA > 110 mmHg », plus la même formule dans `theorie` ;
   **0 occurrence** de « ventricule droit », « V3R », « V4R » ou
   « précharge ». **Quatrième occurrence** du motif corrigé sur AMC 3A (`t1`),
   `Douleur thoracique - Vignette` (`t2`) et `Douleurs thoraciques - DRS`
   (`t3`) ; aucun lot ne l'a vue ici. La grille est un NSTEMI Killip III.
3. **La ranitidine est sur deux grilles, pas une.** `t5` a consigné celle
   d'`Urticaire allergique` (`therapy`). `Choc anaphylactique - Femme de 28 ans`
   porte « Anti-H2 [ranitidine 50mg IV] » **dans un sous-item noté** — molécule
   retirée du marché mondial en 2020 (NDMA), inexistante en Suisse. Jamais
   signalée.
4. **37 unités non suisses, invisibles à `check_nomenclature`.** 29 valeurs en
   litre minuscule (`mmol/l`, `g/l`, `mg/l`, `µmol/l`, `UI/l`) sur 9 grilles, et
   8 gaz du sang en mmHg sur 4 grilles ; la plupart dans des sous-items notés.
   La porte rend 0 : elle borne les **analytes**, pas les **unités**. `l6b` en
   avait consigné 11 ; le balayage élargi en trouve 37.
5. **Candidat non tranché** : `Pédiatrie — État fébrile sans foyer` range « pas
   de boiterie » CONTRE l'arthrite septique et « pas de douleur osseuse
   localisée » CONTRE l'ostéomyélite, chez un nourrisson fébrile sans foyer.
   Même famille que le défaut corrigé par `t4` sur `Nourrisson 6 mois avec
   fièvre`, moins net ; signalé, non jugé.

**Contrôles de résidu qui, eux, sont propres** : `ARS`, « en France », « appeler
le 15 », `Doliprane` → **0 occurrence** (hors deux mentions délibérément
contrastives). Aucune nouvelle occurrence du motif « tératogène sans un mot de
contraception » : les six grilles qui nomment encore un tératogène ont pour
patient un homme ou une femme hors âge de procréer.

---

## Ce que la vérification a mesuré en propre

* **Barème** — snapshot des 14 champs reconstruit depuis les blobs de `7c77e3e`
  (avec application du renommage `RESCOS-69 → RESCOS-69b` avant comparaison) et
  confronté au disque : 2310 comparaisons, 313 divergences, **aucune inattendue**.
  Les huit corrections faites dans une section notée aux lots `t1` à `t4` ne
  déplacent aucun champ — `criteriaCount`, `detailCount`, `radioCount`,
  `checkboxCount` identiques sur les 165.
* **Redondance à l'origine, remesurée** — `report_redundancy` de `rescos-locales`
  appliqué aux blobs de `7c77e3e` avec l'outillage courant : **1258**, exactement
  le chiffre publié par `l2`. La comparaison 1258 → 1003 est donc valide dans les
  deux outillages.
* **Ampleur de `e8bd11e` (ligatures œ/æ dans `norm()`)**, mesurée corpus par
  corpus en rejouant `report_redundancy` avec l'ancienne implémentation :

  | corpus | avant | après | écart | grilles déplacées |
  |---|---:|---:|---:|---|
  | AMBOSS | 147 | 147 | **0** | **2** (AMBOSS-15 8→7, AMBOSS-19 9→10) |
  | RESCOS | 127 | 127 | 0 | 0 |
  | `rescos-locales` | 1002 | 1003 | **+1** | 1 (`Urticaire allergique` 19→20) |

  `cases/german/` non mesuré (vérificateurs hors mandat). **Le total est neutre
  par compensation, pas par absence d'effet** : sur AMBOSS une grille perd une
  paire et une autre en gagne une. Un total stable ne prouve rien ; il faut le
  relevé par grille.
* **Composition des 1003 paires** — `presentation` est présente sur **57
  grilles sur 165** (et non 46 : le 46 du mandat est la couverture d'
  `annexe-image`). **914 des 1003 paires** sont portées par ces 57 grilles ; les
  108 autres s'en partagent **89**. Échantillon de 22 grilles / 183 paires lu un
  par un : plancher structurel (le signe discriminant nommé par chaque bloc dans
  sa fonction), clés de mnémo (une lettre préfixée suffit à créer la paire),
  `expert` face au reste, et synonymes rendus visibles par la passe de
  nomenclature. 33 paires identiques (ratio 1,0) dans l'échantillon, toutes du
  plancher structurel.
* **Motifs de `check_no_loss`** — volume par grille corrélé au gain de
  redondance, aucune grille hors logique ; filtrage sur cinq familles sensibles
  (dose 41, seuil 11, contre-indication 17, drapeau rouge 4, **protection 0**),
  couverture lexicale mesurée sur les 69 items sensibles, 14 items sous seuil
  relus un à un et **tous retrouvés** sous une formulation plus riche.
* **État courant du corpus** — 20 147 items de contenu (contre 19 168 à
  l'import, **+979**), 1466 segments, 12 blocs, 22,4 Mo hors base64 (contre
  27,2), **0 `undefined` affiché**, **0 `<img>` morte** (11 base64 conservées).

---

## Préoccupations

**1. Les huit corrections en section notée n'ont pas de filet.** Elles sont
justes et prouvées inoffensives champ par champ, mais le contrôle qui le prouve
(`criteriaCount` / `detailCount` / `radioCount` / `checkboxCount` + le balayage
du `diff` sur les marqueurs de barème) est **manuel et refait à chaque lot**.
Rien ne l'exécute automatiquement. Le défaut n° 2 ci-dessus montre le coût :
trois lots ont corrigé le même motif, et la quatrième occurrence — dans un
sous-item noté — n'a été trouvée qu'ici, par balayage lexical corpus-large.

**2. Le balayage lexical corpus-large est le contrôle le plus rentable qui
reste.** Les cinq défauts trouvés par cette vérification l'ont tous été ainsi :
un motif (`ranitidine`, `nitr*` sans `ventricule droit`, `mmol/l`, `mmHg`,
`CRP … normale`) appliqué aux 165 grilles d'un coup. Aucun des six vérificateurs
ne le fait, et les onze lots ne l'ont fait que **dans leur périmètre**. C'est
exactement ce que le rapport CasECOS désignait comme « le travail le plus
rentable qui reste à faire sur l'ensemble du projet ».

**3. `check_nomenclature` a un angle mort d'unités, maintenant chiffré à 37.**
Le motif borne les analytes, pas les unités : `7g/dl` collé au chiffre (trouvé
par `l6b`), `mmol/l` en litre minuscule, `PaCO2 > 45 mmHg`. Le correctif relève
d'une passe de motif sur les quatre corpus, pas d'une retouche par corpus.

**4. La règle « une divergence en bloc noté se consigne » a produit 24
consignations, dont quatre erreurs de sécurité.** Sur huit lots consécutifs, le
motif ne s'atténue pas. Deux grilles du corpus enseignent deux doses différentes
du même antibiotique ; une grille prescrit une molécule retirée du marché en
2020 ; une autre prescrit un prokinétique à une obstruction complète. Le rapport
le dit : ce n'est plus une consignation, c'est un arbitrage à rendre sur la règle
elle-même.

**5. `RCI-Fièvre` — l'inclusion stricte a été rompue par le traitement.** Le lot
`t3` a traité la jumelle sans préfixe, qui porte désormais 4 items propres (les
quatre corrections de `t3`) ; `t5` les a reportées, mais le principe demeure :
**traiter une jumelle rompt l'inclusion qui justifiait de ne pas traiter
l'autre.** La suppression reste bloquée par le fait que `SSP — Douleurs
Articulaires` cite la version sans préfixe.

**6. Le corpus n'est toujours pas publié.** `index.html` ne référence aucune
grille de `cases/rescos-locales/`. Les 156 entrées d'`ecos_registry` sont écrites
mais pas affichées. Les `href` devront être percent-encodés : 132 des 165 noms
portent un accent, et `saveToRegistry()` construit sa clé depuis
`location.pathname`.

---

## Ce que ce lot n'a pas fait

* **Aucune modification sous `cases/`** — un seul fichier écrit,
  `docs/superpowers/rapport-rescos-locales-2026-08.md`.
* **Aucune réparation** des cinq défauts trouvés — le mandat était de les
  signaler.
* **Rien lu, écrit ni exécuté sous `cases/german/`, `scripts/german/`,
  `cases/casecos/` ni `scripts/casecos/`** ; leurs vérificateurs n'ont pas servi
  de référence, et la redondance de German n'a pas été mesurée.
* **Aucune lecture de grille entière avec `Read`** : tout passe par
  `strip_base64` puis `block_spans` / `visible_text` / `list_items` /
  `all_items`.
* **Aucun `grep` brut employé comme contrôle** : tous les balayages de contenu
  passent par `visible_text` sur le HTML débarrassé de ses data-URI, ce qui
  exclut par construction les `<style>`, les `<script>` et les commentaires.
  Les seuls motifs appliqués au HTML brut sont structurels (`<!DOCTYPE`,
  `</html>`, appariement de balises, `class="criteria-text"`), et ils masquent
  `<script>`, `<style>` et les commentaires avant de compter.
* **Aucun `git add`, aucun `git push`, aucune commande réseau, aucun `git gc`
  ni `git prune`, aucun `timeout`.**
