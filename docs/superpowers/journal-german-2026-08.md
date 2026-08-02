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

### Tâche g4 — Les 12 grilles riches restantes (15, 19, 22, 27, 34, 42, 43, 48, 56, 69, 72, 88)

Départ `ff4605c`. Ce sont les 12 dernières grilles à porter simultanément
`resume`, `annexe-dd` et `presentation` — le seul couple pédagogique du corpus.
Le patron du pilote German-44 a été suivi dans l'ordre : (1) lire la section
notée en entier, (2) porter les CONTRE dans `annexe-dd`, (3) supprimer de
`presentation` ce qui double `resume` **au même format**, (4) convertir les
réponses Q/R en liste vers le registre parlé, (5) déplacer le mnémo, (6)
vérifier à l'œil qu'aucune réponse ne recopie un `criteria-text`. Les axes 1, 2,
6 et 7 d'AMBOSS restent sans objet (ni `annexe-expert` ni `annexe-theorie`), et
`presentation`/Pièges ECOS n'a été supprimé dans **aucune** grille.

**Pages SSP.** Les huit pages consultées (Douleur Abdominale, Douleurs
Articulaires, Douleur d'Épaule, Dysphagie, Éruption Cutanée, Fièvre du
Nourrisson, Incontinence Urinaire, Amaurose & BAV, Œil Rouge, Troubles de la
Croissance) confirment le constat du pilote : elles ne tranchent presque rien.
**Une seule occurrence de niveau 1** sur les 12 grilles, en German-15. Tout le
reste s'est arbitré au **niveau 2** (section notée), qui est riche.

**Modifications, par grille**

- **German-15** (diverticulite) · `resume` : « coloscopie à distance **4–6**
  semaines » → **6–8**, aux deux endroits (Examens diagnostiques et Examens à
  faire). source : `m7-detail-2` « Coloscopie 6-8 semaines après l'épisode » —
  **niveau 2** ; `presentation` disait déjà 6–8 en quatre endroits, `resume`
  était seul à dire 4–6.
- **German-15** · `resume`/Formes simples : ajout « abstention possible chez le
  patient sélectionné, immunocompétent et sans signe de gravité (SSMI/SGAIM) ».
  source : `SSP — Douleur Abdominale` l. 445, « non compliquée → antibiothérapie
  ambulatoire (voire abstention chez le patient sélectionné, SSMI/SGAIM) » —
  **niveau 1**, seule occurrence du lot.
- **German-15** · `annexe-dd` : Colite et Cancer colorectal reçoivent leurs
  **arguments CONTRE**, portés depuis `presentation` Q2/Q3 ; Q2 et Q3 fusionnent
  en une réponse orale. `presentation` Q « examens », Q2 « Traitement », Q3
  « Suivi » : `list` → `text`. Mnémo DIVERTI déplacé vers Touches ludiques.
- **German-19** (RCUH) · `annexe-dd` : Colite infectieuse et Maladie de Crohn
  reçoivent POUR **et** CONTRE ; l'examen qui départage la colite infectieuse
  passe de « Coloscopie, calprotectine fécale » à « Examen bactériologique et
  parasitologique des selles ; calprotectine et coloscopie si persistance ».
  source : `m3` « Examen bactériologique des selles » et `a17` « Anamnèse de
  voyage [Il y a 2 semaines en Égypte] » — **niveau 2**. Correction de fond : ce
  n'est pas la coloscopie qui tranche une colite infectieuse.
- **German-19** · `presentation`/Pièges : puce « Ne pas proposer coloscopie avec
  biopsies » supprimée — même contenu et même format que `resume`/PEC en
  3 points « Diagnostic par coloscopie avec biopsies », et le point clé n° 2 du
  `resume`. Les trois autres pièges restent. Mnémo SANG déplacé. Trois réponses
  `list` → `text` ; Q « examens » reçoit au passage les gamma-GT et phosphatases
  alcalines de `m3` (dépistage de CSP), qu'aucun bloc pédagogique ne portait.
- **German-22** (épicondylite) · `annexe-dd` : les **cinq** hypothèses reçoivent
  POUR/CONTRE case-appliqués, portés depuis `presentation` Q2-Q5 et depuis la
  sous-section « Diagnostic différentiel rapide » de Touches ludiques ; Q2-Q5
  fusionnent en une réponse orale.
- **German-22** · `presentation`/Touches ludiques : « Tests spécifiques Tennis
  elbow » et « Diagnostic différentiel rapide » supprimées. La première est un
  sous-ensemble strict de `resume`/Tests spécifiques au même format (Cozen, Mill,
  chaise, tous présents, `resume` en portant un quatrième) ; la seconde est du
  **raisonnement différentiel**, que le contrat réserve à `annexe-dd`, et son
  contenu y a été porté avant suppression. Mnémo ELBOW déplacé. Q « examens »,
  Q2, Q3 : `list` → `text`. Q3/Suivi recopiait `m4` (« Bon pronostic, durée
  semaines à mois », « Charge sportive uniquement jusqu'à absence de douleur »).
- **German-27** (conflit sous-acromial) · `annexe-dd` : entrée « Capsulite
  rétractile » **réparée** — son « → Diagnostic clinique, IRM si doute » avait
  été avalé dans la puce d'argument POUR (défaut de structure, pas d'import) —
  puis dotée du CONTRE décisif « Mobilité passive conservée ». Arthrose
  gléno-humérale et Névralgie cervico-brachiale reçoivent POUR/CONTRE.
- **German-27** · `presentation` : les **cinq** `presentation-reponse list`
  converties en `text` ; « Tests spécifiques » et « Conflit sous-acromial
  typique » supprimées de Touches ludiques (sous-ensembles stricts de `resume`,
  même format) ; mnémo ARC déplacé.
