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
- **Management** : un bloc commun, puis un sous-bloc par diagnostic.

La clé de regroupement est **(SSP, diagnostic)** : deux cas de corpus différents portant
le même diagnostic sous la même SSP fusionnent en un seul sous-bloc de management.

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

**Non tranché** : `usmle` (44) et `triage` (40), que la demande initiale ne mentionne pas
et qui figurent pourtant au mapping. À décider avant l'étape 5.

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
qui les rend inexploitables telles quelles. Les 49 fichiers de `.azygos-extraction/*.json`
gardent la séparation :

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
les dix SSP à 4 cas et plus.

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
   l'adosser au mapping SSP. Sortie de contrôle : un mémento par SSP **sans fusion**,
   cas juxtaposés, pour vérifier que l'extraction tient sur 257 grilles.
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

## Risques et limites

- **Le diagnostic déduit peut être faux.** Le champ `confiance` le signale, mais un
  `premier-dd` erroné place des items sous le mauvais sous-bloc. D'où la relecture
  obligatoire de l'étape 2 avant toute fusion.
- **Ces mémentos ne sont pas officiels.** Ils extrapolent la forme des 9 grilles fédérales
  à des grilles qui n'ont jamais été validées par un jury. L'encadré de tête doit le dire.
- **Le vocabulaire canonique est un travail sans fin naturelle.** Le critère d'arrêt
  retenu est fonctionnel : on cure tant que le mémento d'une SSP contient des doublons
  visibles, pas au-delà.
- **AZYGOS dépend d'un dossier non versionné.** `.azygos-extraction/` n'est pas dans git.
  Si les mémentos AZYGOS en dépendent, ce dossier doit être versionné ou son contenu
  utile recopié dans le dépôt.

## Décisions prises

- Approche **B sur socle A** pour l'appariement.
- Marquage par **suffixe `*(diagnostic)*`**, pas par surlignage.
- Découpage en **cinq étapes**, chacune relue avant la suivante.
- Les **32 SSP à cas unique sont générées** malgré l'absence de fusion.
- `rescos-locales` et `casecos` **reportés**, pas abandonnés.
