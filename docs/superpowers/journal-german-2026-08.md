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