- **German-34** (cancer de l'œsophage) · `annexe-dd` : entrée « Compression
  extrinsèque » réparée (même défaut de structure qu'en German-27) ; Cancer ORL
  et Achalasie reçoivent POUR/CONTRE. Touches ludiques : « Signes d'alarme
  dysphagie », « Principaux diagnostics différentiels » et « Examens clés »
  supprimées — sous-ensembles stricts de `resume` pour la première et la
  troisième, d'`annexe-dd` pour la deuxième. Mnémo ALARME déplacé. Q1 examens,
  Q2, Q3 : `list` → `text` ; Q3/Suivi absorbe `m6` (information du patient).
- **German-42** (tinea corporis) · `annexe-dd` : Psoriasis — « coudes, genoux,
  antécédents familiaux » figuraient en **Arguments POUR** alors que la section
  notée les déclare absents ; **déplacés en CONTRE** sous forme négative, pas
  dupliqués (le piège signalé par le pilote). Dermatite atopique et Eczéma
  nummulaire reçoivent POUR/CONTRE. Q2-Q4 fusionnent en une réponse orale.
- **German-42** · Touches ludiques : « Examens utiles » et « PEC antifongique »
  supprimées (sous-ensembles stricts de `resume`, même format) ; le mnémo PED et
  les Pièges restent, RING est déplacé. Q « examens », Q2, Q3 : `list` → `text`.
  Q3/Suivi recopiait `m7` (contrôle à 2 semaines, guérison mycologique,
  adaptation) et `m6` (mesures d'hygiène).
- **German-43** (scarlatine) · `annexe-dd` : Rougeole — sa description (« macules
  puis papules descendantes, signe de Koplik ») figurait en **POUR** alors que
  ces signes sont absents ; restructurée en POUR/CONTRE. Varicelle et Rubéole
  reçoivent POUR/CONTRE. **Ajout de la Maladie de Kawasaki**, présente dans
  `resume`/Différentiels et dans `presentation` mais absente du bloc dont c'est
  le rôle. Q2-Q5 fusionnent en une réponse orale.
- **German-43** · `resume` : l'éruption devient « micropapuleuse, **rugueuse au
  toucher (« papier de verre »)**, accentuée dans les plis » — porté depuis
  `presentation` avant la suppression de « Signes typiques scarlatine » (sous-
  ensemble strict de `resume`/Signes caractéristiques). Traitement symptomatique
  reformulé pour cesser de recopier le `therapy` de `m4`. Mnémo FAR déplacé.
  Q « examens », Q2, Q3 : `list` → `text` ; Q3/Suivi recopiait `m5`, `m6` et `m7`.
- **German-48** (exanthème subit) · `annexe-dd` : la première catégorie ne
  contenait pas un différentiel mais deux fragments d'arguments du diagnostic
  principal (« Âge typique / POUR : 6 mois - 2 ans → Diagnostic clinique » et
  « Fièvre élevée avec bon état général → Surveillance ») ; **refondue en une
  entrée « Exanthème subit (HHV-6/7) — hypothèse principale »** avec POUR/CONTRE
  et examen. Rougeole, Rubéole et Érythème infectieux passent d'un descriptif
  fondu dans le titre à des POUR/CONTRE structurés ; **ajout de la Scarlatine**,
  présente partout ailleurs dans la grille.
- **German-48** · Touches ludiques : « Diagnostic typique exanthème subit »
  (sous-ensemble strict de `resume`), « Différentiels viraux » (rôle
  d'`annexe-dd`, porté) et « Signes d'alerte pédiatriques » supprimées. La
  dernière recopiait les cinq `redflags-text` de `m6` **et** ses cinq
  `detail-text` : duplication pédagogique ↔ section notée, invisible à
  `report_redundancy`. Mnémo 3-1-R déplacé. `resume` : trois formulations de
  « convulsions fébriles » précisées pour cesser de recopier `redflags`/`m6`
  (le pédagogique cède, jamais le corrigé). Q1-Q5 fusionnent en deux réponses
  orales ; Q « examens », Q2, Q3 : `list` → `text`. Le seuil de réévaluation de
  Q3 passe de « fièvre > 5 jours » à « 3 à 4 jours si persistance » —
  source `m5-detail-1`, **niveau 2**.
- **German-56** (incontinence d'effort) · `annexe-dd` : entrée « Vessie
  hyperactive secondaire » réparée (même défaut de structure) ; Vessie
  hyperactive idiopathique et Incontinence mixte reçoivent POUR/CONTRE. Q2/Q3
  fusionnent en une réponse orale. Mnémo MAPS-U déplacé. Q1 examens, Q2, Q3 :
  `list` → `text` ; Q3/Suivi recopiait `m5` mot pour mot.
- **German-69** (cataracte) · `annexe-dd` était déjà **exemplaire** — seul bloc
  du corpus à porter des CONTRE sur onze hypothèses. Il reçoit seulement les deux
  arguments POUR que `presentation` portait en plus (halos lumineux, myopie
  d'induction) et le POUR du glaucome chronique. Q1-Q3 fusionnent en deux
  réponses orales, Q1 examens, Q2, Q3 : `list` → `text`. Mnémo MAPS déplacé.
- **German-72** (maladie cœliaque) · `annexe-dd` : quatre des six hypothèses
  reçoivent POUR/CONTRE et leur examen discriminant (test de la sueur, âge
  osseux, TSH). Q2-Q5 fusionnent en une réponse orale. Mnémo GROWTH déplacé.
  Q1 examens, Q2, Q3 : `list` → `text` ; Q1 reçoit l'albumine et le caryotype de
  `m3`/`m4`, Q3 recopiait `m8` et ignorait `m9`.
- **German-88** (conjonctivite allergique) · `annexe-dd` : Conjonctivite
  infectieuse et Kératite/érosion sur lentilles reçoivent POUR/CONTRE et leur
  examen (prélèvement bactériologique, fluorescéine). `resume` : ajout de
  « **arrêt temporaire du port de lentilles** » et des compresses froides.
  source : `m6` « Arrêt temporaire des lentilles » et `m4` « Compresses froides »
  — **niveau 2** ; le patient porte des lentilles (`a8` « oui habituellement »)
  et aucun bloc pédagogique ne le disait. Mnémo PRURIT déplacé. Q2/Q3 fusionnent
  en une réponse orale ; Q1 examens, Q2, Q3 : `list` → `text`, et la dimension
  IST/Chlamydia de `m3` et `m7` entre enfin dans le pédagogique.

**Divergences consignées**

- **German-56** · le mnémo DAME repose sur « **A = Argenturie** », mot qui
  n'existe pas — le terme est *urgenturie*. Corriger la coquille casse la clé du
  mnémo, et la procédure interdit de supprimer le mot d'origine. **Non corrigé**,
  règle 3 (jugement d'auteur) : à trancher entre garder la coquille et refondre
  le mnémo.
- **German-56**, **German-69** et **German-88** · une `mnemo-box` « SBAR » vit
  dans `section-express`, immédiatement sous la version SBAR dont elle est la
  **légende**. L'axe 5 vise la Checklist mentale, pas la version express : ces
  trois mnémos sont **laissés en place**. État du corpus après cette passe :
  German **13** `mnemo-box` en `section-mnemo`, **3** en `section-express`,
  **0** en `section-checklist` (mesuré).
- **German-27** · la section notée `e4` cote le test de Jobe « Gauche : moins de
  force, douloureux » alors que la version longue dit « pas de perte de force
  nette » et que `resume` décrit le test comme « souvent douloureux mais non
  déficitaire ». Ce n'est pas une contradiction stricte (inhibition antalgique),
  mais la rupture de coiffe ne peut pas être formellement écartée : **aucun
  argument CONTRE n'a été écrit** pour elle dans `annexe-dd`. Consigné.
- **German-43**, **German-48** · deux formulations approximatives ont disparu au
  cours de la restructuration d'`annexe-dd` : « conjonctivite typique absente »
  pour la rubéole (la conjonctivite n'est pas le signe cardinal de la rubéole ;
  remplacée par l'adénopathie rétro-auriculaire) et « convulsions non typiques »
  pour l'érythème infectieux (l'enfant n'en a pas). Remplacements assumés, pas
  des pertes.
- `resume`/`therapy` · German-43 portait une paire `resume ↔ therapy` sur les
  antipyrétiques. Le pédagogique a cédé **par reformulation**, pas par
  suppression : le contenu doit rester dans `resume`, qui est la fiche de
  révision, tandis que `therapy` est le corrigé du critère. Aucun `therapy` ni
  `redflags` n'a été modifié dans les 12 grilles.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, AMBOSS aux trois verts et redondance
**147**. **Aucune modification du barème** : aucun `.criteria-text`, aucun
`<input>`, aucun `<span class="score">`, aucun `maxScores` n'apparaît dans le
diff (vérifié) — règle 1 des arbitrages, `baseline.json` non régénéré. Balises
appariées sur les 12 fichiers (`div`, `ul`, `li`, `span`), `boundsAnomalies` et
`uncoveredContent` vides.

Redondance : **63 → 10** paires inter-blocs sur les 12 grilles ; corpus German
**67 → 14** (les 4 autres sont German-44, 2, et German-68, 2 — hors périmètre).
Les 10 restantes sont **toutes** des clés de mnémo protégées par la règle du
format : DIVERTI/`I` (15), MICI/`C` ×2 (19), ARC/`A` ×2 et `R` (27),
ALARME/`E` (34), 4R/`Rééducation` (56), GROWTH/`R` (72), PRURIT/`Rougeur` (88).
Cinq grilles tombent à **0** : 22, 42, 43, 48 et 69.

`check_no_loss.py ff4605c` : **235 items signalés sur les 12 grilles, verdictés
un à un, aucune perte réelle**. Répartition : ~150 sont l'effet mécanique des
conversions liste → narration — **38 réponses Q/R converties** (29
`presentation-reponse list`, qui tombent ainsi de 29 à **0** sur les 88 grilles,
et 9 `reponse-section` à `<ul>`) et **30 réponses POUR/CONTRE structurées
fusionnées en 13 réponses orales** ; `list_items()` n'extrait pas le texte d'un
`presentation-reponse text` ; ~55 sont des arguments portés dans `annexe-dd`,
où ils ont été réécrits en forme case-appliquée ; ~25 sont les items des
**13 sous-sections** supprimées de Touches ludiques (2 en German-22, 2 en
German-27, 3 en German-34, 2 en German-42, 1 en German-43, 3 en German-48) et de
la puce de Pièges de German-19, tous retrouvés dans `resume`,
`annexe-dd`, `therapy` ou la section notée ; les 5 derniers sont des `<li>`
d'`annexe-dd` dont la normalisation a changé parce que le bloc a été
restructuré. Présence contrôlée chaîne par chaîne sur le HTML après
`strip_base64` — jamais par `grep`.

---

### Lot g5a — les 25 grilles à `annexe-dd` seul de German-1 à German-30

Périmètre établi : German-1 à 30, moins les 4 grilles riches déjà traitées au lot
g4 (15, 19, 22, 27 — `resume` **et** `presentation`) et moins German-1, sans
`annexe-dd` (3 `therapy-section` seulement, niveau 2, hors périmètre). Restent
**25 grilles** : 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21,
23, 24, 25, 26, 28, 29, 30. German-24 y figure : elle porte un `resume` mais pas
de `presentation`, donc elle n'était pas du lot g4.

Aucun dédoublonnage inter-blocs possible (`report_redundancy.py` : **0 paire**
sur les 25 avant comme après). Le travail a porté sur les quatre points de la
consigne. **7 grilles modifiées** : 5, 6, 12, 13, 24, 28, 30.

#### 1. Le défaut de structure d'`annexe-dd` — **32 occurrences, 32 réparées**

Le lot g4 décrivait la flèche « → examen qui départage » avalée dans la puce
« Arguments POUR ». Le balayage de ce lot en trouve **deux variantes**, la
seconde étant de loin la plus fréquente et non encore documentée :

| Variante | Où tombe la flèche | Occurrences | Grilles |
|---|---|---:|---|
| **A** — celle de g4 | dans le `<div>` des arguments (`rgb(80, 90, 110)`) | **2** | 5, 6 |
| **B** — nouvelle | dans le `<strong>` du **nom du diagnostic** | **30** | 5, 6, 13, 28, 30 |

La variante B produit des noms d'hypothèse absurdes — « Fracture de côte →
Radiographie thoracique », « Colite à Clostridium difficile → Recherche de
toxines A et B » — et, dans 9 cas, **coexiste avec un `<div>` d'examen déjà
présent**, si bien que la même entrée porte deux lignes d'examens concurrentes.
Elle échappe entièrement au motif de recherche proposé par g4 (« `Arguments
POUR:` suivi d'un `→` dans la même puce ») : le balayage doit porter sur la
présence d'un `→` **hors** du `<div class` d'examen, pas sur les arguments.

Réparation, dans les deux variantes : l'examen quitte l'élément qui l'avait
avalé et rejoint son propre `<div style="… color: rgb(52, 105, 46);">`, la forme
canonique du corpus. Quand un `<div>` d'examen existait déjà, les deux listes
sont **fusionnées**, l'examen qui départage placé en tête, les doublons stricts
écartés — aucune suppression de contenu.

**Modifications**

- `annexe-dd` · German-30, 4 entrées : « Fracture de côte → Radiographie
  thoracique » + examen « → Radiographie, CT si complexe » → nom « Fracture de
  côte », examen « → Radiographie thoracique, CT si complexe ». Idem Contusion
  costale, Pneumothorax (fusion des trois modalités), Hémothorax.
- `annexe-dd` · German-28, 8 entrées : nom et examen séparés à l'identique
  (Otite moyenne aiguë virale / bactérienne, Otite externe, Pharyngite/angine,
  Douleur dentaire irradiée, Adénite cervicale, Tympan rouge par pleurs
  intenses, Corps étranger auriculaire).
- `annexe-dd` · German-13, 8 entrées : idem, avec fusion pour Colite ulcéreuse,
  Cancer colorectal et Tumeur neuroendocrine.
- `annexe-dd` · German-5, 6 entrées : 5 en variante B, 1 en variante A
  (« Arguments POUR: • WAD grade I-II → Diagnostic clinique » → argument
  « • WAD grade I-II », examen « → Diagnostic clinique »).
- `annexe-dd` · German-6, 6 entrées : 1 en variante A, 5 en variante B. Ces six
  entrées cumulaient un **troisième** défaut — les arguments cliniques logés
  dans le nom après un « : » (« Ménopause : âge compatible, troubles
  menstruels → FSH, LH, œstradiol »). Les trois éléments ont été rendus à leurs
  trois places : nom, `Arguments POUR:` en puces, examen. Contenu intégralement
  conservé, aucune formulation nouvelle.

#### 2. Erreurs factuelles internes — 3 corrections directes

- `annexe-dd` · **German-28**, Pharyngite/angine : l'examen qui départageait
  était « → **ECG, test d'effort, coronarographie** » — un bilan coronarien dans
  une station d'**otalgie pédiatrique**. Contamination d'import manifeste : la
  grille ne porte aucun critère cardiologique (`m1`-`m8` sont otoscopie,
  antibiothérapie, conseils aux parents), la section notée `m3` nomme au
  contraire « Test rapide streptocoque si suspicion d'angine associée ». Ligne
  **supprimée**, l'examen resté prisonnier du nom (« Test rapide streptocoque si
  indiqué ») prenant sa place. C'est la seule suppression sèche du lot.
- `annexe-dd` · **German-13**, Colite à *Clostridium difficile* : « → Coloscopie,
  calprotectine fécale » — ce sont les examens de la MICI, chaîne strictement
  identique à celle de l'entrée « Colite ulcéreuse » deux lignes plus haut.
  Même motif que la colite infectieuse de German-19 (lot g4). Remplacé par le
  test qui départage réellement, cf. § 4.
- `annexe-dd` · **German-5**, Hernie discale cervicale avec compression :
  « → Examen clinique, **US si doute** » — l'ultrason n'explore pas le rachis
  cervical. « US si doute » retiré ; l'IRM, prisonnière du nom (« → IRM si
  déficit neurologique »), reprend sa place : « → Examen neurologique, IRM si
  déficit neurologique ».

#### 3. Alignements de niveau 1 — la page SSP tranche, 4 fois

Contrairement au lot g4 (1 sur 10 pages), quatre points ont été tranchés — parce
que quatre de ces pages sont **mono-grille ou quasi** (AVP, Constipation,
Douleur au Poignet, Diarrhée), là où les pages génériques du lot g4 desservaient
jusqu'à 14 grilles.

**Modifications**

- `annexe-dd` · German-5, Fracture vertébrale : « → Radiographie si critères
  présents, CT si complexe » → « → **Imagerie seulement si les règles
  canadiennes du rachis cervical (CCR) ou NEXUS** ne permettent pas la
  clearance ; CT si complexe ».
  source : `SSP — AVP` — « **Rachis cervical** : palpation des épineuses sous
  MILS, **règles canadiennes (CCR)** ou **NEXUS** pour clearance » et
  « Exclure lésion grave par règles canadiennes (CCR) ou NEXUS ; **pas
  d'imagerie systématique** en WAD I-II ».
- `annexe-dd` · German-12, Constipation fonctionnelle : « → Radiographie
  abdominale, coloscopie si alarme » → « → **Critères de Rome IV et échelle de
  Bristol** ; coloscopie si drapeaux rouges ou début après 50 ans ». Même geste
  pour le SII avec constipation (« → Critères de Rome IV (SII-C) ; coloscopie si
  drapeaux rouges ») et pour le Cancer du côlon, dont l'examen diagnostique
  manquait (« → **Coloscopie avec biopsies** ; imagerie (CT/IRM), marqueurs
  tumoraux »).
  source : `SSP — Constipation`, Règle d'or — « Caractériser avec l'**échelle de
  Bristol** et les **critères de Rome IV** (constipation fonctionnelle). […]
  Une constipation d'apparition récente après 50 ans ou avec drapeaux rouges
  impose une **coloscopie** (cancer colorectal) ». La page ne contient **aucune**
  occurrence de « radiographie », et la section notée `m4` n'en nomme pas non
  plus (FSC/CRP, test FIT, US ou CT, coloscopie).
- `annexe-dd` · German-13, Colite à *C. difficile* : « → Coloscopie,
  calprotectine fécale » → « → **GDH + toxines A/B dans les selles (± PCR
  confirmatoire)** ».
  source : `SSP — Diarrhée` — « *C. difficile* : **GDH + toxines A/B** (± PCR
  confirmatoire) si ATB / hospitalisation < 8 sem ».
- `annexe-dd` · German-13, Infections parasitaires chroniques : le nom portait
  « → Examen parasitologique des selles » et l'argument une puce isolée
  « • 3 échantillons » → examen unique « → **Recherche de parasites dans les
  selles × 3 jours consécutifs** ; FSC, CRP, hémocultures si fièvre ».
  source : `SSP — Diarrhée` — « **Recherche de parasites × 3 jours** (lambliase,
  amibiase, cryptosporidies) ».
- `resume` · German-24, Traitement chirurgical : « section du **ligament
  annulaire antérieur** » → « section du **rétinaculum des fléchisseurs** ».
  source : `SSP — Douleur au Poignet` — « le nerf médian passe sous le
  **rétinaculum des fléchisseurs** avec les 9 tendons fléchisseurs » ; la page
  ne contient aucune occurrence de « ligament annulaire ». La section notée `m6`
  dit déjà « Section du rétinaculum des fléchisseurs » : l'alignement de
  niveau 1 supprime du même coup l'écart de vocabulaire avec le niveau 2.

#### 4. Duplication avec la section notée — **aucun cas**

Recherche menée hors outillage, l'angle mort étant structurel
(`report_redundancy.py` ne voit que des blocs, et les sections notées n'en sont
pas). Deux comparaisons systématiques sur les 25 grilles : items d'`annexe-dd`
et de `resume` contre les `criteria-text`/`detail-text` hors bloc (seuil 0.72),
puis les seuls `<div>` d'examen d'`annexe-dd` contre les `detail-text` (seuil
abaissé à 0.62). Les 18 appariements obtenus sont **tous** des recoupements
légitimes de rôle : le critère noté énumère les examens à proposer, `annexe-dd`
en rattache un à une hypothèse précise — « Coloscopie avec biopsies » figure
dans `m4` de German-13 et départage à la fois Crohn, RCH et cancer colorectal,
c'est exactement son emploi. Aucune reprise de l'ordre ni du découpage d'un
corrigé.

C'est un écart net avec le lot g4, qui trouvait le motif **systématique** (sept
réponses « Suivi » recopiant leur critère). L'explication est structurelle : le
motif de g4 vivait dans `presentation`, bloc **absent des 25 grilles de ce lot**.
Sur German, la duplication pédagogique ↔ noté est un risque de `presentation` et
de `resume`, pas d'`annexe-dd`.

Le seul couple relevé — German-24, `resume`/Traitement conservateur face à `m5`
(« Attelle nocturne en position neutre du poignet » ↔ « Port d'attelle nocturne
en position neutre » ; « Antalgiques ± infiltration cortisonée dans le canal
carpien » ↔ « Infiltration de corticoïdes dans le canal carpien ») — est une
**condensation**, pas une copie : `m5` porte six items dans un autre ordre, le
`resume` en retient trois reformulés. Laissé tel quel.

#### 5. Contrat de rôle — aucune violation

Balayage des 25 `annexe-dd` sur les marqueurs de check-list actionnable, de
conduite de station et de registre oral (guillemets, 1ʳᵉ/2ᵉ personne, verbes de
prescription, posologies, « suivi », « contrôle à »). **Deux occurrences**, toutes
deux légitimes : German-2 « → Audiométrie de suivi, dosage médicamenteux » et
German-11 « Médicaments • Benzodiazépines • Opiacés → Révision du traitement » —
cette dernière étant l'examen qui départage une chute iatrogène, conservée
délibérément par le volet B (`prune_dd_filler.py`, table `GENERIC_EXAMS`).
Rien à retirer, rien à porter ailleurs.

**Divergences consignées**

- section notée · **German-5**, `m3` « Justifie l'absence d'imagerie
  immédiate » : le sous-item dit « **Critères d'Ottawa négatifs** ». Les règles
  d'Ottawa portent sur la cheville, le pied et le genou ; la clearance du rachis
  cervical relève des règles canadiennes (CCR) ou de NEXUS. La page
  `SSP — AVP` le dit huit fois et ne contient **aucune** occurrence
  d'« Ottawa » : c'est un niveau 1 caractérisé. **Non corrigé** — la divergence
  est *dans* la section notée, que la procédure gèle (« une divergence repérée
  dans une section notée se consigne, elle ne se corrige pas »). Le pédagogique,
  lui, a été aligné (§ 3). **À arbitrer par vous** : c'est le seul endroit du lot
  où un étudiant peut apprendre une règle de décision fausse, et elle est dans le
  corrigé que lit l'examinateur.
- `annexe-dd` · **German-13**, Maladie cœliaque : « Anticorps
  anti-transglutaminase, anti-**gliadine**, anti-endomysium ». Les anticorps
  anti-gliadine natifs sont abandonnés au profit des anti-peptides désamidés ;
  la page `SSP — Diarrhée` nomme « sérologie (anti-tTG IgA + IgA totales) » sans
  écarter explicitement les anti-gliadine. Ni niveau 1 ni erreur interne
  caractérisée (la formulation reste défendable, seulement datée) → **niveau 3,
  non corrigé**.
- `annexe-dd` · **German-6** : la section notée `m2` énumère 15 diagnostics
  différentiels, `annexe-dd` n'en porte que 6 — manquent notamment les causes
  médicamenteuses, le syndrome de Cushing, l'abus d'alcool chronique et la
  rosacée. Enrichissement possible (le contenu est dans le fichier), **non
  fait** : hors des quatre points de la consigne, et le geste porterait sur dix
  hypothèses à documenter. Signalé.
- `annexe-dd` · **27 noms de diagnostic entre crochets** sur les 485 du corpus,
  dans 6 grilles (14, 21, 22, 72, 80, 83) — « [Trouble des conduites] ». German-14
  en porte 6, German-21 une. Ces crochets ne sont pas une convention de la
  grille (German-14 ne les emploie ailleurs que pour la question du patient en
  `m7`) ; ils ne touchent aucun `.criteria-text` ni aucune `patient-response` et
  ne peuvent donc pas déplacer le barème. Les lots g3 et g4 ne les ont pas
  touchés non plus dans German-22 et German-72. **Non corrigé**, cohérence de
  traitement ; défaut d'import cosmétique à arbitrer sur le corpus entier.
- `resume` · **German-24** : la fiche est cohérente et autonome, sans doublon
  avec la section notée (§ 4). Aucune modification hors l'alignement de
  niveau 1 du § 3.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, `report_redundancy.py` **14** (inchangé),
AMBOSS aux trois verts et redondance **147**. **Aucune modification du barème** :
`git diff` ne contient aucun `.criteria-text`, aucun `<input>`, aucun
`<span class="score">`, aucun `maxScores`, aucun `sectionInfo` — vérifié
mécaniquement, règle 1 des arbitrages, `baseline.json` non régénéré. Balises
appariées sur les 7 fichiers (`div`, `ul`, `li`, `span`, `strong`),
`boundsAnomalies` et `uncoveredContent` vides. Le diff est symétrique — 36
insertions pour 36 suppressions, aucune ligne créée ni détruite.

`check_no_loss.py deb95f5` : **10 items signalés sur 7 grilles, verdictés un à
un, aucune perte réelle**. Neuf sont l'effet mécanique de la séparation d'un
`<li>` en trois éléments — `list_items()` rendait auparavant le nom, les
arguments et l'examen en une seule chaîne. Le dixième est German-24, où le mot
remplacé est l'alignement lui-même. Chaque fragment conservé a été recontrôlé
par sa présence littérale dans le HTML après `strip_base64` — 89 chaînes
vérifiées, jamais par `grep` — et chacune des cinq suppressions voulues (« US si
doute », « Radiographie abdominale », « Coloscopie, calprotectine fécale »,
« coronarographie », « ligament annulaire ») confirmée absente.

### Volet g5b — Deuxième lot des grilles à `annexe-dd` seul (German-31 à 60)

**Périmètre — 20 grilles.** German-31 à 60, moins les 6 grilles riches déjà
traitées (**34, 42, 43, 48, 56** du lot g4 et **44**, la grille pilote de
`ff4605c` — critère d'exclusion inchangé : un `resume` **et** une
`presentation`), moins **38 et 39** qui ne portent aucun bloc pédagogique, moins
**52 et 54** qui n'ont pas d'`annexe-dd` (`therapy-section` seules, niveau 2,
hors périmètre — même motif que German-1 en g5a) :

> **31, 32, 33, 35, 36, 37, 40, 41, 45, 46, 47, 49, 50, 51, 53, 55, 57, 58, 59, 60**

**10 grilles modifiées** : 31, 32, 33, 37, 40, 41, 46, 49, 51, 55. Les 10 autres
ont été balayées sur les quatre points sans appeler de modification.

**Modifications — défaut de structure (31 occurrences, 4 grilles)**

Le motif corrigé transmis par g5a — **tout `→` situé hors du `<div>` d'examen
canonique** — est le bon et il est le seul nécessaire. Recherche menée sur les
20 grilles : **31 flèches hors emplacement**, toutes de la **variante B** (avalée
dans le `<strong>` du nom du diagnostic), **zéro** de la variante A (avalée dans
la puce d'arguments). Le lot ne contient donc aucun cas de la variante que
décrivait g4.

| Grille | Occ. | Entrées | Dont coexistant avec un `<div>` d'examen déjà présent |
|---|---:|---:|---:|
| German-31 | 7 | 7 | 6 |
| German-32 | 6 | 6 | 5 |
| German-33 | 8 | 8 | 4 |
| German-37 | 10 | 10 | 3 |
| **Total** | **31** | **31** | **18** |

Contrôle de gabarit préalable : les blocs `annexe-dd` du lot ne portent que
**deux** styles de `<div>` — `rgb(52, 105, 46)` (examen, 45 occurrences) et
`rgb(80, 90, 110)` (arguments, 21). Le motif de recherche ne pouvait donc pas
manquer une troisième variante.

Réparation identique partout : l'examen quitte le `<strong>` et rejoint son
propre `<div>`. Quand un `<div>` existait déjà, les deux listes sont fusionnées
— doublons stricts écartés, **rien de supprimé** hors les corrections factuelles
ci-dessous. Après réparation, les 31 entrées portent toutes leur examen à sa
place (German-31 6→7 `<div>` d'examen, German-32 5→6, German-33 4→8,
German-37 3→10).

**Modifications — erreurs factuelles internes et contaminations d'import**

- `annexe-dd` · **German-55**, Lithiase biliaire/cholédocienne :
  « → **CT abdominal sans contraste, US rénal** » → « → Échographie abdominale
  (voies biliaires), cholangio-IRM si doute ». **Contamination d'import
  caractérisée** : la chaîne est **strictement identique** à celle de l'entrée
  « Lithiase urinaire » de German-51, où elle est juste — c'est le protocole de
  la colique néphrétique, transposé tel quel sur une lithiase **biliaire**, donc
  sur le mauvais organe. Même motif que le *C. difficile* de German-13 (g5a) et
  la colite infectieuse de German-19 (g4). Niveaux 1 **et** 2 concordants :
  `SSP — Ictère` porte « Échographie abdominale (1ʳᵉ intention) : dilatation des
  voies biliaires (cholédoque > 7 mm), lithiase » et « Cholangio-IRM (MRCP) :
  exploration non invasive de référence des voies biliaires », et sa liste de
  pièges éliminatoires dit « Pas d'échographie + CPRE si lithiase » ; la section
  notée `m5` énumère « Échographie abdominale · Recherche de lithiase · Voies
  biliaires ».
- `annexe-dd` · **German-46**, Anémie hémolytique auto-immune :
  « → **FSC, ferritine, B12, folates** » → « → Test de Coombs direct, bilan
  d'hémolyse (bilirubine, LDH, haptoglobine), réticulocytes ». La chaîne
  remplacée est celle des **trois entrées d'anémie carentielle** de la même
  grille, recopiée à l'identique : ferritine, B12 et folates diagnostiquent une
  carence, jamais une hémolyse, et le nom de l'entrée dit lui-même « Test de
  Coombs positif ». Niveau 2 : `m2` nomme « Bilan d'hémolyse [Bilirubine, LDH,
  haptoglobine] » et « FSC complète [Hb, VGM, CCMH, **réticulocytes**] ».
- `annexe-dd` · **German-33**, Hernie hiatale : « → **Examen clinique, US si
  doute** » → « → Radiographie, gastroscopie ». L'ultrason n'explore pas une
  hernie hiatale. La chaîne est **la même** que celle que g5a a retirée de la
  hernie discale cervicale de German-5 : boilerplate d'import, deuxième
  occurrence dans le corpus.
- `annexe-dd` · **German-40**, Infection urinaire : « → **FSC, CRP, hémocultures
  si fièvre** » → « → Bandelette urinaire, ECBU ». Station d'**énurésie
  pédiatrique** : l'examen qui départage y est l'analyse d'urine, absente de la
  ligne, et les hémocultures n'ont aucune place dans ce bilan. Niveau 1 :
  `SSP — Énurésie Nocturne` porte « Bandelette urinaire systématique (éliminer
  une infection, une glycosurie) », « Bandelette urinaire + ECBU STAT », et
  range parmi ses pièges éliminatoires « Manquer cause organique (glycosurie,
  ECBU, écho rénale) ». Niveau 2 concordant : `m3` dit « Analyse d'urine
  (bandelette et culture) ».
- `annexe-dd` · **German-51**, Infection urinaire : même chaîne
  « → FSC, CRP, hémocultures si fièvre » → « → ECBU, bandelette urinaire, FSC,
  CRP ; hémocultures si fièvre ». Ici l'ECBU manquait seul ; les autres examens
  sont conservés (fusion, pas remplacement). Niveaux 1 et 2 : `SSP — Hématurie`
  compte « ECBU systematique » parmi ses pièges éliminatoires, `m4` porte
  « Culture urinaire (ECBU) ».
- `annexe-dd` · **German-31**, Syndrome coronarien aigu : « → ECG, troponines,
  **test d'effort** » → « → ECG, troponines, échocardiographie ». L'épreuve
  d'effort est **contre-indiquée** dans un syndrome coronarien aigu ; la chaîne
  est celle du syndrome coronarien **chronique** (elle figure telle quelle sous
  ce diagnostic en German-33). Niveau 2 : `m3` dit « ECG (éliminer SCA) » et
  « FSC, CRP, troponine », jamais de test d'effort.
- `annexe-dd` · **German-37**, Prostatite aiguë : « → ECBU, **PSA**, toucher
  rectal » → « → ECBU, toucher rectal doux, échographie si doute d'obstacle ».
  Niveau 1 : `SSP — Dysurie` ne contient **aucune** occurrence de « PSA »
  (mesuré : 0), et nomme au contraire « Toucher rectal chez l'homme : prostate
  douloureuse, bombée, chaude → prostatite (**massage à éviter en phase
  aiguë**) » et « ECBU • hémocultures ; écho si doute d'obstacle ». Le PSA est
  faussement élevé en prostatite aiguë et n'y départage rien.
- `annexe-dd` · **German-49**, Adénopathie : « → FSC, CRP, **ECBU, hémocultures
  selon contexte** » → « → Échographie inguinale, FSC, CRP ». Station de
  **hernie inguinale** : ni ECBU ni hémocultures n'y départagent une adénopathie
  inguinale. Niveau 2 : `m3` dit « Échographie inguinale pour confirmation » et
  le `therapy` du même critère « Échographie inguinale : confirmation
  diagnostique ».
- `annexe-dd` · **German-49**, Tumeur des tissus mous : « → CT abdominal,
  **marqueurs tumoraux** » → « → Échographie inguinale, CT abdominal ». Aucun
  marqueur sérique ne départage une tumeur des tissus mous.
- `annexe-dd` · **German-41**, Tumeur cérébrale : « → Imagerie (CT/IRM), biopsie,
  **marqueurs tumoraux** » → « → Imagerie cérébrale (CT/IRM), biopsie ». Même
  boilerplate. Niveau 2 : `m3` nomme « Imagerie : échographie carotides, CT/IRM
  cérébral », sans marqueur.
- `annexe-dd` · **German-33**, Cancer de l'œsophage : « → Imagerie (CT/IRM),
  biopsie, **marqueurs tumoraux** » → « → Gastroscopie avec biopsies, imagerie
  (CT/IRM) pour le bilan d'extension ». Troisième occurrence du même
  boilerplate ; l'examen qui départage est la gastroscopie avec biopsies,
  l'imagerie relevant du bilan d'extension.
- `annexe-dd` · **German-46**, Saignement gastro-intestinal occulte :
  « → Gastroscopie, test Helicobacter pylori » → « → Gastroscopie **et
  coloscopie**, test Helicobacter pylori ». Alignement de niveau 2 : `m6` dit
  « Si suspicion saignement GI [Gastroscopie, coloscopie] », et le nom de
  l'entrée cite la maladie inflammatoire intestinale, que la gastroscopie seule
  ne peut pas explorer.

**« Marqueurs tumoraux » est un boilerplate d'import**, présent à l'identique
sous trois diagnostics sans rapport (cancer de l'œsophage en German-33, tumeur
cérébrale en German-41, tumeur des tissus mous en German-49) et faux pour
chacun. Il est retiré des trois ; à rechercher au-delà de German-60.

**Divergences consignées**

- `annexe-dd` · **German-33** : les entrées « Angor stable » et « Syndrome
  coronarien chronique » sont deux noms du même tableau, dans deux catégories
  voisines du même bloc. Ce n'est pas une erreur factuelle mais un doublon
  d'intitulé ; les fusionner relèverait d'un jugement d'auteur → **niveau 3, non
  corrigé**.
- `annexe-dd` · **German-36** : l'entrée « Bronchectasies » n'a aucun examen qui
  départage, alors que le CT thoracique haute résolution est le seul à trancher.
  Entrée réduite au nom du diagnostic seul, forme **voulue** par le volet B —
  non remplie, conformément à la consigne.
- Section notée · **German-51** : `m3` cote « PSA (si homme > 50 ans) » dans une
  station d'hématurie. C'est défendable (le PSA participe au bilan d'une
  hématurie masculine) et la divergence serait **dans** la section notée, que la
  procédure gèle → non corrigé, signalé pour cohérence avec le retrait du PSA en
  German-37, où le contexte (prostatite aiguë) est différent.

**Contrat de rôle — aucune violation.** Balayage des 20 blocs sur 21 marqueurs de
check-list actionnable, de conduite de station et de registre oral (« expliquer »,
« se présenter », « prescrire », « orienter vers », « hospitaliser »…) :
**0 occurrence**. Aucun remplissage rétabli ; les entrées réduites au nom du
diagnostic seul (German-51, 53, 55, 57, 58, 59, 60…) sont restées telles quelles.

**Duplication avec la section notée — aucun cas**, ce qui confirme l'explication
structurelle de g5a. Comparaison systématique des items d'`annexe-dd` aux
`criteria-text`, `detail-text`, `redflags-text` et `patient-response` hors bloc,
seuil 0.72 : **11 appariements**, tous des recoupements légitimes de rôle ou des
faux positifs de similarité de chaîne (German-60 « Hypotension essentielle » face
à « Hypertension artérielle », German-55 « Hépatite médicamenteuse » face à
« Allergies médicamenteuses »). Les autres opposent un **argument** du
différentiel à l'**acte** que cote le critère (German-57 « Tabagisme important »
face à l'item d'anamnèse du même nom, German-49 « Localisation inguinale
typique » face à « Palpation inguinale spécifique »). Rien à supprimer.

**Le rendement du niveau 1 se prédit bien par le nombre de grilles desservies.**
Les trois pages qui ont tranché desservent **2, 5 et 6** grilles
(`SSP — Énurésie Nocturne`, `SSP — Dysurie`, `SSP — Ictère`) ; les pages muettes
en desservent 16 à 27 (`SSP — Douleur Thoracique` 27, `SSP — Dyspnée` 26,
`SSP — Lombalgies` 24, `SSP — Fatigue` 16). L'indicateur de g5a se vérifie sur ce
lot. Exception à noter : `SSP — Ballonnement (Météorisme)` ne dessert que
German-49 mais reste muette, parce qu'elle **ne traite pas le sujet de la
grille** — la station porte sur une hernie inguinale ; la mono-grille prédit la
précision de la page, pas sa pertinence.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, `report_redundancy.py` **14**
(inchangé), AMBOSS aux trois verts et redondance **147**. **Aucune modification
du barème** : `git diff` ne contient aucun `.criteria-text`, aucun `<input>`,
aucun `<span class="score">`, aucun `maxScores`, aucun `sectionInfo`, aucune
`patient-response` — vérifié mécaniquement (0 ligne). Règle 1 des arbitrages,
`baseline.json` non régénéré. Le diff est symétrique : **39 insertions pour 39
suppressions**, aucune ligne créée ni détruite. `boundsAnomalies` et
`uncoveredContent` vides sur les 10 fichiers. Aucun `</div>` déplacé dans un
`criteria-row` — les blocs `redflags` et `therapy` n'ont pas été ouverts.

`check_no_loss.py 129f03b` : **8 items signalés sur 10 grilles**, verdictés un à
un. Aucun n'est une perte accidentelle : un est l'effet mécanique de la fusion
(German-32, reformulation sous le seuil de ressemblance), les **sept autres sont
les suppressions voulues** documentées ci-dessus (« US si doute », « marqueurs
tumoraux » ×2, « PSA », « test d'effort », « FSC, ferritine, B12, folates »,
« CT abdominal sans contraste, US rénal », « ECBU, hémocultures selon
contexte »). Chaque fragment conservé a été recontrôlé par sa présence littérale
dans le HTML après `strip_base64`, jamais par `grep`. Le contrôle de couverture
préalable — résidu des `<li>` après retrait du `<strong>`, du `<div>` d'examen et
du `<div>` d'arguments — rend **zéro caractère** sur les 20 grilles : aucun
contenu du bloc n'a échappé à la relecture.

---

### Lot g5c — Dernier lot des grilles à `annexe-dd` seul (German-61 à 88)

Départ `2e21433`. **19 grilles** : German-61 à 88, moins les **3 grilles riches**
déjà traitées en g4 (69, 72, 88 — un `resume` **et** une `presentation`), moins
**German-63** qui n'a pas d'`annexe-dd` (5 `therapy-section` seulement, niveau 2 —
même motif que German-1, 52 et 54), moins les **5 grilles sans aucun bloc**
(70, 73, 84, 86, 87 : `blocks_present()` rend une liste vide).

> **61, 62, 64, 65, 66, 67, 68, 71, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 85**

German-78 porte **deux** segments `annexe-dd` (DD cardiaques sous `m2`, DD
pulmonaires sous `m3`) : 20 segments pour 19 grilles. Les 20 hébergent bien un
critère « Diagnostics différentiels » — contrat de rôle respecté structurellement,
vérifié un à un.

**5 grilles modifiées** : 71, 75, 77, 79, 85. Les 14 autres ont été balayées sur
les quatre points sans appeler de modification.

**Modifications**

- `annexe-dd` · **German-71**, Infection urinaire : « → FSC, CRP, hémocultures si
  fièvre » → « → **Bandelette urinaire, ECBU** »
  source : niveau 1, `SSP — Pollakiurie` — « **Bandelette urinaire + ECBU** en
  1ère intention », et point clé n° 2 « bandelette urinaire + bladder scan = duo
  clé immédiat ». **Troisième et dernier exemplaire** de la chaîne fausse déjà
  retirée de German-40 et German-51 par g5b ; la recherche corpus n'en laisse
  aucun autre.
- `annexe-dd` · **German-71**, Diabète insipide : « → Glycémie à jeun, HbA1c » →
  « → **Osmolarité plasmatique et urinaire, test de restriction hydrique** »
  source : niveau 1, `SSP — Polydipsie & Polyurie` — 1re intention
  « Osmolarité plasmatique et urinaire, densité urinaire » ; 2e intention « Test
  de restriction hydrique … urines restant diluées → diabète insipide ». La
  chaîne retirée est **strictement identique** à celle de l'entrée « Diabète
  sucré » **quatre lignes plus haut dans la même grille**, et la glycémie à jeun
  est par définition l'examen qui *exclut* un diabète insipide.
- `annexe-dd` · **German-75**, Néoplasie pulmonaire : « → Imagerie (CT/IRM),
  biopsie, **marqueurs tumoraux** » → « → **Radiographie thoracique, CT
  thoracique, bronchoscopie avec biopsies** »
  source : niveau 1, `SSP — Toux Chronique` — « **CT thoracique ± bronchoscopie**
  si hémoptysie, anomalie radiologique, suspicion de cancer » et « Rx thorax en
  urgence, et **CT thoracique même si la radio est normale** ». La page ne
  contient **0 occurrence** de « marqueur ». L'IRM n'explore pas le parenchyme
  pulmonaire.
- `annexe-dd` · **German-77**, Abcès pulmonaire : « → US ou CT selon
  localisation, ponction » → « → **Radiographie thoracique (niveau
  hydro-aérique), CT thoracique** »
  erreur factuelle interne : l'ultrason ne traverse pas le poumon aéré et ne peut
  pas montrer un abcès intraparenchymateux ; « selon localisation » et
  « ponction » sont le protocole d'un abcès des parties molles ou abdominal.
  Niveau 2 concordant : `m3` cote « Radiographie thoracique ».
- `annexe-dd` · **German-79**, Crise d'asthme : « → Spirométrie avec test de
  réversibilité, peak flow » → **ligne retirée**, entrée réduite au nom du
  diagnostic seul
  la station est une **consultation téléphonique pédiatrique de 21h00** pour une
  fillette de 5 ans, diagnostic principal « faux-croup (laryngite striduleuse) ».
  La spirométrie avec test de réversibilité est le test de *diagnostic de
  l'asthme chronique* — la chaîne est celle de German-78 « Asthme » et de
  German-36 « Asthme bronchique » —, elle n'est ni faisable au téléphone, ni
  interprétable en crise, ni praticable en routine à 5 ans. Niveau 2 : la section
  notée de German-79 ne cote **aucun** examen complémentaire (ses critères sont
  urgence, conseils, signes d'alarme, rappel à 1 h, vérification de la
  compréhension). Même geste que la suppression sèche de German-28 en g5a.
- `annexe-dd` · **German-85** (4 entrées) : réparation du défaut de structure —
  la flèche « → examen » quitte l'élément qui l'avait avalée et rejoint son
  propre `<div>` (détail au § défaut de structure ci-dessous). Une **erreur de
  fond** au passage : « Diabète sucré décompensé » portait **deux** lignes
  d'examens concurrentes, « → Glycémie, glycosurie » prisonnière du nom et
  « → Glycémie à jeun, HbA1c » dans le `<div>`. Fusionnées en « → **Glycémie,
  glycosurie et cétonurie, HbA1c** » : le « à jeun » est retiré (on ne met pas à
  jeun un patient en décompensation, et c'est la chaîne du *dépistage* du diabète
  chronique, identique à German-6, 45, 71 et 81), la cétonurie est ajoutée sur
  niveau 1 — `SSP — Pollakiurie` : « Diabète sucré décompensé (révélation) ·
  **Glycémie capillaire + veineuse + HbA1c + cétonurie** », et
  `SSP — Polydipsie & Polyurie` : « Glycémie veineuse ± HbA1c · **glycosurie /
  cétonurie** ». La coproculture de la gastro-entérite est conservée telle quelle,
  niveau 1 concordant (`SSP — Diarrhée` : « Coproculture standard si fièvre,
  sang, voyage… »).

**Divergences consignées**

- `annexe-dd` · **German-75** : la station est une **tuberculose pulmonaire**
  (infirmière de 34 ans, toux de 6 semaines) et son bloc de différentiels ne
  porte **pas** la tuberculose, alors que la section notée lui consacre `m1`,
  `m3`, `m4`, `m6` et `m7`. Enrichissement possible sans invention, **non fait** —
  hors des quatre points de la consigne, comme German-6 en g5a.
- `annexe-dd` · **German-61** : « Syncope vasovagale » et « Syncope réflexe » sont
  deux noms du même tableau, dans la même liste. Doublon d'intitulé, pas erreur
  factuelle → niveau 3, non corrigé (même arbitrage que German-33 en g5b).
- `annexe-dd` · **German-80** : « [Syndrome parkinsonien iatrogène] → Examen
  neurologique, DaTSCAN si doute » — l'anamnèse médicamenteuse serait le premier
  discriminant, mais le DaTSCAN *est* l'examen qui départage un parkinsonisme
  iatrogène (normal) d'une maladie de Parkinson (anormal), et `m3` cote
  « DaTSCAN (si diagnostic incertain) ». Formulation défendable → niveau 3.
- **Boilerplate « marqueurs tumoraux » — la généralisation de g5b est trop
  large.** Après le retrait de German-75, il reste **8 occurrences** dans le
  corpus (German-12, 13, 18, 21 ×2, 29, 34 ×2), toutes hors de ce lot. Elles ne
  sont **pas** toutes fausses : le CA-125 d'une masse ovarienne (German-18,
  « US pelvienne, marqueurs tumoraux si suspecte ») et l'ACE d'un cancer
  colorectal (German-12, 13) sont d'usage courant. Le boilerplate est faux quand
  l'organe n'a pas de marqueur utile — poumon, cerveau, tissus mous, œsophage —
  et il faut le juger **organe par organe**, pas le retirer en masse. À arbitrer
  sur German-21, 29 et 34, hors périmètre ici.
- « **US si doute** » : 2 occurrences résiduelles dans le corpus (German-15,
  German-21), **aucune** dans ce lot.

**Le défaut de structure — 8 flèches hors emplacement relevées, 4 réparées, 4
écartées comme légitimes.** Le motif prescrit — *tout `→` situé hors du `<div>`
d'examen canonique* — rend 8 occurrences sur 3 grilles. Mais **il a ici une classe
de faux positifs que les deux lots précédents n'avaient pas rencontrée** :

| Grille | Occ. brutes | Vrai défaut | Nature des autres |
|---|---:|---:|---|
| German-65 | 3 | 0 | catégorie « Signes d'alarme à rechercher » : `signe → diagnostic` |
| German-66 | 1 | 0 | catégorie « Signes d'alerte à exclure » : `signe → diagnostic` |
| German-85 | 4 | **4** | `diagnostic → examen` (3 en variante B, 1 en variante A) |
| **Total** | **8** | **4** | |

Les 4 écartées sont « Écoulement fétide → cholestéatome », « Écoulement clair →
fistule LCR », « Sang pur → traumatisme » (German-65) et « Syncope vraie →
arythmie grave » (German-66). Ce ne sont pas des examens avalés : la flèche y
signifie « ce signe oriente vers ce diagnostic », dans des catégories qui listent
des **signes** et non des hypothèses. German-65 est de surcroît **aligné mot pour
mot** sur sa section notée, dont `m2` énumère « Otite moyenne chronique avec
cholestéatome (**écoulement fétide**) » et « Traumatisme avec fracture du rocher
(**sang**, LCR) ». German-66 porte, dans la même entrée, un `<div>` d'examen
correct (« → ECG, Holter ECG ») que `m3` confirme. Rien à réparer dans ces deux
grilles.

**La propriété « tout ou rien » de g5b ne tient pas sur ce lot** : German-85 est
atteinte sur **4 de ses 5** entrées, pas sur la totalité. Le contrôle de gabarit
préalable reste valable — les blocs du lot ne portent que deux styles de `<div>`,
`rgb(52, 105, 46)` (examen, 59 occurrences) et `rgb(80, 90, 110)` (arguments, 39)
— et après réparation la recherche rend **4**, exactement les 4 flèches
sémantiques ci-dessus.

**Contrat de rôle — aucune violation.** Balayage des 20 segments sur 29 marqueurs
de check-list actionnable, de conduite de station et de registre oral
(« expliquer », « rassurer », « prescrire », « orienter vers », « hospitaliser »,
« posologie », « organiser le suivi »…) : **0 occurrence**. Troisième
confirmation consécutive. Aucun remplissage rétabli ; les entrées réduites au nom
du diagnostic seul (German-62 en totalité, 61, 74, 80, 82, 83…) sont restées
telles quelles.

**Duplication avec la section notée — aucun cas**, troisième confirmation.
Comparaison systématique des items d'`annexe-dd` aux `criteria-text`,
`detail-text`, `redflags-text` et `patient-response` hors bloc, seuil 0.72 :
**7 appariements**, tous des recoupements légitimes de rôle — un **argument** du
différentiel face à l'**acte** que cote le critère (German-67/68 « anamnèse
médicamenteuse », German-68 « évolution progressive sur des années », German-81
« origine cardiovasculaire » face à « 4. Examen cardiovasculaire »). Rien à
supprimer.

**Le niveau 1 a tranché quatre points, et l'indicateur de g5b se vérifie une
troisième fois.** Les pages qui ont tranché desservent **1 et 9** grilles
(`SSP — Pollakiurie` mono-grille, deux tranchages ; `SSP — Diarrhée`) plus
`SSP — Polydipsie & Polyurie`, atteinte par le lien « Skills connexes » de la
première. `SSP — Toux Chronique` en dessert **19** et a pourtant tranché le point
« marqueurs tumoraux » — par une **absence** mesurable (0 occurrence du terme) et
non par une prescription. C'est une nuance à ajouter à l'indicateur : une page à
forte cardinalité reste utile pour **infirmer** un examen, même quand elle ne
prescrit rien de précis.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, `report_redundancy.py` **14**
(inchangé), AMBOSS aux trois verts et redondance **147**. **Aucune modification
du barème** : `git diff` ne contient aucun `.criteria-text`, aucun `<input>`,
aucun `<span class="score">`, aucun `maxScores`, aucun `sectionInfo`, aucune
`patient-response`, aucune `scoring-rule` — vérifié mécaniquement (0 ligne).
Règle 1 des arbitrages, `baseline.json` non régénéré. Le diff est symétrique :
**9 insertions pour 9 suppressions**. `boundsAnomalies` et `uncoveredContent`
vides sur les 5 fichiers, `<div>`/`</div>` à écart 0. Aucun `</div>` déplacé dans
un `criteria-row` — les blocs `redflags` et `therapy` n'ont pas été ouverts.

`check_no_loss.py 2e21433` : **4 items signalés sur 5 grilles**, verdictés un à
un — ce sont **les 4 suppressions voulues** (« FSC, CRP, hémocultures si fièvre »,
« Imagerie (CT/IRM), biopsie, marqueurs tumoraux », « US ou CT selon
localisation, ponction », « Spirométrie avec test de réversibilité, peak flow »).
Aucune perte accidentelle. Le remplacement de German-71/Diabète insipide n'est
pas signalé parce que l'ancienne chaîne s'apparie encore à celle de « Diabète
sucré », restée dans la grille — c'est la **preuve mécanique** de la duplication
qui motivait la correction. Contrôle de couverture préalable — résidu des `<li>`
après retrait du `<strong>`, du `<div>` d'examen et du `<div>` d'arguments :
**zéro caractère** sur les 19 grilles, rien hors `<ul>` que le titre du bloc et
les intitulés de catégorie. La revue de fond est donc exhaustive et non un
sondage, sans qu'aucune grille ait été lue en entier.

---

### Tâche g7 — Reliquat du défaut de gabarit d'`annexe-dd` (German-27, 34, 56)

**Départ `7e9285e`. 21 occurrences trouvées, 21 réparées. Le corpus German ne
porte plus aucune flèche hors du `<div>` d'examen canonique, hors les 4 flèches
sémantiques légitimes de German-65 et 66.**

**Pourquoi ce reliquat existait — l'ordre des tâches, pas un oubli de
traitement.** Le motif de recherche juste — *tout `→` situé hors du
`<div style="… rgb(52, 105, 46);">`* — a été établi par g5a. Les 13 grilles
riches, dont German-27, 34 et 56, avaient été traitées **avant**, par g3 et g4,
avec le motif erroné de g4 (`Arguments POUR:` + `→` dans la même puce), qui ne
rend qu'une variante marginale. g5a/b/c ont ensuite balayé avec le bon motif,
mais leur périmètre était **les seules grilles à `annexe-dd` seul**. Ces trois
grilles n'étaient donc dans le périmètre d'aucun lot muni du bon motif. C'est la
même mécanique que la leçon du rapport g6 : les trois corrections de patron de la
campagne ont toutes été transmises au lot suivant, aucune n'a été rejouée en
arrière.

**Modifications — 21 entrées sur les 26 des trois blocs**

- `annexe-dd` German-27 (10 entrées, 9 réparées) · l'examen quitte le `<strong>`
  du nom et rejoint son `<div>` canonique : Tendinopathie de la coiffe
  (Échographie ou IRM), Rupture de la coiffe (IRM ou arthro-IRM), Tendinopathie
  calcifiante (Radiographie standard), Syndrome du défilé thoracique (Tests de
  provocation, EMG), Myalgie/contracture (Examen clinique), Pathologie
  acromio-claviculaire (Radiographie ciblée). Névralgie cervico-brachiale :
  l'entrée portait un `<div>` d'arguments mais **aucun** `<div>` d'examen — il a
  été créé à la suite des arguments, avec « Radiographie cervicale, IRM
  cervicale ». Seule « Capsulite rétractile » était déjà saine.
- `annexe-dd` German-27 · **deux couples compatibles fusionnés** — Arthrose
  gléno-humérale : « Radiographie standard » (prisonnier) + « Radiographie, IRM
  si nécessaire » (`<div>`) → « → Radiographie standard, IRM si nécessaire », le
  prisonnier absorbant le « Radiographie » du `<div>`. Arthrite inflammatoire :
  « Bilan biologique, radiographie » (prisonnier) + « VS, CRP, facteur
  rhumatoïde, anti-CCP » (`<div>`) → « → Bilan biologique (VS, CRP, facteur
  rhumatoïde, anti-CCP), radiographie », le `<div>` détaillant précisément le
  « bilan biologique » du prisonnier. Rien de supprimé dans les deux cas.
- `annexe-dd` German-34 (10 entrées, 9 réparées) · sortie de l'examen hors du
  nom : Sténose peptique (Endoscopie, pH-métrie), Corps étranger (Radiographie,
  endoscopie), Anneau de Schatzki (Transit baryte, endoscopie), Myasthénie (Test
  à la néostigmine, anticorps). Seule « Compression extrinsèque » était saine.
- `annexe-dd` German-34 · **trois couples compatibles** — Achalasie :
  « Manométrie œsophagienne » (prisonnier) + « Manométrie si l'endoscopie est
  normale » (`<div>`) → « → Manométrie œsophagienne si l'endoscopie est
  normale ». Niveaux 1 **et** 2 concordants : `SSP — Dysphagie` porte
  « Manométrie œsophagienne haute résolution si OGD normale — **après OGD** pour
  éliminer une pseudo-achalasie tumorale », et `m3` cote « Manométrie
  œsophagienne (si endoscopie normale) ». AVC/tronc cérébral : le prisonnier
  « IRM cérébrale » est un **doublon strict** de ce que porte déjà le `<div>`
  (« CT cérébral, IRM cérébrale ») — le `<div>` est laissé tel quel, seule la
  flèche sort du nom. Sclérose latérale amyotrophique : « EMG, consultation
  neurologique » (prisonnier) + « IRM cérébrale et médullaire, ponction
  lombaire » (`<div>`) → « → EMG, IRM cérébrale et médullaire, ponction lombaire,
  consultation neurologique », l'EMG — le seul examen qui départage réellement une
  SLA — passant en tête, le bilan d'exclusion et l'adressage conservés.
- `annexe-dd` German-34 · **Cancer de l'œsophage — couple incompatible, `<div>`
  générique retiré.** « Cancer de l'œsophage → **Endoscopie digestive haute avec
  biopsies** » (prisonnier, juste) contre « → Imagerie (CT/IRM), biopsie,
  marqueurs tumoraux » (`<div>`). L'examen prisonnier devient le contenu du
  `<div>`, le générique disparaît.
  source : niveau 1, `SSP — Dysphagie` — « **OGD (endoscopie haute) = 1ᵉʳ examen**
  devant une dysphagie œsophagienne, avec **biopsies étagées**… si suspicion de
  cancer » ; la page contient **0 occurrence** de « marqueur » et **0 occurrence**
  de « IRM », et range le bilan d'extension sous « CT TAP, écho-endoscopie, TEP ».
  Niveau 2 concordant : `m3` cote « Endoscopie digestive haute avec biopsies
  (urgent) » et le corrigé de `m4` écrit « Bilan d'extension : CT TAP,
  écho-endoscopie, PET-CT » — jamais d'IRM, jamais de marqueur. Aucun élément du
  `<div>` retiré n'est perdu : « biopsie » est déjà dans le prisonnier, et
  « Imagerie (CT/IRM) » relève du **bilan d'extension**, pas de l'examen qui
  départage — rôle du `<div>` — et sa moitié « IRM » est fausse pour l'œsophage.
- `annexe-dd` German-34 · **Cancer ORL — couple incompatible, `<div>` générique
  retiré, un élément conservé.** L'examen était prisonnier de la puce
  d'arguments (variante A) : « • larynx, pharynx → **Laryngoscopie, CT ORL** »,
  contre le même « → Imagerie (CT/IRM), biopsie, marqueurs tumoraux » dans le
  `<div>`. La puce est ramenée à « • larynx, pharynx » (sa fonction : préciser la
  localisation) et le `<div>` devient « → **Laryngoscopie avec biopsies, CT
  ORL** ».
  source : niveau 1, `SSP — Dysphonie` — atteinte par le lien « Skills connexes »
  de `SSP — Dysphagie`, geste que g5c avait établi comme rentable — « Cancer du
  larynx / pharyngo-laryngé · **Nasofibroscopie** urgente + **scanner
  cervico-thoracique injecté** + **biopsie sous laryngoscopie directe** + RCP onco
  ORL » ; **0 occurrence** de « marqueur » sur cette page comme sur
  `SSP — Dysphagie`. Niveau 2 concordant : `m2` cote « 5. Laryngoscopie
  indirecte ». **« biopsie » a été conservé** et non supprimé : contrairement à
  l'entrée œsophage, le prisonnier ne le portait pas, et la biopsie sous
  laryngoscopie est nommée par la page SSP — c'est la règle « le dédoublonnage ne
  perd jamais d'information » appliquée à un couple incompatible. « Imagerie
  (CT/IRM) » n'a pas été conservée : le CT ORL est déjà nommé, et l'IRM est une
  formule générique qu'aucune des deux pages ne porte.
- `annexe-dd` German-56 (6 entrées, 3 réparées) · Hypermobilité urétrale (Test à
  la toux, pad-test), Insuffisance sphinctérienne intrinsèque (Bilan
  urodynamique), Incontinence par regorgement (Mesure du résidu post-mictionnel).
  Les 3 autres entrées étaient déjà saines.

**Le « marqueurs tumoraux » n'a pas fait l'objet d'une passe globale**, malgré la
tentation. g5c a établi qu'il se juge **organe par organe** : le CA-125 d'une
masse ovarienne (German-18) et l'ACE d'un cancer colorectal (German-12, 13) sont
d'usage courant et légitimes. Seules les deux occurrences de German-34 ont été
traitées, parce qu'elles étaient dans le périmètre de cette réparation. Le corpus
en compte **6** aujourd'hui (German-12, 13, 18, 21 ×2, 29) contre 8 hier. **Les
deux de German-21 portent exactement les mêmes organes** — œsophage et ORL — que
celles retirées ici, et g5c les avait déjà jugées fausses : c'est le premier
candidat d'une passe future, et le seul cas où la réponse est déjà connue.

**Divergences consignées**

- `annexe-dd` German-34 · « Anneau de Schatzki → Transit **baryte**, endoscopie »
  — coquille d'accent (« baryté »), présente avant cette tâche. Non corrigée :
  hors du périmètre du défaut de gabarit, et `check_nomenclature.py` ne la voit
  pas. À traiter par une passe orthographique transverse, pas grille par grille.
- `annexe-dd` German-34 · « consultation neurologique » conservée dans l'examen
  de la SLA. C'est à la limite du contrat de rôle (`annexe-dd` ne porte pas de
  conduite de station), mais la retirer serait une perte d'information dans une
  fusion, et g5a avait retenu le même arbitrage pour German-11 (« → Révision du
  traitement »).

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, `report_redundancy.py` **14**
(inchangé) et **91** intra-bloc (**inchangé également** : les 21 examens sortis du
nom n'ont créé aucune paire nouvelle ni détruit aucune ancienne, parce que la
normalisation d'un `<li>` d'`annexe-dd` concatène déjà ses trois éléments et que
le déplacement d'un fragment à l'intérieur du même `<li>` ne change pas le texte
comparé). AMBOSS aux trois verts et redondance **147**. **Aucune modification du
barème** : `git diff` ne contient aucun `.criteria-text`, aucun `<input>`, aucun
`<span class="score">`, aucun `maxScores`, aucun `sectionInfo`, aucune
`patient-response`, aucune `scoring-rule` — vérifié mécaniquement (0 ligne).
Comptes de `criteria-row`, `<input>`, `<li>`, `<ul>` et `<strong>` **identiques à
`7e9285e`** sur les trois fichiers. Règle 1 des arbitrages, `baseline.json` non
régénéré. Le diff est symétrique : **21 insertions pour 21 suppressions**, une
ligne par entrée réparée. `boundsAnomalies` et `uncoveredContent` vides,
`<div>`/`</div>` à écart 0 sur les trois fichiers. Aucun `</div>` déplacé dans un
`criteria-row` — les blocs `redflags` et `therapy` n'ont pas été ouverts, et le
`<input type="radio">` du `criteria-row` qui héberge `annexe-dd` appartient au
critère englobant, non touché.

`check_no_loss.py 7e9285e` : **3 items signalés sur 3 grilles**, verdictés un à
un. Deux sont des **artefacts du déplacement** — « névralgie cervico-brachiale
radiographie cervicale irm cervicale arguments pour » (German-27) et « achalasie
manométrie œsophagienne arguments pour » (German-34) sont les chaînes qui
concaténaient le nom, l'examen avalé et le début des arguments ; l'examen est
désormais dans son `<div>`, présence littérale vérifiée. Le troisième, « pas
d'odynophagie franche imagerie ct irm biopsie marqueurs tumoraux » (German-34),
est la **suppression voulue** du `<div>` générique du Cancer ORL ; « Pas
d'odynophagie franche » est toujours présent, vérifié littéralement. Aucune perte
accidentelle. La suppression jumelle sur le Cancer de l'œsophage n'est **pas**
signalée, parce que la chaîne retirée s'appariait à celle du Cancer ORL, retirée
dans le même mouvement — même mécanique de silence informatif que German-71 en
g5c, dans l'autre sens.

**Contrôle de couverture préalable** — résidu des `<li>` après retrait du
`<strong>`, du `<div>` d'examen et du `<div>` d'arguments : **zéro caractère** sur
les 26 entrées des trois grilles. Contrôle de gabarit : les trois blocs ne
portent que **deux** styles de `<div>`, `rgb(52, 105, 46)` (examen, 12
occurrences) et `rgb(80, 90, 110)` (arguments, 11) — aucune troisième variante ne
pouvait échapper au motif. Aucune grille n'a été lue en entier, aucun contrôle
n'a employé un `grep` brut.

---

### Tâche g8 — Les deux « marqueurs tumoraux » de German-21 (œsophage, estomac)

**Départ `7ae720f`. 2 entrées d'`annexe-dd` corrigées. Le boilerplate
« marqueurs tumoraux » tombe de 6 à 4 occurrences dans le corpus.**

**Prémisse vérifiée avant d'éditer — elle n'était exacte qu'à moitié.** La
consigne annonçait, comme le § 4.1 du rapport g6, que German-21 portait « les
mêmes organes que German-34 — œsophage et **ORL** ». Lecture du bloc : German-21
(*Douleur abdominale*, station de reflux chez un sacristain de 56 ans) porte
**Cancer de l'œsophage** et **Cancer gastrique**. Son unique `annexe-dd` compte
dix entrées, **aucune ORL** ; le mot n'apparaît nulle part dans la grille. La
prémisse tient sur l'œsophage, tombe sur l'ORL, et l'arbitrage reste valable pour
l'estomac par le même raisonnement — d'où correction, mais avec une formulation
qui n'est pas celle de German-34.

**Les trois autorités, dans l'ordre.**

- **Niveau 1 — page « SSP — Douleur Abdominale »** (mapping `docs/obsidian-mapping.yaml`,
  seule page desservant German-21) : **0 occurrence de « marqueur »**, 0 de
  « œsoph », et l'IRM n'y est citée que pour la **grossesse** et la **lithiase de
  la voie biliaire principale**. Sur l'endoscopie : « Scanner abdominal préféré ;
  **endoscopie** pour confirmation ». La page ne prescrit pas le point mais ne le
  contredit pas — elle **infirme** en revanche « IRM » et « marqueurs tumoraux »
  par absence mesurable, comme « SSP — Toux Chronique » l'avait fait pour
  German-75.
- **Niveau 2 — section notée `m3` « Examens diagnostiques »** : Gastroscopie ·
  pH-métrie œsophagienne · **Test à l'uréase avec biopsie** · Analyses sanguines
  [Gastrine, vitamine B12, auto-anticorps] · Radiographie ou CT [hernie
  para-œsophagienne]. **Aucun marqueur tumoral, aucune IRM.** Le corrigé que lit
  l'examinateur dit « gastroscopie », et le bloc pédagogique disait « imagerie ».
- **Le bloc lui-même** employait déjà « gastroscopie » deux fois sur des entrées
  voisines : « Œsophagite de reflux → pH-métrie, gastroscopie » et « Ulcère
  gastrique ou duodénal → Gastroscopie, test *Helicobacter pylori* ». Le
  boilerplate était donc en contradiction avec ses propres voisins de liste.

**Modifications**

- `annexe-dd` German-21 · Cancer de l'œsophage : « → Imagerie (CT/IRM), biopsie,
  marqueurs tumoraux » → « → **Gastroscopie avec biopsies étagées** »
  source : SSP — Dysphagie, « OGD = 1ᵉʳ examen … avec biopsies étagées », 0
  occurrence de « marqueur » (autorité établie en g7 pour le même organe) ;
  section notée `m3` de German-21, « Gastroscopie ».
- `annexe-dd` German-21 · Cancer gastrique : « → Imagerie (CT/IRM), biopsie,
  marqueurs tumoraux » → « → **Gastroscopie avec biopsies multiples de la
  lésion** »
  source : section notée `m3` de German-21 (« Gastroscopie », « Test à l'uréase
  avec biopsie ») ; page SSP, 0 « marqueur ». L'estomac n'a pas davantage que
  l'œsophage de marqueur d'usage diagnostique — l'ACE et le CA 19-9 y sont des
  outils de suivi, pas de diagnostic.

**Pourquoi « gastroscopie » et non « endoscopie digestive haute » comme en
German-34.** German-34 est une dysphagie, dont la page SSP et le bloc emploient
« endoscopie » ; German-21 est une station de reflux dont la **section notée**
écrit « Gastroscopie » et dont deux entrées voisines l'écrivent aussi. La
consigne autorisait explicitement l'adaptation au contexte de la grille, et le
niveau 2 fait foi sur le vocabulaire du corrigé. Les deux formulations désignent
le même examen.

**Pourquoi les deux entrées ne sont pas rendues identiques.** L'`annexe-dd` sert
à nommer *l'examen qui départage*, et deux hypothèses distinctes qui reçoivent
mot pour mot la même conduite n'apprennent rien — c'était précisément le défaut
du boilerplate. « Biopsies étagées » (protocole de l'œsophage, y compris pour le
Barrett que la même liste porte) et « biopsies multiples de la lésion » (règle de
l'ulcère gastrique, dont la même liste porte l'entrée) distinguent les deux
gestes sans rien ajouter d'inventé. Aucune stadification n'a été ajoutée : le CT
TAP, l'écho-endoscopie et le PET-CT relèvent du bilan d'extension, hors du
contrat de rôle d'`annexe-dd`.

**Divergences consignées — les 4 « marqueurs tumoraux » restants, non corrigés**

- `annexe-dd` German-12 · côlon, « Coloscopie avec biopsies ; imagerie (CT/IRM),
  marqueurs tumoraux » : **le marqueur est juste** (ACE, bilan initial), la
  coloscopie est déjà en tête. Non corrigé. Le point discutable est l'**IRM** —
  page « SSP — Constipation » : 0 « IRM », 7 « coloscopie » ; l'IRM est l'examen
  du rectum, pas du côlon. Priorité basse.
- `annexe-dd` German-13 · côlon **et rectum**, « Coloscopie avec biopsies,
  imagerie (CT/IRM), marqueurs tumoraux » : **juste sur les deux points**,
  « colorectal » incluant le rectum où l'IRM pelvienne est l'examen de
  stadification. Non corrigé, et à ne pas corriger.
- `annexe-dd` German-18 · ovaire, « US pelvienne, marqueurs tumoraux **si
  suspecte** » : **juste**, le CA-125 est le complément standard d'une masse
  annexielle suspecte, et c'est la garde conditionnelle qui rend l'entrée exacte.
  Non corrigé, et à ne pas corriger.
- `annexe-dd` German-29 · os / métastase, « Tumeur osseuse primitive ou métastase
  → CT abdominal, marqueurs tumoraux » : **fautif, mais par l'examen plus que par
  le marqueur.** La page « SSP — Douleur de Hanche » tranche au **niveau 1** —
  « RX hanche + **scintigraphie osseuse** » pour la métastase, puis « IRM / CT
  TAP · **électrophorèse des protéines** » ; **0 occurrence de « marqueur »** sur
  ses 413 lignes. La section notée de German-29 cote radiographie du bassin, IRM
  de hanche, échographie, scintigraphie osseuse si IRM contre-indiquée, FSC/CRP/VS,
  bilan phosphocalcique — **ni CT abdominal ni marqueur**. Un CT abdominal ne
  montre pas la lésion de hanche : il cherche un primitif, et il vient après la
  radiographie. Non corrigé — hors périmètre de cette tâche, qui ne portait que
  sur German-21 ; c'est une réécriture d'entrée, pas un retrait de boilerplate.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, `report_redundancy.py` **14**
(inchangé) et **90** intra-bloc — **91 avant**, et l'écart est expliqué et voulu :
la paire perdue est la seule paire intra-bloc de German-21, appariée à **0,86**,
« cancer de l œsophage imagerie ct irm biopsie marqueurs tumoraux » contre
« cancer gastrique imagerie ct irm biopsie marqueurs tumoraux ». Elle ne devait sa
similarité qu'au boilerplate ; les deux entrées distinguées s'apparient à 0,67,
sous le seuil de 0,72. **Une redondance réelle en moins, pas un item perdu.**
AMBOSS aux trois verts et redondance **147**. Commande de détection du défaut de
gabarit : **4**, les flèches sémantiques de German-65 (×3) et German-66 (×1),
valeur attendue inchangée. `baseline.json` non régénéré.

**Aucune modification du barème** : le diff ne touche que deux `<div>` d'examen à
l'intérieur du bloc `annexe-dd`, qui ne porte aucune case à cocher ; le
`<input type="radio">` du `criteria-row` hôte appartient au critère englobant et
n'a pas été approché. Aucun `.criteria-text`, aucun `<input>`, aucune
`patient-response` dans le diff — 2 insertions pour 2 suppressions, une ligne par
entrée. `boundsAnomalies` et `uncoveredContent` vides.

`check_no_loss.py 7ae720f German-21_` : **2 items signalés**, tous deux
verdictés — ce sont exactement les deux chaînes remplacées. Contrôle mot à mot du
résidu : les seuls mots qui disparaissent de la grille sont **« imagerie »,
« IRM », « marqueurs », « tumoraux »**, c'est-à-dire la totalité de ce qui devait
partir et rien d'autre. « Cancer de l'œsophage », « Cancer gastrique » et
« biopsie » (sous la forme « biopsies ») sont toujours présents ; « CT » reste
dans la grille par la section notée `m3` (« Radiographie ou CT »). Après
correction, la grille porte **0 « marqueur »** et **0 « IRM »**. Aucune perte
accidentelle.

Aucune grille n'a été lue en entier, aucun contrôle n'a employé un `grep` brut.

---

### Tâche g8 (suite) — German-29, l'entrée « tumeur osseuse / métastase »

**Départ `1978c16`. 1 entrée d'`annexe-dd` réécrite. Le boilerplate
« marqueurs tumoraux » tombe de 4 à 3 occurrences, et les 3 restantes sont
justes : le point est clos.**

**Ce n'était pas un retrait, c'était une réécriture — et le niveau 1 la dicte.**
L'entrée disait « Tumeur osseuse primitive ou métastase → **CT abdominal,
marqueurs tumoraux** ». Deux fautes distinctes : un examen qui ne montre pas la
lésion (un CT abdominal cherche un primitif, il n'image pas la hanche, et il
vient après la radiographie) et un marqueur que ni la page ni le corrigé ne
nomment. La station est une **nécrose aseptique de la tête fémorale** chez
M. Müller, 42 ans, **transplanté rénal sous corticothérapie** (`m1` :
« Nécrose aseptique de la tête fémorale (ostéonécrose) » ; `m8` : « Collaboration
avec néphrologue (ajustement immunosuppression) »).

**Niveau 1 — page « SSP — Douleur de Hanche », 413 lignes, 0 occurrence de
« marqueur ».** Elle traite le point trois fois, et chaque fois nommément :

- DD Top 5 : « Douleur nocturne constante + AEG + amaigrissement ± antécédent de
  cancer connu → Métastase osseuse / néoplasie · **RX hanche + scintigraphie
  osseuse** » — c'est la ligne qui répond exactement à la question du bloc,
  « qu'est-ce qui départage ? » ;
- tableau de prise en charge : « Métastase / fracture pathologique · ATCD
  néoplasique (sein, poumon, prostate, rein, thyroïde, **myélome**) → IRM / CT
  TAP · **électrophorèse des protéines** · avis oncologique » ;
- biologie : « Si red flag (fièvre, AEG) : FSC, CRP, VS, créatinine, calcémie,
  phosphatémie, **électrophorèse des protéines** (myélome) ».

**Niveau 2 — la section notée**, qui concorde : `m3` « Examens complémentaires
d'imagerie » cote Radiographie bassin face + hanche face/profil [signes
d'ostéolyse et ostéosclérose côte à côte] · IRM de hanche · Échographie ·
**Scintigraphie osseuse** si IRM contre-indiquée ; `m4` « Examens biologiques »
cote FSC, CRP, VS · hémocultures si fièvre · ponction articulaire · **bilan
phosphocalcique** · fonction rénale. **Ni CT abdominal, ni marqueur tumoral, ni
imagerie abdominale d'aucune sorte.**

**Modifications**

- `annexe-dd` German-29 · Tumeur osseuse primitive ou métastase : « → CT
  abdominal, marqueurs tumoraux » → « → **Radiographie bassin + hanche,
  scintigraphie osseuse, électrophorèse des protéines si suspicion de myélome** »
  source : SSP — Douleur de Hanche, DD Top 5 « RX hanche + scintigraphie
  osseuse » (transcription), et biologie « électrophorèse des protéines
  (myélome) » ; section notée `m3` (« Radiographie bassin face + hanche
  face/profil », « Scintigraphie osseuse ») et `m4` (« bilan phosphocalcique »).

**Trois choix de rédaction, et ce qui les motive.**

1. **La radiographie passe en tête.** C'est le premier examen des trois entrées
   voisines du même bloc (Coxarthrose, Arthrite septique, Arthrite réactive,
   Fracture de contrainte) et le premier de `m3`. L'entrée fautive la sautait.
2. **Le CT est retiré, pas remplacé par « CT TAP ».** La page ne cite le CT TAP
   qu'en **colonne de prise en charge**, une fois la métastase retenue — c'est du
   bilan d'extension et de la recherche du primitif, hors du contrat de rôle
   d'`annexe-dd` (« l'examen qui départage »). La section notée n'a **aucun** CT.
   Le retenir aurait été garder la moitié juste d'un examen mal placé.
3. **L'électrophorèse est incluse, avec sa garde.** Le myélome est le
   différentiel qui change la conduite devant une lésion osseuse, la page le
   nomme deux fois et l'associe explicitement à l'électrophorèse, et `m4` cote
   déjà le bilan phosphocalcique et la VS — les deux autres axes du même
   raisonnement. La garde « si suspicion de myélome » reprend la parenthèse de la
   page et la grammaire du bloc, qui écrit déjà « si doute », « si épanchement »,
   « si IRM contre-indiquée ». **Elle est proposée, pas imposée** — un myélome à
   42 ans reste rare, et sans la garde l'entrée prescrirait une électrophorèse à
   tout le monde.

**Rien n'a été inventé** : chaque terme de la nouvelle entrée est présent
littéralement soit dans la page SSP, soit dans la section notée de German-29,
souvent dans les deux. La question de savoir s'il fallait s'arrêter s'est posée
pour le seul point de l'électrophorèse ; la garde conditionnelle la tranche, sur
le modèle de German-18 (« marqueurs tumoraux **si suspecte** »), la seule entrée
du corpus dont la garde est ce qui la rend exacte.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, `report_redundancy.py` **14** et
**90** intra-bloc — **les deux inchangés** : la nouvelle entrée s'apparie au plus
à **0,44** avec les items du même bloc (voisin le plus proche : « arthrose de
hanche radiographie bassin face hanche profil »), loin du seuil de 0,72, et
l'ancienne n'était appariée à rien. L'unique paire intra-bloc de German-29
(**0,79**, « contexte d'immunosuppression / radiographie, ponction articulaire si
épanchement » contre « syndrome de Reiter / … ») **préexiste et est légitime** :
deux arthrites qui partagent réellement le même examen qui départage — vérifié
identique à `1978c16`. AMBOSS aux trois verts et redondance **147**. Commande de
détection du défaut de gabarit : **4**, inchangée. `baseline.json` non régénéré.

**Aucune modification du barème** : 1 insertion pour 1 suppression, dans le seul
`<div>` d'examen. Aucun `.criteria-text`, aucun `<input>`, aucune
`patient-response` dans le diff (0 ligne). Comptes identiques à `1978c16` :
`<div>` 860, `<li>` 10, `<strong>` 10, `<input>` 169, `criteria-row` 36, radio
52, checkbox 117. Le bloc `redflags` et les quatre blocs `therapy` de la grille
n'ont pas été ouverts — aucun `</div>` déplacé dans un `criteria-row`.
`boundsAnomalies` et `uncoveredContent` vides.

`check_no_loss.py 1978c16 German-29_` : **1 item signalé**, la chaîne remplacée.
Contrôle mot à mot : les seuls mots qui quittent la grille sont **« abdominal »,
« marqueurs », « tumoraux »**. « Tumeur osseuse primitive ou métastase » est
intact, et « CT » reste présent par l'entrée « Fracture de contrainte du col
fémoral → Radiographie, CT ou IRM si doute ». Après correction German-29 porte
**0 « marqueur »** et **0 « CT abdominal »**. Aucune perte accidentelle.

**Le point « marqueurs tumoraux » est clos.** Décompte final mesuré sur les 88
grilles : **3 occurrences**, German-12 et 13 (ACE, cancer colorectal) et
German-18 (CA-125 sur masse annexielle, gardée par « si suspecte »). Les trois
sont **justes** et doivent rester. Les 4 autres occurrences de « marqueur » du
corpus (German-11, 51, 76, 77) sont des « marqueurs **inflammatoires** », sans
rapport. 13 au départ de la campagne → 8 → 6 (g7) → 4 → **3, et plus rien à
retirer ni à réécrire**.

---

### Tâche p1 — German-1 (Abus d'alcool), grille pilote des sections pédagogiques

**Ce qui change de nature.** Les tâches g1 à g8 corrigeaient du contenu existant
et n'en créaient aucun. Celle-ci **crée** quatre sections là où la grille n'en
portait aucune. La garantie qui remplace l'interdiction est le **sourçage
strict** : chaque énoncé provient soit de la page SSP de la grille, soit d'une
section notée de German-1 — jamais d'ailleurs. Le présent journal donne, section
par section, d'où vient sa matière.

**Les deux sources, et rien d'autre.**

| Sigle | Source |
|---|---|
| **SSP** | `SSP — Dépendance & Addictions (Alcool, Tabac, Drogues).md` (vault, lue en entier) |
| **a1…a18 / e1…e8 / m1…m8 / c1…c5** | les quatre sections notées de German-1, `criteria-text`, `detail-text` et `patient-response` |
| **T1/T2/T3** | les trois `therapy-section` du critère `m5` — corrigé de niveau 2, non modifié |

#### Ce qui a été produit

| Bloc | Volume (hors base64) | Structure |
|---|---|---|
| `resume` | 8,5 Ko | 5 `resume-section`, 15 `resume-subsection`, 60 items |
| `annexe-theorie` | 8,4 Ko | 8 `theorie-section` (dont `-rappels` et `-examens`), 28 items |
| `presentation-patient` | 18,4 Ko | 5 `presentation-section`, 9 `presentation-qa`, 41 items |
| `images-wrapper` | 0,8 Ko + 78,7 Ko de base64 | 1 `annexe-item` |

Total de la zone pédagogique hors base64 : **37,1 Ko**. Fichier : 88,0 → 206,3 Ko.

Le gabarit HTML est celui d'AMBOSS-1, repris classe par classe. **Aucune classe
inventée** : les 40 classes employées dans la zone pédagogique sont toutes
déclarées dans `cases/case-styles.css` (contrôle automatique, 0 écart). Les
modificateurs `list` et `text` de `presentation-reponse`, présents dans AMBOSS-1
mais **absents du CSS**, ont été écartés au profit du `presentation-reponse` nu.

#### Sourçage, section par section

**`resume` — 🔍 Anamnèse.** Quantification et contexte : `a3`, `a4`, `a5` +
SSP § ANAMNÈSE (« unités/semaine, pattern de consommation »). Paquets-années :
`a14` + SSP § Mnémoniques. Dépistage : `a7` (CAGE, seuil 2/4) et `a6` (critères
de dépendance, seuil 3/6), la liste des six critères venant de SSP § Critères de
dépendance (CIM-11 / DSM-5). AUDIT-C : SSP § Quantification. Parcours de soins :
`a8` ; « antécédent de sevrage compliqué » : SSP § Comorbidités. Retentissement :
`a16` + SSP (« familial, professionnel, judiciaire, financier »). Comorbidité
psychiatrique : SSP. Prochaska : SSP § Préparation au changement. Plaintes
somatiques : `a9`, `a10`, `a11` mot pour mot.

**`resume` — 👀 Examen clinique.** Signes d'imprégnation chronique : SSP § Signes
d'alcoolisme chronique, complétés par `e6` (érythrose faciale, télangiectasies,
haleine alcoolisée) et `e2` (hypertrophie parotidienne), `e7` (état nutritionnel,
hydratation, hygiène). Examen ciblé : `e1` à `e4` littéralement. Sevrage en
cours : SSP § Signes de sevrage en cours ; le score est donné sous ses deux noms
sourcés — **Cushman** (T1) et **CIWA-Ar** (SSP). Status mental : SSP § Status
mental (Korsakoff → MMSE/MoCA, idéation suicidaire) + `e3`.

