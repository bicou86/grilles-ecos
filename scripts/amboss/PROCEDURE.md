# Procédure de traitement d'une grille AMBOSS

Référence : `docs/superpowers/specs/2026-07-30-amboss-refonte-pedagogique-suisse-design.md`

**Corpus German** : voir `scripts/german/PROCEDURE-german.md`. Ce document-ci reste
la référence pour tout ce que l'autre ne redit pas — hiérarchie à trois niveaux,
règle du format, « le dédoublonnage ne perd jamais d'information », interdits. Les
blocs, eux, diffèrent entièrement d'un corpus à l'autre.

## 1. Situer la zone pédagogique

```bash
python3 -c "
import sys; sys.path.insert(0,'scripts/amboss'); import lib_amboss as lib
p=[g for g in lib.grids() if 'AMBOSS-N_' in g.name][0]
h=p.read_text(encoding='utf-8'); s,e=lib.peda_bounds(h)
print('ligne debut :', h[:s].count(chr(10))+1)
print('ligne fin   :', h[:e].count(chr(10))+1)
print('blocs       :', lib.blocks_present(h))
"
```

Lire ensuite la grille avec `Read` en passant `offset` = ligne de début et
`limit` = (ligne de fin − ligne de début). **Ne jamais lire le fichier entier.**

### 1 bis. Situer le bloc `annexe-dd` — lecture ciblée séparée

`annexe-dd` est le seul bloc pédagogique situé **avant** la zone ci-dessus : il vit
dans la section Management, à l'intérieur du `criteria-row` du critère m1
(« Hypothèses diagnostiques »). Des centaines de lignes de section notée l'en
séparent, c'est pourquoi `peda_bounds()` n'a **pas** été élargi jusqu'à l'englober —
cela ferait relire tout le barème à chaque fois. Il a ses propres bornes :

```bash
python3 -c "
import sys; sys.path.insert(0,'scripts/amboss'); import lib_amboss as lib
p=[g for g in lib.grids() if 'AMBOSS-N_' in g.name][0]
h=p.read_text(encoding='utf-8'); s,e=lib.dd_bounds(h)
print('offset :', h[:s].count(chr(10))+1)
print('limit  :', h[:e].count(chr(10))-h[:s].count(chr(10))+1)
"
```

Deux `Read` ciblés sont donc nécessaires pour voir toute la matière pédagogique
d'une grille : celui du § 1 et celui-ci. Le second est court — le bloc tient en
**30 à 40 lignes** (3 961 à 6 571 caractères, 5 253 en moyenne).

**Bornes.** Début `<div class="annexe-item annexe-dd">`, fin : le `criteria-row`
suivant (celui de m2). Établi par équilibrage des `<div>` sur les 40 grilles : la
fermeture équilibrée du bloc tombe exactement sur
`<div class="criteria-row" id="criteria-m2">`, **40 fois sur 40**, et le bloc ne
contient lui-même aucun `criteria-row`. Le marqueur de fin porte deux alternatives
de repli (`annexes`, `resume`) qui ne servent jamais aujourd'hui : elles bornent la
casse si une grille future plaçait le bloc en fin de section, sans `criteria-row`
derrière lui — sans elles, `block_segment()` avalerait tout le reste du fichier.

## 2. Lire la page SSP de référence

La page est donnée par `docs/obsidian-mapping.yaml`. Racine du vault :
`/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian`.

Sections utiles : `## 🔬 EXAMENS COMPLÉMENTAIRES`, `## 💊 PRISE EN CHARGE`,
`## 📌 Points Clés ECOS`.

## 3. Dédoublonner selon le contrat

| Bloc | Rôle exclusif | Ne porte jamais |
|---|---|---|
| `annexe-expert` | Faire tourner la station | Théorie, listes d'apprentissage |
| `annexe-theorie` | Comprendre le cas | Check-lists actionnables, mnémos, protocoles |
| `annexe-dd` | **Raisonner le différentiel** | Check-lists actionnables, conduite de station, formulation orale |
| `resume` | Réviser vite — **source canonique** | Redites de la théorie, formats oraux |
| `presentation-patient` | Restituer à l'oral | Toute donnée clinique nouvelle |

