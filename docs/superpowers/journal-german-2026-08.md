# Journal de refonte — grilles German

Corpus : `cases/german`, 88 grilles. Outillage : `scripts/german/`.
Procédure : `scripts/german/PROCEDURE-german.md`, pendant de `scripts/amboss/PROCEDURE.md`.

Pendant du `journal-amboss-2026-07.md`, dont il reprend le format. Deux types
d'entrées :

- **Modification** — un changement appliqué, avec ce qui le justifie.
- **Divergence** — un écart repéré mais **non corrigé**, laissé à l'arbitrage.

## Format

    ### <passe ou grille> — <motif>

    **Modifications**
    - <bloc> · <sujet> : « <avant> » → « <après> »
      source : <référentiel — citation>

    **Divergences consignées**
    - <zone> · <sujet> : la grille dit « <x> » — non corrigé (<raison>)

## Entrées

### Volet A — Passe nomenclature suisse (tâche g2)

Mesure de départ, `check_nomenclature.py` au commit `4819f53` : **64 termes non
suisses**, 63 `NFS` dans 37 grilles et 1 `pg/mL` dans German-63. Après la passe,
**0**.

Script : `scripts/german/apply_lab_nomenclature.py`, écrit pour ce corpus.
`scripts/amboss/apply_lab_nomenclature.py` n'est **pas** modifié — il a produit
les mesures publiées d'AMBOSS — et n'est pas non plus réutilisé tel quel : les
règles diffèrent (German ne porte ni `CBC`, ni `BMP`, ni `911`, ni `SAMU`, ni
`g/dL`, ni `ng/mL`, ni `/mm³`). Le principe, lui, est repris : substitution
1 pour 1, **hors zones base64** (`data:image[^"]*` mis de côté avant toute
substitution), aucune modification de structure, donc aucun sous-item noté
touché.

**Contrôle préalable au remplacement** — exigé parce que `cases/scoring.js:159`
découpe `.criteria-text` par `.split(". ")[1].split(" [")[0]` : recherche de
`\bNFS\b` dans tout attribut `data-criteria` et dans tout `.criteria-text` des
88 grilles → **0 occurrence** dans l'un comme dans l'autre. Le remplacement ne
peut donc pas déplacer le libellé qu'affiche la liste des items manquants.

**Contrôle du sens de chaque occurrence** — les 63 `NFS` ont été relus un à un
dans leur contexte visible : tous désignent la numération formule sanguine
(« NFS, CRP, ionogramme », « NFS avec formule [leucocytose] », « NFS (anémie) »).
Aucun n'est un total de barème ni un sigle homonyme. C'est le contrôle qui avait
manqué de corrompre `Score Global 0/112` sur AMBOSS ; aucune règle sur un nombre
n'est d'ailleurs introduite ici.

**Modifications**

- global · laboratoire : « NFS » → « **FSC** », 63 occurrences dans 37 grilles
  (German-1, 2, 3 ×2, 6, 7, 8, 9, 11, 12, 13 ×2, 15 ×6, 19 ×6, 26, 29, 34 ×5,
  35, 40, 43 ×3, 45, 46 ×6, 47 ×2, 48, 49 ×2, 50, 51 ×2, 52, 53, 55, 60, 61, 67,
  69, 71, 74, 75, 76, 85).
  source : nomenclature suisse de laboratoire — formule sanguine complète ;
  même table `BANNED` que le corpus AMBOSS, importée et non recopiée.