**`resume` — 🧪 Examens.** `m3` et `m4` intégralement, fusionnés avec
SSP § EXAMENS COMPLÉMENTAIRES pour ce que `m3` ne cite pas (γ-GT, VGM, CDT,
magnésium, phosphate, glycémie, toxicologie urinaire, sérologies, ECG).

**`resume` — 💊 Prise en charge.** Critères de lieu : `m7` (les quatre)
+ SSP § Règle d'or (« le sevrage d'un buveur chronique est une urgence ») et
SSP § Pièges (ambulatoire proscrit si ATCD de DT, crises ou comorbidités
sévères) + SSP § PRISE EN CHARGE (« DT = soins intensifs »). Traitement :
SSP (lorazépam/oxazépam si insuffisance hépatique ; thiamine avant glucose ;
Mg, K, phosphate). Suivi : `m6` intégralement. Tabac : `a14` + SSP § Sevrage
tabagique. Posture : SSP § Entretien motivationnel (OARS, Ruler, ambivalence,
discours-changement, ne jamais confronter) et SSP § Filet de sécurité (**144**).

**`resume` — ✅ Points clés.** SSP § Points Clés ECOS, recoupé par les seuils de
`a6` et `a7`.

**`annexe-theorie` — premier du corpus German.** Diagnostic : `a6` (seuil 3/6,
atteint 6/6) et SSP § DD Top 5 (« Trouble de l'usage de l'alcool »). Argumentaire :
les six réponses patient de `a6` et les quatre de `a7`, citées ; l'explication de
ce que mesure le CAGE vient de SSP § Cartes ECOS. Physiopathologie GABA-A / NMDA,
chronologie 6-12 h / 12-24 h / 24-48 h / 48-96 h, mortalité 5-15 % : SSP § Cartes
ECOS et § Sevrage alcoolique & complications. Benzodiazépines (pourquoi elles,
pourquoi lorazépam/oxazépam, pourquoi pas les neuroleptiques seuls) : SSP § Cartes
ECOS, carte « Traitement du sevrage alcoolique ». Thiamine avant glucose et triade
de Wernicke : SSP § Cartes ECOS + § Encéphalopathie de Wernicke ; le rattachement
aux réponses de `a11` et `a9` est explicite et prudent. Différentiel : les trois
hypothèses de `m2`, chacune dotée de son discriminant sourcé — CAGE contre
AUDIT/AUDIT-C (SSP), voie d'administration et risque VIH/VHC/endocardite (SSP),
chronologie et comorbidité psychiatrique (SSP). Seuils chiffrés : `a6`, `a7`,
SSP (AUDIT-C /12, paquets-années, DT 48-96 h et mortalité, thiamine 500 mg IV
x3/j puis 250 mg/j).