**Le rôle d'`annexe-dd`** (décision : `docs/superpowers/arbitrages-amboss-2026-08.md`
§ 1.2). Le bloc porte le **raisonnement différentiel** — quelles hypothèses, quels
arguments pour et contre chacune, quel examen les départage. C'est l'**extension
naturelle du rôle d'`annexe-theorie`** (comprendre le cas), appliquée au tri des
hypothèses ; les deux se lisent ensemble et obéissent aux mêmes interdits. Il ne
doit donc porter ni check-list actionnable, ni conduite de station (qui est le rôle
d'`annexe-expert`), ni formulation orale (qui est celui de `presentation`).

Son contenu n'est **pas noté** : il ne contient aucune case à cocher. Le
`<input type="radio">` du `criteria-row` qui l'héberge appartient au critère m1
englobant, pas au bloc. Y toucher ne peut donc pas déplacer le barème — mais les
bornes doivent rester exactes, sous peine d'emporter le critère voisin.

**Règle du format** : une information peut réapparaître si et seulement si elle
change de format de restitution (liste → narration, liste → SBAR, liste →
question d'examinateur). Même format + même contenu = suppression.

Les 7 axes à traiter :

1. **Examens complémentaires** — `resume` canonique ; `theorie` garde le *pourquoi*
   (Se/Sp, seuils, indications) sans la liste ; `presentation` garde sa Q/R, dont la
   réponse est un sous-ensemble strict de `resume`.
2. **Traitement / PEC** — `resume` canonique ; `theorie`/Rappels thérapeutiques garde
   le rationnel ; `presentation` garde sa réponse orale, sous-ensemble strict.
3. **PEC en 3 points** — check-list = sous-ensemble strict de `resume`/Prise en charge.
   Corriger toute divergence, ne rien ajouter.
4. **Examens à faire** — check-list = sous-ensemble strict de `resume`/Examen clinique.
5. **Checklist mentale** (`presentation`) — reste une **trame de présentation**
   (Intro → caractériser → symptômes → ATCD → examen → résumé → examens → PEC),
   jamais une liste de questions cliniques.
6. **Pièges** — `expert`/Pièges canonique. Supprimer `presentation`/Pièges ECOS.
   Concerne les grilles 1, 2, 3, 5, 6, 9, 11, 12, 13, 14, 30, 38, 39.
7. **Points clés** — les deux restent, différenciés : `expert` = ce que l'examinateur
   observe · `resume` = ce que l'étudiant retient.

Utiliser `python3 scripts/amboss/report_redundancy.py AMBOSS-N_` pour lister les
paires détectées sur cette grille précise.

**Le dédoublonnage ne perd jamais d'information.** Avant de supprimer une section ou
une sous-section jugée redondante, la comparer item par item au bloc canonique et
vérifier qu'elle n'en porte aucun qui y soit absent. S'il en reste un, le **porter
dans le canonique avant** la suppression — jamais l'inverse, jamais après. Un item
qui n'a de place dans aucun bloc canonique n'est pas redondant : c'est qu'il est
unique, et il se conserve. Cette vérification est obligatoire et prime sur les
sept axes : un axe dit *où* l'information doit vivre, il n'autorise pas à la perdre.
Elle vaut aussi pour les sections dont un axe prescrit la suppression en bloc.

Deux précédents, tous deux issus de la tâche 5 :

- *Axe 6.* `presentation`/Pièges ECOS d'AMBOSS-3 portait « Oublier de demander un
  test β-hCG », absent d'`expert`/Pièges — et c'est le piège éliminatoire n° 1 de la
  page SSP. L'item a été porté dans `expert`/Pièges, **puis** la sous-section
  supprimée. C'est le geste à reproduire sur les onze grilles restantes de l'axe 6 :
  la suppression est prescrite, la perte ne l'est pas.
- *Mnémos.* Quand une `mnemo-box` de `presentation`/Checklist mentale est le mnémo le
  **plus complet** de la grille, elle se **déplace** vers `presentation`/Touches
  ludiques — la Checklist mentale redevenant une trame pure (axe 5) — au lieu d'être
  supprimée. C'est bien la redondance qui décide, pas le type de bloc : le pilote
  AMBOSS-1 a pu supprimer la sienne parce qu'elle doublait strictement les 6F déjà
  présents dans Touches ludiques ; AMBOSS-2 (APPENDIX ⊃ « les 3A ») et AMBOSS-3
  (OVAIRE, après absorption de NAFT dans ses valeurs) ont dû la déplacer. Les clés
  du mnémo conservé restent intactes, seules les valeurs absorbent les items repris.

**Sections de queue d'`annexe-theorie`.** Les deux dernières sections du bloc —
`theorie-section-rappels` (Rappels thérapeutiques) puis `theorie-section-examens`
(Examens complémentaires) — existent dans les 40 grilles et portent chacune une
couleur propre en CSS (`cases/case-styles.css:961-971` : olive = thérapeutique,
vert = examens, la même convention que les `c-yellow` / `c-green` des pages SSP).
Elles ne se suppriment ni ne se déplacent. Quand un titre y est dupliqué avec une
section du corps du bloc — cas d'`Examens complémentaires` dans les grilles 1 et 2,
les seules concernées — c'est la **section de queue** qu'on conserve et celle du
corps qu'on supprime.

**Redire à l'oral, pas en liste.** Quand `presentation` doit reprendre `resume`, il
le fait en registre parlé (`presentation-reponse text`). Une liste recopiée sous un
en-tête « Q/R » ne constitue pas un changement de format et tombe sous la règle du
format. Les mnémos, eux, gardent leur clé d'origine et reçoivent la traduction en
valeur (`Fat : surcharge pondérale`) — même règle que les glossaires de schéma
ci-dessous, et pour la même raison : supprimer le mot d'origine casserait le mnémo.

## 4. Aligner les prises en charge

Trois autorités, à interroger **dans cet ordre**. La première qui tranche le point
l'emporte ; on ne descend au niveau suivant que si le niveau courant reste muet.

| Niveau | Situation | Autorité |
|---|---|---|
| 1 | La page SSP tranche explicitement le point | **La page SSP fait foi.** Aligner le pédagogique sur elle, journaliser avec la citation |
| 2 | La page SSP reste générique **et** le pédagogique contredit la section notée | **La section notée fait foi.** Aligner le pédagogique sur elle, journaliser |
| 3 | Ni l'une ni l'autre ne tranche | Laisser inchangé, consigner au journal. **Ne rien inventer** |

Pourquoi la section notée l'emporte au niveau 2 : c'est ce sur quoi l'étudiant est
évalué, elle est souvent plus précise (molécule, posologie, durée) et elle a déjà été
suissifiée par les tâches 2 et 3.

**Le barème reste gelé dans les trois cas.** On n'aligne jamais qu'en modifiant le
pédagogique : une divergence repérée *dans* une section notée se consigne, elle ne se
corrige pas. Au niveau 2, reprendre la formulation exacte de la section notée pour
qu'aucun écart ne subsiste, puis vérifier qu'aucun autre bloc pédagogique ne porte
encore l'ancienne formule.

**La hiérarchie n'arbitre qu'entre sources divergentes.** Elle départage la page SSP,
la section notée et le pédagogique quand ils se contredisent. Elle ne s'applique pas
à une **erreur factuelle interne à un bloc** — un énoncé faux en lui-même, qui ne
contredit aucune autre source parce qu'aucune autre source ne le porte. Une telle
erreur **se corrige directement**, sans passer par les trois niveaux, et se documente
au journal comme toute autre modification. Le niveau 3 (« laisser inchangé, ne rien
inventer ») vise l'arbitrage impossible entre deux formulations défendables ; il ne
protège pas un fait faux.

Exemple (AMBOSS-19, tâche 7) : `resume` invoquait « les critères d'Anthonisen » dans
un item, puis indiquait l'antibiothérapie sur « expectoration purulente, dyspnée +
**fièvre** » deux items plus loin. La fièvre ne fait pas partie des critères
d'Anthonisen — l'item contredisait sa propre référence et élargissait indûment
l'indication antibiotique. Ni la page SSP ni la section notée ne définissent ces
critères : il n'y avait donc rien à arbitrer, seulement un fait à corriger.

Le test pratique : *une autre source dit-elle le contraire ?* Si oui → hiérarchie à
trois niveaux. Si non, et que l'énoncé est faux dans l'absolu ou incohérent avec
lui-même → correction directe.

Attention à ne pas confondre **contradiction** et **précision**. Une mise en garde que
la page SSP ajoute à ce que dit la section notée (AMBOSS-1 : « éviter les AINS si
suspicion d'ulcère, IRA ou patient âgé » face à « AINS si pas de CI ») relève du
niveau 1 : elle se porte dans le pédagogique, la section notée reste intacte, et il n'y
a rien à consigner.

Exemple de niveau 2 (AMBOSS-1) : la page SSP dit « antibiothérapie si cholécystite »
sans nommer de molécule → `resume` a été aligné sur le protocole du critère noté `m5`
(amoxicilline-acide clavulanique 1 g × 3/j IV ; ciprofloxacine + métronidazole si
allergie), et non laissé sur le « céphalosporine + métronidazole » qu'il portait.

## 5. Journaliser

Ajouter une entrée dans `docs/superpowers/journal-amboss-2026-07.md` au format
défini en tête de ce fichier.

## 6. Vérifier

```bash
python3 scripts/amboss/check_invariants.py     # doit sortir OK
python3 scripts/amboss/check_nomenclature.py   # doit sortir OK
python3 scripts/amboss/check_reachability.py   # doit sortir OK
```

**Les trois sortent 1 en cas d'écart** — ce sont des portes, pas des rapports.
`check_no_loss.py` et `report_redundancy.py`, eux, sortent toujours 0 : ils listent,
ils ne jugent pas.

**`check_invariants` et `check_reachability` ne posent pas la même question.** Le
premier compare l'état courant à `baseline.json` : il répond à *« le barème est-il le
même qu'hier ? »*. Un barème faux depuis l'origine y reste vert indéfiniment. Le second
ne compare à aucun passé : il rejoue `calculateScores()` sur le DOM, simule le
remplissage complet de la grille et vérifie que le maximum ainsi atteint égale
`maxScores` **et** le `<span class="score">`, section par section, avec un global à
100 %. Il répond à *« le barème est-il atteignable ? »*.

C'est ce trou qu'AMBOSS-9 a traversé pendant tout le projet : `count: 13` pour douze
critères écrits et `anamnese: 53` pour 49 points calculables, défaut présent dès le
commit initial. Aucun compte d'éléments ne pouvait le voir — `criteriaCount` compte les
libellés présents, jamais ceux que la boucle va chercher. `check_reachability.py`
signale les trois formes de l'écart : un `count` qui promet un critère absent
(« ABSENT »), un sous-item **orphelin** dont l'identifiant sort de la séquence
`prefix1..prefixN` et qui n'entre donc jamais dans le calcul (`a12b`), et un `maxScores`
désaccordé du dénominateur affiché.

Depuis, `sectionInfo[].count` est **aussi** capté par `snapshot_one()` sous la clé
`sectionCounts` et gelé par `check_invariants`. Les deux contrôles sont complémentaires
et aucun ne remplace l'autre : l'un empêche la dérive d'une valeur juste, l'autre établit
qu'elle l'est.

**Mesurer la redondance intra-bloc.** `report_redundancy.py` ne compte par défaut que les
paires **entre blocs différents** (`if b1 == b2: continue`) : c'est l'unité dans laquelle
tous les chiffres du projet sont exprimés, de 301 au départ à 147 aujourd'hui, et **ce
comportement par défaut ne doit pas changer** sous peine de rendre les mesures
incomparables. Le drapeau `--intra` ajoute les paires internes à un même bloc, comptées
et affichées **séparément** :

```bash
python3 scripts/amboss/report_redundancy.py --intra
```

Cet angle mort n'avait jamais été mesuré. Il n'était visible que par ricochet — deux items
d'un même `resume` s'appariant au même item de la `presentation` (AMBOSS-1, échographie ;
AMBOSS-31, radiographie). Attention à l'interprétation : une bonne part de l'intra-bloc
d'`annexe-dd` est **structurelle et légitime**, le même argument valant sous plusieurs
hypothèses du différentiel (« nausées et vomissements » figure sous six hypothèses
d'AMBOSS-1). Le chiffre intra-bloc mesure, il ne prescrit pas.

**Toujours vérifier par les scripts, jamais par un `grep` direct.** Les scripts
appliquent `lib.strip_base64` avant toute recherche ; un `grep` brut, lui, fouille
aussi les images encodées, qui pèsent 95 % des fichiers. L'alphabet base64 contient
les lettres, les chiffres, `+` et `/` : n'importe quelle courte séquence de ces
caractères y apparaît par hasard. Constaté en tâche 7 — `grep g/dL` renvoyait trois
occurrences (AMBOSS-33 ×1, AMBOSS-34 ×2), toutes à l'intérieur de blobs d'image
(`…HvU8Jjtt0Mj/MQMVPEks9yEI2g/dLLxj1oAzRDvlVZ…`), alors qu'il n'en restait aucune
dans le texte. Un motif contenant un caractère hors alphabet base64 (accent, `³`,
espace) est immunisé ; les autres ne le sont pas.

**Les règles d'unités SI ne visent que les résultats de laboratoire.** Elles ne
s'appliquent ni aux posologies ni aux concentrations administrées. Cas à protéger,
déjà rencontré : `PC20 = 4 mg/mL` et `PC20 < 8 mg/mL` en AMBOSS-18 désignent la
concentration de méthacholine inhalée, dont `mg/mL` est l'unité internationale
correcte — bannir `mg/mL` corromprait le seuil diagnostique de l'asthme.
L'exception est répétée en commentaire dans `check_nomenclature.py`, à côté de la
table `BANNED`, là où une passe future irait l'ajouter.

**Angle mort assumé : les numérations en unité implicite.** `check_nomenclature.py`
cherche des unités ; une valeur écrite sans unité lui échappe par construction, et
aucun motif ne peut l'attraper — « GB 8500 » ne contient rien à détecter. Ces
numérations sanguines sous-entendent le `/mm³` et doivent se lire en `G/L`
(× 0,001). La recherche exhaustive a été faite **une fois**, en tâche 7, sur les
40 grilles — tout nombre ≥ 1000 au voisinage d'un terme d'hémogramme (GB, globules
blancs, leucocytes, plaquettes, thrombocytes, PNN, neutrophiles, lymphocytes,
éosinophiles) — et n'a donné que trois cas, tous corrigés : AMBOSS-18 « GB 8500 »
→ 8.5 G/L, AMBOSS-31 « leucocytes 12 000 » → 12 G/L, AMBOSS-33 « GB 15 000 » →
15 G/L. **Le corpus est propre à cette date, mais rien ne le maintiendra propre :**
toute grille nouvelle, réécrite ou réimportée doit être relue à la main sur ce
point, car aucun garde-fou automatique n'est possible. Un garde-fou qui ne peut pas
exister doit au moins être documenté comme absent.

**Le seuil « ≥ 1000 » de ce balayage était lui-même un angle mort.** Il a laissé passer
le seuil d'éosinophiles d'AMBOSS-19 — « CSI si éosinophiles > 300 », sans unité, à trois
chiffres donc sous le seuil de recherche. Le défaut a survécu à la tâche 7, à la
vérification finale et à la première phase entière ; il n'a été trouvé qu'en relançant le
même balayage **sur les valeurs à trois chiffres**. Retenir : le critère d'un balayage
exhaustif est aussi faillible que le motif d'un script, et il n'en laisse aucune trace.

**Deux graphies pour la même unité : `/mm³` et `/µL`.** Elles sont strictement
équivalentes (300/µL = 0,3 G/L) et la table `BANNED` ne portait que la première. La
tâche c6 a donc « corrigé » l'unité implicite d'AMBOSS-19 en `≥ 300/µL` — juste sur le
fond, non suisse dans la forme — et `check_nomenclature.py` est resté vert, son propre
journal notant que `/µL` était « hors table `BANNED` ». Les deux occurrences sont
maintenant en `G/L`, et le motif a été ajouté à la table. Il **exige un terme
d'hémogramme devant la valeur**, et c'est délibéré : une numération de LCR se rend
justement par µL et jamais en G/L (« PL : GR 50 000 » d'AMBOSS-33, ci-dessus). Bannir
`/µL` tout court signalerait à tort la seule écriture correcte de ce cas.

Deux corollaires vérifiés en même temps :

- `g/L` (hémoglobine, protéines) et `G/L` (numérations) peuvent cohabiter sur une
  même ligne — « FSC : Hb 112 g/L, leucocytes 12 G/L » en AMBOSS-8 et AMBOSS-31.
  C'est la convention du vault, qui écrit `G/L` sans glose et mélange les deux
  notations au besoin (« plaquettes ≤ 100 G/L », « fibrinogène < 1.5 g/L »). La
  casse seule les distingue : ne pas « harmoniser » l'une sur l'autre.
- Une numération de **LCR** ne se convertit pas en `G/L` : AMBOSS-33 porte
  « PL (si faite) : GR 50 000 », qui est un compte d'érythrocytes dans le liquide
  céphalorachidien, conventionnellement rendu par µL (ou ×10⁶/L), jamais en G/L.
  Le champ des règles ci-dessus est l'hémogramme, pas tout compte cellulaire.

**Piège d'outillage corrigé : `visible_text()` et le chevron nu.** Jusqu'à sa
correction, `lib_amboss.visible_text()` retirait les balises par
`re.sub(r"<[^>]+>", " ", …)`, qui traite tout `<` comme une ouverture de balise.
Or les grilles écrivent des seuils de laboratoire avec des chevrons nus —
`<li>6. Transfusion si Hb < 70 g/L (< 90 si coronarien)</li>` — et le `<` de
« < 70 » ouvrait une **pseudo-balise** que le motif refermait sur le `>` du
`</li>` qui suit, avalant toute la clause : `visible_text()` rendait
« 6. Transfusion si Hb », et « < 90 si coronarien » disparaissait de tout texte
de recherche, sans trace. Le défaut frappe précisément les valeurs de
laboratoire — la donnée la plus sensible du corpus — puisque ce sont elles qui
s'écrivent avec un chevron nu. Une recherche exhaustive du motif (chevron nu
suivi d'un chiffre, fichier entier après `strip_base64`) trouve des dizaines
d'occurrences réparties sur la majorité des 40 grilles : ce n'est pas un cas
isolé, c'est une classe entière de contenu qui échappait à toute recherche
fondée sur `visible_text()`.

Ce que le défaut épargnait, et pourquoi : `check_nomenclature.py` travaille sur
`strip_base64(html)` directement, jamais sur `visible_text()` — il est resté
fiable. `list_items()` (utilisé par `report_redundancy.py` et
`check_no_loss.py`) capture l'intérieur d'un `<li>` par
`r"<li[^>]*>(.*?)</li>"` **avant** de passer chaque fragment à
`visible_text()` : le `</li>` qui aurait refermé la pseudo-balise n'est déjà
plus dans le fragment isolé, donc aucun `>` n'y reste pour l'avaler — la
clause y survit. Ces deux scripts sont restés fiables par construction, pas
par accident : vérifié en confirmant qu'aucune de leurs sorties (ni le total
de `report_redundancy.py`, ni la liste de `check_no_loss.py` sur l'ensemble du
projet) ne change entre l'ancien et le nouveau `visible_text()` — identiques
au bit près.

Corrigé : `visible_text()` ne retire plus qu'une vraie balise — `<` ou `</`
suivi **immédiatement** d'une lettre ASCII, la seule syntaxe qu'une vraie
balise HTML respecte —
`re.sub(r'</?[a-zA-Z][a-zA-Z0-9]*(?:\s[^>]*?)?/?>', " ", …)`. Un chevron nu,
qu'il soit suivi d'un chiffre ou d'un espace puis d'une lettre, n'ouvre plus de
pseudo-balise. Limite résiduelle assumée : une lettre **collée** à un `<` nu
sans espace (`<N` et non `< N`) reste indiscernable d'un vrai début de balise
et peut encore être avalée jusqu'au `>` suivant. Vérifiée absente des 40
grilles à cette date (tout `<lettre` du corpus correspond à une vraie balise
HTML/SVG connue), mais rien ne garantit qu'une grille future n'introduira pas
ce style d'écriture — angle mort à surveiller, du même ordre que les
numérations en unité implicite ci-dessus.

**Règle pratique : ne jamais chercher du texte dans une grille avec
`re.sub(r"<[^>]+>", …)`, ni faire confiance à un `visible_text()` dont on n'a
pas vérifié qu'il porte ce correctif.** Pour chercher un seuil ou toute valeur
susceptible d'être adjacente à un `<` nu, préférer le HTML brut après
`strip_base64` (comme `check_nomenclature.py`) — c'est la méthode qui ne peut
pas être trompée par ce piège, corrigé ou non.

**Le même piège produit aussi des faux positifs, pas seulement des faux négatifs.** La
tâche c6 a signalé « AMBOSS-27 · `expert` : *Cortisol 8h bas (* — parenthèse ouverte
jamais fermée, contenu perdu ». Le texte réel est `Cortisol 8h bas (< 100 nmol/L)` : il
est complet. Ce qui a été signalé, c'est ce qu'un motif du genre `Cortisol[^<]{0,80}`
rend — il s'arrête sur le `<` du seuil. Vérification faite depuis : sur les 40 grilles,
**aucun `<li>` ne porte de parenthèses déséquilibrées**, et neuf autres grilles écrivent
la même construction `(< valeur)` sans que personne l'ait jamais signalée. Avant de
déclarer un texte mutilé, contrôler qu'un chevron nu n'a pas simplement borné la
recherche.

Avant de commit une grille dédoublonnée, vérifier aussi qu'aucune information n'a
disparu (règle du § 3) :

```bash
python3 scripts/amboss/check_no_loss.py HEAD AMBOSS-N_
```

Compare la zone pédagogique de `HEAD` (avant les modifications en cours) à l'état
du disque — utiliser une autre référence si le dédoublonnage a démarré ailleurs.
C'est un **rapport, pas un test** : il sort toujours avec le code 0, y compris
quand il signale des disparitions ; ne jamais le câbler comme porte bloquante.
Chaque item « disparu » listé doit être relu : la plupart sont des fusions ou des
reformulations (le seuil de ressemblance, identique à `report_redundancy.py`, ne
reconnaît pas les paraphrases) — ne creuser que ceux dont le contenu ne se
retrouve nulle part ailleurs dans le fichier, y compris hors de la zone
pédagogique (ex. un critère noté).

**Angle mort corrigé : une variante de classe non prévue rend un bloc entier
invisible à l'outillage.** `BLOCKS` (`lib_amboss.py`) repérait le bloc
`presentation` par une seule classe, `presentation-patient`. AMBOSS-34 porte sa
fiche de présentation orale sous `annexe-item annexe-presentation` — seule
variante de ce type sur les 40 grilles (24 emploient la classe standard, 15 n'ont
aucun bloc `presentation`). La conséquence dépassait la simple non-détection :
faute d'alternative dans le marqueur de fin de `theorie` (qui ne cherchait que
`presentation-patient` ou `annexe-item annexe-scenario`), le bloc `presentation`
d'AMBOSS-34 tout entier était englouti dans le segment `theorie` — 13 382
caractères mesurés avant correctif (segment `theorie` : 20067 → 6685 après ;
segment `presentation` : 0 → 13382). `blocks_present()` ne listait donc pas
`presentation` pour cette grille, et `report_redundancy.py` comparait sa
présentation orale au reste du corpus sous l'étiquette « theorie » : la
redondance d'AMBOSS-34 n'avait jamais été mesurée sur son contenu réel. L'unique
paire qu'affichait `report_redundancy.py AMBOSS-34_` avant correctif était un
artefact de cet étiquetage — après correctif, la mesure réelle donne 0 paire.

Le seul indice disponible, avant toute recherche du défaut, était ce chiffre de
redondance anormalement bas pour une grille à quatre blocs — sans qu'aucun
contrôle ne le signale : `check_invariants.py` et `check_nomenclature.py`
passent tous deux sur `strip_base64(html)` ou sur un compte brut de motifs,
indifférents au découpage en blocs, et `blocks_present()` ne peut chercher que
les classes qu'on lui a explicitement dites de reconnaître. Rien n'empêcherait
une grille future d'introduire une troisième variante de classe pour un bloc
existant, ou une classe pour un bloc qu'aucune grille ne porte encore : ce
serait le même défaut, avec le même unique symptôme observable (une redondance
anormalement basse sur cette grille précise), sans garde-fou automatique
possible par construction. Corrigé pour ce cas précis — `BLOCKS` accepte
désormais les deux classes du bloc `presentation`, marqueur de fin de `theorie`
inclus — mais le principe reste un angle mort à surveiller, du même ordre que
les numérations en unité implicite et le chevron nu ci-dessus.

La classe n'a **pas** été renommée dans la grille : corriger un outil ne doit
pas se faire en modifiant les données qu'il lit. Vérifié dans
`cases/case-styles.css` : `annexe-presentation` ne porte aucune règle CSS
propre (recherche exhaustive du sélecteur, zéro résultat). Le bloc hérite donc
du seul style générique `.annexe-item` (fond blanc, bordure grise fine,
`case-styles.css:591-595`) — ni le fond `#ffecd2` et le bandeau `#fa709a` que
`.presentation-patient` donne aux 24 autres grilles, ni une couleur dédiée
comme en reçoivent les trois autres variantes d'`annexe-item`
(`.annexe-expert`, `.annexe-theorie`, `.annexe-scenario`, chacune stylée).
Écart visuel préexistant, distinct du défaut d'outillage corrigé ici et sans
incidence sur le contenu ni le barème : signalé pour arbitrage éditorial
séparé, non traité par cette tâche.

**Angle mort corrigé : la double invisibilité d'`annexe-dd`.** Le bloc échappait à
tout l'outillage pour **deux** raisons cumulées, chacune suffisante à elle seule —
c'est ce qui l'a fait passer inaperçu si longtemps :

1. *Hors périmètre.* Situé dans la section Management, il est en amont de la zone
   que délimite `peda_bounds()`. `BLOCKS` ne le connaissait pas, donc
   `blocks_present()` ne le listait pas et `block_segment()` ne pouvait pas le
   rendre.
2. *Hors format.* Ses arguments sont des **puces textuelles `•`** séparées par des
   `<br>`, pas des `<li>`. Même à l'intérieur du périmètre, `list_items()` — donc
   `report_redundancy.py` et `check_no_loss.py` — n'aurait rien vu de son contenu :
   chacun de ses 257 `<li>` porte un diagnostic différentiel **entier**, et n'aurait
   été rendu que comme un seul bloc de texte indifférencié.

Corrigé sur les deux fronts : `BLOCKS` gagne le bloc et ses bornes ; `list_items()`
découpe désormais sur `•`. **Un `<li>` qui contient des puces est rendu par ses
puces seules, jamais aussi par son texte entier** — sinon le même contenu serait
compté deux fois, une fois groupé et une fois éclaté, et chaque doublon avec un
autre bloc serait rapporté en double. Hors `<li>`, seules les puces sont retenues,
le texte précédant la première étant jeté faute de borne gauche.

L'extension est **rétro-compatible au bit près** : l'extraction des quatre blocs
préexistants est inchangée, vérifiée item par item sur les 40 grilles. Un seul
d'entre eux contient des puces (le `resume` d'AMBOSS-34, 6 puces) et chacune y ouvre
son propre `<li>`, si bien que la découpe rend exactement ce que `norm()` — qui
efface déjà le caractère `•` — rendait auparavant. Conséquence : les **65 paires**
du périmètre restreint sont toutes conservées, et les **175** que le corpus gagne
viennent toutes du seul `annexe-dd` (total : **240**).

**Pourquoi la découpe ne porte que sur `•`, et pas sur `→`.** Le bloc écrit son
examen discriminant `→ US abdominale`, et il aurait été tentant d'en faire un item.
Mais la flèche est d'usage courant **ailleurs** dans le corpus — 211 occurrences
dans `presentation`, 67 dans `theorie`, 23 dans `resume`, 5 dans `expert`. Découper
dessus aurait modifié l'extraction des quatre blocs préexistants et cassé la
comparabilité avec les mesures antérieures. La flèche reste donc collée à la
dernière puce du diagnostic : limite assumée, et la raison pour laquelle
`report_redundancy.py` ne sait pas isoler un examen discriminant.

**Compter les paires, pas les duplications.** `report_redundancy.py` compare les
items deux à deux : quand un même argument est répété sous plusieurs diagnostics du
bloc — cas fréquent, « nausées et vomissements » figure sous six hypothèses
d'AMBOSS-1 — chaque occurrence produit sa propre paire. Les **175** paires
`annexe-dd` correspondent à **153 duplications distinctes** (15 démultipliées,
multiplicité maximale 6). Le chiffre du script est le bon pour suivre une tendance ;
c'est le nombre de duplications distinctes qui mesure le travail à faire.

## Interdits

- Lire un fichier de grille en entier (jusqu'à 2,77 Mo).
- Réécrire un fichier complet — utiliser le remplacement exact de chaîne.
- Modifier `.criteria-text` : le format `N. Libellé [réponse]` est requis par
  `cases/scoring.js:159`.
- Retirer les crochets `[...]` des réponses patient (`cases/scoring.js:290`).
- Ajouter ou retirer un sous-item noté.
- Toucher aux items ICE du critère `m4`.
- Créer un bloc `resume` ou `presentation` absent.
- Supprimer une section ou une sous-section sans l'avoir comparée item par item au
  bloc canonique — y compris quand un axe en prescrit la suppression.

## Glossaires d'abréviations dans les légendes de schéma

Certaines images (base64, jamais modifiées) affichent des abréviations
anglophones imprimées dans le schéma lui-même (ex. `CBC`, `BMP`, mais aussi
`EGD`/`NPO` en AMBOSS-11, `CTPA`/`PERC`/`PTP` en AMBOSS-12, `UL`/`ML`/`LL`
en AMBOSS-31, `A`/`Vc` en AMBOSS-1). La légende HTML adjacente
(`annexe-description`) sert de glossaire de traduction au format
`ABREV : explication`. Dans ce cas précis, et dans ce cas seulement :

- La **clé** reste l'abréviation d'origine, telle qu'imprimée dans l'image —
  c'est elle que le lecteur voit dans le schéma et doit pouvoir retrouver.
- La traduction / l'équivalent suisse va en **valeur**, après le « : ».

Exemple (AMBOSS-33, schéma « Prise en charge de la méningite ») :
`BMP : chimie sanguine (panel métabolique de base)` — jamais
`chimie sanguine : panel métabolique de base` (la clé ne serait plus dans
l'image, le lien légende ↔ schéma serait rompu).

`check_nomenclature.py` encode cette exception par un lookahead négatif —
`r"\bCBC\b(?! : )"`, `r"\bBMP\b(?! : )"` — qui exempte uniquement la forme
clé-de-glossaire (terme immédiatement suivi de « : »). Toute autre occurrence
de `CBC`/`BMP` comme terme médical ordinaire reste détectée normalement.

Applicable aux tâches 4 à 15 : toute légende de schéma anglophone rencontrée
doit suivre la même règle (clé = abréviation d'origine, valeur = traduction).
