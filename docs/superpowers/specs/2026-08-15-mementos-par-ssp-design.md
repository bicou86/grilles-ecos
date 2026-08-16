# Mémentos ECOS par SSP — fusion multi-cas et subdivision par diagnostic — Design

Date : 2026-08-15 · Statut : design validé, implémentation à planifier

## Problème

Neuf grilles officielles (entraînements fédéraux 2025-2026) ont été alignées sur leur
document papier et condensées en un mémento — `docs/obsidian-memento/Mémento ECOS —
Grilles officielles.md`, produit par `scripts/build_obsidian_memento.py`. Ce mémento
liste, cas par cas, les items d'anamnèse, de status et de management attendus, sans
barème ni réponses du patient.

Il faut étendre ce format aux grilles **non officielles** du dépôt, dont le contenu est
médicalement riche mais dont aucune version officielle n'existe pour arbitrer. Deux
difficultés :

1. **Beaucoup de cas partagent une même SSP** — Douleur Abdominale en compte 17,
   Douleur Thoracique 11 — mais portent des diagnostics différents (STEMI, péricardite,
   embolie…). Un mémento par cas produirait 257 fichiers largement redondants : les
   anamnèses et les status d'une même SSP sont presque superposables.
2. **Le management, lui, diverge fortement selon le diagnostic.** Un bloc unique le
   rendrait faux ; un bloc par cas le rendrait illisible.

## Décision

**Un mémento par SSP**, fusionnant tous ses cas. À l'intérieur :

- **Anamnèse et status** : items mis en commun. Un item qui n'apparaît que dans une
  partie des cas est suffixé du ou des diagnostics qui le portent.
- **Management** : un bloc commun, puis **un sous-bloc par diagnostic attendu de la SSP**,
  y compris ceux qu'aucune grille du corpus ne documente — un sous-bloc vide signale alors
  une lacune de révision (« ce diagnostic tombe à l'ECOS, tu n'as aucune grille dessus »)
  et non un défaut de génération. La liste des diagnostics attendus vient de
  `docs/ecos-priorites-2026.yaml`, pas seulement des grilles.

La clé de regroupement est **(SSP, diagnostic)** : deux cas de corpus différents portant
le même diagnostic sous la même SSP fusionnent en un seul sous-bloc de management.

## Les neuf grilles officielles comme référentiel

C'est le principe directeur de tout le reste. Les 257 grilles à traiter n'ont jamais été
validées par un jury ; les neuf grilles officielles, si. Elles ne servent donc pas
seulement de modèle de mise en forme : **elles sont l'autorité sur ce qui constitue un
item de mémento**, et chaque décision d'inclusion, de granularité ou de vocabulaire doit
pouvoir s'y adosser.

Ce qu'elles enseignent, et qui doit être transposé aux grilles non officielles :

- **La granularité.** Un item est un titre court (3 à 10 mots) éventuellement suivi de
  sous-items d'un ou deux mots — « Caractérisation de la fatigue » puis « Durée · Évolution ·
  Chronologie sur la journée · Circonstances de survenue ». Un libellé qui n'entre pas dans
  ce moule vient d'une grille qui mélange l'item et son commentaire, et doit être ramené à
  cette forme.
- **La structure d'une anamnèse.** Caractérisation du symptôme principal, puis symptômes
  associés, puis facteurs de risque et antécédents, puis habitudes, puis les questions de
  sécurité. Les neuf grilles suivent toutes cet ordre ; il donne l'ossature attendue d'un
  mémento fusionné.
- **La structure d'un management.** Hypothèse diagnostique, diagnostics différentiels,
  examens complémentaires, traitement, suivi. C'est ce squelette qui fonde le partage
  🔬 / 💊 : la table `EXAMENS` du générateur actuel, écrite ligne à ligne pour les neuf
  grilles, est la **semence** de la classification à généraliser.
- **Ce qui n'est pas un item.** Les lignes de synthèse (« Anamnèse en général »), les
  consignes destinées à l'expert·e, les réponses du patient et le barème sont exclus. Ces
  quatre règles d'exclusion sont déjà implémentées et éprouvées sur les neuf grilles ; elles
  s'appliquent telles quelles au reste.