**`presentation-patient` — aucune donnée clinique nouvelle.** Checklist, version
longue, SBAR, mnémos et Q/R ne font que reformater `resume` et `annexe-theorie`.
Les mnémos sont ceux de SSP § Mnémoniques (CAGE, OARS, chronologie du sevrage,
triade de Wernicke). La quatrième question (« le patient refuse le sevrage »)
répond avec SSP § Entretien motivationnel, § Exploration de l'ambivalence,
§ Échelle de motivation, § Filet de sécurité et § Clôture — cinq blocs `phrase`
de la page, restitués à la première personne.

**`images-wrapper`.** Une seule image, `general-signes-et-symptomes-du-syndrome-de-sevrage-d-alcool.png`
(60 465 octets, 80 620 caractères en base64). Gabarit repris des 9 grilles German
à image (36, 42, 43, 44, 57, 61, 68, 75, 78) : `annexe-item` > `annexe-title` +
`annexe-description` + `annexe-image` > `img`, à l'intérieur d'un `images-wrapper`
frère de `annexes-grid`.

#### Trois décisions à consigner

1. **Le choix de l'image.** La page SSP en propose six ; deux étaient candidates.
   **AUDIT-C a été écarté** : c'est un questionnaire de dépistage, et la grille ne
   dépiste pas par l'AUDIT-C mais par le **CAGE** (`a7`) — le score AUDIT-C
   n'apparaît nulle part dans les quatre sections notées. Le tableau du **syndrome
   de sevrage** sert au contraire trois critères notés : `a6` (« Syndrome de
   sevrage »), `m5` (« Sevrage et prévention du syndrome de sevrage ») et `m7`
   (« Risque de sevrage sévère »).

2. **Divergence de source, signalée et non lissée.** L'image situe le delirium
   tremens à **48-72 h**, le texte de la page SSP à **48-96 h**. Le corps des
   fiches emploie le chiffre du texte ; la légende décrit fidèlement l'image et
   **mentionne l'écart**. Aucune des deux sources n'a été corrigée par l'autre.

3. **`annexe-theorie` est déclaré dans `lib_german.BLOCKS`.** Sans cette entrée,
   la classe `theorie-section` — qui figure dans `CONTENT_CLASSES` — serait vue
   **hors de tout bloc** par `uncovered_content()`, et `check_invariants.py`
   échouerait à juste titre : c'est exactement l'angle mort d'AMBOSS-34. Motif de
   début et queue attendue sont repris de `lib_amboss.BLOCKS`. L'ajout **ne
   change rien pour les 87 autres grilles** : `blocks_present()` ne liste que les
   blocs présents, et aucune n'en porte.

#### Là où la source était muette — et où la section a été écourtée

- **Constantes du patient.** Le panneau `vital-signs` de German-1 est **vide** et
  la vignette ne donne aucun chiffre. La version longue présente donc l'examen
  comme ce que l'on **rechercherait**, jamais comme des trouvailles. Aucune
  constante n'a été inventée.
- **Sensibilité et spécificité.** Aucune valeur de performance de test (CAGE,
  AUDIT-C, marqueurs) ne figure dans la page SSP. La section « Seuils et repères
  chiffrés » ne porte donc que des **seuils** et des **délais**, pas de Se/Sp —
  là où l'`annexe-theorie` d'AMBOSS-1 en donne pour le signe de Murphy.
- **Sévérité du trouble.** Ni la grille ni la page ne gradent le trouble de
  l'usage. Le diagnostic est écrit « trouble de l'usage de l'alcool avec
  dépendance, évoluant depuis huit ans », **sans qualificatif de sévérité**.
- **Violence conjugale.** `a7` porte une réponse patient explicite (« je l'ai
  parfois frappée »). Elle est **restituée** dans la version longue, parce
  qu'elle est dans la section notée. Mais la page SSP **ne dit rien** de la
  violence dans le couple : aucune conduite à tenir n'a été rédigée. C'est le
  point le plus net de silence de la source, et il est laissé tel quel.
- **Interprétation du bilan hépatique.** La page ne donne que la liste
  (transaminases ASAT/ALAT > 2, bilirubine, albumine, crase/TP). La phrase
  « l'albumine et la crase mesurent la fonction de synthèse » a été **écrite puis
  retirée** : exacte, mais absente des deux sources.
- **ECG.** La ligne « L'ECG cherche un allongement du QT… » de l'`annexe-theorie`
  a été **supprimée** : la page ne dit rien de plus que ce que le `resume`
  énumère déjà, et la garder n'aurait produit qu'une redite (0,79).
- **Méthadone + BZD + alcool.** Piège majeur de la page SSP, mais **hors sujet
  ici** : ce patient n'a aucun opioïde. La phrase a été écrite puis retirée.

#### Vérifications

`check_invariants.py` **OK 88** après régénération justifiée du baseline —
`snapshot_invariants.py` relancé, puis **diff champ par champ des 88 grilles** :
**une seule grille diffère, German-1, sur un seul champ, `blocks`** :
`[["therapy",3]]` → `[["therapy",3],["resume",1],["annexe-theorie",1],["presentation",1],["annexe-image",1]]`.
Les trois `therapy` sont **inchangés en nombre**, et aucun des sept autres champs
(`maxScores`, `scoreSpans`, `sectionCounts`, `criteriaCount`, `detailCount`,
`radioCount`, `checkboxCount`) ne bouge nulle part. Preuve que le travail n'a
fait qu'**ajouter**.

`check_nomenclature.py` **OK**, aucun terme non suisse : `FSC` (jamais « NFS »),
`g/L`, `G/L`, `144` (jamais « 911 » ni « SAMU »). `check_reachability.py`
**OK 88/88 à 100 %**. AMBOSS aux trois verts, redondance **147** inchangée.

`report_redundancy.py German-1_` : **2 paires**, contre 7 à la première rédaction.
Les cinq supprimées l'ont été en rendant le `presentation` réellement oral (le
`response-list` des examens est passé d'une liste de noms d'analyses à une liste
groupée par intention, la réponse « traitement » à la première personne) et en
retirant la ligne ECG redondante de la théorie. Les **deux qui restent sont
justifiées par un changement de format** :

| Ratio | Paire | Justification |
|---|---|---|
| 0,84 | `resume` ↔ `presentation` — chronologie du sevrage | La **page SSP elle-même** porte ce fait deux fois, en deux formats : chronologie en prose (§ Sevrage alcoolique) et mnémonique (§ Mnémoniques). Le `resume` en fait un point clé, le `presentation` la chaîne fléchée à réciter. |
| 0,77 | `therapy` ↔ `presentation` — hydratation et électrolytes | « Hydratation et correction des troubles électrolytiques » (corrigé du critère `m5`, **non modifié**) contre « Hydratation, et je corrige les électrolytes » — la phrase prononcée. Restituer le corrigé à l'oral **est** le rôle du bloc. |

Total German : **14 → 16 paires**, l'écart étant exactement ces deux-là.
`check_no_loss.py HEAD German-1_` : **0 item disparu**.

**Intégrité.** `<div>` 891/891, `<li>` 132/132, `<ul>` 37/37, `<p>` 29/29,
`<h3>` 4/4, `<h4>` 23/23, `<h5>` 23/23, `<span>` 123/123, `<strong>` 10/10,
`</html>` final présent. `boundsAnomalies` et `uncoveredContent` **vides**.
Aucun **chevron nu** `<` introduit dans la zone pédagogique. Le diff de la grille
est **476 insertions, 0 suppression** : le fichier d'avant est **octet pour
octet** le préfixe du nouveau jusqu'au point d'insertion, et la queue à partir de
`<!-- COMMENTAIRE GÉNÉRAL -->` est identique. `criteria-text` (34),
`detail-text` (112), `patient-response` (57), `<input>` (155),
`communication-text` (5), `communication-desc` (5), `window.caseConfig` et les
trois `therapy-section` : **tous identiques à HEAD**, comparés chaîne par chaîne.

### Tâche p1b — German-1 : cartes de méthode et balisage sémantique

Trois décisions de l'utilisateur appliquées à la grille pilote. HEAD réel au
démarrage : **`06b189e`**, pas `6d8ee8d` — la session RESCOS avait commité six
fois entre-temps. Vérifié, pas supposé.

#### 1. La « Checklist mentale » retirée, deux cartes à sa place

La section `section-checklist` et ses **11 items** ne figurent plus dans German-1
et ne figureront dans aucune grille german. À sa place, `section-commcards` avec
les deux images **référencées** (`../img/commcard-sbar.jpg`,
`../img/commcard-snapps.jpg`), jamais embarquées, dans le `.commcard-grid`
documenté par `case-styles.css` — `figure.commcard-item` + `img` +
`figcaption.commcard-caption`, la forme exacte de son commentaire d'usage.

Les deux `alt` (534 et 621 car.) ont été rédigés **après ouverture des images** :
les cinq lignes du tableau SBAR avec leurs items et la mention des exemples
rédigés, les six étapes de SNAPPS avec leurs consignes et la colonne d'amorces.

**Dix lignes de CSS ajoutées**, en fin du bloc « cartes de communication » :
`.presentation-section-title` porte `border-bottom: 3px solid` sans couleur, que
chaque variante `.section-*` fournit. Sans règle, `section-commcards` héritait
`currentColor` — un trait noir épais. Forme reprise des sept variantes existantes.

#### 2. `annexe-expert` / `annexe-scenario` : rien à faire, rien fait

Contrôlé : aucune occurrence dans German-1.

#### 3. Le balisage sémantique — 260 termes, 0 hors des quatre conteneurs

| Conteneur | red | pink | green | blue | amber | purple | orange | yellow | total | densité |
|---|---|---|---|---|---|---|---|---|---|---|
| `resume` | 24 | 32 | 26 | 0 | 10 | 4 | 2 | 5 | **103** | 1 / 7,5 mots |
| `annexe-theorie` | 22 | 28 | 31 | 6 | 8 | 5 | 2 | 2 | **104** | 1 / 10,4 |
| `section-mnemo` | 3 | 4 | 1 | 0 | 1 | 0 | 0 | 2 | **11** | 1 / 8,5 |
| `section-questions` | 6 | 9 | 18 | 0 | 3 | 2 | 2 | 2 | **42** | 1 / 9,9 |
| **Total** | **55** | **73** | **76** | **6** | **22** | **11** | **6** | **11** | **260** | **1 / 9,1** |

**La dose a été calibrée par la mesure, pas à l'œil.** Densité de la page SSP de
référence, texte visible : **1 span / 11,3 mots** en moyenne, avec une fourchette
régionale de **1 / 7,6** (examens et prise en charge, la plus dense) à 1 / 15,1
(prose de fin de page). Première rédaction : 287 spans, dont un `resume` à
**1 / 6,0** — plus dense que la plus dense région de l'utilisateur. **27 spans
retirés du `resume`** pour le ramener à 1 / 7,5. Ce qui a sauté : les répétitions
internes (`ascite`, `hépatomégalie`, `circulation collatérale` déjà colorés deux
lignes plus haut ; `delirium tremens` trois fois dans la même sous-section), les
étiquettes de méthode prises pour du contenu (`Mini-examen neurologique`,
`Antécédent de sevrage compliqué`), les analyses secondaires (`TSH`,
`CT abdominal`, `magnésium`, `phosphate`) et trois ambres posés sur des
électrolytes qui ne sont pas une prescription. Les intitulés de rubrique
(« Cutanés : », « Foie : ») restent noirs, comme les `**Cutanés**` en gras non
colorés de la page SSP.

`c-blue` reste à 6 emplois (2,3 %) : la page de référence n'en compte **qu'un**
sur 301. Marginal à dessein.

**L'idiome `.c-red.c-red` : le balisage en bénéficie, et c'est mesuré.** Les
classes sont posées sur des `<span>` descendants, jamais sur le `<li>` : la règle
`[data-theme="dark"] .resume-subsection-points li { color: … !important }` ne
leur parvient que par héritage, que toute déclaration directe bat. La classe
doublée verrouille le reste. Contrôle **exhaustif** par sonde JavaScript sur les
**260 spans**, dans les deux thèmes : couleur calculée relevée pour chaque span
et pour son parent, **`NEUTRALISES=0`** — aucun span dont la classe soit
silencieusement écrasée. C'est exactement le mode d'échec que l'idiome existe
pour empêcher.

#### Vérifications

`check_invariants.py`, `check_nomenclature.py`, `check_reachability.py` :
**OK, code 0**, 88/88 à 100 %. AMBOSS (40) et RESCOS (41) aux trois verts.
Aucune section notée touchée : 0 ligne de diff sur `criteria-text`, `<input`,
`maxScores`, `patient-response` ; `maxScores` md5 identique à HEAD.
**0 lien d'image cassé** (5 références non-`data:` résolues + `naturalWidth > 0`).

**`report_redundancy.py German-1_` : 2 paires — inchangé, et c'est normal.**
L'attente était une baisse. Mesuré plutôt que supposé : les 11 items de la
checklist ont été comparés aux 134 autres items de la grille ; **le meilleur
ratio obtenu par l'un d'eux est 0,54**, pour un seuil à 0,72. Aucun n'était à
moins de 0,18 point. La checklist recouvrait bien les mêmes sujets que le reste —
c'était sa raison d'être — mais sous une forme télégraphique (« Examen →
imprégnation chronique, abdomen, bouche ») que `SequenceMatcher`, qui compare des
chaînes et non des sens, ne rapproche pas de la prose. Elle portait une
redondance **éditoriale** que la mesure du projet ne capte pas. Les 2 paires qui
restent sont celles de p1, déjà justifiées.

`check_no_loss.py HEAD` : 11 items disparus = exactement les 11 de la checklist.

#### Contrôle visuel — fait

Chrome headless, `file://`, aucune requête réseau. Deux copies temporaires de la
zone pédagogique à `data-theme` figé (`theme-sync.js` lit `localStorage`,
impraticable en headless), même chaîne d'ancêtres et mêmes feuilles de style ;
supprimées après coup.

Les deux images **se chargent réellement** (`naturalWidth` 1577×825 et 3178×1609).
Point de rupture conforme : **côte à côte à 1400, 1200 et 800 px ; empilées à
767, 600 et 500 px** — bascule entre 768 et 767. Les huit classes sortent dans
les deux thèmes, `c-yellow` en fond surligné et non en couleur de texte. Le titre
`section-commcards` s'affiche en sarcelle avec son filet clair.

#### Deux réserves

**Les fonds teintés de `theorie-section-rappels` (ambre) et
`theorie-section-examens` (vert) neutralisent partiellement `c-amber` et
`c-green` en thème sombre** : les molécules du premier bloc s'y lisent surtout
comme du gras. La sémantique a été privilégiée sur l'effet visuel — la couleur
dit *ce que la chose est*. Le cas se reproduira sur les 87 autres grilles, ces
deux variantes étant au gabarit ; arbitrage à rendre.

**En thème clair, `c-amber` (#9e6c00) sur le crème `#fffbf0` du
`resume-subsection` et le `#fafafa` de `presentation-reponse` reste le plus
faible du jeu** — lisible, mais juste. Consigne suivie : l'ambre a été retiré
partout où une autre classe convenait.

Rapport détaillé : `.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/p1b-report.md`

---

## p2 — German-1 : trois images, et la règle de sélection pour les 87 suivantes

Deux livrables de poids inégal. German-1 passe de une à trois images. Et surtout,
la **règle de sélection** est écrite au § 8 de `scripts/german/PROCEDURE-german.md` :
c'est elle qui gouvernera les 87 grilles restantes.

### L'ordre des trois images : AUDIT-C → sevrage → messages clés

La chronologie de la station, synthèse en dernier. L'AUDIT-C est ce que l'anamnèse
fait d'abord — quantifier. Le tableau du sevrage est la complication à reconnaître
si le patient s'arrête. Le panneau Compas synthétise les deux (il parle du sevrage
et de la carence en B1) : le lire en premier, c'est lire la conclusion avant
l'énoncé. C'est aussi l'ordre de la page SSP, qui place l'AUDIT-C dans `## ANAMNÈSE`,
le tableau dans `## Sevrage alcoolique & complications`, et les trois panneaux de
messages clés en fin de page. Et le message-clé est le plus large — 2040 px contre
~520 px pour les schémas : en tête il écrase la planche, en pied il la ferme.

L'image en place n'a pas été retirée, elle est passée en position 2, légende
reprise caractère pour caractère et base64 réutilisé tel quel — relu et comparé au
fichier du vault avant réécriture, md5 identique.

### La contrainte « `blocks` ne doit pas changer » reposait sur une hypothèse fausse

Ajouter des images dans un `images-wrapper` existant **n'est pas** neutre pour
`blocks`. `lib_german.BLOCKS` ouvre un segment `annexe-image` sur
`<div class="annexe-item"`, et la convention d'import du corpus est **une carte
par image** — German-68 en porte deux. Trois cartes auraient fait passer German-1
de 1 à 3 segments et obligé à re-snapshoter `baseline.json`.

D'où le gabarit retenu : **une seule `annexe-item` — une « planche » — portant les
trois triplets titre + légende + image**. `annexe-image` reste à 1 segment,
`check_invariants.py` sort OK, `baseline.json` n'est pas touché, et chaque image
garde malgré tout sa légende propre. Ce n'est pas un contournement de convenance :
sur 88 grilles, la convention d'import aurait neutralisé pendant toute la campagne
l'invariant qui protège les bornes de blocs — au moment exact où il sert le plus.

`data-image-id` n'a pas été posé : l'attribut déclenche `width: 49% !important`,
qui aurait écrasé le panneau de 2040 px dans ~380 px de colonne.

### La règle, en cinq points, tous mesurés sur les 53 pages SSP du corpus

**Source.** Rien hors des `![[…]]` de la page SSP. La question « et si la page n'en
cite aucune ? » ne se pose pas : **les 53 pages en citent toutes au moins trois**
(min 3, médiane 12, max 57). Tranché par la mesure, pas par une préférence.

**Volume.** Cible 3, plancher 2, plafond 4 — contre 57 images disponibles sur
« Céphalée », 47 sur « Douleur Thoracique », 36 sur « Dyspnée ».

**Critère.** Trois tests par ordre de préférence : barème (l'image documente un
critère noté de *cette* grille), différentiel (une hypothèse nommée dans *son*
`annexe-dd`), piège (le drapeau rouge que la vignette expose). Le test 2 est
mécanisable : les pages sous-titrent `### Arguments clés — <Diagnostic>`, il suffit
de croiser avec les diagnostics que `annexe-dd` nomme. Contrôle le plus utile :
25 des 53 pages portent plusieurs grilles, et deux grilles d'une même page ne
doivent pas porter la même sélection — message-clé excepté. Si elles convergent,
on a sélectionné sur le thème.

**Message-clé.** 49 fichiers dans le vault, **24 des 53 pages** en citent au moins
un, ce qui couvre **52 des 88 grilles**. Obligatoire dès que la page en cite un.
Et oui, une page peut en citer plusieurs — 19 en citent 1, 4 en citent 2, **1 en
cite 3** : celle de German-1. On prend alors celui dont le sujet est l'entité de la
vignette (alcool, pas tabagisme ni dépendances). Jamais deux. Aucun s'il n'y en a
aucun sur l'entité : un message-clé hors sujet affirme avec l'autorité du Compas
quelque chose que la station ne demande pas.

**Scans et PDF convertis.** 39 fichiers distincts, 41 occurrences. Écartés — c'est
une page d'un autre document, avec sa mise en page et ses titres, et elle redit en
image ce que `resume` porte en texte, sans que le dédoublonnage puisse la voir :
`list_items()` ne lit pas les pixels. Même forme d'angle mort qu'AMBOSS-34. Une
exception : quand la page de PDF **est** le schéma (algorithme pleine page). Ouvrir
l'image pour trancher, jamais le nom de fichier.

Relevé au passage : **36 des 700 fichiers cités n'existent nulle part dans le
vault**, essentiellement des `Résumé-SSP_page-00NN.jpg`.

### Poids : ~44 Mo, sous le plafond, mais borné par le plafond par image

Le base64 coûte exactement +33,3 %, vérifié : 60 465 octets dans le vault, 80 620
caractères dans la grille, md5 identique après décodage.

Les images citées ont une queue très lourde — médiane 110 Ko mais **p95 à 3 196 Ko
et max à 13 Mo**. Une règle sans plafond n'est pas bornée. D'où 400 Ko par image
(89 % des éligibles passent) et 700 Ko de source par grille.

