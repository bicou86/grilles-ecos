# Refonte pédagogique des 41 grilles ECOS RESCOS — rapport de vérification finale

Branche `refonte-amboss-suisse` · Référence d'origine (outillage rescos en place, avant
toute modification de contenu) : `a82e036` · État vérifié : `1a0a8f6`, **sept commits
RESCOS** plus loin (dix au total : les trois autres relèvent du chantier German mené en
parallèle et ne touchent pas ce corpus) · Journal détaillé :
`docs/superpowers/journal-rescos-2026-08.md` · Procédure :
`scripts/rescos/PROCEDURE-rescos.md`
>
> **Mise à jour r7** — les trois défauts du § 0, mesurés à `0e82963`, ont été réparés.
> Les chiffres des § 0, 2, 6.4 et 6.6 restent ceux de la vérification ; ce que r7 déplace
> est récapitulé dans l'encadré du § 0 et détaillé dans les trois encadrés « Réparé au
> lot r7 ».

> Ce document est le pendant de `docs/superpowers/rapport-amboss-2026-08.md` et de
> `rapport-german-2026-08.md` pour le troisième corpus. Il en reprend la structure. Tout
> ce qui n'y est pas redit — la hiérarchie à trois niveaux, la règle du format, la règle
> anti-perte — reste valable tel quel.

---

## 0. Résultat des vérifications

Six vérifications ont été menées sur l'ensemble du corpus, et les quatre vérificateurs
d'AMBOSS rejoués pour établir que la campagne RESCOS n'a rien perturbé chez le voisin.
**Les six passent. Trois défauts avaient été signalés ci-dessous ; le lot r7 les a tous
les trois réparés** — le corps de chaque défaut est conservé tel qu'il a été rédigé à la
vérification, suivi d'un encadré « Réparé au lot r7 ».

> **État au lot r7 (réparation des trois défauts).** Les chiffres du présent § 0 et des
> § 6.4 / 6.6 sont ceux de la vérification, à `0e82963`. Ce que r7 a déplacé, et rien
> d'autre :
>
> | | vérification (`0e82963`) | après r7 |
> |---|---|---|
> | redondance inter-blocs | 131 | **127** |
> | dont paires `redflags` | 5 | **3** |
> | chargement sans exception ni erreur de console | 39/41 | **41/41** |
> | score remonté au registre du tableau de bord | 39/41 | **41/41** |
> | `configForm` = `caseConfig` | 39/41 | **41/41** |
> | AMBOSS, témoin | 147 | **147** |
>
> Total à 100 %, note A, minuteur : **41/41 avant comme après**. Le barème n'a pas bougé
> d'un point.

| # | Vérification | Résultat |
|---|---|---|
| 1 | Les vérificateurs, sur RESCOS et sur AMBOSS | **OK** — RESCOS : invariants, nomenclature, atteignabilité au vert, `boundsAnomalies` et `uncoveredContent` vides sur les 41. AMBOSS : quatre vérificateurs au vert, redondance **147**, inchangée |
| 2 | Barème inchangé depuis `a82e036` | **OK** — 328 champs recomparés de part et d'autre sur les 41 grilles. **Huit divergences, toutes admises** : quatre champs sur RESCOS-12, quatre sur RESCOS-13, dont la section vide a perdu son coefficient. Les 320 autres sont identiques |
| 3 | Intégrité structurelle | **OK** — balises appariées 41/41, `</html>` final 41/41, blocs conformes au gel 41/41. Les **52 crochets `[…]` des 40 segments `cloture`** (13 grilles) sont intacts, nombre pour nombre |
| 4 | Redondance | **OK** — 610 → **131** paires inter-blocs (−78 %), 323 → **210** intra-bloc. **124 des 131** relèvent du plancher structurel ou du contrat `therapy`/`redflags` ; **7 sont des faux positifs de polarité**, et une grille concentre à elle seule une redondance qui n'est ni l'un ni l'autre (§ 6.4) |
| 5 | Non-perte d'information | **OK** — 485 items signalés sur 39 grilles, analysés par motifs. **Un seul résidu réel**, mineur (§ 6.5) |
| 6 | Contrôle fonctionnel en navigateur | **OK** — 41/41 grilles remplies intégralement dans Chrome sans interface : total à 100 %, 157 sections au maximum, 1 627 crochets colorés sur 1 627, aucune balise orpheline. **RESCOS-12 et RESCOS-13 atteignent bien 100 %** ; RESCOS-7 et RESCOS-9 aussi, **mais elles lèvent une exception JavaScript à chaque calcul** (§ 0, défaut 1) |

### Défaut 1 — RESCOS-7 et RESCOS-9 embarquent un moteur de calcul périmé, et il plante

**C'est le seul défaut technique du corpus, il est préexistant, et il n'a rien à voir avec
la refonte.** Il est identique à `a82e036` et n'a été introduit par aucun commit de la
campagne.

Ces deux grilles sont les seules du projet à ne pas charger `cases/scoring.js` : elles
embarquent chacune leur **propre copie** de `calculateScores()`. Cette copie est figée sur
une version du moteur **antérieure à deux corrections** que le fichier partagé porte
aujourd'hui :

| | `cases/scoring.js` | copie embarquée de RESCOS-7 et RESCOS-9 |
|---|---|---|
| garde sur `#missingItems` | `var missingEl = …; if (missingEl) …` | `document.getElementById("missingItems").style.display = …`, **sans garde**, dans les deux branches |
| `saveToRegistry(globalPercentage, isStarted)` | présent | **absent** |

Or dans ces deux fichiers le bloc `<div id="missingItems">` est **commenté** dans le HTML
(« ÉLÉMENTS MANQUANTS (MASQUÉS) »). L'élément n'existe donc pas, et
`document.getElementById("missingItems")` rend `null`. Résultat :

```
EXCEPTION TypeError: Cannot read properties of null (reading 'style')
    at calculateScores (…/RESCOS-7_-_BBN_-_Grille_ECOS.html:896:56)
```

**L'exception est levée à chaque appel** — au chargement de la page, puis à chaque clic sur
une case ou un bouton, quelle que soit la branche empruntée (les deux déréférencent
`null`). Elle interrompt le gestionnaire `DOMContentLoaded` juste avant
`colorPatientResponses()`.

**Ce que cela ne casse pas, et pourquoi.** Le score est écrit avant le point de rupture :
les deux grilles affichent bien leurs sections au maximum et **100 %, note A**, ce que le
contrôle fonctionnel confirme. La coloration des crochets est rattrapée par un appel de
secours placé en fin de page (`if (window.colorPatientResponses) { … }`, « forcer la
coloration finale »), indépendant du gestionnaire : les 41 crochets de RESCOS-9 sont bien
colorés, et RESCOS-7 n'en porte aucun. **Un candidat ne voit rien.**

**Ce que cela casse.** Une exception est jetée dans la console à chaque interaction ; le
redimensionnement automatique des zones de commentaire au chargement ne s'exécute pas ; et,
indépendamment de l'exception, ces deux stations **ne remontent jamais leur score au
registre du tableau de bord**, puisque leur copie du moteur ne connaît pas
`saveToRegistry`.

La préoccupation n° 7 du volet r2 annonçait ce risque au futur — « toute correction future
de `scoring.js` devra être reportée à la main dans ces deux fichiers ». **La divergence
n'est pas future : elle est déjà là, et elle plante.** Le champ `configForm`, gelé au
snapshot depuis r1, signale que ces deux grilles ont un autre moteur ; il ne dit pas que ce
moteur est en retard.