- **Le vocabulaire.** Les libellés officiels sont les **formes canoniques par défaut** de
  `docs/ecos-vocabulaire.yaml`. Quand un libellé non officiel désigne la même chose qu'un
  libellé officiel, c'est le second qui l'emporte — pas une forme moyenne inventée. La table
  `NOMENCLATURE` du générateur actuel (« Formule sanguine complète » → `FSC`, « Paramètres
  inflammatoires (VS ou CRP) » → `VS / CRP`) est le premier morceau de ce vocabulaire.

Conséquence opératoire, à appliquer à chaque étape : **un item d'une grille non officielle
qui n'a aucun répondant dans les neuf grilles officielles est suspect**. Il n'est pas
supprimé d'office — le corpus officiel ne couvre que neuf SSP et ne peut pas tout prévoir —
mais il est signalé dans un rapport de contrôle, pour qu'une relecture décide s'il s'agit
d'un apport réel ou d'un artefact du corpus d'origine (les « Question initiale » d'AZYGOS,
les rubriques pédagogiques d'AMBOSS). Le rapport est produit à l'étape 1 et relu avant la
fusion.

Les neuf grilles officielles restent par ailleurs le **test de non-régression** de toute la
chaîne : leur mémento doit rester identique au bit près après chaque évolution du
générateur.

## Périmètre

**Inclus** (257 grilles) :

| Corpus | Grilles | Rattachement SSP |
|---|---|---|
| RESCOS | 80 | dans `docs/obsidian-mapping.yaml` (41 rattachées) |
| AMBOSS | 40 | idem |
| GERMAN | 88 | idem |
| AZYGOS | 49 | **absent du mapping**, à rattacher (étape 5) |

**Reporté à une phase ultérieure, explicitement** : `rescos-locales` (132) et `casecos`
(198). Ils figurent déjà dans le mapping SSP et sont donc prêts à être inclus le jour où
la chaîne aura fait ses preuves.

**Trou connu** : sur les 80 grilles RESCOS, **41 seulement sont rattachées** à une SSP
dans le mapping ; les 39 autres — dont les 9 officielles, ajoutées après la curation —
devront l'être à l'étape 1, sans quoi elles n'apparaîtront dans aucun mémento.

`usmle` (44) et `triage` (40) sont **reportés de la même façon** : ils figurent au mapping
SSP mais hors de la demande initiale. Décision prise le 2026-08-15, **confirmée le
2026-08-16** à l'ouverture du lot 2 : les quatre corpus reportés totalisent 414 grilles,
soit plus que les 252 traitées, et aucune n'a été relue ni pour son rattachement SSP ni
pour son diagnostic.

**Livraison en deux lots.** Le lot 1 ne traite que les SSP portant un diagnostic
« incontournable » ou « probable » de l'analyse de récurrence 2011-2025
(`ECOS_Priorites_2026.html`, hors dépôt) — 16 + 19 diagnostics pour 25 plaintes d'entrée
distinctes. Le lot 2 étend aux SSP restantes, puis à AZYGOS. Cette priorisation ne change
ni le format ni la chaîne : elle ordonne seulement le travail.

## État des lieux mesuré

Le mapping curé rattache **169 cas RESCOS + AMBOSS + GERMAN à 69 SSP**. La distribution
est très déséquilibrée, et c'est ce qui dimensionne le travail :

| Cas par SSP | Nombre de SSP | Nature du travail |
|---|---|---|
| 1 | 32 | Aucune fusion — le format des 9 officielles suffit |
| 2-3 | 27 | Fusion simple |
| 4 et plus | 10 | Le vrai travail de fusion |

Les dix gros : Douleur Abdominale 17, Douleur Thoracique 11, Toux Chronique 8, Œil Rouge 7,
Fatigue 6, Lombalgies 6, Céphalée 5, Diarrhée 5, et deux autres à 4.

**Les quatre corpus partagent le même balisage HTML** (`criteria-row` + `window.caseConfig`) :
l'extracteur écrit pour les 9 grilles officielles s'y applique sans modification.

**AZYGOS fait exception et demande une autre source.** Ses grilles HTML aplatissent le
label court et le paragraphe didactique dans un même `detail-text` de 100 à 250 mots, ce
qui les rend inexploitables telles quelles. Les 49 fichiers JSON — bruts dans
`.azygos-extraction/`, versionnés et projetés dans `docs/azygos-grilles/` depuis le
2026-08-16, cf. « Risques et limites » — gardent la séparation :