À k=3 : **+35,8 Mo de base64, corpus german à 44,1 Mo** (8,3 aujourd'hui). k=2 donne
34,8 Mo, k=4 donne 55,8 Mo. Sans le plafond de 400 Ko, k=3 monte à 84 Mo : c'est le
plafond par image qui borne, pas le nombre d'images. Variante économe documentée et
non retenue faute de nécessité : servir les images en fichiers référencés sous
`cases/img/german/` comme les cartes SBAR/SNAPPS — 25,9 Mo au lieu de 44,1, parce
que 208 fichiers distincts suffisent aux 88 grilles.

German-1 : **212 621 → 839 389 octets**.

### Vérifications

Les trois vérificateurs german : **OK**, `blocks` inchangé, `baseline.json` non
touché. AMBOSS aux trois verts. RESCOS vert sur nomenclature et atteignabilité ;
`check_invariants` échoue sur **RESCOS-7 et RESCOS-9 uniquement**, les deux fichiers
que la session parallèle a en cours d'édition dans l'arbre de travail — hors
périmètre, non touchés, non commités, et hors de portée d'un changement de CSS.

`check_no_loss.py` : 0 item disparu. `report_redundancy.py` : 2 paires, inchangé.

### Contrôle visuel — fait, et un défaut corrigé

Chrome headless, `file://`, copies temporaires à `data-theme` figé, supprimées après
coup. **Aucune image corrompue** : les trois `naturalWidth × naturalHeight` lus au
navigateur sont ceux du vault — 519×639, 520×368, 2040×1455, `complete === true`,
rapport conservé. **Aucun débordement** : `scrollWidth` égale la fenêtre à 1200 px
comme à 500 px. Les deux schémas restent à leur taille native (jamais agrandis, donc
jamais flous) ; le panneau descend à 1046 px sur grand écran.

**Défaut trouvé : en thème sombre, `.annexe-title` était à 1,8:1 de contraste** —
#2c5aa0 sur le #273449 de la carte, sous le seuil AA même pour du gros texte.
Préexistant (la seule légende de German-1 le portait déjà, et 9 autres grilles avec
elle), mais la campagne le multiplie par 88. Corrigé par une règle restreinte à
`.images-wrapper`, avec le #93c5fd que `mobile-responsive.css` emploie déjà en
sombre : **7,0:1**. Vérifié qu'aucune variante `annexe-expert` / `annexe-theorie` /
`annexe-scenario` ne vit dans un `images-wrapper` sur les six corpus. Seconde règle,
un filet entre deux légendes de la planche : sans elle, 10 px seulement séparaient
une image du titre de la suivante.

### Trois préoccupations

**Le poids par grille est le vrai sujet, pas le poids du corpus.** 839 Ko pour un
seul document HTML, sur réseau mobile, c'est plusieurs secondes d'ouverture contre
quelques dixièmes. La variante référencée règle ce point ; elle mérite d'être
retranchée avant la 20ᵉ grille plutôt qu'après la 88ᵉ.

**`.git` pèse 435 Mo et le base64 se delta-compresse mal.** Chaque passe d'édition
sur une grille chargée d'images restocke le blob entier. Consigne inscrite : poser
les images en dernier, une fois le texte stabilisé. `git gc` est interdit.

**Le § 8.3 demande un jugement que les scripts ne vérifient pas.** Le seul
garde-fou automatisable est le corollaire des pages multi-grilles, et il n'est pas
outillé. C'est là que la règle cédera en premier si elle cède.

Rapport détaillé : `.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/p2-report.md`

---

## 2026-08-02 — Bascule des images en fichiers référencés (German-1) et outillage des 87 suivantes

### Ce qui a été fait

German-1 passait 839 Ko avec ses trois images en base64, et le corpus complet
visait ~44 Mo. L'utilisateur a tranché pour la **variante référencée** chiffrée
au § 8.6. German-1 est converti, l'infrastructure est posée pour les 87 grilles
restantes.

Les trois images sont copiées du vault vers `cases/img/german/` et citées en
`../img/german/<nom>`. **La planche reste une `annexe-item` unique** : c'est la
structure qui gèle `blocks` à un seul segment `annexe-image` et protège
`baseline.json` sur les 88 grilles. Seuls les trois attributs `src` ont changé —
le diff structurel, base64 masqué, fait **exactement trois lignes**. Titres,
légendes, `alt` et ordre (AUDIT-C → sevrage → messages clés) sont intacts.

**839 389 o → 135 350 o, soit −83,9 %.** Les trois fichiers pèsent 516 Ko dans
`cases/img/german/`, mutualisables entre grilles.

### La convention de nommage : le nom du vault, normalisé ASCII-minuscules-tirets

Ni préfixe, ni renommage de fond. Deux mesures sur les 664 images citées par les
53 pages german :

- **Zéro homonyme**, y compris entre `Skills ECOS/img/` et les 75 fichiers venus
  de `_bibliotheque/`. Un préfixe de dossier n'écarterait donc aucun risque réel,
  alors qu'il allongerait des noms déjà à 119 caractères — et les noms du vault
  portent **déjà** leur thème (`general-`, `abdo-`, `neuro-`…).
- **La normalisation est l'identité pour 573 d'entre elles (86 %)** et ne produit
  **aucune collision**. Elle ne touche que les 91 noms hérités de
  `_bibliotheque/`.

Elle règle deux pannes concrètes, pas une préférence esthétique : un espace ou un
accent dans un `src=` impose le percent-encoding, illisible à l'édition manuelle ;
et **7 fichiers sont stockés en NFD par macOS quand la page SSP les cite en NFC** —
même chaîne à l'œil, octets différents. `cases/img/german/MANIFEST.tsv` garde le
lien nom livré ↔ nom d'origine, avec sha256 et dimensions.

### L'outil de reprise : `scripts/german/fetch_image.py`

Prend `![[general-score-audit-c.png]]`, résout dans le vault, contrôle, copie,
rend le chemin à coller. **Idempotent** au sha256 : une image déjà reprise n'est
pas réécrite, donc aucun blob git nouveau. `--check` diagnostique à blanc,
`--verify` vérifie les `src` des 88 grilles et signale les orphelines.

Il s'arrête en code 1 plutôt que de livrer du faux : référence cassée, fichier
vide ou tronqué (contrôle des signatures et des marqueurs de fin PNG/JPEG),
homonyme ambigu, collision de nom. Il **avertit** sans bloquer sur un appariement
non exact et sur un dépassement du plafond de 400 Ko.

Deux pièges rencontrés en l'écrivant, et traités :

- **`.backup_transparents`** est une copie de sauvegarde de `Skills ECOS/img/`.
  Sans l'exclure de la résolution, **46 des 664 images citées deviendraient
  ambiguës** alors qu'aucune ne l'est.
- Le premier jet copiait `dermato-resume.jpg`, **2,3 Mo**, sur un simple test de
  référence cassée. D'où l'avertissement de plafond, et le retrait immédiat.

### Ce que la vérification a appris : les « 36 références cassées » sont 29

Le § 8.5 b relève 36 références introuvables sur 700. En résolvant avec
réconciliation NFD/NFC, il en reste **29 vraiment introuvables** ; les **7 autres
existent** et n'étaient manquées que sur la normalisation Unicode
(`Dermato-Résumé.jpg`, `Kératites.jpg`, `Ped-Eruptions cutanées.jpg`,
`Dermato-Impétigo.png`, `Dermato-Descritpion des lésions I.jpg`,
`EM - Résumé-2024_page-0002.jpg`,
`EM - ECOS fédéral - entretien motivationnel_page-0001.jpg`).

Et **28 des 29 vraiment cassées sont des `Résumé-SSP_page-00NN.jpg`**, que le
§ 8.5 a écarte déjà comme scans de PDF. Il ne reste donc **qu'une seule référence
cassée réellement gênante**, `G5rt9XF8OyqqQlfo__MHeJgVB2TIA7ruI.png`.

Le § 8.5 n'a **pas** été modifié — l'utilisateur l'a explicitement gelé. Le
chiffre de 36 y reste ; il est à corriger par qui rouvrira la règle de sélection.

### Contrôle visuel

Chrome headless, sonde injectée dans une copie temporaire placée dans
`cases/german/` puis supprimée, quatre combinaisons (clair/sombre × 1200/500 px).
Les trois images rendent **au pixel près** ce qu'elles rendaient en base64 :
naturalWidth/Height 519×639, 520×368, 2040×1455, `complete === true`, ratios
conservés, `scrollWidth === innerWidth` — aucun débordement. Le correctif de
contraste tient : `.annexe-title` passe de `rgb(44,90,160)` en clair à
`rgb(147,197,253)` en sombre.

### Préoccupations

**Neuf autres grilles portent encore 1,0 Mo de base64** (German-36, 42, 43, 44,
57, 61, 68, 75, 78 — 10 images), héritage de l'import. Elles ne sont pas dans le
périmètre de cette tâche, mais elles sont désormais la seule source de base64 du
corpus et `fetch_image.py` les convertirait sans peine. German-68 porte deux
`annexe-item` : sa conversion demandera l'attention du § 8.7.

**Le plafond de 400 Ko a changé de raison d'être sans changer de valeur.** Il
bornait le poids d'un HTML ; il borne maintenant un stock partagé, où une image
lourde citée par huit grilles ne coûte qu'une fois. La valeur mérite d'être
rediscutée quand la règle de sélection sera rouverte — elle écarte aujourd'hui
11 % des images éligibles pour une raison qui a perdu de sa force.

**L'estimation du corpus dépend fortement du biais de sélection** : à 220 images
distinctes, de 22,3 Mo (biais bas) à 49,9 Mo (biais haut), 29,1 Mo en sélection
neutre. La cible de 25,9 Mo tombe dans la fourchette mais n'est pas un plancher.

Rapport détaillé : `.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/p2b-report.md`

---

## p3a — Les 13 grilles riches : `annexe-theorie`, planche d'images, balisage

**Périmètre** : German-15, 19, 22, 27, 34, 42, 43, 44, 48, 56, 69, 72, 88 — les
13 grilles qui portaient déjà `resume`, `annexe-dd` et `presentation` sans
`annexe-theorie` ni image. Rien d'autre.

**HEAD réel au démarrage** : `fde7e04` (« Bascule les images de German-1 en
fichiers référencés »), et non `383ade6` — la session RESCOS avait commité deux
fois entre-temps. Vérifié par `git log`, pas supposé. Au moment du commit,
l'arbre de travail portait 198 fichiers `cases/casecos/` et 5 `scripts/casecos/`
modifiés par l'autre session : l'index a été construit chemin par chemin.

### 1. Ce qui a été ajouté

| | 13/13 |
|---|---|
| `annexe-theorie` créé | 13 |
| Planches d'images | 13 (34 images distinctes, 2 à 3 par grille) |
| `resume` balisé | 13 |
| `presentation` balisé (`section-mnemo` + `section-questions`) | 13 |
| Section notée touchée | **0** |

`blocks` gagne `annexe-theorie: 1` sur les 13, et `annexe-image: 1` sur 10 —
German-42, 43 et 44 en portaient déjà un, et leurs triplets ont été **ajoutés
dans l'`annexe-item` existant** pour que le compte de segments reste à 1 (§ 8.7).

### 2. La source de chaque section, grille par grille

Chaque `annexe-theorie` est bâtie sur la page SSP de la grille (niveau 1) et sur
sa section notée (niveau 2), et sur rien d'autre. Le tableau donne, pour chaque
grille, sa page de référence et ce que chaque section tire d'où.

| Grille | Diagnostic retenu | Page SSP | Sections et leur source |
|---|---|---|---|
| **German-15** | Diverticulite sigmoïdienne non compliquée | Douleur Abdominale | *Ce qui pose le diagnostic* ← tableau « Orientation par localisation » (FIG = sigmoïde) + détails notés · *Scanner et coloscopie* ← « Imagerie » + résumé · *Classification* ← image Hinchey/Kaiser + « Scores cliniques utiles » · *Ambulatoire* ← algorithme diverticulite + « Conduites ciblées » (abstention SSMI/SGAIM) · *DD* ← « Catégorisation par urgence » + Fireflies (ischémie mésentérique) · *Seuils* ← algorithme |
| **German-19** | Rectocolite ulcéro-hémorragique | Douleur Abdominale | *Durée* ← critères notés 3 et 7 · *Voyage* ← AMPLE items « P » et « E » de la page · *Examens* ← « Biologie 1ʳᵉ intention » + corrigé du critère 3 · *DD* ← bloc Fireflies « Maladie de Crohn (RCI Jenelten) » + score d'Alvarado · *Conduite* ← résumé + `annexe-dd` |
| **German-22** | Épicondylite latérale | Douleurs Articulaires | *Cinq critères* ← tableau « Inflammatoire vs Mécanique » de la page, appliqué détail par détail au corrigé · *Anatomie* ← test noté « épicondyle latéral avec extension du poignet contre résistance » + tendon nommé au résumé · *Médicaments* ← « fluoroquinolones (tendinopathies) » de la page + détail noté (pilule) · *Piège* ← « à faire » n° 2 et « à éviter » n° 1 de la page (ponction avant infiltration) |
| **German-27** | Conflit sous-acromial | Douleur d'Épaule | *Actif/passif* ← « Mobilités » de la page (deux règles citées telles quelles) · *Un test par muscle* ← tableau « Tests spécifiques » · *Trois stades* ← image « Impingement — stades » · *DD* ← « Points Clés ECOS » (capsulite, Spurling, diabète) · *Causes viscérales* ← même bloc + message-clé |
| **German-34** | Cancer de l'œsophage | Dysphagie | *Deux questions* ← « En Bref » et mnémoniques de la page · *Mécanisme solides→liquides* ← carte ECOS de la page, verbatim du raisonnement · *IPP d'épreuve* ← piège n° 1 · *Ordre OGD/manométrie* ← « à faire » n° 5 (pseudo-achalasie) · *Dysphonie* ← « ORL et cervical » (nerf récurrent) + facteurs de risque · *DD* ← tableau oropharyngée/œsophagienne |
| **German-42** | Tinea corporis | Éruption Cutanée | *Décrire avant de nommer* ← règle d'or de la page + détails notés · *Grattage* ← « Examens complémentaires » + critère noté 4 (filaments mycéliens) · *Dermocorticoïde* ← « Prise en charge » (eczéma/psoriasis) + résumé (Majocchi) · *DD* ← `annexe-dd` + « Pièges » (gale) · *Piscine* ← critère noté 8 + résumé |
| **German-43** | Scarlatine | Éruption Cutanée | *Vitropression* ← règle d'or et red flags de la page (purpura fulminans, ceftriaxone) + critère noté 5 · *Texture* ← détails notés (papier de verre, langue framboise) + résumé · *Pourquoi traiter* ← résumé (RAA, GNA) + corrigé (éviction 24 h, pas de prophylaxie) · *TDR* ← corrigé du critère 3 · *DD* ← `annexe-dd` + red flags |
| **German-44** | Lupus érythémateux cutané | Éruption Cutanée | *Lésion élémentaire* ← « Description de la lésion » de la page + détails notés · *Photosensibilité* ← « Facteurs déclenchants » + détails notés (Italie, aggravation) · *Cutané ou systémique* ← résumé (ANA, anti-SSA, lupus band test) + critère noté 6 · *DD* ← `annexe-dd` + résumé · *Photoprotection* ← résumé |
| **German-48** | Exanthème subit (HHV-6/7) | Fièvre du Nourrisson | *Âge* ← « En Bref » (< 1 mois / 1-3 mois / > 3 mois) · *Examen sans foyer* ← pièges de la page (otoscopie, stix urinaire, 15 %, 85 %) + red flags · *Convulsions* ← mnémoniques de la page + `redflags` de la grille · *DD* ← `annexe-dd` + tableau DD de la page |
| **German-56** | Incontinence urinaire d'effort | Incontinence Urinaire | *Quatre types* ← tableau « Types d'incontinence » de la page · *Urgenturie sans fuite* ← détails notés (toilettes à temps, 8 mictions, pas de nycturie) · *Examens* ← « 1ʳᵉ / 2ᵉ intention » de la page · *Rééducation* ← « Mesures conservatrices » + critère noté 19 (internet) · *Terrain* ← « Facteurs de risque » de la page + critères notés 21-27 · *Interdits* ← « à éviter » de la page (queue de cheval, « c'est l'âge ») |
| **German-69** | Cataracte sénile nucléaire | Amaurose & BAV | *Quatre axes* ← « Caractérisation (les 4 axes) » de la page · *Opacité* ← détails notés + résumé (second sight) · *Examens négatifs* ← « à faire » et « pièges » de la page (DPAR, fond d'œil) · *Après 50 ans* ← règle d'or (Horton, corticoïdes avant biopsie) + critère noté 6 · *DD* ← `annexe-dd` + tableau « Délai / Diagnostic / Clés » |
| **German-72** | Maladie cœliaque | Troubles de la Croissance | *Courbe* ← règle d'or de la page + critères notés 2 et 3 · *Deux calculs* ← piège n° 1 (80 %, taille cible, âge osseux et ses trois lectures) · *Cassure sans symptôme* ← red flag « douleurs abdo + diarrhée + petite taille » + résumé (manifestations extra-digestives) · *Examens* ← « Bilan de base (toujours) » · *DD* ← `annexe-dd` + red flags (tumeur, maltraitance, Turner) |
| **German-88** | Conjonctivite allergique | Œil Rouge | *Acuité d'abord* ← règle d'or et « En Bref » de la page · *Tableau des conjonctivites* ← tableau DD de la page · *Deux gestes* ← « à faire » n° 2 et 4, « pièges » n° 5 · *Lentilles* ← red flag « porteur de lentilles » + message-clé · *Corticoïdes* ← règle d'or, pièges et encadré de la page · *DD* ← `annexe-dd` + red flags (Chlamydia, PCR avant traitement) |

**Où la source était muette, la section est courte ou absente.** German-19 n'a
pas de section « repères chiffrés » développée : la page « Douleur Abdominale »
ne porte aucun seuil de RCUH. German-22 n'a pas de section sur la conduite
thérapeutique : la page « Douleurs Articulaires » ne traite que des
arthropathies, jamais des tendinopathies. Rien n'a été comblé.

### 3. Les images — motif de chaque choix

34 images distinctes, **4 892 Ko**, toutes reprises par `fetch_image.py`, aucune
recompressée. Aucune n'est citée par deux de mes grilles : la déduplication n'a
donc rien économisé ici, mais elle jouera à mesure que le corpus se remplira.

| Grille | Image | Test § 8.3 | Motif |
|---|---|---|---|
| **15** | classification diverticulite compliquée | 1 | Le critère noté 5 s'intitule « Classification de la diverticulite » |
| | algorithme diverticulite aiguë | 1 | Le critère noté 6 « Prise en charge » ; l'image porte les quatre conditions de l'ambulatoire |
| | messages clés — douleurs aiguës | 8.4 | Message-clé obligatoire ; ses deux premiers points portent sur la diverticulite, l'entité de la vignette |
| **19** | DD par quadrant | 1+2 | Le critère noté 4 est « Localisation » ; l'image range les hypothèses de l'`annexe-dd` par siège |
| | signe de l'obturateur | 1+2 | Critère noté 4 de l'examen (« Signes péritonéaux ») ; manœuvre de l'appendicite pelvienne, hypothèse de l'`annexe-dd` |
| | score d'Alvarado | 2 | Cote l'appendicite, nommée à l'`annexe-dd` |
| **22** | Rx mains — érosions ou nodosités | 2 | La page donne à cette image deux lectures, PR et arthrose : les deux hypothèses de l'`annexe-dd` |
| | ponction articulaire | 3 | Le piège n° 1 de la page et le premier « piège ECOS » de la grille (arthrite septique) ; l'infiltration est la 2ᵉ ligne du traitement |
| **27** | quel test de la coiffe pour quel muscle | 1 | Le critère noté 4 s'intitule « Tests spécifiques de la coiffe des rotateurs » |
| | conflit sous-acromial — stades | 1 | Le diagnostic retenu ; l'image stadifie l'entité que le critère noté 1 nomme |
| | messages clés — épaule douloureuse | 8.4 | Message-clé obligatoire, sur l'entité de la vignette |
| **34** | trois phases de la déglutition | 1 | Le critère noté 2 de l'examen est « Examen de la déglutition » ; le découpage fonde la distinction oropharyngée / œsophagienne |
| | cancer de l'œsophage — trognon de pomme | 1 | Le diagnostic retenu (critère noté 1) |
| | achalasie — bec d'oiseau | 2 | Hypothèse discutée de l'`annexe-dd`, avec le signe qui la sépare du cancer |
| **42** | la squame | 1 | Le détail noté « Aspect (squameux…) [Desquamation] » |
| | psoriasis en plaques du genou | 2 | Première hypothèse de l'`annexe-dd`, avec la squame pleine qui l'oppose à la bordure active |
| **43** | éruption maculopapuleuse du nourrisson | 2 | Rougeole et roséole, la rougeole étant la première hypothèse de l'`annexe-dd` |
| | purpura fébrile — méningococcémie | 3 | Le critère noté 5 (« Recherche de signes de gravité ») et la règle d'or de la page |
| **44** | la plaque | 1 | Le critère noté 3 (« Caractéristiques de l'érythème ») et le détail « Aspect » |
| | pitting unguéal du psoriasis | 2 | Hypothèse n° 1 de l'`annexe-dd` ; signe à chercher hors de la lésion, comme la page l'exige |
| **48** | otoscopie — tympan normal | 1+3 | Le critère noté 3 (« Examen ORL ») et le piège de la page (« oublier l'otoscopie ») |
| | exanthèmes fébriles du nourrisson | 1+2 | Le diagnostic retenu (roséole HHV-6) et le champ du différentiel |
| | convulsions fébriles simples/complexes | 3 | Red flag n° 2 de la grille, détail noté (« jamais eu de convulsions fébriles »), piège n° 4 de la page |
| **56** | classification de l'incontinence | 1 | Le critère noté 4 (« Circonstances déclenchantes ») : l'image est la question de tri elle-même |
| | types d'incontinence | 2 | Le critère noté 2 du management (« Diagnostics différentiels ») ; l'image détaille les quatre mécanismes de l'`annexe-dd` |
| | messages clés — incontinence urinaire | 8.4 | Message-clé obligatoire, sur l'entité de la vignette |
| **69** | mesure de l'acuité visuelle | 1 | Le critère noté 1 de l'examen ; « à faire absolument » n° 2 de la page |
| | fond d'œil normal | 1 | Le critère noté 7 ; c'est le repère auquel la cataracte est comparée, et le piège n° 5 de la page |
| | algorithme de Horton | 2+3 | L'urgence nommée à l'`annexe-dd` et le critère noté 6 (claudication de la mâchoire, douleurs temporales) |
| **72** | âge osseux (Greulich-Pyle) | 1 | Le critère noté 3 du management ; l'un des deux calculs que le piège n° 1 de la page impose |
| | hypothyroïdie — manifestations | 2 | Hypothèse de l'`annexe-dd`, dont le contre-argument est « aucun signe clinique d'hypothyroïdie » — l'image les liste |
| **88** | démarche diagnostique — œil rouge | 1+2 | Le critère noté 2 (« Diagnostics différentiels ») ; l'arbre porte les délais de recours |
| | test à la fluorescéine | 1 | Le critère noté 7 de l'examen ; « à faire absolument » n° 4 de la page |
| | messages clés — œil rouge | 8.4 | Message-clé obligatoire, sur l'entité de la vignette |

**Corollaire du § 8.3 vérifié.** Trois de mes grilles partagent la page
« Éruption Cutanée » (42, 43, 44) et deux la page « Douleur Abdominale »
(15, 19) : **aucune image n'est commune à deux d'entre elles**, message-clé
compris — les deux messages-clés de « Douleur Abdominale » sont distincts et
German-19 n'en prend aucun (voir plus bas).

### 4. Le balisage

Posé dans les quatre conteneurs prescrits, et **nulle part ailleurs** : sur les
2 246 `<span class="c-*">` des 13 grilles, 2 246 sont dans un de ces conteneurs,
0 en dehors.

| | spans | mots | densité |
|---|---|---|---|
| Total des 13 grilles | **2 246** | 22 395 | **1 / 10,0 mots** |
| Grille la plus dense | German-15 et 44 | | 1 / 9,1 |
| Grille la plus légère | German-88 | | 1 / 11,0 |

Répartition : `c-green` 507 · `c-pink` 459 · `c-red` 355 · `c-amber` 289 ·
`c-yellow` 228 · `c-purple` 170 · `c-blue` 146 · `c-orange` 92.

La cible était l'ordre de grandeur de German-1 (1 / 9,1), lui-même calibré sur
les pages SSP de l'utilisateur (1 / 11,3 en moyenne, 1 / 7,6 dans leur région la
plus dense). **1 / 10,0 tombe entre les deux.** Chaque `resume` a été ramené
après une première rédaction trop dense : les termes retirés sont des
répétitions internes (une check-list qui reprend une section antérieure) et des
intitulés de rubrique, jamais des noms porteurs d'information.

**Aucune dérive de formulation.** Le texte visible de `resume`, `presentation`,
`annexe-dd`, `redflags` et `therapy` est **identique caractère pour caractère**
à celui de `fde7e04` sur les 13 grilles (contrôle automatique par
`visible_text` + `norm`). Une première passe avait introduit 38 micro-réécritures
— abréviations développées, articles ajoutés — toutes annulées.

### 5. Vérifications

| Contrôle | Résultat |
|---|---|
| `check_invariants.py` avant re-snapshot | 13 écarts, **tous sur `blocks`, tous sur mes 13 grilles** |
| Diff champ par champ contre `baseline.json` | `blocks` est **le seul champ** qui bouge ; 0 écart hors périmètre ; aucun bloc retiré, aucun compte de segment modifié |
| `check_invariants.py` après re-snapshot | **OK — 88 grilles** |
| `check_reachability.py` | **OK — 88/88 à 100 %** |
| `check_nomenclature.py` | **OK** |
| AMBOSS — invariants, reachability, nomenclature | **OK — 40 grilles** |
| RESCOS — invariants, reachability, nomenclature | **OK — 41 grilles** |
| `check_no_loss.py HEAD` | **0 item disparu** sur les 13 |
| `fetch_image.py --verify` | **aucun lien cassé, aucune orpheline** ; 37 images, 37 référencées |

### 6. La redondance ne bouge pas d'une paire

| Grille | 15 | 19 | 22 | 27 | 34 | 42 | 43 | 44 | 48 | 56 | 69 | 72 | 88 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Avant | 1 | 2 | 0 | 3 | 1 | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 1 |
| Après | 1 | 2 | 0 | 3 | 1 | 0 | 0 | 2 | 0 | 1 | 0 | 1 | 1 |

**Zéro paire nouvelle.** L'attente de la consigne était plus faible — « des
paires vont apparaître, chacune doit être justifiable par un changement de
format ». Il n'y en a aucune à justifier, et ce n'est pas un hasard de mesure :
la rédaction a été corrigée cinq fois sur signalement du détecteur.

| Grille | Paire apparue à la première rédaction | Correction |
|---|---|---|
| German-27 | `annexe-theorie` ↔ `presentation` et ↔ `resume` à 0,83-0,74 sur « arc douloureux 60-120° » | Ligne retirée des « repères chiffrés » : le `resume` la porte déjà, dans le même format de liste |
| German-42 | `resume` ↔ `annexe-theorie` à 0,84 sur « retour au sport après 72 h » | Remplacée par le délai exposition→lésions, que le `resume` ne porte pas |
| German-56 | `annexe-dd` ↔ `annexe-theorie` à **0,89** sur « elle arrive toujours aux toilettes à temps » | Reformulée en énoncé de mécanisme (« c'est l'échec à différer qui définit le type ») ; le *quoi* reste à l'`annexe-dd`, le *pourquoi* passe à `annexe-theorie` |
| German-69 | `resume` ↔ `annexe-theorie` à 0,75 sur « correction optique à 4-12 semaines » | Ligne remplacée par le terrain de la vignette |
| German-72 | `resume` ↔ `annexe-theorie` à 0,85 sur la réintroduction des laitages | Ligne remplacée par le rythme de suivi |
| German-88 | `annexe-dd` ↔ `annexe-theorie` à **0,88** sur « ni douleur, ni photophobie, ni baisse d'acuité » | Reformulée sans reprendre l'énumération de l'`annexe-dd` |

Deux de ces six paires sont les plus instructives : **German-56 et German-88 ont
recouvert `annexe-dd`**, exactement le risque que la consigne annonçait. Le
détecteur les a vues à 0,89 et 0,88.

### 7. Contrôle visuel — fait, en navigateur headless

Chrome (`--headless=new`), rendu local sur `file://`, aucune requête réseau.
Deux grilles — **German-15** (3 images référencées) et **German-44** (base64
hérité + 2 référencées) —, deux thèmes, deux largeurs, soit **8 rendus**. Copies
temporaires avec `data-theme` figé placées dans `cases/german/` pour que
`../img/german/` résolve, supprimées ensuite (`git status` ne montre aucun
`_tmpvis-*`).

```
German-15 sombre 1200 : IMG0 nat=521x291  rendu=523x293   IMAGES_CASSEES=0
                        IMG1 nat=1156x827 rendu=1046x749  SCROLLWIDTH=1200 DEBORDEMENT=non
                        IMG2 nat=2190x1080 rendu=1046x517  NEUTRALISES=0
German-15 clair   500 : IMG0 rendu=402x225  IMG1 402x288  IMG2 402x199  DEBORDEMENT=non
German-44 sombre 1200 : IMG0 (base64) nat=420x224  IMG1 nat=1964x1422 rendu=1046x758
                        IMG2 nat=797x1000 rendu=799x1002  IMAGES_CASSEES=0  NEUTRALISES=0
```

- **`naturalWidth`/`naturalHeight` égaux aux dimensions du vault** pour les six
  images référencées — aucun fichier tronqué, aucun chemin faux.
- **Rapports conservés** : 1156/827 = 1,398 rendu 1046/749 = 1,397 ;
  2190/1080 = 2,028 rendu 1046/517 = 2,023 ; 797/1000 = 0,797 rendu
  402/504 = 0,798.
- **Aucun débordement horizontal** : `scrollWidth === innerWidth` aux quatre
  couples (1200 et 500 px, sombre et clair).
- **Les huit classes rendent une couleur distincte dans les deux thèmes**, et
  `NEUTRALISES=0` — aucun span dont la couleur calculée égale celle de son
  parent, donc aucune classe silencieusement écrasée. `c-yellow` rend bien un
  fond (`rgba(245,200,66,0.18)` en sombre, `0.22` en clair) et non une couleur
  de texte.

### 8. Préoccupations

**a) Le plafond de 400 Ko a écarté cinq images que la règle de sélection
retenait**, dont deux que je considère comme des pertes réelles :

| Image | Poids | Grille | Ce qu'elle documentait |
|---|---|---|---|
| `pedia-courbe-de-croissance-...-cassure.png` | **443 Ko** | German-72 | Le critère noté 3 dit « Voir courbe de croissance, P3 » : c'est l'image que la grille **désigne** |
| `derma-message-cle-infections-cutanees.png` | **460 Ko** | German-42 | Message-clé, obligatoire au § 8.4 — la règle de poids et la règle du message-clé se contredisent ici |
| `derma-psoriasis-capitis.jpg` | 548 Ko | German-44 | Le cuir chevelu, localisation que l'`annexe-dd` nomme explicitement |
| `Ped-Eruptions cutanées.jpg` | 2 261 Ko | German-43 | Les huit exanthèmes pédiatriques comparés — le différentiel entier sur une planche |
| `dermato-lesions-maculeuses.png` | 838 Ko | German-42/44 | Les lésions élémentaires maculeuses |

Les trois dernières sont défendables : 548 Ko à 2,2 Mo pour une image, c'est le
poids que le garde-fou vise. Les deux premières le sont moins : **443 et 460 Ko,
soit 11 et 15 % au-dessus d'un seuil qui borne aujourd'hui un stock partagé et
non un fichier HTML** — c'est la préoccupation déjà consignée en p2b, et elle a
maintenant un coût mesurable. German-72 se retrouve à deux images sans celle que
sa propre grille désigne ; German-42 est la seule de mes grilles à perdre son
message-clé pour une raison de poids.

**b) German-19 n'a pas de message-clé, et c'est une application du § 8.4 rule 3.**
La page « Douleur Abdominale » en cite deux — « douleurs aiguës » et « douleur
chronique ». Le premier porte sur la diverticulite et l'appendicite, le second
sur le syndrome de l'intestin irritable et la douleur fonctionnelle. **Aucun ne
porte sur la rectocolite ulcéro-hémorragique**, l'entité de cette vignette. Le
second est même activement trompeur ici : il énonce qu'en l'absence de drapeaux
rouges, chez un patient de moins de 50 ans, aucun examen n'est nécessaire — or
ce patient a 21 ans **et** des drapeaux rouges. J'ai appliqué la règle
(« n'en mettre aucun et le consigner ») plutôt que de faire dire au Compas
quelque chose que la station ne demande pas.

**c) Trois fichiers du vault sont inutilisables et l'outil les a arrêtés.**
`fetch_image.py` a refusé `pedia-fievre-sans-foyer-2mois-2ans-algorithme.jpg` et
`ped-algorithme-diagnostique-petite-taille-enfant.jpg` pour en-tête JPEG
incohérent (`ÉCHEC [corrompu]`). Ce sont deux algorithmes que le § 8.3 retenait
sans discussion — l'un couvre exactement la vignette de German-48 (fièvre sans
foyer, 2 mois-2 ans), l'autre exactement celle de German-72 (petite taille
< −2,5 DS). **À réparer dans le vault**, pas ici.