- German-63 · unités : `detail-text criteria-detail` du critère `m2`,
  « Dosage œstradiol (**< 50 pg/mL**) » → « Dosage œstradiol (**< 184 pmol/L**) ».
  Œstradiol : `pg/mL` → `pmol/L`, **× 3,671** (masse molaire 272,4 g/mol) ;
  50 × 3,671 = 183,55 → **184**. Arrondi à l'entier, comme les conversions
  d'AMBOSS (320 → 236, 85 → 63, 200-900 → 148-664).

  *Qualificatif voisin vérifié.* Le seul qualificatif porté par cette valeur est
  le **sens de l'inégalité** : « < 50 pg/mL » et « < 184 pmol/L » décrivent le
  même seuil, le « < » reste donc exact après conversion. Balayage de la grille
  entière (`œstradiol`, `estradiol`, `E2`) : aucune autre mention, donc aucun
  adjectif (« bas », « effondré ») à réaccorder ailleurs. Le sous-item voisin
  « Dosage FSH (> 30 UI/L) » est déjà en unité suisse et n'est pas touché ; les
  deux valeurs restent cohérentes entre elles (FSH haute + œstradiol bas =
  ménopause confirmée).

  *Piège des valeurs multiples sur une ligne.* Les conversions du script portent
  sur la **ligne entière** et non sur le seul nombre, et le compte attendu est
  déclaré (`1`) : le script échoue si la substitution ne s'applique pas
  exactement une fois. C'est ce qui manquait quand « Hb < 7 g/dL (< 9 si
  coronarien) » et « B12 : 85 pg/mL (N: 200-900) » ont failli produire des seuils
  faux sur AMBOSS. Vérification indépendante : `pg/mL` n'apparaît qu'une fois
  dans les 88 grilles, cette ligne ne porte donc pas de seconde valeur.

**Divergences consignées** — aucune.

**Vérifications** — `check_nomenclature.py` 64 → **0** ; `check_invariants.py`
OK (88 grilles, barème inchangé) ; `check_reachability.py` OK (88 grilles à
100 %) ; `report_redundancy.py` **83**, inchangé ; `check_no_loss.py 4819f53` :
**0 item disparu** sur les 38 grilles modifiées ; intégrité `<div>`/`<ul>`/
`<li>`/`<span>` appariés et `</html>` final sur les 88. AMBOSS inchangé :
`check_invariants`, `check_nomenclature`, `check_reachability` OK,
`report_redundancy` 147.

### Volet B — Suppression du remplissage automatique d'`annexe-dd` (tâche g2)

Arbitrage utilisateur : **le remplissage est supprimé, aucun contenu médical
n'est créé en remplacement.** Une entrée réduite à son seul nom de diagnostic
reste utile — la liste des hypothèses à évoquer est en soi le contenu principal
du bloc.

Script : `scripts/german/prune_dd_filler.py`.

**Ce que porte le bloc, mesuré et non échantillonné.** Les 78 segments
`annexe-dd` des 88 grilles portent **484 entrées `<li>`**, toutes de la même
forme, sans une seule exception (contrôlé : le résidu de chaque `<li>` une fois
ses trois éléments retirés est exactement `<br>`) :

    <li><strong>NOM</strong><br>
        <div …rgb(80, 90, 110)>ARGUMENTS</div>
        <div …rgb(52, 105, 46)>→ EXAMEN</div></li>

soit **588 puces d'arguments** (216 formulations distinctes) et **484 examens**
(129 formulations distinctes). Les deux listes ont été lues intégralement pour
établir la liste des formulations génériques — le critère retenu étant *une
formulation qui serait vraie pour n'importe quel diagnostic de n'importe quelle
grille*.

**Modifications**

- annexe-dd · arguments : **345 puces « À évaluer cliniquement » supprimées**,
  dans 71 grilles — 59 % des 588 puces. Une seule formulation générique existe
  dans tout le corpus, et ses 345 occurrences sont **toutes** seules dans leur
  `<div>` : aucun cas mixte où elle cohabiterait avec un argument réel. Le
  `<div>` entier part, jamais le seul texte.
- annexe-dd · examens : **262 flèches supprimées** sur 484, en **quatre**
  formulations — « Examens complémentaires selon contexte clinique » (258),
  « Bilan biologique spécifique » (2), « Évaluation clinique approfondie » (1),
  « Anamnèse » seule (1). Aucune ne nomme d'examen : ni organe, ni technique, ni
  analyte, ni score.