```
onglets → { "Anamnèse": [ {groupe, items: [{label, valeurs}]} ], … }
infos   → { "Anamnèse#0#0": "paragraphe didactique…" }
```

Les `label` y sont déjà de granularité mémento (« Question initiale · Dimension temporelle ·
Début · Évolution · Déclencheur · Localisation · Irradiation · Qualité »). **AZYGOS
s'extrait donc du JSON, pas du HTML.**

## Résolution du diagnostic

Aucun champ ne porte le diagnostic. Il se résout par une cascade, du plus fiable au moins :

1. **Critère de management explicite** — « Hypothèse diagnostique : X », « Diagnostic
   principal - X ». Présent dans 37/80 RESCOS, 48/88 GERMAN, 1/40 AMBOSS, 3/49 AZYGOS.
2. **Premier diagnostic du bloc `dd-category`** — le bloc pédagogique « Diagnostics
   différentiels à considérer », dont la première entrée est le diagnostic du cas
   (règle validée sur AMBOSS-1 → « Cholécystite aiguë »). Présent dans 40/40 AMBOSS,
   77/88 GERMAN, 59/80 RESCOS, **0/49 AZYGOS**.
3. **`Diagnostic de travail` du JSON AZYGOS** — présent dans 20/49 ; le label exact des
   29 autres reste à identifier.

Le résultat est écrit dans `docs/ecos-diagnostics.yaml`, avec un champ `confiance`
(`explicite` | `premier-dd` | `deduit`) qui rend chaque valeur relisible. **Ce fichier
est curé, pas régénéré aveuglément** : une valeur corrigée à la main doit survivre à une
réexécution.

## Appariement des items — socle A, curation B

C'est le point dur : « Début » chez l'un, « Début des symptômes » chez l'autre, « Douleurs »
et « Caractérisation de la douleur ». Sans appariement, la fusion produit des doublons.

**Socle A — normalisation lexicale, sans curation.** Minuscules, accents et numérotation
retirés, ponctuation réduite ; deux libellés dont les tokens significatifs coïncident sont
le même item. Déterministe, instantané, aucune relecture. Suffisant pour les 32 SSP à cas
unique et raisonnable jusqu'à 3 cas.

**Couche B — vocabulaire canonique curé, par SSP.** Une table
`docs/ecos-vocabulaire.yaml` fait correspondre les libellés bruts d'une SSP à un item
canonique. Elle n'est ouverte **que là où A échoue visiblement**, c'est-à-dire d'abord sur
les dix SSP à 4 cas et plus. **Ses formes canoniques sont d'abord celles des neuf grilles
officielles** (voir le référentiel ci-dessus) : on ne réinvente un libellé que lorsque le
corpus officiel n'en propose aucun.

```yaml
"Douleur Thoracique":
  "Caractérisation de la douleur": &douleur Caractérisation de la douleur
  "Douleurs": *douleur
  "Douleur thoracique": *douleur
```

Justification du choix (B sur socle A) plutôt que la normalisation seule ou une fusion
rédigée cas par cas :

- La normalisation seule sous-fusionne les synonymes et sur-fusionne les libellés courts
  et génériques — « Début » ne désigne pas la même chose selon la section qui le porte.
- Une fusion rédigée par IA donnerait la meilleure qualité mais n'est pas reproductible :
  une grille modifiée impose de tout refaire, et rien ne garantit que deux SSP soient
  traitées selon les mêmes critères.
- Le dépôt pratique déjà cette forme : `docs/obsidian-mapping.yaml` porte la mention
  « curation validée », et le mémento actuel a sa table `NOMENCLATURE`. La qualité y
  progresse par petites corrections auditées plutôt que par régénérations opaques.

## Marquage du spécifique

Un item d'anamnèse ou de status présent dans **tous** les cas de la SSP reste nu. Un item
présent dans une partie seulement est suffixé des diagnostics concernés, en italique :

```markdown
> - [ ] **3. Caractérisation de la douleur**
> 	- [ ] Localisation
> 	- [ ] Irradiation
> 	- [ ] Facteurs déclenchants *(STEMI, angor stable)*
> 	- [ ] Soulagement en antéflexion *(péricardite)*
```