> **Réparé au lot r7 — les deux grilles chargent `cases/scoring.js`.**
>
> Le diagnostic ci-dessus sous-estimait l'écart. Le `diff` des deux copies contre le
> fichier partagé montre qu'elles sont **en retard de six choses**, pas de deux : la garde
> `if (missingEl)`, l'appel **et la définition** de `saveToRegistry()`, le chargeur
> dynamique de `srs.js`, la détection du mode circuit, `createNavBar()` et
> `createCircuitNav()`. En mode circuit, ces deux stations ne posent aucune barre de
> navigation et ne reviennent jamais à `exam.html`.
>
> Le même `diff` établit aussi que **les deux copies sont identiques entre elles et
> identiques au fichier partagé** partout ailleurs : le seul `+` est le bloc de
> configuration et un `isNewFormat = true` mort (déclaré, jamais lu — vérifié). Ce n'est
> pas une variante à préserver, c'est une fourche périmée. Reporter deux corrections y
> aurait laissé les quatre autres régressions vivantes **et le mécanisme de dérive
> intact**.
>
> Les deux blocs `<script>` ont donc été remplacés par la forme des 39 autres grilles : un
> `window.caseConfig` déclaratif suivi de `<script src="../scoring.js">`. La transcription
> est exacte — `maxScores` / `coef` / `sectionInfo` sont les trois seuls champs que
> `scoring.js` lit, et les lignes `scores["…"] = 0` de la forme impérative sont redondantes
> (`scoring.js` réinitialise puis écrase par section). RESCOS-7 : `communication` 30, coef
> 1, 15 critères, **sans `isComm`** — ses boutons sont numériques, pas l'échelle A–E ; la
> forme impérative ne le déclarait pas davantage. RESCOS-9 : `anamnese` 41 / coef 0,7 /
> 14 critères, `management` 15 / coef 0,3 / 6 critères.
>
> **Conséquence sur le gel.** `configForm` passe de `inline` à `caseConfig` sur ces deux
> grilles ; `baseline.json` a été régénéré. La régénération **ne déplace que ces deux
> champs** — `criteriaCount`, `detailCount`, `radioCount`, `checkboxCount`,
> `sectionCounts`, le nombre de segments par bloc, `boundsAnomalies` et `uncoveredContent`
> sont identiques sur les 41. C'est la preuve la plus directe que l'échange a touché le
> moteur et rien du contenu ni du barème.
>
> `check_reachability.py` lit désormais ces deux grilles par sa branche `caseConfig` et
> rend toujours 41/41 à 100 %. Contrôle de morsure : `maxScores.anamnese` de RESCOS-9 forcé
> à 40 → le vérificateur crie `ECART · atteignable=41 maxScores=40 affiché=/41`. La
> transcription est donc vérifiée, pas supposée.
>
> **En navigateur** (même harnais qu'au § 6.6, comparaison avant/après sur un miroir de
> `0e82963`) :
>
> | | avant (`0e82963`) | après r7 |
> |---|---|---|
> | RESCOS-7 · exceptions | **16** | **0** |
> | RESCOS-9 · exceptions | **51** | **0** |
> | RESCOS-7 · `ecos_registry` après remplissage | **absent** | `{pct: 100, grade: "A", best: 100, date: …}` |
> | RESCOS-9 · `ecos_registry` après remplissage | **absent** | `{pct: 100, grade: "A", best: 100, date: …}` |
> | total / note / minuteur | 100 %, A, 13:00 → 12:58 | inchangé |
>
> `ecos_registry` n'est écrit qu'à un seul endroit du projet — `cases/scoring.js:804`,
> dans `saveToRegistry()`. L'apparition de ces deux entrées ne peut donc venir que du
> chargement du moteur partagé.
>
> La commande de détection de l'annexe **rend maintenant 0**, sa valeur attendue.

### Défaut 2 — RESCOS-15 concentre une redondance qui n'est pas du plancher structurel

**14 des 131 paires résiduelles du corpus sont dans cette seule grille**, et **11 d'entre
elles** tournent autour de **trois items seulement** : « modification récente du transit
après 50 ans » (7 paires), « alternance diarrhée / constipation » (3) et « perte de poids
inexpliquée » (1).

Le premier figure dans `redflags` (bloc **noté**), dans `expert`, dans `annexe-dd` — et
**deux fois** dans `presentation` : une fois recopié mot pour mot sous la sous-section
« 👉 Signes d'alarme (Red Flags) », une seconde fois comme clé `N` du mnémo SANG. Soit cinq
énoncés du même signe d'alarme dans une même grille.

Ce n'est pas le plancher structurel — un signe cardinal que chaque bloc doit nommer *par sa
fonction*. C'est une **recopie verbatim du bloc noté dans une sous-section de
`presentation` dont le rôle est le mnémo**, alors que le mnémo de la même sous-section
porte déjà l'information. La règle du pilote (« une paire dont un côté est `therapy` ou
`redflags` n'est pas une redondance à retirer ») la protège de fait, et le lot r4a l'avait
signalée en demandant un arbitrage (§ 8.2 de son rapport). **L'arbitrage n'a jamais eu
lieu**, et les trois lots suivants ont appliqué la règle telle qu'écrite.