**d) Un fichier du vault ne contient pas ce que son nom annonce.**
`nephro-bilan-urodynamique-cystomanometrie-trace-courbe.jpg`, cité par la page
« Incontinence Urinaire » comme un tracé de cystomanométrie, **est une
photographie d'avions sur un tarmac d'aéroport**. Écarté après ouverture — c'est
précisément ce que le § 8.5 a demande de faire (« ouvrir l'image pour trancher,
ne pas trancher sur le nom de fichier »). Signalé, non corrigé : le vault n'est
pas modifié.

**e) Une image écartée pour une raison qui n'est pas dans la règle.**
`general-syndrome-de-turner-stigmates-cliniques.jpg` (113 Ko, sous le plafond)
passait le test 3 pour German-72 — la page en fait un red flag et impose le
caryotype chez toute fille de petite taille. C'est **un montage de quinze
portraits de patientes mineures, face et profil, sans aucune annotation** : la
légende n'aurait pu décrire que « quinze paires de photographies », et la page
dit elle-même que les stigmates peuvent être discrets. Je l'ai écartée au titre
du § 8.5 d (photographies cliniques) et de l'identifiabilité des sujets.
**C'est un arbitrage que je n'étais pas mandaté pour prendre seul.**

**f) Deux pages SSP sont pauvres pour la vignette qu'elles desservent.**
« Douleur Abdominale » ne porte **aucune iconographie de rectocolite ou de MICI**
et deux lignes de texte sur le sujet (bloc Fireflies « Maladie de Crohn ») :
German-19 a donc trois images qui documentent la localisation, la manœuvre notée
et le score d'Alvarado, aucune la maladie retenue, et son `annexe-theorie` n'a
pas de section de repères chiffrés propres. « Douleurs Articulaires » ne traite
que des arthropathies : **rien sur l'épicondylite**, ni image, ni texte, ni
message-clé — German-22 est à deux images, et son `annexe-theorie` tire
l'essentiel du tableau « Inflammatoire vs Mécanique », qui est heureusement le
bon outil pour cette vignette.

**g) Les grilles German-42, 43 et 44 restent en base64 pour leur première
image.** Elles portaient déjà une photographie clinique embarquée, à laquelle un
critère noté renvoie explicitement (« Voir image en annexe »). Mes triplets ont
été ajoutés **dans le même `annexe-item`** pour ne pas faire varier `blocks`, et
la photographie a été conservée telle quelle — la retirer aurait cassé la
référence d'un critère noté. Leur conversion en fichier référencé reste au
programme des neuf grilles base64 déjà signalées en p2b.

**h) L'observation de p1b sur les fonds teintés se confirme.**
`.theorie-section-rappels` (fond ambré) et `.theorie-section-examens` (fond
verdâtre) atténuent en thème sombre les `c-amber` et les `c-green` qu'elles
contiennent. La sonde le mesure autrement : `NEUTRALISES=0`, donc la couleur
n'est jamais *écrasée* — elle est seulement moins contrastée. Treize grilles de
plus emploient ces deux variantes ; l'arbitrage reste ouvert.

Rapport détaillé : `.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/p3a-report.md`

## p3a-fix — Révision du plafond § 8.5, deux images posées

**Périmètre** : `scripts/german/PROCEDURE-german.md` § 8, `scripts/german/fetch_image.py`
(constante et messages, en lockstep avec la procédure), German-72 et German-42,
`cases/img/german/` (2 images + manifeste), le journal et le rapport. Rien
d'autre.

**HEAD réel au démarrage** : `4083025` (« Complète les 13 grilles riches german »,
commit de p3a). Vérifié par `git log`, pas supposé. L'arbre de travail portait
**≈370 fichiers `cases/casecos/`** modifiés par la session RESCOS/CasECOS en
cours : aucun n'entre dans ce commit, index construit chemin par chemin.

### 1. Ce qui a motivé la révision

p3a (concern a) avait mesuré que le plafond de 400 Ko — hérité de l'époque
base64, où il bornait le poids d'un fichier HTML — écartait cinq images que la
règle de sélection retenait, dont deux pertes réelles : le message-clé
obligatoire de German-42 (§ 8.4) et l'image que le corrigé de German-72
désigne littéralement. Le plafond n'avait plus de justification propre depuis
le passage aux fichiers référencés (§ 8.6, 2026-08-02) : il ne borne plus qu'un
stock partagé, et sa valeur n'avait pas été revue en même temps que sa raison
d'être.

### 2. Révision de `PROCEDURE-german.md` § 8

- **§ 8.5 d (ex-c)** : plafond porté à **600 Ko**, et **deux exemptions sans
  limite de taille** ajoutées — le message-clé que le § 8.4 rend obligatoire,
  et l'image désignée nommément par un critère noté de la grille. Les deux sont
  sourcées par la grille elle-même, pas par une préférence éditoriale.
- **§ 8.5 b (nouveau)**, placé à côté de l'exclusion des scans PDF : **aucune
  photographie identifiante de patient, a fortiori mineur**, même citée par la
  page SSP et même si le critère de pertinence du § 8.3 est rempli. Motif
  consigné : un montage de portraits sans annotation n'apporte rien qu'un texte
  descriptif ne rende mieux. Cas réel cité :
  `general-syndrome-de-turner-stigmates-cliniques.jpg` (quinze portraits de
  patientes mineures), déjà écarté en p3a (concern e) sur un arbitrage pris
  seul — la règle formalise maintenant cet arbitrage.
- Les lettres b/c/d/e de l'ancien c/d ont été décalées ; toutes les
  cross-références internes (§ 8.6, § 8.7, `fetch_image.py`) ont été mises à
  jour en conséquence — vérifié par `grep -n "8\.5 [a-e]"` sur les deux
  fichiers, aucune référence orpheline.
- **§ 8.4** : « dès que la page en cite un, il est obligatoire » devient
  « quand la page en cite un **qui porte sur la vignette**, il est
  obligatoire ». Exemple ajouté au point 3, German-19 : la page « Douleur
  Abdominale » cite un message-clé sur le syndrome de l'intestin irritable —
  hors sujet pour une rectocolite ulcéro-hémorragique avec drapeaux rouges, et
  déjà écarté à raison en p3a (concern b). La règle documente maintenant
  explicitement ce cas plutôt que de l'implicite par le seul point 3.

`fetch_image.py` mis à jour en lockstep : `SIZE_WARN` 400 → 600 Ko, message
d'avertissement mentionnant les deux exemptions, et les trois références
`§ 8.5 b/c` internes corrigées vers `§ 8.5 c/d`.

### 3. Les deux images posées

| Grille | Image | Poids | Exemption |
|---|---|---|---|
| German-72 | `pedia-courbe-de-croissance-pediatrique-couloirs-p3-p97-cassure.png` | 443 Ko | 2ᵉ — désignée par le critère noté « Paramètres actuels » : `[Voir courbe de croissance, P3]` |
| German-42 | `derma-message-cle-infections-cutanees.png` | 460 Ko | 1ʳᵉ — message-clé obligatoire (§ 8.4) |

**German-72** — insérée en tête de planche (chronologie de la station, § 8.8) :
l'anamnèse (`a3`, « Paramètres actuels ») précède l'examen (`m4`, âge osseux)
et la discussion différentielle (hypothyroïdie, dans `annexe-theorie`). La
grille passe de 2 à 3 images, sous le plafond de 4 (§ 8.2).

**German-42** — le diagnostic retenu est un **tinea corporis** (dermatophytie
cutanée, cf. `annexe-theorie` et `presentation` : « lésion annulaire
prurigineuse, squameuse, au poignet, évocatrice d'un tinea corporis »). La
page SSP « Éruption Cutanée » cite **deux** message-clés :
`derma-message-cle-infections-cutanees.png` et
`general-message-cle-infections-au-virus-varicella-zoster.png`. Seul le
premier porte sur l'entité de la vignette (mycose, pas virose) — appliqué :
« jamais deux » (§ 8.4 point 2). Insérée en fin de planche (synthèse en
dernier, § 8.8) : la grille passe de 3 à 4 images, **au** plafond de 4, pas
au-delà — pas de remplacement nécessaire.

Les deux copies par `scripts/german/fetch_image.py` (idempotent, aucun
avertissement de poids après révision : 443 et 460 Ko sont désormais sous
600 Ko) ; noms exacts retrouvés dans le vault, plus longs que les formes
abrégées données en consigne.

### 4. Vérifications

```
check_invariants.py     OK — 88 grilles, tous les invariants preserves
                         (blocks INCHANGE : aucun annexe-item de plus créé)
check_nomenclature.py   OK — aucun terme non suisse détecté
check_reachability.py   OK — barème atteignable à 100 % sur chaque section
fetch_image.py --verify OK — aucun lien cassé, aucune orpheline
report_redundancy.py    TOTAL : 16 paire(s) — inchangé (vérifié par git stash
                         des deux grilles + comparaison avant/après)
amboss/check_invariants.py         OK — 40 grilles
rescos-locales/check_invariants.py OK — 165 grilles
```

Contrôle visuel en Chrome headless (`--headless=new --dump-dom`), copies
temporaires dans `cases/german/` supprimées ensuite : German-72 (3 images) et
German-42 (4 images, dont l'image base64 héritée), deux thèmes, deux largeurs
(1200/500 px). Les huit images référencées + l'image base64 rendent
`complete === true`, `naturalWidth`/`naturalHeight` égaux aux dimensions du
vault (dont **2760×1812** pour le message-clé et **502×837** pour la courbe de
croissance), rapport largeur/hauteur conservé au redimensionnement, et
`scrollWidth === innerWidth` aux quatre couples — aucun débordement.

### 5. Préoccupations

**a) L'image de German-72 est un montage, pas une figure simple.** Le PNG
502×837 empile trois panneaux : la courbe de croissance (le sujet du critère
noté), un tableau de mesures du carnet de santé, et **deux radiographies**
(main-poignet, bassin-membres inférieurs) sans lien évident avec la maladie
cœliaque retenue par German-72. La légende décrit les trois panneaux sans
prêter aux radiographies une pertinence qu'elles n'ont pas pour cette vignette
— mais je n'ai pas recadré l'image (§ 8.7 : octets tels quels, jamais
recompressés), donc la planche affiche deux radiographies hors-sujet à côté de
la courbe qui, elle, est le sujet exact du critère noté.

**b) German-42 garde sa première image en base64** — pré-existant (p3a
concern g), hors périmètre de cette tâche : la retirer casserait la référence
d'un critère noté (« Voir image en annexe »), et sa conversion reste au
programme des neuf grilles base64 déjà signalées en p2b. Le nouveau
message-clé référencé cohabite avec elle dans le même `annexe-item`, sans
incidence sur `blocks`.

**c) La nouvelle exclusion b) (photographies identifiantes) formalise un
arbitrage déjà pris, pas un nouveau.** Aucune image de ce type n'a été posée
ni retirée dans cette tâche — German-72 ne portait déjà pas le montage Turner.
La règle documente donc rétroactivement une décision de p3a plutôt que d'en
appliquer une nouvelle : à surveiller sur les grilles restantes, si le corpus
s'étend, pour vérifier qu'elle est bien appliquée en amont et pas seulement
consignée après coup.

**d) L'estimation du corpus (§ 8.6, « 220 images distinctes »)** a été laissée
telle quelle avec une note indiquant qu'elle date du plafond à 400 Ko, plutôt
que recalculée : la refaire proprement suppose de rejouer la sélection sur les
53 pages, hors périmètre d'une révision de règle.

Rapport détaillé : `.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/p3a-fix-report.md`

---

## p3b — Les 25 grilles German-2 à German-30 : les quatre blocs pédagogiques

**Périmètre** : German-2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20,
21, 23, 24, 25, 26, 28, 29, 30 — les grilles numérotées 2 à 30 moins les quatre
livrées en p3a (15, 19, 22, 27) et moins la pilote German-1. Plus
`cases/img/german/` (56 images, manifeste), `scripts/german/baseline.json`, le
journal et le rapport. Rien d'autre.

**HEAD réel au démarrage** : `6cd583f`, puis `32a7e3f`, puis `29271b2` — la
session voisine a commité **et rebasé** pendant le travail. Vérifié par `git log`
et `git reflog`, pas supposé. Incident de branche traité au § 0 ci-dessous.
Au moment de la livraison l'arbre de travail portait 198 fichiers
`cases/casecos/` modifiés par l'autre session : l'index a été construit
**chemin par chemin**, aucun de ces fichiers n'y est.

### 0. Incident de branche — trois commits effacés par un reset de la session voisine

`git reflog` porte deux `reset` consécutifs de la session voisine
(`HEAD@{3}` et `HEAD@{4}`, « moving to 7e13f93 ») qui ont retiré de la branche :

| Commit | Corpus | Contenu |
|---|---|---|
| `6cd583f` | **german** | Plafond image 400→600 Ko, deux exemptions, § 8.5 b ; images de German-72 et German-42 |
| `288894d` | CasECOS | Bascule des 198 grilles sur `cases/scoring.js` |
| `566f38d` | CasECOS | Journal CasECOS, incident d'index du lot k2 |

`git merge-base --is-ancestor 6cd583f HEAD` échoue : les trois commits existent
encore comme objets, mais ils ne sont plus atteignables depuis la branche.
Le reset n'était **pas** `--hard` — le contenu a survécu non indexé dans l'arbre
de travail.

**Le volet german a été rétabli** avant d'entamer le lot, en un commit dédié : les
cinq fichiers suivis de `6cd583f` sont byte-identiques (`git diff 6cd583f` vide),
les deux images reprises telles quelles. C'était un préalable et non un à-côté :
la sélection d'images des 25 grilles s'appuie sur le plafond de 600 Ko et sur les
deux exemptions du § 8.5 d, que `fetch_image.py` et la procédure ne portaient
plus sur la branche.

**Les deux commits CasECOS ne sont pas rétablis** — autre corpus, autre session.
Leur contenu est encore présent dans l'arbre de travail, donc récupérable, mais
il ne l'est que là : un `git reset --hard` ou un `git checkout` de la session
voisine le détruirait définitivement. **À signaler à cette session.**

### 1. Ce qui a été ajouté

| | 25/25 |
|---|---|
| `resume` créé | **24** (German-24 en portait déjà un) |
| `annexe-theorie` créé | **25** |
| `presentation-patient` créé | **25** |
| Planche d'images créée | **22** (German-10, 11 et 17 : voir § 5 a) |
| `resume` préexistant balisé sans réécriture | **1** (German-24) |
| `annexe-expert` / `annexe-scenario` créés | **0** — décision actée |
| Section notée touchée | **0** |

Aucune grille du lot ne portait `resume`, `presentation`, `annexe-theorie` ni
`images-wrapper`, à l'exception de German-24 (`resume` + coquille `annexes` vide,
héritée de l'import). Les quatre blocs ont donc été insérés en bloc, juste avant
`<!-- COMMENTAIRE GÉNÉRAL -->`, dans le gabarit de German-1 ; pour German-24,
`annexe-theorie` et `presentation` sont entrés **dans** l'`annexes-grid` vide et
l'`images-wrapper` après sa fermeture.

**La « Checklist mentale » n'existe pas dans ce corpus.** À sa place, chaque
`presentation-patient` s'ouvre sur une `presentation-section section-commcards`
portant `commcard-sbar.jpg` et `commcard-snapps.jpg` côte à côte dans un
`.commcard-grid`, servies depuis `../img/`, avec leurs `alt` descriptifs repris
mot pour mot de German-1.

### 2. La source de chaque section, grille par grille

Chaque section est adossée à la page SSP de la grille (niveau 1) ou à sa section
notée (niveau 2), et à rien d'autre.

| Grille | Diagnostic retenu | Page SSP | Sections et leur source |
|---|---|---|---|
| **German-2** | Acouphène subjectif bilatéral | Acouphènes | *Classer avant de nommer* ← « En Bref » (subjectif/objectif) + tonalité du § Caractérisation · *Examen normal* ← carte ECOS surdité brusque (Weber côté sain/atteint) + critère noté e4 · *Fenêtre de 72 h* ← red flag n° 1 + `therapy` « corticothérapie comme pour surdité brusque » · *DD* ← `annexe-dd` + les six cartes ECOS (mécanismes) · *Ototoxiques* ← carte ECOS (cellules ciliées externes vs strie vasculaire) + critère noté a10 · *Chronique* ← § Prise en charge (TCC, thérapie sonore, TRT) |
| **German-3** | Difficultés alimentaires du nourrisson, satiété précoce par aérophagie | Prévention Pédiatrique | *Couloir* ← red flag « cassure de la courbe » + critères a10/a11/e8 · *Tétée goulue* ← réponses a4/a5/a6 + intitulé m1 + `therapy` · *DD* ← les 10 entrées d'`annexe-dd` confrontées aux réponses · *Bilan* ← détails de m3 · *La mère* ← piège de la page (dépression du post-partum) + a16 · *Seuils* ← Guthrie J3-J5, vit. D 400 UI/j, diversification 4-6 mois |
| **German-4** | Agoraphobie avec attaques de panique | Trouble Anxieux | *Objet de l'anxiété* ← carte ECOS « Spectre » (évitement = mécanisme commun) · *Premier accès* ← carte « 1ʳᵉ attaque » (décharge adrénergique, hyperventilation → alcalose) · *ISRS* ← carte « 1ʳᵉ ligne » (SERT, autorécepteurs 5-HT1A, 2-4 sem., ≥ 12 mois) · *Benzodiazépine* ← carte « piège thérapeutique » (GABA-A, habituation sabotée) · *Deuil* ← § Caractérisation + critères a8/a9/a11/e7 |
| **German-5** | Entorse cervicale post-« coup du lapin » (WAD I-II) | AVP | *Mécanisme* ← § Mécanisme (hyperextension-hyperflexion) · *Classification de Québec 0-IV* ← page · *CCR/NEXUS* ← § Clearance du rachis cervical, in extenso · *Minerve* ← piège n° 4 (> 72 h) · *DD* ← `annexe-dd` + red flags cervicalgies |
| **German-6** | Périménopause à 47 ans, tableau atypique | Ménopause | *47 ans avec des règles* ← « En Bref » + tableau DD (FSH inutile > 45 ans) · *Cinq kilos* ← red flag « bouffées + amaigrissement + palpitations » · *La tension* ← tableau DD (phéochromocytome) · *Contre-indications* ← carte ECOS « Risques avant un THS » (fenêtre d'opportunité, 1ᵉʳ passage hépatique) · *Anxiété* ← § Autres symptômes + m4 |
| **German-7** | Bradycardie sur accumulation de bêta-bloquant, insuffisance cardiaque aiguë | Palpitations | *Seuil* ← « En Bref » + red flags < 40/min · *Tolérance d'abord* ← § PEC point 1 + algorithme manuscrit · *Bêta-bloquant* ← piège n° 5 + critères m1/m3 et réponse a8 · *Examens* ← 1ʳᵉ/2ᵉ ligne + carte ECOS · *Ce qui ne vaut pas ce qu'on croit* ← page (mort subite < 40 ans, déficit de pouls) |
| **German-8** | Céphalée du restaurant chinois, Horton à écarter | Céphalée | *Un bénin en dernier* ← SNOOP4 (O et P) + critères a12/e4/m3 · *D'où vient la douleur* ← carte ECOS (parenchyme insensible, méninges et V1 algogènes) · *Horton* ← carte ECOS (carotide externe) + § Arguments clés ACG · *DD* ← `annexe-dd` + ICHD-3 · *Imagerie* ← § Drapeaux + piège PL/CT + biopsie 7-14 j |
| **German-9** | Méningite virale | Céphalée | *Trois manœuvres* ← même carte ECOS (méninges algogènes) + e1/e2 · *Ne pas attendre le tableau complet* ← § Arguments clés (triade ~45 %) + couverture *Listeria* > 50 ans · *Ce que le LCR tranche* ← m4 + algorithme méningite · *DD* ← `annexe-dd` + ICHD-3 + HSA · *PL avant CT* ← piège de la page (engagement) |
| **German-10** | Accident vasculaire cérébral révélé par une chute | Chute & Éval. gériatrique | *La chute n'est que le décor* ← règle d'or (chute = symptôme) + red flags déficit focal / confusion · *Deux fois l'heure* ← critères a2/a3/a5-a10 et m4 (thrombolyse) · *DD* ← `annexe-dd` + e10 + cartes bêtabloquant et syncope · *Examens* ← m3 + § Examens complémentaires |
| **German-11** | Chute multifactorielle du sujet âgé — aucun diagnostic unique | Chute & Éval. gériatrique | *Pourquoi aucun diagnostic* ← règle d'or + « En Bref » + barème de m1 (six causes exigées) · *Trébucher n'est pas une explication* ← réponse a6 + e2 + m2 · *L'ordonnance d'abord* ← carte ECOS médicaments iatrogènes (polymédication ≥ 4) · *Hématome sous-dural* ← carte ECOS + règle d'or (TC sous antithrombotique) |
| **German-12** | Constipation récente avec drapeaux rouges, obstacle colique suspecté | Constipation | *Deux mécanismes* et *ampoule vide/pleine* ← cartes ECOS de la page · *Fausse diarrhée du constipé* ← carte ECOS + a14 · *Après 50 ans* ← carte ECOS · *Macrogol* ← carte ECOS · *Rome IV* ← tableau de la page + a4/a5 |
| **German-13** | Diarrhée chronique de malabsorption, insuffisance pancréatique exocrine | Diarrhée | *Seuil 2/4 semaines* ← carte ECOS · *Stéatorrhée* ← § Caractérisation (mécanisme) · *Sérologie cœliaque* ← piège de la page · *Insuffisance pancréatique* ← § dédié + réponses a4-a17 · *DD* ← `annexe-dd` |
| **German-14** | TDAH | Troubles du Dévelop. & Croissance | *Configuration* ← découpage du barème (a6 école vs a7 maison ; a8/a9/a10 = trois dimensions) + a4 · *Sensoriel* ← carte ECOS (« un enfant qui n'entend pas paraît distrait, opposant ») + e4 · *Habitudes* ← a5/a12/a14 + m4 · *Ritaline* ← m7 (question de la mère) et m8 (réponse attendue) · *DD* ← `annexe-dd` + signaux d'alarme TSA |
| **German-16** | Douleurs abdominales non spécifiques de l'adolescente (station de contraception) | Douleur Abdominale | *Le motif réel* ← critères a13/a17 · *Diagnostic d'exclusion* ← § Causes fréquentes non urgentes + causes psychogènes · *Discernement* ← e7 · *Contraception* ← m3-m5 · **`annexe-dd` quasi vide (12 mots) : rien n'a été comblé** |
| **German-17** | Endométriose pelvienne | Douleur Abdominale | *Hypogastre* ← tableau « Orientation par localisation » de la page · *Douglas* ← bullet « toucher rectal » + e3 · *Laparoscopie* ← m3 (« seule méthode pour confirmer ») · *Suppression œstrogénique vs désir de grossesse* ← m4 · *Séquelles* ← m5 |
| **German-18** | Infection génitale haute | Douleur Abdominale | *β-hCG d'abord* ← carte ECOS GEU (contraception bien suivie, métrorragies absentes dans un tiers des cas) · *Douglas* ← bullet toucher rectal + e4/e7 · *Traitement du partenaire* ← m4 (« Obligatoire ! ») · *Trois séquelles* ← m5 |
| **German-20** | Ischémie mésentérique aiguë | Douleur Abdominale | *Douleur disproportionnée* ← carte ECOS (physiopathologie de la discordance ; défense et lactates = nécrose transmurale) · *FA* ← red flag + CHA₂DS₂-VASc · *Metformine avant CT injecté* ← § AMPLE · *IAPA* ← carte ECOS (ausculter avant de palper) · *Ce que la grille ne note pas* ← § Mesures générales de la page |
| **German-21** | Maladie de reflux gastro-œsophagien | Douleur Abdominale | *Trois horaires* ← a4/a7/a8 · *Antiacides devenus inefficaces* ← a13/a14 · *Examens* ← m3 (gastroscopie, pH-métrie, uréase, gastrine/B12/auto-anticorps) · *Pression du sphincter* ← m4 (six mesures, quatre classes) · *DD* ← `annexe-dd` |
| **German-23** | Lésion méniscale médiale | Douleur de Genou | *Mécanisme* ← § Mécanisme du trauma · *Délai du gonflement et zone avasculaire* ← carte ECOS hémarthrose · *Valeur du Lachman* ← même carte + tableau des tests · *Ottawa* ← carte « Règle de décision pour l'imagerie » · *Suture vs résection* ← § Prise en charge |
| **German-24** | Syndrome du canal carpien | Douleur au Poignet | *Tunnel inextensible, flexion nocturne, signe du flick* ← carte ECOS « Symptôme évocateur » · *Épargne du thénar* ← piège de la même carte (branche cutanée palmaire en amont du rétinaculum) · *Phalen/Durkan vs Tinel* ← carte « Tests cliniques » · *Gravité* ← § Drapeaux rouges · *C6/C7 et Guyon* ← carte « Diagnostic à ne pas confondre » + tableau DD |
| **German-25** | Tendinopathie d'insertion du tendon d'Achille | Douleurs Articulaires | *Inflammatoire vs mécanique* ← tableau de la page, appliqué critère par critère · *Enthèse → SpA* ← carte ECOS (sacro-iliite, talalgies, dactylite) + red flag « homme < 45 ans » · *Fluoroquinolones* ← § Chronologie & contexte · **le reste ← section notée : voir § 5 b** |
| **German-26** | Occlusion artérielle aiguë fémoro-poplitée | Claudication & AOMI | *Ordre des 6 P* ← carte ECOS (sensibilité décroissante des tissus, nerf avant muscle, fenêtre ~6 h) · *Le pouls fémoral situe l'obstacle* ← § Caractérisation (mollet = fémoro-poplité) + e4 · *Embolie ou thrombose* ← § 6 P + red flag « FA + début brutal » · *L'IPS n'a pas sa place ici* ← § Pièges (ne pas attendre l'écho-Doppler) |
| **German-28** | Otite moyenne aiguë bilatérale | Otalgie | *Bilatérale change la règle* ← les deux blocs `therapy` confrontés à l'âge et à e3 · *Après le rhume* ← § Contexte (IVRS → OMA ; baignade → otite externe) · *Mastoïdite* ← carte ECOS (aditus ad antrum, trois directions, décollement vers le bas et l'avant) + e8 · *DD* ← les 8 entrées d'`annexe-dd` |
| **German-29** | Nécrose aseptique de la tête fémorale | Douleur de Hanche | *Physiopathologie* ← carte ECOS « Facteurs de risque de nécrose » (vascularisation terminale, adipocytes médullaires, secteur antéro-supérieur portant) · *Rx normale vs IRM* ← même carte + piège n° 4 · *Irradiation au genou* ← carte « Radiculalgie à ne pas confondre » (L2-L3, Léri) · *Stadification et bilatéralité* ← m6 et m7 |
| **German-30** | Contusion costale de l'adolescent | Douleur Thoracique | *50 % pariétal en 1ᵉʳ recours vs 54 % cardiovasculaire aux urgences* ← légende de l'épidémiologie comparée · *Ne pas conclure MSQ sans éliminer les cinq urgences* ← avertissement de la page · *Valve unidirectionnelle* ← § pneumothorax sous tension · *Pneumothorax spontané du sujet jeune* ← piège de la page |

