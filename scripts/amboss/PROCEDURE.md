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

## 4. Aligner les prises en charge

Trois cas, et trois seulement :

| Situation | Action |
|---|---|
| La page SSP traite le point et la grille en diverge | Aligner sur la page SSP, journaliser avec la ligne source |
| La page SSP ne traite pas le point | Laisser inchangé. **Ne rien inventer** |
| Contradiction de fond non tranchable sans avis clinique | Laisser inchangé, consigner au journal |

L'alignement ne concerne **que les blocs pédagogiques**. Toute divergence repérée
dans une section notée est consignée, jamais corrigée — le barème est gelé.

## 5. Journaliser

Ajouter une entrée dans `docs/superpowers/journal-amboss-2026-07.md` au format
défini en tête de ce fichier.

## 6. Vérifier

```bash
python3 scripts/amboss/check_invariants.py    # doit sortir OK
python3 scripts/amboss/check_nomenclature.py  # doit sortir OK
```

## Interdits

- Lire un fichier de grille en entier (jusqu'à 2,77 Mo).
- Réécrire un fichier complet — utiliser le remplacement exact de chaîne.
- Modifier `.criteria-text` : le format `N. Libellé [réponse]` est requis par
  `cases/scoring.js:159`.
- Retirer les crochets `[...]` des réponses patient (`cases/scoring.js:290`).
- Ajouter ou retirer un sous-item noté.
- Toucher aux items ICE du critère `m4`.
- Créer un bloc `resume` ou `presentation` absent.