> **Réparé au lot r7 — la recopie a été réduite, les blocs notés n'ont pas bougé.**
>
> L'arbitrage a en réalité été rendu **pendant** la campagne, au geste 4 du lot r4b
> (« réduction des recopies de `therapy` dans `presentation` », appliqué à RESCOS-25, 26
> et 28) — mais après le traitement de RESCOS-15, qui ne l'a donc jamais reçu. Sa teneur :
> les blocs notés restent intouchables, **seule leur recopie dans `presentation` se
> réduit**.
>
> Appliqué ici à la seule sous-section fautive,
> `presentation` / Touches ludiques / « 👉 Signes d'alarme (Red Flags) », qui recopiait mot
> pour mot les cinq `redflags-text` du bloc noté. Elle est **réduite, pas supprimée** :
> trois lignes organisées par mécanisme (saigner — boucher — retentir) remplacent les cinq
> libellés recopiés. C'est aussi un retour au format de la section : les
> `presentation-subsection` de « Touches ludiques » du corpus sont des **mnémos**, et
> RESCOS-15 était la seule des six grilles à `redflags` à y loger une seconde copie du bloc
> noté.
>
> Intouchés, comme prescrit : `redflags`, `expert`, `annexe-dd`, et la clé `N` du mnémo
> SANG (« Nouvelle modification du transit après 50 ans »), protégée par la règle du
> format.
>
> **Effet mesuré** : RESCOS-15 passe de 14 à **10 paires**, le corpus de 131 à **127**, les
> paires `redflags` du corpus de 5 à **3** (celles qui restent ont pour second côté `expert`,
> `annexe-dd` ou la clé de mnémo — toutes hors du périmètre de l'arbitrage). Les quatre
> paires retirées sont exactement les quatre attendues, et **aucune paire nouvelle
> n'apparaît**, ni dans cette grille ni ailleurs.
>
> **`check_no_loss.py` signale un item disparu, et c'est un faux positif** :
> « occlusion arrêt gaz selles distension ». La ligne de remplacement dit « Boucher → arrêt
> des matières et des gaz, ventre distendu » — le comparateur ne reconnaît pas le voisinage
> morphologique parce que la reformulation change deux mots sur quatre. Et l'énoncé
> subsiste **verbatim dans le bloc noté**, non modifié : « 3. Occlusion intestinale — Arrêt
> matières et gaz = urgence chirurgicale potentielle ». Aucune information ne sort de la
> grille.

### Défaut 3 — une réduction partielle non rattrapée dans RESCOS-35

Le `presentation`/Q3 « Suivi » de RESCOS-35 portait « Prévention secondaire : arrêt tabac,
activité physique adaptée ». Le passage au registre oral a conservé le tabac (« et je
reprendrais le tabac avec elle ») et **perdu l'activité physique adaptée**, qui n'existe
plus nulle part dans la grille comme prescription — seulement dans le script de la patiente,
où « activité physique : sédentaire » décrit son habitude.

C'est le seul résidu que l'analyse par motifs de la vérification n° 5 ait laissé, sur
485 items signalés. Il va vers le sous-traitement, il est mineur, et il relève de la
tolérance « fusion » que les lots se sont donnée — mais c'est bien une information sortie
du corpus.

> **Réparé au lot r7 — restauré dans `presentation`, en registre oral.**
>
> Le bloc que le contrat désigne est `presentation` : l'item est la **réponse orale à la
> question Q3 « Suivi » de l'examinateur**, et c'est très exactement l'endroit d'où la
> réécriture l'avait fait tomber. RESCOS-35 ne porte d'ailleurs ni `therapy`, ni
> `redflags`, ni `annexe-dd` — ses seuls blocs sont `resume`, `expert`, `theorie`,
> `presentation` et `scenario`.
>
> La fin de la réponse Q3 passe de « … et je reprendrais le tabac avec elle. » à « … et je
> reprendrais avec elle la prévention secondaire : l'arrêt du tabac, et la reprise d'une
> activité physique adaptée à son âge et à son état. » La prescription perdue est de
> nouveau dans la grille, et le mot « prévention secondaire » qui la portait aussi.
>
> Aucune paire de redondance nouvelle : la seule autre occurrence d'« activité physique »
> de la grille est « Activité physique : sédentaire » dans le `scenario`, qui décrit
> l'habitude de la patiente et que `report_redundancy.py` exclut par défaut.

---

## 1. Ce qui a été fait

Les 41 grilles ont été balayées, **39 modifiées**. Le travail a porté sur les blocs
pédagogiques — `resume`, `expert`, `theorie`, `presentation`, un `cloture-content` — et
jamais sur la structure des sections notées ni sur les deux blocs de niveau 2 qui y vivent
(`therapy`, `redflags`), dont **aucun n'a subi la moindre modification de contenu**.

Les deux grilles intactes sont **RESCOS-8** (rien à traiter dans le périmètre) et
**RESCOS-11**, qui ne porte aucun bloc pédagogique du tout.

### Chiffres

| Mesure | `a82e036` | `1a0a8f6` |
|---|---|---|
| Termes de nomenclature non suisses | **111** | **0** |
| Acronymes anglophones substitués | — | **56** au balayage exhaustif (26 grilles), plus **10** microbiologiques et quelques corrections incidentes |
| Numération en unité implicite | 1 | **0** |
| Paires quasi identiques **entre** blocs | **610** | **131** (−78 %) |
| Paires quasi identiques **dans** un même bloc | **323** | **210** (−35 %) |
| Idem, restreint aux cinq blocs que mesure AMBOSS | **578** | **113** |
| Réponses Q/R en liste (`presentation-reponse list`) | **61** | **8** |
| `mnemo-box` | 28 | 25 |
| Items de contenu, tous blocs | 6 628 | 6 117 |
| Volume rédactionnel des blocs | 518 901 c. | 534 699 c. (**+3,0 %**) |
| Segments de bloc | 313 | **313** — aucun bloc créé ni supprimé |
| Trous du bloc canonique comblés | — | **20** |
| Grilles au barème atteignable à 100 % | 39 / 41 | **41 / 41** |

Volume de diff : 718 lignes ajoutées, 1 696 supprimées dans `cases/rescos`, sur 39 fichiers.

### Ce que cela change pour qui révise

**La fiche de révision et la restitution orale ne se recopient plus.** `presentation` était
impliquée dans 440 des 610 paires de départ : le bloc recopiait mot pour mot `annexe-dd`
(arguments POUR/CONTRE), `resume` (listes d'examens et de traitements) et `theorie`. Le
levier n'a presque jamais été la suppression : les 61 réponses Q/R écrites en `<ul>` sont
tombées à 8, et le **volume rédactionnel a augmenté de 3 %** pendant que le nombre d'items
baissait de 511 — la signature d'un passage de la liste à la phrase parlée. Ce que le
candidat lit dans « Version longue » est maintenant ce qu'il dirait, pas une liste qu'il
relirait.

**`annexe-dd` n'a presque pas bougé.** C'est l'inverse du réflexe German. Le bloc de
différentiels de RESCOS est riche et sain — 92,2 % de formulations distinctes, 139 entrées
sur 139 portant la flèche « → examen qui départage » — au niveau d'AMBOSS et de German
*après* nettoyage. La passe de suppression de remplissage de German (`prune_dd_filler.py`)
n'a délibérément pas été rejouée ici : il n'y avait rien à retirer.

**Vingt trous du bloc canonique ont été comblés.** Ce sont des **ajouts**, pas des
suppressions : des informations que la section notée et `presentation` portaient toutes deux
sans que la fiche de révision les porte. Le détail est au § 3.

**Le vocabulaire est suisse.** 104 `NFS` sont devenues `FSC` ; les valeurs en unités non SI
ont été converties analyte par analyte, avec le facteur propre à chacun (hémoglobine ×10,
leucocytes ÷1000, LDL ÷38,67) ; une numération sans unité a reçu la sienne. Puis les
acronymes anglophones ont été traduits, du `gold standard` (15 occurrences) au `BMI`
(16 occurrences, alors que RESCOS-18 écrivait `BMI` et `IMC` **dans la même ligne
d'en-tête**).

**Le barème n'a bougé que là où il devait.** 328 champs recomparés de part et d'autre de
l'historique sur les 41 grilles. **Huit champs divergent — quatre sur RESCOS-12, quatre sur
RESCOS-13 — et ce sont exactement les huit de la correction du § 2.** Les 320 autres sont
identiques au bit près.

---

## 2. Les trois bugs de barème du projet

Trois corpus, trois manières différentes pour un barème de mentir sur ce qu'il déclare.
Celui-ci est le troisième et le plus subtil.

### AMBOSS-9 — plus de points déclarés qu'il n'en existe

La configuration déclare treize critères d'anamnèse (`count: 13`) et un maximum de
53 points. Le critère `a13` n'existe nulle part dans la page. Les douze critères réels
totalisent 49 points. La section affiche « Score : 49/53 » **tout coché**, et la station
plafonne à 98 %.

Défaut préexistant, présent dès la première version du fichier dans git. Non corrigé : il
vit dans la configuration de notation, gelée par consigne.

### German — aucun

88 grilles, 880 champs de barème recalculés de part et d'autre : zéro divergence, zéro
inatteignabilité. Le corpus German n'a pas ce genre de défaut.

### RESCOS-12 et RESCOS-13 — une section vide qui garde son quart de coefficient

**Les deux grilles (« Crise de panique », « Dépression ») déclarent une section Examen
clinique vide — `count: 0`, `maxScores.examen: 0`, « Score : 0/0 », aucun critère `e*` dans
la page — tout en lui laissant son coefficient de 0,25.**

`cases/scoring.js` calcule le pourcentage d'une section par
`max > 0 ? (score / max) * 100 : 0`, puis l'ajoute à la note globale pondéré par son
coefficient. Pour une section vide, la première expression vaut **0 quoi que fasse le
candidat**, et sa part de coefficient est perdue sans que rien ne le dise.

**Conséquence : une copie parfaite plafonnait à 75 %, note C.** Deux stations de
psychiatrie où l'examen physique n'a pas lieu d'être — c'est précisément pour cela que
la section est vide — punissaient d'un quart de la note tous les candidats, sans exception
et sans recours.

**Pourquoi les vérificateurs hérités ne pouvaient pas le voir.** Les trois écarts de barème
qu'AMBOSS avait appris à détecter portent tous sur une **incohérence entre deux nombres** :
un `count` plus grand que le nombre de critères présents, un sous-item orphelin, un
`maxScores` divergeant du `<span class="score">` affiché. Ici les trois nombres de la
section vide sont **d'accord entre eux** : `count: 0`, `maxScores: 0`, dénominateur affiché
`0`. Le contrôle passe sans bruit, section par section, parce qu'il n'y a rien à comparer.

Le défaut n'est visible **que par le total global**, et seulement si l'on sait que 75 % est
anormal — un vérificateur qui lit « global : 75 % » sans cause n'a aucune raison de
s'alarmer, beaucoup de grilles ont des sections imparfaites. C'est pourquoi
`empty_weighted_sections()` a été ajouté à `check_reachability.py` : il **nomme** le cas au
lieu de laisser lire un pourcentage sans explication.

**La correction.** Le coefficient a été redistribué **à parts égales** sur les trois
sections restantes (`0.3333333333333333` ×3, dont la somme vaut exactement 1,0 en IEEE 754),
et non au prorata des points. Trois raisons, toutes mesurées :

1. **Le corpus pondère à égalité, indépendamment des points.** Les 39 grilles à `caseConfig`
   portent une seule distribution, `0.25` ×4, sans exception — alors que leurs `maxScores`
   varient du simple au sextuple entre sections. Sur les 81 grilles des deux corpus outillés,
   **80 pondèrent à égalité** ; la seule exception, RESCOS-9, porte `0.7 / 0.3` pour 41 et
   15 points, et non le `0.732 / 0.268` qu'aurait donné le prorata. **Aucun coefficient du
   projet n'est dérivé de ses points.**
2. **`scoring.js` est écrit pour que le nombre d'items ne pèse pas** : il normalise chaque
   section en pourcentage *puis* applique le coefficient. Un prorata réintroduirait
   exactement la quantité que le moteur neutralise.
3. **Le prorata rendrait les deux grilles incomparables** : l'anamnèse vaudrait 63 % dans
   RESCOS-12 et 46 % dans RESCOS-13, pour la seule raison que la seconde a plus de critères
   de management.

**Un geste d'affichage était indispensable en plus.** Retirer `examen` de `sectionInfo` la
retire du *calcul*, pas de la *page* : son `<div class="section">` est du HTML statique et
`scoring.js` ne masque aucune section. Sans ce second geste, la grille corrigée aurait
continué d'afficher « Examen clinique (25%) — Score : 0/0 » et une tuile « 0 % » devenue
**morte** — plus mise à jour par personne, donc figée à 0 % à vie. Un étudiant y aurait lu
la perte d'un quart de sa note : exactement le malentendu que la correction supprime. Ont
donc été retirés le dénominateur nul, la tuile de pourcentage et l'en-tête de tableau
orphelin ; l'intitulé est devenu « **Examen clinique — section non cotée** ». La section
et son encadré de commentaire restent visibles : l'examinateur peut vouloir consigner
l'absence d'examen physique.

**Et un trou d'outillage a été fermé au passage.** `coef` gouverne la note globale sans être
reflété par aucun autre champ gelé. `check_reachability.py` exige que le total tombe sur
100 %, donc il rattrape toute valeur qui **casse la somme** — mais pas une redistribution
qui la **conserve**. Vérifié expérimentalement : une copie de RESCOS-12 dont `coef` passe de
trois tiers égaux à `{0.5, 0.25, 0.25}` change la note de toutes les copies et reste
**verte**. `coef` est désormais gelé au snapshot, sur RESCOS **et** sur AMBOSS. C'est
`sectionInfo[].count` d'AMBOSS-9 rejoué sur un autre champ.

> Le même geste reste à faire sur `scripts/german/`. Il n'a pas été engagé : l'utilisateur
> travaille dans cet arbre.

---

## 3. Les erreurs médicales trouvées

Regroupées par nature. Toutes ont été corrigées dans les blocs pédagogiques, aucune dans
une section notée.

### A. L'omission qui fait faire un geste délétère

C'est la famille la plus lourde, et elle est spécifique : l'information manquante ne conduit
pas à **oublier** un traitement, elle conduit à en **administrer un qui nuit**.

| Grille | Ce qui manquait au bloc canonique | Pourquoi c'est grave |
|---|---|---|
| **RESCOS-6** | l'acide tranexamique doit être donné **dans les 3 heures** suivant le traumatisme | au-delà de la troisième heure, il **aggrave la mortalité**. `resume` disait « si hémorragie active », sans délai ; la fenêtre n'existait que dans une puce de `presentation`/Touches ludiques |
| **RESCOS-38** | dépistage d'une **tuberculose latente** avant l'introduction d'un anti-TNF, et sérologies B / C / VIH | un anti-TNF sur une tuberculose latente non traitée la réactive. Absent de la grille entière |
| **RESCOS-38** | **tératogénicité** du méthotrexate, chez une patiente de **45 ans** | contraception obligatoire, et arrêt avant conception. Absent de la grille entière |
| **RESCOS-32** | **jamais d'anesthésique local répété** sur un ulcère de cornée | le collyre anesthésique délivré pour calmer la douleur retarde la cicatrisation et peut mener à la fonte cornéenne. Absent de la grille entière |
| **RESCOS-28** | infiltrations de corticoïdes : **3 par an au maximum** | `resume` écrivait « Infiltrations intra-articulaires (corticoïdes ou acide hyaluronique) » sans aucune limite de fréquence, alors que le bloc **noté** dit « max 3/an ». La répétition accélère la chondrolyse |

Trois de ces cinq — TB latente, tératogénicité, anesthésique cornéen — n'existaient **nulle
part** dans leur grille, ni dans le noté, ni dans le pédagogique. Elles ont été trouvées au
niveau 1, par lecture de la page SSP correspondante.

### B. La valeur chiffrée fausse

| Grille | L'erreur | Ce qu'elle produit |
|---|---|---|
| **RESCOS-26 et RESCOS-27** | `resume` fixait la cible LDL à « **< 0,55 mmol/L** si haut risque » | 0,55 est la valeur **en g/L** portée avec l'unité mmol/L : une cible **dix fois trop basse**, et inatteignable. Corrigée à 1,4 mmol/L sur autorité de deux pages SSP explicites |
| **RESCOS-36 et RESCOS-37** | « LDL < 1,8 mmol/L, voire < 1,4 si haut risque » | **les deux strates sont inversées.** 1,4 est la cible du **très haut risque**, auquel une coronaropathie documentée appartient d'emblée ; 1,8 est celle du haut risque. La phrase donnait comme cible principale une valeur trop haute |
| RESCOS-9b | « hyperleucocytose (> 12 000/mm³) » | unité américaine ; convertie en `> 12 G/L`, ce qui aligne les trois écritures de la même grille |
| RESCOS-3 | « plaquettes 422 » | numération sans unité, à lire 422 G/L. Unité rendue explicite |

L'erreur de RESCOS-26/27 est le type de faute qui ne se voit pas : une phrase clinique
fausse se remarque, un nombre faux ne se remarque pas. Elle conduit soit à surdoser, soit à
conclure à un échec thérapeutique là où l'objectif est atteint.

### C. La conduite du traitement de fond, incomplète

| Grille | Ce qui manquait |
|---|---|
| RESCOS-38 | **acide folique** avec le méthotrexate, et sa posologie |
| RESCOS-38 | corticothérapie **< 10 mg/j**, protection gastrique, prévention de l'ostéoporose cortico-induite |
| RESCOS-34 | colchicine **pendant 3 mois** — `theorie` donnait la dose sans la durée |
| RESCOS-27 | posologie de la rééducation : **3×/sem, 30-60 min, ≥ 3 mois** |
| RESCOS-27 | **3 à 6 mois** de traitement bien conduit avant de poser l'indication de revascularisation |
| RESCOS-28 | chirurgie **après 6 mois**, durée de vie de la prothèse **15-20 ans**, canne **du côté opposé** |
| RESCOS-26 et 27 | **IEC / sartan en protection vasculaire**, distincte du contrôle tensionnel |
| RESCOS-14 | arrêt des AINS, réhydratation, **prophylaxie thromboembolique** (la MICI en poussée hospitalisée est un état prothrombotique) |
| RESCOS-36 | activité physique **30 min/j** |
| RESCOS-34 | en tamponnade, la **vitesse** d'installation prime le volume ; ni diurétique ni dérivé nitré |

### D. Le protocole non suisse

**RESCOS-9b** prescrivait « céfotaxime + oxacilline (ou vancomycine si MRSA) » dans
l'arthrite septique de l'enfant — protocole franco-américain. La page
`SSP — Boiterie de l'Enfant` nomme « céfuroxime / Co-Amoxi-Mepha® IV selon l'âge », et **la
section notée était muette** (« Antibiothérapie intraveineuse après prélèvements »). Sans le
niveau 1, rien n'aurait tranché. `MRSA` est devenu `SARM` au passage — `check_nomenclature`
ne le voyait pas, il n'était pas dans la table.

### E. Les divergences de fond, internes ou par excès

| Grille | La divergence | Tranchée par |
|---|---|---|
| RESCOS-21 | « Éradication *H. pylori* systématique » | la section **notée** disait « si positive ». Corrigé en « recherche sur les biopsies, éradication si positive » — l'erreur allait vers le sur-traitement |
| RESCOS-9b | durée d'antibiothérapie : « ~3-4 semaines » dans `resume`, « 3-6 » dans `theorie` et `presentation` | le contrat : `resume` est canonique. Les deux autres alignés, en conservant la raison de l'écart (« plus longue si ostéomyélite associée ») |
| RESCOS-9b | tableau âge ↔ cause, ligne 0-3 ans | la page SSP nomme la **fracture sur maltraitance** ; le tableau du canonique, qui transcrit précisément cette mnémonique, ne la portait pas. Cas d'espèce : enfant de 2 ans, sept jours de boiterie avant consultation |
| RESCOS-15 | prise en charge de la forme **occlusive** en urgence ; **endoscopie haute si méléna** | absentes de `resume`, présentes dans le noté et dans `presentation` |
| RESCOS-3 | dépistage de l'**anévrisme aortique thoracique** après une artérite à cellules géantes | complication tardive classique, absente du canonique |
| RESCOS-14 | **β-hCG** chez la femme en âge de procréer, avant corticoïdes puis immunosuppresseurs | niveau 1, `SSP — Diarrhée` |
| RESCOS-18 | seuil échographique **> 3 mm** de la paroi vésiculaire | présent dans `theorie`, absent du canonique |
| RESCOS-31 | « hydratation abondante » de la colique néphrétique | la page SSP dit « **pas d'hyperhydratation forcée** » — sens corrigé |

---

## 4. Ce qui reste non corrigé, et pourquoi

### 4.1 Deux blocs **notés** prescrivent un geste discutable

Les blocs notés sont intouchables par consigne. Deux d'entre eux demandent un geste que la
page de référence contredit ou n'encadre pas.

**RESCOS-31 — un AINS et une restriction hydrique au même patient déshydraté.** Le bloc
`therapy`, noté, prescrit « kétoprofène 100 mg IV » **et** « restriction hydrique pendant la
crise (500 mL/24 h) » chez un sportif dont la section notée de la même grille relève
« déshydratation relative » et « hydratation habituelle insuffisante ». La page SSP dit
« pas d'**hyper**hydratation forcée » — ce qui n'est pas la même consigne — et
contre-indique les AINS sur rein hypoperfusé. Le raisonnement a été porté dans `theorie`,
seul bloc pédagogique de cette grille ; le bloc noté n'a pas été touché.

**RESCOS-28 — des infiltrations dont le plafond ne suit pas.** Le bloc `therapy`, noté,
prescrit des infiltrations intra-articulaires de corticoïdes **avec** la mention « max 3/an ».
Le `resume` ne la portait pas ; il a été corrigé (§ 3.A), et l'`expert` la porte aussi.
**Mais la grille nomme les infiltrations neuf fois en tout, et seules trois de ces
occurrences portent le plafond.** Les six autres — la check-list rapide, le mnémo HANCHO,
trois réponses orales de `presentation`, une ligne de `theorie` — écrivent « antalgiques,
infiltrations, chirurgie » sans limite de fréquence. Un candidat qui révise par le mnémo ou
par la version orale ne rencontre jamais le plafond, alors que la répétition des
infiltrations cortisoniques accélère la chondrolyse.

Ce n'est pas réparable dans le périmètre : porter le plafond dans les six mentions
restantes créerait exactement la redondance que la campagne a passé quatre lots à réduire,
et l'omettre laisse un enseignement incomplet. **C'est le point où le contrat de rôle des
blocs et la sécurité du contenu tirent dans deux directions opposées**, et il mérite un
arbitrage propre.

**Avec RESCOS-31, ce sont les deux seuls endroits du chantier où le patron produit un
désaccord qu'il s'interdit de réduire.**

### 4.2 L'écart noté ↔ SSP sur la cible LDL de RESCOS-26 et RESCOS-27

Leurs blocs `therapy`, **notés**, prescrivent « LDL < 0,7 g/L », soit 1,8 mmol/L — l'ancienne
cible « haut risque ». Les deux pages SSP disent 1,4 mmol/L, et l'AOMI symptomatique relève
du **très haut risque**. Le noté est en retard d'une révision de recommandation.

Le `resume` a été corrigé à 1,4. **Résultat : `resume` et `therapy` de la même grille portent
maintenant deux cibles différentes, et c'est l'attendu noté qui est le moins à jour.**

Le lot r4b craignait un défaut de corpus ; la vérification menée au lot r4c l'a réfuté dans
les deux sens. **RESCOS-36 porte la bonne valeur dans son bloc noté** (`0.55 g/L`, soit
1,42 mmol/L, exactement la cible du très haut risque) et **RESCOS-37 n'a aucun bloc
`therapy`**. L'arbitrage à rendre — ouvrir le barème à la correction d'une valeur chiffrée
dans un `therapy` quand une page SSP explicite la contredit — porte donc sur **deux
occurrences**, pas sur un défaut de corpus.

### 4.3 `annexe-expert` n'est pas normalisé

**Quatre lots consécutifs l'ont signalé.** AMBOSS respecte exactement le triptyque
« Rôles et interventions / Points clés / Pièges » : 40 × 3 = 120 sections, **3 intitulés
distincts**. RESCOS porte 118 sections pour **18 intitulés distincts** — Points clés 35,
Pièges 33, et « Rôles et interventions » seulement **26** sur 39. Les treize autres ont des
intitulés ad hoc : Techniques Examen, Critères Diagnostiques, Compétences Clés, Erreurs
Courantes, Protocole SPIKES, Matériel Nécessaire, Points Critiques, Rôles et interventions
(avec minuscule)…

Non renommés, et pour une raison constante d'un lot à l'autre : le geste est **cosmétique**,
sans effet sur la redondance, et une normalisation de corpus faite grille par grille au fil
du dédoublonnage serait irrégulière — elle mérite sa propre passe et son propre arbitrage.

### 4.4 RESCOS-11 est vide de tout bloc pédagogique

**Seule grille du corpus sans aucun bloc de contenu** : ni `annexes`, ni `annexes-grid`, ni
`resume`, ni aucune fiche. Quatre sections notées normales, barème atteignable, `<div>`
équilibrés. C'est une grille d'évaluation nue ; c'est aussi la seule pour laquelle
`peda_bounds()` rend `(-1, -1)`.

Elle n'a pas été modifiée : il n'y avait rien à dédoublonner. **Tout son volet pédagogique
est à créer**, ce qui est un travail de rédaction et non de refonte.

Trois autres grilles sont incomplètes sans l'être autant : **RESCOS-6** et **RESCOS-29**
(très partielles), **RESCOS-26** (sans `annexe-theorie`).

### 4.5 Les autres points laissés ouverts

- ~~**Les défauts 1, 2 et 3 du § 0**~~ — **réparés au lot r7** ; voir les encadrés
  « Réparé au lot r7 » du § 0.
- **RESCOS-3, ligne du bilan de Horton** : « VS 55 », « CRP 32 » et « Hb 113 » restent sans
  unité. Ce ne sont pas des numérations d'hémogramme et aucun contrôle ne les couvre.
- **Les défauts d'import mesurés, non corrigés** : 88 chevrons nus (seuils légitimes, piège
  d'outillage et non défaut de contenu — **96 avant r7** ; les huit qui manquent à l'appel
  étaient des opérateurs de comparaison JavaScript des deux moteurs embarqués supprimés,
  `i <= section.count` et `currentSeconds <= 30`, comptés parce que ce rapport balaye le
  HTML brut, `<script>` compris), 12 comparaisons manquantes et 2 troncatures — tous
  faux positifs documentés. Les deux **signatures exactes** de la moulinette d'AMBOSS
  (`plage-coupee`, `troncature-x-fragment`) sont à **zéro** : le corpus RESCOS n'a pas subi
  cet import.
- **`therapy-section`, `cloture-title` et `redflags-title` existent aussi dans le corpus
  AMBOSS**, alors que le `BLOCKS` d'AMBOSS ne les couvre pas. Sa mesure publiée (147) les
  ignore donc. Élargir son `BLOCKS` changerait cette mesure, ce que la consigne interdit ;
  le constat est consigné pour arbitrage.

---

## 5. Ce que la campagne a appris sur la méthode

Trois acquis, tous transposables aux deux autres corpus.

### 5.1 `report_redundancy.py` lu à l'envers détecte les trous du bloc canonique

C'est l'acquis principal, et il est né d'un accident au pilote RESCOS-21 : une paire
`therapy ↔ presentation` sans `resume` a fait remarquer qu'il n'y avait **pas d'antalgie
dans la fiche de révision d'une perforation d'ulcère**, alors que la section notée et la
`presentation` la portaient toutes deux.

**La signature est exacte** : une information qui relie le **noté** (`therapy`, `redflags`)
à `presentation` **sans passer par `resume`** signale un manque du bloc canonique. Un
détecteur de doublons devient un détecteur de trous, sans une ligne de code de plus.

Rendement mesuré sur la campagne : **20 trous comblés**, dont la fenêtre de 3 h de l'acide
tranexamique, la limite de 3 infiltrations par an, l'endoscopie haute devant un méléna, la
prophylaxie thromboembolique en poussée de MICI hospitalisée.

**Sa limite est nette et elle importe.** `check_no_loss` compare l'avant et l'après d'une
même grille : il ne voit pas les fusions comme des pertes — c'est voulu — mais **il ne voit
pas non plus les trous**, qui sont antérieurs au passage. Les blocs canoniques incomplets
sont un angle mort de tout l'outillage, de la même famille que les numérations en unité
implicite. La lecture inversée est le seul instrument qui les atteint, et elle ne les
atteint que là où une paire subsiste.

### 5.2 Le rendement de la page SSP se prédit — le prédicteur a changé en cours de route

Le volet German avait proposé un indicateur : le rendement du niveau 1 est inversement
proportionnel au nombre de grilles que la page dessert. **RESCOS le prend en défaut par les
deux bouts.** `SSP — Diplopie` ne dessert **qu'une** grille et n'a rien tranché ;
`SSP — Douleur de Hanche` en dessert **huit** et a tranché deux fois.

**Le bon prédicteur n'est pas le fan-out, c'est le chiffre.** Ce qui distingue les pages
productives, c'est que les grilles qu'elles desservent portent des **cibles chiffrées** —
LDL, durée de traitement, seuil de dérouillage, fréquence d'infiltration. Une phrase
clinique diverge visiblement ; un nombre diverge en silence. Le déclencheur retenu est donc :
**lire la page SSP quand la grille porte une cible chiffrée**, quel que soit le fan-out. Il
tient sur les cinq lectures du dernier lot.

**Sa limite, découverte au même lot : la page qui porte le symptôme n'est pas toujours celle
qui porte le chiffre.** `SSP — Douleur Thoracique` est **muette sur la cible LDL** des quatre
grilles de douleur thoracique du lot ; c'est `SSP — Syndrome Métabolique`, qui ne dessert
aucune grille du corpus par son intitulé, qui donne la table complète des cibles par strate
de risque — et c'est elle qui a tranché.

> **Corollaire pratique : quand une grille porte un chiffre, chercher la page qui porte ce
> chiffre, pas celle qui porte son symptôme.** Le prédicteur dit *quand* lire une page, pas
> *laquelle*. Indexer les pages SSP par cibles chiffrées plutôt que par symptôme se mécanise
> (un motif « valeur + unité + strate » sur le vault) et rendrait la lecture de niveau 1
> dirigée au lieu d'être devinée.

### 5.3 Le bordage d'un motif avant activation évite des faux positifs qui casseraient un corpus

Toute passe de nomenclature qui ajoute un motif à la table `BANNED` le mesure d'abord **sur
les trois corpus**, avant activation. Ce n'est pas une précaution de principe : la campagne
a **ajouté 26 motifs** (10 microbiologiques, 16 anglicismes) et **en a écarté 9**, chacun
sur un faux positif **mesuré** — et deux d'entre eux auraient cassé une grille parfaitement
correcte.

**`VRE`** — entérocoque résistant à la vancomycine. Rend un faux positif français :
AMBOSS-19 écrit « VRE = **volume de réserve expiratoire** », abréviation standard de
spirométrie. Dans une porte bloquante, ce motif aurait cassé toute grille portant des
volumes pulmonaires.

**`QID`** — le cas le plus net, et il est neuf. Le même token vaut **quadrant inférieur
droit** dans RESCOS-22 (« QSD, QSG, QID, QIG ») et **quater in die** dans AMBOSS-13 et
AMBOSS-8. Deux sens légitimes, un par corpus, sur trois lettres identiques. Le motif aurait
cassé RESCOS-22 pour un usage parfaitement correct.

Écartés pour la même raison : `ASA` (« 5-ASA », nom de molécule, 8 hits RESCOS / 6 AMBOSS /
10 German), **`Rx`** (« Rx thorax » = graphie **suisse** de la radiographie — faux ami
parfait, `Rx` désignant l'ordonnance en anglais ; bannir le sigle français parce qu'il
ressemble à un sigle anglais serait l'erreur exactement inverse de celle qu'on corrige),
`AF` (« anamnèse familiale (AF) », RESCOS-19), `AAA` (les sigles français et anglais de
l'anévrisme de l'aorte abdominale coïncident), `CRE` (aucun besoin mesuré — on n'ajoute pas
un motif de trois lettres sans besoin), et les usages installés `MI` (membres inférieurs,
8 / 16), `CT` (90), `US` (41), `PR` (polyarthrite rhumatoïde) et `borderline` (terme
diagnostique employé tel quel en français).

Le même réflexe a servi ailleurs qu'aux acronymes : le motif `numeration-implicite` a reçu
un **garde-fou d'année** (`(?!(?:19|20)\d\d\b)`) après avoir vu « plaquettes en 2019 » le
déclencher, et son seuil est `\d{3,}` et non `\d{2,}` **par mesure** — à deux chiffres, il
se déclenchait sur « hyperleucocytose (> 12 000/mm³) », capturant « 12 » et déclarant nue
une valeur dont l'unité est deux caractères plus loin.

**Et un contre-exemple utile, sur le `gold standard`.** Le motif est homogène, installé, et
se prête à un `sed` — mais sur ses 15 occurrences, **une qualifiait un traitement et non un
examen** (RESCOS-38, « Méthotrexate = gold standard »). Un remplacement uniforme aurait
produit « Méthotrexate = examen de référence ». Remplacement occurrence par occurrence, avec
assertion de comptage sur chacune.

**Coût mesuré de l'harmonisation terminologique : +2 paires de redondance**, sur RESCOS-14 et
RESCOS-35. Deux items qui disaient déjà la même chose en deux mots différents la disent
maintenant dans les mêmes mots, et le comparateur les apparie. C'est le prix exact de la
cohérence ; le refuser reviendrait à préférer un chiffre à la lisibilité.

---

## 6. Le détail des six vérifications

### 6.1 Les vérificateurs, sur RESCOS et sur AMBOSS

| Corpus | Commande | Résultat |
|---|---|---|
| RESCOS | `check_invariants.py` | **OK** — 41 grilles, 10 champs gelés (dont `coef`, `sectionCounts`, `configForm`, le nombre de segments par bloc), `boundsAnomalies` et `uncoveredContent` vides, code 0 |
| RESCOS | `check_nomenclature.py` | **OK** — aucun terme non suisse, code 0 (table `BANNED` + 10 motifs microbiologiques + 16 anglicismes) |
| RESCOS | `check_reachability.py` | **OK** — 41 grilles, barème atteignable à 100 % sur chaque section, code 0 |
| RESCOS | `report_redundancy.py` | **131** paires inter-blocs |
| RESCOS | `report_redundancy.py --intra` | + **210** paires intra-bloc |
| RESCOS | `check_no_loss.py a82e036` | 485 items signalés sur 39 grilles, rapport, code 0 |
| RESCOS | `report_import_defects.py` | 0 / 0 / 2 / 96 / 0 / 12 / 0 — `numeration-implicite` à **0** |
| AMBOSS | `check_invariants.py` | **OK** — 40 grilles, code 0 |
| AMBOSS | `check_nomenclature.py` | **OK**, code 0 |
| AMBOSS | `check_reachability.py` | **OK** — 40 grilles à 100 %, code 0 |
| AMBOSS | `report_redundancy.py` | **147 paires — inchangé**, et 236 intra-bloc |

**AMBOSS est le témoin de la campagne**, et il est resté au vert à 147 d'un bout à l'autre.
C'est vérifiable par construction : l'outillage RESCOS **importe** de `scripts/amboss/` tout
ce qui ne décrit pas un corpus — les primitives de texte (`strip_base64`, `visible_text` et
son correctif du chevron nu, `norm`, le découpage par puces), la table `BANNED`, la
simulation de `cases/scoring.js`, les sept familles de motifs d'import — de sorte qu'il
n'existe qu'une seule implémentation de chacune.

L'import se fait par chemin explicite sous un **alias propre à rescos**
(`_rescos_amboss_<nom>`), et ce n'est pas cosmétique : `check_reachability.py` **remplace**
`parse_config` dans le module AMBOSS chargé, pour lui faire lire la seconde forme de
déclaration du barème. Sans alias distinct, ce remplacement fuirait vers German si les deux
tournaient dans le même processus.

`scripts/german/` n'a été ni lu, ni écrit, ni exécuté par cette vérification.

### 6.2 Barème — une seule divergence, celle qui était admise

Recalcul indépendant, en relisant chaque grille à `a82e036` par `git show` et en appliquant
**la même logique d'extraction des deux côtés** — celle du `snapshot_invariants.py` courant —
pour qu'une différence constatée vienne du contenu et jamais de l'outil. Huit champs :
`maxScores`, `<span class="score">`, `sectionInfo[].count`, `coef`, `criteriaCount`,
`detailCount`, `radioCount`, `checkboxCount`. 41 grilles de part et d'autre, aucune disparue,
aucune apparue.

**Huit différences, toutes sur RESCOS-12 et RESCOS-13, quatre par grille — exactement la
correction du § 2 :**

| Champ | `a82e036` | `1a0a8f6` |
|---|---|---|
| `maxScores` | `{anamnese, examen: 0, management, communication}` | la clé `examen` retirée |
| `scoreSpans` | `{…, statusScore: 0, …}` | le `<span class="score">…/0</span>` retiré |
| `sectionCounts` | `{…, examen: 0, …}` | l'entrée retirée de `sectionInfo` |
| `coef` | `0.25` ×4 | `0.3333333333333333` ×3 |

La somme des maxima (76 et 78) est inchangée — la valeur retirée était 0 — et l'affichage
statique `0/76` et `0/78` reste juste.

**`criteriaCount`, `detailCount`, `radioCount` et `checkboxCount` sont identiques sur les
41 grilles.** Autrement dit : **aucun critère, aucun sous-item, aucune case, aucun bouton
n'a été ajouté ni retiré nulle part dans le corpus.** Les substitutions de nomenclature qui
ont touché des libellés de sections notées (RESCOS-1, 2, 15, 31, 36) ont respecté le format
`N. Libellé [réponse]` que `cases/scoring.js:159` découpe, et conservé les crochets de
`patient-response`.

### 6.3 Intégrité structurelle

| Contrôle | Résultat |
|---|---|
| Balises `div`, `ul`, `li`, `p`, `span` appariées | **41/41** — ouvrants (hors auto-fermants) = fermants pour les cinq types |
| `</html>` final | **41/41** |
| Blocs présents et nombre de segments par bloc, contre le gel | **41/41** — 313 segments, identiques à `a82e036` |
| `boundsAnomalies` · `uncoveredContent` | **[] · []** sur 41/41 |
| Équilibrage `<div>` du corpus | **0 écart, 41 fois sur 41** |
| **Crochets `[…]` du bloc `cloture`** | **13/13 grilles intactes** — nombre pour nombre, et appariés |

Le dernier point mérite son détail. `cases/scoring.js:294` fait entrer `.cloture-content`
dans le **même sélecteur** que `.criteria-text`, `.redflags-text`, `.therapy-section` et
`.detail-text` : le moteur y colore les crochets au même titre que les réponses patient du
reste de la grille. **Les perdre casserait silencieusement l'affichage de 13 grilles**, et
rien dans la liste des interdits ne le disait — le bloc `cloture` n'existait ni dans AMBOSS
ni dans German quand cette liste a été écrite. La contrainte a été portée dans
`PROCEDURE-rescos.md` au pilote.

| Grille | segments `cloture` | crochets `a82e036` → `1a0a8f6` |
|---|---|---|
| RESCOS-2 · 26 · 36 · 39 · 28 · 29 | 3 chacune | 4 → 4 (3 → 3 pour RESCOS-26) |
| RESCOS-15 · 21 · 31 · 38 | 3 chacune | 5 → 5 |
| RESCOS-4 | 4 | 3 → 3 |
| RESCOS-8 | 3 | 6 → 6 |
| RESCOS-9b | 3 | 0 → 0 |

40 segments, 13 grilles, **52 crochets** — et le contrôle fonctionnel confirme que les
52 sont colorés à l'exécution.

### 6.4 Redondance

**Inter-blocs : 610 → 131 (−78 %). Intra-bloc : 323 → 210 (−35 %).**

Restreinte aux **cinq blocs que mesure AMBOSS** (`annexe-dd`, `resume`, `expert`, `theorie`,
`presentation`), la mesure comparable passe de **578 à 113**. C'est un point de repère utile :
RESCOS entrait dans le chantier avec **le double** de la redondance d'AMBOSS (578 contre 301
pour un nombre de grilles voisin) et en sort **en dessous** de l'état traité d'AMBOSS
(113 contre 147).

31 grilles portent au moins une paire résiduelle ; **10 sont à zéro**. La distribution des
scores est basse — 71 paires sous 0,80, 43 entre 0,80 et 0,89, 17 au-dessus de 0,90 — alors
que l'état de départ comptait des dizaines de paires à 1,0 exact (RESCOS-21 en portait 4 à
elle seule).

