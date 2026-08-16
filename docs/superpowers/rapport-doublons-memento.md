# Doublons candidats — vocabulaire canonique

Paires d'items d'une même SSP que le socle A n'a pas appariés
mais dont la similarité dépasse 0.72.

Titres de tête **et** sous-items confondus : la couche B s'applique aux
deux. Les grilles porteuses suivent chaque libellé.

## Ce que « à juger » veut dire, et ce que ça ne veut pas dire

Les paires **à juger** viennent d'abord. « À juger » signifie **une seule
chose** : `check_vocabulaire` ne les refuserait pas. Ce n'est **pas** une
recommandation de les fusionner, et surtout pas en lot. Les neuf propriétés
du contrôle attrapent ce qu'une **grille** distingue ; elles ne voient pas
ce qu'un **clinicien** distingue. `Échographie abdominale` ⟷ `Échographie
vaginale` les passe toutes les neuf.

D'où deux sous-seaux, et lire le second **une paire à la fois** :

- **écart de forme** — les deux libellés disent les mêmes mots, à l'accord,
  au genre ou à la graphie près (`familial` / `familiaux`, `bi-manuelle` /
  `bimanuelle`). Réunir n'efface rien ;
- **écart de contenu** — un mot de contenu diffère, ou n'existe que d'un
  côté (`abdominale` / `vaginale`, `initiaux` / `urgents`, `des organes` /
  `des reins`). Réunir **efface une distinction clinique** : chaque paire
  est un jugement, pas une ligne d'une liste.

À l'intérieur de chaque sous-seau, tri par similarité **décroissante**.
⚠️ Ce tri est **local à la section** : le document, lui, est alphabétique
par SSP, donc la première paire du fichier n'est **pas** la plus plausible
du corpus. Les dix plus similaires (0,983 → 0,964) sont ailleurs —
`Auscultation cardio-pulmonaire` ⟷ `cardiopulmonaire`, `Palpation
bi-manuelle` ⟷ `bimanuelle`.

Suivent deux catégories à ne lire **que si tout le reste est traité** :

- **⚠️ inerte ou antonyme présumé**. *Inerte* : les deux titres ne vivent
  pas au même endroit (section ou parent différents), donc l'entrée ne
  réunirait rien et la propriété 7 la refuserait. *Antonyme présumé* : les
  libellés s'opposent par un motif connu (`hyper`/`hypo`, `flexion`/
  `extension`…) et **aucune grille ne les porte ensemble**, donc la
  propriété 8 n'a pas de témoin — c'est la seule classe que rien
  n'automatise, voir la section finale ;
- **⛔ irrecevable par construction** : soit l'entrée confondrait deux
  libellés qu'une grille distingue **dans une même section** (propriété 8
  — le test porte sur les signatures **après** la table, donc il attrape
  aussi les variantes et les fusions indirectes), soit les deux libellés
  ont **déjà la même signature** pour le socle A (propriété 6).

## AVP (Accident de la Voie Publique) — 3 cas · 3 à juger (0 de forme, 3 de contenu), 25 ⚠️, 17 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Antécédents et allergies` (RESCOS-6)  ⟷  `Antécédents médicaux et allergies` (RESCOS-5)
- `Circonstances de l'accident` (RESCOS-5)  ⟷  `Circonstances détaillées de l'accident` (German-5)
- `Antécédents de céphalées` (German-5)  ⟷  `Antécédents et allergies` (RESCOS-6)

- ⚠️ `Date de l'accident` (German-5)  ⟷  `Heure de l'accident` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Date de l'accident` (German-5)  ⟷  `Mécanisme de l'accident` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Deux voies veineuses de gros calibre` (RESCOS-5)  ⟷  `Mise en place de 2 voies veineuses de gros calibre` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur abdominale` (RESCOS-5)  ⟷  `Douleur principale` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur épaule droite` (RESCOS-5)  ⟷  `Examen épaule droite` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur épaule droite` (RESCOS-5)  ⟷  `Radiographie épaule droite` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen de l'épaule droite` (RESCOS-6)  ⟷  `Fracture de l'épaule droite` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen respiratoire` (RESCOS-6)  ⟷  `Fréquence respiratoire` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Mise en place de 2 voies veineuses de gros calibre` (RESCOS-6)  ⟷  `Mise en place de voies veineuses` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments` (RESCOS-6)  ⟷  `Médicaments actuels` (German-5, RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nausées/vomissements` (German-5)  ⟷  `Vomissements` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation` (RESCOS-6)  ⟷  `Palpation douce` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation abdominale` (RESCOS-6)  ⟷  `Palpation douce` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation douce` (RESCOS-5)  ⟷  `Palpation du rachis` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perméabilité des voies aériennes` (RESCOS-5)  ⟷  `Vérifier la perméabilité des voies aériennes` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Port de la ceinture` (German-5)  ⟷  `Port de la ceinture de sécurité` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie de l'épaule` (RESCOS-6)  ⟷  `Radiographie épaule droite` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie du bassin` (RESCOS-6)  ⟷  `Radiographie du bassin de face` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche autres lésions` (RESCOS-5)  ⟷  `Recherche de lésions cachées` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche autres lésions` (RESCOS-5)  ⟷  `Recherche des limitations` (German-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de lésions cachées` (RESCOS-6)  ⟷  `Recherche de lésions postérieures` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Stabilisation de la colonne cervicale` (RESCOS-6)  ⟷  `Évaluation de la mobilité cervicale` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Stabilisation hémodynamique` (RESCOS-6)  ⟷  `Évaluation hémodynamique` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation choc hémorragique` (RESCOS-5)  ⟷  `Évaluation hémodynamique` (RESCOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation hémodynamique` (RESCOS-6)  ⟷  `Évaluation phonation` (RESCOS-5) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `ABCDE - Breathing` (RESCOS-6)  ⟷  `ABCDE - Circulation` (RESCOS-6) — **RESCOS-6, section « a »** distingue ces deux items
- ⛔ `Anamnèse familiale` (German-5)  ⟷  `Anamnèse sociale` (German-5) — **German-5, section « a »** distingue ces deux items
- ⛔ `Antécédents médicaux` (German-5, RESCOS-5, RESCOS-6)  ⟷  `Antécédents médicaux et allergies` (RESCOS-5) — **RESCOS-5, section « a »** distingue ces deux items
- ⛔ `En extension` (German-5)  ⟷  `En flexion` (German-5) — **German-5, section « e »** distingue ces deux items
- ⛔ `En extension` (German-5)  ⟷  `Extension` (German-5) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `En flexion` (German-5)  ⟷  `Flexion` (German-5) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Examen de l'épaule droite` (RESCOS-6)  ⟷  `Examen épaule droite` (RESCOS-5) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs d'aggravation` (German-5)  ⟷  `Facteurs d'amélioration` (German-5) — **German-5, section « a »** distingue ces deux items
- ⛔ `Force musculaire` (German-5)  ⟷  `Symétrie musculaire` (German-5) — **German-5, section « e »** distingue ces deux items
- ⛔ `Palpation abdominale` (RESCOS-6)  ⟷  `Palpation bassin` (RESCOS-5) — **RESCOS-6, section « e »** distingue ces deux items
- ⛔ `Palpation bassin` (RESCOS-5)  ⟷  `Palpation du bassin` (RESCOS-6) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Palpation du bassin` (RESCOS-6)  ⟷  `Palpation du rachis` (RESCOS-6) — **RESCOS-6, section « e »** distingue ces deux items
- ⛔ `Prévention de l'hypothermie` (RESCOS-6)  ⟷  `Prévention hypothermie` (RESCOS-5) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Recherche d'hémorragie externe` (RESCOS-6)  ⟷  `Recherche hémorragie externe` (RESCOS-5) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Recherche d'un pneumothorax` (RESCOS-6)  ⟷  `Recherche pneumothorax` (RESCOS-5) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Rotation en extension (teste rachis cervical inférieur)` (German-5)  ⟷  `Rotation en flexion (teste rachis cervical supérieur)` (German-5) — **German-5, section « e »** distingue ces deux items
- ⛔ `Test de mobilité cervicale active` (German-5)  ⟷  `Test de mobilité cervicale passive` (German-5) — **German-5, section « e »** distingue ces deux items

## Adénopathie — 2 cas · 7 à juger (0 de forme, 7 de contenu), 15 ⚠️, 13 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Caractérisation de la plainte principale` (RESCOS-1)  ⟷  `Caractéristiques de la plainte principale` (RESCOS-2)
- `Examens complémentaires de première intention` (RESCOS-2)  ⟷  `Proposition d'examens complémentaires de première intention` (RESCOS-1)
- `Symptômes d'accompagnement` (RESCOS-2)  ⟷  `Symptômes d'accompagnement généraux` (RESCOS-1)
- `Décubitus dorsal` (RESCOS-1)  ⟷  `Technique décubitus dorsal` (RESCOS-2)
- `Examen des ganglions sus-claviculaires` (RESCOS-2)  ⟷  `Palpation des aires sus-claviculaires` (RESCOS-1)
- `Auscultation préalable` (RESCOS-2)  ⟷  `Inspection et auscultation préalables` (RESCOS-1)
- `Examen des aires axillaires` (RESCOS-1)  ⟷  `Examen des autres aires ganglionnaires` (RESCOS-2)

- ⚠️ `Aires sous-claviculaires` (RESCOS-2)  ⟷  `Palpation des aires sus-claviculaires` (RESCOS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents personnels et familiaux` (RESCOS-1)  ⟷  `Cancers personnels ou familiaux` (RESCOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (RESCOS-1)  ⟷  `Auscultation préalable` (RESCOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT scan thoraco-abdomino-pelvien` (RESCOS-1)  ⟷  `CT thoraco-abdomino-pelvien` (RESCOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractérisation de la plainte principale` (RESCOS-1)  ⟷  `Caractérisation si rate palpable` (RESCOS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contact avec animaux` (RESCOS-1)  ⟷  `Contact avec malades` (RESCOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen complémentaire selon contexte` (RESCOS-1)  ⟷  `Examens complémentaires orientés` (RESCOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hépatomégalie` (RESCOS-2)  ⟷  `Recherche hépatomégalie` (RESCOS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Immunodépression` (RESCOS-1)  ⟷  `Immunosuppression` (RESCOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Position du patient` (RESCOS-2)  ⟷  `Position patient assis` (RESCOS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Prise de médicaments` (RESCOS-2)  ⟷  `Prise de médicaments récente` (RESCOS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie thoracique` (RESCOS-1)  ⟷  `Radiographie thoracique face et profil` (RESCOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'une splénomégalie` (RESCOS-2)  ⟷  `Recherche hépatomégalie` (RESCOS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche hépatomégalie` (RESCOS-1)  ⟷  `Recherche organomégalies` (RESCOS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Échographie abdominale` (RESCOS-1)  ⟷  `Échographie abdominale et cervicale` (RESCOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Arguments pour cause infectieuse` (RESCOS-1)  ⟷  `Arguments pour cause tumorale` (RESCOS-1) — **RESCOS-1, section « m »** distingue ces deux items
- ⛔ `Auscultation préalable` (RESCOS-2)  ⟷  `Inspection préalable` (RESCOS-2) — **RESCOS-2, section « e »** distingue ces deux items
- ⛔ `Caractérisation des adénopathies palpées` (RESCOS-1)  ⟷  `Caractérisation si rate palpable` (RESCOS-1) — **RESCOS-1, section « e »** distingue ces deux items
- ⛔ `Douleurs abdominales` (RESCOS-2)  ⟷  `Douleurs associées` (RESCOS-1, RESCOS-2) — **RESCOS-2, section « a »** distingue ces deux items
- ⛔ `Examens complémentaires de première intention` (RESCOS-2)  ⟷  `Examens complémentaires orientés` (RESCOS-2) — **RESCOS-2, section « m »** distingue ces deux items
- ⛔ `Facteurs de risque VIH` (RESCOS-1, RESCOS-2)  ⟷  `Facteurs de risque VIH et IST` (RESCOS-1) — **RESCOS-1, section « a »** distingue ces deux items
- ⛔ `Facteurs de risque VIH` (RESCOS-1, RESCOS-2)  ⟷  `Facteurs de risque infectieux` (RESCOS-1) — **RESCOS-1, section « a »** distingue ces deux items
- ⛔ `Facteurs de risque VIH et IST` (RESCOS-1)  ⟷  `Facteurs de risque infectieux` (RESCOS-1) — **RESCOS-1, section « a »** distingue ces deux items
- ⛔ `Infections récentes` (RESCOS-1)  ⟷  `Vaccinations récentes` (RESCOS-1) — **RESCOS-1, section « a »** distingue ces deux items
- ⛔ `Palpation de la rate` (RESCOS-1, RESCOS-2)  ⟷  `Percussion de la rate` (RESCOS-2) — **RESCOS-2, section « e »** distingue ces deux items
- ⛔ `Palpation des ganglions cervicaux et occipitaux` (RESCOS-1)  ⟷  `Palpation des ganglions épitrochléens et inguinaux` (RESCOS-1) — **RESCOS-1, section « e »** distingue ces deux items
- ⛔ `Sueurs nocturnes` (RESCOS-1, RESCOS-2)  ⟷  `Sueurs nocturnes profuses` (RESCOS-2) — **RESCOS-2, section « a »** distingue ces deux items
- ⛔ `Voyage récent` (RESCOS-1)  ⟷  `Voyages récents` (RESCOS-2) — **même signature socle A**, déjà appariés dans leur section

## Amaurose & Perte Brutale de Vision — 5 cas · 17 à juger (0 de forme, 17 de contenu), 29 ⚠️, 25 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Caractérisation de la baisse de vision` (German-69)  ⟷  `Caractérisation de la perte de vision` (AMBOSS-34)
- `Examens complémentaires` (German-69)  ⟷  `Examens complémentaires urgents` (AMBOSS-34)
- `Examen neurologique` (AMBOSS-34)  ⟷  `Examen neurologique de base` (German-69)
- `Symptômes associés` (AMBOSS-34, AZYGOS-40)  ⟷  `Symptômes visuels associés` (German-69)
- `Segments antérieurs` (AZYGOS-40)  ⟷  `Segments antérieurs de l'œil` (AZYGOS-48)
- `Antécédents ophtalmologiques` (German-69)  ⟷  `Non ophtalmologiques` (AZYGOS-48)
- `Symptômes associés` (AMBOSS-34, AZYGOS-40)  ⟷  `Symptômes oculaires associés` (German-69)
- `Caractérisation céphalées` (RESCOS-3)  ⟷  `Caractérisation de la céphalée associée` (AMBOSS-34)
- `Fond d'œil` (German-69)  ⟷  `Fond d'œil droit` (AZYGOS-48)
- `Examens complémentaires` (German-69)  ⟷  `Examens diagnostiques complémentaires` (AZYGOS-48)
- `Décollement de rétine` (AZYGOS-40)  ⟷  `Symptômes de décollement de rétine` (AZYGOS-48)
- `Question d'entrée ouverte` (German-69)  ⟷  `Question d’entrée` (AZYGOS-40)
- `Examens complémentaires` (German-69)  ⟷  `Investigations complémentaires` (AZYGOS-40)
- `Fond d'œil` (German-69)  ⟷  `Fond d'œil gauche` (AZYGOS-48)
- `Trouble de la parole` (AZYGOS-48)  ⟷  `Trouble du langage` (AZYGOS-40)
- `Examen cardiovasculaire` (AMBOSS-34)  ⟷  `Examen monoculaire` (AZYGOS-48)
- `Antécédents ophtalmologiques` (German-69)  ⟷  `Ophtalmologiques` (AZYGOS-48)

- ⚠️ `Antécédents chirurgicaux` (AMBOSS-34, AZYGOS-48)  ⟷  `Antécédents médico-chirurgicaux` (RESCOS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des 4 foyers` (RESCOS-3)  ⟷  `Auscultation des carotides` (AZYGOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des 4 foyers` (RESCOS-3)  ⟷  `Auscultation des poumons` (AMBOSS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des artères carotides` (AMBOSS-34)  ⟷  `Auscultation des carotides` (AZYGOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des carotides` (AZYGOS-40)  ⟷  `Auscultation des carotides des deux côtés` (RESCOS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des carotides` (AZYGOS-40)  ⟷  `Auscultation des poumons` (AMBOSS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des carotides` (AZYGOS-40)  ⟷  `Auscultation du cœur` (AMBOSS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres médicaments` (German-69)  ⟷  `Médicaments` (AMBOSS-34, AZYGOS-40, AZYGOS-48, RESCOS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Chambre antérieure` (German-69)  ⟷  `Chirurgies antérieures` (German-69) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Claudication de la mâchoire` (German-69)  ⟷  `Palpation de la mâchoire` (RESCOS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostic principal` (German-69)  ⟷  `Motif principal` (AMBOSS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs oculaires` (German-69)  ⟷  `Tonus oculaire` (German-69) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen ciblé de la sensibilité` (AMBOSS-34)  ⟷  `Trouble de la sensibilité` (AZYGOS-40, AZYGOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AMBOSS-34)  ⟷  `Neurologique` (AZYGOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fond d'œil gauche` (AZYGOS-48)  ⟷  `Œil gauche` (RESCOS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fundoscopie` (AZYGOS-40)  ⟷  `Fundoscopie directe` (AMBOSS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Halos lumineux` (German-69)  ⟷  `Éclairs lumineux` (AZYGOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Motilité` (AZYGOS-48)  ⟷  `Motricité` (RESCOS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Motricité` (RESCOS-3)  ⟷  `Oculomotricité` (German-69) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Neuro-ophtalmologique` (RESCOS-3)  ⟷  `Neurologique` (AZYGOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Neuro-ophtalmologique` (RESCOS-3)  ⟷  `Non ophtalmologiques` (AZYGOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Neuro-ophtalmologique` (RESCOS-3)  ⟷  `Ophtalmologiques` (AZYGOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de la mâchoire` (RESCOS-3)  ⟷  `Palpation de la tête` (AMBOSS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perte de sensibilité` (RESCOS-3)  ⟷  `Photosensibilité` (German-69) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perte de sensibilité` (RESCOS-3)  ⟷  `Trouble de la sensibilité` (AZYGOS-40, AZYGOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Photosensibilité` (German-69)  ⟷  `Sensibilité` (RESCOS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (AZYGOS-40, AZYGOS-48)  ⟷  `Progression` (AMBOSS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Rougeur oculaire` (German-69)  ⟷  `Tonus oculaire` (German-69) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Situation` (RESCOS-3)  ⟷  `Statine` (AZYGOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Acuité visuelle de loin à droite` (AZYGOS-48)  ⟷  `Acuité visuelle de loin à gauche` (AZYGOS-48) — **AZYGOS-48, section « e »** distingue ces deux items
- ⛔ `Alimentation` (AMBOSS-34)  ⟷  `Palpitations` (AMBOSS-34) — **AMBOSS-34, section « a »** distingue ces deux items
- ⛔ `Allergies médicamenteuses` (German-69)  ⟷  `Autres médicaments` (German-69) — **German-69, section « a »** distingue ces deux items
- ⛔ `Anamnèse par système - générale` (RESCOS-3)  ⟷  `Anamnèse par système - neurologique` (RESCOS-3) — **RESCOS-3, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-34, AZYGOS-48)  ⟷  `Antécédents familiaux` (AMBOSS-34, AZYGOS-40, AZYGOS-48, German-69) — **AMBOSS-34, section « a »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (AZYGOS-40)  ⟷  `Auscultation des carotides` (AZYGOS-40) — **AZYGOS-40, section « e »** distingue ces deux items
- ⛔ `Auscultation des poumons` (AMBOSS-34)  ⟷  `Auscultation du cœur` (AMBOSS-34) — **AMBOSS-34, section « e »** distingue ces deux items
- ⛔ `Caractérisation cécité` (RESCOS-3)  ⟷  `Caractérisation céphalées` (RESCOS-3) — **RESCOS-3, section « a »** distingue ces deux items
- ⛔ `Champ visuel` (AZYGOS-40, AZYGOS-48)  ⟷  `Champs visuels` (RESCOS-3) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Chirurgie oculaire antérieure` (German-69)  ⟷  `Chirurgies antérieures` (German-69) — **German-69, section « a »** distingue ces deux items
- ⛔ `Constante/intermittente` (AMBOSS-34)  ⟷  `Progression/constante/intermittente` (AMBOSS-34) — **AMBOSS-34, section « a »** distingue ces deux items
- ⛔ `Douleurs oculaires` (German-69)  ⟷  `Rougeur oculaire` (German-69) — **German-69, section « a »** distingue ces deux items
- ⛔ `Examen ciblé de la marche` (AMBOSS-34)  ⟷  `Examen ciblé de la sensibilité` (AMBOSS-34) — **AMBOSS-34, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-34)  ⟷  `Facteurs améliorants` (AMBOSS-34) — **AMBOSS-34, section « a »** distingue ces deux items
- ⛔ `IRM cérébrale` (AMBOSS-34)  ⟷  `Imagerie cérébrale` (AMBOSS-34, AZYGOS-40) — **AMBOSS-34, section « m »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-34)  ⟷  `Palpation de la tête` (AMBOSS-34) — **AMBOSS-34, section « e »** distingue ces deux items
- ⛔ `Non ophtalmologiques` (AZYGOS-48)  ⟷  `Ophtalmologiques` (AZYGOS-48) — **AZYGOS-48, section « a »** distingue ces deux items
- ⛔ `Paupière` (RESCOS-3)  ⟷  `Paupières` (German-69) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Qualité` (AMBOSS-34, AZYGOS-40, RESCOS-3)  ⟷  `Quantité` (RESCOS-3) — **RESCOS-3, section « a »** distingue ces deux items
- ⛔ `Segments antérieurs` (AZYGOS-40)  ⟷  `Épisodes antérieurs` (AMBOSS-34, AZYGOS-40) — **AZYGOS-40, section « a »** distingue ces deux items
- ⛔ `Segments antérieurs de l'œil` (AZYGOS-48)  ⟷  `Segments externes de l'œil` (AZYGOS-48) — **AZYGOS-48, section « e »** distingue ces deux items
- ⛔ `Signe de Babinski` (AMBOSS-34)  ⟷  `Signe de Brudzinski` (AMBOSS-34) — **AMBOSS-34, section « e »** distingue ces deux items
- ⛔ `Symptômes oculaires associés` (German-69)  ⟷  `Symptômes visuels associés` (German-69) — **German-69, section « a »** distingue ces deux items
- ⛔ `Vision de loin avec correction` (German-69)  ⟷  `Vision de près avec correction` (German-69) — **German-69, section « e »** distingue ces deux items
- ⛔ `Vision des couleurs` (German-69)  ⟷  `Vision double` (German-69) — **German-69, section « a »** distingue ces deux items

## Boiterie de l'Enfant — 2 cas · 0 à juger (0 de forme, 0 de contenu), 0 ⚠️, 12 ⛔

- ⛔ `Antécédents familiaux` (RESCOS-9, RESCOS-9b)  ⟷  `Antécédents médicaux` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (RESCOS-9, RESCOS-9b)  ⟷  `Antécédents similaires` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la boiterie` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation de la fièvre` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la boiterie` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation de la hanche` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la boiterie` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation de la rhinorrhée` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la boiterie` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation des douleurs` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la fièvre` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation de la hanche` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la fièvre` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation de la rhinorrhée` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la fièvre` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation des douleurs` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la hanche` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation de la rhinorrhée` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la hanche` (RESCOS-9, RESCOS-9b)  ⟷  `Caractérisation des douleurs` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « a »** distingue ces deux items
- ⛔ `Investigations complémentaires - bilan sanguin` (RESCOS-9, RESCOS-9b)  ⟷  `Investigations complémentaires - imagerie` (RESCOS-9, RESCOS-9b) — **RESCOS-9, section « m »** distingue ces deux items

## Chute & Évaluation Gériatrique — 5 cas · 1 à juger (0 de forme, 1 de contenu), 14 ⚠️, 22 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Analyse de la marche` (AZYGOS-4)  ⟷  `Examen de la marche` (German-10)

- ⚠️ `AVC antérieurs` (German-10)  ⟷  `Chutes antérieures` (AZYGOS-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation` (AZYGOS-4)  ⟷  `Palpitations` (German-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Audition` (AZYGOS-4, German-10)  ⟷  `Irradiation` (RESCOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Coudes` (RESCOS-11)  ⟷  `Courses` (AZYGOS-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Début/moment de l'événement` (AMBOSS-24)  ⟷  `Moment de l'événement` (German-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dépression` (AMBOSS-24)  ⟷  `Profession` (AZYGOS-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen de la marche` (German-10)  ⟷  `Examens de laboratoire` (German-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants` (AMBOSS-24)  ⟷  `Facteurs atténuants/aggravants` (RESCOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Imagerie cérébrale` (German-11)  ⟷  `Imagerie cérébrale / CT` (German-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des membres supérieurs` (AMBOSS-24)  ⟷  `Palpation des deux membres supérieurs` (RESCOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Motricité` (AZYGOS-4, German-11)  ⟷  `Motricité fine` (German-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation` (AZYGOS-4)  ⟷  `Palpitations` (German-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (AZYGOS-4)  ⟷  `Progression` (AMBOSS-24) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Variations pondérales` (AMBOSS-24)  ⟷  `Évolution pondérale` (AZYGOS-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-24, RESCOS-11)  ⟷  `Antécédents familiaux` (AMBOSS-24) — **AMBOSS-24, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-24, RESCOS-11)  ⟷  `Antécédents hémorragiques` (AMBOSS-24) — **AMBOSS-24, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-24, RESCOS-11)  ⟷  `Antécédents médicaux` (AMBOSS-24, German-11, RESCOS-11) — **AMBOSS-24, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-24)  ⟷  `Antécédents médicaux` (AMBOSS-24, German-11, RESCOS-11) — **AMBOSS-24, section « a »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (AZYGOS-4, German-10)  ⟷  `Auscultation des carotides` (German-10) — **German-10, section « e »** distingue ces deux items
- ⛔ `BADL` (AZYGOS-4)  ⟷  `IADL` (AZYGOS-4) — **AZYGOS-4, section « a »** distingue ces deux items
- ⛔ `Dépression` (AMBOSS-24)  ⟷  `Progression` (AMBOSS-24) — **AMBOSS-24, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-24)  ⟷  `Facteurs améliorants` (AMBOSS-24) — **AMBOSS-24, section « a »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-24)  ⟷  `Inspection des mains` (AMBOSS-24) — **AMBOSS-24, section « e »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-24)  ⟷  `Inspection des sclères` (AMBOSS-24) — **AMBOSS-24, section « e »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-24)  ⟷  `Palpation de la tête` (AMBOSS-24) — **AMBOSS-24, section « e »** distingue ces deux items
- ⛔ `Inspection des conjonctives` (AMBOSS-24)  ⟷  `Inspection des mains` (AMBOSS-24) — **AMBOSS-24, section « e »** distingue ces deux items
- ⛔ `Inspection des conjonctives` (AMBOSS-24)  ⟷  `Inspection des sclères` (AMBOSS-24) — **AMBOSS-24, section « e »** distingue ces deux items
- ⛔ `Inspection des mains` (AMBOSS-24)  ⟷  `Inspection des sclères` (AMBOSS-24) — **AMBOSS-24, section « e »** distingue ces deux items
- ⛔ `Inspection des membres inférieurs` (AMBOSS-24)  ⟷  `Inspection des membres supérieurs` (AMBOSS-24) — **AMBOSS-24, section « e »** distingue ces deux items
- ⛔ `Motricité sur les terrains des nerfs` (RESCOS-11)  ⟷  `Sensibilité sur les terrains des nerfs` (RESCOS-11) — **RESCOS-11, section « e »** distingue ces deux items
- ⛔ `Médicaments` (AMBOSS-24, AZYGOS-4, German-10, German-11, RESCOS-11)  ⟷  `Médicaments actuels` (German-11) — **German-11, section « a »** distingue ces deux items
- ⛔ `Saignements accrus pendant l'accouchement` (AMBOSS-24)  ⟷  `Saignements accrus pendant les règles` (AMBOSS-24) — **AMBOSS-24, section « a »** distingue ces deux items
- ⛔ `Test d'Unterberger` (German-10)  ⟷  `Test de Romberg` (German-10) — **German-10, section « e »** distingue ces deux items
- ⛔ `Transfert` (AZYGOS-4)  ⟷  `Transferts` (AZYGOS-4) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Transfert` (AZYGOS-4)  ⟷  `Transports` (AZYGOS-4) — **AZYGOS-4, section « a »** distingue ces deux items
- ⛔ `Transferts` (AZYGOS-4)  ⟷  `Transports` (AZYGOS-4) — **AZYGOS-4, section « a »** distingue ces deux items

## Colique Néphrétique — 3 cas · 2 à juger (0 de forme, 2 de contenu), 9 ⚠️, 17 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Examen de base` (AZYGOS-9)  ⟷  `Examen de la vessie` (RESCOS-25)
- `Symptômes associés` (AZYGOS-9, RESCOS-24)  ⟷  `Symptômes associés et généraux` (RESCOS-25)

- ⚠️ `Agitation` (RESCOS-25)  ⟷  `Alimentation` (AZYGOS-9) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alcalinisation` (AZYGOS-9)  ⟷  `Localisation` (AZYGOS-9, RESCOS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents chirurgicaux` (AZYGOS-9)  ⟷  `Antécédents urologiques` (RESCOS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen complémentaire orienté` (RESCOS-25)  ⟷  `Examens complémentaires de première intention` (RESCOS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants/soulageant` (RESCOS-25)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-9) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections urinaires antérieures` (AZYGOS-9)  ⟷  `Interventions chirurgicales antérieures` (RESCOS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Information du patient` (AZYGOS-9)  ⟷  `Position du patient` (RESCOS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du foie` (AZYGOS-9)  ⟷  `Palpation profonde` (RESCOS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation et percussion des loges rénales` (RESCOS-24)  ⟷  `Percussion loges rénales` (RESCOS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Algurie` (RESCOS-25)  ⟷  `Fécalurie` (RESCOS-25) — **RESCOS-25, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AZYGOS-9)  ⟷  `Antécédents familiaux` (AZYGOS-9) — **AZYGOS-9, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AZYGOS-9)  ⟷  `Antécédents généraux` (AZYGOS-9) — **AZYGOS-9, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AZYGOS-9)  ⟷  `Antécédents généraux` (AZYGOS-9) — **AZYGOS-9, section « a »** distingue ces deux items
- ⛔ `Aspect des urines` (RESCOS-25)  ⟷  `Odeur des urines` (RESCOS-25) — **RESCOS-25, section « a »** distingue ces deux items
- ⛔ `Aspect général` (RESCOS-25)  ⟷  `Inspection générale` (RESCOS-25) — **RESCOS-25, section « e »** distingue ces deux items
- ⛔ `Aspect général` (RESCOS-25)  ⟷  `État général` (AZYGOS-9, RESCOS-25) — **RESCOS-25, section « e »** distingue ces deux items
- ⛔ `Débitmétrie et résidu post-mictionnel` (RESCOS-25)  ⟷  `Mesure résidu post-mictionnel` (RESCOS-25) — **RESCOS-25, section « m »** distingue ces deux items
- ⛔ `Hématurie initiale` (RESCOS-25)  ⟷  `Hématurie terminale` (RESCOS-25) — **RESCOS-25, section « a »** distingue ces deux items
- ⛔ `Hématurie initiale` (RESCOS-25)  ⟷  `Hématurie totale` (RESCOS-25) — **RESCOS-25, section « a »** distingue ces deux items
- ⛔ `Hématurie terminale` (RESCOS-25)  ⟷  `Hématurie totale` (RESCOS-25) — **RESCOS-25, section « a »** distingue ces deux items
- ⛔ `Incontinence d'urgence` (RESCOS-25)  ⟷  `Incontinence de stress` (RESCOS-25) — **RESCOS-25, section « a »** distingue ces deux items
- ⛔ `Inspection générale` (RESCOS-25)  ⟷  `Inspection péri-anale` (RESCOS-25) — **RESCOS-25, section « e »** distingue ces deux items
- ⛔ `Intensité de la douleur` (RESCOS-24)  ⟷  `Qualité de la douleur` (RESCOS-24) — **RESCOS-24, section « a »** distingue ces deux items
- ⛔ `Localisation de la douleur` (RESCOS-24)  ⟷  `Qualité de la douleur` (RESCOS-24) — **RESCOS-24, section « a »** distingue ces deux items
- ⛔ `Palpation de la rate` (AZYGOS-9)  ⟷  `Palpation des organes` (AZYGOS-9) — **AZYGOS-9, section « e »** distingue ces deux items
- ⛔ `Palpation sus-pubienne` (RESCOS-25)  ⟷  `Percussion sus-pubienne` (RESCOS-25) — **RESCOS-25, section « e »** distingue ces deux items

## Confusion - État Confusionnel Aigu — 2 cas · 0 à juger (0 de forme, 0 de contenu), 5 ⚠️, 4 ⛔

- ⚠️ `Consistance` (RESCOS-57b)  ⟷  `Constantes` (RESCOS-57b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Refus de réhydratation` (RESCOS-57b)  ⟷  `Signes de déshydratation` (RESCOS-57) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes de déshydratation` (RESCOS-57)  ⟷  `Signes de déshydratation sévère` (RESCOS-57) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Status neurologique` (RESCOS-57b)  ⟷  `État neurologique` (RESCOS-57) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Trouble de l'état de conscience` (RESCOS-57b)  ⟷  `État de conscience` (RESCOS-57) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `En EMS depuis 6 ans` (RESCOS-57)  ⟷  `Veuf depuis 8 ans` (RESCOS-57) — **RESCOS-57, section « a »** distingue ces deux items
- ⛔ `Pas de défense` (RESCOS-57)  ⟷  `Pas de détente` (RESCOS-57) — **RESCOS-57, section « e »** distingue ces deux items
- ⛔ `Se renseigne sur l'état du patient` (RESCOS-57b)  ⟷  `Se renseigne sur le patient : nom, âge` (RESCOS-57b) — **RESCOS-57b, section « a »** distingue ces deux items
- ⛔ `Vomissements` (RESCOS-57, RESCOS-57b)  ⟷  `Vomissements, nausées` (RESCOS-57b) — **RESCOS-57b, section « a »** distingue ces deux items

## Céphalée — 6 cas · 16 à juger (2 de forme, 14 de contenu), 20 ⚠️, 24 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Communication avec la patiente` (AMBOSS-33)  ⟷  `Communication avec le patient` (AMBOSS-26)
- `Facteurs de soulagement` (German-8)  ⟷  `Facteurs soulageants` (AZYGOS-3)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Examen cardiovasculaire` (AMBOSS-33)  ⟷  `Examen vasculaire` (RESCOS-10)
- `Réaction appropriée au défi concernant l'entretien d'embauche` (AMBOSS-26)  ⟷  `Réaction appropriée au défi concernant le mari` (AMBOSS-33)
- `Caractérisation de la céphalée` (AMBOSS-26, AMBOSS-33, RESCOS-10)  ⟷  `Caractéristiques des céphalées` (German-9)
- `Examens complémentaires - imagerie` (RESCOS-10)  ⟷  `Examens complémentaires urgents` (AMBOSS-33)
- `Hypothèse diagnostique principale` (RESCOS-10)  ⟷  `Hypothèses diagnostiques` (AMBOSS-26, AMBOSS-33)
- `Examens complémentaires - laboratoire` (RESCOS-10)  ⟷  `Examens complémentaires urgents` (AMBOSS-33)
- `Artère temporale` (AZYGOS-3)  ⟷  `Palpation artère temporale` (German-8)
- `Question d'entrée ouverte → Symptôme principal` (German-9)  ⟷  `Question ouverte d'introduction → Symptôme principal` (German-8)
- `Alimentation` (AMBOSS-26, AMBOSS-33, German-8)  ⟷  `Menstruation` (AZYGOS-3)
- `Nausées/vomissements` (RESCOS-10)  ⟷  `Vomissements` (German-8)
- `Prise en charge` (AMBOSS-26)  ⟷  `Prise en charge immédiate` (RESCOS-10)
- `Symptômes B` (German-9)  ⟷  `Symptômes d'aura` (AZYGOS-3)
- `Prise en charge` (AMBOSS-26)  ⟷  `Traitement/Prise en charge` (German-8)
- `Anamnèse sociale` (German-9)  ⟷  `Anamnèse sociale, profession` (German-8)

- ⚠️ `Agitation` (AMBOSS-26)  ⟷  `Palpitations` (AMBOSS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents familiaux` (AMBOSS-26, AMBOSS-33, AZYGOS-3, German-8)  ⟷  `Antécédents familiaux vasculaires` (RESCOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents neurologiques` (RESCOS-10)  ⟷  `Examen neurologique` (AMBOSS-26, AMBOSS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Arrêt contraception orale` (RESCOS-10)  ⟷  `Contraception orale` (RESCOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Artère temporale` (AZYGOS-3)  ⟷  `Palpation artères temporales` (RESCOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect général` (RESCOS-10)  ⟷  `État général` (RESCOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (AMBOSS-33)  ⟷  `Auscultation carotidienne` (RESCOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractéristiques des céphalées` (German-9)  ⟷  `Caractéristiques des migraines habituelles` (RESCOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Constante/intermittente` (German-8)  ⟷  `Progression/constant/intermittent` (AMBOSS-26, AMBOSS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Céphalée en coup de tonnerre` (RESCOS-10)  ⟷  `Début en coup de tonnerre` (AZYGOS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Drapeaux rouges - céphalée` (RESCOS-10)  ⟷  `Drapeaux rouges à rechercher` (AMBOSS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Déficit neurologique focal` (AZYGOS-3)  ⟷  `Déficits neurologiques focaux` (AMBOSS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AMBOSS-26, AMBOSS-33)  ⟷  `Surveillance neurologique` (RESCOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Explications au patient des impressions diagnostiques préliminaires` (AMBOSS-26)  ⟷  `Explications à la patiente des impressions diagnostiques préliminaires` (AMBOSS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fond d'œil` (German-8)  ⟷  `Fond d'œil direct` (AMBOSS-26, AMBOSS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Glucose, électrolytes` (AMBOSS-33)  ⟷  `Électrolytes` (German-9) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection` (AZYGOS-3)  ⟷  `Inspection du cou` (AMBOSS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Intensité` (RESCOS-10)  ⟷  `Intensité EVA` (German-9) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche des préoccupations et questions de la patiente` (AMBOSS-33)  ⟷  `Recherche des préoccupations et questions du patient` (AMBOSS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'accord de la patiente avec le plan diagnostique` (AMBOSS-33)  ⟷  `Évaluation de l'accord du patient avec le plan diagnostique` (AMBOSS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Agitation` (AMBOSS-26)  ⟷  `Alimentation` (AMBOSS-26, AMBOSS-33, German-8) — **AMBOSS-26, section « a »** distingue ces deux items
- ⛔ `Alimentation` (AMBOSS-26, AMBOSS-33, German-8)  ⟷  `Palpitations` (AMBOSS-33) — **AMBOSS-33, section « a »** distingue ces deux items
- ⛔ `Anamnèse personnelle` (German-9)  ⟷  `Anamnèse sociale` (German-9) — **German-9, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-26, AMBOSS-33, AZYGOS-3)  ⟷  `Antécédents familiaux` (AMBOSS-26, AMBOSS-33, AZYGOS-3, German-8) — **AMBOSS-26, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-26, AMBOSS-33, AZYGOS-3)  ⟷  `Antécédents médicaux` (AMBOSS-26, AMBOSS-33, AZYGOS-3, German-9) — **AMBOSS-26, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-26, AMBOSS-33, AZYGOS-3, German-8)  ⟷  `Antécédents médicaux` (AMBOSS-26, AMBOSS-33, AZYGOS-3, German-9) — **AMBOSS-26, section « a »** distingue ces deux items
- ⛔ `Donner l'option de s'allonger et proposer de tamiser la lumière` (AMBOSS-26)  ⟷  `Proposer au patient de s'allonger et tamiser la lumière` (AMBOSS-26) — **AMBOSS-26, section « m »** distingue ces deux items
- ⛔ `Examen ciblé de la marche` (AMBOSS-26, AMBOSS-33)  ⟷  `Examen ciblé de la sensibilité` (AMBOSS-26, AMBOSS-33) — **AMBOSS-26, section « e »** distingue ces deux items
- ⛔ `Examen neurologique - nerfs crâniens` (RESCOS-10)  ⟷  `Examen neurologique - voies longues` (RESCOS-10) — **RESCOS-10, section « e »** distingue ces deux items
- ⛔ `Examens complémentaires - imagerie` (RESCOS-10)  ⟷  `Examens complémentaires - laboratoire` (RESCOS-10) — **RESCOS-10, section « m »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-26, AMBOSS-33, AZYGOS-3, German-8, German-9)  ⟷  `Facteurs améliorants` (AMBOSS-26, AMBOSS-33, German-9) — **AMBOSS-26, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-26, AMBOSS-33, AZYGOS-3, German-8, German-9)  ⟷  `Facteurs soulageants` (AZYGOS-3) — **AZYGOS-3, section « a »** distingue ces deux items
- ⛔ `Hospitalisation` (RESCOS-10)  ⟷  `Hospitalisations` (AMBOSS-26, AMBOSS-33) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Hospitalisation` (RESCOS-10)  ⟷  `Localisation` (AMBOSS-26, AMBOSS-33, AZYGOS-3, RESCOS-10) — **AMBOSS-26, section « a »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-26, AMBOSS-33)  ⟷  `Palpation de la tête` (AMBOSS-26, AMBOSS-33) — **AMBOSS-26, section « e »** distingue ces deux items
- ⛔ `Inspection du cou` (AMBOSS-26)  ⟷  `Palpation du cou` (AMBOSS-26) — **AMBOSS-26, section « e »** distingue ces deux items
- ⛔ `Motricité` (AZYGOS-3)  ⟷  `Oculomotricité` (AZYGOS-3, RESCOS-10) — **AZYGOS-3, section « e »** distingue ces deux items
- ⛔ `Nausées / vomissements` (AZYGOS-3)  ⟷  `Nausées/vomissements` (RESCOS-10) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Palpation artère temporale` (German-8)  ⟷  `Palpation artères temporales` (RESCOS-10) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Phonophobie` (AZYGOS-3)  ⟷  `Photophobie` (AZYGOS-3, German-8, German-9) — **AZYGOS-3, section « a »** distingue ces deux items
- ⛔ `Sensibilité` (AZYGOS-3, RESCOS-10)  ⟷  `Sensibilité faciale` (RESCOS-10) — **RESCOS-10, section « e »** distingue ces deux items
- ⛔ `Signe de Babinski` (AMBOSS-26, AMBOSS-33)  ⟷  `Signe de Brudzinski` (AMBOSS-33, German-9, RESCOS-10) — **AMBOSS-33, section « e »** distingue ces deux items
- ⛔ `Traitement de la crise par AINS` (AZYGOS-3)  ⟷  `Traitement de la crise par triptan` (AZYGOS-3) — **AZYGOS-3, section « m »** distingue ces deux items
- ⛔ `Trouble de la conscience` (AZYGOS-3)  ⟷  `Troubles de conscience` (AMBOSS-26) — **même signature socle A**, déjà appariés dans leur section

## Diarrhée — 5 cas · 29 à juger (1 de forme, 28 de contenu), 61 ⚠️, 32 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Communication avec la patiente` (RESCOS-14)  ⟷  `Communication avec le patient` (AMBOSS-8)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Antécédents familiaux pertinents` (German-85)  ⟷  `Antécédents médicaux pertinents` (German-13)
- `Évaluation clinique de l'état d'hydratation` (German-85)  ⟷  `Évaluation de l'état d'hydratation` (German-13)
- `L'étudiant propose les examens complémentaires appropriés` (German-85)  ⟷  `L'étudiant propose les examens complémentaires spécifiques` (German-13)
- `Examens complémentaires` (RESCOS-14)  ⟷  `Examens complémentaires urgents` (AMBOSS-8)
- `Signes cliniques de déshydratation` (German-85)  ⟷  `Signes de déshydratation` (German-13)
- `Antécédents familiaux digestifs` (German-13)  ⟷  `Antécédents familiaux pertinents` (German-85)
- `Examens d'imagerie et endoscopie` (AMBOSS-8)  ⟷  `Imagerie et endoscopie` (RESCOS-15)
- `Caractérisation des troubles du transit` (AMBOSS-8)  ⟷  `Définitions des troubles du transit` (RESCOS-15)
- `Symptômes digestifs` (German-85)  ⟷  `Symptômes digestifs associés` (RESCOS-15)
- `Antécédents familiaux` (AMBOSS-8)  ⟷  `Antécédents familiaux digestifs` (German-13)
- `L'étudiant propose les examens complémentaires appropriés` (German-85)  ⟷  `L'étudiant propose les examens complémentaires de première intention` (German-13)
- `Symptômes associés` (RESCOS-14)  ⟷  `Symptômes associés généraux` (German-13)
- `Examens complémentaires de première intention` (RESCOS-15)  ⟷  `L'étudiant propose les examens complémentaires de première intention` (German-13)
- `Antécédents familiaux` (AMBOSS-8)  ⟷  `Antécédents familiaux pertinents` (German-85)
- `Antécédents médicaux` (AMBOSS-8)  ⟷  `Antécédents médicaux pertinents` (German-13)
- `Symptômes associés` (RESCOS-14)  ⟷  `Symptômes digestifs associés` (RESCOS-15)
- `Hypothèse diagnostique principale` (RESCOS-14)  ⟷  `Hypothèses diagnostiques` (AMBOSS-8)
- `Auscultation abdominale` (RESCOS-15)  ⟷  `Auscultation cardiopulmonaire` (German-13)
- `L'étudiant organise le suivi et l'orientation` (German-85)  ⟷  `L'étudiant organise le suivi et reconnaît les complications` (German-13)
- `Caractéristiques des selles` (AMBOSS-8, German-13)  ⟷  `Caractéristiques des selles - Aspect anormal` (RESCOS-15)
- `Question ouverte pour identifier le motif de consultation` (German-85)  ⟷  `Question ouverte pour identifier le symptôme principal` (German-13)
- `Masses rectales` (German-13)  ⟷  `Masses rectales palpables` (RESCOS-15)
- `Évaluation de l'état d'hydratation` (German-13)  ⟷  `Évaluation de l'état général` (German-85, RESCOS-14)
- `Symptômes digestifs associés` (RESCOS-15)  ⟷  `Symptômes gastro-intestinaux associés` (German-13)
- `Caractérisation de la modification du transit` (RESCOS-15)  ⟷  `Caractérisation des troubles du transit` (AMBOSS-8)
- `Examens complémentaires de première intention` (RESCOS-15)  ⟷  `Examens complémentaires urgents` (AMBOSS-8)
- `Caractérisation des rectorragies` (RESCOS-14)  ⟷  `Caractérisation des troubles du transit` (AMBOSS-8)
- `Palpation superficielle` (RESCOS-15)  ⟷  `Palpation vésicale` (German-85)

- ⚠️ `Alimentation` (AMBOSS-8)  ⟷  `Alimentation récente` (RESCOS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation` (AMBOSS-8)  ⟷  `Alimentation, gluten` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation` (AMBOSS-8)  ⟷  `Palpitations` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation récente` (RESCOS-15)  ⟷  `Alimentation, gluten` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation récente` (RESCOS-15)  ⟷  `Infection récente` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Altération de l'état général` (RESCOS-15)  ⟷  `Évaluation de l'état général` (German-85, RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ampoule rectale` (RESCOS-15)  ⟷  `Douleurs rectales` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents familiaux` (AMBOSS-8)  ⟷  `Antécédents familiaux de diabète` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents familiaux de cancer colorectal` (RESCOS-15)  ⟷  `Antécédents familiaux de diabète` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents familiaux de diabète` (German-85)  ⟷  `Antécédents familiaux digestifs` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Asthénie chronique` (German-85)  ⟷  `Diarrhée chronique` (RESCOS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation abdominale` (RESCOS-15)  ⟷  `Auscultation de l'abdomen` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation abdominale` (RESCOS-15)  ⟷  `US abdominale` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres manifestations extra-intestinales` (German-13)  ⟷  `Recherche de manifestations extra-intestinales` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres médicaments` (German-85)  ⟷  `Autres médicaments pertinents` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres médicaments` (German-85)  ⟷  `Médicaments` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres médicaments` (German-85)  ⟷  `Prise médicamenteuse` (RESCOS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cancer colorectal` (German-13)  ⟷  `Carcinome colorectal` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Chirurgies abdominales` (German-13)  ⟷  `US abdominale` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Colonoscopie avec biopsies` (RESCOS-14)  ⟷  `Coloscopie avec biopsies` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Consommation d'aliments suspects` (German-85)  ⟷  `Consommation d'aliments à risque` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Critères d'hospitalisation définis` (German-85)  ⟷  `Critères d'hospitalisation évalués` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostics différentiels des troubles du transit` (RESCOS-15)  ⟷  `Définitions des troubles du transit` (RESCOS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diarrhée (couleur/consistance)` (AMBOSS-8)  ⟷  `Diarrhée (fréquence, consistance)` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à l'ébranlement` (RESCOS-15)  ⟷  `Recherche de douleur à l'ébranlement` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs abdominales` (German-13, RESCOS-15)  ⟷  `US abdominale` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs articulaires` (AMBOSS-8)  ⟷  `Douleurs musculaires/articulaires` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs articulaires` (AMBOSS-8)  ⟷  `Pas de douleurs articulaires` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Déshydratation aiguë` (German-85)  ⟷  `Réhydratation IV` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen abdominal` (AMBOSS-8, RESCOS-14)  ⟷  `Silence abdominal` (RESCOS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen articulaire` (RESCOS-14)  ⟷  `Examen cardiovasculaire` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen articulaire` (RESCOS-14)  ⟷  `Examen pulmonaire` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cutané` (AMBOSS-8, RESCOS-14)  ⟷  `Examen rectal` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (AMBOSS-8)  ⟷  `Examens complémentaires` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen rectal` (AMBOSS-8)  ⟷  `Examen rénal` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisations` (AMBOSS-8)  ⟷  `Hospitalisations récentes` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisations et contacts malades` (AMBOSS-8)  ⟷  `Hospitalisations récentes` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection abdominale` (RESCOS-15)  ⟷  `Inspection de l'abdomen` (AMBOSS-8, RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies inflammatoires intestinales` (RESCOS-15)  ⟷  `Maladies inflammatoires intestinales (MICI)` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies préexistantes` (German-13)  ⟷  `Maladies rénales` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments` (AMBOSS-8)  ⟷  `Médicaments actuels` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (German-13)  ⟷  `Médicaments gastrotoxiques` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de l'abdomen` (AMBOSS-8)  ⟷  `Palpation de la thyroïde` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation rectale` (RESCOS-14)  ⟷  `Palpation vésicale` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpitations` (RESCOS-14)  ⟷  `Pulsations` (RESCOS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion abdominale` (RESCOS-15)  ⟷  `Percussion de l'abdomen` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion abdominale` (RESCOS-15)  ⟷  `US abdominale` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perte de poids` (RESCOS-14, RESCOS-15)  ⟷  `Perte de poids récente` (German-85) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Prise des signes vitaux` (RESCOS-14)  ⟷  `Signes vitaux` (RESCOS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Présence de sang` (German-13)  ⟷  `Présence de sang frais` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Présence de sang` (German-13)  ⟷  `Présence de sang/méléna` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Présence de sang frais` (RESCOS-14)  ⟷  `Présence de sang/méléna` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Présence de sang frais` (RESCOS-14)  ⟷  `Recherche de sang frais` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie abdominale simple` (AMBOSS-8)  ⟷  `Radiothérapie abdominale` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'hypotension orthostatique` (German-85)  ⟷  `Vertiges/hypotension orthostatique` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de complications` (RESCOS-14)  ⟷  `Surveillance des complications` (RESCOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de masses` (RESCOS-14)  ⟷  `Recherche de nodules` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de sang occulte dans les selles` (AMBOSS-8)  ⟷  `Test immunologique fécal (recherche de sang occulte dans les selles)` (RESCOS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes de déshydratation` (RESCOS-14)  ⟷  `Signes de déshydratation` (German-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Silence abdominal` (RESCOS-15)  ⟷  `US abdominale` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sueurs nocturnes` (RESCOS-15)  ⟷  `Sueurs nocturnes/fatigue` (AMBOSS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-8)  ⟷  `Antécédents familiaux` (AMBOSS-8) — **AMBOSS-8, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-8)  ⟷  `Antécédents médicaux` (AMBOSS-8) — **AMBOSS-8, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-8)  ⟷  `Antécédents médicaux` (AMBOSS-8) — **AMBOSS-8, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux de diabète` (German-85)  ⟷  `Antécédents familiaux pertinents` (German-85) — **German-85, section « a »** distingue ces deux items
- ⛔ `Antécédents médicaux pertinents` (German-13)  ⟷  `Autres médicaments pertinents` (German-13) — **German-13, section « a »** distingue ces deux items
- ⛔ `Auscultation abdominale` (RESCOS-15)  ⟷  `Inspection abdominale` (RESCOS-15) — **RESCOS-15, section « e »** distingue ces deux items
- ⛔ `Auscultation abdominale` (RESCOS-15)  ⟷  `Percussion abdominale` (RESCOS-15) — **RESCOS-15, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-8)  ⟷  `Inspection de l'abdomen` (AMBOSS-8, RESCOS-14) — **AMBOSS-8, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-8)  ⟷  `Palpation de l'abdomen` (AMBOSS-8) — **AMBOSS-8, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-8)  ⟷  `Percussion de l'abdomen` (AMBOSS-8) — **AMBOSS-8, section « e »** distingue ces deux items
- ⛔ `Autres médicaments` (German-85)  ⟷  `Toxiques et médicaments` (German-85) — **German-85, section « a »** distingue ces deux items
- ⛔ `Calprotectine fécale (inflammation intestinale)` (German-13)  ⟷  `Calprotectine fécale: inflammation intestinale` (RESCOS-15) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Constant/intermittent` (AMBOSS-8)  ⟷  `Progression/constant/intermittent` (AMBOSS-8) — **AMBOSS-8, section « a »** distingue ces deux items
- ⛔ `Diarrhée` (RESCOS-15)  ⟷  `Diarrhée aiguë` (RESCOS-15) — **RESCOS-15, section « a »** distingue ces deux items
- ⛔ `Durée et fréquence` (RESCOS-14)  ⟷  `Quantité et fréquence` (RESCOS-14) — **RESCOS-14, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-8, RESCOS-14)  ⟷  `Facteurs améliorants` (AMBOSS-8) — **AMBOSS-8, section « a »** distingue ces deux items
- ⛔ `Fonction rénale (créatinine, urée)` (German-85)  ⟷  `Fonction rénale : créatinine, urée` (German-13) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Inspection abdominale` (RESCOS-15)  ⟷  `Inspection générale` (RESCOS-15) — **RESCOS-15, section « e »** distingue ces deux items
- ⛔ `Inspection abdominale` (RESCOS-15)  ⟷  `Percussion abdominale` (RESCOS-15) — **RESCOS-15, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-8, RESCOS-14)  ⟷  `Inspection de l'oropharynx` (AMBOSS-8) — **AMBOSS-8, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-8, RESCOS-14)  ⟷  `Inspection de la marge anale` (RESCOS-14) — **RESCOS-14, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-8, RESCOS-14)  ⟷  `Palpation de l'abdomen` (AMBOSS-8) — **AMBOSS-8, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-8, RESCOS-14)  ⟷  `Percussion de l'abdomen` (AMBOSS-8) — **AMBOSS-8, section « e »** distingue ces deux items
- ⛔ `L'étudiant propose les examens complémentaires de première intention` (German-13)  ⟷  `L'étudiant propose les examens complémentaires spécifiques` (German-13) — **German-13, section « m »** distingue ces deux items
- ⛔ `Masses palpables` (RESCOS-15)  ⟷  `Masses rectales palpables` (RESCOS-15) — **RESCOS-15, section « e »** distingue ces deux items
- ⛔ `Nausées et vomissements` (RESCOS-14)  ⟷  `Nausées/vomissements` (AMBOSS-8, German-13) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Palpation de l'abdomen` (AMBOSS-8)  ⟷  `Percussion de l'abdomen` (AMBOSS-8) — **AMBOSS-8, section « e »** distingue ces deux items
- ⛔ `Palpation superficielle` (RESCOS-15)  ⟷  `Veines superficielles` (RESCOS-15) — **RESCOS-15, section « e »** distingue ces deux items
- ⛔ `Pas d'atteinte cutanée` (RESCOS-14)  ⟷  `Pas d'atteinte oculaire` (RESCOS-14) — **RESCOS-14, section « a »** distingue ces deux items
- ⛔ `Selles noires déféquées` (RESCOS-15)  ⟷  `Selles noires luisantes` (RESCOS-15) — **RESCOS-15, section « a »** distingue ces deux items
- ⛔ `Syndrome cholérique` (RESCOS-15)  ⟷  `Syndrome dysentérique` (RESCOS-15) — **RESCOS-15, section « a »** distingue ces deux items
- ⛔ `Voyage récent` (AMBOSS-8, German-85, RESCOS-14, RESCOS-15)  ⟷  `Voyages récents` (German-13) — **même signature socle A**, déjà appariés dans leur section

## Douleur - Masse Pelvienne — 2 cas · 1 à juger (0 de forme, 1 de contenu), 8 ⚠️, 14 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Antécédents familiaux` (AMBOSS-6)  ⟷  `Antécédents personnels et familiaux` (RESCOS-33)

- ⚠️ `Antécédents familiaux` (AMBOSS-6)  ⟷  `Antécédents familiaux oncologiques` (RESCOS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation abdominale` (RESCOS-33)  ⟷  `Auscultation de l'abdomen` (AMBOSS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Date des dernières règles` (RESCOS-33)  ⟷  `Dernières règles` (AMBOSS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostic principal` (RESCOS-33)  ⟷  `Motif principal` (AMBOSS-6, RESCOS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Explication des résultats d'examen` (RESCOS-33)  ⟷  `Explication du déroulement de l'examen` (RESCOS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants` (AMBOSS-6)  ⟷  `Facteurs aggravants/soulageants` (RESCOS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection abdominale` (RESCOS-33)  ⟷  `Inspection de l'abdomen` (AMBOSS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Prélèvements microbiologiques si nécessaire` (RESCOS-33)  ⟷  `Prélèvements microbiologiques si symptômes` (RESCOS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-6, RESCOS-33)  ⟷  `Antécédents familiaux` (AMBOSS-6) — **AMBOSS-6, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-6, RESCOS-33)  ⟷  `Antécédents médicaux` (AMBOSS-6, RESCOS-33) — **AMBOSS-6, section « a »** distingue ces deux items
- ⛔ `Antécédents d'IST` (RESCOS-33)  ⟷  `Antécédents médicaux` (AMBOSS-6, RESCOS-33) — **RESCOS-33, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-6)  ⟷  `Antécédents médicaux` (AMBOSS-6, RESCOS-33) — **AMBOSS-6, section « a »** distingue ces deux items
- ⛔ `Auscultation abdominale` (RESCOS-33)  ⟷  `Inspection abdominale` (RESCOS-33) — **RESCOS-33, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-6)  ⟷  `Inspection de l'abdomen` (AMBOSS-6) — **AMBOSS-6, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-6)  ⟷  `Palpation de l'abdomen` (AMBOSS-6) — **AMBOSS-6, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-6)  ⟷  `Percussion de l'abdomen` (AMBOSS-6) — **AMBOSS-6, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-6)  ⟷  `Facteurs améliorants` (AMBOSS-6) — **AMBOSS-6, section « a »** distingue ces deux items
- ⛔ `IST antérieures` (AMBOSS-6)  ⟷  `Épisodes antérieurs` (AMBOSS-6) — **AMBOSS-6, section « a »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-6)  ⟷  `Palpation de l'abdomen` (AMBOSS-6) — **AMBOSS-6, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-6)  ⟷  `Percussion de l'abdomen` (AMBOSS-6) — **AMBOSS-6, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-6)  ⟷  `Percussion de l'abdomen` (AMBOSS-6) — **AMBOSS-6, section « e »** distingue ces deux items
- ⛔ `Pertes vaginales` (AMBOSS-6)  ⟷  `Sécheresse vaginale` (AMBOSS-6) — **AMBOSS-6, section « a »** distingue ces deux items

## Douleur Abdominale — 20 cas · 114 à juger (5 de forme, 109 de contenu), 203 ⚠️, 117 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Identification des symptômes principaux` (German-17, German-19)  ⟷  `Identification du symptôme principal` (German-15, German-16, German-18, German-20)
- `Conseils diététiques et de prévention` (RESCOS-22)  ⟷  `Conseils diététiques et préventifs` (RESCOS-23)
- `Factors aggravants ⊕` (AZYGOS-14)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-16)
- `Habitudes - alimentation` (RESCOS-18)  ⟷  `Habitudes alimentaires` (AMBOSS-15, German-21)
- `Anamnèse par systèmes` (German-15)  ⟷  `Anamnèse systémique` (German-21)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Anamnèse gynécologique` (German-17, German-18)  ⟷  `Anamnèse urogynécologique` (German-15)
- `Communication avec la patiente` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Communication avec le parent` (AMBOSS-15)
- `Prise en charge thérapeutique` (German-15, German-17, German-18, German-19, German-21)  ⟷  `Prise en charge thérapeutique urgente` (German-20)
- `Délimitation de la taille du foie à la percussion (ou autre technique appropriée)` (RESCOS-18)  ⟷  `Délimite la taille du foie en percutant (ou autre technique appropriée)` (RESCOS-17, RESCOS-19)
- `Douleur directe à la décompression` (AZYGOS-14)  ⟷  `Douleur à la décompression` (AZYGOS-16)
- `Caractérisation de la douleur` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-17, RESCOS-18, RESCOS-20)  ⟷  `Caractérisation de la douleur (OPQRST)` (German-15)
- `Caractérisation de la douleur` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-17, RESCOS-18, RESCOS-20)  ⟷  `Caractérisation de la douleur biliaire` (RESCOS-23)
- `Information du patient et planification` (RESCOS-23)  ⟷  `Information du patient et éducation` (RESCOS-22)
- `Réaction appropriée au défi concernant la chirurgie` (AMBOSS-3)  ⟷  `Réaction appropriée au défi concernant la grossesse` (AMBOSS-2)
- `Échographie abdominale` (German-15, German-19, German-20, RESCOS-23)  ⟷  `Échographie vaginale` (German-17)
- `Prise en charge thérapeutique` (German-15, German-17, German-18, German-19, German-21)  ⟷  `Prise en charge thérapeutique immédiate` (RESCOS-22, RESCOS-23)
- `Palpation des organes` (German-15)  ⟷  `Palpation des reins` (German-21, RESCOS-23)
- `Caractérisation de la douleur abdominale` (AMBOSS-15, RESCOS-21, RESCOS-22)  ⟷  `Caractérisation de la douleur biliaire` (RESCOS-23)
- `Prise en charge thérapeutique immédiate` (RESCOS-22, RESCOS-23)  ⟷  `Prise en charge thérapeutique urgente` (German-20)
- `Caractérisation de la douleur` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-17, RESCOS-18, RESCOS-20)  ⟷  `Caractérisation de la douleur abdominale` (AMBOSS-15, RESCOS-21, RESCOS-22)
- `Recherche de symptômes spécifiques` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Recherche de symptômes spécifiques pédiatriques` (AMBOSS-15)
- `Transit intestinal` (German-17)  ⟷  `Transit intestinal et gaz` (German-18, German-19, German-20)
- `Caractérisation de la douleur` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-17, RESCOS-18, RESCOS-20)  ⟷  `Localisation de la douleur` (German-21)
- `Échographie abdominale` (German-15, German-19, German-20, RESCOS-23)  ⟷  `Échographie abdominale/vaginale` (German-18)
- `Symptômes associés - Souillures` (AMBOSS-15)  ⟷  `Symptômes associés - fièvre` (RESCOS-18)
- `Examens complémentaires de seconde ligne` (AMBOSS-1)  ⟷  `Examens complémentaires secondaires` (AMBOSS-2, AMBOSS-3)
- `Examens complémentaires initiaux` (AMBOSS-1)  ⟷  `Examens complémentaires urgents` (AMBOSS-2, AMBOSS-3)
- `Examens complémentaires proposés` (RESCOS-17)  ⟷  `Examens complémentaires urgents` (AMBOSS-2, AMBOSS-3)
- `Analgésie` (AZYGOS-14)  ⟷  `Antalgie` (AZYGOS-16)
- `Localisation de la douleur` (German-21)  ⟷  `Migration de la douleur` (German-18, German-19, German-20)
- `Caractérisation de la douleur (OPQRST)` (German-15)  ⟷  `Caractérisation de la douleur biliaire` (RESCOS-23)
- `Recherche de signes de choc` (RESCOS-22)  ⟷  `Recherche signes de cholécystite` (RESCOS-23)
- `Symptômes associés - Souillures` (AMBOSS-15)  ⟷  `Symptômes associés - nausées` (RESCOS-18)
- `Signe de McBurney` (AMBOSS-2)  ⟷  `Signe de Murphy` (AMBOSS-1, AZYGOS-14, German-15, RESCOS-17, RESCOS-18, RESCOS-19, RESCOS-23)
- `Symptômes digestifs` (German-17, German-18, German-19)  ⟷  `Symptômes digestifs associés` (German-15, German-21)
- `Caractère de la douleur` (German-17, German-18, German-19, German-20, German-21)  ⟷  `Caractérisation de la douleur` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-17, RESCOS-18, RESCOS-20)
- `Examen abdominal` (AMBOSS-1, AMBOSS-2, AMBOSS-3, German-16, German-17)  ⟷  `Examen abdominal général` (RESCOS-23)
- `Information de la patiente` (German-18)  ⟷  `Information et éducation de la patiente` (German-17)
- `Status vasculaire` (German-20)  ⟷  `Statut articulaire` (AZYGOS-16)
- `Symptômes associés` (AMBOSS-1, AMBOSS-2, AMBOSS-3, AZYGOS-16, German-16, German-18, RESCOS-21)  ⟷  `Symptômes associés - fièvre` (RESCOS-18)
- `Caractérisation de la douleur (OPQRST)` (German-15)  ⟷  `Caractérisation de la douleur abdominale` (AMBOSS-15, RESCOS-21, RESCOS-22)
- `Palpation superficielle` (RESCOS-20, RESCOS-21)  ⟷  `Palpation superficielle et profonde` (German-15, German-21)
- `Facteurs aggravant/soulageant` (RESCOS-17)  ⟷  `Facteurs aggravants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15, RESCOS-19, RESCOS-20, RESCOS-22, RESCOS-23)
- `Échographie abdominale/vaginale` (German-18)  ⟷  `Échographie vaginale` (German-17)
- `Symptômes associés` (AMBOSS-1, AMBOSS-2, AMBOSS-3, AZYGOS-16, German-16, German-18, RESCOS-21)  ⟷  `Symptômes associés - nausées` (RESCOS-18)
- `Symptômes associés` (AMBOSS-1, AMBOSS-2, AMBOSS-3, AZYGOS-16, German-16, German-18, RESCOS-21)  ⟷  `Symptômes digestifs associés` (German-15, German-21)
- `Inspection abdominale` (German-15, RESCOS-21)  ⟷  `Palpation abdominale` (German-18, German-19, German-20, German-21)
- `Palpation superficielle` (RESCOS-20, RESCOS-21)  ⟷  `Palpation superficielle de l'abdomen` (RESCOS-22)
- `Inspection buccale` (German-21)  ⟷  `Inspection cutanée` (AZYGOS-16)
- `Inspection des conjonctives` (AMBOSS-3)  ⟷  `Inspection des sclérotiques` (AMBOSS-1)
- `Examens complémentaires de première intention` (AMBOSS-15)  ⟷  `Examens complémentaires de seconde ligne` (AMBOSS-1)
- `Douleur à la décompression` (AZYGOS-16)  ⟷  `Douleur à la décompression controlatérale` (AZYGOS-14)
- `Examens complémentaires proposés` (RESCOS-17)  ⟷  `Examens complémentaires secondaires` (AMBOSS-2, AMBOSS-3)
- `Facteurs aggravant/soulageant` (RESCOS-17)  ⟷  `Facteurs soulageants` (German-21, RESCOS-19, RESCOS-20)
- `Inspection générale` (German-16)  ⟷  `Inspection générale - Ambiance` (RESCOS-21)
- `Signes péritonéaux` (German-18, German-19, German-20)  ⟷  `Signes vitaux` (German-15, RESCOS-21)
- `Hypothèse diagnostique principale` (RESCOS-17)  ⟷  `Hypothèses diagnostiques` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3)
- `Symptômes généraux et signes d'alarme` (RESCOS-23)  ⟷  `Symptômes généraux et signes de déshydratation` (RESCOS-22)
- `Caractérisation de la douleur` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-17, RESCOS-18, RESCOS-20)  ⟷  `Migration de la douleur` (German-18, German-19, German-20)
- `Inspection abdominale` (German-15, RESCOS-21)  ⟷  `Inspection buccale` (German-21)
- `Présence de sang dans les selles` (RESCOS-17)  ⟷  `Sang dans les selles` (AMBOSS-1, German-15, German-17, German-18, German-20, RESCOS-19, RESCOS-20)
- `Localisation de la douleur` (German-21)  ⟷  `Localisation et durée` (German-16)
- `Localisation de la douleur` (German-21)  ⟷  `Qualité de la douleur` (German-16)
- `Symptômes généraux et digestifs` (German-20)  ⟷  `Symptômes généraux et signes d'alarme` (RESCOS-23)
- `Inspection abdominale` (German-15, RESCOS-21)  ⟷  `Inspection abdominale systématique` (RESCOS-22)
- `Conseil et prévention` (AMBOSS-2, AMBOSS-3)  ⟷  `Conseils et éducation` (German-16)
- `Symptômes digestifs` (German-17, German-18, German-19)  ⟷  `Symptômes généraux et digestifs` (German-20)
- `Diagnostic principal et classification` (RESCOS-23)  ⟷  `Diagnostic principal et différentiel` (RESCOS-22)
- `Diagnostic présumé` (AZYGOS-16)  ⟷  `Diagnostic suspecté` (German-16, German-17, German-18, German-19, German-20)
- `Inspection buccale` (German-21)  ⟷  `Inspection générale` (German-16)
- `Inspection cutanée` (AZYGOS-16)  ⟷  `Inspection générale` (German-16)
- `Communication avec la patiente` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Information de la patiente` (German-18)
- `Examens biologiques` (AMBOSS-15, German-15)  ⟷  `Examens diagnostiques` (German-17, German-18, German-19, German-20, German-21)
- `Examens complémentaires initiaux` (AMBOSS-1)  ⟷  `Examens complémentaires proposés` (RESCOS-17)
- `Inspection abdominale` (German-15, RESCOS-21)  ⟷  `Inspection générale` (German-16)
- `Localisation` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, AZYGOS-16, German-17, German-18, German-19, German-20, RESCOS-17, RESCOS-18, RESCOS-19, RESCOS-21, RESCOS-22, RESCOS-23)  ⟷  `Localisation précise` (German-15, RESCOS-20)
- `Recherche de signes hémorragiques` (German-18)  ⟷  `Recherche de signes péritonéaux` (German-15)
- `Signes péritonéaux` (German-18, German-19, German-20)  ⟷  `Signes péritonéaux spécifiques` (RESCOS-21)
- `Examens complémentaires initiaux` (AMBOSS-1)  ⟷  `Examens complémentaires secondaires` (AMBOSS-2, AMBOSS-3)
- `Distension abdominale` (German-15)  ⟷  `Respiration abdominale` (RESCOS-21)
- `Anamnèse gynécologique` (German-17, German-18)  ⟷  `Gynécologique` (AZYGOS-14)
- `Palpation du foie` (AZYGOS-16, German-21)  ⟷  `Palpation profonde` (RESCOS-20, RESCOS-21)
- `Signes vitaux` (German-15, RESCOS-21)  ⟷  `Signes vitaux complets` (RESCOS-22, RESCOS-23)
- `Facteurs de risque cardiovasculaire` (German-20)  ⟷  `Facteurs de risque ulcéreux` (RESCOS-21)
- `Tympanisme` (RESCOS-22)  ⟷  `Tympanisme diffus` (RESCOS-21)
- `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `Auscultation pulmonaire` (AMBOSS-3, German-16)
- `Examens complémentaires de première intention` (AMBOSS-15)  ⟷  `Examens complémentaires urgents` (AMBOSS-2, AMBOSS-3)
- `Recherche de signes de choc` (RESCOS-22)  ⟷  `Recherche signes de péritonite` (RESCOS-23)
- `Traitement spécifique et antibiotiques` (RESCOS-22)  ⟷  `Traitement spécifique selon diagnostic` (RESCOS-23)
- `Diagnostics différentiels` (German-15, German-16, German-17, German-18, German-19, German-20, German-21, RESCOS-17)  ⟷  `Diagnostics différentiels de l'abdomen aigu` (RESCOS-21)
- `Recherche de signes péritonéaux` (German-15)  ⟷  `Signes péritonéaux` (German-18, German-19, German-20)
- `Symptômes associés` (AMBOSS-1, AMBOSS-2, AMBOSS-3, AZYGOS-16, German-16, German-18, RESCOS-21)  ⟷  `Symptômes associés - Souillures` (AMBOSS-15)
- `Symptômes généraux` (German-17, German-18, German-19)  ⟷  `Symptômes généraux et digestifs` (German-20)
- `Caractérisation de la douleur` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-17, RESCOS-18, RESCOS-20)  ⟷  `Caractéristiques spécifiques de la douleur` (RESCOS-21)
- `Examens complémentaires de seconde ligne` (AMBOSS-1)  ⟷  `Examens complémentaires urgents` (AMBOSS-2, AMBOSS-3)
- `Palpation superficielle de l'abdomen` (RESCOS-22)  ⟷  `Palpation superficielle et profonde` (German-15, German-21)
- `Prise en charge initiale d'urgence` (RESCOS-21)  ⟷  `Prise en charge thérapeutique urgente` (German-20)
- `Anamnèse gynécologique` (German-17, German-18)  ⟷  `Anamnèse systémique` (German-21)
- `Antécédents personnels et facteurs de risque` (RESCOS-23)  ⟷  `Habitudes de vie et facteurs de risque` (German-15)
- `Critères d'hospitalisation` (German-15, RESCOS-22, RESCOS-23)  ⟷  `Hospitalisation` (AZYGOS-14)
- `Palpation de la rate` (German-21, RESCOS-22, RESCOS-23)  ⟷  `Palpation des organes` (German-15)
- `Radiographie ou CT` (German-21)  ⟷  `Radiographie thoracique` (German-20)
- `Caractère de la douleur` (German-17, German-18, German-19, German-20, German-21)  ⟷  `Qualité de la douleur` (German-16)
- `Complications et surveillance` (RESCOS-21)  ⟷  `Complications potentielles` (German-15)
- `Constipation` (AMBOSS-15, German-15, German-17, German-19, RESCOS-20)  ⟷  `Diarrhée/Constipation` (German-18, German-20)
- `Examens complémentaires de première intention` (AMBOSS-15)  ⟷  `Examens complémentaires initiaux` (AMBOSS-1)
- `Localisation` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, AZYGOS-16, German-17, German-18, German-19, German-20, RESCOS-17, RESCOS-18, RESCOS-19, RESCOS-21, RESCOS-22, RESCOS-23)  ⟷  `Localisation et durée` (German-16)
- `Migration de la douleur` (German-18, German-19, German-20)  ⟷  `Qualité de la douleur` (German-16)
- `Status abdominal` (RESCOS-20)  ⟷  `Status abdominal - palpation` (RESCOS-17)
- `Symptômes généraux et digestifs` (German-20)  ⟷  `Symptômes généraux et signes de déshydratation` (RESCOS-22)
- `Facteurs aggravants et déclenchants` (RESCOS-23)  ⟷  `Facteurs déclenchants, aggravants et calmants` (RESCOS-22)
- `Facteurs aggravants et déclenchants` (RESCOS-23)  ⟷  `Facteurs aggravants ou soulageants` (German-17, German-18, German-19, German-20)
- `Conseil et prévention` (AMBOSS-2, AMBOSS-3)  ⟷  `Conseils diététiques et de prévention` (RESCOS-22)
- `Information de la patiente` (German-18)  ⟷  `Information du patient et éducation` (RESCOS-22)

- ⚠️ `Allergies et médicaments` (AMBOSS-15)  ⟷  `Allergies médicamenteuses` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Amplitude respiratoire` (RESCOS-21)  ⟷  `Symptômes respiratoires` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Analgésie` (AZYGOS-14)  ⟷  `Analgésiques` (German-17) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Analgésiques` (German-17)  ⟷  `Antalgiques` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Anamnèse gynécologique` (German-17, German-18)  ⟷  `Antécédents gynécologiques` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antalgie` (AZYGOS-16)  ⟷  `Antalgiques` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antiémétiques si vomissements` (RESCOS-23)  ⟷  `Caractéristiques des vomissements` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédent de chirurgie gynécologique` (German-17)  ⟷  `Antécédents gynécologiques` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents de diverticulose` (German-15)  ⟷  `Antécédents de maladie ulcéreuse` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents de douleurs similaires` (German-20)  ⟷  `Antécédents similaires` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents familiaux` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, RESCOS-22, RESCOS-23)  ⟷  `Antécédents familiaux d'ulcère` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents familiaux d'ulcère` (RESCOS-21)  ⟷  `Antécédents familiaux et habitudes` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Appendicite` (RESCOS-18)  ⟷  `DD : appendicite` (RESCOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect des selles` (German-19, RESCOS-22, RESCOS-23)  ⟷  `Aspect des vomissements` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect des vomissements` (AZYGOS-16)  ⟷  `Nausées/Vomissements` (German-17, German-18, German-19, German-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect des vomissements` (AZYGOS-16)  ⟷  `Présence de vomissement` (RESCOS-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect des vomissements` (AZYGOS-16)  ⟷  `Sang dans les vomissements` (German-17, German-18, German-19, German-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `Auscultation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `US abdominale` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `US transabdominale` (AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation avant toute autre partie de l'examen clinique` (RESCOS-18)  ⟷  `Auscultation avant toute autre partie du status` (RESCOS-17, RESCOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardio-pulmonaire` (German-21)  ⟷  `Auscultation pulmonaire` (AMBOSS-3, German-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardio-pulmonaire` (German-21)  ⟷  `Status cardio-pulmonaire` (German-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Automédication fréquente` (RESCOS-21)  ⟷  `Automédication récente` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bilan biologique` (RESCOS-22, RESCOS-23)  ⟷  `Examens biologiques` (AMBOSS-15, German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bras & jambes décroisées` (RESCOS-17, RESCOS-19)  ⟷  `Jambes décroisées` (RESCOS-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bruits intestinaux` (RESCOS-21)  ⟷  `Transit intestinal` (German-17) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT abdominal` (AMBOSS-1, AMBOSS-2)  ⟷  `Inspection abdominale` (German-15, RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT abdominal` (AMBOSS-1, AMBOSS-2)  ⟷  `Silence abdominal` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT abdominal` (AMBOSS-1, AMBOSS-2)  ⟷  `Status abdominal` (RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractère` (RESCOS-22, RESCOS-23)  ⟷  `Type/caractère` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractéristiques des selles` (AZYGOS-16)  ⟷  `Caractéristiques des vomissements` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractéristiques des selles` (AZYGOS-16)  ⟷  `Caractéristiques du foie palpé` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractéristiques des selles` (AZYGOS-16)  ⟷  `Examen bactériologique des selles` (German-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cholécystectomie` (RESCOS-23)  ⟷  `Hystérectomie` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Coliques` (RESCOS-21)  ⟷  `Toxiques` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Coloscopie` (German-20)  ⟷  `Laparoscopie` (AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Conseils d'hygiène` (RESCOS-22)  ⟷  `Mesures d'hygiène` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Consommation d'AINS` (RESCOS-21)  ⟷  `Consommation de substances` (German-16, German-17, German-18, German-19, German-20, German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contracture abdominale` (German-15, RESCOS-21)  ⟷  `Status abdominal` (RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contracture abdominale` (German-15, RESCOS-21)  ⟷  `Échographie abdominale` (German-15, German-19, German-20, RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Couleur` (AMBOSS-15, RESCOS-18)  ⟷  `Douleurs` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Couleur des urines` (RESCOS-19, RESCOS-20)  ⟷  `Volume des urines` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Demande un test de grossesse` (RESCOS-20)  ⟷  `Test de grossesse` (German-17, German-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dernier repas` (AZYGOS-14)  ⟷  `Dernier transit` (RESCOS-19, RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dernières règles` (AMBOSS-2, AMBOSS-3, German-17, RESCOS-22)  ⟷  `Dernières selles` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diabète` (German-16, German-20)  ⟷  `Diète` (RESCOS-17, RESCOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostic de travail` (AZYGOS-14)  ⟷  `Diagnostic différentiel` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Distension abdominale` (German-15)  ⟷  `Palpation abdominale` (German-18, German-19, German-20, German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur directe à la décompression` (AZYGOS-14)  ⟷  `Douleur à la décompression (Blumberg)` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur directe à la décompression` (AZYGOS-14)  ⟷  `Douleur à la décompression brutale` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur directe à la décompression` (AZYGOS-14)  ⟷  `Douleur à la pression` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à l'ébranlement` (AZYGOS-14, RESCOS-21)  ⟷  `Douleur à l'ébranlement et à la détente` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression` (AZYGOS-16)  ⟷  `Douleur à la décompression (Blumberg)` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression` (AZYGOS-16)  ⟷  `Douleur à la décompression brutale` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression` (AZYGOS-16)  ⟷  `Douleur à la détente` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression` (AZYGOS-16)  ⟷  `Douleur à la miction` (RESCOS-17) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression` (AZYGOS-16)  ⟷  `Douleur à la percussion` (German-15, RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression` (AZYGOS-16)  ⟷  `Douleur à la pression` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression (Blumberg)` (German-15)  ⟷  `Douleur à la décompression brutale` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression (Blumberg)` (German-15)  ⟷  `Douleur à la décompression controlatérale` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression brutale` (RESCOS-21)  ⟷  `Douleur à la décompression controlatérale` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression brutale` (RESCOS-21)  ⟷  `Douleur à la percussion rénale` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la décompression brutale` (RESCOS-21)  ⟷  `Douleur à la pression` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la détente` (RESCOS-22)  ⟷  `Douleur à la miction` (RESCOS-17) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la détente` (RESCOS-22)  ⟷  `Douleur à la pression` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la détente` (RESCOS-22)  ⟷  `Douleur à la secousse` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la détente` (RESCOS-22)  ⟷  `Douleur à la toux` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la miction` (RESCOS-17)  ⟷  `Douleur à la percussion` (German-15, RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la miction` (RESCOS-17)  ⟷  `Douleur à la pression` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la miction` (RESCOS-17)  ⟷  `Douleur à la secousse` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la miction` (RESCOS-17)  ⟷  `Douleur à la toux` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la miction` (RESCOS-17)  ⟷  `Troubles de la miction` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la percussion` (German-15, RESCOS-21)  ⟷  `Douleur à la percussion rénale` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la percussion` (German-15, RESCOS-21)  ⟷  `Douleur à la secousse` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la percussion du talon` (RESCOS-21)  ⟷  `Douleur à la percussion rénale` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la percussion du talon` (RESCOS-21)  ⟷  `Douleur à la pression` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la percussion rénale` (AZYGOS-16)  ⟷  `Douleur à la pression` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la pression` (German-15)  ⟷  `Douleur à la secousse` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la pression` (German-15)  ⟷  `Douleur à la toux` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la secousse` (AZYGOS-16)  ⟷  `Douleur à la toux` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs articulaires` (AMBOSS-2)  ⟷  `Souffles vasculaires` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs articulaires` (AMBOSS-2)  ⟷  `Troubles articulaires` (German-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen abdominal` (AMBOSS-1, AMBOSS-2, AMBOSS-3, German-16, German-17)  ⟷  `Silence abdominal` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (AMBOSS-1, AMBOSS-2, AMBOSS-3, German-20)  ⟷  `Maladies cardiovasculaires` (German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (AMBOSS-1, AMBOSS-2, AMBOSS-3, German-20)  ⟷  `Symptômes cardiovasculaires` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen de base` (AZYGOS-16)  ⟷  `Examen des sclères` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AZYGOS-16)  ⟷  `Examens biologiques` (AMBOSS-15, German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen physique` (AMBOSS-15)  ⟷  `Exercice physique` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Explication du diagnostic et évolution probable` (RESCOS-22)  ⟷  `Explication du diagnostic probable` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Explications au parent des impressions diagnostiques préliminaires` (AMBOSS-15)  ⟷  `Explications au patient des impressions diagnostiques préliminaires` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `FSC, CRP` (RESCOS-23)  ⟷  `VS, CRP` (AMBOSS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Faciès douloureux` (German-15)  ⟷  `Faciès douloureux, crispé` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravant/soulageant` (RESCOS-17)  ⟷  `Facteurs aggravants et déclenchants` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravant/soulageant` (RESCOS-17)  ⟷  `Facteurs soulageants ⊖` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravant/soulageant` (RESCOS-17)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15, RESCOS-19, RESCOS-20, RESCOS-22, RESCOS-23)  ⟷  `Factors aggravants ⊕` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants ou soulageants` (German-17, German-18, German-19, German-20)  ⟷  `Facteurs soulageants` (German-21, RESCOS-19, RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs améliorants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15)  ⟷  `Facteurs calmants` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs améliorants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15)  ⟷  `Facteurs déclenchants` (German-21, RESCOS-22, RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs calmants` (RESCOS-22)  ⟷  `Facteurs soulageants` (German-21, RESCOS-19, RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs de risque` (RESCOS-23)  ⟷  `Facteurs de risque ulcéreux` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs modulateurs` (German-15)  ⟷  `Facteurs soulageants` (German-21, RESCOS-19, RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Forme (perte de poids)` (RESCOS-19)  ⟷  `Perte de poids` (German-17, German-18, German-19, German-20, German-21, RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Gastroscopie` (German-21)  ⟷  `Laparoscopie` (AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Gynécologique` (AZYGOS-14)  ⟷  `Trouble gynécologique` (RESCOS-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisations` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-18)  ⟷  `Hospitalisations antérieures` (AMBOSS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisations / opérations` (RESCOS-17, RESCOS-19)  ⟷  `Hospitalisations antérieures` (AMBOSS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-16, German-20)  ⟷  `Prise de la tension artérielle` (German-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-16, German-20)  ⟷  `Tension artérielle` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Impact professionnel` (RESCOS-23)  ⟷  `Stress professionnel` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Importance de l'observance thérapeutique` (German-15)  ⟷  `Importance de la compliance thérapeutique` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Information sur les complications` (German-19)  ⟷  `Information sur les complications possibles` (German-17, German-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection` (AZYGOS-14, AZYGOS-16, German-18, German-19, German-21)  ⟷  `Instruction` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection abdominale` (German-15, RESCOS-21)  ⟷  `Inspection de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection cutanée` (AZYGOS-16)  ⟷  `Éruption cutanée` (AMBOSS-1, AMBOSS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Inspection de l'abdomen et de la peau` (German-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Inspection de la peau` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'abdomen et de la peau` (German-20)  ⟷  `Inspection de la peau` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Installation du patient` (RESCOS-18)  ⟷  `Éducation du patient` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Instruction` (AZYGOS-16)  ⟷  `Menstruation` (German-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Intensité (échelle 0-10)` (AMBOSS-15)  ⟷  `Sévérité (échelle 1-10)` (German-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Localisation et durée` (German-16)  ⟷  `Localisation précise` (German-15, RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Loges rénales` (AZYGOS-14, RESCOS-19)  ⟷  `Maladies rénales` (German-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladie ulcéreuse connue` (RESCOS-21)  ⟷  `Maladies connues` (RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies cardiovasculaires` (German-21)  ⟷  `Symptômes cardiovasculaires` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies connues` (RESCOS-20)  ⟷  `Maladies rénales` (German-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (German-15)  ⟷  `Médicaments et habitudes` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nausées/Vomissements` (German-17, German-18, German-19, German-20)  ⟷  `Vomissements` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, AZYGOS-16, German-15, German-16, German-21, RESCOS-17, RESCOS-19, RESCOS-20, RESCOS-21, RESCOS-22, RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation` (AZYGOS-14, AZYGOS-16, RESCOS-17, RESCOS-18, RESCOS-19)  ⟷  `Pulsations` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation abdominale` (German-18, German-19, German-20, German-21)  ⟷  `Palpation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation abdominale` (German-18, German-19, German-20, German-21)  ⟷  `Palpation de l'aorte abdominale` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation abdominale` (German-18, German-19, German-20, German-21)  ⟷  `Respiration abdominale` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation bi-manuelle` (RESCOS-20)  ⟷  `Palpation bimanuelle` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Palpation de l'aorte abdominale` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Palpation de la rate` (German-21, RESCOS-22, RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Palpation des reins` (German-21, RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Palpation superficielle de l'abdomen` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation superficielle` (RESCOS-20, RESCOS-21)  ⟷  `Superficielle` (RESCOS-17, RESCOS-18, RESCOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Partenaire` (AMBOSS-2)  ⟷  `Partenaire stable` (German-17) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion abdominale` (German-15, German-21, RESCOS-21, RESCOS-22)  ⟷  `Percussion de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion abdominale` (German-15, German-21, RESCOS-21, RESCOS-22)  ⟷  `US abdominale` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perte de poids` (German-17, German-18, German-19, German-20, German-21, RESCOS-22)  ⟷  `Prise de poids` (AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pertes vaginales` (AMBOSS-2, AMBOSS-3, German-17, RESCOS-20)  ⟷  `Pertes vaginales anormales` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Prise de la tension artérielle` (German-16)  ⟷  `Tension artérielle` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Problèmes de sommeil` (AMBOSS-15)  ⟷  `Troubles du sommeil` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (AZYGOS-14, RESCOS-23)  ⟷  `Progression` (RESCOS-19, RESCOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Présence de sang` (RESCOS-17, RESCOS-18)  ⟷  `Recherche de sang` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'ascite` (RESCOS-23)  ⟷  `Recherche d'ictère` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'ascite` (RESCOS-23)  ⟷  `Recherche de masse` (German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'ascite` (RESCOS-23)  ⟷  `Recherche de masses` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de douleur localisée` (RESCOS-22)  ⟷  `Recherche de douleur rénale` (German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de douleur localisée` (RESCOS-22)  ⟷  `Recherche de douleur épigastrique` (German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de masse` (German-21)  ⟷  `Recherche de sang` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de masses` (RESCOS-22)  ⟷  `Recherche de sang` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de pouls périphériques` (German-20)  ⟷  `Recherche de symptômes spécifiques` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'alarme` (German-15, German-21)  ⟷  `Recherche de signes de choc` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'alarme` (German-15, German-21)  ⟷  `Recherche de signes hémorragiques` (German-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'œsophagite` (German-21)  ⟷  `Recherche de signes de choc` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'œsophagite` (German-21)  ⟷  `Recherche de signes hémorragiques` (German-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'œsophagite` (German-21)  ⟷  `Recherche de signes péritonéaux` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes de choc` (RESCOS-22)  ⟷  `Recherche de signes péritonéaux` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes de choc` (RESCOS-22)  ⟷  `Recherche des signes de cholestase chronique` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes péritonéaux` (German-15)  ⟷  `Recherche signes de péritonite` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche des préoccupations et questions du parent` (AMBOSS-15)  ⟷  `Recherche des préoccupations et questions du patient` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche signes de péritonite` (RESCOS-23)  ⟷  `Signes de péritonisme` (AZYGOS-16, RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Reins` (German-15)  ⟷  `Urines` (AZYGOS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Risque de grossesse` (RESCOS-22)  ⟷  `Test de grossesse` (German-17, German-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Rythme respiratoire` (RESCOS-21)  ⟷  `Symptômes respiratoires` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réaction appropriée au défi concernant la chirurgie` (AMBOSS-3)  ⟷  `Réaction appropriée au défi concernant la frustration parentale` (AMBOSS-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réaction appropriée au défi concernant la chirurgie` (AMBOSS-3)  ⟷  `Réaction appropriée au défi concernant le poids` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réaction appropriée au défi concernant la frustration parentale` (AMBOSS-15)  ⟷  `Réaction appropriée au défi concernant la grossesse` (AMBOSS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réaction appropriée au défi concernant la frustration parentale` (AMBOSS-15)  ⟷  `Réaction appropriée au défi concernant le poids` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réaction appropriée au défi concernant la grossesse` (AMBOSS-2)  ⟷  `Réaction appropriée au défi concernant le poids` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Régime alimentaire` (AMBOSS-1, AMBOSS-2)  ⟷  `Régime alimentaire (fibres)` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réhydratation` (RESCOS-22)  ⟷  `Réhydratation i.v.` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réévaluation du traitement médicamenteux` (German-20)  ⟷  `Traitement médicamenteux` (German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Se place à droite du patient` (RESCOS-17, RESCOS-19)  ⟷  `Se positionne à droite de la patiente` (RESCOS-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes d'alarme nécessitant reconsultation` (RESCOS-22)  ⟷  `Signes nécessitant une reconsultation urgente` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes de dénutrition` (RESCOS-21)  ⟷  `Signes de péritonisme` (AZYGOS-16, RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Silence abdominal` (RESCOS-21)  ⟷  `US abdominale` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Souffles vasculaires` (German-15)  ⟷  `Status vasculaire` (German-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Souffles vasculaires` (German-15)  ⟷  `Troubles articulaires` (German-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Status abdominal` (RESCOS-20)  ⟷  `US abdominale` (AMBOSS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Status urinaire` (AZYGOS-14)  ⟷  `Status vasculaire` (German-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Status urinaire` (AZYGOS-14)  ⟷  `Troubles urinaires` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-22, RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Superficielle` (RESCOS-17, RESCOS-18, RESCOS-19)  ⟷  `Veines superficielles` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Symptômes articulaires` (German-15)  ⟷  `Troubles articulaires` (German-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Technique bimanuelle correcte` (RESCOS-23)  ⟷  `Technique correcte` (RESCOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de grossesse` (German-17, German-18)  ⟷  `Test de grossesse si approprié` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de grossesse` (German-17, German-18)  ⟷  `Test de grossesse urinaire` (AMBOSS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traitement antérieur` (RESCOS-21)  ⟷  `Traitement médicamenteux` (German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Transit intestinal` (German-17)  ⟷  `Transit intestinal - diarrhée` (German-15) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Transit intestinal - diarrhée` (German-15)  ⟷  `Transit intestinal et gaz` (German-18, German-19, German-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles articulaires` (German-19)  ⟷  `Troubles urinaires` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-22, RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles de la coagulation` (German-16)  ⟷  `Troubles de la miction` (AZYGOS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles du sommeil` (RESCOS-22)  ⟷  `Troubles du transit` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles urinaires` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-22, RESCOS-23)  ⟷  `Troubles urinaires associés` (RESCOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `US abdominale` (AMBOSS-1)  ⟷  `US transabdominale` (AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Épisodes antérieurs` (AMBOSS-15)  ⟷  `Épisodes antérieurs similaires` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Épisodes antérieurs` (AMBOSS-15)  ⟷  `Épisodes similaires antérieurs` (RESCOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'accord du parent avec le plan diagnostique` (AMBOSS-15)  ⟷  `Évaluation de l'accord du patient avec le plan diagnostique` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Événements précipitants` (AMBOSS-15, AMBOSS-2, AMBOSS-3)  ⟷  `Événements récents` (German-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Amplitude respiratoire` (RESCOS-21)  ⟷  `Rythme respiratoire` (RESCOS-21) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Analyse d'urine (ECBU)` (German-15)  ⟷  `Analyse d'urine et ECBU` (AMBOSS-2) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Anamnèse de l'entourage` (AZYGOS-14, German-17, German-18, German-19, German-20)  ⟷  `Anamnèse de voyage` (AZYGOS-14, German-17, German-18, German-19, German-20) — **AZYGOS-14, section « a »** distingue ces deux items
- ⛔ `Anamnèse personnelle` (German-17, German-18, German-19, German-20)  ⟷  `Anamnèse sociale` (German-16, German-17, German-18, German-19, German-20, German-21) — **German-17, section « a »** distingue ces deux items
- ⛔ `Antécédent de chirurgie abdominale` (German-17, German-18, German-19, German-20)  ⟷  `Antécédent de chirurgie gynécologique` (German-17) — **German-17, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, RESCOS-20)  ⟷  `Antécédents familiaux` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, RESCOS-22, RESCOS-23) — **AMBOSS-1, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, RESCOS-20)  ⟷  `Antécédents médicaux et chirurgicaux` (AMBOSS-15) — **AMBOSS-15, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, RESCOS-22, RESCOS-23)  ⟷  `Antécédents familiaux et habitudes` (RESCOS-23) — **RESCOS-23, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, RESCOS-22, RESCOS-23)  ⟷  `Antécédents similaires` (RESCOS-22) — **RESCOS-22, section « a »** distingue ces deux items
- ⛔ `Antécédents gynécologiques` (German-15)  ⟷  `Antécédents obstétricaux et gynécologiques` (German-15) — **German-15, section « a »** distingue ces deux items
- ⛔ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `Auscultation cardio-pulmonaire` (German-21) — **German-21, section « e »** distingue ces deux items
- ⛔ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `Distension abdominale` (German-15) — **German-15, section « e »** distingue ces deux items
- ⛔ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `Inspection abdominale` (German-15, RESCOS-21) — **German-15, section « e »** distingue ces deux items
- ⛔ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `Palpation abdominale` (German-18, German-19, German-20, German-21) — **German-18, section « e »** distingue ces deux items
- ⛔ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `Percussion abdominale` (German-15, German-21, RESCOS-21, RESCOS-22) — **German-15, section « e »** distingue ces deux items
- ⛔ `Auscultation abdominale` (German-15, German-18, German-19, German-20, German-21, RESCOS-18, RESCOS-21, RESCOS-22)  ⟷  `Respiration abdominale` (RESCOS-21) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Inspection de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **AMBOSS-1, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Palpation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **AMBOSS-1, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Percussion de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **AMBOSS-1, section « e »** distingue ces deux items
- ⛔ `Ausculte les 4 quadrants` (RESCOS-18)  ⟷  `Les 4 quadrants` (RESCOS-17, RESCOS-19) — **RESCOS-18, section « e »** distingue ces deux items
- ⛔ `CPRE si angiocholite` (RESCOS-23)  ⟷  `Exclusion angiocholite` (RESCOS-23) — **RESCOS-23, section « m »** distingue ces deux items
- ⛔ `CT abdominal` (AMBOSS-1, AMBOSS-2)  ⟷  `US abdominale` (AMBOSS-1) — **AMBOSS-1, section « m »** distingue ces deux items
- ⛔ `Caractère de la douleur` (German-17, German-18, German-19, German-20, German-21)  ⟷  `Localisation de la douleur` (German-21) — **German-21, section « a »** distingue ces deux items
- ⛔ `Caractère de la douleur` (German-17, German-18, German-19, German-20, German-21)  ⟷  `Migration de la douleur` (German-18, German-19, German-20) — **German-18, section « a »** distingue ces deux items
- ⛔ `Caractéristiques du résultat cutané` (AZYGOS-16)  ⟷  `Caractéristiques du résultat urinaire` (AZYGOS-16) — **AZYGOS-16, section « a »** distingue ces deux items
- ⛔ `Chronologie` (RESCOS-18)  ⟷  `Début/chronologie` (RESCOS-18) — **RESCOS-18, section « a »** distingue ces deux items
- ⛔ `Comment le problème affecte l'enfant` (AMBOSS-15)  ⟷  `Comment le problème affecte le parent` (AMBOSS-15) — **AMBOSS-15, section « a »** distingue ces deux items
- ⛔ `Consommation d'AINS` (RESCOS-21)  ⟷  `Consommation d'alcool` (German-15, RESCOS-18, RESCOS-21) — **RESCOS-21, section « a »** distingue ces deux items
- ⛔ `Contracture abdominale` (German-15, RESCOS-21)  ⟷  `Contracture abdominale généralisée` (RESCOS-21) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Couleur de l'urine` (RESCOS-17)  ⟷  `Couleur des selles` (RESCOS-17, RESCOS-19) — **RESCOS-17, section « a »** distingue ces deux items
- ⛔ `Couleur de l'urine` (RESCOS-17)  ⟷  `Couleur des urines` (RESCOS-19, RESCOS-20) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Couleur des selles` (RESCOS-17, RESCOS-19)  ⟷  `Couleur des urines` (RESCOS-19, RESCOS-20) — **RESCOS-17, section « a »** distingue ces deux items
- ⛔ `Critères d'amélioration` (RESCOS-22)  ⟷  `Critères d'hospitalisation` (German-15, RESCOS-22, RESCOS-23) — **RESCOS-22, section « m »** distingue ces deux items
- ⛔ `Critères d'hospitalisation` (German-15, RESCOS-22, RESCOS-23)  ⟷  `Surveillance et critères d'hospitalisation` (RESCOS-22, RESCOS-23) — **RESCOS-22, section « m »** distingue ces deux items
- ⛔ `Des 4 quadrants` (RESCOS-18)  ⟷  `Les 4 quadrants` (RESCOS-17, RESCOS-19) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Diagnostic différentiel` (RESCOS-22)  ⟷  `Diagnostic principal et différentiel` (RESCOS-22) — **RESCOS-22, section « m »** distingue ces deux items
- ⛔ `Diagnostic différentiel` (RESCOS-22)  ⟷  `Diagnostics différentiels` (German-15, German-16, German-17, German-18, German-19, German-20, German-21, RESCOS-17) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Diagnostic principal et différentiel` (RESCOS-22)  ⟷  `Diagnostics différentiels` (German-15, German-16, German-17, German-18, German-19, German-20, German-21, RESCOS-17) — **RESCOS-22, section « m »** distingue ces deux items
- ⛔ `Diarrhée` (AMBOSS-15, German-16, German-17, German-19)  ⟷  `Diarrhées` (RESCOS-20) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Distension abdominale` (German-15)  ⟷  `Inspection abdominale` (German-15, RESCOS-21) — **German-15, section « e »** distingue ces deux items
- ⛔ `Distension abdominale` (German-15)  ⟷  `Percussion abdominale` (German-15, German-21, RESCOS-21, RESCOS-22) — **German-15, section « e »** distingue ces deux items
- ⛔ `Douglas douloureux` (German-15)  ⟷  `Faciès douloureux` (German-15) — **German-15, section « e »** distingue ces deux items
- ⛔ `Douleur à la décompression` (AZYGOS-16)  ⟷  `Douleur à la secousse` (AZYGOS-16) — **AZYGOS-16, section « e »** distingue ces deux items
- ⛔ `Douleur à la décompression (Blumberg)` (German-15)  ⟷  `Douleur à la pression` (German-15) — **German-15, section « e »** distingue ces deux items
- ⛔ `Douleur à la décompression brutale` (RESCOS-21)  ⟷  `Douleur à la percussion du talon` (RESCOS-21) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Douleur à la percussion` (German-15, RESCOS-21)  ⟷  `Douleur à la percussion du talon` (RESCOS-21) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Douleur à la percussion` (German-15, RESCOS-21)  ⟷  `Douleur à la pression` (German-15) — **German-15, section « e »** distingue ces deux items
- ⛔ `Douleur à la percussion rénale` (AZYGOS-16)  ⟷  `Douleur à la secousse` (AZYGOS-16) — **AZYGOS-16, section « e »** distingue ces deux items
- ⛔ `Début / Durée` (AZYGOS-14)  ⟷  `Début/durée` (RESCOS-17) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Examens complémentaires de seconde ligne` (AMBOSS-1)  ⟷  `Examens complémentaires initiaux` (AMBOSS-1) — **AMBOSS-1, section « m »** distingue ces deux items
- ⛔ `Examens complémentaires secondaires` (AMBOSS-2, AMBOSS-3)  ⟷  `Examens complémentaires urgents` (AMBOSS-2, AMBOSS-3) — **AMBOSS-2, section « m »** distingue ces deux items
- ⛔ `Facteur déclenchant` (AZYGOS-14)  ⟷  `Facteurs calmants` (RESCOS-22) — **RESCOS-22, section « a »** distingue ces deux items
- ⛔ `Facteur déclenchant` (AZYGOS-14)  ⟷  `Facteurs déclenchants` (German-21, RESCOS-22, RESCOS-23) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravant/soulageant` (RESCOS-17)  ⟷  `Facteurs aggravants ou soulageants` (German-17, German-18, German-19, German-20) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15, RESCOS-19, RESCOS-20, RESCOS-22, RESCOS-23)  ⟷  `Facteurs améliorants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15) — **AMBOSS-1, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15, RESCOS-19, RESCOS-20, RESCOS-22, RESCOS-23)  ⟷  `Facteurs calmants` (RESCOS-22) — **RESCOS-22, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15, RESCOS-19, RESCOS-20, RESCOS-22, RESCOS-23)  ⟷  `Facteurs soulageants` (German-21, RESCOS-19, RESCOS-20) — **RESCOS-19, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15, RESCOS-19, RESCOS-20, RESCOS-22, RESCOS-23)  ⟷  `Facteurs soulageants ⊖` (AZYGOS-14) — **RESCOS-19, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15, RESCOS-19, RESCOS-20, RESCOS-22, RESCOS-23)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-16) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants et déclenchants` (RESCOS-23)  ⟷  `Facteurs déclenchants` (German-21, RESCOS-22, RESCOS-23) — **RESCOS-23, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, German-15)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-16) — **AMBOSS-1, section « a »** distingue ces deux items
- ⛔ `Facteurs calmants` (RESCOS-22)  ⟷  `Facteurs déclenchants` (German-21, RESCOS-22, RESCOS-23) — **RESCOS-22, section « a »** distingue ces deux items
- ⛔ `Facteurs calmants` (RESCOS-22)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-16) — **RESCOS-22, section « a »** distingue ces deux items
- ⛔ `Facteurs déclenchants` (German-21, RESCOS-22, RESCOS-23)  ⟷  `Facteurs soulageants` (German-21, RESCOS-19, RESCOS-20) — **German-21, section « a »** distingue ces deux items
- ⛔ `Facteurs soulageants` (German-21, RESCOS-19, RESCOS-20)  ⟷  `Facteurs soulageants ⊖` (AZYGOS-14) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs soulageants` (German-21, RESCOS-19, RESCOS-20)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-16) — **RESCOS-19, section « a »** distingue ces deux items
- ⛔ `Fièvre et frissons` (RESCOS-19)  ⟷  `Fièvre/frissons` (AMBOSS-2, AMBOSS-3) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Grossesse` (German-18)  ⟷  `Grossesses` (AMBOSS-2, AMBOSS-3) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Hospitalisation` (AZYGOS-14)  ⟷  `Hospitalisations` (AMBOSS-1, AMBOSS-2, AMBOSS-3, RESCOS-18) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Hospitalisation` (AZYGOS-14)  ⟷  `Localisation` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, AZYGOS-16, German-17, German-18, German-19, German-20, RESCOS-17, RESCOS-18, RESCOS-19, RESCOS-21, RESCOS-22, RESCOS-23) — **AMBOSS-1, section « a »** distingue ces deux items
- ⛔ `Impact fonctionnel` (RESCOS-23)  ⟷  `Impact professionnel` (RESCOS-23) — **RESCOS-23, section « a »** distingue ces deux items
- ⛔ `Induction de rémission` (German-19)  ⟷  `Maintien de rémission` (German-19) — **German-19, section « m »** distingue ces deux items
- ⛔ `Inspection abdominale` (German-15, RESCOS-21)  ⟷  `Percussion abdominale` (German-15, German-21, RESCOS-21, RESCOS-22) — **German-15, section « e »** distingue ces deux items
- ⛔ `Inspection abdominale` (German-15, RESCOS-21)  ⟷  `Respiration abdominale` (RESCOS-21) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Palpation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **AMBOSS-1, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Percussion de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **AMBOSS-1, section « e »** distingue ces deux items
- ⛔ `Modifications de la couleur des selles` (AMBOSS-1)  ⟷  `Modifications de la couleur des urines` (AMBOSS-1) — **AMBOSS-1, section « a »** distingue ces deux items
- ⛔ `Mère` (AMBOSS-1, AMBOSS-3)  ⟷  `Père` (AMBOSS-1, AMBOSS-3) — **AMBOSS-1, section « a »** distingue ces deux items
- ⛔ `Nausées/Vomissements` (German-17, German-18, German-19, German-20)  ⟷  `Sang dans les vomissements` (German-17, German-18, German-19, German-20) — **German-17, section « a »** distingue ces deux items
- ⛔ `Observation` (RESCOS-20)  ⟷  `Observation du col` (RESCOS-20) — **RESCOS-20, section « e »** distingue ces deux items
- ⛔ `Palpation abdominale` (German-18, German-19, German-20, German-21)  ⟷  `Palpation du foie` (AZYGOS-16, German-21) — **German-21, section « e »** distingue ces deux items
- ⛔ `Palpation abdominale` (German-18, German-19, German-20, German-21)  ⟷  `Percussion abdominale` (German-15, German-21, RESCOS-21, RESCOS-22) — **German-21, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3)  ⟷  `Percussion de l'abdomen` (AMBOSS-1, AMBOSS-2, AMBOSS-3) — **AMBOSS-1, section « e »** distingue ces deux items
- ⛔ `Palpation de la rate` (German-21, RESCOS-22, RESCOS-23)  ⟷  `Palpation des reins` (German-21, RESCOS-23) — **German-21, section « e »** distingue ces deux items
- ⛔ `Palpation superficielle` (RESCOS-20, RESCOS-21)  ⟷  `Veines superficielles` (RESCOS-21) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Par système - digestif` (RESCOS-17)  ⟷  `Par système - urinaire` (RESCOS-17) — **RESCOS-17, section « a »** distingue ces deux items
- ⛔ `Percussion abdominale` (German-15, German-21, RESCOS-21, RESCOS-22)  ⟷  `Respiration abdominale` (RESCOS-21) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Pertes vaginales` (AMBOSS-2, AMBOSS-3, German-17, RESCOS-20)  ⟷  `Sécheresse vaginale` (AMBOSS-2) — **AMBOSS-2, section « a »** distingue ces deux items
- ⛔ `Présence de frissons` (RESCOS-18)  ⟷  `Présence de sang` (RESCOS-17, RESCOS-18) — **RESCOS-18, section « a »** distingue ces deux items
- ⛔ `Présence de frissons` (RESCOS-18)  ⟷  `Présence de vomissement` (RESCOS-18) — **RESCOS-18, section « a »** distingue ces deux items
- ⛔ `Présence de nausée` (RESCOS-18)  ⟷  `Présence de sang` (RESCOS-17, RESCOS-18) — **RESCOS-18, section « a »** distingue ces deux items
- ⛔ `Punition pour les symptômes` (AMBOSS-15)  ⟷  `Récompense pour les symptômes` (AMBOSS-15) — **AMBOSS-15, section « a »** distingue ces deux items
- ⛔ `Qualité` (AMBOSS-1, AMBOSS-15, AMBOSS-2, AMBOSS-3, AZYGOS-14, AZYGOS-16, RESCOS-17, RESCOS-18, RESCOS-19, RESCOS-20)  ⟷  `Quantité` (RESCOS-18) — **RESCOS-18, section « a »** distingue ces deux items
- ⛔ `Questions CAGE - Besoin de boire le matin` (AMBOSS-1)  ⟷  `Questions CAGE - Besoin de réduire` (AMBOSS-1) — **AMBOSS-1, section « a »** distingue ces deux items
- ⛔ `Radiographie abdominale` (German-20)  ⟷  `Échographie abdominale` (German-15, German-19, German-20, RESCOS-23) — **German-20, section « m »** distingue ces deux items
- ⛔ `Recherche de douleur rénale` (German-21)  ⟷  `Recherche de douleur épigastrique` (German-21) — **German-21, section « e »** distingue ces deux items
- ⛔ `Recherche de masse` (German-21)  ⟷  `Recherche de masses` (RESCOS-22) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Recherche de masse` (German-21)  ⟷  `Recherche de splénomégalie` (German-21) — **German-21, section « e »** distingue ces deux items
- ⛔ `Recherche de signes d'alarme` (German-15, German-21)  ⟷  `Recherche de signes d'œsophagite` (German-21) — **German-21, section « e »** distingue ces deux items
- ⛔ `Recherche signes de cholécystite` (RESCOS-23)  ⟷  `Recherche signes de péritonite` (RESCOS-23) — **RESCOS-23, section « m »** distingue ces deux items
- ⛔ `Sang dans les selles` (AMBOSS-1, German-15, German-17, German-18, German-20, RESCOS-19, RESCOS-20)  ⟷  `Sang dans les vomissements` (German-17, German-18, German-19, German-20) — **German-17, section « a »** distingue ces deux items
- ⛔ `Signe du Psoas` (RESCOS-17, RESCOS-18, RESCOS-19)  ⟷  `Signe du flot` (German-15) — **German-15, section « e »** distingue ces deux items
- ⛔ `Signe du Psoas` (RESCOS-17, RESCOS-18, RESCOS-19)  ⟷  `Signe du psoas` (AMBOSS-2, German-15) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Signe du flot` (German-15)  ⟷  `Signe du psoas` (AMBOSS-2, German-15) — **German-15, section « e »** distingue ces deux items
- ⛔ `Signes de dénutrition` (RESCOS-21)  ⟷  `Signes de déshydratation` (RESCOS-21, RESCOS-22) — **RESCOS-21, section « e »** distingue ces deux items
- ⛔ `Status abdominal - auscultation` (RESCOS-17)  ⟷  `Status abdominal - installation` (RESCOS-17, RESCOS-19) — **RESCOS-17, section « e »** distingue ces deux items
- ⛔ `Status abdominal - auscultation` (RESCOS-17)  ⟷  `Status abdominal - palpation` (RESCOS-17) — **RESCOS-17, section « e »** distingue ces deux items
- ⛔ `Status abdominal - auscultation` (RESCOS-17)  ⟷  `Status abdominal - percussion` (RESCOS-17) — **RESCOS-17, section « e »** distingue ces deux items
- ⛔ `Status abdominal - installation` (RESCOS-17, RESCOS-19)  ⟷  `Status abdominal - palpation` (RESCOS-17) — **RESCOS-17, section « e »** distingue ces deux items
- ⛔ `Status abdominal - installation` (RESCOS-17, RESCOS-19)  ⟷  `Status abdominal - percussion` (RESCOS-17) — **RESCOS-17, section « e »** distingue ces deux items
- ⛔ `Status abdominal - palpation` (RESCOS-17)  ⟷  `Status abdominal - percussion` (RESCOS-17) — **RESCOS-17, section « e »** distingue ces deux items
- ⛔ `Status gynécologique - 1` (RESCOS-20)  ⟷  `Status gynécologique - 2` (RESCOS-20) — **RESCOS-20, section « e »** distingue ces deux items
- ⛔ `Symptômes articulaires` (German-15)  ⟷  `Symptômes cardiovasculaires` (German-15) — **German-15, section « a »** distingue ces deux items
- ⛔ `Symptômes associés - fièvre` (RESCOS-18)  ⟷  `Symptômes associés - nausées` (RESCOS-18) — **RESCOS-18, section « a »** distingue ces deux items
- ⛔ `Symptômes généraux` (German-17, German-18, German-19)  ⟷  `Symptômes vaginaux` (AZYGOS-14, German-17, German-18) — **German-17, section « a »** distingue ces deux items
- ⛔ `US transabdominale` (AMBOSS-3)  ⟷  `US transvaginale` (AMBOSS-3) — **AMBOSS-3, section « m »** distingue ces deux items
- ⛔ `Urine` (AZYGOS-16)  ⟷  `Urines` (AZYGOS-16) — **même signature socle A**, déjà appariés dans leur section

## Douleur Thoracique — 12 cas · 37 à juger (2 de forme, 35 de contenu), 89 ⚠️, 53 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Rassurer la patiente sur la prise en charge` (AMBOSS-12)  ⟷  `Rassurer le patient sur la prise en charge` (AMBOSS-13)
- `Communication avec la patiente` (AMBOSS-12)  ⟷  `Communication avec le patient` (AMBOSS-13, AMBOSS-14)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Bref examen neurologique` (German-30)  ⟷  `Examen neurologique` (AMBOSS-13)
- `Énonce le diagnostic de suspicion` (German-30)  ⟷  `Énonce le diagnostic de suspicion principal` (German-31, German-32, German-33)
- `Pas de reflux hépato-jugulaire` (RESCOS-36)  ⟷  `Reflux hépato-jugulaire` (RESCOS-35, RESCOS-37)
- `Prise en charge thérapeutique` (German-32, German-33)  ⟷  `Prise en charge thérapeutique initiale` (German-31)
- `Examens complémentaires demandés` (RESCOS-34)  ⟷  `Examens complémentaires urgents` (AMBOSS-12, AMBOSS-13, AMBOSS-14)
- `Pas de turgescence jugulaire` (RESCOS-36)  ⟷  `Turgescence jugulaire` (RESCOS-35)
- `Examens complémentaires` (RESCOS-36)  ⟷  `Examens complémentaires urgents` (AMBOSS-12, AMBOSS-13, AMBOSS-14)
- `Examen cardiovasculaire` (AMBOSS-12, AMBOSS-13, AMBOSS-14, RESCOS-34)  ⟷  `Examen vasculaire` (German-33)
- `Examens diagnostiques` (German-32, German-33)  ⟷  `Examens diagnostiques urgents` (German-31)
- `Examens complémentaires` (RESCOS-36)  ⟷  `Examens complémentaires demandés` (RESCOS-34)
- `Antécédents médicaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-30)  ⟷  `Antécédents médicaux récents` (RESCOS-34)
- `Facteurs de risque d'embolie pulmonaire` (AZYGOS-22, German-33)  ⟷  `Facteurs de risque d'embolie pulmonaire (Score de Wells)` (German-31, German-32)
- `Hépatomégalie` (RESCOS-37)  ⟷  `Pas d'hépatomégalie` (RESCOS-36)
- `Examens diagnostiques` (German-32, German-33)  ⟷  `Nomme les examens diagnostiques` (German-30)
- `Recherche de symptômes spécifiques` (AMBOSS-12, AMBOSS-14)  ⟷  `Recherche de symptômes spécifiques post-traumatiques` (AMBOSS-13)
- `Auscultation cardiaque` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-31, RESCOS-35, RESCOS-36)  ⟷  `Auscultation des foyers cardiaques` (RESCOS-34)
- `Évaluation du risque global` (RESCOS-37)  ⟷  `Évaluation du risque à 10 ans` (RESCOS-36)
- `Examen cardiovasculaire` (AMBOSS-12, AMBOSS-13, AMBOSS-14, RESCOS-34)  ⟷  `Palpation cardiovasculaire` (RESCOS-37)
- `Intensité de la douleur` (German-31, German-32, German-33)  ⟷  `Qualité de la douleur` (German-30)
- `Auscultation cardiaque` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-31, RESCOS-35, RESCOS-36)  ⟷  `Auscultation cardiaque systématique` (RESCOS-37)
- `Circonstances de la chute` (German-30)  ⟷  `Circonstances déclenchantes` (RESCOS-36)
- `Facteurs améliorants` (AMBOSS-12, AMBOSS-13, AMBOSS-14)  ⟷  `Facteurs atténuants` (RESCOS-35)
- `Inspection de l'état général` (AZYGOS-22)  ⟷  `Inspection générale` (German-31, German-32, German-33, RESCOS-36)
- `Examen pulmonaire` (RESCOS-34)  ⟷  `Examen vasculaire` (German-33)
- `Circonstances de la chute` (German-30)  ⟷  `Circonstances de survenue` (RESCOS-34)
- `Examen corporel général` (AMBOSS-13)  ⟷  `Examen général` (RESCOS-35)
- `Examen thoracique` (AMBOSS-12, AMBOSS-13, AMBOSS-14)  ⟷  `Excursion thoracique` (AZYGOS-22)
- `Auscultation cardiaque` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-31, RESCOS-35, RESCOS-36)  ⟷  `Auscultation des carotides` (RESCOS-37)
- `Examens biologiques` (AMBOSS-12)  ⟷  `Examens diagnostiques` (German-32, German-33)
- `Symptômes associés` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-31, German-32, German-33, RESCOS-34, RESCOS-35, RESCOS-36)  ⟷  `Symptômes pulmonaires associés` (AZYGOS-22)
- `Critères d'hospitalisation` (German-32)  ⟷  `Hospitalisation` (AZYGOS-22)
- `Caractère de la douleur` (German-31, German-32, German-33)  ⟷  `Qualité de la douleur` (German-30)
- `Début de la douleur` (German-30)  ⟷  `Irradiation de la douleur` (German-31, German-32, German-33)
- `Examen vasculaire` (German-33)  ⟷  `Examen vasculaire périphérique` (RESCOS-35)
- `Recherche de signes d'alarme` (German-33)  ⟷  `Recherche de signes d'insuffisance cardiaque` (RESCOS-35, RESCOS-36)

- ⚠️ `Activité physique` (RESCOS-37)  ⟷  `Activité physique régulière` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Affections cardiaques` (RESCOS-37)  ⟷  `Auscultation cardiaque` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-31, RESCOS-35, RESCOS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ampliation thoracique` (RESCOS-35)  ⟷  `Examen thoracique` (AMBOSS-12, AMBOSS-13, AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ampliation thoracique` (RESCOS-35)  ⟷  `Inspection thoracique` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ampliation thoracique` (RESCOS-35)  ⟷  `Traumatisme thoracique` (German-31, German-32, German-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Arrêt du tabac` (AZYGOS-22)  ⟷  `Arrêt du tabac impératif` (German-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Asymétrie thoracique` (German-32)  ⟷  `CT thoracique` (AMBOSS-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Asymétrie thoracique` (German-32)  ⟷  `Examen thoracique` (AMBOSS-12, AMBOSS-13, AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation bilatérale des carotides` (RESCOS-37)  ⟷  `Auscultation des artères carotides` (AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des artères carotides` (AMBOSS-14)  ⟷  `Auscultation des carotides` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des artères carotides` (AMBOSS-14)  ⟷  `Auscultation des foyers cardiaques` (RESCOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des carotides` (RESCOS-37)  ⟷  `Auscultation des foyers cardiaques` (RESCOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bilan biologique` (RESCOS-37)  ⟷  `Examens biologiques` (AMBOSS-12) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT thoracique` (AMBOSS-13)  ⟷  `Examen thoracique` (AMBOSS-12, AMBOSS-13, AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT thoracique` (AMBOSS-13)  ⟷  `Excursion thoracique` (AZYGOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT thoracique` (AMBOSS-13)  ⟷  `Inspection thoracique` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Circonstances de survenue` (RESCOS-34)  ⟷  `Condition de survenue` (RESCOS-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Classification` (RESCOS-35)  ⟷  `Classification probable` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contrôle des facteurs de risque cardiovasculaire` (German-31)  ⟷  `Facteurs de risque cardiovasculaire` (German-31, German-33, RESCOS-36, RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contrôle des facteurs de risque cardiovasculaire` (German-31)  ⟷  `Identification des facteurs de risque cardiovasculaire` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contrôle des facteurs de risque cardiovasculaire` (German-31)  ⟷  `Éducation sur les facteurs de risque cardiovasculaires` (AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Creux épigastrique` (RESCOS-37)  ⟷  `Douleur épigastrique` (German-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur liée à la respiration` (German-31, German-32, German-33)  ⟷  `Douleur à la pression` (AZYGOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la poitrine` (RESCOS-34)  ⟷  `Douleur à la pression` (AZYGOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs ou œdèmes des membres inférieurs` (RESCOS-35)  ⟷  `Pas d'œdèmes des membres inférieurs` (RESCOS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs ou œdèmes des membres inférieurs` (RESCOS-35)  ⟷  `Œdèmes membres inférieurs` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Drainage thoracique` (AZYGOS-22)  ⟷  `Examen thoracique` (AMBOSS-12, AMBOSS-13, AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Drainage thoracique` (AZYGOS-22)  ⟷  `Radiographie thoracique` (AMBOSS-12, German-31, German-33, RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Drainage thoracique` (AZYGOS-22)  ⟷  `Traumatisme thoracique` (German-31, German-32, German-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Embolie pulmonaire` (German-31, German-32)  ⟷  `Examen pulmonaire` (RESCOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen des extrémités` (AMBOSS-12, AMBOSS-14)  ⟷  `Observation des extrémités` (RESCOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen des extrémités` (AMBOSS-12, AMBOSS-14)  ⟷  `Température des extrémités` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AMBOSS-13)  ⟷  `Examens biologiques` (AMBOSS-12) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (RESCOS-34)  ⟷  `Examens complémentaires` (RESCOS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (RESCOS-34)  ⟷  `Pulmonaire` (RESCOS-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Excursion thoracique` (AZYGOS-22)  ⟷  `Inspection thoracique` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Expectoration` (AZYGOS-22)  ⟷  `Toux/expectoration` (German-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Explications au patient des impressions diagnostiques préliminaires` (AMBOSS-13, AMBOSS-14)  ⟷  `Explications à la patiente des impressions diagnostiques préliminaires` (AMBOSS-12) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteur déclenchant 1er épisode` (RESCOS-37)  ⟷  `Facteurs déclenchants et modulateurs` (German-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-30, RESCOS-35)  ⟷  `Facteurs soulageants` (RESCOS-37) — **antonymes présumés** (aggravant / soulageant) : aucune grille ne les porte ensemble, donc la propriété 8 n'a pas de témoin. *(Par ailleurs inerte : la propriété 7 la refuserait.)*
- ⚠️ `Facteurs améliorants` (AMBOSS-12, AMBOSS-13, AMBOSS-14)  ⟷  `Facteurs d'amélioration` (German-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs de risque cardiovasculaire` (German-31, German-33, RESCOS-36, RESCOS-37)  ⟷  `Identification des facteurs de risque cardiovasculaire` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs de risque cardiovasculaire` (German-31, German-33, RESCOS-36, RESCOS-37)  ⟷  `Stratification du risque cardiovasculaire` (RESCOS-36, RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs de risque cardiovasculaire` (German-31, German-33, RESCOS-36, RESCOS-37)  ⟷  `Éducation sur les facteurs de risque cardiovasculaires` (AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs modulateurs` (German-31, German-32, RESCOS-34)  ⟷  `Facteurs soulageants` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fièvre` (AZYGOS-22, German-31)  ⟷  `Frère` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence cardiaque` (RESCOS-37)  ⟷  `Prise de la fréquence cardiaque` (RESCOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension` (German-31, German-33)  ⟷  `Hypertension probable` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (RESCOS-37)  ⟷  `Hypertension probable` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (RESCOS-37)  ⟷  `Tension artérielle` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Identification des facteurs de risque cardiovasculaire` (RESCOS-37)  ⟷  `Éducation sur les facteurs de risque cardiovasculaires` (AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Information du patient` (German-32, German-33)  ⟷  `Position du patient` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des membres inférieurs` (AMBOSS-12, German-31)  ⟷  `Pas d'œdèmes des membres inférieurs` (RESCOS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des membres inférieurs` (AMBOSS-12, German-31)  ⟷  `Œdèmes membres inférieurs` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du thorax` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-30)  ⟷  `Inspection thoracique` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Laboratoire de base` (AZYGOS-22)  ⟷  `Laboratoires` (RESCOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Observation d'une turgescence jugulaire` (RESCOS-34)  ⟷  `Pas de turgescence jugulaire` (RESCOS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Observation des extrémités` (RESCOS-34)  ⟷  `Température des extrémités` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Occupation` (AMBOSS-12, AMBOSS-13, AMBOSS-14)  ⟷  `Préoccupations` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Oxygénothérapie` (AZYGOS-22)  ⟷  `Oxygénothérapie haut débit` (German-32) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation` (German-30)  ⟷  `Palpitations` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-31, German-33, RESCOS-34, RESCOS-35, RESCOS-36, RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation des membres inférieurs` (AMBOSS-12)  ⟷  `Pas d'œdèmes des membres inférieurs` (RESCOS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation des membres inférieurs` (AMBOSS-12)  ⟷  `Œdèmes membres inférieurs` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation des pouls pédieux` (AMBOSS-12)  ⟷  `Palpation des pouls périphériques` (RESCOS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas d'œdèmes des membres inférieurs` (RESCOS-36)  ⟷  `Œdèmes membres inférieurs` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas de reflux hépato-jugulaire` (RESCOS-36)  ⟷  `Recherche d'un reflux hépato-jugulaire` (RESCOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas de reflux hépato-jugulaire` (RESCOS-36)  ⟷  `Réflux hépato-jugulaire` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas de souffle abdominal` (RESCOS-36)  ⟷  `Recherche de souffle abdominal` (RESCOS-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pneumonie` (German-31, RESCOS-34)  ⟷  `Pulmonaire` (RESCOS-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pneumothorax` (German-30, German-31, RESCOS-35)  ⟷  `Pneumothorax > 20%` (German-32) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie de contrôle` (AZYGOS-22)  ⟷  `Radiographie du thorax` (RESCOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie du thorax` (RESCOS-34)  ⟷  `Radiographie thoracique` (AMBOSS-12, German-31, German-33, RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie thoracique` (AMBOSS-12, German-31, German-33, RESCOS-37)  ⟷  `Radiographie thoracique (2 incidences)` (AZYGOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie thoracique` (AMBOSS-12, German-31, German-33, RESCOS-37)  ⟷  `Échographie thoracique` (AZYGOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'un reflux hépato-jugulaire` (RESCOS-34)  ⟷  `Reflux hépato-jugulaire` (RESCOS-35, RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'un reflux hépato-jugulaire` (RESCOS-34)  ⟷  `Réflux hépato-jugulaire` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'alarme` (German-33)  ⟷  `Recherche de signes de TVP` (German-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de souffle` (German-31)  ⟷  `Recherche de souffle abdominal` (RESCOS-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de souffle` (German-31)  ⟷  `Recherche de souffle carotidien` (RESCOS-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de souffle` (German-31)  ⟷  `Recherche de souffles carotidiens` (RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de souffle` (German-31)  ⟷  `Recherche de souffles fémoraux` (RESCOS-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche des préoccupations et questions de la patiente` (AMBOSS-12)  ⟷  `Recherche des préoccupations et questions du patient` (AMBOSS-13, AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réaction appropriée au défi concernant l'anxiété` (AMBOSS-12)  ⟷  `Réaction appropriée au défi concernant les médicaments` (AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes d'alarme nécessitant une prise en charge urgente` (RESCOS-36)  ⟷  `Signes d'alarme nécessitant une reconsultation urgente` (German-32) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes infectieux` (AZYGOS-22)  ⟷  `Signes vitaux` (RESCOS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Échocardiographie` (AMBOSS-14)  ⟷  `Échocardiographie de repos` (RESCOS-36, RESCOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Échocardiographie transthoracique` (AMBOSS-12)  ⟷  `Échographie thoracique` (AZYGOS-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Éruption/changements cutanés` (AMBOSS-12, AMBOSS-14)  ⟷  `Éruption/changements cutanés (ecchymoses)` (AMBOSS-13) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'accord de la patiente avec le plan diagnostique` (AMBOSS-12)  ⟷  `Évaluation de l'accord du patient avec le plan diagnostique` (AMBOSS-13, AMBOSS-14) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Alimentation` (AMBOSS-12)  ⟷  `Palpitations` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-31, German-33, RESCOS-34, RESCOS-35, RESCOS-36, RESCOS-37) — **AMBOSS-12, section « a »** distingue ces deux items
- ⛔ `Antécédents cardiaques` (German-32)  ⟷  `Antécédents familiaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, RESCOS-36) — **German-32, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22)  ⟷  `Antécédents familiaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, RESCOS-36) — **AMBOSS-12, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22)  ⟷  `Antécédents médicaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-30) — **AMBOSS-12, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, RESCOS-36)  ⟷  `Antécédents familiaux d'infarctus` (German-31, German-33) — **German-31, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, RESCOS-36)  ⟷  `Antécédents médicaux` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-30) — **AMBOSS-12, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux cardiovasculaires` (RESCOS-37)  ⟷  `Antécédents personnels cardiovasculaires` (RESCOS-37) — **RESCOS-37, section « a »** distingue ces deux items
- ⛔ `Auscultation bilatérale des carotides` (RESCOS-37)  ⟷  `Auscultation des carotides` (RESCOS-37) — **RESCOS-37, section « e »** distingue ces deux items
- ⛔ `Caractère de la douleur` (German-31, German-32, German-33)  ⟷  `Localisation de la douleur` (German-30, German-31, German-32, German-33) — **German-31, section « a »** distingue ces deux items
- ⛔ `Classe II: Limitation légère` (RESCOS-36)  ⟷  `Classe III: Limitation marquée` (RESCOS-36) — **RESCOS-36, section « a »** distingue ces deux items
- ⛔ `Coronarographie` (AMBOSS-14)  ⟷  `Échocardiographie` (AMBOSS-14) — **AMBOSS-14, section « m »** distingue ces deux items
- ⛔ `Drainage thoracique` (AZYGOS-22)  ⟷  `Échographie thoracique` (AZYGOS-22) — **AZYGOS-22, section « m »** distingue ces deux items
- ⛔ `Début de la douleur` (German-30)  ⟷  `Qualité de la douleur` (German-30) — **German-30, section « a »** distingue ces deux items
- ⛔ `Facteur aggravant` (RESCOS-34)  ⟷  `Facteurs aggravants` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-30, RESCOS-35) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteur aggravant` (RESCOS-34)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-22) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteur atténuant` (RESCOS-34)  ⟷  `Facteurs atténuants` (RESCOS-35) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteur déclenchant 1er épisode` (RESCOS-37)  ⟷  `Facteur déclenchant 2ème épisode` (RESCOS-37) — **RESCOS-37, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-30, RESCOS-35)  ⟷  `Facteurs améliorants` (AMBOSS-12, AMBOSS-13, AMBOSS-14) — **AMBOSS-12, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-30, RESCOS-35)  ⟷  `Facteurs atténuants` (RESCOS-35) — **RESCOS-35, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-30, RESCOS-35)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-22) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AMBOSS-12, AMBOSS-13, AMBOSS-14, German-30, RESCOS-35)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-22) — **AZYGOS-22, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (AMBOSS-12, AMBOSS-13, AMBOSS-14)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-22) — **AMBOSS-12, section « a »** distingue ces deux items
- ⛔ `Facteurs de risque cardiovasculaire` (German-31, German-33, RESCOS-36, RESCOS-37)  ⟷  `Facteurs de risque d'embolie pulmonaire` (AZYGOS-22, German-33) — **German-33, section « a »** distingue ces deux items
- ⛔ `Facteurs soulageants` (RESCOS-37)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-22) — **AZYGOS-22, section « a »** distingue ces deux items
- ⛔ `Facteurs soulageants` (RESCOS-37)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-22) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Hospitalisation` (AZYGOS-22)  ⟷  `Hospitalisations` (AMBOSS-12, AMBOSS-13, AMBOSS-14, RESCOS-35, RESCOS-37) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Hospitalisation` (AZYGOS-22)  ⟷  `Localisation` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, RESCOS-34, RESCOS-35, RESCOS-37) — **AMBOSS-12, section « a »** distingue ces deux items
- ⛔ `Identification des facteurs de risque cardiovasculaire` (RESCOS-37)  ⟷  `Stratification du risque cardiovasculaire` (RESCOS-36, RESCOS-37) — **RESCOS-37, section « m »** distingue ces deux items
- ⛔ `Impact sur activités` (RESCOS-37)  ⟷  `Limitation des activités` (RESCOS-37) — **RESCOS-37, section « a »** distingue ces deux items
- ⛔ `Importance des mesures hygiéno-diététiques` (German-33)  ⟷  `Mesures hygiéno-diététiques` (German-33) — **German-33, section « m »** distingue ces deux items
- ⛔ `Infection récente` (German-32)  ⟷  `Infections récentes` (AMBOSS-12, AMBOSS-13, AMBOSS-14) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Inspection des membres inférieurs` (AMBOSS-12, German-31)  ⟷  `Palpation des membres inférieurs` (AMBOSS-12) — **AMBOSS-12, section « e »** distingue ces deux items
- ⛔ `Inspection du thorax` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, German-30)  ⟷  `Palpation du thorax` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22) — **AMBOSS-12, section « e »** distingue ces deux items
- ⛔ `Irradiation de la douleur` (German-31, German-32, German-33)  ⟷  `Localisation de la douleur` (German-30, German-31, German-32, German-33) — **German-31, section « a »** distingue ces deux items
- ⛔ `Localisation de la douleur` (German-30, German-31, German-32, German-33)  ⟷  `Qualité de la douleur` (German-30) — **German-30, section « a »** distingue ces deux items
- ⛔ `Mère` (RESCOS-37)  ⟷  `Père` (RESCOS-37) — **RESCOS-37, section « a »** distingue ces deux items
- ⛔ `Palpation des pouls pédieux` (AMBOSS-12)  ⟷  `Palpation du pouls radial` (AMBOSS-12, AMBOSS-13, AMBOSS-14) — **AMBOSS-12, section « e »** distingue ces deux items
- ⛔ `Palpation du pouls radial` (AMBOSS-12, AMBOSS-13, AMBOSS-14)  ⟷  `Palpation du thorax` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22) — **AMBOSS-12, section « e »** distingue ces deux items
- ⛔ `Pas de souffle abdominal` (RESCOS-36)  ⟷  `Pas de souffle audible` (RESCOS-36) — **RESCOS-36, section « e »** distingue ces deux items
- ⛔ `Position du patient` (RESCOS-37)  ⟷  `Positionnement du patient` (RESCOS-37) — **RESCOS-37, section « e »** distingue ces deux items
- ⛔ `Pouls fémoraux présents` (RESCOS-36)  ⟷  `Pouls pédieux présents` (RESCOS-36) — **RESCOS-36, section « e »** distingue ces deux items
- ⛔ `Qualité` (AMBOSS-12, AMBOSS-13, AMBOSS-14, AZYGOS-22, RESCOS-34, RESCOS-35, RESCOS-37)  ⟷  `Quantité` (RESCOS-35) — **RESCOS-35, section « a »** distingue ces deux items
- ⛔ `Radiographie thoracique` (AMBOSS-12, German-31, German-33, RESCOS-37)  ⟷  `Échocardiographie transthoracique` (AMBOSS-12) — **AMBOSS-12, section « m »** distingue ces deux items
- ⛔ `Recherche de souffle abdominal` (RESCOS-35)  ⟷  `Recherche de souffle carotidien` (RESCOS-35) — **RESCOS-35, section « e »** distingue ces deux items
- ⛔ `Recherche de souffle abdominal` (RESCOS-35)  ⟷  `Recherche de souffles carotidiens` (RESCOS-37) — **RESCOS-35, section « e »** distingue ces deux items
- ⛔ `Recherche de souffle abdominal` (RESCOS-35)  ⟷  `Recherche de souffles fémoraux` (RESCOS-35) — **RESCOS-35, section « e »** distingue ces deux items
- ⛔ `Recherche de souffle carotidien` (RESCOS-35)  ⟷  `Recherche de souffles carotidiens` (RESCOS-37) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Recherche de souffle carotidien` (RESCOS-35)  ⟷  `Recherche de souffles fémoraux` (RESCOS-35) — **RESCOS-35, section « e »** distingue ces deux items
- ⛔ `Recherche de souffles carotidiens` (RESCOS-37)  ⟷  `Recherche de souffles fémoraux` (RESCOS-35) — **RESCOS-35, section « e »** distingue ces deux items
- ⛔ `Reflux hépato-jugulaire` (RESCOS-35, RESCOS-37)  ⟷  `Réflux hépato-jugulaire` (RESCOS-37) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Stress professionnel` (RESCOS-36)  ⟷  `Stress émotionnel` (RESCOS-36) — **RESCOS-36, section « a »** distingue ces deux items
- ⛔ `Voyage récent` (AMBOSS-12, AMBOSS-14, German-31, German-32, German-33)  ⟷  `Voyages récents` (RESCOS-34, RESCOS-35) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-22)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-22) — **AZYGOS-22, section « a »** distingue ces deux items

## Douleur au Poignet — 2 cas · 3 à juger (0 de forme, 3 de contenu), 2 ⚠️, 4 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Test de Tinel` (German-24)  ⟷  `Test de ténodèse` (AZYGOS-5)
- `Localisation` (AZYGOS-5)  ⟷  `Localisation précise` (German-24)
- `Désinfection des mains` (German-24)  ⟷  `Inspection de la main` (AZYGOS-5)

- ⚠️ `Examens complémentaires` (German-24)  ⟷  `Tests complémentaires` (German-24) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fonction du pouce` (AZYGOS-5)  ⟷  `Opposition du pouce` (German-24) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Pronation / supination` (AZYGOS-5)  ⟷  `Pronation/supination` (German-24) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Traitement conservateur` (AZYGOS-5, German-24)  ⟷  `Traitement opératoire` (AZYGOS-5) — **AZYGOS-5, section « m »** distingue ces deux items
- ⛔ `Évaluation de la force` (German-24)  ⟷  `Évaluation de la musculature` (German-24) — **German-24, section « e »** distingue ces deux items
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-5)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-5) — **AZYGOS-5, section « a »** distingue ces deux items

## Douleur d'Épaule — 5 cas · 8 à juger (2 de forme, 6 de contenu), 17 ⚠️, 31 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Déplacé` (RESCOS-69)  ⟷  `Déplacée` (RESCOS-69b)
- `Distal` (RESCOS-69)  ⟷  `Distale` (RESCOS-69b)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Tests de la coiffe des rotateurs` (AZYGOS-11)  ⟷  `Tests spécifiques de la coiffe des rotateurs` (German-27)
- `Facteurs aggravant` (RESCOS-69b)  ⟷  `Facteurs aggravant/atténuant` (RESCOS-69)
- `Facteurs aggravant/atténuant` (RESCOS-69)  ⟷  `Facteurs atténuant` (RESCOS-69b)
- `Inspection` (AZYGOS-11)  ⟷  `Inspection bras D` (RESCOS-69, RESCOS-69b)
- `Caractérisation de la douleur à l'épaule` (AMBOSS-39)  ⟷  `Caractérisation temporelle de la douleur` (German-27)
- `Consultation et suivi orthopédique` (RESCOS-69b)  ⟷  `Réduction fermée, plâtre, consultation et suivi orthopédique` (RESCOS-69)

- ⚠️ `Autres douleurs articulaires` (AZYGOS-11)  ⟷  `Douleurs articulaires` (AMBOSS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs ailleurs` (RESCOS-69, RESCOS-69b)  ⟷  `Douleurs articulaires` (AMBOSS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravant/atténuant` (RESCOS-69)  ⟷  `Facteurs aggravants` (AMBOSS-39, German-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravant/atténuant` (RESCOS-69)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs améliorants` (AMBOSS-39, German-27)  ⟷  `Facteurs atténuant` (RESCOS-69b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Faiblesse des membres supérieurs` (AMBOSS-39)  ⟷  `Inspection des membres supérieurs` (AMBOSS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fièvre aiguë / frissons` (AZYGOS-11)  ⟷  `Fièvre/frissons` (AMBOSS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'épaule` (German-27)  ⟷  `Inspection de la région de l'épaule` (AMBOSS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Les deux` (RESCOS-69)  ⟷  `Les deux types` (RESCOS-69) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Lésions antérieures` (AZYGOS-11)  ⟷  `Épisodes antérieurs` (AMBOSS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Prise en charge` (RESCOS-69, RESCOS-69b)  ⟷  `Prise en charge antérieure` (AZYGOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie de l'épaule gauche` (AMBOSS-39)  ⟷  `Radiographie de l’épaule` (AZYGOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Symptomatique` (AZYGOS-11)  ⟷  `Symptomatologie B` (AZYGOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test d'appréhension antérieur` (German-27)  ⟷  `Test d’appréhension` (AZYGOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test d'appréhension postérieur` (German-27)  ⟷  `Test d’appréhension` (AZYGOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test d'injection lidocaïne sous-acromiale` (AMBOSS-39)  ⟷  `Tests de conflit sous-acromial` (German-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traumatisme` (AMBOSS-39, German-27)  ⟷  `Traumatisme / chute` (AZYGOS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-39, German-27)  ⟷  `Antécédents familiaux` (AMBOSS-39, AZYGOS-11, German-27) — **AMBOSS-39, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-39, German-27)  ⟷  `Antécédents médicaux` (AMBOSS-39, AZYGOS-11, German-27) — **AMBOSS-39, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-39, AZYGOS-11, German-27)  ⟷  `Antécédents médicaux` (AMBOSS-39, AZYGOS-11, German-27) — **AMBOSS-39, section « a »** distingue ces deux items
- ⛔ `Articulation acromio-claviculaire` (German-27)  ⟷  `Examen de l'articulation acromio-claviculaire` (German-27) — **German-27, section « e »** distingue ces deux items
- ⛔ `Espace sous-acromial` (AZYGOS-11)  ⟷  `Tests sous-acromiaux` (AZYGOS-11) — **AZYGOS-11, section « e »** distingue ces deux items
- ⛔ `Examen ciblé de la sensibilité des membres supérieurs` (AMBOSS-39)  ⟷  `Examen ciblé des mouvements passifs et actifs des membres supérieurs` (AMBOSS-39) — **AMBOSS-39, section « e »** distingue ces deux items
- ⛔ `Examen ciblé de la sensibilité des membres supérieurs` (AMBOSS-39)  ⟷  `Examen ciblé des réflexes ostéotendineux des membres supérieurs` (AMBOSS-39) — **AMBOSS-39, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravant` (RESCOS-69b)  ⟷  `Facteurs aggravants` (AMBOSS-39, German-27) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravant` (RESCOS-69b)  ⟷  `Facteurs améliorants` (AMBOSS-39, German-27) — **AMBOSS-39, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravant` (RESCOS-69b)  ⟷  `Facteurs atténuant` (RESCOS-69b) — **RESCOS-69b, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravant` (RESCOS-69b)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-11) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AMBOSS-39, German-27)  ⟷  `Facteurs améliorants` (AMBOSS-39, German-27) — **AMBOSS-39, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-39, German-27)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-11) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AMBOSS-39, German-27)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-11) — **AZYGOS-11, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (AMBOSS-39, German-27)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-11) — **AMBOSS-39, section « a »** distingue ces deux items
- ⛔ `IRM de l'épaule gauche` (AMBOSS-39)  ⟷  `Radiographie de l'épaule gauche` (AMBOSS-39) — **AMBOSS-39, section « m »** distingue ces deux items
- ⛔ `IRM de l'épaule gauche` (AMBOSS-39)  ⟷  `US de l'épaule gauche` (AMBOSS-39) — **AMBOSS-39, section « m »** distingue ces deux items
- ⛔ `Infection récente` (German-27)  ⟷  `Infections récentes` (AMBOSS-39) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Inspection de la région de l'épaule` (AMBOSS-39)  ⟷  `Palpation de la région de l'épaule` (AMBOSS-39) — **AMBOSS-39, section « e »** distingue ces deux items
- ⛔ `Mobilité active` (AZYGOS-11)  ⟷  `Mobilité passive` (AZYGOS-11) — **AZYGOS-11, section « e »** distingue ces deux items
- ⛔ `Questions de la patiente` (German-27)  ⟷  `Synthèse et questions de la patiente` (German-27) — **German-27, section « a »** distingue ces deux items
- ⛔ `Radiographie de l'épaule gauche` (AMBOSS-39)  ⟷  `US de l'épaule gauche` (AMBOSS-39) — **AMBOSS-39, section « m »** distingue ces deux items
- ⛔ `Rotation externe` (German-27)  ⟷  `Rotation interne` (German-27) — **German-27, section « e »** distingue ces deux items
- ⛔ `Rotation externe le long du corps / en abduction 90°` (AZYGOS-11)  ⟷  `Rotation interne le long du corps / en abduction 90°` (AZYGOS-11) — **AZYGOS-11, section « e »** distingue ces deux items
- ⛔ `Rotation externe le long du corps / en abduction 90°` (AZYGOS-11)  ⟷  `Rotation interne selon Apley / en abduction 90°` (AZYGOS-11) — **AZYGOS-11, section « e »** distingue ces deux items
- ⛔ `Rotation interne le long du corps / en abduction 90°` (AZYGOS-11)  ⟷  `Rotation interne selon Apley / en abduction 90°` (AZYGOS-11) — **AZYGOS-11, section « e »** distingue ces deux items
- ⛔ `Test d'appréhension antérieur` (German-27)  ⟷  `Test d'appréhension postérieur` (German-27) — **German-27, section « e »** distingue ces deux items
- ⛔ `Test de Jobe` (AMBOSS-39)  ⟷  `Test de Neer` (AMBOSS-39, AZYGOS-11, German-27) — **AMBOSS-39, section « e »** distingue ces deux items
- ⛔ `Test de Neer` (AMBOSS-39, AZYGOS-11, German-27)  ⟷  `Test de Speed` (AZYGOS-11) — **AZYGOS-11, section « e »** distingue ces deux items
- ⛔ `Test de Speed` (AZYGOS-11)  ⟷  `Tests de DD` (AZYGOS-11) — **AZYGOS-11, section « e »** distingue ces deux items
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-11)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-11) — **AZYGOS-11, section « a »** distingue ces deux items

## Douleur de Hanche — 3 cas · 6 à juger (0 de forme, 6 de contenu), 23 ⚠️, 15 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Examens complémentaires` (RESCOS-28)  ⟷  `Examens complémentaires d'imagerie` (German-29)
- `Inspection de la marche et posture` (RESCOS-28)  ⟷  `Observation de la marche et de la posture` (German-29)
- `Surveillance et pronostic` (German-29)  ⟷  `Surveillance et suivi` (RESCOS-28)
- `Extension de la hanche` (AZYGOS-19)  ⟷  `Palpation de la hanche` (RESCOS-28)
- `Palpation de la hanche` (RESCOS-28)  ⟷  `Phase 1: Articulation de la hanche` (AZYGOS-19)
- `Symptômes associés` (AZYGOS-19)  ⟷  `Symptômes associés locomoteurs` (German-29)

- ⚠️ `Abducteurs (moyen fessier)` (RESCOS-28)  ⟷  `Force des abducteurs (moyen fessier)` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Adaptation de la charge` (AZYGOS-19)  ⟷  `Augmentation de la charge` (AZYGOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Adaptation de la charge` (AZYGOS-19)  ⟷  `Palpation de la hanche` (RESCOS-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aggravation progressive de l'impotence fonctionnelle` (RESCOS-28)  ⟷  `Progression de l'impotence fonctionnelle` (RESCOS-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Asthénie importante` (German-29)  ⟷  `Pas d'asthénie importante` (RESCOS-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres anti-inflammatoires` (RESCOS-28)  ⟷  `Signes inflammatoires` (AZYGOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `DD Hanche` (AZYGOS-19)  ⟷  `IRM de hanche` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs nocturnes` (German-29)  ⟷  `Pas de sueurs nocturnes` (RESCOS-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Extenseurs de hanche` (RESCOS-28)  ⟷  `Extension de hanche` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Extenseurs de hanche` (RESCOS-28)  ⟷  `Extension de la hanche` (AZYGOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants` (German-29)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-19) — **antonymes présumés** (aggravant / soulageant) : aucune grille ne les porte ensemble, donc la propriété 8 n'a pas de témoin. *(Par ailleurs inerte : la propriété 7 la refuserait.)*
- ⚠️ `Flexion de hanche` (German-29)  ⟷  `IRM de hanche` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fléchisseurs de hanche` (RESCOS-28)  ⟷  `Force des fléchisseurs de hanche` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fonction de l’articulation de la hanche` (AZYGOS-19)  ⟷  `Phase 1: Articulation de la hanche` (AZYGOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Force des abducteurs` (RESCOS-28)  ⟷  `Force des rotateurs` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fractures antérieures` (German-29)  ⟷  `Opérations antérieures` (AZYGOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Localisation` (AZYGOS-19, RESCOS-28)  ⟷  `Localisation précise` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas de sueurs nocturnes` (RESCOS-28)  ⟷  `Sueurs nocturnes` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie bassin face debout` (RESCOS-28)  ⟷  `Radiographie du bassin de face` (AZYGOS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test FABER (Flexion-Abduction-External-Rotation)` (RESCOS-28)  ⟷  `Test FADER-R (Flexion Adduction External Rotation - Resisted)` (AZYGOS-19) — **antonymes présumés** (abduction / adduction) : aucune grille ne les porte ensemble, donc la propriété 8 n'a pas de témoin. *(Par ailleurs inerte : la propriété 7 la refuserait.)*
- ⚠️ `Test FABER (Patrick / en 4)` (AZYGOS-19)  ⟷  `Test FABER/Patrick (signe du 4)` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traumatisme / Chute` (AZYGOS-19)  ⟷  `Traumatisme récent` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Type de douleur` (RESCOS-28)  ⟷  `Type/qualité de douleur` (German-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Abduction` (German-29, RESCOS-28)  ⟷  `Adduction` (German-29, RESCOS-28) — **German-29, section « e »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (German-29)  ⟷  `Antécédents familiaux` (AZYGOS-19, German-29) — **German-29, section « a »** distingue ces deux items
- ⛔ `Douleurs nocturnes` (German-29)  ⟷  `Sueurs nocturnes` (German-29) — **German-29, section « a »** distingue ces deux items
- ⛔ `Examen fonctionnel - Mobilité active` (RESCOS-28)  ⟷  `Examen fonctionnel - Mobilité passive` (RESCOS-28) — **RESCOS-28, section « e »** distingue ces deux items
- ⛔ `Extension de hanche` (German-29)  ⟷  `Extension de la hanche` (AZYGOS-19) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Extension de hanche` (German-29)  ⟷  `Flexion de hanche` (German-29) — **German-29, section « e »** distingue ces deux items
- ⛔ `Extension de la hanche` (AZYGOS-19)  ⟷  `Flexion de hanche` (German-29) — **German-29, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (German-29)  ⟷  `Facteurs améliorants` (German-29) — **German-29, section « a »** distingue ces deux items
- ⛔ `Immunosuppresseurs` (German-29)  ⟷  `Immunosuppression` (German-29) — **German-29, section « a »** distingue ces deux items
- ⛔ `Recherche d'asymétrie` (German-29)  ⟷  `Recherche de varices` (German-29) — **German-29, section « e »** distingue ces deux items
- ⛔ `Rotateurs externes` (RESCOS-28)  ⟷  `Rotateurs internes` (RESCOS-28) — **RESCOS-28, section « e »** distingue ces deux items
- ⛔ `Rotateurs externes` (RESCOS-28)  ⟷  `Rotation externe` (German-29, RESCOS-28) — **RESCOS-28, section « e »** distingue ces deux items
- ⛔ `Rotateurs internes` (RESCOS-28)  ⟷  `Rotation interne` (German-29, RESCOS-28) — **RESCOS-28, section « e »** distingue ces deux items
- ⛔ `Rotation externe` (German-29, RESCOS-28)  ⟷  `Rotation interne` (German-29, RESCOS-28) — **German-29, section « e »** distingue ces deux items
- ⛔ `Symptômes urinaires` (German-29)  ⟷  `Symptômes vasculaires` (German-29) — **German-29, section « a »** distingue ces deux items

## Douleur du Genou — 3 cas · 7 à juger (0 de forme, 7 de contenu), 11 ⚠️, 16 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Caractérisation de la douleur` (AMBOSS-25)  ⟷  `Irradiation de la douleur` (German-23)
- `Inspection globale` (AZYGOS-17)  ⟷  `Inspection générale` (German-23)
- `Caractère de la douleur` (German-23)  ⟷  `Caractérisation de la douleur` (AMBOSS-25)
- `Ligaments croisés` (AZYGOS-17)  ⟷  `Tests des ligaments croisés` (German-23)
- `Symptômes actuels` (German-23)  ⟷  `Symptômes mécaniques` (AZYGOS-17)
- `Symptômes actuels` (German-23)  ⟷  `Symptômes associés` (AMBOSS-25, AZYGOS-17)
- `Caractérisation de la douleur` (AMBOSS-25)  ⟷  `Localisation précise de la douleur` (German-23)

- ⚠️ `Axes des membres inférieurs` (German-23)  ⟷  `Chaleur du membre inférieur` (AMBOSS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Axes des membres inférieurs` (German-23)  ⟷  `Inspection des membres inférieurs` (AMBOSS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Axes des membres inférieurs` (German-23)  ⟷  `Palpation des membres inférieurs` (AMBOSS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostic principal` (German-23)  ⟷  `Motif principal` (AMBOSS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Intensité (échelle 0-10)` (AMBOSS-25)  ⟷  `Intensité de la douleur (échelle 0-10)` (German-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ligaments collatéraux` (German-23)  ⟷  `Ligaments latéraux` (AZYGOS-17) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie du genou` (AZYGOS-17)  ⟷  `Radiographie genou droit` (AMBOSS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Remettre le bandage de la patiente` (AMBOSS-25)  ⟷  `Retrait du bandage de la patiente` (AMBOSS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Stress en valgus` (AZYGOS-17)  ⟷  `Test de stress en valgus` (AMBOSS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Stress en varus` (AZYGOS-17)  ⟷  `Test de stress en varus` (AMBOSS-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test du tiroir postérieur` (AMBOSS-25)  ⟷  `Tiroir postérieur` (AZYGOS-17) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Anamnèse psychosociale` (AZYGOS-17)  ⟷  `Charge psychosociale` (AZYGOS-17) — **AZYGOS-17, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-25, AZYGOS-17)  ⟷  `Antécédents familiaux` (AMBOSS-25, AZYGOS-17) — **AMBOSS-25, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-25, AZYGOS-17)  ⟷  `Antécédents médicaux` (AMBOSS-25, AZYGOS-17) — **AMBOSS-25, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-25, AZYGOS-17)  ⟷  `Antécédents médicaux` (AMBOSS-25, AZYGOS-17) — **AMBOSS-25, section « a »** distingue ces deux items
- ⛔ `Examen ciblé de la sensibilité des membres inférieurs` (AMBOSS-25)  ⟷  `Examen ciblé des mouvements passifs et actifs des membres inférieurs` (AMBOSS-25) — **AMBOSS-25, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-25)  ⟷  `Facteurs améliorants` (AMBOSS-25) — **AMBOSS-25, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-25)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-17) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AMBOSS-25)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-17) — **AZYGOS-17, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (AMBOSS-25)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-17) — **AMBOSS-25, section « a »** distingue ces deux items
- ⛔ `Inspection des membres inférieurs` (AMBOSS-25)  ⟷  `Palpation des membres inférieurs` (AMBOSS-25) — **AMBOSS-25, section « e »** distingue ces deux items
- ⛔ `Palpation des pouls pédieux` (AMBOSS-25)  ⟷  `Palpation du pouls radial` (AMBOSS-25) — **AMBOSS-25, section « e »** distingue ces deux items
- ⛔ `Stress en valgus` (AZYGOS-17)  ⟷  `Stress en varus` (AZYGOS-17) — **AZYGOS-17, section « e »** distingue ces deux items
- ⛔ `Stress varus-valgus en extension complète` (German-23)  ⟷  `Stress varus-valgus en flexion 20-30°` (German-23) — **German-23, section « e »** distingue ces deux items
- ⛔ `Test de stress en valgus` (AMBOSS-25)  ⟷  `Test de stress en varus` (AMBOSS-25) — **AMBOSS-25, section « e »** distingue ces deux items
- ⛔ `Tiroir antérieur` (AZYGOS-17)  ⟷  `Tiroir postérieur` (AZYGOS-17) — **AZYGOS-17, section « e »** distingue ces deux items
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-17)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-17) — **AZYGOS-17, section « a »** distingue ces deux items

## Douleur du Membre Inférieur — 3 cas · 8 à juger (0 de forme, 8 de contenu), 18 ⚠️, 24 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Examens complémentaires` (RESCOS-26)  ⟷  `Examens complémentaires urgents` (RESCOS-29)
- `Auscultation pulmonaire` (RESCOS-29)  ⟷  `Auscultation vasculaire` (RESCOS-26, RESCOS-27)
- `Palpation des pouls périphériques` (RESCOS-26)  ⟷  `Palpation des pouls périphériques - membres inférieurs` (RESCOS-27)
- `Palpation des pouls périphériques` (RESCOS-26)  ⟷  `Palpation des pouls périphériques - membres supérieurs` (RESCOS-27)
- `Symptômes associés` (RESCOS-29)  ⟷  `Symptômes associés et sévérité` (RESCOS-27)
- `Examens complémentaires de première intention` (RESCOS-27)  ⟷  `Examens complémentaires urgents` (RESCOS-29)
- `Recherche de symptômes associés` (RESCOS-26)  ⟷  `Symptômes associés` (RESCOS-29)
- `Inspection des membres inférieurs` (RESCOS-26)  ⟷  `Inspection et palpation membre inférieur gauche` (RESCOS-29)

- ⚠️ `Activité physique` (RESCOS-27)  ⟷  `Activité physique régulière` (RESCOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Artères tibiales postérieures` (RESCOS-26)  ⟷  `Pouls tibial postérieur` (RESCOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractère répétitif` (RESCOS-27)  ⟷  `Caractère répétitif des symptômes` (RESCOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractérisation de la claudication intermittente` (RESCOS-26)  ⟷  `Stade II: Claudication intermittente` (RESCOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contrôle facteurs de risque` (RESCOS-27)  ⟷  `Contrôle facteurs de risque CV` (RESCOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs de repos` (RESCOS-26, RESCOS-27)  ⟷  `Stade III: Douleur de repos` (RESCOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Echo-Doppler artériel membres inférieurs` (RESCOS-26)  ⟷  `Echo-Doppler veineux membres inférieurs` (RESCOS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Echo-Doppler veineux membres inférieurs` (RESCOS-29)  ⟷  `Écho-Doppler artériel membres inférieurs` (RESCOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Embolie pulmonaire associée` (RESCOS-29)  ⟷  `Embolie pulmonaire mère` (RESCOS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (RESCOS-29)  ⟷  `Examens d'imagerie vasculaire` (RESCOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Index de pression systolique cheville-bras (IPS)` (RESCOS-27)  ⟷  `Mesure index pression systolique (IPS)` (RESCOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Mesure de l'index de pression systolique (IPS/ABI)` (RESCOS-26)  ⟷  `Mesure index pression systolique (IPS)` (RESCOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Paresis` (RESCOS-27)  ⟷  `Paresthésies` (RESCOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Paresthesia` (RESCOS-27)  ⟷  `Paresthésies` (RESCOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pâleur des extrémités` (RESCOS-27)  ⟷  `Température des extrémités` (RESCOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Périmètre de marche` (RESCOS-27)  ⟷  `Périmètre de marche 150m` (RESCOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Stade IV: Troubles trophiques` (RESCOS-26)  ⟷  `Troubles trophiques` (RESCOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de marche sur tapis` (RESCOS-26)  ⟷  `Test de marche sur tapis roulant` (RESCOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents familiaux` (RESCOS-26, RESCOS-29)  ⟷  `Antécédents médicaux` (RESCOS-26, RESCOS-29) — **RESCOS-26, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux cardiovasculaires` (RESCOS-27)  ⟷  `Antécédents personnels cardiovasculaires` (RESCOS-27) — **RESCOS-27, section « a »** distingue ces deux items
- ⛔ `Artères fémorales` (RESCOS-26, RESCOS-27)  ⟷  `Artères rénales` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Cancer du sein` (RESCOS-29)  ⟷  `Cancer du sein droit` (RESCOS-29) — **RESCOS-29, section « a »** distingue ces deux items
- ⛔ `Cheville gauche > droite` (RESCOS-29)  ⟷  `Cuisse gauche > droite` (RESCOS-29) — **RESCOS-29, section « e »** distingue ces deux items
- ⛔ `Cheville gauche > droite` (RESCOS-29)  ⟷  `Mollet gauche > droit` (RESCOS-29) — **RESCOS-29, section « e »** distingue ces deux items
- ⛔ `Cuisse gauche > droite` (RESCOS-29)  ⟷  `Mollet gauche > droit` (RESCOS-29) — **RESCOS-29, section « e »** distingue ces deux items
- ⛔ `Echo-Doppler artériel membres inférieurs` (RESCOS-26)  ⟷  `Écho-Doppler artériel membres inférieurs` (RESCOS-27) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteur aggravant` (RESCOS-27)  ⟷  `Facteur soulageant` (RESCOS-27) — **RESCOS-27, section « a »** distingue ces deux items
- ⛔ `Mère` (RESCOS-27)  ⟷  `Père` (RESCOS-27) — **RESCOS-27, section « a »** distingue ces deux items
- ⛔ `Mère décédée à 94 ans` (RESCOS-29)  ⟷  `Père décédé à 78 ans` (RESCOS-29) — **RESCOS-29, section « a »** distingue ces deux items
- ⛔ `Palpation des pouls périphériques - membres inférieurs` (RESCOS-27)  ⟷  `Palpation des pouls périphériques - membres supérieurs` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Palpation pouls brachial` (RESCOS-27)  ⟷  `Pouls brachial` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Paresia (parésie)` (RESCOS-26)  ⟷  `Paresthesia (paresthésies)` (RESCOS-26) — **RESCOS-26, section « a »** distingue ces deux items
- ⛔ `Pouls brachial` (RESCOS-27)  ⟷  `Pouls radial` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Périmètre de marche` (RESCOS-27)  ⟷  `Évolution et périmètre de marche` (RESCOS-27) — **RESCOS-27, section « a »** distingue ces deux items
- ⛔ `Stade 1` (RESCOS-27)  ⟷  `Stade 2` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Stade 1` (RESCOS-27)  ⟷  `Stade 3` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Stade 1` (RESCOS-27)  ⟷  `Stade 4` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Stade 2` (RESCOS-27)  ⟷  `Stade 3` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Stade 2` (RESCOS-27)  ⟷  `Stade 4` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Stade 3` (RESCOS-27)  ⟷  `Stade 4` (RESCOS-27) — **RESCOS-27, section « e »** distingue ces deux items
- ⛔ `Stade IIa: > 200m` (RESCOS-26)  ⟷  `Stade IIb: < 200m` (RESCOS-26) — **RESCOS-26, section « m »** distingue ces deux items
- ⛔ `Tachyarythmie` (RESCOS-29)  ⟷  `Tachycardie` (RESCOS-29) — **RESCOS-29, section « e »** distingue ces deux items

## Douleurs Articulaires — 4 cas · 12 à juger (0 de forme, 12 de contenu), 12 ⚠️, 38 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Localisation de la douleur` (German-22)  ⟷  `Localisation précise de la douleur` (German-25)
- `Examen des mains et poignets` (RESCOS-38)  ⟷  `Examen orienté des mains et des poignets` (AZYGOS-42)
- `Diagnostics différentiels` (German-22)  ⟷  `Diagnostics différentiels (au moins 2)` (German-25)
- `Analyse de la marche` (German-25)  ⟷  `Se lever / Analyse de la marche` (AZYGOS-42)
- `Facteurs aggravants` (AZYGOS-42)  ⟷  `Facteurs aggravants/atténuants` (German-25)
- `Antécédents de traumatisme` (German-22)  ⟷  `Notion de traumatisme` (German-25)
- `Antécédents de traumatisme` (German-22)  ⟷  `Antécédents et terrain` (RESCOS-38)
- `Examen neurologique` (German-22)  ⟷  `Tests neurologiques` (German-25)
- `Diagnostics différentiels` (German-22)  ⟷  `Diagnostics différentiels des polyarthrites` (RESCOS-38)
- `Caractère de la douleur` (German-25)  ⟷  `Localisation de la douleur` (German-22)
- `Polyarthrite rhumatoïde` (AZYGOS-42)  ⟷  `Traitement de la polyarthrite rhumatoïde` (RESCOS-38)
- `Caractère de la douleur` (German-25)  ⟷  `Qualité de la douleur` (German-22)

- ⚠️ `Anti-inflammatoires (antalgiques)` (RESCOS-38)  ⟷  `Anti-inflammatoires locaux` (German-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autre atteinte vasculaire` (AZYGOS-42)  ⟷  `Autres plaintes articulaires` (German-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `DD Hypothyroïdie` (AZYGOS-42)  ⟷  `Hypothyroïdie` (AZYGOS-42) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Horaire inflammatoire` (RESCOS-38)  ⟷  `Myopathie inflammatoire` (AZYGOS-42) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Myopathie inflammatoire` (AZYGOS-42)  ⟷  `Type inflammatoire` (RESCOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments` (AZYGOS-42)  ⟷  `Médicaments actuels` (German-22) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pronation-Neutre-Supination` (German-22)  ⟷  `Pronation/supination` (German-25) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Raideur matinale` (AZYGOS-42)  ⟷  `Raideur matinale importante` (RESCOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Gänslen` (German-25)  ⟷  `Test de Phalen` (RESCOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traitement déjà essayé` (German-22)  ⟷  `Traitement essayé` (RESCOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tuméfaction articulaire` (RESCOS-38)  ⟷  `Tuméfaction des articulations IPP` (RESCOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tuméfaction articulaire` (RESCOS-38)  ⟷  `Tuméfaction des articulations MCP` (RESCOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `1-3 petites articulations: 2 points` (RESCOS-38)  ⟷  `2-10 grandes articulations: 1 point` (RESCOS-38) — **RESCOS-38, section « m »** distingue ces deux items
- ⛔ `1-3 petites articulations: 2 points` (RESCOS-38)  ⟷  `4-10 petites articulations: 3 points` (RESCOS-38) — **RESCOS-38, section « m »** distingue ces deux items
- ⛔ `1-3 petites articulations: 2 points` (RESCOS-38)  ⟷  `>10 articulations: 5 points` (RESCOS-38) — **RESCOS-38, section « m »** distingue ces deux items
- ⛔ `2-10 grandes articulations: 1 point` (RESCOS-38)  ⟷  `4-10 petites articulations: 3 points` (RESCOS-38) — **RESCOS-38, section « m »** distingue ces deux items
- ⛔ `2-10 grandes articulations: 1 point` (RESCOS-38)  ⟷  `>10 articulations: 5 points` (RESCOS-38) — **RESCOS-38, section « m »** distingue ces deux items
- ⛔ `4-10 petites articulations: 3 points` (RESCOS-38)  ⟷  `>10 articulations: 5 points` (RESCOS-38) — **RESCOS-38, section « m »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AZYGOS-42)  ⟷  `Antécédents médicaux` (AZYGOS-42, German-25) — **AZYGOS-42, section « a »** distingue ces deux items
- ⛔ `Arguments contre mentionnés` (AZYGOS-42)  ⟷  `Arguments pour mentionnés` (AZYGOS-42) — **AZYGOS-42, section « m »** distingue ces deux items
- ⛔ `Auscultation des vaisseaux périphériques` (AZYGOS-42)  ⟷  `Palpation des artères périphériques` (AZYGOS-42) — **AZYGOS-42, section « e »** distingue ces deux items
- ⛔ `CK demandée` (AZYGOS-42)  ⟷  `CRP demandée` (AZYGOS-42) — **AZYGOS-42, section « m »** distingue ces deux items
- ⛔ `Douleur à la pression des IPP` (RESCOS-38)  ⟷  `Douleur à la pression des MCP` (RESCOS-38) — **RESCOS-38, section « e »** distingue ces deux items
- ⛔ `FR ou anti-CCP faiblement positifs: 2 points` (RESCOS-38)  ⟷  `FR ou anti-CCP fortement positifs: 3 points` (RESCOS-38) — **RESCOS-38, section « m »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AZYGOS-42)  ⟷  `Facteurs soulageants` (AZYGOS-42) — **AZYGOS-42, section « a »** distingue ces deux items
- ⛔ `Horaire inflammatoire` (RESCOS-38)  ⟷  `Type inflammatoire` (RESCOS-38) — **RESCOS-38, section « a »** distingue ces deux items
- ⛔ `Inspection de la plante du pied en position assise` (German-25)  ⟷  `Inspection globale du pied en position debout` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Localisation de la douleur` (German-22)  ⟷  `Qualité de la douleur` (German-22) — **German-22, section « a »** distingue ces deux items
- ⛔ `Marche sur les orteils` (German-25)  ⟷  `Marche sur les talons` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Mobilité articulaire des mains` (RESCOS-38)  ⟷  `Palpation articulaire des mains` (RESCOS-38) — **RESCOS-38, section « e »** distingue ces deux items
- ⛔ `Myopathie associée aux statines` (AZYGOS-42)  ⟷  `Myopathie aux statines` (AZYGOS-42) — **AZYGOS-42, section « m »** distingue ces deux items
- ⛔ `Pouls tibial postérieur` (German-25)  ⟷  `Tendon du tibial postérieur` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied bot (Klumpfuss)` (German-25)  ⟷  `Recherche de pied creux (Hohlfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied bot (Klumpfuss)` (German-25)  ⟷  `Recherche de pied plat (Senkfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied bot (Klumpfuss)` (German-25)  ⟷  `Recherche de pied valgus (Knickfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied bot (Klumpfuss)` (German-25)  ⟷  `Recherche de pied étalé (Spreizfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied creux (Hohlfuss)` (German-25)  ⟷  `Recherche de pied plat (Senkfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied creux (Hohlfuss)` (German-25)  ⟷  `Recherche de pied valgus (Knickfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied plat (Senkfuss)` (German-25)  ⟷  `Recherche de pied valgus (Knickfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied plat (Senkfuss)` (German-25)  ⟷  `Recherche de pied étalé (Spreizfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Recherche de pied valgus (Knickfuss)` (German-25)  ⟷  `Recherche de pied étalé (Spreizfuss)` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Réflexes : biceps (C5)` (German-22)  ⟷  `Réflexes : triceps (C7)` (German-22) — **German-22, section « e »** distingue ces deux items
- ⛔ `Stress en valgus` (German-22)  ⟷  `Stress en varus` (German-22) — **German-22, section « e »** distingue ces deux items
- ⛔ `Traitement médicamenteux` (German-25)  ⟷  `Traitement non médicamenteux` (German-25) — **German-25, section « m »** distingue ces deux items
- ⛔ `Traumatisme actuel` (German-22)  ⟷  `Traumatisme antérieur` (German-22) — **German-22, section « a »** distingue ces deux items
- ⛔ `Tuméfaction des articulations IPP` (RESCOS-38)  ⟷  `Tuméfaction des articulations MCP` (RESCOS-38) — **RESCOS-38, section « e »** distingue ces deux items
- ⛔ `Épicondyle latéral de l'humérus` (German-22)  ⟷  `Épicondyle médial de l'humérus` (German-22) — **German-22, section « e »** distingue ces deux items
- ⛔ `Évaluation des axes de l'arrière-pied` (German-25)  ⟷  `Évaluation des axes des jambes` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Évaluation des axes de l'arrière-pied` (German-25)  ⟷  `Évaluation des axes du bassin` (German-25) — **German-25, section « e »** distingue ces deux items
- ⛔ `Évaluation des axes des jambes` (German-25)  ⟷  `Évaluation des axes du bassin` (German-25) — **German-25, section « e »** distingue ces deux items

## Dysphagie — 2 cas · 1 à juger (0 de forme, 1 de contenu), 1 ⚠️, 16 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Motif principal` (AMBOSS-22)  ⟷  `Symptôme principal` (German-34)

- ⚠️ `Symptômes associés` (AMBOSS-22)  ⟷  `Symptômes associés ORL` (German-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-22)  ⟷  `Antécédents familiaux` (AMBOSS-22) — **AMBOSS-22, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-22)  ⟷  `Antécédents médicaux` (AMBOSS-22, German-34) — **AMBOSS-22, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-22)  ⟷  `Antécédents médicaux` (AMBOSS-22, German-34) — **AMBOSS-22, section « a »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-22)  ⟷  `Inspection de l'abdomen` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-22)  ⟷  `Palpation de l'abdomen` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-22)  ⟷  `Percussion de l'abdomen` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-22)  ⟷  `Facteurs améliorants` (AMBOSS-22) — **AMBOSS-22, section « a »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-22)  ⟷  `Inspection de l'oropharynx` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-22)  ⟷  `Palpation de l'abdomen` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-22)  ⟷  `Percussion de l'abdomen` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Inspection de l'oropharynx` (AMBOSS-22)  ⟷  `Inspection du thorax` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Inspection du cou` (AMBOSS-22)  ⟷  `Inspection du thorax` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Inspection du thorax` (AMBOSS-22)  ⟷  `Palpation du thorax` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-22)  ⟷  `Percussion de l'abdomen` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Palpation du choc apexien` (AMBOSS-22)  ⟷  `Palpation du thorax` (AMBOSS-22) — **AMBOSS-22, section « e »** distingue ces deux items
- ⛔ `Régurgitation` (AMBOSS-22)  ⟷  `Régurgitations` (German-34) — **même signature socle A**, déjà appariés dans leur section

## Dyspnée — 5 cas · 22 à juger (0 de forme, 22 de contenu), 81 ⚠️, 46 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Symptômes associés - ORL et respiratoires` (German-35)  ⟷  `Symptômes associés respiratoires` (RESCOS-40)
- `Antécédents médicaux personnels` (German-35, German-36)  ⟷  `Antécédents médicaux pertinents` (RESCOS-40)
- `Examens complémentaires - Fonction respiratoire` (German-35, German-36)  ⟷  `Examens complémentaires respiratoires` (RESCOS-40)
- `Examens complémentaires cardiaques` (RESCOS-40)  ⟷  `Examens complémentaires urgents` (RESCOS-39)
- `Prise en charge de l'insuffisance cardiaque` (RESCOS-40)  ⟷  `Traitement de l'insuffisance cardiaque` (RESCOS-39)
- `Inspection générale` (RESCOS-39)  ⟷  `Inspection générale intégrée` (RESCOS-40)
- `Maladies respiratoires` (German-35)  ⟷  `Maladies respiratoires familiales` (German-36)
- `Symptômes associés` (RESCOS-39)  ⟷  `Symptômes associés - Autres` (German-35)
- `Examens complémentaires respiratoires` (RESCOS-40)  ⟷  `Examens complémentaires urgents` (RESCOS-39)
- `Contexte social et environnemental` (German-35)  ⟷  `Contexte social et professionnel` (German-36)
- `Auscultation pulmonaire` (AZYGOS-23, RESCOS-39)  ⟷  `Auscultation pulmonaire systématique` (German-36)
- `Examen cardiaque` (German-35)  ⟷  `Examen cardiovasculaire` (German-36)
- `Traitement aigu proposé` (German-35)  ⟷  `Traitement médicamenteux proposé` (German-36)
- `Symptômes associés - Autres` (German-35)  ⟷  `Symptômes associés cardiovasculaires` (RESCOS-40)
- `Auscultation pulmonaire - bruits pathologiques` (RESCOS-40)  ⟷  `Auscultation pulmonaire systématique` (German-36)
- `Symptômes associés - Autres` (German-35)  ⟷  `Symptômes associés respiratoires` (RESCOS-40)
- `Caractéristiques de l'expectoration` (German-36)  ⟷  `Caractéristiques de la toux` (German-35)
- `Test de réversibilité aux bronchodilatateurs` (German-36)  ⟷  `Test de réversibilité aux bêta-2 mimétiques` (German-35)
- `Traitement actuel` (RESCOS-39)  ⟷  `Traitements et habitudes` (German-35)
- `Diagnostic principal` (German-36)  ⟷  `Synthèse diagnostique principale` (RESCOS-40)
- `Inspection générale` (RESCOS-39)  ⟷  `Inspection générale et pulmonaire` (German-36)
- `Facteurs d'amélioration` (German-36)  ⟷  `Facteurs d'amélioration et d'aggravation` (German-35)

- ⚠️ `Activité physique` (RESCOS-40)  ⟷  `Activité physique adaptée` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Activité physique` (RESCOS-40)  ⟷  `Activités physiques et loisirs` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Activité physique adaptée` (German-36)  ⟷  `Activité physique régulière adaptée` (RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Activités antérieures` (German-36)  ⟷  `Maladies antérieures` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aggravation progressive` (RESCOS-39)  ⟷  `Limitations progressives` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Allergies alimentaires` (German-35)  ⟷  `Allergies médicamenteuses` (German-36, RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Allergies respiratoires` (German-35)  ⟷  `Pathologies respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Allergies respiratoires` (German-35)  ⟷  `Sifflements respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Allergies respiratoires` (German-35)  ⟷  `Éléments respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ampliation thoracique` (German-35, German-36)  ⟷  `Palpation ampliation thoracique` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Amélioration en position assise` (RESCOS-39)  ⟷  `Patient en position semi-assise` (RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (RESCOS-39)  ⟷  `Antécédents familiaux cardiovasculaires` (German-36, RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (RESCOS-39)  ⟷  `Antécédents judiciaires` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (RESCOS-39)  ⟷  `Examen cardiovasculaire` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (RESCOS-39)  ⟷  `Pathologies cardiovasculaires` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Apparition progressive` (RESCOS-39)  ⟷  `Limitations progressives` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation antérieure complète` (German-36)  ⟷  `Auscultation antérieure systématique` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation antérieure complète` (German-36)  ⟷  `Auscultation postérieure systématique` (German-35) — **antonymes présumés** (anterieur / posterieur) : aucune grille ne les porte ensemble, donc la propriété 8 n'a pas de témoin. *(Par ailleurs inerte : la propriété 7 la refuserait.)*
- ⚠️ `Auscultation antérieure systématique` (German-35)  ⟷  `Auscultation pulmonaire systématique` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (AZYGOS-23, German-36, RESCOS-39)  ⟷  `Auscultation cardiaque systématique` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque - bruits pathologiques` (RESCOS-40)  ⟷  `Auscultation cardiaque systématique` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque systématique` (German-35)  ⟷  `Auscultation pulmonaire systématique` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation postérieure complète` (German-36)  ⟷  `Auscultation postérieure systématique` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation postérieure systématique` (German-35)  ⟷  `Auscultation pulmonaire systématique` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bruits respiratoires` (German-35)  ⟷  `Sifflements respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bruits respiratoires` (German-35)  ⟷  `Éléments respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contexte psychosocial` (RESCOS-40)  ⟷  `Support psychosocial` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Critères diagnostiques d'insuffisance cardiaque` (RESCOS-39)  ⟷  `Signes périphériques d'insuffisance cardiaque` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cyanose des extrémités` (German-36)  ⟷  `Cyanose légère des extrémités` (RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cyanose des extrémités` (German-36)  ⟷  `Examen des extrémités` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diminution du murmure vésiculaire` (RESCOS-39)  ⟷  `Murmure vésiculaire` (German-36, RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs thoraciques` (AZYGOS-23, German-35, RESCOS-40)  ⟷  `Déformations thoraciques` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Déformations thoraciques` (German-35)  ⟷  `Palpation thoracique` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiaque` (German-35)  ⟷  `Éléments cardiaques` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen des extrémités` (German-35)  ⟷  `Température des extrémités` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen des membres inférieurs` (RESCOS-39)  ⟷  `Œdèmes des membres inférieurs` (German-36, RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen des membres inférieurs` (RESCOS-39)  ⟷  `Œdèmes membres inférieurs` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Expiration prolongée` (RESCOS-40)  ⟷  `Immobilisation prolongée` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs de risque identifiés` (German-36)  ⟷  `Facteurs déclenchants identifiés` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs déclenchants et aggravants` (German-36)  ⟷  `Facteurs déclenchants identifiés` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Frottement péricardique` (RESCOS-40)  ⟷  `Pas de frottement péricardique` (RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence respiratoire` (German-36, RESCOS-40)  ⟷  `Éléments respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Galop B3` (RESCOS-39)  ⟷  `Galop B3 ou B4` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hippocratisme digital` (German-36)  ⟷  `Recherche d'hippocratisme digital` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisations` (German-35, German-36)  ⟷  `Hospitalisations antérieures` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-36, RESCOS-39, RESCOS-40)  ⟷  `Pression artérielle` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Importance de l'observance thérapeutique` (RESCOS-39)  ⟷  `Observance thérapeutique` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections ORL récentes` (German-35)  ⟷  `Infections respiratoires récurrentes` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du thorax` (AZYGOS-23)  ⟷  `Inspection forme thorax` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection mouvements respiratoires` (RESCOS-40)  ⟷  `Symétrie des mouvements respiratoires` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies respiratoires` (German-35)  ⟷  `Pathologies respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies respiratoires` (German-35)  ⟷  `Sifflements respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies respiratoires` (German-35)  ⟷  `Éléments respiratoires` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Management intégré cardio-respiratoire` (RESCOS-40)  ⟷  `Technique d'examen intégré cardio-respiratoire` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Morphologie thoracique` (German-36)  ⟷  `Radiographie thoracique` (German-35, German-36, RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Observance thérapeutique` (German-36)  ⟷  `Observance thérapeutique potentielle` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation` (AZYGOS-23)  ⟷  `Palpitations` (AZYGOS-23, RESCOS-39, RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation ampliation thoracique` (RESCOS-40)  ⟷  `Palpation thoracique` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du choc de pointe` (German-35)  ⟷  `Palpation précordiale et choc de pointe` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation vibrations vocales` (RESCOS-40)  ⟷  `Vibrations vocales` (AZYGOS-23, German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Plan d'action en cas d'exacerbation` (German-36)  ⟷  `Plan d'action en cas de crise` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pouls périphériques` (German-36, RESCOS-40)  ⟷  `Pouls périphériques présents` (RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Prise de poids` (RESCOS-39)  ⟷  `Prise de poids récente` (German-36, RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (German-35)  ⟷  `Progression` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie du thorax AP au lit` (AZYGOS-23)  ⟷  `Radiographie thorax` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie thoracique` (German-35, German-36, RESCOS-39)  ⟷  `Radiographie thorax` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Râles crépitants` (RESCOS-39, RESCOS-40)  ⟷  `Râles crépitants bilatéraux` (RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réévaluation` (AZYGOS-23)  ⟷  `Évolution` (AZYGOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Scanner thoracique si indication` (RESCOS-40)  ⟷  `Scanner thoracique si indiqué` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes périphériques d'insuffisance cardiaque` (RESCOS-40)  ⟷  `Symptômes d'insuffisance cardiaque` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Souffle systolique d'insuffisance mitrale` (RESCOS-39)  ⟷  `Souffle systolique mitral` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Spirométrie` (RESCOS-40)  ⟷  `Spirométrie de base` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Symptômes d'insuffisance cardiaque` (German-36)  ⟷  `Traitement de l'insuffisance cardiaque` (RESCOS-39) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tabagisme` (German-35, RESCOS-39, RESCOS-40)  ⟷  `Tabagisme actif` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traitement actuel` (RESCOS-39)  ⟷  `Traitement diurétique` (AZYGOS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Utilisation des muscles accessoires` (German-35)  ⟷  `Évaluation des muscles respiratoires accessoires` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccination antigrippale et antipneumococcique` (German-36)  ⟷  `Vaccination grippe/pneumocoque` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vibrations vocales` (AZYGOS-23, German-36)  ⟷  `Vibrations vocales (frémitus)` (German-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vol long récent` (German-35)  ⟷  `Évolution récente` (German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évolution pondérale` (German-35)  ⟷  `Évolution temporelle` (RESCOS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évolution temporelle` (RESCOS-40)  ⟷  `Évolution temporelle des symptômes` (German-35, German-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Activités antérieures` (German-36)  ⟷  `Chirurgies antérieures` (German-36) — **German-36, section « a »** distingue ces deux items
- ⛔ `Adénopathies sus-claviculaires` (German-35)  ⟷  `Ganglions sus-claviculaires` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Aggravation progressive` (RESCOS-39)  ⟷  `Apparition progressive` (RESCOS-39) — **RESCOS-39, section « a »** distingue ces deux items
- ⛔ `Ajustement thérapeutique` (German-35)  ⟷  `Éducation thérapeutique` (German-35, German-36, RESCOS-39, RESCOS-40) — **German-35, section « m »** distingue ces deux items
- ⛔ `Allergies détaillées` (German-35)  ⟷  `Allergies familiales` (German-35, German-36) — **German-35, section « a »** distingue ces deux items
- ⛔ `Allergies respiratoires` (German-35)  ⟷  `Bruits respiratoires` (German-35) — **German-35, section « a »** distingue ces deux items
- ⛔ `Allergies respiratoires` (German-35)  ⟷  `Maladies respiratoires` (German-35) — **German-35, section « a »** distingue ces deux items
- ⛔ `Ampliation thoracique` (German-35, German-36)  ⟷  `Déformations thoraciques` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Ampliation thoracique` (German-35, German-36)  ⟷  `Palpation thoracique` (German-36) — **German-36, section « e »** distingue ces deux items
- ⛔ `Anticholinergique de courte durée d'action (SAMA)` (German-36)  ⟷  `Bêta-2 agoniste de courte durée d'action (SABA)` (German-36) — **German-36, section « m »** distingue ces deux items
- ⛔ `Auscultation antérieure complète` (German-36)  ⟷  `Auscultation postérieure complète` (German-36) — **German-36, section « e »** distingue ces deux items
- ⛔ `Auscultation antérieure systématique` (German-35)  ⟷  `Auscultation cardiaque systématique` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Auscultation antérieure systématique` (German-35)  ⟷  `Auscultation postérieure systématique` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiaque - bruits pathologiques` (RESCOS-40)  ⟷  `Auscultation pulmonaire - bruits pathologiques` (RESCOS-40) — **RESCOS-40, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiaque systématique` (German-35)  ⟷  `Auscultation postérieure systématique` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Bruits respiratoires` (German-35)  ⟷  `Maladies respiratoires` (German-35) — **German-35, section « a »** distingue ces deux items
- ⛔ `Classe I: Pas de limitation` (RESCOS-39)  ⟷  `Classe II: Limitation légère` (RESCOS-39) — **RESCOS-39, section « a »** distingue ces deux items
- ⛔ `Classe II: Limitation légère` (RESCOS-39)  ⟷  `Classe III: Limitation marquée` (RESCOS-39) — **RESCOS-39, section « a »** distingue ces deux items
- ⛔ `Critères diagnostiques d'insuffisance cardiaque` (RESCOS-39)  ⟷  `Traitement de l'insuffisance cardiaque` (RESCOS-39) — **RESCOS-39, section « m »** distingue ces deux items
- ⛔ `Effort physique` (German-36)  ⟷  `Performance physique` (German-35, German-36) — **German-36, section « a »** distingue ces deux items
- ⛔ `Examen pulmonaire - Inspection` (German-35)  ⟷  `Examen pulmonaire - Palpation` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Examen pulmonaire - Inspection` (German-35)  ⟷  `Examen pulmonaire - Percussion` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Examen pulmonaire - Palpation` (German-35)  ⟷  `Examen pulmonaire - Percussion` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Examens complémentaires cardiaques` (RESCOS-40)  ⟷  `Examens complémentaires respiratoires` (RESCOS-40) — **RESCOS-40, section « m »** distingue ces deux items
- ⛔ `Expectoration` (AZYGOS-23)  ⟷  `Expectoration purulente` (AZYGOS-23) — **AZYGOS-23, section « a »** distingue ces deux items
- ⛔ `Expectoration` (AZYGOS-23)  ⟷  `Expectorations` (RESCOS-40) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Exposition professionnelle` (German-35)  ⟷  `Expositions professionnelles` (RESCOS-40) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Exposition professionnelle` (German-35)  ⟷  `Situation professionnelle` (RESCOS-40) — **RESCOS-40, section « a »** distingue ces deux items
- ⛔ `Expositions professionnelles` (RESCOS-40)  ⟷  `Situation professionnelle` (RESCOS-40) — **RESCOS-40, section « a »** distingue ces deux items
- ⛔ `Facteurs d'amélioration` (German-36)  ⟷  `Périodes d'amélioration` (German-36) — **German-36, section « a »** distingue ces deux items
- ⛔ `Galop (B3)` (RESCOS-39)  ⟷  `Galop B3` (RESCOS-39) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Ganglions axillaires` (German-35)  ⟷  `Ganglions sous-mandibulaires` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Ganglions axillaires` (German-35)  ⟷  `Ganglions sus-claviculaires` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Ganglions sous-mandibulaires` (German-35)  ⟷  `Ganglions sus-claviculaires` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Inspection du thorax` (AZYGOS-23)  ⟷  `Percussion du thorax` (AZYGOS-23) — **AZYGOS-23, section « e »** distingue ces deux items
- ⛔ `Médicaments actuels` (German-35, German-36, RESCOS-40)  ⟷  `Médicaments éventuels` (German-36) — **German-36, section « a »** distingue ces deux items
- ⛔ `Radiographie thoracique` (German-35, German-36, RESCOS-39)  ⟷  `Échocardiographie transthoracique` (RESCOS-39) — **RESCOS-39, section « m »** distingue ces deux items
- ⛔ `Recherche de cyanose` (German-35)  ⟷  `Recherche de souffles` (German-35) — **German-35, section « e »** distingue ces deux items
- ⛔ `Sifflements respiratoires` (RESCOS-40)  ⟷  `Éléments respiratoires` (RESCOS-40) — **RESCOS-40, section « a »** distingue ces deux items
- ⛔ `Souffle systolique aortique` (RESCOS-40)  ⟷  `Souffle systolique mitral` (RESCOS-40) — **RESCOS-40, section « e »** distingue ces deux items
- ⛔ `Symptômes associés - Autres` (German-35)  ⟷  `Symptômes associés - ORL et respiratoires` (German-35) — **German-35, section « a »** distingue ces deux items
- ⛔ `Symptômes associés - Autres` (German-35)  ⟷  `Symptômes associés - État général` (German-35) — **German-35, section « a »** distingue ces deux items
- ⛔ `Symptômes associés cardiovasculaires` (RESCOS-40)  ⟷  `Symptômes associés respiratoires` (RESCOS-40) — **RESCOS-40, section « a »** distingue ces deux items
- ⛔ `Tabagisme actif` (German-36)  ⟷  `Tabagisme passif` (German-36) — **German-36, section « a »** distingue ces deux items
- ⛔ `Test de marche 6 minutes` (RESCOS-40)  ⟷  `Test de marche de 6 minutes` (German-36) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Œdèmes des membres inférieurs` (German-36, RESCOS-39)  ⟷  `Œdèmes membres inférieurs` (RESCOS-40) — **même signature socle A**, déjà appariés dans leur section

## Dysurie — 4 cas · 10 à juger (0 de forme, 10 de contenu), 17 ⚠️, 15 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Anamnèse gynécologique` (RESCOS-41)  ⟷  `Anamnèse urologique` (RESCOS-42)
- `Diagnostics différentiels` (German-37)  ⟷  `Évoque les diagnostics différentiels` (RESCOS-42)
- `Hypothèse diagnostique` (AZYGOS-8)  ⟷  `Hypothèse diagnostique principale` (RESCOS-41)
- `Utilisation du préservatif` (RESCOS-41)  ⟷  `Utilisation systématique du préservatif` (German-37)
- `Anamnèse génitale` (RESCOS-42)  ⟷  `Anamnèse sociale` (German-37)
- `Examens complémentaires` (RESCOS-41)  ⟷  `Examens diagnostiques complémentaires` (AZYGOS-8)
- `Caractérisation de la douleur mictionnelle` (RESCOS-42)  ⟷  `Caractérisation de la dysurie` (German-37)
- `Anamnèse sexuelle` (RESCOS-41, RESCOS-42)  ⟷  `Anamnèse sociale` (German-37)
- `Examens diagnostiques` (German-37)  ⟷  `Examens diagnostiques complémentaires` (AZYGOS-8)
- `Antécédents chirurgicaux` (AZYGOS-8)  ⟷  `Antécédents urologiques` (German-37)

- ⚠️ `+ Azithromycine 1g PO dose unique (Chlamydia)` (German-37)  ⟷  `Azithromycine 1g dose unique` (RESCOS-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Analyse d'urine` (AZYGOS-8, RESCOS-41)  ⟷  `Analyse d'urine/ECBU` (RESCOS-42) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Consistance de la prostate` (German-37)  ⟷  `Consistance et surface de la prostate` (AZYGOS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Consistance de la prostate` (German-37)  ⟷  `Taille de la prostate` (AZYGOS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dates des dernières règles` (RESCOS-42)  ⟷  `Dernières règles` (RESCOS-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur prostatique` (German-37)  ⟷  `Douleurs hypogastriques` (German-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur à la palpation` (AZYGOS-8)  ⟷  `Douleurs à la miction` (RESCOS-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs mictionnelles` (German-37)  ⟷  `Douleurs à la miction` (RESCOS-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants ET soulageants` (RESCOS-42)  ⟷  `Facteurs soulageants` (AZYGOS-8) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence et volume mictionnel` (German-37)  ⟷  `Fréquence mictionnelle` (RESCOS-42) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Indication` (AZYGOS-8)  ⟷  `Irradiation` (RESCOS-42) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments` (RESCOS-42)  ⟷  `Médicaments actuels` (German-37, RESCOS-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation bilatérale` (German-37)  ⟷  `Palpation bimanuelle` (RESCOS-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation bimanuelle` (RESCOS-41)  ⟷  `Palpation vésicale` (German-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation vésicale` (German-37)  ⟷  `Simulation - palpation vésicale` (RESCOS-42) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Prise de sang` (AZYGOS-8)  ⟷  `Présence de sang` (German-37, RESCOS-42) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traitement du partenaire` (RESCOS-41)  ⟷  `Traitement empirique des partenaires` (German-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AZYGOS-8)  ⟷  `Antécédents familiaux` (AZYGOS-8) — **AZYGOS-8, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AZYGOS-8)  ⟷  `Antécédents médicaux` (AZYGOS-8, German-37) — **AZYGOS-8, section « a »** distingue ces deux items
- ⛔ `Antécédents d'IST` (RESCOS-41, RESCOS-42)  ⟷  `Antécédents médicaux` (AZYGOS-8, German-37) — **RESCOS-42, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AZYGOS-8)  ⟷  `Antécédents médicaux` (AZYGOS-8, German-37) — **AZYGOS-8, section « a »** distingue ces deux items
- ⛔ `Douleurs associées` (German-37)  ⟷  `Douleurs lombaires` (German-37, RESCOS-41) — **German-37, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AZYGOS-8)  ⟷  `Facteurs soulageants` (AZYGOS-8) — **AZYGOS-8, section « a »** distingue ces deux items
- ⛔ `Importance du traitement du partenaire` (RESCOS-41)  ⟷  `Traitement du partenaire` (RESCOS-41) — **RESCOS-41, section « m »** distingue ces deux items
- ⛔ `Introduction correcte du spéculum` (RESCOS-41)  ⟷  `Retrait correct du spéculum` (RESCOS-41) — **RESCOS-41, section « e »** distingue ces deux items
- ⛔ `Mobilisation du col` (RESCOS-41)  ⟷  `Visualisation du col` (RESCOS-41) — **RESCOS-41, section « e »** distingue ces deux items
- ⛔ `Organes génitaux externes` (AZYGOS-8)  ⟷  `Organes génitaux externes / Périnée` (AZYGOS-8) — **AZYGOS-8, section « e »** distingue ces deux items
- ⛔ `Palpation abdominale` (German-37, RESCOS-41)  ⟷  `Palpation du foie` (RESCOS-41) — **RESCOS-41, section « e »** distingue ces deux items
- ⛔ `Palpation abdominale` (German-37, RESCOS-41)  ⟷  `Palpation vésicale` (German-37) — **German-37, section « e »** distingue ces deux items
- ⛔ `Palpation bilatérale` (German-37)  ⟷  `Palpation vésicale` (German-37) — **German-37, section « e »** distingue ces deux items
- ⛔ `Palpation testiculaire` (German-37)  ⟷  `Palpation vésicale` (German-37) — **German-37, section « e »** distingue ces deux items
- ⛔ `Pertes vaginales` (RESCOS-42)  ⟷  `Prurit vaginal` (RESCOS-42) — **RESCOS-42, section « a »** distingue ces deux items

## Décision Partagée — 2 cas · 2 à juger (0 de forme, 2 de contenu), 8 ⚠️, 1 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Présentation des options (Option Talk)` (RESCOS-59)  ⟷  `Présentation des options thérapeutiques (Option Talk)` (RESCOS-60)
- `Explorer les préférences pour chaque option (Decision Talk)` (RESCOS-60)  ⟷  `Explorer valeurs et préférences (Decision Talk)` (RESCOS-59)

- ⚠️ `Assurer la réversibilité du choix` (RESCOS-60)  ⟷  `Réversibilité des choix` (RESCOS-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Calculateurs de risque cardiovasculaire` (RESCOS-59)  ⟷  `Facteurs de risque cardiovasculaire` (RESCOS-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Effets sur qualité de vie` (RESCOS-59)  ⟷  `Focus sur qualité de vie` (RESCOS-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Effets sur qualité de vie` (RESCOS-59)  ⟷  `Impact sur la qualité de vie` (RESCOS-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fiches d'information patient` (RESCOS-59)  ⟷  `Sources d'information du patient` (RESCOS-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Focus sur qualité de vie` (RESCOS-60)  ⟷  `Impact sur la qualité de vie` (RESCOS-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Option 2: Traitement par statine` (RESCOS-59)  ⟷  `Option 3: Traitement symptomatique seul` (RESCOS-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Valider le choix de la patiente` (RESCOS-60)  ⟷  `Valider les émotions de la patiente` (RESCOS-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Option 2: Sonde naso-gastrique` (RESCOS-60)  ⟷  `Option 2: Sonde naso-gastrique à demeure` (RESCOS-60) — **RESCOS-60, section « e »** distingue ces deux items

## Dépendance & Addictions (Alcool, Tabac, Drogues) — 2 cas · 3 à juger (0 de forme, 3 de contenu), 3 ⚠️, 7 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Tentatives de sevrage antérieures` (German-1)  ⟷  `Traitements de sevrage antérieurs` (AZYGOS-7)
- `Circonstances de la consommation` (AZYGOS-7)  ⟷  `Contexte de consommation` (German-1)
- `Contexte de consommation` (German-1)  ⟷  `Schéma de consommation` (AZYGOS-7)

- ⚠️ `Horaires de consommation` (German-1)  ⟷  `Schéma de consommation` (AZYGOS-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments` (AZYGOS-7)  ⟷  `Médicaments actuels` (German-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Symptômes de sevrage` (AZYGOS-7)  ⟷  `Syndrome de sevrage` (German-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Auscultation cardiaque` (German-1)  ⟷  `Auscultation cardiopulmonaire` (German-1) — **German-1, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiopulmonaire` (German-1)  ⟷  `Auscultation pulmonaire` (German-1) — **German-1, section « e »** distingue ces deux items
- ⛔ `Contexte de consommation` (German-1)  ⟷  `Horaires de consommation` (German-1) — **German-1, section « a »** distingue ces deux items
- ⛔ `L'étudiant énonce le diagnostic principal` (German-1)  ⟷  `L'étudiant évoque les diagnostics différentiels` (German-1) — **German-1, section « m »** distingue ces deux items
- ⛔ `Perte de contrôle` (AZYGOS-7, German-1)  ⟷  `Perte de contrôle / Craving` (AZYGOS-7) — **AZYGOS-7, section « a »** distingue ces deux items
- ⛔ `Recherche d'érythroplasie` (German-1)  ⟷  `Recherche de leucoplasie` (German-1) — **German-1, section « e »** distingue ces deux items
- ⛔ `Recherche de signes d'insuffisance cardiaque` (German-1)  ⟷  `Recherche de signes d'intoxication chronique` (German-1) — **German-1, section « e »** distingue ces deux items

## Entorse de Cheville — 2 cas · 0 à juger (0 de forme, 0 de contenu), 2 ⚠️, 5 ⛔

- ⚠️ `Douleurs articulaires` (AMBOSS-38)  ⟷  `Douleurs au repos` (AZYGOS-12) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de la cheville` (AZYGOS-12)  ⟷  `Palpation des pieds et chevilles` (AMBOSS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-38)  ⟷  `Antécédents familiaux` (AMBOSS-38, AZYGOS-12) — **AMBOSS-38, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-38)  ⟷  `Antécédents médicaux` (AMBOSS-38) — **AMBOSS-38, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-38, AZYGOS-12)  ⟷  `Antécédents médicaux` (AMBOSS-38) — **AMBOSS-38, section « a »** distingue ces deux items
- ⛔ `Examen ciblé de la sensibilité des membres inférieurs` (AMBOSS-38)  ⟷  `Examen ciblé des mouvements passifs et actifs des membres inférieurs` (AMBOSS-38) — **AMBOSS-38, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-38)  ⟷  `Facteurs améliorants` (AMBOSS-38) — **AMBOSS-38, section « a »** distingue ces deux items

## Entretien Motivationnel — 2 cas · 0 à juger (0 de forme, 0 de contenu), 6 ⚠️, 5 ⛔

- ⚠️ `"Qu'est-ce qui vous dérange dans le tabagisme?"` (German-38)  ⟷  `Qu'est-ce qui vous préoccupe dans votre tabagisme?` (RESCOS-43) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exploration des barrières à l'arrêt` (German-38)  ⟷  `Exploration des craintes liées à l'arrêt` (German-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exploration des tentatives d'arrêt antérieures` (German-38)  ⟷  `Tentatives d'arrêt antérieures` (RESCOS-43) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Laisser la porte ouverte` (RESCOS-43)  ⟷  `Maintien de la porte ouverte` (German-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Niveau de motivation actuel` (RESCOS-43)  ⟷  `Niveau de motivation sur échelle 1-10` (German-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Respecter l'autonomie du patient` (RESCOS-43)  ⟷  `Respecter le timing du patient` (RESCOS-43) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `"Qu'est-ce qui vous dérange dans le tabagisme?"` (German-38)  ⟷  `"Qu'est-ce qui vous plaît dans le fait de fumer?"` (German-38) — **German-38, section « m »** distingue ces deux items
- ⛔ `Durée du tabagisme` (German-38, RESCOS-43)  ⟷  `Début du tabagisme` (German-38) — **German-38, section « a »** distingue ces deux items
- ⛔ `Recherche de souffles` (German-38)  ⟷  `Recherche de varices` (German-38) — **German-38, section « e »** distingue ces deux items
- ⛔ `Reflet complexe` (RESCOS-43)  ⟷  `Reflet simple` (RESCOS-43) — **RESCOS-43, section « e »** distingue ces deux items
- ⛔ `Stratégies comportementales proposées` (German-38)  ⟷  `Thérapies comportementales` (German-38) — **German-38, section « m »** distingue ces deux items

## Fatigue — 11 cas · 29 à juger (1 de forme, 28 de contenu), 68 ⚠️, 34 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Communication avec la patiente` (AMBOSS-27, AMBOSS-29)  ⟷  `Communication avec le patient` (AMBOSS-36)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Symptômes B associés` (RESCOS-67, RESCOS-67b)  ⟷  `Symptômes associés` (AMBOSS-27, AMBOSS-29, AMBOSS-36, AZYGOS-30, German-45)
- `Examens complémentaires biologiques` (AMBOSS-29)  ⟷  `Examens complémentaires hématologiques` (AMBOSS-27)
- `Palpation de la glande thyroïde` (RESCOS-67, RESCOS-67b)  ⟷  `Palpation de la thyroïde` (RESCOS-44)
- `Auscultation cardiopulmonaire` (AZYGOS-30)  ⟷  `Auscultation cardiovasculaire` (German-46)
- `Recherche de symptômes spécifiques` (AMBOSS-29)  ⟷  `Recherche de symptômes spécifiques post-partum` (AMBOSS-27)
- `Examens complémentaires différés` (AMBOSS-36)  ⟷  `Examens complémentaires proposés` (German-45, German-46, German-47)
- `Autres symptômes associés` (RESCOS-67, RESCOS-67b)  ⟷  `Symptômes associés` (AMBOSS-27, AMBOSS-29, AMBOSS-36, AZYGOS-30, German-45)
- `Inspection` (AZYGOS-30)  ⟷  `Inspection ORL` (German-45)
- `Examens complémentaires proposés` (German-45, German-46, German-47)  ⟷  `Examens complémentaires urgents` (AMBOSS-36)
- `Examens complémentaires biologiques` (AMBOSS-29)  ⟷  `Examens complémentaires urgents` (AMBOSS-36)
- `Examen cardio-pulmonaire` (German-45)  ⟷  `Examen cardiovasculaire` (AMBOSS-27)
- `Examen neurologique` (AMBOSS-27, AMBOSS-29, German-46)  ⟷  `Examen neurologique sommaire` (German-45, German-47)
- `Examen des extrémités` (AMBOSS-36)  ⟷  `Examen des extrémités et cutané` (AMBOSS-27, AMBOSS-29)
- `Examens complémentaires biologiques` (AMBOSS-29)  ⟷  `Examens complémentaires proposés` (German-45, German-46, German-47)
- `Habitudes alimentaires et consommation` (German-45)  ⟷  `Habitudes alimentaires et nutritionnelles` (German-46)
- `Examens complémentaires biologiques` (AMBOSS-29)  ⟷  `Examens complémentaires différés` (AMBOSS-36)
- `Anamnèse sociale` (AZYGOS-30, German-46)  ⟷  `Anamnèse uro-génitale` (RESCOS-44)
- `Examens complémentaires hématologiques` (AMBOSS-27)  ⟷  `Examens complémentaires urgents` (AMBOSS-36)
- `Examens complémentaires différés` (AMBOSS-36)  ⟷  `Examens complémentaires hématologiques` (AMBOSS-27)
- `Examens complémentaires hématologiques` (AMBOSS-27)  ⟷  `Examens complémentaires proposés` (German-45, German-46, German-47)
- `Évolution temporelle` (AMBOSS-27, AMBOSS-29, German-45)  ⟷  `Évolution temporelle des symptômes` (German-47)
- `Examen ciblé des réflexes ostéo-tendineux` (AMBOSS-27, AMBOSS-29)  ⟷  `Réflexes ostéo-tendineux` (German-46)
- `Anamnèse psychiatrique` (RESCOS-67, RESCOS-67b)  ⟷  `Anamnèse sociale` (AZYGOS-30, German-46)
- `Antécédents familiaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36, German-45, German-46)  ⟷  `Antécédents familiaux psychiatriques` (German-47)
- `Examens complémentaires de première intention` (AMBOSS-27, AMBOSS-29)  ⟷  `Examens complémentaires urgents` (AMBOSS-36)
- `Inspection des conjonctives` (AMBOSS-27, AMBOSS-29)  ⟷  `Inspection des sclères` (AMBOSS-36)
- `Auscultation cardiovasculaire` (German-46)  ⟷  `Examen cardiovasculaire` (AMBOSS-27)
- `Réaction appropriée au défi sur l'expérience du médecin` (AMBOSS-29)  ⟷  `Réaction appropriée au défi sur la maternité` (AMBOSS-27)

- ⚠️ `Activité physique` (RESCOS-67, RESCOS-67b)  ⟷  `Activité physique régulière` (German-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Allaitement` (AMBOSS-27)  ⟷  `Traitement` (RESCOS-67, RESCOS-67b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents familiaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36, German-45, German-46)  ⟷  `Antécédents familiaux de suicide` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents opératoires` (AZYGOS-30)  ⟷  `Antécédents prénataux` (AMBOSS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (AMBOSS-27)  ⟷  `Auscultation cardiopulmonaire` (AZYGOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (AMBOSS-27)  ⟷  `Auscultation cardiovasculaire` (German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (AMBOSS-27)  ⟷  `Auscultation de la carotide` (RESCOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (AMBOSS-27)  ⟷  `Status cardiaque` (RESCOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation de l'abdomen` (AMBOSS-36)  ⟷  `Auscultation de la carotide` (RESCOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation de la carotide` (RESCOS-44)  ⟷  `Palpation de la rate` (AMBOSS-29, AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Capacité de concentration` (German-45)  ⟷  `Difficultés de concentration` (AMBOSS-27, AMBOSS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Changements de poids` (AMBOSS-36)  ⟷  `Changements de voix` (AMBOSS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `DD fatigue` (AZYGOS-30)  ⟷  `Fatigue` (German-46, German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Difficultés de concentration` (AMBOSS-27, AMBOSS-29)  ⟷  `Troubles de concentration` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleur abdominale` (AMBOSS-36)  ⟷  `US abdominal` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs abdominales` (AZYGOS-30, RESCOS-44, RESCOS-67, RESCOS-67b)  ⟷  `US abdominal` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs articulaires` (AMBOSS-36)  ⟷  `Douleurs musculaires ou articulaires` (RESCOS-67, RESCOS-67b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Durée du sommeil` (RESCOS-44)  ⟷  `Troubles du sommeil` (AMBOSS-27, AMBOSS-29, German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Désinfection des mains` (RESCOS-45)  ⟷  `Inspection des mains` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Envies suicidaires` (RESCOS-44)  ⟷  `Idées suicidaires` (AMBOSS-27, AMBOSS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (AMBOSS-27)  ⟷  `Symptômes cardiovasculaires` (German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen de la glande thyroïde` (AMBOSS-27, AMBOSS-29)  ⟷  `Palpation de la glande thyroïde` (RESCOS-67, RESCOS-67b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Explications au patient des impressions diagnostiques préliminaires` (AMBOSS-36)  ⟷  `Explications à la patiente des impressions diagnostiques préliminaires` (AMBOSS-27, AMBOSS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition professionnelle` (German-46)  ⟷  `Situation professionnelle` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `FSC et frottis sanguin` (AMBOSS-29)  ⟷  `Frottis sanguin` (AMBOSS-27, German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ferritine` (AZYGOS-30, RESCOS-67, RESCOS-67b)  ⟷  `Ferritine basse` (German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-45)  ⟷  `Mesure de la tension artérielle` (German-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-45)  ⟷  `Tension artérielle` (German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypothyroïdie` (RESCOS-44)  ⟷  `Hypothyroïdie primaire` (RESCOS-67b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypothyroïdie` (RESCOS-44)  ⟷  `Thyroïde` (AZYGOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Idées suicidaires` (AMBOSS-27, AMBOSS-29)  ⟷  `Idées suicidaires actives` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infection récente` (German-46)  ⟷  `Infections récurrentes` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections récentes` (AMBOSS-27)  ⟷  `Infections récurrentes` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection` (AZYGOS-30)  ⟷  `Inspection du cou` (AMBOSS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection ORL` (German-45)  ⟷  `Inspection du cou` (AMBOSS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection ORL` (German-45)  ⟷  `Inspection du thorax` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'abdomen` (AMBOSS-36)  ⟷  `Inspection de l'oropharynx` (AMBOSS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'abdomen` (AMBOSS-36)  ⟷  `Inspection de la pâleur` (German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'abdomen` (AMBOSS-36)  ⟷  `Inspection de la tête` (AMBOSS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'oropharynx` (AMBOSS-29)  ⟷  `Inspection du thorax` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de la pâleur` (German-46)  ⟷  `Inspection de la tête` (AMBOSS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de la tête` (AMBOSS-27)  ⟷  `Inspection des mains` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de la tête` (AMBOSS-27)  ⟷  `Inspection des sclères` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des conjonctives` (AMBOSS-27, AMBOSS-29)  ⟷  `Inspection des mains` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du cou` (AMBOSS-29)  ⟷  `Inspection du thorax` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Intolérance au froid` (AMBOSS-29, RESCOS-67, RESCOS-67b)  ⟷  `Transpiration/intolérance au froid` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Mesure de la tension artérielle` (German-45)  ⟷  `Tension artérielle` (German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Orientation hospitalière` (AZYGOS-30)  ⟷  `Orientation temporo-spatiale` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation` (AZYGOS-30)  ⟷  `Palpitations` (AMBOSS-27, AMBOSS-29, German-46, German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation abdominale` (AZYGOS-30, German-46)  ⟷  `Palpation de l'abdomen` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation abdominale` (AZYGOS-30, German-46)  ⟷  `Palpation du foie` (AMBOSS-29, AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de l'abdomen` (AMBOSS-36)  ⟷  `Palpation de la thyroïde` (RESCOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de la rate` (AMBOSS-29, AMBOSS-36)  ⟷  `Palpation de la thyroïde` (RESCOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation de la rate` (AMBOSS-29, AMBOSS-36)  ⟷  `Palpation des 4 quadrants` (RESCOS-67b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du choc de pointe` (RESCOS-44)  ⟷  `Palpation du foie` (AMBOSS-29, AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perte de poids` (German-47, RESCOS-44)  ⟷  `Perte/prise de poids` (German-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Problèmes intestinaux` (AMBOSS-27, AMBOSS-29)  ⟷  `Troubles gastro-intestinaux` (German-46, German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Qualité` (RESCOS-67, RESCOS-67b)  ⟷  `Quantité` (RESCOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche des préoccupations et questions de la patiente` (AMBOSS-27, AMBOSS-29)  ⟷  `Recherche des préoccupations et questions du patient` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sensibilité profonde` (German-46)  ⟷  `Troubles de la sensibilité profonde` (German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Situation professionnelle` (German-47)  ⟷  `Situation professionnelle/études` (German-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Souffle cardiaque` (German-46)  ⟷  `Status cardiaque` (RESCOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles de la marche` (German-46)  ⟷  `Troubles de la pensée` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Épisodes antérieurs` (AMBOSS-27, AMBOSS-29, AMBOSS-36)  ⟷  `Épisodes dépressifs antérieurs` (German-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `État psychique` (German-46)  ⟷  `État psychique et humeur` (German-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'accord de la patiente avec le plan diagnostique` (AMBOSS-27, AMBOSS-29)  ⟷  `Évaluation de l'accord du patient avec le plan diagnostique` (AMBOSS-36) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation du palais` (German-45)  ⟷  `Évaluation du risque` (AZYGOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation du risque` (AZYGOS-30)  ⟷  `Évaluation morphologique` (German-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Alimentation` (AMBOSS-27, RESCOS-44, RESCOS-67, RESCOS-67b)  ⟷  `Palpitations` (AMBOSS-27, AMBOSS-29, German-46, German-47) — **AMBOSS-27, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36)  ⟷  `Antécédents familiaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36, German-45, German-46) — **AMBOSS-27, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36)  ⟷  `Antécédents médicaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36, German-47, RESCOS-67, RESCOS-67b) — **AMBOSS-27, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36, German-45, German-46)  ⟷  `Antécédents médicaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36, German-47, RESCOS-67, RESCOS-67b) — **AMBOSS-27, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36, German-45, German-46)  ⟷  `Antécédents prénataux` (AMBOSS-27) — **AMBOSS-27, section « a »** distingue ces deux items
- ⛔ `Antécédents médicaux` (AMBOSS-27, AMBOSS-29, AMBOSS-36, German-47, RESCOS-67, RESCOS-67b)  ⟷  `Antécédents prénataux` (AMBOSS-27) — **AMBOSS-27, section « a »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-36)  ⟷  `Inspection de l'abdomen` (AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-36)  ⟷  `Palpation de l'abdomen` (AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-36)  ⟷  `Percussion de l'abdomen` (AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Autres symptômes associés` (RESCOS-67, RESCOS-67b)  ⟷  `Symptômes B associés` (RESCOS-67, RESCOS-67b) — **RESCOS-67, section « a »** distingue ces deux items
- ⛔ `Couleur` (AZYGOS-30, RESCOS-44)  ⟷  `Douleur` (RESCOS-44) — **RESCOS-44, section « a »** distingue ces deux items
- ⛔ `Douleur abdominale` (AMBOSS-36)  ⟷  `Douleurs abdominales` (AZYGOS-30, RESCOS-44, RESCOS-67, RESCOS-67b) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Durée de sommeil` (German-45)  ⟷  `Durée du sommeil` (RESCOS-44) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Durée du sommeil` (RESCOS-44)  ⟷  `Qualité du sommeil` (German-46, German-47, RESCOS-44) — **RESCOS-44, section « a »** distingue ces deux items
- ⛔ `Dyspnée d’effort` (AZYGOS-30)  ⟷  `Dyspnée à l'effort` (RESCOS-44) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Examens complémentaires différés` (AMBOSS-36)  ⟷  `Examens complémentaires urgents` (AMBOSS-36) — **AMBOSS-36, section « m »** distingue ces deux items
- ⛔ `Exposition professionnelle` (German-46)  ⟷  `Situation professionnelle/études` (German-46) — **German-46, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-27, AMBOSS-29, AMBOSS-36)  ⟷  `Facteurs améliorants` (AMBOSS-27, AMBOSS-29, AMBOSS-36) — **AMBOSS-27, section « a »** distingue ces deux items
- ⛔ `Fonction hépatique` (RESCOS-67, RESCOS-67b)  ⟷  `Fonction rénale` (RESCOS-67, RESCOS-67b) — **RESCOS-67, section « m »** distingue ces deux items
- ⛔ `Infection récente` (German-46)  ⟷  `Infections récentes` (AMBOSS-27) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Inspection de l'abdomen` (AMBOSS-36)  ⟷  `Inspection des mains` (AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-36)  ⟷  `Palpation de l'abdomen` (AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-36)  ⟷  `Percussion de l'abdomen` (AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Inspection des mains` (AMBOSS-36)  ⟷  `Inspection des sclères` (AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Nausées / vomissements` (AZYGOS-30)  ⟷  `Nausées/vomissements` (AMBOSS-27, AMBOSS-36) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Palpation de l'abdomen` (AMBOSS-36)  ⟷  `Palpation de la rate` (AMBOSS-29, AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-36)  ⟷  `Percussion de l'abdomen` (AMBOSS-36) — **AMBOSS-36, section « e »** distingue ces deux items
- ⛔ `Perte de plaisir` (RESCOS-44)  ⟷  `Perte de poids` (German-47, RESCOS-44) — **RESCOS-44, section « a »** distingue ces deux items
- ⛔ `Polyurie / polydipsie` (AZYGOS-30)  ⟷  `Polyurie ou polydipsie` (RESCOS-67, RESCOS-67b) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Polyurie / polydipsie` (AZYGOS-30)  ⟷  `Polyurie/polydipsie` (German-45) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Polyurie ou polydipsie` (RESCOS-67, RESCOS-67b)  ⟷  `Polyurie/polydipsie` (German-45) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Problèmes intestinaux/changements de couleur des selles` (AMBOSS-36)  ⟷  `Problèmes urinaires/changements de couleur de l'urine` (AMBOSS-36) — **AMBOSS-36, section « a »** distingue ces deux items
- ⛔ `Troubles de concentration` (German-47)  ⟷  `Troubles de la concentration` (RESCOS-67, RESCOS-67b) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Troubles du moi` (German-47)  ⟷  `Troubles du sommeil` (AMBOSS-27, AMBOSS-29, German-47) — **German-47, section « a »** distingue ces deux items

## Fièvre — 3 cas · 5 à juger (0 de forme, 5 de contenu), 7 ⚠️, 15 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Recoloration capillaire` (AZYGOS-32)  ⟷  `Temps de recoloration capillaire` (AZYGOS-31)
- `Symptômes abdominaux associés` (AZYGOS-32)  ⟷  `Symptômes associés` (AZYGOS-31)
- `Question d'ouverture` (AZYGOS-31)  ⟷  `Question ouverte d’entrée` (AZYGOS-32)
- `Symptômes associés` (AZYGOS-31)  ⟷  `Symptômes associés à la fièvre` (RESCOS-46)
- `Coloration cutanée` (AZYGOS-31)  ⟷  `Inspection cutanée` (RESCOS-46)

- ⚠️ `Auscultation antérieure` (RESCOS-46)  ⟷  `Auscultation pulmonaire` (AZYGOS-32) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Coloration cutanée` (AZYGOS-31)  ⟷  `Éruptions cutanées` (RESCOS-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Général` (AZYGOS-31)  ⟷  `État général` (AZYGOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection cutanée` (RESCOS-46)  ⟷  `Éruptions cutanées` (RESCOS-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Méningisme` (AZYGOS-31)  ⟷  `Méningite` (RESCOS-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pneumonie` (RESCOS-46)  ⟷  `Pulmonaire` (RESCOS-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccinations` (AZYGOS-31)  ⟷  `Vaccins` (RESCOS-46) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AZYGOS-31)  ⟷  `Antécédents familiaux` (AZYGOS-31) — **AZYGOS-31, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AZYGOS-31)  ⟷  `Antécédents médicaux` (AZYGOS-31) — **AZYGOS-31, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AZYGOS-31)  ⟷  `Antécédents médicaux` (AZYGOS-31) — **AZYGOS-31, section « a »** distingue ces deux items
- ⛔ `Auscultation antérieure` (RESCOS-46)  ⟷  `Auscultation cardiaque` (RESCOS-46) — **RESCOS-46, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (RESCOS-46)  ⟷  `Auscultation des carotides` (RESCOS-46) — **RESCOS-46, section « e »** distingue ces deux items
- ⛔ `Caractérisation de la fièvre` (RESCOS-46)  ⟷  `Caractérisation de la toux` (RESCOS-46) — **RESCOS-46, section « a »** distingue ces deux items
- ⛔ `Douleur au relâchement croisée` (AZYGOS-32)  ⟷  `Douleur au relâchement direct` (AZYGOS-32) — **AZYGOS-32, section « e »** distingue ces deux items
- ⛔ `Début / Durée` (AZYGOS-31)  ⟷  `Début/durée` (RESCOS-46) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AZYGOS-32)  ⟷  `Facteurs soulageants` (AZYGOS-32, RESCOS-46) — **AZYGOS-32, section « a »** distingue ces deux items
- ⛔ `Foyer pulmonaire` (RESCOS-46)  ⟷  `Pulmonaire` (RESCOS-46) — **RESCOS-46, section « e »** distingue ces deux items
- ⛔ `Hémoculture` (AZYGOS-31)  ⟷  `Hémocultures` (RESCOS-46) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Hémoculture` (AZYGOS-31)  ⟷  `Uroculture` (AZYGOS-31) — **AZYGOS-31, section « m »** distingue ces deux items
- ⛔ `Hémocultures` (RESCOS-46)  ⟷  `Uroculture` (AZYGOS-31) — **AZYGOS-31, section « m »** distingue ces deux items
- ⛔ `Inspection de l’abdomen` (AZYGOS-32)  ⟷  `Percussion de l’abdomen` (AZYGOS-32) — **AZYGOS-32, section « e »** distingue ces deux items
- ⛔ `Palpation` (AZYGOS-31, AZYGOS-32)  ⟷  `Palpation douce` (AZYGOS-32) — **AZYGOS-32, section « e »** distingue ces deux items

## Fièvre au Retour de Voyage — 2 cas · 10 à juger (0 de forme, 10 de contenu), 30 ⚠️, 7 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Ordonnances pour les vaccins` (German-87)  ⟷  `Ordonnances pour tous les vaccins` (German-86)
- `Documentation et assurances` (German-86)  ⟷  `Documentation et ressources` (German-87)
- `Présentation avec nom, fonction et objectif de la consultation` (German-86)  ⟷  `Présentation professionnelle avec nom, fonction et objectif de la consultation` (German-87)
- `Expérience de voyages internationaux` (German-86)  ⟷  `Expériences de voyages internationaux antérieurs` (German-87)
- `Protection anti-vectorielle` (German-87)  ⟷  `Protection anti-vectorielle complète` (German-86)
- `Planification du suivi` (German-87)  ⟷  `Planification du suivi médical` (German-86)
- `Questions et préoccupations de la patiente` (German-86)  ⟷  `Questions et préoccupations spécifiques du patient` (German-87)
- `Trousse de pharmacie complète` (German-86)  ⟷  `Trousse à pharmacie adaptée` (German-87)
- `Évaluation du statut vaccinal actuel` (German-87)  ⟷  `Évaluation détaillée du statut vaccinal` (German-86)
- `Antécédents médicaux et allergies` (German-87)  ⟷  `Antécédents médicaux et état de santé` (German-86)

- ⚠️ `Allergies médicamenteuses` (German-86)  ⟷  `Prescriptions médicamenteuses` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antalgiques/antipyrétiques (paracétamol)` (German-87)  ⟷  `Antalgiques/antipyrétiques (paracétamol, ibuprofène)` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bilan au retour si symptômes` (German-86)  ⟷  `Consultation au retour si symptômes` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Carnet de vaccination international` (German-86, German-87)  ⟷  `Carnet de vaccination à jour` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contact avec animaux` (German-86)  ⟷  `Contact avec animaux prévu` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contacts ambassade/consulat` (German-86)  ⟷  `Coordonnées ambassade/consulat` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contacts d'urgence locaux` (German-86)  ⟷  `Numéros d'urgence locaux` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contraception` (German-86)  ⟷  `Contraception d'urgence` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Disponibilité pour questions` (German-87)  ⟷  `Disponibilité questions par email` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Délai avant le départ` (German-86, German-87)  ⟷  `Délais nécessaires avant le départ` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Eau embouteillée uniquement` (German-86)  ⟷  `Eau en bouteille capsulée uniquement` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition solaire intense` (German-87)  ⟷  `Protection solaire intensive` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Heures de protection renforcée (crépuscule)` (German-87)  ⟷  `Protection renforcée au crépuscule` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Instructions d'utilisation détaillées` (German-87)  ⟷  `Instructions d'utilisation écrites` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies chroniques` (German-86)  ⟷  `Maladies chroniques fils` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies chroniques` (German-86)  ⟷  `Maladies chroniques père` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Mise à jour vaccinations de base` (German-86)  ⟷  `Vaccinations de base` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (German-86)  ⟷  `Médicaments réguliers` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nombre de voyageurs` (German-86)  ⟷  `Nombre et âge des voyageurs` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Numéros d'urgence 24/7` (German-86)  ⟷  `Numéros d'urgence locaux` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Protection solaire indice 50+` (German-87)  ⟷  `Protection solaire intensive` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Protection solaire indice 50+` (German-87)  ⟷  `Protection solaire renforcée` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Protection solaire intensive` (German-86)  ⟷  `Protection solaire renforcée` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Rage (selon activités en jungle)` (German-86)  ⟷  `Rage (selon activités)` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Risques spécifiques au Brésil` (German-86)  ⟷  `Risques spécifiques et prévention` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Risques spécifiques au Brésil` (German-86)  ⟷  `Risques spécifiques à Madagascar` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Règle d'or: "Cook it, boil it, peel it or forget it"` (German-87)  ⟷  `Règle: "Cook it, boil it, peel it or forget it"` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccinations de base` (German-86)  ⟷  `Vaccinations de base complètes` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccinations de base` (German-86)  ⟷  `Vaccinations requises` (German-87) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `État de santé actuel des voyageurs` (German-87)  ⟷  `État de santé actuel et aptitude au voyage` (German-86) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Accidents de circulation` (German-86)  ⟷  `Accidents de la circulation` (German-87) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Antibiotique large spectre (ciprofloxacine ou azithromycine)` (German-86)  ⟷  `Antibiotique à large spectre (ciprofloxacine ou azithromycine)` (German-87) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Comprimés de purification d'eau` (German-87)  ⟷  `Comprimés purification d'eau` (German-86) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Destination et durée` (German-86, German-87)  ⟷  `Destinations visitées` (German-87) — **German-87, section « a »** distingue ces deux items
- ⛔ `Hépatite A` (German-86)  ⟷  `Hépatite B` (German-86) — **German-86, section « a »** distingue ces deux items
- ⛔ `Maladies chroniques fils` (German-87)  ⟷  `Maladies chroniques père` (German-87) — **German-87, section « a »** distingue ces deux items
- ⛔ `Vaccinations de base` (German-86)  ⟷  `Vaccinations nécessaires` (German-86) — **German-86, section « a »** distingue ces deux items

## Fièvre du Nourrisson — 3 cas · 2 à juger (0 de forme, 2 de contenu), 21 ⚠️, 11 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Antécédents médicaux personnels` (German-48)  ⟷  `Antécédents médicaux pertinents` (German-84)
- `Caractérisation de la fièvre` (German-84)  ⟷  `Caractérisation de la toux et de la fièvre` (AMBOSS-7)

- ⚠️ `Altération de l'état de conscience` (German-48, German-84)  ⟷  `Altération de l'état de conscience/léthargie` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres adultes disponibles` (German-84)  ⟷  `Autres anomalies visibles` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ballonnement abdominal` (German-84)  ⟷  `Examen abdominal` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Comportement actuel` (German-84)  ⟷  `Comportement récent` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contact avec des malades` (German-48)  ⟷  `Contacts malades` (AMBOSS-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Couleur` (AMBOSS-7, German-84)  ⟷  `Douleurs` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exanthème` (German-48)  ⟷  `Exanthème subit` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisations` (AMBOSS-7, German-48)  ⟷  `Hospitalisations antérieures` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Irritabilité` (German-48)  ⟷  `Pleurs/irritabilité` (AMBOSS-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments` (AMBOSS-7)  ⟷  `Médicaments actuels` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nausées/vomissements` (AMBOSS-7)  ⟷  `Vomissements` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nombre de couches mouillées aujourd'hui` (German-84)  ⟷  `Nombre de couches mouillées/24h` (AMBOSS-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Raideur de nuque` (German-48)  ⟷  `Raideur de nuque/méningisme` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes de déshydratation` (German-48)  ⟷  `Tentatives de réhydratation` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Surveillance de l'efficacité` (German-84)  ⟷  `Surveillance de l'état général` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Température` (AMBOSS-7)  ⟷  `Température mesurée` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccinations` (AMBOSS-7, German-48)  ⟷  `Vaccinations à jour` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Épisodes antérieurs` (AMBOSS-7)  ⟷  `Épisodes similaires antérieurs` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Éruption cutanée` (AMBOSS-7, German-48)  ⟷  `Éruption cutanée purpurique` (German-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Éruption cutanée` (AMBOSS-7, German-48)  ⟷  `Éruption cutanée/exanthème` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Éruption cutanée purpurique` (German-48)  ⟷  `Éruption cutanée purpurique non effaçable` (German-84) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Chirurgie` (AMBOSS-7)  ⟷  `Chirurgies` (German-48, German-84) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Coloration cutanée` (German-48)  ⟷  `Éruption cutanée` (AMBOSS-7, German-48) — **German-48, section « e »** distingue ces deux items
- ⛔ `Croissance et développement` (AMBOSS-7)  ⟷  `Vaccination et développement` (AMBOSS-7) — **AMBOSS-7, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-7)  ⟷  `Facteurs améliorants` (AMBOSS-7) — **AMBOSS-7, section « a »** distingue ces deux items
- ⛔ `Ganglions cervicaux` (German-48)  ⟷  `Ganglions inguinaux` (German-48) — **German-48, section « e »** distingue ces deux items
- ⛔ `Ganglions cervicaux` (German-48)  ⟷  `Ganglions occipitaux` (German-48) — **German-48, section « e »** distingue ces deux items
- ⛔ `Ganglions inguinaux` (German-48)  ⟷  `Ganglions occipitaux` (German-48) — **German-48, section « e »** distingue ces deux items
- ⛔ `Motif principal` (AMBOSS-7)  ⟷  `Symptôme principal` (AMBOSS-7) — **AMBOSS-7, section « a »** distingue ces deux items
- ⛔ `Revue des systèmes - Digestif` (German-48)  ⟷  `Revue des systèmes - Respiratoire` (German-48) — **German-48, section « a »** distingue ces deux items
- ⛔ `Voyage récent` (AMBOSS-7)  ⟷  `Voyages récents` (German-48, German-84) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Écoulement auriculaire` (AMBOSS-7)  ⟷  `Écoulement oculaire` (AMBOSS-7) — **AMBOSS-7, section « a »** distingue ces deux items

## Grossesse  - Surveillance & Complications — 2 cas · 1 à juger (0 de forme, 1 de contenu), 11 ⚠️, 13 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Antécédents familiaux` (RESCOS-61)  ⟷  `Antécédents médicaux` (AZYGOS-6)

- ⚠️ `Acide folique` (AZYGOS-6)  ⟷  `Acide folique et iode` (AZYGOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents gynécologiques` (AZYGOS-6, RESCOS-61)  ⟷  `Examen gynécologique` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bilan pré-éclampsie` (RESCOS-61)  ⟷  `Pré-éclampsie` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contractions utérines` (RESCOS-61)  ⟷  `Palpation contractions utérines` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examens complémentaires` (RESCOS-61)  ⟷  `Examens complémentaires spécialisés` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Menace accouchement prématuré` (RESCOS-61)  ⟷  `Tocolyse si menace accouchement prématuré` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pré-éclampsie` (RESCOS-61)  ⟷  `Symptômes pré-éclampsie` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes d'alarme` (AZYGOS-6)  ⟷  `Éducation signes d'alarme` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Situation familiale` (RESCOS-61)  ⟷  `Situation sociale` (AZYGOS-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Échographie` (AZYGOS-6)  ⟷  `Échographie fœtale` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Échographie fœtale` (RESCOS-61)  ⟷  `Échographies` (RESCOS-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `1er trimestre` (RESCOS-61)  ⟷  `2ème trimestre` (RESCOS-61) — **RESCOS-61, section « a »** distingue ces deux items
- ⛔ `1er trimestre` (RESCOS-61)  ⟷  `3ème trimestre` (RESCOS-61) — **RESCOS-61, section « a »** distingue ces deux items
- ⛔ `2ème trimestre` (RESCOS-61)  ⟷  `3ème trimestre` (RESCOS-61) — **RESCOS-61, section « a »** distingue ces deux items
- ⛔ `Auscultation Doppler` (RESCOS-61)  ⟷  `Auscultation abdominale` (RESCOS-61) — **RESCOS-61, section « e »** distingue ces deux items
- ⛔ `Auscultation abdominale` (RESCOS-61)  ⟷  `Auscultation cardio-pulmonaire` (RESCOS-61) — **RESCOS-61, section « e »** distingue ces deux items
- ⛔ `Auscultation abdominale` (RESCOS-61)  ⟷  `Palpation abdominale` (RESCOS-61) — **RESCOS-61, section « e »** distingue ces deux items
- ⛔ `Contraception antérieure` (RESCOS-61)  ⟷  `Contractions utérines` (RESCOS-61) — **RESCOS-61, section « a »** distingue ces deux items
- ⛔ `Examen abdominal général` (RESCOS-61)  ⟷  `Examen abdominal obstétrical` (RESCOS-61) — **RESCOS-61, section « e »** distingue ces deux items
- ⛔ `Prévention des infections` (AZYGOS-6)  ⟷  `Prévention et conseils` (RESCOS-61) — **RESCOS-61, section « m »** distingue ces deux items
- ⛔ `Prévention des infections` (AZYGOS-6)  ⟷  `Prévention infections` (RESCOS-61) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Prévention et conseils` (RESCOS-61)  ⟷  `Prévention infections` (RESCOS-61) — **RESCOS-61, section « m »** distingue ces deux items
- ⛔ `Surveillance fœtale` (RESCOS-61)  ⟷  `Surveillance maternelle et fœtale` (RESCOS-61) — **RESCOS-61, section « m »** distingue ces deux items
- ⛔ `Échographie` (AZYGOS-6)  ⟷  `Échographies` (RESCOS-61) — **même signature socle A**, déjà appariés dans leur section

## HTA (Suivi & Crise Hypertensive) — 2 cas · 1 à juger (0 de forme, 1 de contenu), 20 ⚠️, 13 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Examens complémentaires` (German-53)  ⟷  `Examens complémentaires urgents` (German-54)

- ⚠️ `Activité physique` (German-53, German-54)  ⟷  `Activité physique adaptée` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (German-53)  ⟷  `Examen cardiovasculaire` (German-53, German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Automesure tensionnelle` (German-54)  ⟷  `MAPA ou automesure tensionnelle` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres médicaments` (German-54)  ⟷  `Autres médicaments réguliers` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bilan biologique (FSC, ionogramme, créatinine, glycémie)` (German-53)  ⟷  `Bilan biologique (ionogramme, créatinine)` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Carnet de suivi` (German-54)  ⟷  `Carnet de suivi tensionnel` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Complications cardiovasculaires` (German-54)  ⟷  `Maladies cardiovasculaires` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Consommation de sel` (German-54)  ⟷  `Consommation de sel élevée` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contrôle dans 1 mois` (German-53)  ⟷  `Contrôle dans 1 semaine` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (German-53, German-54)  ⟷  `Maladies cardiovasculaires` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (German-54)  ⟷  `Examens complémentaires` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fond d'œil (ou mention)` (German-54)  ⟷  `Fond d'œil (ou mentionner la nécessité)` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Insuffisance cardiaque` (German-54)  ⟷  `Insuffisance cardiaque décompensée` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Insuffisance cardiaque` (German-54)  ⟷  `Signes d'insuffisance cardiaque` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Mauvaise observance thérapeutique` (German-54)  ⟷  `Observance thérapeutique` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Objectifs thérapeutiques` (German-53)  ⟷  `Observance thérapeutique` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Poids et taille` (German-53)  ⟷  `Poids et taille (IMC)` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'œdèmes des membres inférieurs` (German-53)  ⟷  `Œdèmes des membres inférieurs` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de souffles vasculaires` (German-54)  ⟷  `Recherche de souffles vasculaires (carotides, abdomen)` (German-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Surveillance de la fonction rénale et kaliémie` (German-53)  ⟷  `Surveillance fonction rénale et ionogramme` (German-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Alimentation` (German-53, German-54)  ⟷  `Palpitations` (German-53, German-54) — **German-53, section « a »** distingue ces deux items
- ⛔ `Antécédents cardiovasculaires` (German-53)  ⟷  `Antécédents familiaux cardiovasculaires` (German-54) — **German-53, section « a »** distingue ces deux items
- ⛔ `Antécédents cardiovasculaires` (German-53)  ⟷  `Maladies cardiovasculaires` (German-53) — **German-53, section « a »** distingue ces deux items
- ⛔ `Artériopathie périphérique` (German-54)  ⟷  `Cardiopathie ischémique` (German-54) — **German-54, section « a »** distingue ces deux items
- ⛔ `Carnet de suivi` (German-54)  ⟷  `Plan de suivi` (German-54) — **German-54, section « m »** distingue ces deux items
- ⛔ `Consommation d'alcool` (German-53, German-54)  ⟷  `Consommation de sel` (German-54) — **German-54, section « a »** distingue ces deux items
- ⛔ `Insuffisance cardiaque` (German-54)  ⟷  `Insuffisance rénale` (German-54) — **German-54, section « a »** distingue ces deux items
- ⛔ `Maladies cardiaques` (German-53)  ⟷  `Maladies cardiovasculaires` (German-53) — **German-53, section « a »** distingue ces deux items
- ⛔ `Palpation rénale` (German-54)  ⟷  `Évaluation générale` (German-54) — **German-54, section « e »** distingue ces deux items
- ⛔ `Recherche d'œdèmes` (German-54)  ⟷  `Recherche de râles` (German-54) — **German-54, section « e »** distingue ces deux items
- ⛔ `Recherche de B3/B4` (German-54)  ⟷  `Recherche de râles` (German-54) — **German-54, section « e »** distingue ces deux items
- ⛔ `Recherche de râles` (German-54)  ⟷  `Recherche de souffle` (German-54) — **German-54, section « e »** distingue ces deux items
- ⛔ `Recherche de souffle` (German-54)  ⟷  `Recherche de souffles vasculaires` (German-54) — **German-54, section « e »** distingue ces deux items

## Hypoacousie — 4 cas · 8 à juger (1 de forme, 7 de contenu), 21 ⚠️, 22 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Test de Rinne droit` (German-68)  ⟷  `Test de Rinne à droite` (German-67)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Symptômes associés` (AMBOSS-23, AZYGOS-33)  ⟷  `Symptômes associés ORL` (German-67, German-68)
- `Antécédents médicaux` (AMBOSS-23)  ⟷  `Antécédents médicaux et ORL` (German-68)
- `Examen neurologique` (AMBOSS-23)  ⟷  `Examen neurologique de base` (German-68)
- `Conduit auditif externe visible` (German-68)  ⟷  `Inspection du conduit auditif externe visible` (German-67)
- `Information du patient et pronostic` (German-67)  ⟷  `Information et pronostic` (German-68)
- `Question d'entrée ouverte` (German-67)  ⟷  `Question d’entrée` (AZYGOS-33)
- `Audiométrie` (AMBOSS-23, AZYGOS-33)  ⟷  `Audiométrie vocale` (German-67)

- ⚠️ `Apparition temporelle` (German-67, German-68)  ⟷  `Dimension temporelle` (AZYGOS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Compréhension en groupe` (German-68)  ⟷  `Compréhension à droite` (German-68) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Compréhension en groupe` (German-68)  ⟷  `Compréhension à gauche` (German-68) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition professionnelle antérieure` (German-68)  ⟷  `Exposition professionnelle au bruit` (German-67) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-67, German-68)  ⟷  `Recherche d'hypertension artérielle` (German-67) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-67, German-68)  ⟷  `Tension artérielle` (AZYGOS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections passées` (AZYGOS-33)  ⟷  `Infections récentes` (AMBOSS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments` (AMBOSS-23, AZYGOS-33)  ⟷  `Médicaments actuels` (German-67, German-68) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nausées/vomissements` (AMBOSS-23)  ⟷  `Vomissements` (German-67, German-68) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Otoscopie bilatérale` (German-67, German-68)  ⟷  `Presbyacousie bilatérale` (German-68) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du tragus` (German-67)  ⟷  `Pression du tragus` (German-68) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (AZYGOS-33, German-67)  ⟷  `Progression` (AMBOSS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Situation familiale` (German-67)  ⟷  `Situation sociale` (AZYGOS-33) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Surdité de perception symétrique bilatérale` (German-68)  ⟷  `Surdité de perception unilatérale gauche` (German-67) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Rinne` (AZYGOS-33)  ⟷  `Test de Rinne droit` (German-68) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Rinne` (AZYGOS-33)  ⟷  `Test de Rinne à droite` (German-67) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Rinne` (AZYGOS-33)  ⟷  `Test de Rinne à gauche` (German-67) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Rinne` (AZYGOS-33)  ⟷  `Tests de Rinne et Weber` (AMBOSS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Weber` (AZYGOS-33, German-67, German-68)  ⟷  `Tests de Rinne et Weber` (AMBOSS-23) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traction du pavillon` (German-68)  ⟷  `Traction du pavillon auriculaire` (German-67) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traumatisme` (AMBOSS-23)  ⟷  `Traumatisme récent` (German-67) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-23)  ⟷  `Antécédents familiaux` (AMBOSS-23, German-67) — **AMBOSS-23, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-23)  ⟷  `Antécédents médicaux` (AMBOSS-23) — **AMBOSS-23, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-23, German-67)  ⟷  `Antécédents médicaux` (AMBOSS-23) — **AMBOSS-23, section « a »** distingue ces deux items
- ⛔ `Apparition temporelle` (German-67, German-68)  ⟷  `Évolution temporelle` (German-67) — **German-67, section « a »** distingue ces deux items
- ⛔ `Compréhension à droite` (German-68)  ⟷  `Compréhension à gauche` (German-68) — **German-68, section « e »** distingue ces deux items
- ⛔ `Conduit auditif externe droit` (German-67, German-68)  ⟷  `Conduit auditif externe gauche` (German-67, German-68) — **German-67, section « e »** distingue ces deux items
- ⛔ `Conduit auditif externe droit` (German-67, German-68)  ⟷  `Conduit auditif externe visible` (German-68) — **German-68, section « e »** distingue ces deux items
- ⛔ `Conduit auditif externe gauche` (German-67, German-68)  ⟷  `Conduit auditif externe visible` (German-68) — **German-68, section « e »** distingue ces deux items
- ⛔ `Douleur auriculaire` (AMBOSS-23)  ⟷  `Douleurs auriculaires` (German-67, German-68) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Douleur auriculaire` (AMBOSS-23)  ⟷  `Écoulement auriculaire` (AMBOSS-23) — **AMBOSS-23, section « a »** distingue ces deux items
- ⛔ `Douleurs auriculaires` (German-67, German-68)  ⟷  `Écoulement auriculaire` (AMBOSS-23) — **AMBOSS-23, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-23, AZYGOS-33)  ⟷  `Facteurs améliorants` (AMBOSS-23, AZYGOS-33) — **AMBOSS-23, section « a »** distingue ces deux items
- ⛔ `Inspection de l'oreille` (German-67, German-68)  ⟷  `Inspection des oreilles` (AMBOSS-23) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Inspection des oreilles` (AMBOSS-23)  ⟷  `Palpation des oreilles` (AMBOSS-23) — **AMBOSS-23, section « e »** distingue ces deux items
- ⛔ `Inspection du pavillon auriculaire` (German-67)  ⟷  `Traction du pavillon auriculaire` (German-67) — **German-67, section « e »** distingue ces deux items
- ⛔ `Médicaments actuels` (German-67, German-68)  ⟷  `Médicaments ototoxiques` (German-67, German-68) — **German-67, section « a »** distingue ces deux items
- ⛔ `Palpation auriculaire` (German-68)  ⟷  `Pavillon auriculaire droit` (German-68) — **German-68, section « e »** distingue ces deux items
- ⛔ `Pavillon auriculaire droit` (German-68)  ⟷  `Pavillon auriculaire gauche` (German-68) — **German-68, section « e »** distingue ces deux items
- ⛔ `Récupération complète dans 60% des cas` (German-67)  ⟷  `Récupération partielle dans 20% des cas` (German-67) — **German-67, section « m »** distingue ces deux items
- ⛔ `Situation familiale` (German-67)  ⟷  `Situation particulière` (German-67) — **German-67, section « a »** distingue ces deux items
- ⛔ `Situation familiale` (German-67)  ⟷  `Surdité familiale` (German-67) — **German-67, section « a »** distingue ces deux items
- ⛔ `Test de Rinne à droite` (German-67)  ⟷  `Test de Rinne à gauche` (German-67) — **German-67, section « e »** distingue ces deux items

## Hématurie — 2 cas · 2 à juger (0 de forme, 2 de contenu), 5 ⚠️, 15 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Caractérisation de l'hématurie` (AMBOSS-21)  ⟷  `Caractéristiques de l'hématurie` (German-51)
- `Examens d'imagerie et biopsie` (AMBOSS-21)  ⟷  `Examens d'imagerie et explorations` (German-51)

- ⚠️ `Créatinine` (German-51)  ⟷  `Urée, créatinine` (AMBOSS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cystoscopie` (German-51)  ⟷  `Otoscopie` (AMBOSS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen génito-urinaire` (German-51)  ⟷  `Traumatisme génito-urinaire` (German-51) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Manipulations urétrales` (German-51)  ⟷  `Éviter les manipulations urétrales` (German-51) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Rétention urinaire` (German-51)  ⟷  `Sédiment urinaire` (German-51) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-21)  ⟷  `Antécédents familiaux` (AMBOSS-21, German-51) — **AMBOSS-21, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-21)  ⟷  `Antécédents médicaux` (AMBOSS-21, German-51) — **AMBOSS-21, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-21, German-51)  ⟷  `Antécédents médicaux` (AMBOSS-21, German-51) — **AMBOSS-21, section « a »** distingue ces deux items
- ⛔ `Caractérisation de l'hématurie` (AMBOSS-21)  ⟷  `Caractérisation de la toux` (AMBOSS-21) — **AMBOSS-21, section « a »** distingue ces deux items
- ⛔ `Douleur dorsale` (AMBOSS-21)  ⟷  `Douleur thoracique` (AMBOSS-21) — **AMBOSS-21, section « a »** distingue ces deux items
- ⛔ `Examen du cou` (AMBOSS-21)  ⟷  `Examen du dos` (AMBOSS-21) — **AMBOSS-21, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-21)  ⟷  `Facteurs améliorants` (AMBOSS-21) — **AMBOSS-21, section « a »** distingue ces deux items
- ⛔ `Infections urinaires` (German-51)  ⟷  `Rétention urinaire` (German-51) — **German-51, section « a »** distingue ces deux items
- ⛔ `Inspection de l'oropharynx` (AMBOSS-21)  ⟷  `Inspection du thorax` (AMBOSS-21) — **AMBOSS-21, section « e »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-21)  ⟷  `Inspection des oreilles` (AMBOSS-21) — **AMBOSS-21, section « e »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-21)  ⟷  `Palpation de la tête` (AMBOSS-21) — **AMBOSS-21, section « e »** distingue ces deux items
- ⛔ `Inspection des conjonctives` (AMBOSS-21)  ⟷  `Inspection des oreilles` (AMBOSS-21) — **AMBOSS-21, section « e »** distingue ces deux items
- ⛔ `Inspection des oreilles` (AMBOSS-21)  ⟷  `Palpation des oreilles` (AMBOSS-21) — **AMBOSS-21, section « e »** distingue ces deux items
- ⛔ `Inspection du nez` (AMBOSS-21)  ⟷  `Inspection du thorax` (AMBOSS-21) — **AMBOSS-21, section « e »** distingue ces deux items
- ⛔ `Inspection du thorax` (AMBOSS-21)  ⟷  `Palpation du thorax` (AMBOSS-21) — **AMBOSS-21, section « e »** distingue ces deux items

## Ictère — 2 cas · 1 à juger (0 de forme, 1 de contenu), 7 ⚠️, 8 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Anamnèse sociale` (German-55)  ⟷  `Anamnèse uro-génitale` (RESCOS-47)

- ⚠️ `Chirurgies abdominales` (German-55)  ⟷  `Échographie abdominale` (German-55, RESCOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `DD : hépatites` (RESCOS-47)  ⟷  `Hépatite` (RESCOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccination hépatite A` (German-55)  ⟷  `Vaccination ultérieure hépatites A et B` (German-55) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccination hépatite A` (German-55)  ⟷  `Vaccins hépatites A et B` (RESCOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccination hépatite B` (German-55)  ⟷  `Vaccination ultérieure hépatites A et B` (German-55) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccination hépatite B` (German-55)  ⟷  `Vaccins hépatites A et B` (RESCOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccination ultérieure hépatites A et B` (German-55)  ⟷  `Vaccins hépatites A et B` (RESCOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents familiaux` (German-55, RESCOS-47)  ⟷  `Antécédents médicaux` (German-55) — **German-55, section « a »** distingue ces deux items
- ⛔ `Couleur des selles` (German-55, RESCOS-47)  ⟷  `Couleur des urines` (German-55, RESCOS-47) — **German-55, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (RESCOS-47)  ⟷  `Facteurs atténuants` (RESCOS-47) — **RESCOS-47, section « a »** distingue ces deux items
- ⛔ `Maladies génétiques` (German-55)  ⟷  `Maladies hépatiques` (German-55) — **German-55, section « a »** distingue ces deux items
- ⛔ `Maladies hépatiques` (German-55)  ⟷  `Maladies hépatiques familiales` (German-55) — **German-55, section « a »** distingue ces deux items
- ⛔ `Profession` (German-55)  ⟷  `Progression` (German-55) — **German-55, section « a »** distingue ces deux items
- ⛔ `Sang dans les selles` (RESCOS-47)  ⟷  `Sang dans les urines` (RESCOS-47) — **RESCOS-47, section « a »** distingue ces deux items
- ⛔ `Vaccination hépatite A` (German-55)  ⟷  `Vaccination hépatite B` (German-55) — **German-55, section « a »** distingue ces deux items

## Ictère Néonatal — 2 cas · 1 à juger (0 de forme, 1 de contenu), 4 ⚠️, 8 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Antécédents médicaux de la mère` (AZYGOS-35)  ⟷  `Antécédents médicaux et de naissance` (AMBOSS-37)

- ⚠️ `Antécédents médicaux` (AMBOSS-37)  ⟷  `Antécédents médicaux de la mère` (AZYGOS-35) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Circulation cutanée` (AZYGOS-35)  ⟷  `Éruption cutanée` (AMBOSS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Groupage sanguin` (AMBOSS-37)  ⟷  `Groupes sanguins` (AMBOSS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Coombs direct` (AZYGOS-35)  ⟷  `Test de Coombs direct et indirect` (AMBOSS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Alimentation` (AZYGOS-35)  ⟷  `Élimination` (AZYGOS-35) — **AZYGOS-35, section « a »** distingue ces deux items
- ⛔ `Alimentation et comportement de succion` (AZYGOS-35)  ⟷  `Comportement de succion` (AZYGOS-35) — **AZYGOS-35, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-37)  ⟷  `Antécédents familiaux` (AMBOSS-37) — **AMBOSS-37, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-37)  ⟷  `Antécédents médicaux` (AMBOSS-37) — **AMBOSS-37, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-37)  ⟷  `Antécédents médicaux` (AMBOSS-37) — **AMBOSS-37, section « a »** distingue ces deux items
- ⛔ `Groupe sanguin maternel` (AMBOSS-37)  ⟷  `Groupe sanguin paternel` (AMBOSS-37) — **AMBOSS-37, section « a »** distingue ces deux items
- ⛔ `Infections pendant la grossesse` (AZYGOS-35)  ⟷  `Médicaments pendant la grossesse` (AZYGOS-35) — **AZYGOS-35, section « a »** distingue ces deux items
- ⛔ `Écoulement auriculaire` (AMBOSS-37)  ⟷  `Écoulement oculaire` (AMBOSS-37) — **AMBOSS-37, section « a »** distingue ces deux items

## Lombalgies — 8 cas · 40 à juger (0 de forme, 40 de contenu), 73 ⚠️, 42 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Caractérisation de la douleur` (RESCOS-31, RESCOS-48)  ⟷  `Caractérisation de la douleur dorsale` (AMBOSS-10, AMBOSS-9)
- `Examens complémentaires` (German-58)  ⟷  `Examens complémentaires urgents` (AMBOSS-10, AMBOSS-9, German-59)
- `Intensité de la douleur` (German-58, German-59)  ⟷  `Type et intensité de la douleur` (German-57)
- `Symptômes neurologiques` (AZYGOS-20, German-59, RESCOS-48)  ⟷  `Symptômes neurologiques - Force` (German-58)
- `Autres symptômes associés` (German-57)  ⟷  `Symptômes associés` (AMBOSS-10, AMBOSS-9, AZYGOS-20)
- `Fracture vertébrale ostéoporotique` (German-59)  ⟷  `Fracture vertébrale traumatique` (German-57)
- `Prise en charge thérapeutique` (German-57, German-58)  ⟷  `Prise en charge thérapeutique ambulatoire` (German-59)
- `Recherche des drapeaux rouges` (RESCOS-48)  ⟷  `Recherche des drapeaux rouges (red flags)` (German-57)
- `Examen neurologique` (AMBOSS-10, AMBOSS-9)  ⟷  `Examen neurologique complet` (German-57)
- `Examens complémentaires biologiques` (German-57)  ⟷  `Examens complémentaires urgents` (AMBOSS-10, AMBOSS-9, German-59)
- `Mobilité rachidienne` (German-57)  ⟷  `Tests de mobilité rachidienne` (German-58)
- `Facteurs modulants` (German-57, German-58, German-59)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-20)
- `Recherche de symptômes neurologiques` (AMBOSS-9)  ⟷  `Recherche de symptômes spécifiques` (AMBOSS-10)
- `Régime adapté selon composition du calcul` (RESCOS-31)  ⟷  `Régime adapté selon type de calcul` (German-59)
- `Examens complémentaires` (German-58)  ⟷  `Examens complémentaires biologiques` (German-57)
- `Recherche de symptômes spécifiques` (AMBOSS-10)  ⟷  `Recherche de symptômes spécifiques - Drapeaux rouges` (AMBOSS-9)
- `Ionogramme sanguin` (German-59)  ⟷  `Ionogramme sanguin, calcémie` (RESCOS-31)
- `Symptômes associés` (AMBOSS-10, AMBOSS-9, AZYGOS-20)  ⟷  `Symptômes urinaires associés` (German-59, RESCOS-31)
- `Recherche de symptômes neurologiques` (AMBOSS-9)  ⟷  `Symptômes neurologiques` (AZYGOS-20, German-59, RESCOS-48)
- `Signe de Lasègue` (AZYGOS-20)  ⟷  `Test de Lasègue` (German-57, German-58, German-59, RESCOS-48)
- `Hypothèse diagnostique principale` (RESCOS-48)  ⟷  `Hypothèses diagnostiques` (AMBOSS-10, AMBOSS-9)
- `Symptômes neurologiques` (AZYGOS-20, German-59, RESCOS-48)  ⟷  `Symptômes neurologiques - Sensibilité` (German-58)
- `Antécédents de fractures` (German-58)  ⟷  `Antécédents opératoires` (AZYGOS-20)
- `Examen des hanches` (German-57, German-58)  ⟷  `Examen du rachis` (German-59)
- `Critères d'hospitalisation` (German-59)  ⟷  `Indications d'hospitalisation` (RESCOS-31)
- `Fracture vertébrale` (German-58)  ⟷  `Fracture vertébrale traumatique` (German-57)
- `Examen du dos` (AMBOSS-10, AMBOSS-9)  ⟷  `Examen du rachis` (German-59)
- `Anamnèse sociale` (German-57, German-59)  ⟷  `Anamnèse uro-génitale` (RESCOS-48)
- `Question d’entrée` (AZYGOS-20)  ⟷  `Questions de clôture` (German-57, German-58, German-59)
- `Antécédents de lombalgies` (German-58, German-59)  ⟷  `Antécédents urologiques` (RESCOS-31)
- `Examen génital` (AMBOSS-10)  ⟷  `Examen rectal` (AMBOSS-9)
- `Localisation précise` (German-57, German-59)  ⟷  `Localisation précise de la douleur` (German-58)
- `Antécédents opératoires` (AZYGOS-20)  ⟷  `Antécédents urologiques` (RESCOS-31)
- `Examens de laboratoire` (RESCOS-48)  ⟷  `Résultats de laboratoire` (AZYGOS-20)
- `Événement déclenchant` (German-58)  ⟷  `Événement déclenchant ou traumatisme` (German-59)
- `Pattern de la douleur` (German-58)  ⟷  `Type et intensité de la douleur` (German-57)
- `Caractérisation de la douleur` (RESCOS-31, RESCOS-48)  ⟷  `Localisation précise de la douleur` (German-58)
- `Réaction appropriée au défi concernant la dépendance aux antalgiques` (AMBOSS-9)  ⟷  `Réaction appropriée au défi concernant le manque d'exercice` (AMBOSS-10)
- `Antécédents chirurgicaux` (AMBOSS-10, AMBOSS-9, German-57, German-58, German-59)  ⟷  `Antécédents urologiques` (RESCOS-31)
- `Antécédents de fractures` (German-58)  ⟷  `Antécédents de lithiase` (German-59)

- ⚠️ `Activité physique` (German-57, German-59, RESCOS-48)  ⟷  `Activité physique régulière` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation riche en oxalates` (German-59)  ⟷  `Alimentation riche en protéines` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Allergies médicamenteuses` (RESCOS-31)  ⟷  `Médicamenteuses` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents de lithiase` (German-59)  ⟷  `Antécédents de lithiase urinaire` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents de lithiase` (German-59)  ⟷  `Antécédents familiaux de lithiase` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents familiaux` (AMBOSS-10, AMBOSS-9, AZYGOS-20)  ⟷  `Antécédents familiaux de lithiase` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents néoplasiques` (RESCOS-48)  ⟷  `Antécédents opératoires` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents néoplasiques` (RESCOS-48)  ⟷  `Antécédents urologiques` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents néoplasiques` (RESCOS-48)  ⟷  `Causes néoplasiques` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres pathologies` (German-57)  ⟷  `Autres pathologies pertinentes` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Brûlures mictionnelles` (RESCOS-48)  ⟷  `Brûlures mictionnelles possibles` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Brûlures mictionnelles` (RESCOS-48)  ⟷  `Urgences mictionnelles` (German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT du rachis` (AMBOSS-9)  ⟷  `Inspection du rachis` (German-57, RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Causes infectieuses` (AZYGOS-20)  ⟷  `Signes infectieux` (German-57) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Consommation d'alcool` (RESCOS-31)  ⟷  `Consommation de sel` (German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Consommation de bière` (RESCOS-31)  ⟷  `Consommation de sel` (German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Consommation de sel` (German-59)  ⟷  `Consommation de sel importante` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contrôle clinique à 4-6 semaines` (German-57)  ⟷  `Contrôle à 2 semaines` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostics différentiels` (German-57, German-58, German-59)  ⟷  `Examens différentiels` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Drogues` (German-57, German-58, German-59)  ⟷  `Drogues i.v.` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen ciblé des réflexes ostéo-tendineux` (AMBOSS-9)  ⟷  `Réflexes ostéo-tendineux` (German-57, RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cutané` (AMBOSS-10)  ⟷  `Examen rectal` (AMBOSS-9) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen des fosses lombaires` (RESCOS-31)  ⟷  `Percussion des fosses lombaires` (German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen du rachis` (German-59)  ⟷  `IRM du rachis` (AMBOSS-9) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AMBOSS-10, AMBOSS-9)  ⟷  `Examen neurologique sommaire` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AMBOSS-10, AMBOSS-9)  ⟷  `Examens immunologiques` (AMBOSS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AMBOSS-10, AMBOSS-9)  ⟷  `Examens microbiologiques` (AMBOSS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique complet` (German-57)  ⟷  `Examen neurologique sommaire` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteur déclenchant` (German-57)  ⟷  `Facteurs déclenchants et contexte` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs aggravants` (AMBOSS-10, AMBOSS-9)  ⟷  `Facteurs atténuants/aggravants` (RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs améliorants` (AMBOSS-10, AMBOSS-9)  ⟷  `Facteurs modulants` (German-57, German-58, German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs atténuants/aggravants` (RESCOS-48)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Flexion antérieure` (German-57)  ⟷  `IST antérieures` (AMBOSS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Force musculaire segmentaire` (German-57)  ⟷  `Testing musculaire segmentaire` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fracture atraumatique` (AZYGOS-20)  ⟷  `Fracture vertébrale traumatique` (German-57) — **antonymes présumés** (préfixe privatif « a- ») : aucune grille ne les porte ensemble, donc la propriété 8 n'a pas de témoin. *(Par ailleurs inerte : la propriété 7 la refuserait.)*
- ⚠️ `Fractures antérieures` (German-59)  ⟷  `IST antérieures` (AMBOSS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Général` (AZYGOS-20)  ⟷  `État général` (German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Incontinence` (German-59)  ⟷  `Incontinence fécale` (German-58, RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Incontinence` (German-59)  ⟷  `Incontinence urinaire` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Incontinence` (German-59)  ⟷  `Urgences/incontinence` (RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Incontinence fécale` (German-58, RESCOS-48)  ⟷  `Incontinence urinaire ou fécale` (German-57) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Incontinence urinaire` (German-58)  ⟷  `Incontinence urinaire ou fécale` (German-57) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections passées` (AZYGOS-20)  ⟷  `Infections récentes` (AMBOSS-10, AMBOSS-9) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections récentes` (AMBOSS-10, AMBOSS-9)  ⟷  `Infections urinaires récurrentes` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection` (AZYGOS-20, German-59)  ⟷  `Inspection du dos` (AMBOSS-10, AMBOSS-9) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du dos` (AMBOSS-10, AMBOSS-9)  ⟷  `Inspection du rachis` (German-57, RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du rachis` (German-57, RESCOS-48)  ⟷  `Inspection du thorax` (AMBOSS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Insuffisance rénale aiguë` (German-59)  ⟷  `Insuffisance rénale aiguë obstructive` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicamenteuses` (AZYGOS-20)  ⟷  `Médicaments` (AMBOSS-10, AMBOSS-9, AZYGOS-20, RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (AMBOSS-9)  ⟷  `Médicaments et habitudes` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (AMBOSS-9)  ⟷  `Médicaments réguliers` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (AMBOSS-9)  ⟷  `Traitements actuels` (German-57, German-58, German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nausées/vomissements` (German-59)  ⟷  `Vomissements` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ostéoporose familiale` (German-57)  ⟷  `Ostéoporose primaire` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du rachis` (German-57)  ⟷  `Palpation du thorax` (AMBOSS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du rachis` (German-57)  ⟷  `Palpation/percussion du rachis` (RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion des champs pulmonaires` (AMBOSS-10)  ⟷  `Percussion des fosses lombaires` (German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Protection` (AMBOSS-10)  ⟷  `Rotation` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Protection` (AMBOSS-10)  ⟷  `Rotations` (German-57) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'un contact lombaire` (RESCOS-31)  ⟷  `Recherche de contracture musculaire` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de complications` (RESCOS-31)  ⟷  `Recherche de scoliose` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de contracture musculaire` (German-58)  ⟷  `Recherche de contracture paravertébrale` (German-57, German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de sang` (RESCOS-48)  ⟷  `Recherche de scoliose` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche syndrome de la queue de cheval` (German-58)  ⟷  `Syndrome de la queue de cheval` (German-57, RESCOS-48) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Résultat` (German-57, German-59)  ⟷  `Résultat du CT` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Rétention aiguë d'urine` (RESCOS-31)  ⟷  `Rétention urinaire` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes infectieux` (German-57)  ⟷  `Signes vitaux` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sudations nocturnes` (RESCOS-48)  ⟷  `Sueurs nocturnes` (AMBOSS-10, AMBOSS-9, AZYGOS-20, German-57, German-58, German-59) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Bragard` (German-57, German-58)  ⟷  `Test de Romberg` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test de Romberg` (AZYGOS-20)  ⟷  `Test de Schober` (German-58) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tonus sphinctérien` (German-58, RESCOS-48)  ⟷  `Troubles vésico-sphinctériens` (AZYGOS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Épisodes antérieurs` (AMBOSS-10, AMBOSS-9, German-58, German-59)  ⟷  `Épisodes similaires antérieurs` (RESCOS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Éruption/changements cutanés (sur le dos)` (AMBOSS-9)  ⟷  `Éruption/changements cutanés et unguéaux` (AMBOSS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédent de fracture` (German-57)  ⟷  `Antécédents de fractures` (German-58) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Antécédents chirurgicaux` (AMBOSS-10, AMBOSS-9, German-57, German-58, German-59)  ⟷  `Antécédents familiaux` (AMBOSS-10, AMBOSS-9, AZYGOS-20) — **AMBOSS-10, section « a »** distingue ces deux items
- ⛔ `Antécédents de fractures` (German-58)  ⟷  `Antécédents de lombalgies` (German-58, German-59) — **German-58, section « a »** distingue ces deux items
- ⛔ `Antécédents de lithiase` (German-59)  ⟷  `Antécédents de lombalgies` (German-58, German-59) — **German-59, section « a »** distingue ces deux items
- ⛔ `CT du rachis` (AMBOSS-9)  ⟷  `IRM du rachis` (AMBOSS-9) — **AMBOSS-9, section « m »** distingue ces deux items
- ⛔ `Calculs 5-10mm: expulsion dans 50% des cas` (RESCOS-31)  ⟷  `Calculs < 5mm: expulsion spontanée dans 70% des cas` (RESCOS-31) — **RESCOS-31, section « m »** distingue ces deux items
- ⛔ `Consommation de bière` (RESCOS-31)  ⟷  `Consommation de sel importante` (RESCOS-31) — **RESCOS-31, section « a »** distingue ces deux items
- ⛔ `Douleur nocturne` (AZYGOS-20)  ⟷  `Douleurs nocturnes` (German-58) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Douleur nocturne` (AZYGOS-20)  ⟷  `Sueurs nocturnes` (AMBOSS-10, AMBOSS-9, AZYGOS-20, German-57, German-58, German-59) — **AZYGOS-20, section « a »** distingue ces deux items
- ⛔ `Douleurs nocturnes` (German-58)  ⟷  `Sueurs nocturnes` (AMBOSS-10, AMBOSS-9, AZYGOS-20, German-57, German-58, German-59) — **German-58, section « a »** distingue ces deux items
- ⛔ `Examen ciblé de la marche` (AMBOSS-10, AMBOSS-9)  ⟷  `Examen ciblé de la sensibilité` (AMBOSS-9) — **AMBOSS-9, section « e »** distingue ces deux items
- ⛔ `Examen du dos` (AMBOSS-10, AMBOSS-9)  ⟷  `Examen du genou` (AMBOSS-10) — **AMBOSS-10, section « e »** distingue ces deux items
- ⛔ `Examen en position assise` (German-58)  ⟷  `Examen en position debout` (German-58) — **German-58, section « e »** distingue ces deux items
- ⛔ `Examens immunologiques` (AMBOSS-10)  ⟷  `Examens microbiologiques` (AMBOSS-10) — **AMBOSS-10, section « m »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-10, AMBOSS-9)  ⟷  `Facteurs améliorants` (AMBOSS-10, AMBOSS-9) — **AMBOSS-10, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-10, AMBOSS-9)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-20) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AMBOSS-10, AMBOSS-9)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-20) — **AZYGOS-20, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (AMBOSS-10, AMBOSS-9)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-20) — **AMBOSS-10, section « a »** distingue ces deux items
- ⛔ `IST antérieures` (AMBOSS-10)  ⟷  `Épisodes antérieurs` (AMBOSS-10, AMBOSS-9, German-58, German-59) — **AMBOSS-10, section « a »** distingue ces deux items
- ⛔ `Incontinence fécale` (German-58, RESCOS-48)  ⟷  `Incontinence urinaire` (German-58) — **German-58, section « a »** distingue ces deux items
- ⛔ `Inspection de l'oropharynx` (AMBOSS-10)  ⟷  `Inspection du thorax` (AMBOSS-10) — **AMBOSS-10, section « e »** distingue ces deux items
- ⛔ `Inspection des conjonctives` (AMBOSS-10)  ⟷  `Inspection des mains` (AMBOSS-10) — **AMBOSS-10, section « e »** distingue ces deux items
- ⛔ `Inspection des membres inférieurs` (AMBOSS-10, AMBOSS-9)  ⟷  `Inspection des membres supérieurs` (AMBOSS-10) — **AMBOSS-10, section « e »** distingue ces deux items
- ⛔ `Inspection du dos` (AMBOSS-10, AMBOSS-9)  ⟷  `Inspection du thorax` (AMBOSS-10) — **AMBOSS-10, section « e »** distingue ces deux items
- ⛔ `Inspection du rachis` (German-57, RESCOS-48)  ⟷  `Palpation du rachis` (German-57) — **German-57, section « e »** distingue ces deux items
- ⛔ `Inspection du thorax` (AMBOSS-10)  ⟷  `Palpation du thorax` (AMBOSS-10) — **AMBOSS-10, section « e »** distingue ces deux items
- ⛔ `Intensité de la douleur` (German-58, German-59)  ⟷  `Pattern de la douleur` (German-58) — **German-58, section « a »** distingue ces deux items
- ⛔ `Intensité de la douleur` (German-58, German-59)  ⟷  `Qualité de la douleur` (German-58, German-59) — **German-58, section « a »** distingue ces deux items
- ⛔ `L5 : Face dorsale du pied` (German-58)  ⟷  `S1 : Face latérale du pied` (German-58) — **German-58, section « e »** distingue ces deux items
- ⛔ `Localisation` (AMBOSS-10, AMBOSS-9, AZYGOS-20, German-57, German-58, RESCOS-31, RESCOS-48)  ⟷  `Localisation précise` (German-57, German-59) — **German-57, section « a »** distingue ces deux items
- ⛔ `Maladies osseuses ou tumorales` (AZYGOS-20)  ⟷  `Maladies tumorales` (AZYGOS-20) — **AZYGOS-20, section « a »** distingue ces deux items
- ⛔ `Médicaments` (AMBOSS-10, AMBOSS-9, AZYGOS-20, RESCOS-48)  ⟷  `Médicaments actuels` (AMBOSS-9) — **AMBOSS-9, section « a »** distingue ces deux items
- ⛔ `Pattern de la douleur` (German-58)  ⟷  `Qualité de la douleur` (German-58, German-59) — **German-58, section « a »** distingue ces deux items
- ⛔ `Point urétéral inférieur` (German-59, RESCOS-31)  ⟷  `Point urétéral moyen` (German-59, RESCOS-31) — **German-59, section « e »** distingue ces deux items
- ⛔ `Point urétéral inférieur` (German-59, RESCOS-31)  ⟷  `Point urétéral supérieur` (German-59, RESCOS-31) — **German-59, section « e »** distingue ces deux items
- ⛔ `Point urétéral moyen` (German-59, RESCOS-31)  ⟷  `Point urétéral supérieur` (German-59, RESCOS-31) — **German-59, section « e »** distingue ces deux items
- ⛔ `Problèmes oculaires` (AMBOSS-10)  ⟷  `Problèmes urinaires` (AMBOSS-10, AMBOSS-9) — **AMBOSS-10, section « a »** distingue ces deux items
- ⛔ `Recherche de douleur` (German-58)  ⟷  `Recherche de points douloureux` (German-58) — **German-58, section « e »** distingue ces deux items
- ⛔ `Recherche de douleur` (German-58)  ⟷  `Recherche de scoliose` (German-58) — **German-58, section « e »** distingue ces deux items
- ⛔ `Rotation` (AZYGOS-20)  ⟷  `Rotations` (German-57) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Symptômes neurologiques - Force` (German-58)  ⟷  `Symptômes neurologiques - Sensibilité` (German-58) — **German-58, section « a »** distingue ces deux items
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-20)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-20) — **AZYGOS-20, section « a »** distingue ces deux items

## Mal de Gorge (Angine) — 2 cas · 2 à juger (0 de forme, 2 de contenu), 5 ⚠️, 25 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Antécédents ORL` (AZYGOS-21)  ⟷  `Antécédents sexuels` (AMBOSS-30)
- `Antécédents` (AZYGOS-21)  ⟷  `Antécédents sexuels` (AMBOSS-30)

- ⚠️ `Inspection de l'oropharynx` (AMBOSS-30)  ⟷  `Inspection du pharynx` (AZYGOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du cou` (AMBOSS-30)  ⟷  `Inspection du pharynx` (AZYGOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du cou` (AMBOSS-30)  ⟷  `Palpation du cou` (AZYGOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du nez` (AMBOSS-30)  ⟷  `Inspection du pharynx` (AZYGOS-21) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du cou` (AZYGOS-21)  ⟷  `Palpation du foie` (AMBOSS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents` (AZYGOS-21)  ⟷  `Antécédents ORL` (AZYGOS-21) — **AZYGOS-21, section « a »** distingue ces deux items
- ⛔ `Antécédents ORL` (AZYGOS-21)  ⟷  `Antécédents familiaux` (AMBOSS-30, AZYGOS-21) — **AZYGOS-21, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-30)  ⟷  `Antécédents familiaux` (AMBOSS-30, AZYGOS-21) — **AMBOSS-30, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-30)  ⟷  `Antécédents médicaux` (AMBOSS-30) — **AMBOSS-30, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-30, AZYGOS-21)  ⟷  `Antécédents médicaux` (AMBOSS-30) — **AMBOSS-30, section « a »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-30)  ⟷  `Inspection de l'abdomen` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-30)  ⟷  `Palpation de l'abdomen` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-30)  ⟷  `Percussion de l'abdomen` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-30)  ⟷  `Facteurs améliorants` (AMBOSS-30) — **AMBOSS-30, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-30)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-21) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AMBOSS-30)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-21) — **AZYGOS-21, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (AMBOSS-30)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-21) — **AMBOSS-30, section « a »** distingue ces deux items
- ⛔ `Hospitalisation` (AZYGOS-21)  ⟷  `Hospitalisations` (AMBOSS-30) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Hospitalisation` (AZYGOS-21)  ⟷  `Localisation` (AMBOSS-30, AZYGOS-21) — **AMBOSS-30, section « a »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-30)  ⟷  `Inspection de l'oropharynx` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-30)  ⟷  `Inspection de la tête` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-30)  ⟷  `Palpation de l'abdomen` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-30)  ⟷  `Percussion de l'abdomen` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-30)  ⟷  `Palpation de la tête` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Inspection du cou` (AMBOSS-30)  ⟷  `Inspection du nez` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-30)  ⟷  `Palpation de la rate` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-30)  ⟷  `Palpation de la tête` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-30)  ⟷  `Percussion de l'abdomen` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `Palpation de la rate` (AMBOSS-30)  ⟷  `Palpation de la tête` (AMBOSS-30) — **AMBOSS-30, section « e »** distingue ces deux items
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-21)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-21) — **AZYGOS-21, section « a »** distingue ces deux items

## Masse Mammaire — 2 cas · 2 à juger (0 de forme, 2 de contenu), 5 ⚠️, 13 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Antécédents familiaux` (German-62)  ⟷  `Cancers familiaux` (AZYGOS-37)
- `Palpation des ganglions` (AZYGOS-37)  ⟷  `Palpation des ganglions lymphatiques` (German-62)

- ⚠️ `Auto-examen des seins` (AZYGOS-37)  ⟷  `Examen des seins` (German-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cancer du sein familial` (German-62)  ⟷  `Cancers familiaux` (AZYGOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Localisation` (AZYGOS-37)  ⟷  `Localisation précise` (German-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Localisation` (AZYGOS-37)  ⟷  `Réalisation` (AZYGOS-37) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Échographie mammaire` (AZYGOS-37)  ⟷  `Échographie mammaire (US)` (German-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Anamnèse gynécologique` (German-62)  ⟷  `Maladies gynécologiques` (German-62) — **German-62, section « a »** distingue ces deux items
- ⛔ `Anamnèse obstétricale` (German-62)  ⟷  `Anamnèse sociale` (AZYGOS-37, German-62) — **German-62, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (German-62)  ⟷  `Antécédents médicaux` (German-62) — **German-62, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (German-62)  ⟷  `Antécédents parentaux` (German-62) — **German-62, section « a »** distingue ces deux items
- ⛔ `Antécédents médicaux` (German-62)  ⟷  `Antécédents parentaux` (German-62) — **German-62, section « a »** distingue ces deux items
- ⛔ `Axillaires des deux côtés` (AZYGOS-37)  ⟷  `Sous-claviculaires des deux côtés` (AZYGOS-37) — **AZYGOS-37, section « e »** distingue ces deux items
- ⛔ `Axillaires des deux côtés` (AZYGOS-37)  ⟷  `Sus-claviculaires des deux côtés` (AZYGOS-37) — **AZYGOS-37, section « e »** distingue ces deux items
- ⛔ `Contraception actuelle` (German-62)  ⟷  `Contraception antérieure` (German-62) — **German-62, section « a »** distingue ces deux items
- ⛔ `Contraception actuelle` (German-62)  ⟷  `Médication actuelle` (German-62) — **German-62, section « a »** distingue ces deux items
- ⛔ `Ganglions axillaires` (German-62)  ⟷  `Ganglions sous-claviculaires` (German-62) — **German-62, section « e »** distingue ces deux items
- ⛔ `Ganglions axillaires` (German-62)  ⟷  `Ganglions sus-claviculaires` (German-62) — **German-62, section « e »** distingue ces deux items
- ⛔ `Ganglions sous-claviculaires` (German-62)  ⟷  `Ganglions sus-claviculaires` (German-62) — **German-62, section « e »** distingue ces deux items
- ⛔ `Sous-claviculaires des deux côtés` (AZYGOS-37)  ⟷  `Sus-claviculaires des deux côtés` (AZYGOS-37) — **AZYGOS-37, section « e »** distingue ces deux items

## Ménopause — 2 cas · 8 à juger (0 de forme, 8 de contenu), 13 ⚠️, 8 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Symptômes uro-génitaux` (German-63)  ⟷  `Symptômes urogénitaux` (German-6)
- `Autres cancers familiaux` (German-6)  ⟷  `Cancers familiaux` (German-63)
- `Examen gynécologique` (German-63)  ⟷  `Examen neurologique` (German-6)
- `Symptômes neurologiques` (German-6)  ⟷  `Symptômes psychologiques` (German-63)
- `Symptômes généraux` (German-6)  ⟷  `Symptômes uro-génitaux` (German-63)
- `Symptômes cardiovasculaires` (German-6)  ⟷  `Symptômes ostéo-articulaires` (German-63)
- `Symptômes neuropsychiatriques` (German-6)  ⟷  `Symptômes psychologiques` (German-63)
- `Examen mammaire` (German-63)  ⟷  `Examen pulmonaire` (German-6)

- ⚠️ `Crampes abdominales` (German-6)  ⟷  `Examen abdominal` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Crampes abdominales` (German-6)  ⟷  `Masses abdominales` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (German-6)  ⟷  `Maladies cardiovasculaires` (German-6, German-63) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (German-6)  ⟷  `Symptômes cardiovasculaires` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen gynécologique` (German-63)  ⟷  `Statut gynécologique` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (German-6)  ⟷  `Examens complémentaires` (German-63) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (German-6)  ⟷  `Examens urinaires` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (German-6)  ⟷  `Œdème pulmonaire` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs déclenchants` (German-6)  ⟷  `Éviter les facteurs déclenchants` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies thyroïdiennes` (German-6)  ⟷  `Palpation thyroïdienne` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Modifications cutanées actuelles` (German-6)  ⟷  `Modifications cutanées lors des épisodes` (German-6) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (German-6)  ⟷  `Traitements actuels` (German-63) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tension artérielle` (German-6)  ⟷  `Tension intérieure` (German-63) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Alimentation` (German-63)  ⟷  `Palpitations` (German-6, German-63) — **German-63, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (German-6)  ⟷  `Cancers familiaux` (German-63) — **German-63, section « a »** distingue ces deux items
- ⛔ `Concentration` (German-63)  ⟷  `Contraception` (German-6, German-63) — **German-63, section « a »** distingue ces deux items
- ⛔ `Maladies cardiovasculaires` (German-6, German-63)  ⟷  `Symptômes cardiovasculaires` (German-6) — **German-6, section « a »** distingue ces deux items
- ⛔ `Symptômes généraux` (German-6)  ⟷  `Symptômes urogénitaux` (German-6) — **German-6, section « a »** distingue ces deux items
- ⛔ `Symptômes neurologiques` (German-6)  ⟷  `Symptômes neuropsychiatriques` (German-6) — **German-6, section « a »** distingue ces deux items
- ⛔ `Symptômes neurologiques` (German-6)  ⟷  `Symptômes urogénitaux` (German-6) — **German-6, section « a »** distingue ces deux items
- ⛔ `Tremblements` (German-6)  ⟷  `Tremblements fins` (German-6) — **German-6, section « a »** distingue ces deux items

## Neuropathie Périphérique — 4 cas · 11 à juger (0 de forme, 11 de contenu), 47 ⚠️, 56 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Orientation et suivi spécialisé` (RESCOS-30)  ⟷  `Orientations spécialisées` (German-83)
- `Symptômes associés` (AMBOSS-20, AZYGOS-29)  ⟷  `Symptômes moteurs associés` (German-83)
- `Caractérisation de la douleur` (AMBOSS-20)  ⟷  `Caractérisation de la douleur neuropathique` (RESCOS-30)
- `Facteurs modulants` (German-83)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-29)
- `Sensibilité vibratoire` (RESCOS-30)  ⟷  `Sensibilité vibratoire (diapason)` (German-83)
- `Examens complémentaires` (German-83)  ⟷  `Examens complémentaires spécialisés` (RESCOS-30)
- `Caractérisation des symptômes sensitifs` (AMBOSS-20)  ⟷  `Caractéristiques des troubles sensitifs` (German-83)
- `Facteurs déclenchants` (AZYGOS-29, RESCOS-30)  ⟷  `Facteurs modulants` (German-83)
- `Médicaments actuels` (German-83)  ⟷  `Médicaments et toxiques` (RESCOS-30)
- `Examens complémentaires additionnels` (AMBOSS-20, German-83)  ⟷  `Examens complémentaires spécialisés` (RESCOS-30)
- `Symptômes autonomes` (AZYGOS-29)  ⟷  `Symptômes visuels` (German-83)

- ⚠️ `Alimentation` (AMBOSS-20)  ⟷  `Orientation` (AZYGOS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation` (AMBOSS-20)  ⟷  `Palpitations` (AZYGOS-29, German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents chirurgicaux` (AMBOSS-20)  ⟷  `Antécédents chirurgicaux rachidiens` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Audition` (German-83)  ⟷  `Irradiation` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation de l'abdomen` (AMBOSS-20)  ⟷  `Auscultation des carotides` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bilan hépatique complet` (AMBOSS-20)  ⟷  `Bilan lipidique complet` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Centre de la douleur` (RESCOS-30)  ⟷  `Type de douleur` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Doigt-nez` (AZYGOS-29)  ⟷  `Test doigt-nez` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs articulaires` (AMBOSS-20, German-83)  ⟷  `Douleurs lumbo(radiculaires)` (AZYGOS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Déformation des pieds` (RESCOS-30)  ⟷  `Déformations` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (AMBOSS-20, German-83)  ⟷  `Symptômes cardiovasculaires` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen ciblé de la sensibilité` (AMBOSS-20)  ⟷  `Examen de la sensibilité` (German-83, RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen vasculaire des membres inférieurs` (RESCOS-30)  ⟷  `Œdèmes des membres inférieurs` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteur déclencheur` (German-83)  ⟷  `Facteurs déclenchants` (AZYGOS-29, RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs améliorants` (AMBOSS-20, German-83)  ⟷  `Facteurs déclenchants` (AZYGOS-29, RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fièvre` (AZYGOS-29)  ⟷  `Frère` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fond d'œil` (German-83)  ⟷  `Fond d'œil direct` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Glycémie à jeun` (German-83)  ⟷  `Glycémie à jeun, HbA1c` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension` (German-83)  ⟷  `Signes d'hypertension` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections antérieures` (AZYGOS-29)  ⟷  `Infections récentes` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections récentes` (AMBOSS-20)  ⟷  `Vaccinations récentes` (AZYGOS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection` (AZYGOS-29)  ⟷  `Inspection rachis` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'abdomen` (AMBOSS-20)  ⟷  `Inspection de la plaie` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de la plaie` (German-83)  ⟷  `Inspection des mains` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de la plaie` (German-83)  ⟷  `Inspection des sclères` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des conjonctives` (AMBOSS-20)  ⟷  `Inspection des pieds` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des mains` (AMBOSS-20)  ⟷  `Inspection des pieds` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des membres inférieurs` (AMBOSS-20)  ⟷  `Œdèmes des membres inférieurs` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des pieds` (German-83)  ⟷  `Inspection des sclères` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Localisation` (AMBOSS-20, AZYGOS-29, German-83)  ⟷  `Localisation précise` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Opérations antérieures` (AZYGOS-29)  ⟷  `Traitements antérieurs` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation cardiaque` (German-83)  ⟷  `Palpation du foie` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation des pouls pédieux` (AMBOSS-20)  ⟷  `Palpation processus épineux` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Problèmes urinaires` (AMBOSS-20)  ⟷  `Symptômes urinaires` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (AZYGOS-29, German-83)  ⟷  `Progression` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Présence de douleur` (German-83)  ⟷  `Type de douleur` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Questions du patient` (German-83)  ⟷  `Éducation du patient` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sensibilité MI` (AZYGOS-29)  ⟷  `Sensibilité tactile` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sensibilité MI` (AZYGOS-29)  ⟷  `Sensibilité thermique` (German-83, RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sensibilité MI` (AZYGOS-29)  ⟷  `Sensibilité vibratoire` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sensibilité MS` (AZYGOS-29)  ⟷  `Sensibilité tactile` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sensibilité MS` (AZYGOS-29)  ⟷  `Sensibilité thermique` (German-83, RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signe de Babinski` (AMBOSS-20)  ⟷  `Signe de Babinski bilatéral` (RESCOS-30) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles de l’équilibre` (AZYGOS-29)  ⟷  `Troubles de mémoire` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles sphinctériens` (RESCOS-30)  ⟷  `Troubles vésico-sphinctériens` (AZYGOS-29) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles trophiques` (RESCOS-30)  ⟷  `Troubles visuels` (German-83) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Variations journalières` (AZYGOS-29)  ⟷  `Variations pondérales` (AMBOSS-20) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Activités professionnelles` (RESCOS-30)  ⟷  `Positions profesionnelles` (RESCOS-30) — **RESCOS-30, section « a »** distingue ces deux items
- ⛔ `Acuité visuelle (N. opticus II)` (AZYGOS-29)  ⟷  `Champs visuels (N. opticus II)` (AZYGOS-29) — **AZYGOS-29, section « e »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-20)  ⟷  `Antécédents familiaux` (AMBOSS-20, AZYGOS-29, German-83) — **AMBOSS-20, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-20)  ⟷  `Antécédents médicaux` (AMBOSS-20) — **AMBOSS-20, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-20, AZYGOS-29, German-83)  ⟷  `Antécédents médicaux` (AMBOSS-20) — **AMBOSS-20, section « a »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (AMBOSS-20, German-83)  ⟷  `Auscultation des carotides` (German-83) — **German-83, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (AMBOSS-20, German-83)  ⟷  `Palpation cardiaque` (German-83) — **German-83, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-20)  ⟷  `Inspection de l'abdomen` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-20)  ⟷  `Palpation de l'abdomen` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-20)  ⟷  `Percussion de l'abdomen` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Constant/intermittent` (AMBOSS-20)  ⟷  `Progression/constant/intermittent` (AMBOSS-20) — **AMBOSS-20, section « a »** distingue ces deux items
- ⛔ `Coordination MI` (AZYGOS-29)  ⟷  `Coordination MS` (AZYGOS-29) — **AZYGOS-29, section « e »** distingue ces deux items
- ⛔ `Digestif` (German-83)  ⟷  `Digestion` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Discussion sur la consommation d'alcool` (German-83)  ⟷  `Réduction de la consommation d'alcool` (German-83) — **German-83, section « m »** distingue ces deux items
- ⛔ `Dorsiflexion du pied` (RESCOS-30)  ⟷  `Éversion du pied` (RESCOS-30) — **RESCOS-30, section « e »** distingue ces deux items
- ⛔ `Examen ciblé de l'état mental` (AMBOSS-20)  ⟷  `Examen ciblé de la marche` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Examen ciblé de l'état mental` (AMBOSS-20)  ⟷  `Examen ciblé de la sensibilité` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Examen ciblé de la marche` (AMBOSS-20)  ⟷  `Examen ciblé de la sensibilité` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Examens complémentaires` (German-83)  ⟷  `Examens complémentaires additionnels` (AMBOSS-20, German-83) — **German-83, section « m »** distingue ces deux items
- ⛔ `Examens complémentaires additionnels` (AMBOSS-20, German-83)  ⟷  `Examens complémentaires de première intention` (AMBOSS-20) — **AMBOSS-20, section « m »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-20, German-83)  ⟷  `Facteurs améliorants` (AMBOSS-20, German-83) — **AMBOSS-20, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-20, German-83)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-29) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (AMBOSS-20, German-83)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-29) — **AZYGOS-29, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (AMBOSS-20, German-83)  ⟷  `Facteurs modulants` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (AMBOSS-20, German-83)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-29) — **AMBOSS-20, section « a »** distingue ces deux items
- ⛔ `Flexion plantaire` (RESCOS-30)  ⟷  `Réflexe cutané plantaire` (RESCOS-30) — **RESCOS-30, section « e »** distingue ces deux items
- ⛔ `Flexion plantaire` (RESCOS-30)  ⟷  `Réflexe médio-plantaire` (RESCOS-30) — **RESCOS-30, section « e »** distingue ces deux items
- ⛔ `Infections antérieures` (AZYGOS-29)  ⟷  `Opérations antérieures` (AZYGOS-29) — **AZYGOS-29, section « a »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-20)  ⟷  `Inspection des mains` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-20)  ⟷  `Palpation de l'abdomen` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-20)  ⟷  `Percussion de l'abdomen` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Inspection de la plaie` (German-83)  ⟷  `Inspection des pieds` (German-83) — **German-83, section « e »** distingue ces deux items
- ⛔ `Inspection des conjonctives` (AMBOSS-20)  ⟷  `Inspection des mains` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Inspection des conjonctives` (AMBOSS-20)  ⟷  `Inspection des sclères` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Inspection des mains` (AMBOSS-20)  ⟷  `Inspection des sclères` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Motricité MI` (AZYGOS-29)  ⟷  `Motricité MS` (AZYGOS-29) — **AZYGOS-29, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-20)  ⟷  `Percussion de l'abdomen` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Pollakiurie` (German-83)  ⟷  `Polyurie` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Recherche d'œdème déclive` (AMBOSS-20)  ⟷  `Recherche de matité déclive` (AMBOSS-20) — **AMBOSS-20, section « e »** distingue ces deux items
- ⛔ `Revue des systèmes - Digestif` (German-83)  ⟷  `Revue des systèmes - Locomoteur` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Revue des systèmes - Digestif` (German-83)  ⟷  `Revue des systèmes - Neurologique` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Revue des systèmes - Digestif` (German-83)  ⟷  `Revue des systèmes - Respiratoire` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Revue des systèmes - Locomoteur` (German-83)  ⟷  `Revue des systèmes - Neurologique` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Revue des systèmes - Neurologique` (German-83)  ⟷  `Revue des systèmes - Respiratoire` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Réflexe achilléen` (AZYGOS-29, RESCOS-30)  ⟷  `Réflexes achilléens` (German-83) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Réflexe bicipital` (AZYGOS-29)  ⟷  `Réflexe tricipital` (AZYGOS-29) — **AZYGOS-29, section « e »** distingue ces deux items
- ⛔ `Réflexe cutané plantaire` (RESCOS-30)  ⟷  `Réflexe médio-plantaire` (RESCOS-30) — **RESCOS-30, section « e »** distingue ces deux items
- ⛔ `Réflexe rotulien` (AZYGOS-29, RESCOS-30)  ⟷  `Réflexes rotuliens` (German-83) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Réflexes MI` (AZYGOS-29)  ⟷  `Réflexes MS` (AZYGOS-29) — **AZYGOS-29, section « e »** distingue ces deux items
- ⛔ `Sensibilité MI` (AZYGOS-29)  ⟷  `Sensibilité MS` (AZYGOS-29) — **AZYGOS-29, section « e »** distingue ces deux items
- ⛔ `Sensibilité tactile` (RESCOS-30)  ⟷  `Sensibilité thermique` (German-83, RESCOS-30) — **RESCOS-30, section « e »** distingue ces deux items
- ⛔ `Sensibilité tactile` (RESCOS-30)  ⟷  `Sensibilité vibratoire` (RESCOS-30) — **RESCOS-30, section « e »** distingue ces deux items
- ⛔ `Symptômes cardiovasculaires` (German-83)  ⟷  `Symptômes urinaires` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Symptômes urinaires` (German-83)  ⟷  `Symptômes visuels` (German-83) — **German-83, section « a »** distingue ces deux items
- ⛔ `Tonus musculaire` (AZYGOS-29)  ⟷  `Tonus musculaire MS` (AZYGOS-29) — **AZYGOS-29, section « e »** distingue ces deux items
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-29)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-29) — **AZYGOS-29, section « a »** distingue ces deux items

## Otalgie — 2 cas · 9 à juger (1 de forme, 8 de contenu), 9 ⚠️, 13 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Auscultation cardio-pulmonaire` (German-65)  ⟷  `Auscultation cardiopulmonaire` (German-28)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Conduit auditif externe` (German-65)  ⟷  `État du conduit auditif externe` (German-28)
- `Symptômes auriculaires associés` (German-65)  ⟷  `Symptômes auriculaires spécifiques` (German-28)
- `Information sur les complications possibles` (German-65)  ⟷  `L'étudiant informe sur les complications possibles` (German-28)
- `Antécédents médicaux` (German-65)  ⟷  `Antécédents médicaux généraux` (German-28)
- `Palpation des aires ganglionnaires` (German-28)  ⟷  `Palpation ganglionnaire` (German-65)
- `Douleur à la traction du pavillon` (German-28)  ⟷  `Traction du pavillon` (German-65)
- `Douleur à la pression du tragus` (German-28)  ⟷  `Pression du tragus` (German-65)
- `Symptômes associés` (German-28)  ⟷  `Symptômes auriculaires associés` (German-65)

- ⚠️ `Ganglions pré-auriculaires` (German-65)  ⟷  `Ganglions sous-mandibulaires` (German-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ganglions pré-auriculaires` (German-65)  ⟷  `Région rétro-auriculaire` (German-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ganglions rétro-auriculaires` (German-28, German-65)  ⟷  `Tuméfaction rétro-auriculaire` (German-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisations` (German-65)  ⟷  `Hospitalisations antérieures` (German-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Oropharynx` (German-65)  ⟷  `Pharynx` (German-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Paralysie faciale (par œdème du nerf)` (German-65)  ⟷  `Paralysie faciale périphérique (par œdème)` (German-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Région rétro-auriculaire` (German-28)  ⟷  `Tuméfaction rétro-auriculaire` (German-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccin pneumocoque à jour` (German-28)  ⟷  `Vaccination antipneumococcique à jour` (German-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `État de santé de la famille` (German-28)  ⟷  `État de santé familial` (German-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Auscultation cardiaque` (German-28, German-65)  ⟷  `Auscultation cardio-pulmonaire` (German-65) — **German-65, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (German-28, German-65)  ⟷  `Auscultation cardiopulmonaire` (German-28) — **German-28, section « e »** distingue ces deux items
- ⛔ `Auscultation cardio-pulmonaire` (German-65)  ⟷  `Auscultation pulmonaire` (German-28, German-65) — **German-65, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiopulmonaire` (German-28)  ⟷  `Auscultation pulmonaire` (German-28, German-65) — **German-28, section « e »** distingue ces deux items
- ⛔ `Autres symptômes` (German-28)  ⟷  `Début des symptômes` (German-28) — **German-28, section « a »** distingue ces deux items
- ⛔ `Ganglions pré-auriculaires` (German-65)  ⟷  `Ganglions rétro-auriculaires` (German-28, German-65) — **German-65, section « e »** distingue ces deux items
- ⛔ `Ganglions pré-auriculaires` (German-65)  ⟷  `Palpation auriculaire` (German-28, German-65) — **German-65, section « e »** distingue ces deux items
- ⛔ `Ganglions rétro-auriculaires` (German-28, German-65)  ⟷  `Ganglions sous-mandibulaires` (German-28) — **German-28, section « e »** distingue ces deux items
- ⛔ `Ganglions rétro-auriculaires` (German-28, German-65)  ⟷  `Région rétro-auriculaire` (German-28) — **German-28, section « e »** distingue ces deux items
- ⛔ `Mastoïdite (tuméfaction rétro-auriculaire)` (German-65)  ⟷  `Tuméfaction rétro-auriculaire` (German-65) — **German-65, section « m »** distingue ces deux items
- ⛔ `Palpation auriculaire` (German-28, German-65)  ⟷  `Palpation ganglionnaire` (German-65) — **German-65, section « e »** distingue ces deux items
- ⛔ `Palpation auriculaire` (German-28, German-65)  ⟷  `Pavillon auriculaire` (German-28) — **German-28, section « e »** distingue ces deux items
- ⛔ `Recherche d'hépatomégalie` (German-28)  ⟷  `Recherche de splénomégalie` (German-28) — **German-28, section « e »** distingue ces deux items

## Palpitations — 3 cas · 12 à juger (1 de forme, 11 de contenu), 34 ⚠️, 25 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Anamnèse par systèmes` (German-66)  ⟷  `Anamnèse systémique` (German-7)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Caractérisation du rythme cardiaque` (German-66)  ⟷  `Caractéristiques du rythme cardiaque` (German-74)
- `Examen pulmonaire` (German-66)  ⟷  `Examen pulmonaire complet` (German-74)
- `Examens complémentaires` (German-66)  ⟷  `Imagerie et examens complémentaires` (German-74)
- `Prise en charge immédiate` (German-74)  ⟷  `Prise en charge non médicamenteuse` (German-66)
- `Examen cardiovasculaire` (German-66)  ⟷  `Palpation cardiovasculaire` (German-74)
- `Traitement médicamenteux` (German-66, German-7)  ⟷  `Traitement médicamenteux au long cours` (German-74)
- `Examen cardiovasculaire` (German-66)  ⟷  `Inspection cardiovasculaire` (German-74)
- `Examen cutané` (German-7)  ⟷  `Examen cutanéo-muqueux` (German-74)
- `Auscultation cardiaque` (German-74)  ⟷  `Status cardiaque` (German-7)
- `Antécédents cardiovasculaires personnels` (German-74)  ⟷  `Antécédents médicaux personnels` (German-66)
- `Habitudes de vie` (German-74)  ⟷  `Habitudes de vie et toxiques` (German-66)

- ⚠️ `Activité physique` (German-74)  ⟷  `Activité physique et loisirs` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Allergies connues` (German-74)  ⟷  `Pathologies connues` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Artériopathie périphérique` (German-7)  ⟷  `Cardiopathie ischémique` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bruits cardiaques` (German-74)  ⟷  `Rythme cardiaque` (German-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bruits cardiaques` (German-74)  ⟷  `Status cardiaque` (German-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Café` (German-66)  ⟷  `Caféine` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Durée des épisodes` (German-66)  ⟷  `Fréquence des épisodes` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (German-66)  ⟷  `Examens complémentaires` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen thyroïdien` (German-66, German-7)  ⟷  `Thyroïdien` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen thyroïdien` (German-66, German-7)  ⟷  `Volume thyroïdien` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence des épisodes` (German-74)  ⟷  `Fréquence respiratoire` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence estimée` (German-74)  ⟷  `Fréquence respiratoire` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Habitudes alimentaires` (German-7)  ⟷  `Habitudes alimentaires et hydratation` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-74)  ⟷  `Tension artérielle` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hyperthyroïdie` (German-66)  ⟷  `Signes d'hyperthyroïdie` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hyperthyroïdie` (German-66)  ⟷  `TSH (hyperthyroïdie)` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hyperthyroïdie` (German-66)  ⟷  `Thyroïde` (German-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hyperthyroïdie` (German-66)  ⟷  `Thyroïdien` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Interventions antérieures` (German-74)  ⟷  `Interventions chirurgicales` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies thyroïdiennes` (German-7)  ⟷  `Palpation thyroïdienne` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies thyroïdiennes` (German-7)  ⟷  `Pathologie thyroïdienne` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Matité cardiaque` (German-74)  ⟷  `Status cardiaque` (German-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation cardiovasculaire` (German-74)  ⟷  `Palpation précordiale` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation thyroïdienne` (German-74)  ⟷  `Pathologie thyroïdienne` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perte de poids` (German-74)  ⟷  `Prise de poids` (German-7) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Prise de poids` (German-7)  ⟷  `Prise de poids récente` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Sensation de chaleur` (German-66)  ⟷  `Sensations de pauses` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes d'hyperthyroïdie` (German-74)  ⟷  `Signes d'hypothyroïdie` (German-7) — **antonymes présumés** (hyper / hypo) : aucune grille ne les porte ensemble, donc la propriété 8 n'a pas de témoin. **L'entrée mordrait — à vérifier à la main.**
- ⚠️ `Signes d'hyperthyroïdie` (German-74)  ⟷  `TSH (hyperthyroïdie)` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes d'insuffisance cardiaque` (German-74)  ⟷  `Signes périphériques d'insuffisance cardiaque` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Thyroïde` (German-7)  ⟷  `Thyroïdien` (German-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Thyroïdien` (German-66)  ⟷  `Volume thyroïdien` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vertiges/Collapsus` (German-7)  ⟷  `Vertiges/malaises` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Échocardiographie si anomalie ECG` (German-66)  ⟷  `Échocardiographie transthoracique` (German-74) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Allergies médicamenteuses` (German-74)  ⟷  `Autres médicaments` (German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Anamnèse familiale` (German-66, German-7)  ⟷  `Anamnèse sociale` (German-66, German-7) — **German-66, section « a »** distingue ces deux items
- ⛔ `Anesthésies` (German-74)  ⟷  `Asthénie` (German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Antécédents cardiovasculaires personnels` (German-74)  ⟷  `Antécédents familiaux cardiovasculaires` (German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Auscultation antérieure systématique` (German-66)  ⟷  `Auscultation postérieure systématique` (German-66) — **German-66, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (German-74)  ⟷  `Auscultation thyroïdienne` (German-74) — **German-74, section « e »** distingue ces deux items
- ⛔ `Auscultation thyroïdienne` (German-74)  ⟷  `Palpation thyroïdienne` (German-74) — **German-74, section « e »** distingue ces deux items
- ⛔ `Bruits cardiaques` (German-74)  ⟷  `Matité cardiaque` (German-74) — **German-74, section « e »** distingue ces deux items
- ⛔ `Consommation actuelle` (German-74)  ⟷  `Consommation d'alcool` (German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Consommation d'alcool` (German-74)  ⟷  `Consommation de café` (German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Diabète, hypertension` (German-7)  ⟷  `Hypertension` (German-7) — **German-7, section « a »** distingue ces deux items
- ⛔ `Durée actuelle` (German-74)  ⟷  `Durée habituelle` (German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Durée habituelle` (German-74)  ⟷  `Fatigue inhabituelle` (German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Examens biologiques - Bilan pré-thérapeutique` (German-74)  ⟷  `Examens biologiques - Bilan étiologique` (German-74) — **German-74, section « m »** distingue ces deux items
- ⛔ `Frottement péricardique` (German-74)  ⟷  `Épanchement péricardique` (German-74) — **German-74, section « e »** distingue ces deux items
- ⛔ `Inspection cardiovasculaire` (German-74)  ⟷  `Palpation cardiovasculaire` (German-74) — **German-74, section « e »** distingue ces deux items
- ⛔ `Interventions antérieures` (German-74)  ⟷  `Réactions antérieures` (German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Mort subite` (German-74)  ⟷  `Morts subites` (German-7) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Parasympatholytiques : Atropine 0,5-1 mg IV` (German-7)  ⟷  `Sympathomimétiques : Adrénaline 0,1 mg IV` (German-7) — **German-7, section « m »** distingue ces deux items
- ⛔ `Pouls périphérique` (German-74)  ⟷  `Œdèmes périphériques` (German-74) — **German-74, section « e »** distingue ces deux items
- ⛔ `Radiographie thoracique` (German-74)  ⟷  `Échocardiographie transthoracique` (German-74) — **German-74, section « m »** distingue ces deux items
- ⛔ `Recherche de goitre` (German-66)  ⟷  `Recherche de nodules` (German-66) — **German-66, section « e »** distingue ces deux items
- ⛔ `Réactions antérieures` (German-74)  ⟷  `Épisodes antérieurs` (German-7, German-74) — **German-74, section « a »** distingue ces deux items
- ⛔ `Souffle thyroïdien` (German-74)  ⟷  `Volume thyroïdien` (German-74) — **German-74, section « e »** distingue ces deux items
- ⛔ `Troubles du rythme` (German-74)  ⟷  `Troubles du rythme connus` (German-74) — **German-74, section « a »** distingue ces deux items

## Parésie - AVC — 4 cas · 4 à juger (0 de forme, 4 de contenu), 10 ⚠️, 16 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Symptômes similaires par le passé` (RESCOS-52)  ⟷  `Épisodes similaires par le passé` (RESCOS-70b)
- `Examens complémentaires` (RESCOS-70)  ⟷  `Examens complémentaires en urgence` (RESCOS-53)
- `Caractérisation de l'épisode` (RESCOS-70b)  ⟷  `Caractérisation de l'épisode neurologique aigu` (RESCOS-53)
- `Examen des autres paires crâniennes` (RESCOS-70)  ⟷  `Examen des nerfs crâniens` (RESCOS-53)

- ⚠️ `Antiagrégants plaquettaires` (RESCOS-53)  ⟷  `Antiagrégation plaquettaire` (RESCOS-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cinétique d'installation` (RESCOS-70b)  ⟷  `Mode d'installation` (RESCOS-53, RESCOS-70) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Circonstance de survenue` (RESCOS-52)  ⟷  `Circonstances de découverte` (RESCOS-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Circonstances de découverte` (RESCOS-53)  ⟷  `Circonstances de survenue` (RESCOS-70b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contrôle facteurs de risque` (RESCOS-53)  ⟷  `Terrain et facteurs de risque` (RESCOS-70) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Corticothérapie orale précoce (moins de 72 h)` (RESCOS-70b)  ⟷  `Corticothérapie précoce (dans les 72 h)` (RESCOS-70) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diabète ou hypertension artérielle` (RESCOS-70)  ⟷  `Hypertension artérielle` (RESCOS-53) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen de la sensibilité` (RESCOS-53)  ⟷  `Perte de sensibilité` (RESCOS-52) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pathologies carotidiennes` (RESCOS-53)  ⟷  `Échographie carotidienne` (RESCOS-52) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Symptômes associés` (RESCOS-70b)  ⟷  `Symptômes oculaires` (RESCOS-70) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Abduction` (RESCOS-52)  ⟷  `Adduction` (RESCOS-52) — **RESCOS-52, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (RESCOS-53)  ⟷  `Auscultation carotidienne` (RESCOS-53) — **RESCOS-53, section « e »** distingue ces deux items
- ⛔ `Circonstance de survenue` (RESCOS-52)  ⟷  `Circonstances de survenue` (RESCOS-70b) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Examen de la motricité` (RESCOS-53)  ⟷  `Examen de la sensibilité` (RESCOS-53) — **RESCOS-53, section « e »** distingue ces deux items
- ⛔ `Froncer les sourcils` (RESCOS-70b)  ⟷  `Lever les sourcils` (RESCOS-70b) — **RESCOS-70b, section « e »** distingue ces deux items
- ⛔ `Inspection de la conjonctive et de la cornée` (RESCOS-70b)  ⟷  `Inspection de la cornée et de la conjonctive` (RESCOS-70) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Motricité des membres inférieurs` (RESCOS-52)  ⟷  `Motricité des membres supérieurs` (RESCOS-52) — **RESCOS-52, section « e »** distingue ces deux items
- ⛔ `Présence de douleurs` (RESCOS-52)  ⟷  `Présence de la douleur` (RESCOS-70) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Réflexe bicipital des deux côtés` (RESCOS-52)  ⟷  `Réflexe stylo-radial des deux côtés` (RESCOS-52) — **RESCOS-52, section « e »** distingue ces deux items
- ⛔ `Réflexe bicipital des deux côtés` (RESCOS-52)  ⟷  `Réflexe tricipital des deux côtés` (RESCOS-52) — **RESCOS-52, section « e »** distingue ces deux items
- ⛔ `Réflexe stylo-radial des deux côtés` (RESCOS-52)  ⟷  `Réflexe tricipital des deux côtés` (RESCOS-52) — **RESCOS-52, section « e »** distingue ces deux items
- ⛔ `Réflexes ostéo-tendineux des membres inférieurs (des deux côtés)` (RESCOS-52)  ⟷  `Réflexes ostéo-tendineux des membres supérieurs` (RESCOS-52) — **RESCOS-52, section « e »** distingue ces deux items
- ⛔ `Sensibilité des membres inférieurs - évalue globalement la sensibilité sur tous les dermatomes` (RESCOS-52)  ⟷  `Sensibilité des membres supérieurs - évalue globalement la sensibilité sur tous les dermatomes` (RESCOS-52) — **RESCOS-52, section « e »** distingue ces deux items
- ⛔ `Testing du territoire facial inférieur` (RESCOS-70)  ⟷  `Testing du territoire facial supérieur` (RESCOS-70) — **RESCOS-70, section « e »** distingue ces deux items
- ⛔ `Trouble du goût` (RESCOS-70)  ⟷  `Trouble du langage` (RESCOS-70, RESCOS-70b) — **RESCOS-70, section « a »** distingue ces deux items
- ⛔ `Troubles de la conscience` (RESCOS-53)  ⟷  `Troubles de la parole` (RESCOS-53) — **RESCOS-53, section « a »** distingue ces deux items

## Rectorragies & Hémorragie Digestive Basse — 3 cas · 5 à juger (0 de forme, 5 de contenu), 6 ⚠️, 15 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Effectué dans les 4 quadrants` (RESCOS-58b)  ⟷  `Effectué dans les 4 quadrants = oui` (RESCOS-58)
- `Antécédents chirurgicaux` (AMBOSS-11)  ⟷  `Antécédents médicaux-chirurgicaux` (RESCOS-58, RESCOS-58b)
- `Palpation profonde` (RESCOS-58b)  ⟷  `Palpation profonde bimanuelle` (RESCOS-58)
- `Antécédents médicaux` (AMBOSS-11)  ⟷  `Antécédents médicaux-chirurgicaux` (RESCOS-58, RESCOS-58b)
- `1er épisode` (RESCOS-58)  ⟷  `Première épisode` (RESCOS-58b)

- ⚠️ `Auscultation abdominale` (RESCOS-58)  ⟷  `Auscultation de l'abdomen` (AMBOSS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Endoscopie digestive / CT abdominal` (RESCOS-58b)  ⟷  `Endoscopie digestive haute` (AMBOSS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cutané` (AMBOSS-11)  ⟷  `Examen rectal` (AMBOSS-11) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hémorroïdes ou autre problème proctologique (fissure)` (RESCOS-58)  ⟷  `Hémorroïdes ou autre problème proctologique (fissure, etc.)` (RESCOS-58b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nausées/vomissements` (AMBOSS-11)  ⟷  `Vomissements` (RESCOS-58, RESCOS-58b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Souffles vasculaires (aorte, a. iliaques et a. rénales)` (RESCOS-58)  ⟷  `Souffles vasculaires (aorte, artères iliaques et artères rénales)` (RESCOS-58b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-11)  ⟷  `Antécédents familiaux` (AMBOSS-11) — **AMBOSS-11, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-11)  ⟷  `Antécédents médicaux` (AMBOSS-11) — **AMBOSS-11, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-11)  ⟷  `Antécédents médicaux` (AMBOSS-11) — **AMBOSS-11, section « a »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-11)  ⟷  `Inspection de l'abdomen` (AMBOSS-11) — **AMBOSS-11, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-11)  ⟷  `Palpation de l'abdomen` (AMBOSS-11) — **AMBOSS-11, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-11)  ⟷  `Percussion de l'abdomen` (AMBOSS-11) — **AMBOSS-11, section « e »** distingue ces deux items
- ⛔ `Bruits dans les 4 quadrants` (RESCOS-58, RESCOS-58b)  ⟷  `Effectué dans les 4 quadrants` (RESCOS-58b) — **RESCOS-58b, section « e »** distingue ces deux items
- ⛔ `Constant/intermittent` (AMBOSS-11)  ⟷  `Progression/constant/intermittent` (AMBOSS-11) — **AMBOSS-11, section « a »** distingue ces deux items
- ⛔ `Endoscopie digestive / CT abdominal` (RESCOS-58b)  ⟷  `Propose une endoscopie digestive, propose un CT abdominal` (RESCOS-58b) — **RESCOS-58b, section « m »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-11)  ⟷  `Facteurs améliorants` (AMBOSS-11) — **AMBOSS-11, section « a »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-11)  ⟷  `Palpation de l'abdomen` (AMBOSS-11) — **AMBOSS-11, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-11)  ⟷  `Percussion de l'abdomen` (AMBOSS-11) — **AMBOSS-11, section « e »** distingue ces deux items
- ⛔ `Médicaments` (AMBOSS-11, RESCOS-58, RESCOS-58b)  ⟷  `Médicaments actuels` (AMBOSS-11) — **AMBOSS-11, section « a »** distingue ces deux items
- ⛔ `Non = pas ou incomplètement effectué` (RESCOS-58)  ⟷  `Pas ou incomplètement effectué = non` (RESCOS-58) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Palpation de l'abdomen` (AMBOSS-11)  ⟷  `Percussion de l'abdomen` (AMBOSS-11) — **AMBOSS-11, section « e »** distingue ces deux items

## Saignement Vaginal Anormal — 2 cas · 1 à juger (0 de forme, 1 de contenu), 4 ⚠️, 13 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Symptômes associés` (AMBOSS-4)  ⟷  `Symptômes vaginaux associés` (AZYGOS-44)

- ⚠️ `Facteurs aggravants` (AMBOSS-4)  ⟷  `Facteurs aggravants / atténuants` (AZYGOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Frottis cervical` (AZYGOS-44)  ⟷  `Frottis cervical et test HPV` (AMBOSS-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection de l'abdomen` (AMBOSS-4)  ⟷  `Inspection de la vulve` (AZYGOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation` (AZYGOS-44)  ⟷  `Palpitations` (AZYGOS-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-4, AZYGOS-44)  ⟷  `Antécédents familiaux` (AMBOSS-4) — **AMBOSS-4, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-4, AZYGOS-44)  ⟷  `Antécédents médicaux` (AMBOSS-4, AZYGOS-44) — **AMBOSS-4, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-4)  ⟷  `Antécédents médicaux` (AMBOSS-4, AZYGOS-44) — **AMBOSS-4, section « a »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-4)  ⟷  `Inspection de l'abdomen` (AMBOSS-4) — **AMBOSS-4, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-4)  ⟷  `Palpation de l'abdomen` (AMBOSS-4) — **AMBOSS-4, section « e »** distingue ces deux items
- ⛔ `Auscultation de l'abdomen` (AMBOSS-4)  ⟷  `Percussion de l'abdomen` (AMBOSS-4) — **AMBOSS-4, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-4)  ⟷  `Facteurs améliorants` (AMBOSS-4) — **AMBOSS-4, section « a »** distingue ces deux items
- ⛔ `IST antérieures` (AMBOSS-4)  ⟷  `Épisodes antérieurs` (AMBOSS-4) — **AMBOSS-4, section « a »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-4)  ⟷  `Palpation de l'abdomen` (AMBOSS-4) — **AMBOSS-4, section « e »** distingue ces deux items
- ⛔ `Inspection de l'abdomen` (AMBOSS-4)  ⟷  `Percussion de l'abdomen` (AMBOSS-4) — **AMBOSS-4, section « e »** distingue ces deux items
- ⛔ `Palpation de l'abdomen` (AMBOSS-4)  ⟷  `Percussion de l'abdomen` (AMBOSS-4) — **AMBOSS-4, section « e »** distingue ces deux items
- ⛔ `Pertes vaginales` (AMBOSS-4, AZYGOS-44)  ⟷  `Sécheresse vaginale` (AMBOSS-4) — **AMBOSS-4, section « a »** distingue ces deux items
- ⛔ `Qualité` (AZYGOS-44)  ⟷  `Quantité` (AZYGOS-44) — **AZYGOS-44, section « a »** distingue ces deux items

## Syncope & Perte de Connaissance — 6 cas · 29 à juger (1 de forme, 28 de contenu), 64 ⚠️, 37 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Examens complémentaires - Cardiologie` (German-60)  ⟷  `Examens complémentaires cardiologiques` (German-61)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Examens complémentaires - Biologie` (German-60)  ⟷  `Examens complémentaires cardiologiques` (German-61)
- `Symptômes cardiovasculaires` (German-60)  ⟷  `Symptômes cardiovasculaires associés` (German-61)
- `Recherche de signes d'anémie` (RESCOS-50)  ⟷  `Recherche de signes d'hypovolémie` (German-60)
- `Examen cardiovasculaire` (German-60, RESCOS-50)  ⟷  `Examen vasculaire` (German-61)
- `Examen neurologique de base` (RESCOS-50)  ⟷  `Examen neurologique de dépistage` (German-60, German-61)
- `Examen cardio-pulmonaire` (AZYGOS-38, German-41)  ⟷  `Examen pulmonaire` (German-60, German-61)
- `Antécédents médicaux autres` (German-60)  ⟷  `Antécédents médicaux personnels` (German-41, German-61)
- `Recherche de signes d'insuffisance cardiaque` (German-61, RESCOS-50)  ⟷  `Signes d'insuffisance cardiaque` (German-60)
- `Auscultation carotidienne` (German-41)  ⟷  `Auscultation des carotides` (AZYGOS-38)
- `Phase post-critique` (German-41)  ⟷  `État post-critique` (RESCOS-50)
- `Examen cardio-pulmonaire` (AZYGOS-38, German-41)  ⟷  `Examen cardiovasculaire` (German-60, RESCOS-50)
- `Symptômes cardiaques` (AZYGOS-38)  ⟷  `Symptômes cardiovasculaires` (German-60)
- `Auscultation bilatérale` (German-61)  ⟷  `Auscultation pulmonaire bilatérale` (German-60)
- `Éducation du patient et prévention` (German-60)  ⟷  `Éducation et prévention` (German-61)
- `Examens complémentaires cardiologiques` (German-61)  ⟷  `Examens complémentaires proposés` (German-41)
- `Organisation du suivi` (German-61)  ⟷  `Planification du suivi` (German-60)
- `Examens complémentaires - Biologie` (German-60)  ⟷  `Examens complémentaires proposés` (German-41)
- `Examens complémentaires - Cardiologie` (German-60)  ⟷  `Examens complémentaires proposés` (German-41)
- `Question d'entrée ouverte - Symptôme principal` (German-61)  ⟷  `Question ouverte initiale → symptôme principal` (German-41)
- `Examens complémentaires proposés` (German-41)  ⟷  `Propose des examens complémentaires appropriés` (RESCOS-50)
- `Recherche de râles` (German-60)  ⟷  `Recherche de râles crépitants` (German-61)
- `Examens complémentaires - Monitoring` (German-60)  ⟷  `Examens complémentaires proposés` (German-41)
- `Constantes vitales et état général` (RESCOS-50)  ⟷  `Signes vitaux et état général` (German-61)
- `Symptômes cardiovasculaires` (German-60)  ⟷  `Symptômes neurologiques et cardiovasculaires` (German-41)
- `Symptômes cardiaques` (AZYGOS-38)  ⟷  `Symptômes neurologiques` (German-61)
- `Symptômes neurovégétatifs associés` (German-60)  ⟷  `Symptômes végétatifs` (German-41)
- `Symptômes associés` (AZYGOS-38, RESCOS-50)  ⟷  `Symptômes associés - Infectieux` (German-41)
- `Organisation du suivi` (German-61)  ⟷  `Orientation et suivi` (German-41)

- ⚠️ `Agitation` (German-41)  ⟷  `Alimentation` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Agitation` (German-41)  ⟷  `Palpitations` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation` (RESCOS-50)  ⟷  `Palpitations` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Allergies médicamenteuses` (German-61)  ⟷  `Révision médicamenteuse` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (German-60)  ⟷  `Examen cardiovasculaire` (German-60, RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (German-60)  ⟷  `Maladies cardiovasculaires` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents neurologiques` (AZYGOS-38)  ⟷  `Maladies neurologiques` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (AZYGOS-38, German-41)  ⟷  `Auscultation cardiaque (4 foyers)` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque` (AZYGOS-38, German-41)  ⟷  `Auscultation des bruits cardiaques` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque (4 foyers)` (German-60)  ⟷  `Auscultation carotidienne (souffles)` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation carotidienne` (German-41)  ⟷  `Auscultation carotidienne (souffles)` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation de min 4 plages pulmonaires` (RESCOS-49)  ⟷  `Auscultation pulmonaire` (German-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation des bruits cardiaques` (German-61)  ⟷  `Auscultation des carotides` (AZYGOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation pulmonaire` (German-41)  ⟷  `Auscultation pulmonaire bilatérale` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Avis neurologique` (AZYGOS-38)  ⟷  `Maladies neurologiques` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bilan de base` (AZYGOS-38)  ⟷  `Bilan de syncope` (AZYGOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT cérébral` (AZYGOS-38)  ⟷  `Tumeur cérébrale` (German-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractérisation de la perte de connaissance` (RESCOS-50)  ⟷  `Durée de la perte de connaissance` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Circonstance du malaise` (RESCOS-49)  ⟷  `Circonstances similaires` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cortisol (insuffisance surrénalienne)` (German-60)  ⟷  `Signes d'insuffisance surrénalienne` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Demande la mesure de la tension artérielle` (RESCOS-49)  ⟷  `Mesure de la tension artérielle` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Documentation des symptômes` (German-60)  ⟷  `Durée des symptômes` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Durée de la crise` (German-41)  ⟷  `Pattern de la crise` (AZYGOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Déficit focal` (German-61)  ⟷  `Déficits focaux` (AZYGOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Déficit neurologique focal` (German-61)  ⟷  `Déficits neurologiques/AIT/AVC` (German-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Déficit neurologique focal` (German-61)  ⟷  `Recherche de déficit neurologique focal` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `ECG 12 dérivations` (RESCOS-50)  ⟷  `ECG 12 dérivations en urgence` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (German-60, RESCOS-50)  ⟷  `Maladies cardiovasculaires` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (German-60, RESCOS-50)  ⟷  `Symptômes cardiovasculaires` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence cardiaque` (German-61)  ⟷  `Fréquence cardiaque et pouls` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisation` (AZYGOS-38)  ⟷  `Localisation` (German-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-60)  ⟷  `Mesure de la tension artérielle` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-60)  ⟷  `Pression artérielle` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypotension orthostatique` (German-60)  ⟷  `Test d'hypotension orthostatique` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `IRM cérébrale` (AZYGOS-38)  ⟷  `Tumeur cérébrale` (German-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Insuffisance cardiaque` (German-60)  ⟷  `Signes d'insuffisance cardiaque` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies cardiaques` (German-61)  ⟷  `Maladies cardiaques connues` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies cardiaques` (German-61)  ⟷  `Maladies neurologiques` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies cardiovasculaires` (German-61)  ⟷  `Maladies cardiovasculaires familiales` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies cardiovasculaires` (German-61)  ⟷  `Symptômes cardiovasculaires` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies neurologiques` (German-60)  ⟷  `Symptômes neurologiques` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Mesure de la pression artérielle orthostatique` (German-60)  ⟷  `Mesure de la tension artérielle` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (German-41, German-60, German-61)  ⟷  `Médicaments habituels` (RESCOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Notion de perte de connaissance / syncope` (RESCOS-49)  ⟷  `Perte de connaissance complète` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Notion de traumatisme crânien` (RESCOS-49)  ⟷  `Traumatisme crânien` (German-41) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Orientation temporo-spatiale` (German-60)  ⟷  `Réorientation postictale` (AZYGOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation des pouls périphériques` (German-61, RESCOS-50)  ⟷  `Palpations des pouls périphériques aux 4 extrémités` (RESCOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perte d'urine/selles` (German-41)  ⟷  `Perte d'urines` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pression artérielle` (German-61)  ⟷  `Profession antérieure` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de pâleur` (German-60)  ⟷  `Recherche de pâleur cutanée` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de pâleur cutanée` (RESCOS-50)  ⟷  `Recherche de râles crépitants` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'anémie` (RESCOS-50)  ⟷  `Recherche des signes d'hémorragie` (RESCOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'hypotension orthostatique` (RESCOS-50)  ⟷  `Test d'hypotension orthostatique` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'hypovolémie` (German-60)  ⟷  `Recherche des signes d'hémorragie` (RESCOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Réflexes ostéo-tendineux` (German-41, German-60, German-61)  ⟷  `Réflexes ostéo-tendineux comparés` (AZYGOS-38) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Révision du traitement médicamenteux` (German-61)  ⟷  `Traitements médicamenteux` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes d'hypothyroïdie` (German-60)  ⟷  `TSH (hypothyroïdie)` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes d'insuffisance cardiaque` (German-60)  ⟷  `Signes d'insuffisance surrénalienne` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Test d'effort différé` (German-61)  ⟷  `Test d'effort si indiqué` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traitement médicamenteux spécifique` (German-60)  ⟷  `Traitements médicamenteux` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Troubles du rythme` (German-60)  ⟷  `Troubles du rythme familiaux` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `État d'hydratation` (RESCOS-50)  ⟷  `État d'hydratation cutanée` (German-60) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `État de conscience` (German-41)  ⟷  `État de conscience actuel` (German-61) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `État de conscience actuel` (German-61)  ⟷  `État de conscience et orientation` (RESCOS-50) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents cardiovasculaires` (German-60)  ⟷  `Symptômes cardiovasculaires` (German-60) — **German-60, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (German-61)  ⟷  `Antécédents familiaux` (German-60, German-61, RESCOS-50) — **AZYGOS-38, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (German-61)  ⟷  `Antécédents généraux` (AZYGOS-38) — **AZYGOS-38, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (German-60, German-61, RESCOS-50)  ⟷  `Antécédents généraux` (AZYGOS-38) — **AZYGOS-38, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (German-60, German-61, RESCOS-50)  ⟷  `Cancers familiaux` (AZYGOS-38) — **AZYGOS-38, section « a »** distingue ces deux items
- ⛔ `Aura auditive` (German-41)  ⟷  `Aura olfactive` (German-41) — **German-41, section « a »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (AZYGOS-38, German-41)  ⟷  `Auscultation carotidienne` (German-41) — **German-41, section « e »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (AZYGOS-38, German-41)  ⟷  `Auscultation des carotides` (AZYGOS-38) — **AZYGOS-38, section « e »** distingue ces deux items
- ⛔ `Autres pathologies chroniques` (German-60, German-61)  ⟷  `Autres pathologies héréditaires` (German-60) — **German-60, section « a »** distingue ces deux items
- ⛔ `CT cérébral` (AZYGOS-38)  ⟷  `IRM cérébrale` (AZYGOS-38) — **AZYGOS-38, section « m »** distingue ces deux items
- ⛔ `Circonstance du malaise` (RESCOS-49)  ⟷  `Circonstances du début du malaise` (RESCOS-49) — **RESCOS-49, section « a »** distingue ces deux items
- ⛔ `Drogue` (RESCOS-49)  ⟷  `Drogues` (AZYGOS-38, German-41) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Examen pulmonaire` (German-60, German-61)  ⟷  `Examen vasculaire` (German-61) — **German-61, section « e »** distingue ces deux items
- ⛔ `Examens complémentaires - Biologie` (German-60)  ⟷  `Examens complémentaires - Cardiologie` (German-60) — **German-60, section « m »** distingue ces deux items
- ⛔ `Examens complémentaires - Biologie` (German-60)  ⟷  `Examens complémentaires - Monitoring` (German-60) — **German-60, section « m »** distingue ces deux items
- ⛔ `Examens complémentaires - Cardiologie` (German-60)  ⟷  `Examens complémentaires - Monitoring` (German-60) — **German-60, section « m »** distingue ces deux items
- ⛔ `Hypertension artérielle` (German-60)  ⟷  `Hypotension familiale` (German-60) — **German-60, section « a »** distingue ces deux items
- ⛔ `Hétéro-anamnèse avec infirmier/-ère - anamnèse actuelle` (RESCOS-49)  ⟷  `Hétéroanamnèse avec infirmier/-ère - infos sur le/la patient·e` (RESCOS-49) — **RESCOS-49, section « a »** distingue ces deux items
- ⛔ `Interventions antérieures` (German-61)  ⟷  `Réactions antérieures` (German-61) — **German-61, section « a »** distingue ces deux items
- ⛔ `Maladies cardiaques` (German-61)  ⟷  `Maladies cardiovasculaires` (German-61) — **German-61, section « a »** distingue ces deux items
- ⛔ `Maladies respiratoires` (German-61)  ⟷  `Symptômes respiratoires` (German-61) — **German-61, section « a »** distingue ces deux items
- ⛔ `Membre inférieur` (AZYGOS-38)  ⟷  `Membre supérieur` (AZYGOS-38) — **AZYGOS-38, section « e »** distingue ces deux items
- ⛔ `Mesure en position couchée (après 5 min de repos)` (German-60)  ⟷  `Mesure en position debout (après 3 min)` (German-60) — **German-60, section « e »** distingue ces deux items
- ⛔ `Mesure en position debout (après 3 min)` (German-60)  ⟷  `Mesure en position debout (immédiatement)` (German-60) — **German-60, section « e »** distingue ces deux items
- ⛔ `Mesure ou demande la fréquence cardiaque` (RESCOS-49)  ⟷  `Mesure ou demande la fréquence respiratoire` (RESCOS-49) — **RESCOS-49, section « e »** distingue ces deux items
- ⛔ `Mère` (German-41)  ⟷  `Père` (German-41) — **German-41, section « a »** distingue ces deux items
- ⛔ `Recherche de pâleur` (German-60)  ⟷  `Recherche de râles` (German-60) — **German-60, section « e »** distingue ces deux items
- ⛔ `Recherche de pâleur` (German-60)  ⟷  `Recherche de souffles` (German-60, German-61) — **German-60, section « e »** distingue ces deux items
- ⛔ `Recherche de râles` (German-60)  ⟷  `Recherche de souffles` (German-60, German-61) — **German-60, section « e »** distingue ces deux items
- ⛔ `Recherche de signes d'anémie` (RESCOS-50)  ⟷  `Recherche de signes d'insuffisance cardiaque` (German-61, RESCOS-50) — **RESCOS-50, section « e »** distingue ces deux items
- ⛔ `Reflexes pupillaires` (RESCOS-50)  ⟷  `Réflexes pupillaires` (RESCOS-49) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Symptômes B` (AZYGOS-38, German-41, German-61)  ⟷  `Symptômes SNC` (AZYGOS-38) — **AZYGOS-38, section « a »** distingue ces deux items
- ⛔ `Symptômes SNC` (AZYGOS-38)  ⟷  `Symptômes associés` (AZYGOS-38, RESCOS-50) — **AZYGOS-38, section « a »** distingue ces deux items
- ⛔ `Tumeur cérébrale` (German-41)  ⟷  `Tumeur cérébrale familiale` (German-41) — **German-41, section « a »** distingue ces deux items
- ⛔ `Épreuve de maintien des bras` (AZYGOS-38)  ⟷  `Épreuve de maintien des jambes` (AZYGOS-38) — **AZYGOS-38, section « e »** distingue ces deux items
- ⛔ `Épreuve de maintien des bras` (AZYGOS-38)  ⟷  `Épreuves de maintien` (AZYGOS-38) — **AZYGOS-38, section « e »** distingue ces deux items
- ⛔ `Épreuve de maintien des jambes` (AZYGOS-38)  ⟷  `Épreuves de maintien` (AZYGOS-38) — **AZYGOS-38, section « e »** distingue ces deux items

## Syndrome Métabolique — 2 cas · 2 à juger (0 de forme, 2 de contenu), 7 ⚠️, 7 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Examens complémentaires` (German-64)  ⟷  `Examens complémentaires spécialisés` (AMBOSS-28)
- `Caractérisation de la prise de poids` (AMBOSS-28)  ⟷  `Caractérisation du surpoids` (German-64)

- ⚠️ `Examen cardiovasculaire` (AMBOSS-28, German-64)  ⟷  `Maladies cardiovasculaires` (German-64) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (German-64)  ⟷  `Examens complémentaires` (German-64) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-64)  ⟷  `Mesure de la tension artérielle` (German-64) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des membres inférieurs` (AMBOSS-28)  ⟷  `Œdèmes des membres inférieurs` (German-64) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du nez` (AMBOSS-28)  ⟷  `Inspection générale` (German-64) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Mesure de la tension artérielle` (German-64)  ⟷  `Mesure de la tension artérielle (24 heures)` (AMBOSS-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Régimes antérieurs` (German-64)  ⟷  `Épisodes antérieurs` (AMBOSS-28) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-28)  ⟷  `Antécédents familiaux` (AMBOSS-28) — **AMBOSS-28, section « a »** distingue ces deux items
- ⛔ `Examen cardiovasculaire` (AMBOSS-28, German-64)  ⟷  `Examen ostéo-articulaire` (German-64) — **German-64, section « e »** distingue ces deux items
- ⛔ `Habitudes alimentaires - Déjeuner` (German-64)  ⟷  `Habitudes alimentaires - Dîner` (German-64) — **German-64, section « a »** distingue ces deux items
- ⛔ `Habitudes alimentaires - Déjeuner` (German-64)  ⟷  `Habitudes alimentaires - Petit-déjeuner` (German-64) — **German-64, section « a »** distingue ces deux items
- ⛔ `Habitudes alimentaires - Dîner` (German-64)  ⟷  `Habitudes alimentaires - Petit-déjeuner` (German-64) — **German-64, section « a »** distingue ces deux items
- ⛔ `Obésité familiale` (German-64)  ⟷  `Situation familiale` (German-64) — **German-64, section « a »** distingue ces deux items
- ⛔ `Symptômes évocateurs d'endocrinopathie` (German-64)  ⟷  `Symptômes évocateurs de diabète` (German-64) — **German-64, section « a »** distingue ces deux items

## Toux — 13 cas · 84 à juger (2 de forme, 82 de contenu), 174 ⚠️, 76 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Communication avec la patiente` (AMBOSS-18, AMBOSS-19)  ⟷  `Communication avec le patient` (AMBOSS-31)
- `Facteurs améliorants` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-77)  ⟷  `Facteurs d'amélioration` (German-76)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Caractérisation de la toux et des expectorations` (AMBOSS-31)  ⟷  `Caractéristiques de la toux et des expectorations` (German-75, German-76)
- `Symptômes ORL associés` (German-75)  ⟷  `Symptômes associés` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, German-78)
- `Caractérisation temporelle de la toux` (German-76)  ⟷  `Caractérisation temporelle de la toux actuelle` (German-75)
- `Question d'entrée ouverte - Plainte principale` (German-76)  ⟷  `Question d'entrée ouverte - Symptôme principal` (German-75)
- `Examens biologiques` (German-76)  ⟷  `Examens microbiologiques` (AMBOSS-31)
- `Recherche de frémitus` (AMBOSS-18)  ⟷  `Recherche de frémitus vocal` (AMBOSS-19)
- `Diminution du murmure vésiculaire` (German-76)  ⟷  `Modifications du murmure vésiculaire` (German-75)
- `Examens cardiologiques` (German-76)  ⟷  `Examens microbiologiques` (AMBOSS-31)
- `Autres examens complémentaires` (German-75)  ⟷  `Examens complémentaires` (RESCOS-63, RESCOS-63b)
- `Radiographie thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-76, German-77, German-78)  ⟷  `Radiographie thorax` (RESCOS-62)
- `Symptômes ORL et infectieux` (German-76)  ⟷  `Symptômes infectieux` (German-78)
- `Signes d'infection ORL` (German-79)  ⟷  `Signes d’infection` (AZYGOS-47)
- `Diminution du murmure vésiculaire` (German-76)  ⟷  `Évaluation du murmure vésiculaire` (RESCOS-64-1)
- `Examens complémentaires selon gravité` (RESCOS-62)  ⟷  `Examens complémentaires selon orientation` (RESCOS-64-1)
- `Présence de sang` (German-75, RESCOS-62)  ⟷  `Présence de sang franc` (German-76)
- `Maladies cardiovasculaires` (German-76)  ⟷  `Pathologies cardiovasculaires` (RESCOS-62)
- `Radiographie thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-76, German-77, German-78)  ⟷  `Radiographie/Ultrason thoracique` (RESCOS-63, RESCOS-63b)
- `Caractérisation de la toux et des expectorations` (AMBOSS-31)  ⟷  `Caractérisation des expectorations` (RESCOS-62)
- `Caractérisation de la toux` (AMBOSS-18, AMBOSS-19, RESCOS-62)  ⟷  `Caractérisation temporelle de la toux` (German-76)
- `Antécédents cardiaques` (German-78)  ⟷  `Antécédents cardiovasculaires` (German-76)
- `Présentation avec nom et fonction` (German-79)  ⟷  `Présentation avec nom, fonction et tâche` (German-75, German-76, German-77, German-78)
- `Épisodes antérieurs de symptômes similaires` (German-77)  ⟷  `Épisodes antérieurs similaires` (German-76)
- `Diagnostics différentiels` (German-79, RESCOS-63, RESCOS-63b)  ⟷  `Diagnostics différentiels cardiaques` (German-78)
- `Symptômes généraux - Signes B` (German-75)  ⟷  `Symptômes généraux et signes d'alarme` (RESCOS-64-1)
- `Modifications du murmure vésiculaire` (German-75)  ⟷  `Évaluation du murmure vésiculaire` (RESCOS-64-1)
- `Inspection thoracique` (German-78, RESCOS-64-1)  ⟷  `Percussion thoracique` (German-77, RESCOS-62)
- `Antécédents respiratoires` (RESCOS-64-1)  ⟷  `Antécédents similaires` (German-78, German-79)
- `Diagnostics différentiels` (German-79, RESCOS-63, RESCOS-63b)  ⟷  `Diagnostics différentiels pulmonaires` (German-78)
- `Hospitalisations antérieures` (German-79, RESCOS-62)  ⟷  `Opérations antérieures` (AZYGOS-47)
- `Réaction appropriée au défi concernant l'arrêt du tabac` (AMBOSS-19)  ⟷  `Réaction appropriée au défi concernant la guérison` (AMBOSS-18)
- `Anamnèse de l'entourage` (German-79)  ⟷  `Anamnèse de l'entourage (contagion)` (German-77)
- `Examens complémentaires de première intention` (AMBOSS-18, AMBOSS-19, AMBOSS-31, RESCOS-62)  ⟷  `Examens complémentaires selon orientation` (RESCOS-64-1)
- `Diagnostic différentiel respiratoire` (RESCOS-62)  ⟷  `Diagnostics différentiels` (German-79, RESCOS-63, RESCOS-63b)
- `Exposition (professionnelle, environnementale)` (German-77)  ⟷  `Exposition professionnelle et contages` (German-75)
- `Aspect des expectorations` (German-75)  ⟷  `Couleur des expectorations` (AMBOSS-18, AMBOSS-19, German-76, German-77)
- `Examens complémentaires de première intention` (AMBOSS-18, AMBOSS-19, AMBOSS-31, RESCOS-62)  ⟷  `Examens de première intention` (RESCOS-64-1)
- `Hippocratisme digital` (German-76, RESCOS-62)  ⟷  `Recherche d'hippocratisme digital` (German-75, German-77, RESCOS-64-1)
- `Productive ou non` (German-79)  ⟷  `Productive ou sèche` (German-77)
- `Auscultation cardiaque` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, German-75, German-77, RESCOS-62)  ⟷  `Auscultation cardiaque systématique` (RESCOS-64-1)
- `Caractérisation des expectorations` (RESCOS-62)  ⟷  `Caractéristiques de la toux et des expectorations` (German-75, German-76)
- `Caractéristiques de la respiration` (German-79)  ⟷  `Caractéristiques de la toux et des expectorations` (German-75, German-76)
- `Examen cardiaque` (German-75, German-77, German-78)  ⟷  `Examen cardiovasculaire` (AMBOSS-18, AMBOSS-19, AMBOSS-31, RESCOS-64-1)
- `Examens complémentaires` (RESCOS-63, RESCOS-63b)  ⟷  `Examens complémentaires selon gravité` (RESCOS-62)
- `Symptômes généraux` (German-76)  ⟷  `Symptômes généraux - Signes B` (German-75)
- `Vibrations vocales` (German-76, RESCOS-62)  ⟷  `Vibrations vocales (frémitus)` (German-75)
- `Signes vitaux` (German-75, German-76)  ⟷  `Signes vitaux mesurés` (German-77)
- `Examen cardiovasculaire` (AMBOSS-18, AMBOSS-19, AMBOSS-31, RESCOS-64-1)  ⟷  `Examen cardiovasculaire complémentaire` (RESCOS-62)
- `Symptômes respiratoires associés` (German-75, RESCOS-64-1)  ⟷  `Symptômes végétatifs associés` (AZYGOS-47)
- `Diagnostic différentiel respiratoire` (RESCOS-62)  ⟷  `Diagnostics différentiels cardiaques` (German-78)
- `Maladies génétiques` (German-75)  ⟷  `Maladies héréditaires` (RESCOS-62)
- `Tabagisme` (German-75, German-76)  ⟷  `Tabagisme actif` (RESCOS-64-1)
- `Hypothèse diagnostique : Coqueluche` (RESCOS-63, RESCOS-63b)  ⟷  `Hypothèses diagnostiques` (AMBOSS-18, AMBOSS-19, AMBOSS-31)
- `Antécédents cardiovasculaires` (German-76)  ⟷  `Antécédents similaires` (German-78, German-79)
- `Symptômes ORL associés` (German-75)  ⟷  `Symptômes végétatifs associés` (AZYGOS-47)
- `Autres symptômes respiratoires` (German-76, RESCOS-62)  ⟷  `Symptômes respiratoires associés` (German-75, RESCOS-64-1)
- `Examen ORL` (German-75, German-77)  ⟷  `Examen ORL rapide` (German-76)
- `Diagnostic différentiel respiratoire` (RESCOS-62)  ⟷  `Diagnostics différentiels pulmonaires` (German-78)
- `Exposition (professionnelle, environnementale)` (German-77)  ⟷  `Exposition environnementale` (German-75, German-76)
- `Symptômes associés - Reflux gastro-œsophagien` (German-77)  ⟷  `Symptômes gastro-œsophagiens` (German-75, German-76)
- `Examen pulmonaire` (German-77)  ⟷  `Examen pulmonaire - Palpation` (German-75, German-76)
- `Caractérisation de l'hémoptysie` (RESCOS-64-1)  ⟷  `Caractérisation de la toux` (AMBOSS-18, AMBOSS-19, RESCOS-62)
- `Symptômes généraux` (German-76)  ⟷  `Symptômes principaux` (German-77, German-78)
- `Symptômes associés` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, German-78)  ⟷  `Symptômes associés - Sibilances` (German-77)
- `Antécédents personnels et facteurs de risque` (RESCOS-62)  ⟷  `Antécédents personnels et familiaux` (RESCOS-64-1)
- `Contexte social et autonomie` (German-76)  ⟷  `Contexte social et professionnel` (RESCOS-64-1)
- `Offrir mouchoir et eau lors de la crise de toux` (AMBOSS-19)  ⟷  `Offrir mouchoir et/ou eau pendant la crise de toux de la patiente` (AMBOSS-18)
- `Facteurs améliorants` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-77)  ⟷  `Facteurs déclenchants` (RESCOS-62)
- `Diminution du murmure vésiculaire` (German-76)  ⟷  `Murmure vésiculaire` (RESCOS-62)
- `Murmure vésiculaire` (RESCOS-62)  ⟷  `Évaluation du murmure vésiculaire` (RESCOS-64-1)
- `Prise en charge immédiate` (RESCOS-63, RESCOS-63b, RESCOS-64-1)  ⟷  `Prise en charge étiologique` (German-76)
- `Examen cardiaque` (German-75, German-77, German-78)  ⟷  `Examen cardiaque - Palpation` (German-76)
- `Examen cardiaque` (German-75, German-77, German-78)  ⟷  `Examen thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31)
- `Habitudes et facteurs de risque` (German-76)  ⟷  `Habitudes et mode de vie` (AMBOSS-18, AMBOSS-19, AMBOSS-31)
- `Ampliation thoracique` (German-75, German-76, RESCOS-62)  ⟷  `Évaluation de l'ampliation thoracique` (RESCOS-64-1)
- `Inspection thoracique` (German-78, RESCOS-64-1)  ⟷  `Inspection thoracique - patient assis` (RESCOS-62)
- `Examen pulmonaire` (German-77)  ⟷  `Examen pulmonaire - Inspection` (German-75, German-76)
- `Examen pulmonaire` (German-77)  ⟷  `Examen pulmonaire - Percussion` (German-75, German-76)
- `Maladies cardiovasculaires` (German-76)  ⟷  `Maladies héréditaires` (RESCOS-62)
- `Symptômes ORL et infectieux` (German-76)  ⟷  `Symptômes principaux` (German-77, German-78)
- `Anamnèse personnelle` (RESCOS-63, RESCOS-63b)  ⟷  `Anamnèse sociale` (German-77, German-78)
- `Caractérisation de la toux` (AMBOSS-18, AMBOSS-19, RESCOS-62)  ⟷  `Caractérisation temporelle de la toux actuelle` (German-75)
- `Épisodes antérieurs de symptômes similaires` (German-77)  ⟷  `Épisodes antérieurs de toux ou problèmes respiratoires` (German-75)

- ⚠️ `Activité physique` (German-75, RESCOS-62)  ⟷  `Activité physique actuelle` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aires axillaires` (German-76)  ⟷  `Ganglions axillaires` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation` (RESCOS-63, RESCOS-63b)  ⟷  `Orientation` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Alimentation` (RESCOS-63, RESCOS-63b)  ⟷  `Palpitations` (AMBOSS-18, AMBOSS-19, German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ampliation thoracique` (German-75, German-76, RESCOS-62)  ⟷  `Examen thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ampliation thoracique` (German-75, German-76, RESCOS-62)  ⟷  `Inspection thoracique` (German-78, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antibiotiques` (RESCOS-63, RESCOS-63b)  ⟷  `Antibiotiques récents` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antibiotiques` (RESCOS-63, RESCOS-63b)  ⟷  `Antipyrétiques` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (German-76)  ⟷  `Antécédents pulmonaires` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (German-76)  ⟷  `Examen cardiovasculaire` (AMBOSS-18, AMBOSS-19, AMBOSS-31, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents cardiovasculaires` (German-76)  ⟷  `Pathologies cardiovasculaires` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents pulmonaires` (RESCOS-62)  ⟷  `Antécédents respiratoires` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents pulmonaires` (RESCOS-62)  ⟷  `Antécédents similaires` (German-78, German-79) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Arrêt de travail` (German-77)  ⟷  `Repos et arrêt de travail` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect des expectorations` (German-75)  ⟷  `Caractérisation des expectorations` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect des expectorations` (German-75)  ⟷  `Diagnostic des expectorations` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect des expectorations` (German-75)  ⟷  `Sang dans les expectorations` (AMBOSS-18, AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect des expectorations` (German-75)  ⟷  `Volume des expectorations` (AMBOSS-18, AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect général` (RESCOS-62)  ⟷  `Inspection générale` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aspect général` (RESCOS-62)  ⟷  `État général` (German-76, RESCOS-63, RESCOS-63b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Asymétrie thoracique` (RESCOS-62)  ⟷  `CT thoracique` (AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Asymétrie thoracique` (RESCOS-62)  ⟷  `Examen thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Asymétrie thoracique` (RESCOS-62)  ⟷  `Symétrie thoracique` (German-75, German-76) — **antonymes présumés** (préfixe privatif « a- ») : aucune grille ne les porte ensemble, donc la propriété 8 n'a pas de témoin. *(Par ailleurs inerte : la propriété 7 la refuserait.)*
- ⚠️ `Auscultation` (AZYGOS-47, German-75, German-78)  ⟷  `Points d'auscultation` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation antérieure systématique` (German-75, German-76)  ⟷  `Auscultation cardiaque systématique` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Auscultation cardiaque systématique` (RESCOS-64-1)  ⟷  `Auscultation postérieure systématique` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres examens complémentaires` (German-75)  ⟷  `Planification des examens complémentaires` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres symptômes respiratoires` (German-76, RESCOS-62)  ⟷  `Détresse respiratoire` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `BNP ou NT-proBNP` (German-76)  ⟷  `BNP, NT-pro BNP` (AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bruits surajoutés` (German-75)  ⟷  `Bruits surajoutés (B3, B4)` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT thoracique` (AMBOSS-31)  ⟷  `Examen thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT thoracique` (AMBOSS-31)  ⟷  `Inspection thoracique` (German-78, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT thoracique` (AMBOSS-31)  ⟷  `Palpation thoracique` (RESCOS-62, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `CT thoracique` (AMBOSS-31)  ⟷  `Symétrie thoracique` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractère des expectorations habituelles` (RESCOS-64-1)  ⟷  `Culture des expectorations (3 échantillons)` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractérisation des expectorations` (RESCOS-62)  ⟷  `Diagnostic des expectorations` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractérisation des expectorations` (RESCOS-62)  ⟷  `Recherche bactério dans les expectorations` (RESCOS-63, RESCOS-63b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Circonstances` (German-77, RESCOS-62)  ⟷  `Circonstances de début` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Circonstances` (German-77, RESCOS-62)  ⟷  `Début et circonstances` (German-79) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Classification NYHA` (German-76)  ⟷  `Classification NYHA ou mMRC` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Compliance thérapeutique` (German-76)  ⟷  `Conseils thérapeutiques` (German-79) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Compliance thérapeutique` (German-76)  ⟷  `Observance thérapeutique` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Compliance thérapeutique` (German-76)  ⟷  `Éducation thérapeutique` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Conseils thérapeutiques` (German-79)  ⟷  `Observance thérapeutique` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Conseils thérapeutiques` (German-79)  ⟷  `Tentatives thérapeutiques` (German-79) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Conseils thérapeutiques` (German-79)  ⟷  `Éducation thérapeutique` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Couleur` (AMBOSS-31)  ⟷  `Douleurs` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Couleur des crachats` (RESCOS-62)  ⟷  `Couleur des expectorations` (AMBOSS-18, AMBOSS-19, German-76, German-77) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Couleur des expectorations` (AMBOSS-18, AMBOSS-19, German-76, German-77)  ⟷  `Diagnostic des expectorations` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Critères d'hospitalisation` (German-76)  ⟷  `Hospitalisation` (AZYGOS-47, RESCOS-63, RESCOS-63b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Critères d'hospitalisation` (German-76)  ⟷  `Surveillance et critères d'hospitalisation` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cyanose centrale et périphérique` (RESCOS-62)  ⟷  `Cyanose périphérique` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cyanose périphérique` (German-76)  ⟷  `Pouls périphériques` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cycle respiratoire` (RESCOS-62)  ⟷  `Dépendance respiratoire` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cycle respiratoire` (RESCOS-62)  ⟷  `PCR respiratoire` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Cycle respiratoire` (RESCOS-62)  ⟷  `Pattern respiratoire` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostic des expectorations` (AZYGOS-47)  ⟷  `Sang dans les expectorations` (AMBOSS-18, AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostic des expectorations` (AZYGOS-47)  ⟷  `Volume des expectorations` (AMBOSS-18, AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostic différentiel douleur thoracique` (AZYGOS-47)  ⟷  `Diagnostic différentiel respiratoire` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Diagnostic différentiel douleur thoracique` (AZYGOS-47)  ⟷  `Diagnostics différentiels cardiaques` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Durée et circonstances` (RESCOS-62)  ⟷  `Début et circonstances` (German-79) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dyspnée paroxystique nocturne` (German-75, RESCOS-62)  ⟷  `Orthopnée et dyspnée paroxystique nocturne` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Début et durée` (RESCOS-64-1)  ⟷  `Début et fréquence` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dégradation de l'état général` (German-79)  ⟷  `Évaluation de l'état général` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dépendance respiratoire` (AZYGOS-47)  ⟷  `Détresse respiratoire` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dépendance respiratoire` (AZYGOS-47)  ⟷  `Fréquence respiratoire` (German-75, German-76, RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dépendance respiratoire` (AZYGOS-47)  ⟷  `PCR respiratoire` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dépendance respiratoire` (AZYGOS-47)  ⟷  `Pattern respiratoire` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dépistages antérieurs` (German-75)  ⟷  `Épisodes antérieurs` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Détresse respiratoire` (RESCOS-62)  ⟷  `PCR respiratoire` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Détresse respiratoire` (RESCOS-62)  ⟷  `Pattern respiratoire` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Détresse respiratoire` (RESCOS-62)  ⟷  `Signes de détresse respiratoire` (German-79) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `ECG/Échocardiographie` (German-78)  ⟷  `Échocardiographie` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiaque` (German-75, German-77, German-78)  ⟷  `Examens cardiologiques` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (AMBOSS-18, AMBOSS-19, AMBOSS-31, RESCOS-64-1)  ⟷  `Maladies cardiovasculaires` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire` (AMBOSS-18, AMBOSS-19, AMBOSS-31, RESCOS-64-1)  ⟷  `Symptômes cardiovasculaires` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen cardiovasculaire complémentaire` (RESCOS-62)  ⟷  `Examens complémentaires` (RESCOS-63, RESCOS-63b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen de la cavité buccale` (RESCOS-64-1)  ⟷  `Examen de la colonne vertébrale` (AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen pulmonaire` (German-77)  ⟷  `Examens complémentaires` (RESCOS-63, RESCOS-63b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examens complémentaires` (RESCOS-63, RESCOS-63b)  ⟷  `Examens complémentaires si pertinents` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examens complémentaires de première intention` (AMBOSS-18, AMBOSS-19, AMBOSS-31, RESCOS-62)  ⟷  `Examens complémentaires si pertinents` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examens complémentaires selon gravité` (RESCOS-62)  ⟷  `Examens complémentaires si pertinents` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examens complémentaires selon orientation` (RESCOS-64-1)  ⟷  `Examens complémentaires si pertinents` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Expectoration` (AZYGOS-47)  ⟷  `Expectorations rosées` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Expectorations rosées` (German-76)  ⟷  `Expectorations sanglantes` (German-79) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Explication du plan de prise en charge` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Organisation de la prise en charge` (German-77) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Explications au patient des impressions diagnostiques préliminaires` (AMBOSS-31)  ⟷  `Explications à la patiente des impressions diagnostiques préliminaires` (AMBOSS-18, AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition (professionnelle, environnementale)` (German-77)  ⟷  `Exposition professionnelle` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition aux fumées/poussières` (AMBOSS-18)  ⟷  `Exposition aux moisissures` (AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition professionnelle` (RESCOS-62)  ⟷  `Exposition professionnelle aux toxiques` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition professionnelle` (RESCOS-62)  ⟷  `Exposition professionnelle et contages` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition professionnelle` (RESCOS-62)  ⟷  `Situation professionnelle` (German-77) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition à la tuberculose et dépistage` (AMBOSS-31)  ⟷  `Exposition à la tuberculose, dernier test cutané` (AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs déclenchants` (RESCOS-62)  ⟷  `Éviction des facteurs déclenchants` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Frémissements` (German-76)  ⟷  `Vomissements` (RESCOS-63, RESCOS-63b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence des épisodes` (German-75)  ⟷  `Fréquence respiratoire` (German-75, German-76, RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence respiratoire` (German-75, German-76, RESCOS-62)  ⟷  `Mesure de la fréquence respiratoire` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence respiratoire` (German-75, German-76, RESCOS-62)  ⟷  `PCR respiratoire` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Fréquence respiratoire` (German-75, German-76, RESCOS-62)  ⟷  `R - Fréquence respiratoire ≥ 30/min` (German-77) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ganglions lymphatiques` (German-78)  ⟷  `Palpation des ganglions lymphatiques` (German-77) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisation` (AZYGOS-47, RESCOS-63, RESCOS-63b)  ⟷  `Localisation` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hospitalisations` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75)  ⟷  `Hospitalisations antérieures` (German-79, RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hygiène des mains` (German-78)  ⟷  `Lavage des mains` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (German-77)  ⟷  `Pression artérielle` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Identification des lésions tuberculeuses` (German-75)  ⟷  `Identification des sibilances` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infection ORL récente` (German-76)  ⟷  `Infections récentes` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infections passées` (AZYGOS-47)  ⟷  `Infections récentes` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des mains` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Inspection veineuse` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection des veines jugulaires` (German-77)  ⟷  `Turgescence des veines jugulaires` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du thorax` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Inspection statique du thorax` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du thorax` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Inspection thoracique` (German-78, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Limites pulmonaires` (German-75)  ⟷  `Pathologies pulmonaires` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Localisation` (RESCOS-62)  ⟷  `Localisation (apex)` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies chroniques` (German-75)  ⟷  `Pathologies chroniques` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Marqueurs inflammatoires (CRP)` (German-76)  ⟷  `Valeurs inflammatoires (CRP)` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Nausées/vomissements` (AMBOSS-18)  ⟷  `Vomissements` (RESCOS-63, RESCOS-63b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Oxygénothérapie si SpO2 < 92%` (RESCOS-62)  ⟷  `Oxygénothérapie si hypoxémie` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `PCR respiratoire` (RESCOS-62)  ⟷  `Pattern respiratoire` (AZYGOS-47) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation` (AZYGOS-47)  ⟷  `Palpitations` (AMBOSS-18, AMBOSS-19, German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation choc de pointe` (RESCOS-62)  ⟷  `Palpation du choc apexien` (AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation des ganglions lymphatiques` (German-77)  ⟷  `Palpation des ganglions lymphatiques de la tête et du cou` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du pouls radial` (AMBOSS-19)  ⟷  `Palpation du précordium` (German-75, German-76, German-77) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Palpation du thorax` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Palpation thoracique` (RESCOS-62, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas d'œdèmes des membres inférieurs` (RESCOS-64-1)  ⟷  `Recherche d'œdèmes des membres inférieurs` (German-77, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas d'œdèmes des membres inférieurs` (RESCOS-64-1)  ⟷  `Symptômes associés - Œdèmes des membres inférieurs` (German-77) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas d'œdèmes des membres inférieurs` (RESCOS-64-1)  ⟷  `Œdèmes des membres inférieurs` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas d'œdèmes des membres inférieurs` (RESCOS-64-1)  ⟷  `Œdèmes membres inférieurs` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas de voyage récent` (RESCOS-64-1)  ⟷  `Voyage récent` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pas de voyage récent` (RESCOS-64-1)  ⟷  `Voyages récents` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Pathologies cardiovasculaires` (RESCOS-62)  ⟷  `Symptômes cardiovasculaires` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion des champs pulmonaires` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Percussion pulmonaire` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion des champs pulmonaires` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Percussion systématique des deux champs pulmonaires` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion pulmonaire` (RESCOS-64-1)  ⟷  `Tuberculose pulmonaire` (German-75, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Percussion systématique` (German-75)  ⟷  `Percussion thoracique` (German-77, RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Position assise` (German-76)  ⟷  `Position semi-assise` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Problèmes de sommeil` (AMBOSS-18)  ⟷  `Troubles du sommeil` (AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Productive` (AMBOSS-31)  ⟷  `Productive ou non` (German-79) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Productive` (AMBOSS-31)  ⟷  `Toux productive` (AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (German-75, German-78, RESCOS-64-1)  ⟷  `Progression` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Progression` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Progression récente` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Qualité` (RESCOS-63, RESCOS-63b)  ⟷  `Quantité` (German-75, German-76, RESCOS-62, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie` (AZYGOS-47)  ⟷  `Radiographie thorax` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie` (AZYGOS-47)  ⟷  `Échocardiographie` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-76, German-77, German-78)  ⟷  `Radiographie thoracique (face et profil)` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Radiographie/Ultrason thoracique` (RESCOS-63, RESCOS-63b)  ⟷  `Échocardiographie transthoracique` (AMBOSS-19) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'œdème déclive` (AMBOSS-19)  ⟷  `Recherche d'œdèmes` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'œdèmes des membres inférieurs` (German-77, RESCOS-64-1)  ⟷  `Œdèmes des membres inférieurs` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'œdèmes des membres inférieurs` (German-77, RESCOS-64-1)  ⟷  `Œdèmes membres inférieurs` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de frémitus` (AMBOSS-18)  ⟷  `Recherche de matité` (German-75, RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'insuffisance cardiaque droite` (German-75, RESCOS-64-1)  ⟷  `Signes d'insuffisance cardiaque` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes d'insuffisance cardiaque droite` (German-75, RESCOS-64-1)  ⟷  `Signes d'insuffisance cardiaque droite` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche des préoccupations et questions de la patiente` (AMBOSS-18, AMBOSS-19)  ⟷  `Recherche des préoccupations et questions du patient` (AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche du reflux hépato-jugulaire` (AMBOSS-19)  ⟷  `Reflux hépato-jugulaire` (German-75, German-76, RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes d'insuffisance cardiaque` (RESCOS-62)  ⟷  `Signes d'insuffisance cardiaque droite` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Signes de détresse respiratoire` (German-79)  ⟷  `Évaluation des signes de détresse respiratoire` (RESCOS-64-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Suivi et éducation thérapeutique` (German-76)  ⟷  `Éducation thérapeutique` (German-78) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Symptômes associés - Œdèmes des membres inférieurs` (German-77)  ⟷  `Œdèmes des membres inférieurs` (German-75, German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tabagisme actif` (RESCOS-64-1)  ⟷  `Tabagisme passif` (German-75, German-76) — **antonymes présumés** (actif / passif) : aucune grille ne les porte ensemble, donc la propriété 8 n'a pas de témoin. *(Par ailleurs inerte : la propriété 7 la refuserait.)*
- ⚠️ `Tests de fonction pulmonaire` (AMBOSS-19)  ⟷  `Tests de fonction pulmonaire (EFR)` (AMBOSS-18) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Traitement médicamenteux de l'IC` (German-76)  ⟷  `Traitements médicamenteux` (German-75) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Turgescence des veines jugulaires` (German-75, German-76)  ⟷  `Turgescence jugulaire` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Vaccinations` (RESCOS-62)  ⟷  `Vaccins` (RESCOS-63, RESCOS-63b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Épisodes antérieurs` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Épisodes antérieurs similaires` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'accord de la patiente avec le plan diagnostique` (AMBOSS-18, AMBOSS-19)  ⟷  `Évaluation de l'accord du patient avec le plan diagnostique` (AMBOSS-31) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'urgence` (German-79)  ⟷  `Évaluation de la FEVG` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'état général` (RESCOS-64-1)  ⟷  `Évaluation de la FEVG` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'état général` (RESCOS-64-1)  ⟷  `Évaluation de la dyspnée` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de l'état général` (RESCOS-64-1)  ⟷  `Évaluation de la gravité` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de la FEVG` (German-76)  ⟷  `Évaluation de la dyspnée` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de la FEVG` (German-76)  ⟷  `Évaluation de la gravité` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de la dyspnée` (RESCOS-62)  ⟷  `Évaluation de la gravité` (RESCOS-62) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de la dyspnée` (RESCOS-62)  ⟷  `Évaluation de la sévérité` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de la gravité` (RESCOS-62)  ⟷  `Évaluation de la sévérité` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Évaluation de la sonorité pulmonaire` (RESCOS-64-1)  ⟷  `Évaluation de la sévérité` (German-76) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Adénopathies sus-claviculaires` (German-75)  ⟷  `Ganglions sus-claviculaires` (German-75) — **German-75, section « e »** distingue ces deux items
- ⛔ `Aggravation en décubitus` (German-76)  ⟷  `Aggravation nocturne` (German-76) — **German-76, section « a »** distingue ces deux items
- ⛔ `Ampliation thoracique` (German-75, German-76, RESCOS-62)  ⟷  `Palpation thoracique` (RESCOS-62, RESCOS-64-1) — **RESCOS-62, section « e »** distingue ces deux items
- ⛔ `Antécédents cardiaques` (German-78)  ⟷  `Antécédents familiaux` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, German-75, German-76, RESCOS-62, RESCOS-64-1) — **German-78, section « a »** distingue ces deux items
- ⛔ `Antécédents cardiaques` (German-78)  ⟷  `Antécédents similaires` (German-78, German-79) — **German-78, section « a »** distingue ces deux items
- ⛔ `Antécédents cardiovasculaires` (German-76)  ⟷  `Maladies cardiovasculaires` (German-76) — **German-76, section « a »** distingue ces deux items
- ⛔ `Antécédents cardiovasculaires` (German-76)  ⟷  `Symptômes cardiovasculaires` (German-75, German-76) — **German-76, section « a »** distingue ces deux items
- ⛔ `Antécédents cardiovasculaires` (German-76)  ⟷  `Traitements cardiovasculaires actuels` (German-76) — **German-76, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Antécédents familiaux` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, German-75, German-76, RESCOS-62, RESCOS-64-1) — **AMBOSS-18, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, German-75, German-76, RESCOS-62, RESCOS-64-1)  ⟷  `Antécédents personnels et familiaux` (RESCOS-64-1) — **RESCOS-64-1, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, German-75, German-76, RESCOS-62, RESCOS-64-1)  ⟷  `Antécédents similaires` (German-78, German-79) — **German-78, section « a »** distingue ces deux items
- ⛔ `Auscultation antérieure systématique` (German-75, German-76)  ⟷  `Auscultation postérieure systématique` (German-75, German-76) — **German-75, section « e »** distingue ces deux items
- ⛔ `Auscultation pulmonaire` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-78, RESCOS-62, RESCOS-64-1)  ⟷  `Percussion pulmonaire` (RESCOS-64-1) — **RESCOS-64-1, section « e »** distingue ces deux items
- ⛔ `Auscultation systématique des deux champs pulmonaires` (RESCOS-64-1)  ⟷  `Percussion systématique des deux champs pulmonaires` (RESCOS-64-1) — **RESCOS-64-1, section « e »** distingue ces deux items
- ⛔ `Autres positions` (German-76)  ⟷  `Facteurs positionnels` (German-76) — **German-76, section « a »** distingue ces deux items
- ⛔ `Caractérisation de la douleur thoracique` (RESCOS-62)  ⟷  `Caractérisation de la toux` (AMBOSS-18, AMBOSS-19, RESCOS-62) — **RESCOS-62, section « a »** distingue ces deux items
- ⛔ `Circonstances` (German-77, RESCOS-62)  ⟷  `Durée et circonstances` (RESCOS-62) — **RESCOS-62, section « a »** distingue ces deux items
- ⛔ `Coloration cutanée` (German-79)  ⟷  `Éruption cutanée` (German-79) — **German-79, section « a »** distingue ces deux items
- ⛔ `Couleur des expectorations` (AMBOSS-18, AMBOSS-19, German-76, German-77)  ⟷  `Volume des expectorations` (AMBOSS-18, AMBOSS-19) — **AMBOSS-18, section « a »** distingue ces deux items
- ⛔ `Critères d'hospitalisation` (German-76)  ⟷  `Indication d'hospitalisation` (German-76, RESCOS-62) — **German-76, section « m »** distingue ces deux items
- ⛔ `Cycle respiratoire` (RESCOS-62)  ⟷  `Fréquence respiratoire` (German-75, German-76, RESCOS-62) — **RESCOS-62, section « e »** distingue ces deux items
- ⛔ `Diagnostics différentiels cardiaques` (German-78)  ⟷  `Diagnostics différentiels pulmonaires` (German-78) — **German-78, section « m »** distingue ces deux items
- ⛔ `Douleur thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, RESCOS-64-1)  ⟷  `Douleurs thoraciques` (German-75, German-76) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Début / durée` (AZYGOS-47)  ⟷  `Début et durée` (RESCOS-64-1) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Dépistage des effets secondaires` (German-75)  ⟷  `Surveillance des effets secondaires` (German-75) — **German-75, section « m »** distingue ces deux items
- ⛔ `Détresse respiratoire` (RESCOS-62)  ⟷  `Fréquence respiratoire` (German-75, German-76, RESCOS-62) — **RESCOS-62, section « e »** distingue ces deux items
- ⛔ `Examen cardiaque - Auscultation` (German-76)  ⟷  `Examen cardiaque - Palpation` (German-76) — **German-76, section « e »** distingue ces deux items
- ⛔ `Examen cardiaque - Palpation` (German-76)  ⟷  `Examen pulmonaire - Palpation` (German-75, German-76) — **German-76, section « e »** distingue ces deux items
- ⛔ `Examen des extrémités` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-76, German-77)  ⟷  `Température des extrémités` (German-75) — **German-75, section « e »** distingue ces deux items
- ⛔ `Examen du cou` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Examen du dos` (AMBOSS-31) — **AMBOSS-31, section « e »** distingue ces deux items
- ⛔ `Examen pulmonaire - Inspection` (German-75, German-76)  ⟷  `Examen pulmonaire - Palpation` (German-75, German-76) — **German-75, section « e »** distingue ces deux items
- ⛔ `Examen pulmonaire - Inspection` (German-75, German-76)  ⟷  `Examen pulmonaire - Percussion` (German-75, German-76) — **German-75, section « e »** distingue ces deux items
- ⛔ `Examen pulmonaire - Palpation` (German-75, German-76)  ⟷  `Examen pulmonaire - Percussion` (German-75, German-76) — **German-75, section « e »** distingue ces deux items
- ⛔ `Examens biologiques` (German-76)  ⟷  `Examens cardiologiques` (German-76) — **German-76, section « m »** distingue ces deux items
- ⛔ `Examens de première intention` (RESCOS-64-1)  ⟷  `Examens de seconde intention` (RESCOS-64-1) — **RESCOS-64-1, section « m »** distingue ces deux items
- ⛔ `Exposition professionnelle aux toxiques` (German-75)  ⟷  `Exposition professionnelle et contages` (German-75) — **German-75, section « a »** distingue ces deux items
- ⛔ `Exposition à la tuberculose` (AMBOSS-18, AMBOSS-31)  ⟷  `Exposition à la tuberculose et dépistage` (AMBOSS-31) — **AMBOSS-31, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-77)  ⟷  `Facteurs améliorants` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-77) — **AMBOSS-18, section « a »** distingue ces deux items
- ⛔ `Ganglions axillaires` (German-75)  ⟷  `Ganglions sus-claviculaires` (German-75) — **German-75, section « e »** distingue ces deux items
- ⛔ `Hospitalisation` (AZYGOS-47, RESCOS-63, RESCOS-63b)  ⟷  `Hospitalisations` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Hépatomégalie` (German-76)  ⟷  `Hépatomégalie de stase` (German-76) — **German-76, section « e »** distingue ces deux items
- ⛔ `Immunosuppresseurs` (German-75)  ⟷  `Immunosuppression` (German-75) — **German-75, section « a »** distingue ces deux items
- ⛔ `Importance de l'observance` (German-75)  ⟷  `Suivi de l'observance` (German-75) — **German-75, section « m »** distingue ces deux items
- ⛔ `Inspection de l'oropharynx` (AMBOSS-18, AMBOSS-31)  ⟷  `Inspection du thorax` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **AMBOSS-18, section « e »** distingue ces deux items
- ⛔ `Inspection du thorax` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Palpation du thorax` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **AMBOSS-18, section « e »** distingue ces deux items
- ⛔ `Inspection thoracique` (German-78, RESCOS-64-1)  ⟷  `Palpation thoracique` (RESCOS-62, RESCOS-64-1) — **RESCOS-64-1, section « e »** distingue ces deux items
- ⛔ `Justification clinique` (German-75)  ⟷  `Justification épidémiologique` (German-75) — **German-75, section « m »** distingue ces deux items
- ⛔ `Maladies cardiovasculaires` (German-76)  ⟷  `Symptômes cardiovasculaires` (German-75, German-76) — **German-76, section « a »** distingue ces deux items
- ⛔ `Maladies chroniques` (German-75)  ⟷  `Maladies génétiques` (German-75) — **German-75, section « a »** distingue ces deux items
- ⛔ `Mère` (German-78)  ⟷  `Père` (German-78) — **German-78, section « a »** distingue ces deux items
- ⛔ `Médicaments` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, RESCOS-63, RESCOS-63b)  ⟷  `Médicaments actuels` (AMBOSS-31, German-75, German-77, German-78) — **AMBOSS-31, section « a »** distingue ces deux items
- ⛔ `Médicaments` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, RESCOS-63, RESCOS-63b)  ⟷  `Vaccins/Médicaments` (RESCOS-63, RESCOS-63b) — **RESCOS-63, section « a »** distingue ces deux items
- ⛔ `Palpation des aires ganglionnaires (sus-claviculaires, axillaires)` (RESCOS-64-1)  ⟷  `Palpation des aires ganglionnaires cervicales` (RESCOS-64-1) — **RESCOS-64-1, section « e »** distingue ces deux items
- ⛔ `Palpation des aires ganglionnaires (sus-claviculaires, axillaires)` (RESCOS-64-1)  ⟷  `Palpation des aires ganglionnaires sus-claviculaires` (RESCOS-64-1) — **RESCOS-64-1, section « e »** distingue ces deux items
- ⛔ `Palpation des aires ganglionnaires cervicales` (RESCOS-64-1)  ⟷  `Palpation des aires ganglionnaires sus-claviculaires` (RESCOS-64-1) — **RESCOS-64-1, section « e »** distingue ces deux items
- ⛔ `Palpation du choc apexien` (AMBOSS-19)  ⟷  `Palpation du thorax` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **AMBOSS-19, section « e »** distingue ces deux items
- ⛔ `Palpation du pouls radial` (AMBOSS-19)  ⟷  `Palpation du thorax` (AMBOSS-18, AMBOSS-19, AMBOSS-31) — **AMBOSS-19, section « e »** distingue ces deux items
- ⛔ `Palpation thoracique` (RESCOS-62, RESCOS-64-1)  ⟷  `Percussion thoracique` (German-77, RESCOS-62) — **RESCOS-62, section « e »** distingue ces deux items
- ⛔ `Pathologies cardiovasculaires` (RESCOS-62)  ⟷  `Pathologies pulmonaires` (RESCOS-62) — **RESCOS-62, section « a »** distingue ces deux items
- ⛔ `Pathologies chroniques` (RESCOS-62)  ⟷  `Pathologies pulmonaires` (RESCOS-62) — **RESCOS-62, section « a »** distingue ces deux items
- ⛔ `Propose surveillance et rappel dans 1 heure` (German-79)  ⟷  `Proposer rappel dans 1 heure` (German-79) — **German-79, section « m »** distingue ces deux items
- ⛔ `Radiographie thoracique` (AMBOSS-18, AMBOSS-19, AMBOSS-31, German-75, German-76, German-77, German-78)  ⟷  `Échocardiographie transthoracique` (AMBOSS-19) — **AMBOSS-19, section « m »** distingue ces deux items
- ⛔ `Reflux gastro-œsophagien` (German-75, German-76)  ⟷  `Symptômes gastro-œsophagiens` (German-75, German-76) — **German-75, section « a »** distingue ces deux items
- ⛔ `Symptômes ORL associés` (German-75)  ⟷  `Symptômes respiratoires associés` (German-75, RESCOS-64-1) — **German-75, section « a »** distingue ces deux items
- ⛔ `Symptômes associés` (AMBOSS-18, AMBOSS-19, AMBOSS-31, AZYGOS-47, German-78)  ⟷  `Symptômes végétatifs associés` (AZYGOS-47) — **AZYGOS-47, section « a »** distingue ces deux items
- ⛔ `Symptômes associés - Baisse de performance` (German-77)  ⟷  `Symptômes associés - Sibilances` (German-77) — **German-77, section « a »** distingue ces deux items
- ⛔ `Symptômes associés - Douleurs thoraciques` (German-77)  ⟷  `Symptômes associés - Sibilances` (German-77) — **German-77, section « a »** distingue ces deux items
- ⛔ `Symptômes associés - Douleurs thoraciques` (German-77)  ⟷  `Symptômes associés - Symptômes cardiaques` (German-77) — **German-77, section « a »** distingue ces deux items
- ⛔ `Symptômes associés - Infection ORL` (German-77)  ⟷  `Symptômes associés - Sibilances` (German-77) — **German-77, section « a »** distingue ces deux items
- ⛔ `Symptômes généraux - Performance` (German-75)  ⟷  `Symptômes généraux - Signes B` (German-75) — **German-75, section « a »** distingue ces deux items
- ⛔ `Symptômes infectieux` (German-78)  ⟷  `Symptômes principaux` (German-77, German-78) — **German-78, section « a »** distingue ces deux items
- ⛔ `Traitements antiallergiques` (German-75)  ⟷  `Traitements utilisés` (German-75) — **German-75, section « a »** distingue ces deux items
- ⛔ `Voyage récent` (AMBOSS-18, AMBOSS-19, AMBOSS-31)  ⟷  `Voyages récents` (German-75) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Évaluation de la FEVG` (German-76)  ⟷  `Évaluation de la sévérité` (German-76) — **German-76, section « m »** distingue ces deux items
- ⛔ `Évaluation de la symétrie respiratoire` (RESCOS-64-1)  ⟷  `Évaluation des signes de détresse respiratoire` (RESCOS-64-1) — **RESCOS-64-1, section « e »** distingue ces deux items
- ⛔ `Œdèmes des membres inférieurs` (German-75, German-76)  ⟷  `Œdèmes membres inférieurs` (RESCOS-62) — **même signature socle A**, déjà appariés dans leur section

## Tremblement — 2 cas · 8 à juger (0 de forme, 8 de contenu), 19 ⚠️, 17 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Caractérisation du tremblement` (RESCOS-65)  ⟷  `Caractéristiques du tremblement` (German-80)
- `Examen de la marche` (German-80)  ⟷  `Examen de la marche et posture` (RESCOS-65)
- `Examens complémentaires` (German-80)  ⟷  `Examens complémentaires diagnostiques` (RESCOS-65)
- `Examen du tonus musculaire` (RESCOS-65)  ⟷  `Tonus musculaire` (German-80)
- `Troubles de l'humeur` (RESCOS-65)  ⟷  `Troubles de l'odorat` (German-80)
- `Troubles de l'odorat` (German-80)  ⟷  `Troubles de l'olfaction` (RESCOS-65)
- `Observation du tremblement` (German-80)  ⟷  `Observation et caractérisation du tremblement` (RESCOS-65)
- `Information au patient` (German-80)  ⟷  `Information patient et famille` (RESCOS-65)

- ⚠️ `Adaptation posologique` (RESCOS-65)  ⟷  `Adaptation posturale` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Asymétrie initiale` (RESCOS-65)  ⟷  `Asymétrie tonique` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres nerfs crâniens` (German-80)  ⟷  `Nerfs crâniens` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Bradykinésie` (German-80)  ⟷  `Dyskinésies` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractérisation du tremblement` (RESCOS-65)  ⟷  `Observation du tremblement` (German-80) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Caractérisation du tremblement` (RESCOS-65)  ⟷  `Observation et caractérisation du tremblement` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dépression` (German-80)  ⟷  `Progression` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique général` (RESCOS-65)  ⟷  `Symptômes neurologiques généraux` (German-80) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Facteurs modulants` (German-80)  ⟷  `Facteurs modulateurs` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Force musculaire` (RESCOS-65)  ⟷  `Raideur musculaire` (German-80, RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Force musculaire` (RESCOS-65)  ⟷  `Tonus musculaire` (German-80) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladie de Parkinson` (German-80)  ⟷  `Triade de Parkinson` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Neurologie` (RESCOS-65)  ⟷  `Neurologiques` (German-80) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Orientation spatiale` (German-80)  ⟷  `Orientation spécialisée` (German-80) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ouverture-fermeture du poing` (German-80)  ⟷  `Ouverture-fermeture mains` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (German-80)  ⟷  `Progression` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tremblement de repos` (German-80, RESCOS-65)  ⟷  `Tremblements` (German-80) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tremblement postural` (German-80)  ⟷  `Tremblements` (German-80) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Tremblements` (German-80)  ⟷  `Tremblements autres` (RESCOS-65) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antiémétiques` (German-80, RESCOS-65)  ⟷  `Antiépileptiques` (RESCOS-65) — **RESCOS-65, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (German-80, RESCOS-65)  ⟷  `Antécédents médicaux` (German-80) — **German-80, section « a »** distingue ces deux items
- ⛔ `Auscultation cardiaque` (German-80)  ⟷  `Auscultation carotidienne` (German-80) — **German-80, section « e »** distingue ces deux items
- ⛔ `Autres nerfs crâniens` (German-80)  ⟷  `Examen des nerfs crâniens` (German-80) — **German-80, section « e »** distingue ces deux items
- ⛔ `Diagnostic syndromique - syndrome parkinsonien` (RESCOS-65)  ⟷  `Diagnostic étiologique - causes de syndrome parkinsonien` (RESCOS-65) — **RESCOS-65, section « m »** distingue ces deux items
- ⛔ `Dépression` (German-80)  ⟷  `Profession` (German-80) — **German-80, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (German-80)  ⟷  `Facteurs améliorants` (German-80) — **German-80, section « a »** distingue ces deux items
- ⛔ `Facteurs améliorants` (German-80)  ⟷  `Facteurs modulants` (German-80) — **German-80, section « a »** distingue ces deux items
- ⛔ `Modifications capillaires` (German-80)  ⟷  `Modifications cutanées` (German-80) — **German-80, section « a »** distingue ces deux items
- ⛔ `Médicaments` (German-80)  ⟷  `Médicaments récents` (German-80) — **German-80, section « a »** distingue ces deux items
- ⛔ `Neuroleptiques` (German-80, RESCOS-65)  ⟷  `Neurologiques` (German-80) — **German-80, section « a »** distingue ces deux items
- ⛔ `Orientation personnelle` (German-80)  ⟷  `Orientation temporelle` (German-80) — **German-80, section « e »** distingue ces deux items
- ⛔ `Symptômes moteurs associés` (German-80, RESCOS-65)  ⟷  `Symptômes non-moteurs` (German-80) — **German-80, section « a »** distingue ces deux items
- ⛔ `Tremblement de repos` (German-80, RESCOS-65)  ⟷  `Tremblement postural` (German-80) — **German-80, section « e »** distingue ces deux items
- ⛔ `Tremblement de repos` (German-80, RESCOS-65)  ⟷  `Tremblements autres` (RESCOS-65) — **RESCOS-65, section « e »** distingue ces deux items
- ⛔ `Troubles cognitifs` (German-80, RESCOS-65)  ⟷  `Troubles digestifs` (RESCOS-65) — **RESCOS-65, section « a »** distingue ces deux items
- ⛔ `Troubles de l'humeur` (RESCOS-65)  ⟷  `Troubles de la marche` (RESCOS-65) — **RESCOS-65, section « a »** distingue ces deux items

## Trouble Anxieux — 4 cas · 1 à juger (0 de forme, 1 de contenu), 21 ⚠️, 13 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Question d'entrée ouverte` (German-4)  ⟷  `Question d’ouverture` (AZYGOS-2)

- ⚠️ `Anamnèse psychiatrique familiale` (AZYGOS-2)  ⟷  `Maladies psychiatriques familiales` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents d'idées suicidaires` (German-4)  ⟷  `Présence d'idées suicidaires` (RESCOS-12, RESCOS-12b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Arrêt de la pensée` (AZYGOS-2)  ⟷  `Contenu de la pensée` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Arrêt de la pensée` (AZYGOS-2)  ⟷  `Vol de la pensée` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Autres stress récents` (German-4)  ⟷  `Autres troubles perceptifs` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Concentration` (German-4)  ⟷  `Contraception` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `DD idées délirantes` (AZYGOS-2)  ⟷  `Idées délirantes` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Idées obsessionnelles` (German-4)  ⟷  `Impulsions obsessionnelles` (AZYGOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Idées obsessionnelles` (German-4)  ⟷  `Pensées obsessionnelles` (AZYGOS-2) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Limitation` (AZYGOS-2)  ⟷  `Palpitations` (German-4, RESCOS-12, RESCOS-12b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Motivation personnelle` (German-4)  ⟷  `Orientation personnelle` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Orientation personnelle` (German-4)  ⟷  `Ressenti personnel` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Orientation personnelle` (German-4)  ⟷  `Situation professionnelle` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Perte d'emploi` (German-4)  ⟷  `Perte de plaisir` (RESCOS-12, RESCOS-12b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Plans / actes suicidaires` (AZYGOS-2)  ⟷  `Plans ou gestes suicidaires` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Symptômes de panique` (AZYGOS-2)  ⟷  `Symptômes physiques` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Symptômes de panique` (AZYGOS-2)  ⟷  `Symptômes psychiques` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Trouble de la concentration` (RESCOS-12, RESCOS-12b)  ⟷  `Troubles de la conscience` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Trouble de la mémoire` (RESCOS-12, RESCOS-12b)  ⟷  `Troubles de la conscience` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Trouble de la mémoire` (RESCOS-12, RESCOS-12b)  ⟷  `Troubles du moi` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Trouble du sommeil` (RESCOS-12, RESCOS-12b)  ⟷  `Troubles du moi` (German-4) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents d'idées suicidaires` (German-4)  ⟷  `Antécédents de suicide familiaux` (German-4) — **German-4, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux psychiatriques` (German-4)  ⟷  `Antécédents médicaux et psychiatriques` (German-4) — **German-4, section « a »** distingue ces deux items
- ⛔ `Consommation de drogues` (German-4)  ⟷  `Consommation de substances` (AZYGOS-2, German-4) — **German-4, section « a »** distingue ces deux items
- ⛔ `Contenu de la pensée` (German-4)  ⟷  `Vol de la pensée` (German-4) — **German-4, section « e »** distingue ces deux items
- ⛔ `Décès de la sœur` (AZYGOS-2, German-4)  ⟷  `Réaction au décès de la sœur` (German-4) — **German-4, section « a »** distingue ces deux items
- ⛔ `Dépersonnalisation` (German-4)  ⟷  `Déréalisation` (German-4) — **German-4, section « e »** distingue ces deux items
- ⛔ `Hallucinations auditives` (German-4)  ⟷  `Hallucinations visuelles` (German-4) — **German-4, section « e »** distingue ces deux items
- ⛔ `Impact professionnel` (German-4)  ⟷  `Situation professionnelle` (German-4) — **German-4, section « a »** distingue ces deux items
- ⛔ `Impulsions obsessionnelles` (AZYGOS-2)  ⟷  `Pensées obsessionnelles` (AZYGOS-2) — **AZYGOS-2, section « a »** distingue ces deux items
- ⛔ `Motivation personnelle` (German-4)  ⟷  `Situation professionnelle` (German-4) — **German-4, section « a »** distingue ces deux items
- ⛔ `Médicaments actuels` (German-4)  ⟷  `Médicaments psychotropes` (German-4) — **German-4, section « a »** distingue ces deux items
- ⛔ `Symptômes physiques` (German-4)  ⟷  `Symptômes psychiques` (German-4) — **German-4, section « a »** distingue ces deux items
- ⛔ `Troubles du jugement` (German-4)  ⟷  `Troubles du moi` (German-4) — **German-4, section « e »** distingue ces deux items

## Troubles de la Croissance (Retard - Grande taille) — 2 cas · 1 à juger (0 de forme, 1 de contenu), 4 ⚠️, 12 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Anamnèse du développement` (German-72)  ⟷  `Jalons du développement` (AZYGOS-34)

- ⚠️ `Alimentation` (AZYGOS-34)  ⟷  `Alimentation actuelle` (German-72) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Puberté des parents` (AZYGOS-34)  ⟷  `Puberté tardive chez les parents` (German-72) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Taille de la mère` (German-72)  ⟷  `Taille des parents` (AZYGOS-34) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Taille des parents` (AZYGOS-34)  ⟷  `Taille du père` (German-72) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Alcool pendant la grossesse` (German-72)  ⟷  `Infections pendant la grossesse` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Anamnèse alimentaire` (German-72)  ⟷  `Anamnèse digestive` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Anamnèse digestive` (German-72)  ⟷  `Anamnèse infectieuse` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Anamnèse familiale` (German-72)  ⟷  `Anamnèse sociale` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Anamnèse obstétricale` (German-72)  ⟷  `Anamnèse sociale` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Auscultation cardio-pulmonaire` (German-72)  ⟷  `Auscultation pulmonaire` (German-72) — **German-72, section « e »** distingue ces deux items
- ⛔ `Développement langagier` (German-72)  ⟷  `Développement moteur` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Exposition à des substances toxiques` (German-72)  ⟷  `Exposition à des toxiques` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Paramètres de naissance` (German-72)  ⟷  `Terme de naissance` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Poids à la naissance` (German-72)  ⟷  `Taille à la naissance` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Périmètre crânien actuel` (German-72)  ⟷  `Périmètre crânien à la naissance` (German-72) — **German-72, section « a »** distingue ces deux items
- ⛔ `Taille de la mère` (German-72)  ⟷  `Taille du père` (German-72) — **German-72, section « a »** distingue ces deux items

## Troubles du Sommeil — 3 cas · 3 à juger (0 de forme, 3 de contenu), 12 ⚠️, 14 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Autres examens biologiques` (German-82)  ⟷  `Examens biologiques` (AMBOSS-16)
- `Examens biologiques` (AMBOSS-16)  ⟷  `Examens biologiques thyroïdiens` (German-82)
- `Examen ciblé des réflexes ostéo-tendineux` (AMBOSS-16)  ⟷  `Réflexes ostéo-tendineux` (German-82)

- ⚠️ `Activation comportementale` (AZYGOS-49)  ⟷  `Cognition / Comportement` (AZYGOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Agenda du sommeil` (AMBOSS-16)  ⟷  `Anamnèse du sommeil` (AZYGOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Agenda du sommeil` (AMBOSS-16)  ⟷  `Hygiène du sommeil` (AMBOSS-16, AZYGOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Anxiété` (German-82)  ⟷  `DD Anxiété` (AZYGOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AMBOSS-16, German-82)  ⟷  `Examens biologiques` (AMBOSS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen neurologique` (AMBOSS-16, German-82)  ⟷  `Neurologique` (AZYGOS-49) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen ophtalmologique` (German-82)  ⟷  `Examens biologiques` (AMBOSS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Inspection du cou` (German-82)  ⟷  `Inspection du thorax` (AMBOSS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies thyroïdiennes` (German-82)  ⟷  `Palpation thyroïdienne` (German-82) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments` (AMBOSS-16)  ⟷  `Médicaments actuels` (German-82) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Profession` (AZYGOS-49, German-82)  ⟷  `Progression` (AMBOSS-16) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Variations pondérales` (AMBOSS-16)  ⟷  `Évolution pondérale` (German-82) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Alcool avant le coucher` (AMBOSS-16)  ⟷  `Exercice avant le coucher` (AMBOSS-16) — **AMBOSS-16, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-16, German-82)  ⟷  `Antécédents familiaux` (AMBOSS-16, AZYGOS-49, German-82) — **AMBOSS-16, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-16, German-82)  ⟷  `Antécédents médicaux` (AMBOSS-16, AZYGOS-49) — **AMBOSS-16, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-16, German-82)  ⟷  `Antécédents médicaux et chirurgicaux` (AMBOSS-16) — **AMBOSS-16, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-16, AZYGOS-49, German-82)  ⟷  `Antécédents médicaux` (AMBOSS-16, AZYGOS-49) — **AMBOSS-16, section « a »** distingue ces deux items
- ⛔ `Consommation de caféine` (AZYGOS-49)  ⟷  `Consommation de substances` (AZYGOS-49) — **AZYGOS-49, section « a »** distingue ces deux items
- ⛔ `Examen neurologique` (AMBOSS-16, German-82)  ⟷  `Examen ophtalmologique` (German-82) — **German-82, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-16)  ⟷  `Facteurs améliorants` (AMBOSS-16) — **AMBOSS-16, section « a »** distingue ces deux items
- ⛔ `Humeur dépressive` (AZYGOS-49)  ⟷  `Humeur élevée` (AZYGOS-49) — **AZYGOS-49, section « a »** distingue ces deux items
- ⛔ `Inspection des conjonctives` (AMBOSS-16)  ⟷  `Inspection des mains` (AMBOSS-16) — **AMBOSS-16, section « e »** distingue ces deux items
- ⛔ `Médicaments actuels` (German-82)  ⟷  `Médicaments et substances` (German-82) — **German-82, section « a »** distingue ces deux items
- ⛔ `Recherche d'arythmie` (German-82)  ⟷  `Recherche d'exophtalmie` (German-82) — **German-82, section « e »** distingue ces deux items
- ⛔ `Scintigraphie thyroïdienne` (German-82)  ⟷  `Échographie thyroïdienne` (German-82) — **German-82, section « m »** distingue ces deux items
- ⛔ `T3 libre (fT3)` (German-82)  ⟷  `T4 libre (fT4)` (German-82) — **German-82, section « m »** distingue ces deux items

## Vertiges — 2 cas · 2 à juger (0 de forme, 2 de contenu), 5 ⚠️, 15 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Examen neurologique` (AMBOSS-40)  ⟷  `Examen neurologique général` (RESCOS-66)
- `Examens complémentaires` (AMBOSS-40)  ⟷  `Examens complémentaires neurologiques` (RESCOS-66)

- ⚠️ `Alcool` (AMBOSS-40)  ⟷  `Alcoolisme` (RESCOS-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Analyse de l'amaigrissement` (RESCOS-66)  ⟷  `Bilan étiologique de l'amaigrissement` (RESCOS-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Ataxie cérébelleuse` (RESCOS-66)  ⟷  `Dysarthrie cérébelleuse` (RESCOS-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen ciblé des réflexes ostéotendineux` (AMBOSS-40)  ⟷  `Réflexes ostéotendineux` (RESCOS-66) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Manœuvre de Dix-Hallpike` (RESCOS-66)  ⟷  `Test de Dix-Hallpike` (AMBOSS-40) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Antécédents chirurgicaux` (AMBOSS-40)  ⟷  `Antécédents familiaux` (AMBOSS-40) — **AMBOSS-40, section « a »** distingue ces deux items
- ⛔ `Antécédents chirurgicaux` (AMBOSS-40)  ⟷  `Antécédents médicaux` (AMBOSS-40) — **AMBOSS-40, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (AMBOSS-40)  ⟷  `Antécédents médicaux` (AMBOSS-40) — **AMBOSS-40, section « a »** distingue ces deux items
- ⛔ `Caractérisation des vertiges` (AMBOSS-40)  ⟷  `Description des vertiges` (AMBOSS-40) — **AMBOSS-40, section « a »** distingue ces deux items
- ⛔ `Diagnostic syndromique des troubles de l'équilibre` (RESCOS-66)  ⟷  `Diagnostic étiologique - causes des troubles de l'équilibre` (RESCOS-66) — **RESCOS-66, section « m »** distingue ces deux items
- ⛔ `Examen ciblé de la marche` (AMBOSS-40)  ⟷  `Examen ciblé de la sensibilité` (AMBOSS-40) — **AMBOSS-40, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (AMBOSS-40, RESCOS-66)  ⟷  `Facteurs améliorants` (AMBOSS-40) — **AMBOSS-40, section « a »** distingue ces deux items
- ⛔ `Force musculaire` (RESCOS-66)  ⟷  `Tonus musculaire` (RESCOS-66) — **RESCOS-66, section « e »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-40)  ⟷  `Inspection des oreilles` (AMBOSS-40) — **AMBOSS-40, section « e »** distingue ces deux items
- ⛔ `Inspection de la tête` (AMBOSS-40)  ⟷  `Palpation de la tête` (AMBOSS-40) — **AMBOSS-40, section « e »** distingue ces deux items
- ⛔ `Inspection des oreilles` (AMBOSS-40)  ⟷  `Palpation des oreilles` (AMBOSS-40) — **AMBOSS-40, section « e »** distingue ces deux items
- ⛔ `Signes pyramidaux` (RESCOS-66)  ⟷  `Signes vitaux` (RESCOS-66) — **RESCOS-66, section « e »** distingue ces deux items
- ⛔ `Troubles cognitifs` (RESCOS-66)  ⟷  `Troubles digestifs` (RESCOS-66) — **RESCOS-66, section « a »** distingue ces deux items
- ⛔ `Troubles cognitifs` (RESCOS-66)  ⟷  `Troubles sensitifs` (RESCOS-66) — **RESCOS-66, section « a »** distingue ces deux items
- ⛔ `Troubles digestifs` (RESCOS-66)  ⟷  `Troubles sensitifs` (RESCOS-66) — **RESCOS-66, section « a »** distingue ces deux items

## Énurésie Nocturne — 2 cas · 0 à juger (0 de forme, 0 de contenu), 0 ⚠️, 4 ⛔

- ⛔ `Antécédents chirurgicaux` (AZYGOS-25)  ⟷  `Antécédents médicaux` (AZYGOS-25, German-40) — **AZYGOS-25, section « a »** distingue ces deux items
- ⛔ `Fréquence diurne` (German-40)  ⟷  `Fréquence nocturne` (German-40) — **German-40, section « a »** distingue ces deux items
- ⛔ `Moticité des membres inférieurs` (AZYGOS-25)  ⟷  `Sensibilité des membres inférieurs` (AZYGOS-25) — **AZYGOS-25, section « e »** distingue ces deux items
- ⛔ `Mère` (German-40)  ⟷  `Père` (German-40) — **German-40, section « a »** distingue ces deux items

## Éruption Cutanée — 8 cas · 28 à juger (1 de forme, 27 de contenu), 14 ⚠️, 11 ⛔

**À juger — écart de forme** (accord, genre, graphie : réunir n'efface rien)

- `Intention de faire status ORL, pulmonaire ou cardio` (RESCOS-68)  ⟷  `Intention de faire un status ORL, pulmonaire ou cardiaque` (RESCOS-68b)

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Avec les éléments pertinents de l'anamnèse et du status` (RESCOS-68b)  ⟷  `Éléments pertinent de l'anamnèse et du status` (RESCOS-68)
- `Symptômes génitaux` (AZYGOS-26)  ⟷  `Symptômes généraux` (AZYGOS-27)
- `Hypothèse Diagnostique` (RESCOS-68)  ⟷  `Hypothèse diagnostique : ZONA` (RESCOS-68b)
- `Caractéristiques de l'éruption` (German-43)  ⟷  `Caractéristiques des lésions` (German-42)
- `Inspection des lésions` (RESCOS-68, RESCOS-68b)  ⟷  `Inspection des ongles` (AZYGOS-1)
- `Caractéristiques de l'éruption` (German-43)  ⟷  `Caractéristiques de l'érythème` (German-44)
- `Examens complémentaires indiqués` (RESCOS-68, RESCOS-68b)  ⟷  `Examens complémentaires proposés` (German-42, German-43, German-44)
- `Culture bactériologique` (German-43)  ⟷  `Culture mycologique` (German-42)
- `Désinfection des mains, présentation avec nom, fonction et but de la consultation` (German-44)  ⟷  `Se présente avec nom, fonction et but de la consultation` (German-42, German-43)
- `Examen des muqueuses (intention)` (RESCOS-68b)  ⟷  `Examen des muqueuses : Bouche/Nez/OGE (intention)` (RESCOS-68)
- `Inspection cutanée` (AZYGOS-1)  ⟷  `Inspection cutanée détaillée` (German-42)
- `Exploration du symptôme principal` (German-44)  ⟷  `Exploration du symptôme principal : éruption cutanée` (German-42, German-43)
- `Anamnèse sociale et exposition` (German-43)  ⟷  `Anamnèse sociale et professionnelle` (German-42)
- `Mesures préventives et conseils` (German-42)  ⟷  `Mesures préventives et prophylaxie` (German-43)
- `Caractéristiques de l'érythème` (German-44)  ⟷  `Caractéristiques des lésions` (German-42)
- `Antécédents médicaux et traitements` (German-43)  ⟷  `Antécédents médicaux personnels` (German-42)
- `Anamnèse personnelle` (RESCOS-68, RESCOS-68b)  ⟷  `Anamnèse sexuelle` (AZYGOS-26)
- `Inspection cutanée` (AZYGOS-1)  ⟷  `Inspection générale` (German-44)
- `Anamnèse environnementale` (AZYGOS-1)  ⟷  `Anamnèse personnelle` (RESCOS-68, RESCOS-68b)
- `Localisation` (AZYGOS-1, AZYGOS-26, AZYGOS-27, German-44, RESCOS-68, RESCOS-68b)  ⟷  `Localisation précise` (German-42)
- `Anamnèse de voyage et exposition solaire` (German-44)  ⟷  `Anamnèse sociale et exposition` (German-43)
- `Évolution temporelle` (German-42)  ⟷  `Évolution temporelle de l'éruption` (German-43)
- `Anamnèse de varicelle` (RESCOS-68, RESCOS-68b)  ⟷  `Anamnèse sexuelle` (AZYGOS-26)
- `Autres plaintes cutanées` (AZYGOS-27)  ⟷  `Maladies cutanées` (AZYGOS-1)
- `Anamnèse sexuelle` (AZYGOS-26)  ⟷  `Anamnèse sociale` (German-44)
- `Anamnèse personnelle` (RESCOS-68, RESCOS-68b)  ⟷  `Anamnèse sociale` (German-44)
- `Examen articulaire` (German-44)  ⟷  `Statut articulaire` (AZYGOS-1)

- ⚠️ `Caractéristiques des lésions` (German-42)  ⟷  `Frottis des lésions` (RESCOS-68b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `DD Eczéma de contact` (AZYGOS-27)  ⟷  `Dermatite de contact` (RESCOS-68b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Description des lésions` (German-42)  ⟷  `Inspection des lésions` (RESCOS-68, RESCOS-68b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Début & Évolution` (RESCOS-68)  ⟷  `Prurit — début ET évolution` (RESCOS-68b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Exposition solaire` (AZYGOS-26, German-44)  ⟷  `Éviction scolaire` (German-43) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infection préalable` (AZYGOS-1)  ⟷  `Infection récente` (RESCOS-68b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infection secondaire` (AZYGOS-27)  ⟷  `Signes d'infection secondaire` (German-42) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Infection secondaire` (AZYGOS-27)  ⟷  `Éviction scolaire` (German-43) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Localisation précise` (German-42)  ⟷  `Localisation périorale` (AZYGOS-27) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Mal de gorge` (German-43)  ⟷  `Maux de gorge` (AZYGOS-26) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Maladies antérieures` (German-42, German-43)  ⟷  `Maladies cutanées` (AZYGOS-1) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Médicaments actuels` (German-42, German-43, German-44)  ⟷  `Médicaments pris` (RESCOS-68, RESCOS-68b) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Plaintes articulaires` (AZYGOS-1)  ⟷  `Épanchement articulaire` (German-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche de signes de gravité` (German-43)  ⟷  `Recherche de signes de lupus systémique` (German-44) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Allergie` (RESCOS-68, RESCOS-68b)  ⟷  `Allergies` (AZYGOS-1, AZYGOS-26, AZYGOS-27) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Anamnèse de varicelle` (RESCOS-68, RESCOS-68b)  ⟷  `Anamnèse personnelle` (RESCOS-68, RESCOS-68b) — **RESCOS-68, section « a »** distingue ces deux items
- ⛔ `Autres symptômes systémiques` (German-43)  ⟷  `État général et symptômes systémiques` (German-43) — **German-43, section « a »** distingue ces deux items
- ⛔ `Douleur` (German-44)  ⟷  `Douleurs` (AZYGOS-1, AZYGOS-26, RESCOS-68, RESCOS-68b) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Examen articulaire` (German-44)  ⟷  `Examen cardio-pulmonaire` (German-44) — **German-44, section « e »** distingue ces deux items
- ⛔ `Examen articulaire` (German-44)  ⟷  `Épanchement articulaire` (German-44) — **German-44, section « e »** distingue ces deux items
- ⛔ `Facteurs aggravants` (RESCOS-68b)  ⟷  `Facteurs atténuants` (RESCOS-68b) — **RESCOS-68b, section « a »** distingue ces deux items
- ⛔ `Facteurs aggravants` (RESCOS-68b)  ⟷  `⊕ Facteurs aggravants` (AZYGOS-1, AZYGOS-26, AZYGOS-27) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Facteurs aggravants` (RESCOS-68b)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-1, AZYGOS-26, AZYGOS-27) — **AZYGOS-1, section « a »** distingue ces deux items
- ⛔ `Évolution en caractère` (RESCOS-68, RESCOS-68b)  ⟷  `Évolution en nombre` (RESCOS-68, RESCOS-68b) — **RESCOS-68, section « a »** distingue ces deux items
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-1, AZYGOS-26, AZYGOS-27)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-1, AZYGOS-26, AZYGOS-27) — **AZYGOS-1, section « a »** distingue ces deux items

## Œdèmes des Membres Inférieurs — 2 cas · 3 à juger (0 de forme, 3 de contenu), 7 ⚠️, 11 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Pas de reflux hépato-jugulaire` (RESCOS-54)  ⟷  `Reflux hépato-jugulaire` (RESCOS-51)
- `Pas de turgescence jugulaire` (RESCOS-54)  ⟷  `Turgescence jugulaire` (RESCOS-51)
- `Examens complémentaires de première intention` (RESCOS-51)  ⟷  `Examens complémentaires présentés` (RESCOS-54)

- ⚠️ `Caractérisation des œdèmes` (RESCOS-51)  ⟷  `Palpation des œdèmes` (RESCOS-51) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Contexte prise en charge difficile ambulatoirement` (RESCOS-54)  ⟷  `Prise en charge difficile ambulatoirement` (RESCOS-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Dernière tension artérielle` (RESCOS-51)  ⟷  `Tension artérielle` (RESCOS-51) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen des membres inférieurs` (RESCOS-54)  ⟷  `Œdèmes des membres inférieurs` (RESCOS-54) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hypertension artérielle` (RESCOS-51)  ⟷  `Tension artérielle` (RESCOS-51) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Recherche d'épanchements séreux` (RESCOS-51)  ⟷  `Recherche d'événements synchrones` (RESCOS-51) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Éléments cliniques` (RESCOS-54)  ⟷  `Œdèmes cliniques` (RESCOS-51) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Anamnèse par systèmes - Autres` (RESCOS-54)  ⟷  `Anamnèse par systèmes - Cardiovasculaire` (RESCOS-54) — **RESCOS-54, section « a »** distingue ces deux items
- ⛔ `Antécédents familiaux` (RESCOS-51)  ⟷  `Antécédents rénaux` (RESCOS-51) — **RESCOS-51, section « a »** distingue ces deux items
- ⛔ `Bilan étiologique du syndrome néphrotique` (RESCOS-51)  ⟷  `Complications du syndrome néphrotique` (RESCOS-51) — **RESCOS-51, section « m »** distingue ces deux items
- ⛔ `Bilan étiologique du syndrome néphrotique` (RESCOS-51)  ⟷  `Critères diagnostiques du syndrome néphrotique` (RESCOS-51) — **RESCOS-51, section « m »** distingue ces deux items
- ⛔ `Critères diagnostiques du syndrome néphrotique` (RESCOS-51)  ⟷  `Traitement symptomatique du syndrome néphrotique` (RESCOS-51) — **RESCOS-51, section « m »** distingue ces deux items
- ⛔ `Dernière tension artérielle` (RESCOS-51)  ⟷  `Hypertension artérielle` (RESCOS-51) — **RESCOS-51, section « a »** distingue ces deux items
- ⛔ `Infection récente` (RESCOS-51)  ⟷  `Infections récurrentes` (RESCOS-51) — **RESCOS-51, section « a »** distingue ces deux items
- ⛔ `Infection récente` (RESCOS-51)  ⟷  `Vaccination récente` (RESCOS-51) — **RESCOS-51, section « a »** distingue ces deux items
- ⛔ `Inspection des œdèmes` (RESCOS-51)  ⟷  `Palpation des œdèmes` (RESCOS-51) — **RESCOS-51, section « e »** distingue ces deux items
- ⛔ `Prise de médicaments` (RESCOS-51)  ⟷  `Prise de nouveaux médicaments` (RESCOS-51) — **RESCOS-51, section « a »** distingue ces deux items
- ⛔ `Technique main droite` (RESCOS-51)  ⟷  `Technique main gauche` (RESCOS-51) — **RESCOS-51, section « e »** distingue ces deux items

## Œil Rouge & Douleur Oculaire — 4 cas · 10 à juger (0 de forme, 10 de contenu), 18 ⚠️, 21 ⛔

**À juger — écart de contenu** (un mot de contenu diffère : réunir efface une distinction, à examiner de près)

- `Pression intraoculaire` (German-88)  ⟷  `Pression oculaire` (AZYGOS-45)
- `Examen à la lampe à fente` (German-88)  ⟷  `Propose un examen à la lampe à fente` (RESCOS-32)
- `Examen pupillaire` (German-88)  ⟷  `Réflexe pupillaire` (RESCOS-32)
- `Symptômes associés` (AZYGOS-10)  ⟷  `Symptômes oculaires associés` (German-88)
- `Acuité visuelle` (AZYGOS-10, AZYGOS-45)  ⟷  `Baisse d’acuité visuelle` (AZYGOS-45)
- `Anamnèse familiale d'allergie` (German-88)  ⟷  `Anamnèse familiale de glaucome` (AZYGOS-10)
- `Examen monoculaire` (AZYGOS-10)  ⟷  `Examen pupillaire` (German-88)
- `Palpation oculaire` (RESCOS-32)  ⟷  `Pression oculaire` (AZYGOS-45)
- `Antécédents familiaux` (AZYGOS-45)  ⟷  `Antécédents généraux` (AZYGOS-10)
- `Palpation du globe` (AZYGOS-10)  ⟷  `Palpation oculaire` (RESCOS-32)

- ⚠️ `Acuité visuelle` (AZYGOS-10, AZYGOS-45)  ⟷  `Baisse d'acuité visuelle` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Aide visuelle utilisée` (AZYGOS-10)  ⟷  `Aides visuelles` (AZYGOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Antécédents` (AZYGOS-10, AZYGOS-45)  ⟷  `Antécédents d'IST` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Baisse d'acuité visuelle` (German-88)  ⟷  `Mesure de l'acuité visuelle` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Baisse d’acuité visuelle` (AZYGOS-45)  ⟷  `Mesure de l'acuité visuelle` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Douleurs articulaires` (AZYGOS-45)  ⟷  `Douleurs oculaires` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Examen ORL complémentaire` (German-88)  ⟷  `Examens complémentaires` (AZYGOS-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Expression` (AZYGOS-45)  ⟷  `Profession` (AZYGOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hygiène des bords palpébraux` (AZYGOS-45)  ⟷  `Plaintes des bords palpébraux` (AZYGOS-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Hygiène palpébrale` (German-88)  ⟷  `Œdème palpébral` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Information sur le risque de cécité` (AZYGOS-10)  ⟷  `Information sur les risques` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Intégration sociale` (German-88)  ⟷  `Situation sociale` (AZYGOS-10, AZYGOS-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `La périphérie` (RESCOS-32)  ⟷  `Périphérique` (AZYGOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Larmoiement` (German-88)  ⟷  `Larmoiement associé` (AZYGOS-45) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Les 4 quadrants` (RESCOS-32)  ⟷  `Test des quadrants` (AZYGOS-10) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Photophobie` (AZYGOS-10, German-88)  ⟷  `Photophobie marquée` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Port de lunettes de soleil` (German-88)  ⟷  `Port de lunettes/lentilles` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⚠️ `Qualité` (AZYGOS-10)  ⟷  `Quantité` (German-88) — **inerte** : ces deux titres ne vivent pas au même endroit (section ou parent différents), l'entrée ne réunirait rien
- ⛔ `Acuité visuelle` (AZYGOS-10, AZYGOS-45)  ⟷  `Aides visuelles` (AZYGOS-10) — **AZYGOS-10, section « a »** distingue ces deux items
- ⛔ `Antécédents généraux` (AZYGOS-10)  ⟷  `Médicaments généraux` (AZYGOS-10) — **AZYGOS-10, section « a »** distingue ces deux items
- ⛔ `Aspect des paupières` (German-88)  ⟷  `Examen des paupières` (German-88) — **German-88, section « e »** distingue ces deux items
- ⛔ `Auscultation systématique antérieure` (German-88)  ⟷  `Auscultation systématique postérieure` (German-88) — **German-88, section « e »** distingue ces deux items
- ⛔ `Avec correction` (German-88)  ⟷  `Sans correction` (German-88) — **German-88, section « e »** distingue ces deux items
- ⛔ `Baisse d'acuité visuelle` (German-88)  ⟷  `Baisse d’acuité visuelle` (AZYGOS-45) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Changements récents d'environnement` (German-88)  ⟷  `Changements récents de produits` (German-88) — **German-88, section « a »** distingue ces deux items
- ⛔ `Clinique ophtalmologique` (AZYGOS-10)  ⟷  `Transfert en clinique ophtalmologique` (AZYGOS-10) — **AZYGOS-10, section « m »** distingue ces deux items
- ⛔ `Convergence` (RESCOS-32)  ⟷  `À la convergence` (RESCOS-32) — **même signature socle A**, déjà appariés dans leur section
- ⛔ `Céphalée` (AZYGOS-10)  ⟷  `DD-céphalée` (AZYGOS-10) — **AZYGOS-10, section « a »** distingue ces deux items
- ⛔ `Examen des paupières` (German-88)  ⟷  `Examen des paupières et cils` (German-88) — **German-88, section « e »** distingue ces deux items
- ⛔ `Mobilité de la face (VII)` (RESCOS-32)  ⟷  `Sensibilité de la face (V)` (RESCOS-32) — **RESCOS-32, section « e »** distingue ces deux items
- ⛔ `Médio-périphérique` (AZYGOS-10)  ⟷  `Périphérique` (AZYGOS-10) — **AZYGOS-10, section « e »** distingue ces deux items
- ⛔ `Port de lentilles` (German-88, RESCOS-32)  ⟷  `Port de lunettes/lentilles` (German-88) — **German-88, section « a »** distingue ces deux items
- ⛔ `Rhinite allergique` (German-88)  ⟷  `Rhinite allergique familiale` (German-88) — **German-88, section « a »** distingue ces deux items
- ⛔ `Réaction consensuelle à la lumière` (AZYGOS-10)  ⟷  `Réaction directe à la lumière` (AZYGOS-10) — **AZYGOS-10, section « e »** distingue ces deux items
- ⛔ `Segment antérieur de l’œil` (AZYGOS-10)  ⟷  `Segment postérieur de l’œil` (AZYGOS-10) — **AZYGOS-10, section « a »** distingue ces deux items
- ⛔ `Sous paupière inférieure` (RESCOS-32)  ⟷  `Sous paupière supérieure` (RESCOS-32) — **RESCOS-32, section « e »** distingue ces deux items
- ⛔ `Symptômes ORL et respiratoires associés` (German-88)  ⟷  `Symptômes oculaires associés` (German-88) — **German-88, section « a »** distingue ces deux items
- ⛔ `Symptômes généraux` (German-88)  ⟷  `Symptômes urogénitaux` (German-88) — **German-88, section « a »** distingue ces deux items
- ⛔ `⊕ Facteurs aggravants` (AZYGOS-10)  ⟷  `⊖ Facteurs soulageants` (AZYGOS-10) — **AZYGOS-10, section « a »** distingue ces deux items

## ⚠️ Antonymes présumés — la classe que rien n'automatise

Aucune grille ne porte ces libellés **ensemble**, donc la propriété 8
n'a pas de témoin et ne peut rien dire. Le filtre lexical les signale ;
il ne les juge pas, et il ne prétend pas les avoir tous.

- **Douleur Thoracique** — `Facteurs aggravants` ⟷ `Facteurs soulageants` *(aggravant / soulageant)* — par ailleurs inerte
- **Douleur de Hanche** — `Facteurs aggravants` ⟷ `⊖ Facteurs soulageants` *(aggravant / soulageant)* — par ailleurs inerte
- **Douleur de Hanche** — `Test FABER (Flexion-Abduction-External-Rotation)` ⟷ `Test FADER-R (Flexion Adduction External Rotation - Resisted)` *(abduction / adduction)* — par ailleurs inerte
- **Dyspnée** — `Auscultation antérieure complète` ⟷ `Auscultation postérieure systématique` *(anterieur / posterieur)* — par ailleurs inerte
- **Lombalgies** — `Fracture atraumatique` ⟷ `Fracture vertébrale traumatique` *(préfixe privatif « a- »)* — par ailleurs inerte
- **Palpitations** — `Signes d'hyperthyroïdie` ⟷ `Signes d'hypothyroïdie` *(hyper / hypo)* — **l'entrée mordrait**
- **Toux** — `Asymétrie thoracique` ⟷ `Symétrie thoracique` *(préfixe privatif « a- »)* — par ailleurs inerte
- **Toux** — `Tabagisme actif` ⟷ `Tabagisme passif` *(actif / passif)* — par ailleurs inerte