Le surlignage `==…==` d'Obsidian a été écarté : il colore sans dire pourquoi, dépend du
thème et ne survit pas à l'export. Le suffixe est greppable et lisible en clair.

Au-delà de trois diagnostics, le suffixe est abrégé (`*(3 diagnostics)*`) pour ne pas
noyer la ligne ; le détail reste consultable dans les grilles liées.

## Format de sortie

Un fichier par SSP dans `docs/obsidian-memento/`, nommé `Mémento — <SSP>.md`, reprenant
la charte déjà validée : frontmatter typé, légende, `# Spécialité`, `## Cas`, encadrés
📋 / 🩺 / 🔬 / 💊, cases à cocher imbriquées, ⭐️ tirée du champ `priorite` du coffre.

Le mémento actuel des 9 grilles officielles **reste tel quel** : il est la référence de
forme et sert de test de non-régression. Les mémentos générés portent en tête un encadré
rappelant qu'ils sont **dérivés de grilles non officielles**.

Structure d'une SSP à plusieurs diagnostics :

```markdown
## Douleur thoracique — 6 cas, 4 diagnostics

> [!note] 📋 Anamnèse            ← items mis en commun, spécifiques suffixés
> [!tip] 🩺 Status               ← idem
> [!question] 🔬 Examens complémentaires — communs
> [!success] 💊 Management — commun
> [!success] 💊 — si STEMI
> [!success] 💊 — si péricardite
```

## Les cinq étapes

1. **Généraliser l'extracteur** aux quatre corpus, ajouter le lecteur JSON AZYGOS,
   l'adosser au mapping SSP, rattacher les 39 grilles RESCOS absentes. Deux sorties de
   contrôle : un mémento par SSP **sans fusion**, cas juxtaposés, pour vérifier que
   l'extraction tient sur 257 grilles ; et le **rapport d'écart au référentiel** listant
   les items sans répondant dans les neuf grilles officielles, à relire avant l'étape 3.
2. **Résoudre le diagnostic** par la cascade ci-dessus → `docs/ecos-diagnostics.yaml`,
   à relire avant de continuer.
3. **Fusionner** : appariement socle A, mise en commun anamnèse/status avec marquage,
   management commun + sous-blocs par diagnostic.
4. **Curer** les dix SSP à 4 cas et plus via `docs/ecos-vocabulaire.yaml`.
5. **Rattacher AZYGOS** au mapping SSP (49 grilles absentes), puis étendre. Décider à
   ce moment du sort d'`usmle` et `triage`.

Chaque étape produit un artefact vérifiable et s'arrête sur une relecture. L'étape 1 est
la seule qui doive tenir sur les 257 grilles avant qu'on aille plus loin.

## Vérification

- **Idempotence** : deux exécutions consécutives produisent des fichiers identiques au bit
  près. Déjà vrai du générateur actuel, à préserver.
- **Non-régression** : le mémento des 9 grilles officielles doit rester inchangé après la
  généralisation de l'extracteur.
- **Couverture** : tout cas rattaché à une SSP dans le mapping apparaît dans exactement un
  mémento ; tout cas non rattaché est listé explicitement, jamais perdu en silence.
- **Comptage** : le nombre d'items d'un mémento non fusionné égale la somme des items de
  ses grilles, lignes de synthèse et consignes expert·e exclues.
- **Conformité au référentiel** : la part d'items sans répondant officiel est mesurée et
  suivie SSP par SSP. Une SSP dont la majorité des items n'a aucun répondant signale une
  grille source hors format, pas un apport clinique.

## Risques et limites

- **Le diagnostic déduit peut être faux.** Le champ `confiance` le signale, mais un
  `premier-dd` erroné place des items sous le mauvais sous-bloc. D'où la relecture
  obligatoire de l'étape 2 avant toute fusion.
- **Ces mémentos ne sont pas officiels.** Ils extrapolent la forme des 9 grilles fédérales
  à des grilles qui n'ont jamais été validées par un jury. L'encadré de tête doit le dire.
- **Le vocabulaire canonique est un travail sans fin naturelle.** Le critère d'arrêt
  retenu est fonctionnel : on cure tant que le mémento d'une SSP contient des doublons
  visibles, pas au-delà.