Les 131 paires ont été classées, et un échantillon lu dans le HTML.

| Famille | Paires | Ce que c'est |
|---|---|---|
| **Plancher structurel** | 107 | le signe cardinal du diagnostic, que chaque bloc doit nommer **par sa fonction** |
| **Contrat `therapy` / `redflags`** | 17 | l'accord voulu entre l'attendu **noté** et la fiche de révision — pas une redondance à retirer |
| **Faux positifs de polarité** | 7 | un piège d'`expert` et la règle de `theorie` qu'il nie, appariés par leur ressemblance de chaîne |

**Le plancher structurel se lit sans ambiguïté sur les grilles denses.** RESCOS-21 (18
paires) : la triade de la perforation d'ulcère — coup de poignard, ventre de bois, matité
hépatique disparue — que `annexe-dd` nomme comme arguments POUR, `resume` comme signes
d'examen, `expert` comme décodage pour l'examinateur, `presentation` comme mnémo. RESCOS-38
(14 paires) : raideur matinale et syndrome inflammatoire, les deux signes cardinaux de la
polyarthrite. RESCOS-32 (7 paires) : sensation de corps étranger, rougeur unilatérale, ceux
de la kératite. Le contenu est irréductible ; seule la forme change. Les essais de
reformulation menés au pilote et au lot r4a l'ont confirmé deux fois — ils **déplacent** les
paires sans les réduire (« ventre de bois (contracture) » remplace une paire à 0,81 par une
paire à 0,84), au prix d'une dégradation du mnémo.

