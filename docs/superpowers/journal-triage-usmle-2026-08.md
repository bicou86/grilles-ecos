# Journal — campagne images sur les corpus `triage` et `usmle`

Corpus : `cases/triage` (40 grilles) et `cases/usmle` (44). Menée par six lots
(T1-T3, U1-U3) à périmètres disjoints, sur consigne commune unique.

Ces deux corpus **n'avaient jamais été refondus** — dernière modification le
25 mai, à l'import. Ils n'ont ni outillage propre (`scripts/triage/`,
`scripts/usmle/` n'existent pas), ni journal antérieur.

---

## 1. Résultat

| | triage | usmle |
|---|---|---|
| Grilles | 40 | 44 |
| Balisées | **40 / 40** | **44 / 44** |
| Densité | **1/9,28** | **1/9,05** |
| Illustrées | 37 | 42 |
| Images | 104 fichiers, 118 références | 113 fichiers, 124 références |
| Spans imbriqués · `<div>` déséquilibrés · spans hors zone | **0 · 0 · 0** | **0 · 0 · 0** |

Barème vérifié intact sur les 84 grilles, contre la révision `e7644fb` figée
avant la campagne : `window.caseConfig` identique à l'octet près, comptes
inchangés de `criteria-text`, `<input>`, `<label>`, `<span class="score">`,
radios, cases à cocher et `<li>`.

`fetch_image --verify` : aucun lien cassé, aucune orpheline sur les deux corpus.

---

## 2. Vérifier sans outillage

Faute de `check_invariants.py` et `check_no_loss.py`, la consigne a prescrit
**les contrôles équivalents, écrits à la main par chaque lot**. Ils portent sur
les mêmes propriétés : le bloc `caseConfig` comparé octet pour octet vaut le
`maxScores` d'un baseline, les comptes de balises valent `criteriaCount` et
`radioCount`, le nombre de `<li>` vaut `check_no_loss`.

Écrire l'outillage complet de deux corpus aurait coûté plus cher que le contrôle
direct sur 84 grilles. Le choix serait inverse au-delà d'une centaine.

### Trois pièges de méthode, tous trouvés par les lots eux-mêmes

- **Le strip-back contre `git show HEAD:` devient faux dès le premier commit du
  lot** : HEAD contient alors la version balisée, et les grilles déjà validées
  « échouent ». Il faut **figer une révision de base avant la première
  écriture**. Trouvé par T3, relayé aux cinq autres, appliqué par tous sans
  qu'aucun ne revienne à tort sur son travail.
- **Un vérificateur peut passer à vide.** Le `verify.py` de U1, invoqué avec le
  seul `--base=…`, filtrait l'argument après avoir appliqué le défaut : il
  validait **zéro grille** en affichant « tout passe ». C'est le défaut le plus
  dangereux d'un contrôle — ne rien examiner en le disant avec assurance. D'où
  l'exigence, dans les rapports, de chiffres par grille plutôt que d'un OK
  global.
- **`<[^>]*>` n'est pas un motif de balise, et le piège vaut à l'écriture.** La
  consigne le signalait pour la mesure ; T2 a découvert qu'il fausse aussi le
  marquage — sur Triage-27, `« Hb<10 ou plaq<100 … >` a avalé un pan entier de
  l'`annexe-theorie`. Il a repris les trois grilles concernées : **résultat
  identique à l'octet près**, le bug ne pouvant que sur-protéger. La
  vérification a permis de l'affirmer plutôt que de le supposer.

### Un défaut du dispositif, pas des agents

Le scratchpad fourni aux six lots **n'avait aucun espace de noms**. Les fichiers
`mark.py` et `plate.py` de U2 ont été écrasés par un autre lot en cours
d'exécution. L'erreur fut bruyante — le fichier arrivé importait un module
inexistant — mais son avertissement est juste : à signature d'appel identique,
la collision aurait produit des écritures silencieusement fausses. Les lots se
sont isolés dans des sous-répertoires nommés, et U3 a repassé au strip-back les
13 grilles déjà écrites après son déplacement.

---

## 3. Ce que le contrôle visuel a encore trouvé

Onze discordances nom/contenu de plus, versées à
`docs/superpowers/defauts-vault-2026-08.md`. La plus conséquente :

**`neuro-morsure-laterale-de-la-langue-syncope-vs-epilepsie.jpg`** annonce une
morsure **latérale** et une comparaison ; le fichier montre un cliché unique
d'érosions de la **pointe**. Or le siège est précisément ce qui discrimine —
bord latéral vers l'épilepsie, pointe vers la syncope. Légender selon le nom
aurait enseigné l'inverse du signe.

Et un cas d'indécision assumée : **`orl-otoscopie-tympan-normal.jpg`** est donnée
par sa page comme tympan normal de référence. Membrane rosée, opaque, convexité
pâle sur la moitié inférieure, ni manche du marteau ni triangle lumineux. Le lot
n'a pas pu trancher entre normal mal éclairé et bombé : image posée, discordance
écrite dans la légende.

**Une méthode nouvelle** : `qlmanage -t` rend les SVG en PNG. Les campagnes
antérieures les écartaient faute de pouvoir les regarder — leurs glyphes sont
souvent vectorisés, donc invisibles à toute recherche textuelle.

---

## 4. Nomenclature — ne pas aggraver ce qu'on ne corrige pas

Ces corpus portent **307 termes non suisses préexistants** (166 NFS, 59 g/dL,
55 mg/dL, 13 ANA, 4 PCI…). Les corriger était hors mandat, et l'essentiel vit
dans les sections notées où toute édition est interdite.

La consigne imposait donc de **n'en ajouter aucun**. Un lot a intercepté une
occurrence de « NFS » glissée dans une de ses propres légendes, reformulée en
« formule sanguine complète avec CRP et VS ». Les six lots ont passé leurs
légendes au crible : aucun terme non suisse introduit.

---

## 5. Grilles restées sans planche

Cinq au total, toutes par absence de source et non par oubli :

- **Triage-39**, **Triage-40**, **USMLE-34**, **USMLE-9** — leurs pages
  (`SSP — Capacité de Discernement & Éthique`, `SSP — Intoxications Aiguës`) ne
  citent **que des PDF, aucune image**.
- **Triage-30** — `SSP — Œdème Scrotal` ne cite qu'un PDF. Or
  `SSP — Douleur Testiculaire` existe et porte cinq images utilisables : c'est
  le seul cas du relevé où la page de remplacement est identifiée et
  immédiatement disponible.

`SSP — Capacité de Discernement & Éthique` prive désormais **sept grilles** sur
quatre corpus. Dans chacun de ces cas l'appariement est juste : c'est la page
qui n'a aucune iconographie. Voir
`docs/superpowers/mappings-a-revoir-2026-08.md` § 6.