**Où la source était muette, la section est courte — rien n'a été comblé.**
German-7 est la grille la plus courte du lot (4 788 mots) parce que sa page ne
traite pas la bradycardie ; German-25 n'a pas de section sur la physiopathologie
de la tendinopathie parce que sa page ne la porte pas ; German-8 ne dit rien du
mécanisme de la céphalée du restaurant chinois, absent de sa page ; German-14
tient presque entièrement sur sa section notée. Les passages concernés le disent
en toutes lettres au lieu de se taire.

### 3. Les images — motif de chaque choix

**56 images distinctes, 6 789 Ko**, toutes reprises par `fetch_image.py`, aucune
recompressée ni redimensionnée, toutes inscrites au manifeste avec leur sha256 et
leur chemin dans le vault. **Aucune image n'est citée par deux grilles du lot** —
le corollaire du § 8.3 est donc vérifié, y compris sur les cinq grilles qui
partagent la page « Douleur Abdominale » et sur les deux paires qui partagent
« Céphalée » et « Chute ». `neuro-algorithme-horton.png` est en revanche partagée
avec German-69 (p3a), qui la tient d'une **autre page** : c'est la déduplication
du § 8.6 qui joue, pas une collision de sélection.

| Grille | Images | Poids | Message-clé |
|---|---|---|---|
| German-2 | 3 | 305 Ko | la page n'en cite aucun |
| German-3 | 3 | 312 Ko | la page n'en cite aucun |
| German-4 | 3 | 506 Ko | oui — troubles anxieux |
| German-5 | 2 | 247 Ko | la page n'en cite aucun |
| German-6 | 1 | 370 Ko | **non** — ostéoporose, hors sujet |
| German-7 | 3 | 474 Ko | **non** — fibrillation auriculaire, hors sujet |
| German-8 | 4 | 635 Ko | oui — céphalée aiguë non traumatique |
| German-9 | 3 | 368 Ko | non — déjà porté par German-8 |
| German-10 | **0** | — | la page n'en cite aucun |
| German-11 | **0** | — | la page n'en cite aucun |
| German-12 | 4 | 612 Ko | oui — constipation |
| German-13 | 3 | 325 Ko | **non** — diarrhée aiguë, hors sujet |
| German-14 | 1 | 24 Ko | la page n'en cite aucun |
| German-16 | 1 | 291 Ko | oui — douleur abdominale chronique |
| German-17 | **0** | — | **non** — le même, trompeur ici |
| German-18 | 1 | 27 Ko | non |
| German-20 | 2 | 117 Ko | non |
| German-21 | 1 | 145 Ko | **non** — le même, trompeur ici |
| German-23 | 4 | 406 Ko | oui — gonalgies |
| German-24 | 3 | 286 Ko | la page n'en cite aucun |
| German-25 | 1 | 70 Ko | la page n'en cite aucun |
| German-26 | 2 | 267 Ko | la page n'en cite aucun |
| German-28 | 4 | 434 Ko | la page n'en cite aucun |
| German-29 | 4 | 177 Ko | la page n'en cite aucun |
| German-30 | 3 | 391 Ko | **non** — coronaropathie, hors sujet |

Chaque image passe au moins un des trois tests du § 8.3 ; le motif est consigné
image par image dans le rapport p3b. **Le budget de 700 Ko par grille est
respecté partout** ; German-8 est le plus chargé, à 635 Ko, dont un message-clé
de 404 Ko exempté de plafond au titre du § 8.5 d.

**Cinq message-clés écartés pour hors-sujet** (§ 8.4 point 3) : ostéoporose
(German-6), fibrillation auriculaire (German-7), diarrhée aiguë (German-13),
douleur abdominale chronique (German-17 et German-21). Le cas German-19 de p3a
n'était donc pas isolé : la condition « qui porte sur la vignette » fait un
travail réel, et elle a mordu **cinq fois sur vingt-cinq**. Le plus net est celui
de German-17 et German-21 : le panneau énonce qu'en l'absence de drapeaux rouges,
chez un patient de moins de 50 ans, aucun examen n'est nécessaire — or German-17
exige une laparoscopie diagnostique (utérus fixé, Douglas induré) et German-21
une gastroscopie chez une patiente de 57 ans.

**Une exception du § 8.5 a appliquée, après ouverture du fichier** :
`anamnese-052-algorithme-tachycardie-bradycardie.jpeg` (German-7) est un scan de
page manuscrite, retenu parce que la page **est** le schéma — et parce que c'est
la seule image de toute la page « Palpitations » qui traite la bradycardie.

**Photographies identifiantes écartées** (§ 8.5 b), toutes après ouverture :
`general-mils-collier-rigide-log-roll-a-4.jpg` (German-5, patient dévêtu sur plan
dur), `general-signes-de-deshydratation-…jpg` (German-13, nourrisson dénutri),
`gyneco-atrophie-vulvo-vaginale-…png` (German-6), et **six clichés de mensuration
d'enfants identifiables** sur la page de German-14 — dont deux du même enfant en
sous-vêtements, visage entier visible.

### 4. Le balisage sémantique

**16 180 spans / 143 655 mots = 1 pour 8,9 mots**, mesuré sur les quatre
conteneurs prescrits (`resume`, `annexe-theorie`, `presentation-section
section-mnemo`, `presentation-section section-questions`). Même métrique
appliquée à German-1 : **1 / 8,5** ; aux 13 grilles de p3a : **1 / 9,5**. Le lot
tombe donc entre la pilote validée par l'utilisateur et le lot précédent. Grille
la plus dense 1 / 8,5 (German-2, 4 et 20), la plus légère 1 / 10,2 (German-24).

Répartition : `c-green` 4 196 · `c-pink` 3 087 · `c-red` 2 407 · `c-yellow` 1 907 ·
`c-amber` 1 821 · `c-blue` 1 027 · `c-purple` 1 023 · `c-orange` 712.

**0 span hors des quatre conteneurs prescrits** sur les 25 grilles, et **0 span
dans `section-longue` ni `section-express`** — la restitution orale reste du
texte nu.

**`annexe-dd` n'a pas été balisé**, contrairement à la lettre de la consigne, et
c'est un écart assumé : voir § 5 f.

**Aucune dérive de formulation.** Le texte visible d'`annexe-dd`, `redflags`,
`therapy` et du `resume` préexistant de German-24 est identique à celui de HEAD
sur les 25 grilles, vérifié par comparaison `visible_text` bloc à bloc. Pour
German-24 la comparaison a dû se faire **blancs supprimés** : `visible_text()`
insère un espace à chaque frontière de balise, si bien que poser un `<span>`
autour d'« annulaire » scinde « l'annulaire) » en deux jetons. Hors blancs, les
deux textes font **2 585 caractères** et sont identiques.

### 5. Vérifications

| Contrôle | Résultat |
|---|---|
| `check_invariants.py` avant re-snapshot | **25 écarts, tous sur `blocks`, tous sur mes 25 grilles** |
| Diff champ par champ contre `baseline.json` | `blocks` seul champ modifié · 0 écart hors périmètre · aucun bloc retiré · aucun compte de segment existant modifié |
| `check_invariants.py` après re-snapshot | **OK — 88 grilles** |
| `check_reachability.py` | **OK — 88/88 à 100 %** |
| `check_nomenclature.py` | **OK** |
| AMBOSS — 3 scripts | **OK — 40 grilles** |
| RESCOS — 3 scripts | **OK — 41 grilles** |
| `check_no_loss.py HEAD` | **0 item disparu** sur 27 grilles modifiées |
| `fetch_image.py --verify` | **0 lien cassé, 0 orpheline** |
| `report_redundancy.py` | **0 paire sur chacune des 25** |

#### Justification du re-snapshot

Comparaison **champ par champ** de `baseline.json` au nouvel état, sur les
88 grilles :

```
Champs qui changent : ['blocks']
Grilles touchees    : [2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,20,21,23,24,25,26,28,29,30] (25)
Ecarts hors champ 'blocks' : 0
Delta blocks purement additif : True
   annexe-image: 1     ajoute sur 22 grille(s)
   annexe-theorie: 1   ajoute sur 25 grille(s)
   presentation: 1     ajoute sur 25 grille(s)
   resume: 1           ajoute sur 24 grille(s)
```

`annexe-image` n'est ajouté que sur 22 grilles (German-10, 11 et 17 n'ont pas de
planche) et `resume` que sur 24 (German-24 en portait un). **Aucun bloc retiré,
aucun compte de segment existant modifié** ; `maxScores`, `scoreSpans`,
`sectionCounts`, `criteriaCount`, `detailCount`, `radioCount`, `checkboxCount`
sont identiques sur les 88 grilles ; `boundsAnomalies` et `uncoveredContent`
restent vides.

#### La redondance

**0 paire inter-blocs avant, 0 paire après, sur chacune des 25 grilles.** Il n'y
a donc aucune paire à justifier par un changement de format. Ce n'est pas un
artefact : le détecteur a signalé des paires au fil de la rédaction, toutes
corrigées avant la fin. Sur la pilote German-2, cinq paires sont apparues à la
première passe, et c'est le pédagogique qui a cédé dans les cinq cas —
`therapy` et `redflags` n'ont pas été touchés :

- `therapy ↔ annexe-theorie` à 0,76 sur la posologie de la prednisone. La ligne a
  été **retirée** d'`annexe-theorie` : la posologie est le *quoi*, elle appartient
  au corrigé du critère. Divergence relevée au passage et **laissée telle quelle**
  (niveau 3) : la page SSP écrit « prednisone 1 mg/kg/j PO × 7-14 j », le
  `therapy` de la grille « Prednisolone 1 mg/kg/j pendant 7-10 jours ».
- `therapy ↔ presentation` à 0,75 et 0,74 (contrôle de l'HTA ; TCC) — reformulés
  dans la réponse orale.
- `resume ↔ presentation` à 0,81 et 0,74 — le mnémo « aigu = cochléaire, grave =
  Ménière » recopiait le `resume` ; réécrit en « le timbre situe l'étage ».

#### Contrôle visuel

Chrome `--headless=new`, rendu local `file://`, aucune requête réseau. Deux
grilles × deux thèmes × deux largeurs = **8 rendus**. German-8 (4 images, dont un
message-clé de 2190×1689) et German-24 (le cas particulier : `resume` préexistant
balisé + trois blocs neufs).

Copies temporaires à `data-theme` figé placées dans `cases/german/` pour que
`../img/german/` résolve, **supprimées ensuite** : `git status` ne montre aucun
`_tmpvis-*`.

- **Chargement** : `complete === true` et `naturalWidth`/`naturalHeight` **égaux
  aux dimensions du vault** pour les onze images (dont les deux cartes de
  communication). `cassees=0` aux huit rendus.
- **Rapports conservés** : 2190/1689 = 1,2966 → rendu 1046/807 = 1,2962 ;
  846/917 = 0,9226 → 848/919 = 0,9227 ; 614/330 = 1,8606 → 616/332 = 1,8554.
- **Aucun débordement horizontal** : `scrollWidth === innerWidth` à 1200 comme à
  500 px, dans les deux thèmes.
- **Les huit classes rendent une couleur distincte dans chaque thème**, et
  `neutralises=0`. `c-yellow` rend un **fond** (`rgba(245,200,66,0.18)` en sombre)
  et non une couleur de texte, conformément au relevé de p3a.

### 6. Préoccupations

**a) Trois grilles sont livrées sans planche d'images, et ce n'est pas un défaut
de sélection.**

- **German-10 et German-11** partagent `SSP — Chute & Évaluation Gériatrique.md`,
  qui ne cite que **4 images** — contre une médiane de 12 sur les 53 pages. Deux
  passent le test 1 (`neuro-epreuve-romberg.png` pour le critère e3,
  `gals-inspection-marche.png` pour le critère e2) et sont écartées à **5 403 Ko
  et 3 008 Ko**, soit 9× et 5× le plafond ; les deux autres (fracture du col
  fémoral, échelle GDS-15) échouent les trois tests. Aucun message-clé.
- **German-17 (endométriose)** : la page « Douleur Abdominale » ne porte **aucune
  iconographie gynécologique** — ni annexe, ni GEU, ni torsion, ni kyste, ni
  endométriose — alors que ces entités sont nommées dans son texte, dans ses red
  flags et dans deux `annexe-dd`. Son contenu est presque entièrement construit
  autour de l'abdomen aigu chirurgical.

**b) Sept pages SSP ne couvrent pas la vignette qu'elles desservent.** C'est le
relevé le plus important de ce lot, et il est plus large que celui de p3a.

| Page | Grille | Ce qui manque |
|---|---|---|
| Palpitations | German-7 | Page de **tachycardie**. Sur la bradycardie : la définition, deux drapeaux rouges chiffrés, le BAV en liste, un piège. **Muette** sur l'hypothyroïdie (que l'`annexe-dd` nomme, chez une patiente thyroïdectomisée), la maladie du sinus, les indications du stimulateur (critère m6, 2 points) et l'accumulation médicamenteuse par baisse de filtration — **qui est le diagnostic retenu du corrigé**. Toute la conduite bradycardique ne figure que dans une image |
| Douleur Thoracique | German-30 | 653 lignes, 47 images, et **deux lignes** sur la traumatologie pariétale de l'adolescent. Rien sur la contusion costale, la fracture de côte isolée, la physiothérapie respiratoire, le certificat. La page la plus riche du corpus, la plus mal appariée à sa vignette |
| Douleurs Articulaires | German-25 | Confirmation aggravée du signalement de p3a. **Trois lignes** touchent le talon sur 380 ; aucune des six hypothèses de l'`annexe-dd` (tibial postérieur, fasciite plantaire, fracture de fatigue, bursite, Haglund, rupture partielle) n'est documentée ; **aucune** des 15 images ne concerne le pied |
| Troubles du Dévelop. & Croissance | German-14 | Traite le retard psychomoteur, le TSA et la croissance staturale. Le **TDAH** n'apparaît que dans le « DD Top 5 » et un renvoi. Une page « SSP — TDAH » serait la bonne source |
| Douleur Abdominale | German-16, 17, 18, 21 | Page d'**abdomen aigu chirurgical**. German-16 est une station de contraception et de discernement ; German-17 et German-18 sont gynécologiques ; German-21 est un reflux traité en une ligne de tableau. Seule German-20 est réellement couverte |
| Chute & Éval. gériatrique | German-10 | Porte bien le red flag « déficit focal post-chute → AVC », mais est **muette** sur la thrombolyse, la consigne de ne pas trop abaisser la TA, la distinction AIT/DNIR/AVC progressif et la dissection carotidienne — quatre éléments que la grille note |
| Céphalée | German-8 | « Céphalée du restaurant chinois » — le diagnostic retenu du critère m1 — **n'apparaît nulle part** sur la page |
| Prévention Pédiatrique | German-3 | Page de consultations systématiques ; la vignette est une difficulté d'allaitement bâtie sur des percentiles, et **la page ne cite aucune courbe de croissance** |

**c) Le plafond de 600 Ko coûte le plus cher au musculo-squelettique, et pour une
raison technique, pas éditoriale.** Onze images écartées sur ce seul motif
documentent chacune un **critère explicitement noté** :

| Image | Poids | Grille | Critère noté |
|---|---|---|---|
| `cardio-palpation-vasculaire.png` | 5 065 Ko | 26 | e4, les quatre pouls et la comparaison controlatérale |
| `hanche-genou-test-faber.png` | 10 501 Ko | 29 | e5, tests spécifiques |
| `main-test-froment.png` | 11 100 Ko | 24 | e-main |
| `main-manoeuvre-watson.png` | 11 100 Ko | 24 | e-main |
| `neuro-epreuve-romberg.png` | 5 403 Ko | 10 | e3 |
| `gals-inspection-marche.png` | 3 008 Ko | 10 | e2 |
| `abdo-palpation-aorte.png` | 7 722 Ko | 20 | e8, anévrisme de l'aorte |
| `hanche-genou-test-pivot-shift.png` | 5 500 Ko | 23 | e5 |
| `test-fadir.png` · `test-gaenslen.png` · `log-roll-test.png` | 7 800 à 9 400 Ko | 29 | e5 |

Ce sont des **PNG non optimisés d'illustrations vectorielles simples** :
`main-manoeuvre-de-phalen.png` (188 Ko, retenue) et `main-test-phalen.png`
(12 600 Ko, écartée) portent **le même contenu à un facteur 67**. Une passe de
recompression **côté vault** — hors périmètre ici, et interdite côté grille par
le § 8.7 — rendrait accessible une dizaine d'images qui passent le test 1. C'est
le geste au meilleur rendement de tout ce relevé.

**d) Neuf références cassées, toutes des pages de PDF converties.**
`Résumé-SSP_page-0023` à `0027` (page « Douleur Abdominale ») et
`Résumé-SSP_page-0056` à `0059` (page « Céphalée ») : **0 octet** dans le vault.
Elles étaient de toute façon exclues au § 8.5 a, mais à lire leurs légendes ce
sont les planches les plus utiles de la page « Douleur Abdominale »
(caractérisation de la douleur, drapeaux rouges et déroulé de l'examen,
manœuvres ciblées, DD par topographie, urgences abdominales). Les réparer
débloquerait d'un coup l'iconographie d'examen de cinq grilles.

**e) Un fichier défectueux du vault confirmé, non contourné.**
`ped-algorithme-diagnostique-petite-taille-enfant.jpg` → `ÉCHEC [corrompu]`,
en-tête JPEG incohérent — deuxième relevé après p3a. Aucun troisième rencontré.
Signalé, **le vault n'a pas été modifié**.
Doublon relevé par ailleurs : `rachis-dermatomes-mi.png` et `main-dermatomes.png`
existent en double (`Skills ECOS/img/…` et `Skills ECOS/.backup_transparents/img/…`) ;
`fetch_image.py` n'a pas signalé `[ambigu]` et a repris la version principale,
mais c'est une source d'échec futur.

**f) `annexe-dd` n'a pas été balisé — écart assumé à la consigne.**
La consigne demandait de baliser `resume` **ou** `annexe-dd` quand ils
préexistent sans balisage. Le `resume` de German-24 l'a été. `annexe-dd` ne l'a
pas été, sur les 25 grilles, pour trois raisons : les **88 grilles du corpus**
portent aujourd'hui `annexe-dd` sans un seul span ; le lot p3a l'a laissé tel
quel sur ses 13 grilles et en a fait un résultat publié (« 0 span hors des quatre
conteneurs prescrits ») ; et la cible de densité est définie sur ces quatre
conteneurs, si bien que baliser un cinquième bloc rendrait la mesure non
comparable. Baliser 25 `annexe-dd` sur 88 aurait créé une hétérogénéité durable
au moment précis où le corpus s'uniformise. **Arbitrage à confirmer** : si le
balisage d'`annexe-dd` est voulu, il doit être fait sur les 88 en une passe, pas
sur 25.

**g) Deux incohérences internes de grille relevées, laissées inchangées
(niveau 3).** German-13 : l'en-tête annonce « diarrhée évoluant depuis 6 mois »,
la réponse patient du critère a4 dit « depuis 4 mois » — la restitution orale
écrit « plusieurs mois ». German-26 : le critère a18 porte « Antécédents
familiaux positifs [non] » et le critère a25 « [Père : infarctus du myocarde à
63 ans] » — seule la seconde est utilisée, sans énoncer la négation.
German-9 ne note **aucune température** alors que la vignette est une méningite
et que la page fait de la fièvre le pivot du tableau : trou de la grille, pas de
la page, traité dans l'`annexe-theorie` par la triade incomplète (~45 %).

**h) `annexe-dd` de German-16 est quasi vide** — une seule entrée, « Douleurs
abdominales non spécifiques », 12 mots. Rien n'a été comblé : l'`annexe-theorie`
s'adosse à la page et aux critères notés, et pose explicitement le caractère de
diagnostic d'exclusion. C'est le plus court `annexe-dd` des 88.

**i) Neuf grilles restent en base64**, dont German-42, 43 et 44 dont un critère
noté renvoie explicitement à l'image (« Voir image en annexe »). Chantier déjà
signalé en p2b et p3a, hors périmètre ici.

Rapport détaillé : `.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/p3b-report.md`

---

# Lot p3c — sections pédagogiques des grilles German-31 à 60

## Liste établie sur pièces

`German-31` à `German-60`, moins les six déjà complétées (34, 42, 43, 44, 48, 56)
= **24 grilles**. Composition initiale relevée grille par grille avec
`lib_german.py`, et non supposée :

| Composition de départ | Grilles |
|---|---|
| `annexe-dd` seul, ± `therapy`, ± `redflags` | 31, 32, 33, 35, 37, 40, 41, 45, 46, 47, 49, 50, 51, 53, 55, 57, 58, 59, 60 |
| `annexe-dd` + `annexe-image` + coquille `annexes` | 36, 57 |
| `therapy` seul, sans `annexe-dd` | 52, 54 |
| **aucun bloc pédagogique** | **38, 39** |
| `resume` préexistant | **aucune** |

Aucune des 24 ne portait de `resume` : le cas « baliser un resume préexistant
sans le réécrire » ne s'est donc pas présenté dans ce lot.

## Ce qui a été livré — 17 grilles sur 24

**Livrées et commitées** : 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 45, 46, 47,
49, 50, 51, 52.

**Non traitées, restant à faire** : **53, 54, 55, 57, 58, 59, 60** — sept
grilles, dont trois lombalgies (57, 58, 59), la paire HTA (53, 54), l'ictère (55)
et le malaise (60). Le travail s'est arrêté sur épuisement du budget de contexte
de la session, et non sur un obstacle technique. Le relevé préparatoire de
German-53 et German-54 figure ci-dessous pour la session suivante.

| | 17/17 |
|---|---|
| `resume` créé | 17 |
| `annexe-theorie` créé | 17 |
| `presentation-patient` créé | 17 |
| Planche d'images créée ou complétée | 17 |
| `annexe-expert` / `annexe-scenario` créés | **0** |
| Section notée touchée | **0** |
| `annexe-dd` balisé | **0** (écart assumé, cf. p3b § 6 f) |

Chaque `presentation-patient` s'ouvre sur une `section-commcards` portant
`commcard-sbar.jpg` et `commcard-snapps.jpg` dans un `.commcard-grid`, servies
depuis `../img/`, avec les `alt` de German-1 repris mot pour mot. **Aucune
« Checklist mentale »** dans les 17 grilles.

## Les pages SSP qui ne couvrent pas leur vignette — quatre cas

Le relevé de p3b portait sur huit pages ; celui-ci en ajoute quatre, dont deux
plus sévères que tout ce qui avait été signalé jusqu'ici.

1. **Skills — Entretien Motivationnel / German-39 (conseil vaccinal)** — le cas
   le plus net du corpus à ce jour. La page est une page de *méthode* consacrée à
   l'entretien motivationnel, dont les applications développées sont l'alcool et
   le tabac. Elle ne mentionne l'hésitation vaccinale **qu'une seule fois, sous
   forme d'un renvoi vidéo**, dans une liste d'autres applications possibles.
   Aucun contenu vaccinal n'en provient : calendrier, maladies évitées,
   complications, létalités, cadre légal suisse, remboursement, carnet de
   vaccination — tout vient du corrigé. Ce que la page apporte réellement est la
   moitié communicationnelle : Ask-Tell-Ask, OARS, esprit d'acceptation et
   d'autonomie, erreurs à éviter. **Une page consacrée au conseil vaccinal
   pédiatrique serait la source appropriée.**
2. **Ballonnement (Météorisme) / German-49 (hernie inguinale)** — la page traite
   les troubles fonctionnels intestinaux, la distension gazeuse, l'ascite et
   l'occlusion. Elle mentionne les **hernies pariétales une seule fois**, comme
   une ligne de l'examen abdominal. Sémiologie herniaire, réductibilité,
   distinction directe/indirecte, techniques opératoires et complications
   viennent du corrigé seul. La page apporte en revanche le versant occlusif, qui
   est exactement la complication vers laquelle pointent les cinq signaux
   d'alarme du `redflags` — d'où le choix des deux images retenues.
3. **Dysurie / German-37 (urétrite IST)** — la page traite les infections
   urinaires : cystite, pyélonéphrite, prostatite, bactériurie de la femme
   enceinte. Elle nomme l'urétrite et le contexte sexuel à risque dans son
   différentiel, indique la PCR sur premier jet et pose le principe de traiter le
   partenaire, mais ne développe pas la prise en charge des IST : ni protocole
   antibiotique, ni modalités de notification, ni calendrier de dépistage
   sérologique et de test de guérison.
4. **Douleur Thoracique / German-33 (RGO)** — confirmation du signalement de p3b
   sur German-30. La page range le RGO parmi les causes fréquentes, oriente vers
   lui la douleur à type de brûlure, fait palper l'épigastre et met en garde
   contre le raisonnement par le test aux IPP — mais ne développe ni la
   physiopathologie du reflux, ni le mécanisme des IPP, ni les indications
   comparées de la pH-métrie et de l'endoscopie.

