# Intégration des grilles ECOS dans les pages SSP du vault Obsidian — Design

Date : 2026-07-23 · Statut : pilote + généralisation implémentés (443/451 grilles sur 109 pages)

## Problème

Relier les 451 grilles interactives de `grilles-ecos` aux pages `SSP ECOS/*.md` du vault
Obsidian (`~/Documents/Damien/Medecine/Obsidian`), images et interactivité comprises.

## Décision

**Liens https vers l'app déployée** (`https://grilles-ecos.replit.app`), présentés dans une
vignette repliée en tête de chaque page SSP. Ni copie des HTML dans le vault, ni conversion
Markdown, ni iframe.

Justification :

- Les HTML de grilles dépendent de 5 fichiers partagés (`cases/case-styles.css`,
  `mobile-responsive.css`, `theme-sync.js`, `scoring.js`, `persistence.js`) : un fichier
  copié seul perd style et interactivité.
- L'interactivité (modes Révision/Examen, minuteur, scoring, persistance localStorage,
  SRS SM-2) ne survit pas dans Obsidian, qui n'exécute pas les `<script>` des notes.
- Le déploiement Replit est **privé** (Replit Shield → `replit.com/deployment-login`) :
  un `<iframe>` dans Obsidian ne peut pas s'authentifier ; un lien ouvert dans un
  navigateur/webview connecté à Replit fonctionne. Le maintien en privé est volontaire
  (contenu dérivé d'AMBOSS/USMLE — ne pas exposer publiquement).
- Le vault est sous Obsidian Sync : dupliquer 451 fichiers de 0,1–2,7 Mo (images JPEG
  en base64) dégraderait la synchronisation.
- Une seule source de vérité : les grilles évoluent dans ce repo, les pages SSP ne
  portent que des liens.

## Format d'intégration (validé sur le pilote)

Callout `[!figure]-` placé **juste sous** le titre `## 📚 Références PDF`, **hors** du
`[!vrow|full]` des vignettes PDF (révision du 2026-07-23 : pas en vignette) :

```markdown
## 📚 Références PDF
> [!figure]- 🥼 Grilles ECOS interactives (N)
> **AMBOSS**
> [AMBOSS-1 — Femme 47 ans, douleurs abdominales — Urgences](https://grilles-ecos.replit.app/cases/amboss/….html)
> [AMBOSS-2 — …](…)
> 
> **German**
> [German-15 — Femme 73 ans, douleurs abdominales — Cabinet MG](…)
> …
> 
> 🔐 [Application complète](https://grilles-ecos.replit.app/) — connexion Replit requise

> [!vrow|full]
> > [!vignette]- 🩺 SSP-…
```

- Icône 🥼 (blouse blanche), callout replié par défaut (`-`).
- Groupement par corpus en gras, **un lien par ligne** (pas de séparateurs `·`).
- Libellés détaillés `ID — sexe/âge, motif — lieu de consultation`, extraits des lignes
  `👤` (patient) et `📍` (lieu) de l'en-tête HTML de chaque grille ; pour CasECOS
  (structure différente, sans 👤/📍), depuis le `<title>`.
- Le plugin core Obsidian **Web viewer** est activé : sur desktop les liens s'ouvrent
  dans Obsidian avec session Replit persistante (connexion une seule fois).

## Schéma d'URL

`https://grilles-ecos.replit.app/cases/{corpus}/{fichier}.html`

- Corpus `amboss`, `german`, `rescos`, `usmle`, `triage` : noms de fichiers en ASCII pur
  (accents aplatis en `_`, ex. `te_le_phonique`) → URL = nom de fichier tel quel.
- Corpus `casecos` : espaces et accents réels → percent-encoding en **NFC**
  (hypothèse : git macOS a précomposé les noms au commit). À confirmer au premier clic
  authentifié ; si 404, réencoder en NFD.

## Pilote réalisé (2026-07-23)

`SSP ECOS/SSP — Douleur Abdominale.md` : bloc `[!figure]- 🥼` avec 25 grilles —
AMBOSS 1/2/3 · German 15–21 · RESCOS 17–23 · USMLE 13/31 · Triage 16/19/36 ·
CasECOS Crohn / Cancer gastrique / Appendicite (Olivia Veyre).

Choix de mapping actés pour la suite :

| Grilles | Page SSP cible |
|---|---|
| CasECOS chirurgicaux (AAA ×3, ulcère perforé, abdomen aigu ×2, traumas ×2) | SSP — Urgences Abdominales Chirurgicales |
| AMBOSS-15 (douleur abdominale chronique, enfant 6 ans) | future page pédiatrique |
| German-49 (gonflement abdominal) | SSP — Ballonnement (Météorisme) |

## Généralisation (réalisée le 2026-07-23)

443/451 grilles mappées sur **109 pages** (107 SSP + 2 Skills). 86 pages ont reçu une
section `## 📚 Références PDF` créée juste après le frontmatter (elles n'en avaient pas),
22 une insertion dans leur section existante, 1 remplacement (pilote).

Artefacts :

1. **`docs/obsidian-mapping.yaml`** — source de vérité : chaque grille → page cible +
   libellé. Éditable à la main (changer une cible, corriger un libellé), puis relancer
   le script. Section `unmapped:` avec la raison pour les 8 grilles sans page.
2. **`scripts/inject_obsidian_blocks.py`** — injection idempotente : le bloc est reconnu
   structurellement (callout commençant par `> [!figure]- 🥼 Grilles ECOS interactives`,
   fin à la première ligne ne commençant pas par `>`) et remplacé ; page inchangée si le
   bloc est identique (pas de marqueurs HTML nécessaires). Crée la section Références PDF
   si absente. `--dry-run` disponible. Une ligne vide est garantie après le bloc (deux
   callouts adjacents fusionneraient).
3. Libellés générés depuis les lignes 👤 (sexe/âge + motif) et 📍 (lieu abrégé) des HTML ;
   depuis le `<title>` pour CasECOS. Les 25 libellés du pilote sont figés à l'identique.

Décisions de mapping notables (validées par sondage du contenu des grilles) :

- BBN (RESCOS-7/8) = Breaking Bad News → `Skills — Annonce Mauvaise Nouvelle (SPIKES)` ;
  EM Tabac / EM Vaccinations → `Skills — Entretien Motivationnel` (seules cibles Skills).
- Médico-légal (violences conjugales, agression sexuelle, maltraitance, consentement,
  aptitude à la conduite, AMBOSS-24 « évaluation après chute » = violence conjugale
  vérifiée dans le contenu) → `SSP — Capacité de Discernement & Éthique`.
- CasECOS chirurgicaux abdominaux (AAA ×4, ulcère perforé, abdomen aigu, traumas,
  fuite anastomotique, diverticulite abcédée) → `SSP — Urgences Abdominales Chirurgicales`.
- German-26 « douleur aux jambes » = ischémie aiguë (vérifié) → AOMI ; German-50
  « gonflement du visage » = œdème palpébral → Syndrome Néphrotique ; German-64
  « obésité » adulte → Syndrome Métabolique (PAS Obésité Pédiatrique).

Non mappées (8) — pages manquantes dans le vault : masse mammaire/sein (German-62,
Triage-10, GynObs-V3), douleur abdominale pédiatrique (AMBOSS-15), évaluation
préopératoire (MCPR-ARC21), TDAH adulte (Psy-P12), paraphilie (Psy-P2), autisme
adulte (Psy-P4). Si ces pages sont créées un jour : les ajouter au YAML et relancer.

Pièges rencontrés : normalisation NFC/NFD — les clés accentuées doivent être normalisées
avant comparaison avec les noms de fichiers du disque (NFD sur macOS) ; le script
normalise les deux côtés. Sauvegarde pré-injection :
`~/Developer/ECOS-backups/pre-grilles-ecos-2026-07-23/`.

## Grilles locales hors app (ajout du 2026-07-23)

33 grilles RESCOS-41 à 69 vivent dans le vault
(`_bibliotheque/rescos-grilles-locales/`) et ne sont pas déployées sur Replit.
Dans le YAML, leur `file:` est le chemin relatif au vault (pas de préfixe `cases/`) ;
le script génère alors un lien `file://` percent-encodé (NFC) au lieu d'une URL https,
les groupe sous **RESCOS** (préfixe du nom de fichier), et ajoute la légende
« 📁 = grille locale » au pied du bloc des pages concernées (suffixe 📁 dans le libellé).
Libellés écrits à la main dans build_mapping (pas de parsing). Cibles supplémentaires :
`Skills — Présentation de Cas` (RESCOS-54, 55, 64-station 2) et `Skills — Décision
Partagée` (RESCOS-60 iléus palliatif). Limites : liens valides sur cette machine
uniquement (desktop) ; à terme, déployer ces grilles dans l'app rendrait les liens
universels. Images : 11/14 restaurées en base64 (retrouvées sur disque, vérifiées
visuellement) ; manquent zona thoracique (RESCOS-68) et 2 radios d'humérus (RESCOS-69).

## Hors périmètre

- Améliorations de l'app elle-même (via ce repo GitHub ou Replit directement).
- Extraction d'images des grilles vers le vault (les images restent en base64 dans les HTML).
- Résumés statiques des critères dans les pages SSP (option écartée au design : duplication).