- annexe-dd · mise en forme : le `<br>` qui suivait le nom est retiré dans les
  **209 entrées réduites au nom seul**, où il n'a plus rien à séparer. Il est
  conservé partout ailleurs, ce qui laisse l'interligne existant inchangé.

**Ce qui subsiste** : les 484 noms de diagnostic (aucun n'est touché),
**243 puces d'arguments réelles** et **222 examens discriminants réels**. Sur
les 209 entrées réduites au nom seul, 82 portent déjà dans leur nom l'examen ou
la précision qui départage — « Achalasie → Manométrie œsophagienne », « Corps
étranger/calcul → Radiographie, échographie », « Irritation du nerf ulnaire
[Signe de Tinel] » — et 127 restent un nom nu, c'est-à-dire une hypothèse à
évoquer.

**Suppression d'élément, jamais de texte.** Le script ne fait que supprimer des
plages de caractères mesurées et disjointes, chacune couvrant un élément entier.
Preuve *a posteriori*, rejouée sur les 88 grilles : le contenu de chaque fichier
après passe est **exactement** son contenu avant passe privé des 816 plages
planifiées, et l'ensemble des chaînes retirées ne compte que **6 formes
distinctes** (les 4 `<div>` d'examen générique, le `<div>` d'argument générique,
et `<br>`), pour 70 401 caractères. Rien d'autre n'a bougé dans les 88 fichiers.
Le bloc `annexe-dd` étant le **frère** d'un `criteria-row` qui porte l'`<input
type="radio">` du critère englobant, c'est la propriété qui garantit qu'aucun
`</div>` n'a pu se déplacer — le défaut de German-84. German-84 ne porte
d'ailleurs aucun `annexe-dd` et n'est pas modifiée.

**Divergences consignées**

- annexe-dd · formulations **limites conservées**, parce qu'elles ne seraient
  pas vraies de n'importe quel diagnostic : arguments « rare » (2),
  « diagnostic d'exclusion », « peu probable vu l'âge », « sans cause évidente »,
  « processus inflammatoire » ; examens « Anamnèse médicamenteuse » (2),
  « Anamnèse, audiométrie », « Examen neurologique, imagerie », « Examen
  ophtalmologique », « Évaluation cognitive », « Révision du traitement »,
  « Examen clinique, évaluation environnement », « Critères temporels DSM-5 »,
  « Évaluation temporelle des symptômes », « Diagnostic clinique, biopsie si
  doute ». La plus discutable est **« Évaluation temporelle des symptômes »**
  (German-4, trouble de l'adaptation) : conservée parce que le calendrier est
  précisément ce qui la sépare du trouble dépressif persistant de la même liste,
  dont l'examen est « Critères temporels DSM-5 ».
- annexe-dd · les **89 flèches portées par le nom lui-même** (« Fracture
  vertébrale → Radiographie si critères présents ») ne sont pas touchées : elles
  font partie du nom, qui est hors périmètre. Elles expliquent qu'une entrée
  puisse perdre son `<div>` d'examen générique tout en conservant un examen.
- annexe-dd · trois formulations citées au brief comme génériques **n'existent
  pas dans ce bloc** : « selon contexte clinique » seul (0 — les 258 occurrences
  sont la formule longue), « Examen clinique complet » (2 occurrences, toutes
  **hors** `annexe-dd`, donc hors périmètre et non touchées), « Anamnèse et
  examen clinique » (0 dans tout le corpus).

**Vérifications** — `check_invariants.py` OK (barème inchangé : le bloc ne porte
aucune case à cocher) ; `check_reachability.py` OK, 88/88 à 100 % ;
`check_nomenclature.py` OK ; `bounds_anomalies()` et `uncovered_content()` vides
sur les 88 ; intégrité `<div>`/`<ul>`/`<li>`/`<span>` appariés et `</html>` final
sur les 88. Redondance **inter-blocs 83 → 82**, **intra-bloc 638 → 118**
(−81 %) : le remplissage était dupliqué d'une entrée à l'autre *dans* le même
bloc, donc intra ; le chiffre inter-blocs bouge peu parce que 63 des 88 grilles
n'ont qu'`annexe-dd` et aucun bloc avec quoi former une paire.
`check_no_loss.py 4819f53` : 405 items signalés sur 79 grilles, **audités un à
un**, aucune perte réelle — 379 ont un résidu vide (pur remplissage) ou retrouvé
tel quel ; les 26 restants sont des artefacts de mesure, vérifiés présents dans
le fichier caractère par caractère : 20 sont des puces réelles conservées mais
devenues plus courtes que le seuil `min_len=18` de `list_items()` (« AIT »,
« TVP », « FAI », « L2-L3 », « alcool d'hier », « signe de Déjérine »…), et 6
sont l'effet du renommage `NFS` → `FSC` du volet A dans le même intervalle.

### German-44 (Érythème — lupus érythémateux cutané) — grille pilote du corpus, tâche g3

Page SSP : `SSP ECOS/SSP — Éruption Cutanée.md` (mapping ligne 1254).
Blocs présents : `annexe-dd`, `redflags`, `therapy` ×2, `resume`, `presentation`,
`annexe-image`. **Ni `annexe-expert` ni `annexe-theorie`** — ils n'existent nulle
part dans ce corpus, donc les axes 1, 2, 6 et 7 de `scripts/amboss/PROCEDURE.md`
§ 3, qui reposent sur eux, sont **sans objet ici**. Restent applicables : `resume`
canonique (axes 3 et 4), la trame de présentation (axe 5), la règle du format et
la règle anti-perte.

**La page SSP ne tranche rien de cette grille.** Elle couvre l'éruption cutanée
générique — toxidermie, purpura fébrile, SJS/Lyell, DRESS, érysipèle — et ne porte
aucune occurrence de « lupus », « ANA », « anti-SSA », « hydroxychloroquine » ni
« photosensibilité ». Le seul point où elle recoupe la grille est
« Biopsie cutanée si doute diagnostique » (§ 🔬 EXAMENS COMPLÉMENTAIRES), que
`resume` porte déjà mot pour mot. **Niveau 3** sur toute la prise en charge : rien
à aligner, rien inventé. L'arbitrage s'est donc fait au niveau 2 (section notée)
et par le contrat de blocs.

**Modifications**

- annexe-dd · Psoriasis : « Arguments POUR : Plaques érythémato-squameuses bien
  délimitées · **Localisations typiques (coudes, genoux)** · **Antécédents
  familiaux possibles** » → POUR conservé sur la seule plaque, les deux autres
  **déplacés en Arguments CONTRE** sous leur forme négative
  (« Localisations typiques absentes (coudes, genoux, cuir chevelu) »,
  « Pas d'antécédents familiaux »).
  source : section notée `e2` « Examen cutané détaillé [Érythème rouge légèrement
  squameux **au niveau du dos**] » et `a11` « Antécédents familiaux [Grands-parents
  hypertendus après 65 ans, grand-père avec goutte] » — **niveau 2**. Le bloc
  affirmait comme arguments *pour* le psoriasis deux éléments que la section notée
  déclare absents chez cette patiente.
- annexe-dd · Photodermatose : « POUR : Éruption liée à l'exposition solaire ·
  **Amélioration à l'ombre** · **Récidive à chaque exposition** » → POUR resserré
  sur « Aggravation nette pendant les vacances en Italie », les deux autres
  critères **déplacés en CONTRE** en gardant leur nom
  (« Persistance après la fin de l'exposition, sans amélioration à l'ombre »,
  « Premier épisode, sans récidive à chaque exposition »), plus « Pas de prurit ».
  source : sections notées `a4` [Depuis environ 3 semaines], `a13` [Retour d'Italie
  il y a 2 semaines], `a5` [Non, premier épisode], `a3` [Pas de démangeaisons].
- annexe-dd · les cinq arguments CONTRE ci-dessus sont **portés depuis**
  `presentation`/« Arguments pour et contre » (Q2 et Q3), pas inventés. C'est le
  geste anti-perte : porter d'abord dans le bloc dont c'est le rôle, supprimer
  ensuite. Le bloc ne portait que des « Arguments POUR » et ne **départageait**
  donc rien, alors que c'est sa raison d'être au contrat.
- resume · Prise en charge / Traitement topique : « Inhibiteurs de calcineurine
  (tacrolimus, off-label) » → « … **— surtout sur le visage** ».
  source : `therapy` du critère noté `m5`, « Inhibiteurs de la calcineurine :
  Alternative aux corticoïdes, **surtout pour le visage** » — niveau 2. Porté
  avant la suppression de « Inhibiteurs de la calcineurine si visage » dans
  `presentation`.
- resume · Prise en charge : **nouvelle sous-section « Signes d'alarme (passage
  systémique) »** — atteinte rénale (protéinurie, hématurie), atteinte
  neurologique (convulsions, troubles cognitifs), arthrites franches, cytopénies
  inexpliquées. Portée depuis `presentation`/Touches ludiques, où elle était la
  seule **donnée clinique** que le bloc canonique ne portait pas — ce que le
  contrat interdit à `presentation` (« ne porte jamais : toute donnée clinique
  nouvelle »). Elle rend enfin actionnable le point clé « Toujours rechercher
  signes de passage en lupus systémique », qui restait sans contenu.
- presentation · Touches ludiques / **« Formes cliniques de lupus cutané »** :
  supprimée. Doublon strict de `resume`/Examen clinique/Formes cliniques
  principales, **même format** (liste) — 3 des 17 paires. Comparée item par item
  avant suppression : aigu, subaigu, chronique discoïde et tumidus figurent tous
  dans `resume` ; « risque alopécie cicatricielle » y est déjà (« parfois alopécie
  cicatricielle ») et « malaire » subsiste trois fois ailleurs dans la grille.
- presentation · Touches ludiques / **« PEC pratique »** : supprimée. Check-list
  actionnable — ce que le contrat interdit à `presentation` — doublant
  `resume`/Prise en charge et le `therapy` du critère `m5`. Ses cinq items sont
  tous retrouvés (le « visage » ayant été porté dans `resume` juste avant).
- presentation · Touches ludiques / Pièges ECOS : puce « Toujours relier à
  exposition solaire » supprimée. Même contenu et même format que
  `resume`/Questions à poser « Relation avec exposition solaire ? », et déjà le
  point clé n° 1 du `resume` (« Photosensibilité + lésions cutanées chroniques =
  évoquer lupus cutané »). Les trois autres pièges restent : **l'axe 6 d'AMBOSS
  — « supprimer `presentation`/Pièges ECOS » — est sans objet ici**, faute
  d'`annexe-expert` ; c'est le seul bloc de pièges de la grille.
- presentation · `mnemo-box` LUPUS **déplacée** de « Checklist mentale » vers
  « Touches ludiques / mnémos ». Geste de l'axe 5 et précédent AMBOSS-2/3 : la
  checklist redevient une trame pure. Les cinq clés sont intactes. État du corpus
  après coup : AMBOSS 15/15 en `section-mnemo`, German 11 encore en
  `section-checklist` et 3 en `section-express` — les 14 autres grilles à mnémo
  suivront.
- presentation · Q1 « Lupus érythémateux cutané » : « Érythème squameux chronique,
  non prurigineux » + « Aggravation après exposition solaire » **fusionnés** en
  « Érythème squameux chronique **photosensible**, non prurigineux ». Réduction
  aux arguments décisifs ; « photosensible » dit exactement l'aggravation solaire,
  qui figure par ailleurs dans la version longue, le SBAR et `annexe-dd`.
- presentation · Q2 « Psoriasis » et Q3 « Photodermatose » (POUR/CONTRE
  structurés) **remplacés par une seule réponse orale** : « Pourquoi écarter le
  psoriasis et la photodermatose ? ». C'est le miroir d'`annexe-dd` qui cède,
  après que le contenu discriminant y a été porté ; le passage liste → narration
  parlée est le changement de format que la règle autorise, et c'est le rôle même
  du bloc (restituer à l'oral).
- presentation · Q « Quels examens demanderiez-vous ? », Q2 « Traitement », Q3
  « Suivi » : les trois `presentation-reponse list` / `<ul>` **convertis en
  `presentation-reponse text`** en registre parlé.
  motif : « Une liste recopiée sous un en-tête Q/R ne constitue pas un changement
  de format » (`scripts/amboss/PROCEDURE.md` § 3, « Redire à l'oral, pas en
  liste »). Q3/Suivi recopiait de surcroît **mot pour mot** les quatre
  sous-items du critère noté `m7` — duplication de niveau 2 qu'aucune mesure de
  redondance ne peut voir, les sections notées n'étant pas des blocs. Contenu
  strictement conservé, `<span class="highlight-range">` et
  `<span class="highlight-important">` compris.

**Divergences consignées**

- redflags (`m6`) · le second signal d'alarme s'intitule **« 2. Signes d'alerte »**
  et ne dit rien. C'est le corrigé d'un critère noté (**niveau 2**), et le
  compléter reviendrait à écrire le corrigé à la place de l'auteur — règle 3 des
  arbitrages (jugement d'auteur). **Non corrigé.** Le contenu qui le remplirait
  est désormais dans `resume`/« Signes d'alarme (passage systémique) ». À noter
  que la procédure interdit par ailleurs de modifier `redflags` pour résoudre un
  doublon : ici il ne s'agissait pas d'un doublon, mais la conclusion est la même.
- resume · deux paires **intra-bloc** subsistent, structurelles : « Éviter
  médicaments inducteurs » (Prise en charge) ↔ « Prise de médicaments
  inducteurs ? » (Questions à poser) — une mesure et une question ; et « Biopsie
  cutanée confirme le diagnostic » (Points clés) ↔ « Biopsie cutanée si diagnostic
  incertain » (Examens à faire) — l'indication et son rendement. Le chiffre
  intra-bloc mesure, il ne prescrit pas.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %. **Aucune modification du barème** : les
trois blocs touchés ne portent ni `<input>` ni case, `maxScores`, `scoreSpans`,
`sectionCounts`, `criteriaCount`, `detailCount`, `radioCount` et `checkboxCount`
sont inchangés — règle 1 des arbitrages, pas de régénération de `baseline.json`.
AMBOSS intact, redondance **147**. `<div>`/`<ul>`/`<li>`/`<span>` appariés (602,
21, 79, 87), équilibre bloc par bloc vérifié.

Redondance German-44 : **17 → 2** paires inter-blocs (corpus 82 → 67).
Les deux qui restent sont **le même item** — la clé `S` du mnémo LUPUS,
« S = Surveillance évolutive vers lupus systémique », face à
`resume`/PEC en 3 points et à `redflags`/`m6`. Un mnémo garde sa clé d'origine
(§ 3, « supprimer le mot d'origine casserait le mnémo ») : la paire est le prix
du format mnémotechnique, qui n'est ni une liste ni une narration.

`check_no_loss.py fbe42f9` : 18 items signalés, **verdictés un à un, aucune perte
réelle**. Cinq sont les arguments portés dans `annexe-dd`, un est la nuance
« visage » portée dans `resume`, quatre sont les items de « Formes cliniques » et
« PEC pratique » retrouvés dans `resume` ou `therapy`, et les huit derniers sont
l'effet mécanique des trois conversions liste → narration : `list_items()`
n'extrait pas le texte d'un `presentation-reponse text`, si bien qu'une réponse
orale complète y apparaît toujours comme une disparition. Présence contrôlée
chaîne par chaîne sur le HTML brut après `strip_base64` — jamais par `grep`.