**Les 7 faux positifs de polarité sont un artefact de mesure, pas des doublons.** Le
comparateur travaille sur du texte normalisé et ne voit pas la négation : « ne pas rechercher
d'hémorragie externe » (piège d'`expert`, RESCOS-4) contre « recherche hémorragie externe »
(règle de `theorie`) s'apparient à 0,85 en disant l'inverse l'un de l'autre. Même chose pour
« faire des suppositions sur l'orientation sexuelle » contre « éviter les suppositions… »
(RESCOS-33, 0,91), et pour un piège d'`expert` contre une **légende d'image**
(RESCOS-35, 0,82 : « ne pas évoquer le diagnostic d'embolie pulmonaire » contre « score
clinique pour le diagnostic d'embolie pulmonaire »). **Aucune action n'est requise** ; le
fait est signalé pour que le chiffre 131 ne se lise pas comme 131 doublons.

**La thèse ne couvre pas RESCOS-15**, et c'est le défaut 2 du § 0 : 14 paires, dont
11 issues de trois items seulement, avec une recopie verbatim du bloc **noté** `redflags`
dans une sous-section de `presentation` dont le rôle est le mnémo — lequel porte déjà
l'information. C'est la seule grille du corpus dans ce cas — et elle porte à elle seule
**les 5 paires `redflags` résiduelles du corpus entier**. **Réparé au lot r7** : la
sous-section a été réduite, 14 → 10 paires pour la grille, 131 → 127 pour le corpus,
5 → 3 paires `redflags` ; voir l'encadré du défaut 2 au § 0.

### 6.5 Non-perte d'information

`check_no_loss.py a82e036` signale **485 items sur 39 grilles**. Le volume est attendu : la
campagne a converti 53 réponses Q/R de la liste à la phrase parlée, fusionné les arguments
recopiés de `presentation`/§1 et supprimé des sous-sections surnuméraires. Un item converti
change de forme, il ne disparaît pas — mais l'extracteur ne sait pas le suivre.

L'analyse a porté sur des **motifs**, pas sur un verdict item par item.

| Lecture | Résultat |
|---|---|
| **Volume par grille** | taux de suppression maximal **19,8 %** (RESCOS-34), médiane ≈ 8 %, total du corpus **−9,5 %** d'items pour **+3,0 %** de volume rédactionnel. **Aucune grille au volume anormal** : les huit plus chargées (RESCOS-34, 37, 28, 38, 35, 36, 24, 20) sont exactement les huit où le dédoublonnage a le plus rendu |
| **Filtre par mots porteurs** (≥ 6 lettres ou contenant un chiffre, hors mots outils) | 140 des 485 items perdent au moins un mot porteur ; **345 sont des reformulations pures** |
| Idem, après retrait des variantes morphologiques | **49 items** — dont la grande majorité perd un qualificatif sans contenu médical (« plutôt », « toujours », « encore », « habituellement », « crucial », « possible ») |
| **Filtre thématique** (dose, seuil, contre-indication, drapeau rouge, grossesse, dépistage) | **54 items**, dont **16** perdent un mot porteur → **relus un par un** |

Les 16 items sensibles se répartissent ainsi, tous vérifiés dans le fichier courant :

- **12 variantes morphologiques** — le mot porteur a un voisin de même racine dans la grille :
  « systématiquement » → « systématique », « objectifs » → « objectif », « quantifié » →
  « quantifier », « contrôle » → « contrôle clinique **à 48 heures** » (que `a82e036` écrivait
  « 48h », d'où la fausse disparition du token), « amélioré » → « amélioration »,
  « hyperleuco » → « hyperleucocytose », « limiter » → « limite ».
- **4 sans aucun voisin morphologique, relus intégralement** :
  - RESCOS-27 et RESCOS-37, le token `55` et le mot « objectif » des cibles LDL —
    **corrections voulues** (§ 3.B). RESCOS-37 écrit désormais « une coronaropathie
    documentée classe d'emblée en très haut risque, donc **cible LDL 1,4 mmol/L, soit
    0,55 g/L** » : la grille explicite l'équivalence entre les deux unités, ce qui est
    précisément la confusion qui avait produit l'erreur.
  - RESCOS-28, « amélioration à l'effort » du contraste mécanique / inflammatoire —
    **réécrit et enrichi** : `theorie` porte maintenant « raideur matinale > 60 min, seuil
    des critères ACR ; en pratique clinique c'est un dérouillage > 30 min qui fait basculer
    vers l'inflammatoire ».
  - RESCOS-34, « pas d'allergie connue, pas de traitement régulier » — **présent dans le
    `scenario`** (« il n'a pas d'allergie connue ») ; l'item retiré n'était que sa recopie
    dans `presentation`/Version longue.

**Aucune perte sur un thème sensible.** Les 16 items se résolvent tous, et les quatre
relectures intégrales ne laissent aucun contenu hors du corpus.

**Le seul résidu réel du corpus vient de l'autre passe** — celle des 49 items dont un mot
porteur disparaît **sans voisin morphologique**, dont la grande majorité perd un qualificatif
sans contenu médical. Onze d'entre eux ont été recontrôlés, ceux qui portaient un contenu
identifiable :

| Item | Verdict |
|---|---|
| RESCOS-18, seuil de paroi vésiculaire « > 3 mm » | **survit** dans le `resume` où il a été porté — écrit « 3 mm » au lieu de « 3mm », d'où la fausse alerte |
| RESCOS-24, « ECBU obligatoire » | **survit** — 14 occurrences, dont « ECBU systématique avant ATB » |
| RESCOS-36, « bêtabloquant 1re intention » | **survit** — 7 occurrences |
| RESCOS-38, « corticothérapie faible dose » | **survit** dans `therapy` **et** `resume`, avec « ≤ 10 mg/j » et la prévention de l'ostéoporose |
| RESCOS-35, « surveillance créatinine, plaquettes » | **survit** — réparation déjà faite au lot r4c |
| RESCOS-9b, « durée ATB 3-6 semaines » | **correction voulue** — aligné sur « 3-4 semaines, plus longue si ostéomyélite associée » (§ 3.E) |
| RESCOS-34, « pas d'hypoxémie rapportée » | **survit** — « une saturation conservée » dans `annexe-dd` |
| RESCOS-7, « anévrisme 9 mm avec indication chirurgicale » | **survit**, et la règle qui la fonde aussi : `theorie` écrit « anévrismes > 7 mm : indication chirurgicale » et « surveillance si anévrisme < 7 mm » |
| **RESCOS-35, « activité physique adaptée »** | **résidu réel** — défaut 3 du § 0, **restauré au lot r7** dans la réponse orale Q3 « Suivi » de `presentation` |

Un mot sur la méthode : ce filtrage par mots porteurs est celui que les lots r4b et r4c
avaient mis au point et qui leur avait déjà rattrapé **trois réductions réelles** —
« spondyloarthrite » (RESCOS-28), « créatinine, plaquettes » (RESCOS-35) et « consultation
cardiologique régulière » (RESCOS-36). Rejoué ici sur l'ensemble du corpus et non lot par
lot, il en rend **un quatrième**, mineur.

### 6.6 Contrôle fonctionnel en navigateur

Mené sur les **41 grilles**, dans Chrome sans interface piloté par le protocole DevTools
(aucun paquet installé, aucune connexion hors de la boucle locale). Le remplissage est
**piloté par le DOM et non par `window.caseConfig`** — sans quoi RESCOS-7 et RESCOS-9, qui
n'en ont pas, seraient sorties du contrôle : toutes les cases de détail cochées, chaque
groupe de boutons à sa valeur maximale, la communication au meilleur niveau de l'échelle
A–E.

| Contrôle | Résultat |
|---|---|
| Total global | **100 %**, note **A** — **41/41** |
| Score de chaque section = dénominateur affiché | **41/41** — **157 sections**, aucune en écart |
| Réponses entre crochets colorées en `rgb(44, 90, 160)` | **1 627 crochets, 1 627 colorés** |
| dont crochets du bloc `cloture` | **52 / 52** |
| Balise orpheline visible dans le texte rendu | **aucune**, 41/41 |
| Chargement sans exception ni erreur de console | **39/41** — RESCOS-7 et RESCOS-9 lèvent un `TypeError` (§ 0, défaut 1) · **41/41 après r7** |
| Score remonté à `ecos_registry` après remplissage | **39/41** — RESCOS-7 et RESCOS-9 n'ont pas `saveToRegistry` · **41/41 après r7** |
| Minuteur : démarre en mode examen, affiche « En cours », décompte | **41/41** — 13:00 → 12:58 en 2 s, sur les 41 |

**RESCOS-12 et RESCOS-13 atteignent 100 %, note A**, là où elles plafonnaient à 75 %, note C.
Vérifié à l'écran, sur les trois sections restantes : 48/48 + 8/8 + 20/20 pour RESCOS-12,
36/36 + 22/22 + 20/20 pour RESCOS-13. La section « Examen clinique — section non cotée » ne
porte plus ni dénominateur ni tuile de pourcentage.

**RESCOS-7 et RESCOS-9 fonctionnent** : 30/30 pour la première (communication seule), 41/41
et 15/15 pour la seconde, 100 % et note A pour les deux. Leur exception ne les empêche ni de
calculer, ni d'afficher, ni de colorer leurs crochets — elle est absorbée par l'appel de
secours de fin de page. Elle reste un défaut, et son détail est au § 0.

> **Repasse r7, les 41 grilles.** Après réparation : **41/41** à 100 %, note A ; **41/41**
> sans aucune exception ni erreur de console ; **41/41** avec un `ecos_registry` à
> `pct: 100, grade: "A"` ; **41/41** au minuteur 13:00 → 12:58. Une seule grille rend zéro
> crochet coloré, **RESCOS-7, et c'est correct** : hors de ses `<script>`, elle ne porte
> aucun `[…]` — station d'annonce de mauvaise nouvelle, quinze critères de communication
> purs, aucune réponse de patient entre crochets. Vérifié des deux côtés de r7 : 0 avant,
> 0 après. Les 36 « crochets » que `visible_text()` y voyait à `0e82963` étaient des
> littéraux de tableau JavaScript du moteur embarqué.

> **Note d'arrondi, sans conséquence vérifiée.** Sur RESCOS-12 et RESCOS-13,
> l'accumulation réelle (`globalPercentage += 100 * coef`, trois fois) donne
> **99.99999999999999**, pas 100 — l'ordre des opérations diffère de la somme des
> coefficients, qui vaut exactement 1,0. Les trois consommateurs de cette valeur sont
> inoffensifs : `Math.round(…)` rend **100**, `getClass(p)` teste `p >= 90` et rend **A**,
> `saveToRegistry` stocke l'arrondi. **Aucune comparaison `=== 100` n'existe dans
> `cases/*.js`** — vérifié. Tout code futur qui comparerait `globalPercentage` à 100 sans
> arrondir échouerait ; un `Math.round` en amont fermerait la question.

---

## Annexe — comment reproduire les vérifications

```bash
python3 scripts/rescos/check_invariants.py          # OK — 41 grilles, code 0
python3 scripts/rescos/check_nomenclature.py        # OK — aucun terme non suisse, code 0
python3 scripts/rescos/check_reachability.py        # OK — 41 grilles à 100 %, code 0
python3 scripts/rescos/report_redundancy.py         # TOTAL : 127 paire(s)  (131 avant r7)
python3 scripts/rescos/report_redundancy.py --intra # + paires intra-bloc
python3 scripts/rescos/check_no_loss.py a82e036     # rapport, code 0 en toutes circonstances
python3 scripts/rescos/report_import_defects.py     # rapport, code 0

python3 scripts/amboss/check_invariants.py          # OK — 40 grilles, code 0
python3 scripts/amboss/check_nomenclature.py        # OK, code 0
python3 scripts/amboss/check_reachability.py        # OK — 40 grilles à 100 %, code 0
python3 scripts/amboss/report_redundancy.py         # TOTAL : 147 paire(s) — le témoin
```

Les trois premiers de chaque corpus sortent en erreur si un écart apparaît : ce sont des
portes. Les rapports listent sans juger et sortent toujours 0 — **ne jamais les câbler comme
portes bloquantes**, ce serait bloquer le projet sur des suppressions parfaitement légitimes.

**Le défaut 1 du § 0 se retrouve en une commande**, qui cherche toute grille dont le moteur
de calcul déréférence `#missingItems` sans garde alors que l'élément n'existe pas dans le
HTML vivant :

```bash
python3 -c "
import re, sys; sys.path.insert(0, 'scripts/rescos'); import lib_rescos as lib
COMMENT = re.compile(r'<!--.*?-->', re.S)
for p in lib.grids():
    h = lib.strip_base64(p.read_text(encoding='utf-8'))
    ecrit = bool(re.search(r'getElementById\(\"missingItems\"\)\.style', h))
    vivant = 'id=\"missingItems\"' in COMMENT.sub('', h)
    if ecrit and not vivant: print(p.name)
"
```

**Il rendait deux grilles — RESCOS-7 et RESCOS-9 — et zéro est la valeur attendue.** La
même commande sur `a82e036` rend les deux mêmes : le défaut était préexistant. **Depuis le
lot r7, elle rend 0** : les deux grilles chargent `cases/scoring.js`, dont la garde
`if (missingEl)` rend la question sans objet.

L'intégrité structurelle, la comparaison du barème avec `a82e036`, l'analyse par motifs du
rapport de non-perte et le contrôle fonctionnel en navigateur sont menés par des scripts
d'audit ponctuels, non versionnés — recalcul indépendant des deux côtés de l'historique pour
le barème, pilotage direct de Chrome par le protocole DevTools pour le contrôle fonctionnel.
