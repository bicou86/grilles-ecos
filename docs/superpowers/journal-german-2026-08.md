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