- ~~**AZYGOS dépend d'un dossier non versionné.**~~ **Levé le 2026-08-16.** La branche
  « recopier le contenu utile » a été retenue contre `git add -f` : les 49 fichiers bruts
  portent 43 URL Supabase signées dont la query-string contient un JWT, et une
  ré-extraction en produit de nouvelles à chaque fois. `docs/azygos-grilles/` (0,29 Mo)
  ne garde que `meta` et, par onglet, le nom de groupe et le `label` de chaque item —
  exactement ce que `lire_azygos()` et `classifie_onglets()` lisent. Tous les noms
  d'onglet sont conservés, y compris les exclus, sans quoi le garde-fou des onglets
  inconnus n'aurait plus rien à examiner. `fige_azygos.py` prouve la fidélité en
  comparant le cas pivot des deux côtés ; `check_azygos.py` rejoue la comparaison quand
  le brut est présent et **dit** qu'il ne l'a pas faite quand il est absent.

## Décisions prises

- Les **neuf grilles officielles font autorité** sur ce qui constitue un item : granularité, ossature des sections, vocabulaire canonique, règles d'exclusion. Tout item sans répondant officiel est signalé pour relecture, jamais supprimé en silence.
- Approche **B sur socle A** pour l'appariement.
- Marquage par **suffixe `*(diagnostic)*`**, pas par surlignage.
- Découpage en **cinq étapes**, chacune relue avant la suivante.
- Les **32 SSP à cas unique sont générées** malgré l'absence de fusion.
- **Un sous-bloc de management par diagnostic attendu**, même sans grille pour le couvrir
  (décision du 2026-08-15). Le vide est une information, pas un trou.
- La table des priorités est **écrite et maintenue à la main** ; son `ssp` peut nommer une
  page SSP qui n'existe pas encore, à créer pour les plaintes fréquentes à l'ECOS.
- `rescos-locales` et `casecos` **reportés**, pas abandonnés.
- **Le lot 2 est ouvert (2026-08-16), en une seule fois.** Les 88 SSP reçoivent un
  mémento — 56 s'ajoutent aux 32 du lot 1, pour 252 grilles. Le découpage en tranches a
  été écarté sur un chiffre : des 56 SSP du lot 2, **23 ne portent qu'une seule grille**
  et n'ont donc rien à fusionner, et 23 des 33 restantes n'en portent que deux. Générer
  est gratuit et sans risque (aucune fusion à juger) ; c'est la **curation** qui coûte, et
  elle se découpe toute seule par le rapport de doublons.
- **`usmle` (44 grilles) et `triage` (40) restent hors périmètre**, comme
  `rescos-locales` (132) et `casecos` (198). Décision confirmée le 2026-08-16 : la chaîne
  a fait ses preuves sur 252 grilles, mais les quatre corpus doubleraient le corpus
  (+414 grilles) sans qu'aucune ait été relue pour son rattachement SSP ni pour son
  diagnostic. Ils entreront par un lot dédié, avec leur propre relecture.
- **La curation du lot 2 n'ouvre aucune famille de synonymes nouvelle.** Elle applique
  aux SSP qui entrent en périmètre les 25 familles propageables déjà adjugées en tâche 10,
  chacune restant jugée séparément par les neuf propriétés de `check_vocabulaire`. Motif :
  une famille nouvelle est un jugement clinique neuf, non relu ; une famille déjà adjugée
  est un jugement déjà rendu et déjà relu. Trois familles sont déclarées **non
  propageables** parce que la tâche 10 les avait acceptées pour une raison locale à HTA.
- **Le défaut par défaut de `build_memento.py` est le lot complet.** `nettoyer()` efface
  tous les mémentos avant de réécrire ceux du lot demandé : le dépôt commitant les 88, un
  appel sans argument sous l'ancien défaut en supprimait 56 en silence. Le lot 1 reste
  accessible par `--lot prioritaire`, et `mesure_couche_b.py` accepte le même drapeau —
  c'est le seul moyen de **rejouer** l'instrument sur un état dont on connaît déjà la
  réponse (2 743 / 1 480 / 1 579 sur 2 297, tâche 10).