Cas apparentés, moins sévères, également consignés dans les `annexe-theorie` :
**Dyspnée / German-35 et German-36** (la page traite l'asthme aigu et
l'exacerbation de BPCO, non l'asthme d'effort ni la BPCO stable) et
**Malaise & PC brève / German-41** (excellente sur le différentiel syncope contre
épilepsie, muette sur le bilan d'une première crise, les antiépileptiques et les
métastases cérébrales).

**À l'inverse**, la page « Fatigue » couvre correctement ses trois vignettes
(SAOS, anémie ferriprive, dépression), et la page « Syndrome Néphrotique » couvre
la sienne : le problème n'est donc pas général, il est d'appariement.

## Les images

**41 images distinctes ajoutées, 5 410 Ko**, toutes reprises par
`fetch_image.py`, aucune recompressée ni redimensionnée, toutes au manifeste avec
sha256 et chemin du vault.

**Corollaire du § 8.3 vérifié.** Trois grilles partagent la page « Douleur
Thoracique », deux la page « Dyspnée », trois la page « Fatigue », deux la page
« Skills — Entretien Motivationnel » : **aucune image n'est commune à deux
grilles du lot**, message-clé excepté. Deux images planifiées pour German-32 ont
dû être réattribuées après constat que German-30, traitée en p3b sur la même
page, les portait déjà.

### Message-clé — la condition du § 8.4 a mordu 4 fois sur 17

| Grille | Message-clé | Décision |
|---|---|---|
| German-33 (RGO, cabinet) | douleur thoracique | **posé** — porte sur la médecine de premier recours, le score TOPIC et l'angor stable, c'est-à-dire la vignette |
| German-31 (EP, urgences) | douleur thoracique | **écarté** — parle de premier recours et d'exclusion coronarienne, hors sujet aux urgences pour une EP |
| German-32 (pneumothorax, urgences) | douleur thoracique | **écarté** — même motif |
| German-35 (asthme d'effort) | asthme | **posé** — diagnostic par spirométrie réversible, tabac comme facteur de mauvais contrôle |
| German-36 (BPCO GOLD I) | BPCO | **posé** |
| German-38 (EM tabac) | arrêt du tabagisme | **posé** |
| German-37 (urétrite IST) | infection urinaire simple | **écarté** — porte sur la bactériurie asymptomatique et les germes multirésistants, pas sur une IST |
| German-46 (anémie ferriprive) | fatigue | **posé** — son troisième message nomme explicitement la carence en fer |
| German-47 (dépression) | fatigue | **posé** — ses deux premiers messages portent sur le lien psychosocial et le bilan organique systématique |
| German-45 (SAOS) | fatigue | **écarté** — ni psychosocial ni martial |

Chaque message-clé écarté a été **ouvert et lu** avant décision. Quatre écarts sur
dix-sept : la condition « qui porte sur la vignette » continue de mordre, dans la
même proportion qu'en p3b (cinq sur vingt-cinq).

### Images écartées pour le poids — § 8.5 d

Trois fichiers documentant un **critère explicitement noté** ont été écartés au
seul motif du plafond de 600 Ko :

| Fichier | Poids | Critère noté qu'il documentait |
|---|---|---|
| `abdo-punch-renal.png` | **10 646 Ko** | Giordano — German-37 (e2) et German-51 (e2) |
| `abdo-palpation-reins.png` | **8 723 Ko** | palpation des fosses lombaires — German-51 (e2) |
| `general-fatigue-examens-paracliniques.jpg` | **798 Ko** | bilan de la fatigue ; sa légende porte de surcroît le piège de la ferritine, protéine de la phase aiguë, directement utile à German-46 |

Ces trois-là s'ajoutent aux onze relevés en p3b, et confirment son constat § 6 c :
ce sont des PNG non optimisés dont une passe de recompression **côté vault**
rendrait accessible une dizaine d'images qui passent le test 1.

### Exception du § 8.5 a appliquée, et une refusée

- **Retenue** : `EM_Aide_page-0004.jpg` (557 Ko, German-39) — fiche PEPra à
  figure unique sur l'attitude de base en entretien motivationnel, ouverte et
  lue avant décision : la page **est** le schéma.
- **Refusée** : `EM_Aide_page-0002.jpg` (403 Ko) — dix questions évocatrices en
  liste. C'est du texte long en image, exactement ce que le § 8.5 a proscrit :
  non sélectionnable, non traduisible, et invisible au dédoublonnage.

### Grilles à moins de trois images

- **German-41** : une seule. Sa page (« Malaise ») cite sept images, dont six
  portent sur la syncope et le rythme cardiaque ; German-41 n'a **aucun critère
  ECG** et **aucune cause cardiaque dans son `annexe-dd`**. Seule la morsure
  latérale de la langue passe le § 8.3.
- **German-39** : une seule, cf. supra.
- **German-45, 46, 47** : deux chacune. La page « Fatigue » cite douze fichiers,
  dont **cinq cassés** et un hors plafond ; il en reste six exploitables pour
  trois vignettes.

## Fichiers du vault défectueux — signalés, non contournés

1. **`pulmo-ep-algorithme-sans-choc-esc.jpg`** → `ÉCHEC [corrompu]`. Diagnostic
   posé : le fichier est **un PNG portant une extension `.jpg`**
   (`file` : *PNG image data, 1669 x 1358*). Ce n'est pas une troncature.
   `fetch_image.py` a raison de refuser : livrer l'octet tel quel sous un nom
   mensonger casserait le rendu sur tout serveur qui se fie à l'extension.
2. **`pulmo-ep-algorithme-avec-choc-esc.jpg`** — **même défaut**, vérifié dans la
   foulée (*PNG image data, 1854 x 1636*). Les deux algorithmes ESC de l'embolie
   pulmonaire de la page « Douleur Thoracique » sont donc inutilisables en l'état.
   German-31 a reçu à la place l'angio-CT, qui documente le critère m3.
   **Correction souhaitable côté vault : renommer les deux fichiers en `.png`.**
3. **Six références cassées** (0 octet) découvertes sur deux pages nouvelles :
   `Résumé-SSP_page-0018` à `0022` (page « Fatigue », cinq fichiers) et
   `Résumé-SSP_page-0040` (page « Hématurie »). Elles s'ajoutent aux neuf de
   p3b, portant le total connu à **quinze**, toutes de la même famille
   `Résumé-SSP_page-00NN.jpg`. Écartées de toute façon au § 8.5 a, mais leurs
   légendes décrivent des planches utiles — pour la page « Fatigue » :
   l'anamnèse par hypothèse, la trame ECOS en trois temps, les étiologies
   endocriniennes, l'opposition insuffisance surrénalienne / hypothyroïdie, et le
   bilan de laboratoire.

Aucun contournement n'a été tenté et **le vault n'a pas été modifié**.

## Divergences page / corrigé relevées, barème inchangé (niveau 3)

- **German-35** — les messages clés de la page posent qu'un bêta-2 mimétique de
  courte durée ne doit **jamais** être utilisé seul en monothérapie à la demande,
  et donnent pour traitement de choix l'association corticoïde inhalé et
  formotérol ; le corrigé place le bêta-2 mimétique à la demande en traitement
  aigu et ne réserve le corticoïde inhalé qu'aux symptômes fréquents. Les deux
  formulations sont rapportées telles quelles dans l'`annexe-theorie`.
- **German-41** — la page pose l'**ECG 12 dérivations comme systématique devant
  toute perte de connaissance transitoire**, et fait de son omission un piège
  explicite. Le corrigé ne le cote pas parmi ses examens complémentaires.
- **German-38** — la station propose un rendez-vous de suivi « dans 6 mois
  maximum », les points clés de la page un suivi « à moins de 2 à 4 semaines ».
  Les deux se comprennent par leur contexte : la page décrit le suivi d'un arrêt
  engagé, la station celui d'un patient en contemplation à qui l'on laisse la
  porte ouverte.
- **German-31** — le corrigé conditionne l'oxygénothérapie à une SpO₂ inférieure
  à 94 %, la page à 90 % dans sa section SCA. Contextes différents ; le `resume`
  renvoie au seuil de la station sans le contredire.

## Particularités internes de grille, laissées inchangées

- **German-39** — la section « examen clinique » **ne contient aucun examen
  physique** : elle est entièrement consacrée à l'explication des vaccins et de
  leur calendrier. Relevé sans être corrigé, barème inchangé.
- **German-40** — la fillette a des **fuites diurnes** une à deux fois par
  semaine, ce qui la place hors du cadre monosymptomatique au sens de la page, et
  fait entrer l'échographie réno-vésicale dans les indications. Le corrigé
  formule prudemment « échographie rénale si nécessaire dans le suivi ». La
  tension est explicitée dans l'`annexe-theorie` sans toucher au barème.
- **German-41** — céphalées décrites à **gauche** et hémiparésie **gauche**, qui
  renverrait à une atteinte de l'hémisphère droit. La latéralisation d'une
  céphalée étant un mauvais localisateur, le fait est relevé sans être présenté
  comme une erreur.
- **German-36** — orthopnée à trois oreillers et dyspnée paroxystique nocturne
  chez une vignette dont le corrigé retient une BPCO GOLD I. La station donne
  elle-même les moyens d'explorer la tension (critère d'anamnèse sur les
  symptômes d'IC, critère d'examen sur l'IC droite, NT-proBNP et échocardiographie
  au différentiel) ; l'`annexe-theorie` la traite sans trancher.
- **German-46** — grille sans critère de diagnostic principal ni réponses patient
  chiffrées : elle cote directement les différentiels puis la *reconnaissance*
  d'une anémie ferriprive et d'une carence vitaminique sur leurs caractéristiques
  biologiques. C'est la démarche qui est évaluée, non la reconnaissance d'un
  tableau donné.

## Mesures

| Contrôle | Résultat |
|---|---|
| `report_redundancy.py`, avant et après, sur chacune des 17 | **0 paire nouvelle** |
| Densité de balisage, 4 conteneurs prescrits | **9 571 spans / 90 892 mots = 1 pour 9,5** |
| Spans hors conteneur | **0** |
| Spans dans `section-longue` / `section-express` | **0** |
| `check_invariants.py` après re-snapshot | **OK — 88 grilles** |
| Diff baseline champ par champ | `blocks` seul champ modifié · 17 grilles · 0 écart hors champ · **delta purement additif** |
| `check_reachability.py` | **OK — 88/88 à 100 %** |
| `check_nomenclature.py` | **OK** |
| AMBOSS — 3 scripts | **OK — 40 grilles** |
| RESCOS — 3 scripts | **OK — 41 grilles** |
| `fetch_image.py --verify` | **0 lien cassé, 0 orpheline** |
| Contrôle visuel | **4 grilles × 2 thèmes × 2 largeurs = 16 rendus, 0 image cassée, 0 débordement** |

Densité par grille : plus dense **1/8,0** (German-52), plus légère **1/12,1**
(German-38). Les deux grilles les plus légères sont German-38 et German-39, deux
stations de **pure communication** : elles offrent structurellement moins de
termes balisables — pas de pathologie, pas d'examen complémentaire, pas de
traitement à nommer. C'est une propriété du sujet, non un défaut d'application.

Répartition : `c-pink` 2 524 · `c-green` 2 473 · `c-red` 1 682 · `c-yellow` 797 ·
`c-purple` 772 · `c-blue` 566 · `c-amber` 478 · `c-orange` 279.

## Contrôle visuel

Chrome `--headless=new`, rendu local `file://`, aucune requête réseau. Quatre
grilles retenues pour leur diversité de format : **German-33** (message-clé de
2280 px), **German-36** (mélange base64 hérité et images référencées),
**German-38** (fichier **SVG**, premier du corpus) et **German-51** (trois JPEG).

- Chargement : `complete === true` et `naturalWidth`/`naturalHeight` **égaux aux
  dimensions du vault** pour les seize images ; `cassees=0` aux seize rendus.
  Le SVG rend 600×600.
- Aucun débordement horizontal : `scrollWidth === innerWidth` à 1200 et 500 px,
  dans les deux thèmes.
- Huit couleurs distinctes dans chaque thème, `neutralises=0` ; `c-yellow` rend
  un fond et non une couleur de texte.
- Copies temporaires supprimées : aucun `_tmpvis-*` dans `git status`.

## Relevé préparatoire pour la session suivante

Les sept grilles restantes ont été partiellement instruites :

- **German-53** (HTA essentielle grade 2, femme 56, découverte à l'automesure) et
  **German-54** (HTA non contrôlée avec début d'insuffisance cardiaque, femme 67,
  observance imparfaite et AINS) partagent `SSP — HTA (Suivi & Crise
  Hypertensive).md`, qui cite 16 images dont un message-clé. German-54 ne porte
  **aucun `annexe-dd`**. Sélections envisagées, à valider :
  German-53 — classification de l'HTA, MAPA 24 h, critères d'investigation d'une
  HTA secondaire ; German-54 — HVG à l'ECG, Rx d'OAP hypertensif, message-clé.
  **Le message-clé n'a pas encore été ouvert** : la condition du § 8.4 reste à
  vérifier pour les deux.
- **German-55** (ictère), **German-57**, **58**, **59** (lombalgies, page
  commune à trois vignettes — le corollaire du § 8.3 y sera le plus exigeant du
  corpus), **German-60** (malaise, page partagée avec German-41 déjà traitée :
  les six images de syncope encore disponibles lui reviennent).
- **German-57** porte déjà une coquille `annexes` et une image en base64, comme
  German-36 : même procédure d'insertion.

## Commits

| Hash | Contenu |
|---|---|
| `8e82399` | German-31, 32, 33, 35, 36 + 15 images |
| `5a7e02c` | German-37, 38, 39, 40, 41 + 10 images |
| `ca2bdc8` | German-45, 46, 47, 49, 50 + 10 images |
| `6e112f4` | German-51, 52 + 6 images |

Index construit **chemin par chemin** avant chaque commit, avec vérification
explicite qu'aucun fichier de `cases/rescos/`, `cases/casecos/`,
`cases/rescos-locales/`, `scripts/rescos/` ou `scripts/casecos/` n'y figurait.
Aucun `git add -A`. La session voisine a commité `e54b127` et `135dbca` entre
mes commits ; la réaccessibilité de `8e82399` et `5a7e02c` depuis HEAD a été
vérifiée après coup.

Rapport détaillé : `.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/p3c-report.md`

---

# Lot p3c-bis — les sept grilles restantes du lot p3c

## Périmètre et point de départ

`German-53, 54, 55, 57, 58, 59, 60` — les sept grilles que le lot p3c avait
laissées, sur épuisement de budget de contexte et non sur obstacle technique.
Le relevé préparatoire de p3c (§ « Relevé préparatoire pour la session
suivante ») a servi de point d'entrée : il a épargné le repérage des pages SSP
et l'inventaire de composition, tous deux vérifiés et exacts.

**HEAD réel au démarrage** : `9b8c1bd`, et non le HEAD documenté par p3c. La
session voisine avait commité `741cd86` et `626fde7` entre-temps ; mes trois
commits sont restés accessibles depuis HEAD, vérifié par
`git merge-base --is-ancestor` sur chacun.

Composition de départ, mesurée et non supposée :

| Grille | Blocs présents avant |
|---|---|
| German-53 | `annexe-dd` ×1, `therapy` ×3 |
| German-54 | `therapy` ×2 — **aucun `annexe-dd`** |
| German-55 | `annexe-dd` ×1, `therapy` ×3 |
| German-57 | `annexe-dd` ×1, `therapy` ×4, `annexe-image` ×1 + coquille `annexes` |
| German-58 | `annexe-dd` ×1, `therapy` ×4 |
| German-59 | `annexe-dd` ×1, `therapy` ×3 |
| German-60 | `annexe-dd` ×1 |

Aucune ne portait de `resume` : le cas « baliser un `resume` préexistant sans
le réécrire » ne s'est pas présenté dans ce lot non plus.

## Livré

7 grilles sur 7. Chacune reçoit `resume`, `annexe-theorie`,
`presentation-patient` et **une seule** `annexe-item` d'images.

| | 7/7 |
|---|---|
| `resume` créé | 7 |
| `annexe-theorie` créé | 7 |
| `presentation-patient` créé | 7 |
| Planche d'images créée ou complétée | 7 |
| `annexe-expert` / `annexe-scenario` créés | **0** |
| Section notée touchée | **0** |
| `annexe-dd` balisé | **0** (écart assumé, cf. p3b § 6 f) |
| « Checklist mentale » | **0** — remplacée par `section-commcards` (SBAR + SNAPPS) |

German-57 est le second cas du corpus, après German-36, d'une grille portant
déjà une coquille `annexes` vide et une image en base64 dans un
`images-wrapper`. Procédure identique : le `resume` s'insère avant
`<div class="annexes">`, `annexe-theorie` et `presentation-patient` dans
l'`annexes-grid` vide, et les deux images nouvelles **encadrent** le triplet
hérité à l'intérieur de l'unique `annexe-item` — l'ordre du § 8.8 étant
respecté (signaux d'alarme, puis radiographie, puis message-clé). Aucun second
`annexe-item` ouvert : `annexe-image` reste à 1 segment.

## Les pages SSP qui ne couvrent pas leur vignette — quatre cas de plus

Le relevé de p3a en comptait huit, celui de p3c quatre. Ce lot en ajoute
quatre, dont un plus sévère que tout ce qui a été signalé jusqu'ici.

1. **Lombalgies / German-59 (colique néphrétique)** — **le cas le plus net du
   corpus à ce jour, devant German-39.** La page ne mentionne la colique
   néphrétique que trois fois, toujours comme *piège* : dans son encadré
   « Pièges » (« oublier les causes extra-spinales »), dans la colonne
   « douleurs référées » de son tableau de différentiel, et dans sa
   catégorisation par mécanisme. Ses « skills connexes » **renvoient
   explicitement à `[[SSP — Colique Néphrétique]]` avec la mention
   "DDx référé"** — la page dit elle-même où se trouve le contenu. Rien sur la
   maladie lithiasique : ni mécanisme de la douleur colique, ni taille du
   calcul et probabilité d'expulsion, ni antalgie de première intention, ni
   raison d'éviter la morphine, ni alpha-bloquants, ni filtration des urines,
   ni bilan métabolique, ni prévention des récidives. Tout cela vient du
   corrigé. **Ce que la page apporte réellement est le raisonnement d'exclusion
   du rachis** — et c'est sur lui que l'`annexe-theorie` a été construite, avec
   une section explicite disant ce qui manque. `SSP — Colique Néphrétique`
   existe dans le vault : **c'est un défaut de la table d'appariement, pas de
   la page.**
2. **HTA / German-54 (HTA non contrôlée avec insuffisance cardiaque
   débutante)** — la page couvre parfaitement la moitié tensionnelle :
   observance comme cause n° 1, AINS, pseudo-résistance, définition de l'HTA
   résistante, effets indésirables par classe, cibles par âge, hypotension
   orthostatique avant intensification. Elle ne couvre pas la moitié
   cardiologique : diurétique de l'anse, pesée quotidienne, surveillance de la
   diurèse, restriction hydrique. Le `NT-proBNP` et la radiographie thoracique
   n'y figurent qu'au bilan de l'*urgence* hypertensive.
3. **Ictère / German-55 (hépatite A aiguë)** — la page couvre intégralement le
   raisonnement diagnostique : classification par la bilirubine, triplet
   selles-urines-prurit, seuils de transaminases, TP-facteur V comme marqueur
   de gravité, sérologies, échographie. Elle ne couvre pas la santé publique de
   l'hépatite A : déclaration obligatoire, éviction d'un professionnel de
   l'alimentation, vaccination de l'entourage, délai de normalisation.
4. **Lombalgies / German-57 (fracture vertébrale ostéoporotique)** — la page
   couvre les drapeaux rouges, l'examen du rachis et la stratégie d'imagerie,
   et rattache explicitement la fracture vertébrale aux facteurs de risque
   d'ostéoporose. Elle ne couvre pas l'ostéoporose : interprétation de la
   densitométrie, seuils de traitement, calcium et vitamine D,
   bisphosphonates, dénosumab, prévention des chutes. Elle n'en cite que
   l'outil `FRAX`.

Dans les quatre cas, la section concernée de l'`annexe-theorie` porte un
paragraphe intitulé « Ce que la page SSP ne couvre pas ici », qui nomme
précisément ce qui manque et renvoie au corrigé. **On n'a rien comblé.**

## Message-clés — deux embarqués, deux écartés

| Page | Fichier | Décision |
|---|---|---|
| HTA | `cardio-message-cle-hypertension-arterielle.png` | **Embarqué** dans German-53 et German-54 |
| Ictère | `abdo-message-cle-tests-hepatiques-perturbes.png` | **Écarté** (§ 8.4 pt 3) |
| Lombalgies | `rachis-message-cle-rachialgie-aigue.png` | **Embarqué** dans German-57 et German-58 · **écarté** pour German-59 |
| Malaise | — | La page n'en cite aucun |

**Le message-clé de la page Ictère** porte sur les *tests hépatiques
perturbés* dans un cadre de maladie chronique : trois de ses cinq messages
traitent du dépistage des hépatites B et C, de l'intervention sur les
habitudes de vie et du suivi conjoint des hépatopathies chroniques. La
vignette est une **hépatite A aiguë chez un homme de 28 ans, de guérison
attendue**. Poser ce panneau affirmerait, avec l'autorité du Compas, un cadre
de chronicité que la station contredit — exactement le cas German-19. Écarté.

**Le message-clé de la page Lombalgies pour German-59** : son deuxième message
est « en l'absence de ces situations, il n'y a pas d'indication aux
radiographies standard ou d'autres imageries ». La vignette est une colique
néphrétique dont le corrigé note **échographie rénale en urgence** et **CT
abdominal**. Le message serait faux au chevet de cette patiente. Écarté, et
c'est le troisième relevé de ce type après German-19 et German-55.

Corollaire vérifié : les deux grilles d'une même page **ne partagent que le
message-clé**. Vérifiable en une ligne — voir le tableau des sélections
ci-dessous.

## Images — sélection, § 8.3 et défauts du vault

| Grille | Images | Poids source | Test dominant |
|---|---|---|---|
| German-53 | classification de l'HTA · critères d'investigation d'une HTA secondaire · diagnostic au cabinet et PEC initiale · **message-clé** | 411 Ko | 1 (grade 2 noté en m1) et 2 (`annexe-dd`) |
| German-54 | HVG à l'ECG · Rx thorax d'OAP · **message-clé** | 587 Ko | 1 (m3 note ECG et Rx) et 3 |
| German-55 | métabolisme de la bilirubine · classification par niveau · algorithme diagnostique | 540 Ko | 1 (a5, m3, m5) |
| German-57 | signaux d'alarme dans les lombalgies · *Rx lombaire (base64 hérité)* · **message-clé** | 467 Ko + hérité | 1 et 2 (ATCD de cancer) |
| German-58 | dermatomes du membre inférieur · **message-clé** | 345 Ko | 1 (e7 nomme les dermatomes) |
| German-59 | drapeaux rouges (colonne « origine non rachidienne ») · algorithme (branche « lombalgie non rachidienne ») | 194 Ko | 3 (piège de la page) |
| German-60 | classification étiologique des syncopes · physiopathologie des voies autonomes · ECG à RR irréguliers | 322 Ko | 2 (`annexe-dd`) et 1 (m5) |

**16 fichiers nouveaux, 2350 Ko au total**, médiane 133 Ko, maximum 310 Ko —
aucun au-delà du plafond du § 8.5 d, aucune grille au-delà du budget de 700 Ko
de source. `rachis-dermatomes-mi.png` était déjà présent (reconnu au sha256,
non réécrit) : l'idempotence de `fetch_image.py` a joué.

**L'arbitrage le plus serré du lot** a porté sur
`rachis-drapeaux-rouges-pour-les-lombalgies-et-lombosciatalgies-aigues.png`,
qui convient à German-58 (colonne « atteinte neurologique », ligne
« radiculopathie irritative ou déficitaire ») **et** à German-59 (colonne
« origine non rachidienne », ligne « douleur non mécanique : … calculs
rénaux … »). Le corollaire du § 8.3 interdisant la double attribution, elle est
allée à German-59, qui n'avait rien d'autre. German-58 reste donc à **deux**
images — le plancher, et le bon résultat au sens du § 8.2.

### Quatre fichiers du vault écartés, et pourquoi

| Fichier | Défaut | Décision |
|---|---|---|
| `rachis-rx-lombaire-profil.jpg` | **PNG 1438×1783 nommé `.jpg`** (`file`), 3 118 Ko | `ÉCHEC [corrompu]`, code 1 — **troisième extension mensongère du corpus** |
| `rachis-test-lasegue.png` | **7 774 Ko** (4928×3736) | Écarté, § 8.5 d — aucune exemption applicable |
| `rachis-test-schober.png` | **1 030 Ko** (1190×890) | Écarté, § 8.5 d |
| `syncope-01-causes-syncopales.jpeg` | **2 472 Ko** (3024×4032) | Écarté, § 8.5 d |

Les deux premiers coûtent cher : la page Lombalgies dessert trois grilles dont
deux notent explicitement le **test de Lasègue** (German-57 e6, German-58 e8,
German-59 e3) et une le **test de Schöber** (German-58 e3). Ce sont les seules
images du corpus qui illustrent des manœuvres nommément notées, et elles sont
inaccessibles pour une raison de poids sans rapport avec leur contenu. Voir
§ « Préoccupations ».

Un critère noté qui **nomme une manœuvre** n'est pas un critère qui **désigne
une image** : l'exemption du § 8.5 d ne s'applique pas. Le point est tranché
ici pour la première fois et mérite d'être consigné.

## Divergences page / corrigé relevées, barème inchangé (niveau 3)

| Grille | Divergence | Traitement |
|---|---|---|
| German-53 | Page SSP : **bithérapie d'emblée** (ESC 2023), monothérapie réservée au sujet âgé fragile et au grade 1 à bas risque · corrigé m7 : « IEC ou ARA2 en première intention », bithérapie si objectif non atteint | Page explicite → niveau 1, le pédagogique suit la page **en la nommant** ; divergence dite dans l'`annexe-theorie` |
| German-53 | Page SSP : **sel < 5 g/j** · corrigé `therapy` : < 6 g/j | Consigné, non corrigé ; le `resume` cite explicitement « repères de la page SSP » |
| German-57 | Page SSP : **myorelaxant (tizanidine) courte période** si contracture · corrigé m5 : « éviter les myorelaxants (risque de chute) » | Le corrigé est propre au terrain de la vignette → niveau 2, le pédagogique n'emporte pas le myorelaxant |
| German-58 | Page SSP : **pas de corticoïde systémique** · corrigé m4 : « corticothérapie orale courte si hyperalgie » | Consigné dans l'`annexe-theorie`, barème inchangé |

## Mesures

| Contrôle | Résultat |
|---|---|
| `report_redundancy.py`, avant et après, sur chacune des 7 | **0 paire nouvelle** — 12 paires arbitrées en cours de rédaction |
| Densité de balisage, 4 conteneurs prescrits | **2 172 spans / 18 475 mots = 1 pour 8,5** |
| Spans hors conteneur | **0** |
| Spans dans `section-longue` / `section-express` | **0** |
| Équilibrage `<div>`, `<span>`, `<li>` sur les 7 | **exact** |
| `check_invariants.py` après re-snapshot | **OK — 88 grilles** |
| Diff baseline champ par champ | `blocks` seul champ modifié · 7 grilles · 0 écart hors champ · **delta purement additif** |
| `check_reachability.py` | **OK — 88/88 à 100 %** |
| `check_nomenclature.py` | **OK** |
| AMBOSS — 3 scripts | **OK — 40 grilles** |
| RESCOS — 3 scripts | **OK — 41 grilles** |
| `fetch_image.py --verify` | **151 images, 0 lien cassé, 0 orpheline** |
| Contrôle visuel | **3 grilles × 2 thèmes × 2 largeurs = 12 rendus, 0 image cassée, 0 débordement** |

Densité par grille : plus dense **1/7,3** (German-53), plus légère **1/10,8**
(German-59). German-59 est la plus légère du lot pour la même raison qu'elle
est la plus courte : sa page ne couvre pas sa vignette, et une section écourtée
offre moins de termes à baliser. C'est une propriété du sourçage, non un défaut
d'application.

Répartition : `c-green` 602 · `c-red` 448 · `c-pink` 404 · `c-blue` 205 ·
`c-yellow` 187 · `c-purple` 148 · `c-amber` 129 · `c-orange` 49.

### Passe d'allègement du balisage

La première rédaction sortait à **1 pour 8,0**, plus dense que les deux lots
précédents (8,9 et 9,5) et plus dense que la grille la plus chargée de p3c
(German-52, 1/8,0). Le motif était identifiable : les longues énumérations
homogènes — douze substances hypertensives en `c-amber`, onze DCI suisses, huit
sérologies en `c-green` — où **chaque item portait la même couleur**.

Règle appliquée mécaniquement aux 7 grilles : dans un `<li>` contenant au moins
cinq spans **tous de la même classe**, seul le premier reste balisé. 25 `<li>`
concernés, 133 spans déballés, densité portée à **1 pour 8,5**. La couleur y
était portée par la liste entière et non par chaque item ; un terme balisé sur
douze d'une même liste n'ajoute aucune information de plus que le premier.

## Contrôle visuel

Chrome `--headless=new`, rendu local `file://`, aucune requête réseau. Trois
grilles retenues : **German-53** (message-clé de 2400 px, huit couleurs
présentes), **German-57** (mélange base64 hérité et images référencées) et
**German-60** (trois JPEG dont un panorama d'ECG de 2121 px).

- Chargement : `complete === true` et `naturalWidth`/`naturalHeight` **égaux aux
  dimensions du vault** pour les douze rendus ; `cassees=0` partout.
- Aucun débordement horizontal : `scrollWidth === innerWidth` à 1200 et 500 px,
  dans les deux thèmes.
- Rapports largeur/hauteur conservés à toutes les largeurs.
- Huit couleurs distinctes dans chaque thème pour German-53 et German-60 ; sept
  pour German-57, qui **ne contient pas de `c-orange`** — absence de contenu, non
  de rendu.
- Copies temporaires supprimées : aucun `_tmpvis-*` dans `git status`.

## Commits

| Hash | Contenu |
|---|---|
| `16a8133` | German-53, 54, 55 + 10 images |
| `933dc45` | German-57, 58, 59 + 4 images |
| `cf04617` | German-60 + 3 images, allègement du balisage des 7, re-snapshot de `baseline.json` |

Index construit **chemin par chemin** avant chaque commit, avec vérification
explicite qu'aucun fichier de `cases/rescos/`, `cases/casecos/`,
`cases/rescos-locales/`, `scripts/rescos/` ou `scripts/casecos/` n'y figurait —
la vérification a mordu : `docs/superpowers/journal-rescos-locales-2026-08.md`
et 37 fichiers `cases/casecos/` et `cases/rescos-locales/` de la session voisine
étaient modifiés dans l'arbre de travail au moment du premier commit. Aucun
`git add -A`. Réaccessibilité des trois commits depuis HEAD vérifiée par
`git merge-base --is-ancestor`.

**Le lot p3c est clos : les 30 grilles German-31 à 60 portent désormais leurs
quatre blocs pédagogiques.**

Rapport détaillé : `.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/p3c-bis-report.md`
