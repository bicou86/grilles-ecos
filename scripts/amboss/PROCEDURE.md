# Procédure de traitement d'une grille AMBOSS

Référence : `docs/superpowers/specs/2026-07-30-amboss-refonte-pedagogique-suisse-design.md`

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
| `resume` | Réviser vite — **source canonique** | Redites de la théorie, formats oraux |
| `presentation-patient` | Restituer à l'oral | Toute donnée clinique nouvelle |

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
python3 scripts/amboss/check_invariants.py    # doit sortir OK
python3 scripts/amboss/check_nomenclature.py  # doit sortir OK
```

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
