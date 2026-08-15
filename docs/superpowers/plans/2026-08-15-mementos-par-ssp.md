# Mémentos ECOS par SSP — Plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produire un mémento Obsidian par SSP, fusionnant les 257 grilles RESCOS, AMBOSS, GERMAN et AZYGOS, avec les items d'anamnèse et de status mis en commun et le management subdivisé par diagnostic.

**Architecture:** Une chaîne en quatre couches, chacune dans son module et testable seule — lecture (HTML et JSON AZYGOS → structure de cas), résolution du diagnostic (cascade à trois niveaux), fusion (normalisation lexicale puis vocabulaire canonique curé), rendu (callouts Obsidian). L'orchestration lit le rattachement SSP depuis `docs/obsidian-mapping.yaml`. Deux tables curées à la main — `docs/ecos-diagnostics.yaml` et `docs/ecos-vocabulaire.yaml` — sont relues par un humain entre les étapes.

**Tech Stack:** Python 3 (bibliothèque standard uniquement — **ni PyYAML ni pytest ne sont disponibles**), Markdown Obsidian.

**Spec:** `docs/superpowers/specs/2026-08-15-mementos-par-ssp-design.md`

## Global Constraints

- **Bibliothèque standard seule.** `import yaml` échoue, `import pytest` échoue. Aucune dépendance à installer.
- **Vérification par `check_*.py`.** Convention du dépôt : un script qui imprime un rapport lisible et sort en `0` si tout va bien, `1` sinon. Pas de framework de test. Le cycle est : écrire le checker qui échoue → implémenter → le checker passe → commit.
- **Idempotence.** Deux exécutions consécutives d'un générateur produisent des fichiers identiques à l'octet près.
- **Non-régression absolue.** `docs/obsidian-memento/Mémento ECOS — Grilles officielles.md` doit rester identique à l'octet près jusqu'à la tâche 8 incluse. Son empreinte de référence est figée en tâche 2.
- **Pas de `Date.now()` ni d'aléa** dans les générateurs : la sortie ne dépend que des sources.
- **Les neuf grilles officielles font autorité** sur la granularité, l'ossature, le vocabulaire et les règles d'exclusion (spec § « Les neuf grilles officielles comme référentiel »).
- **Français dans les sorties utilisateur**, commentaires de code en français sans accents (convention des scripts existants).
- **Structure de données pivot**, produite par la couche lecture et consommée par tout le reste :

```python
# Un cas
{
    "id": "AMBOSS-1",                      # identifiant court, unique
    "corpus": "amboss",                    # amboss | german | rescos | azygos
    "fichier": "cases/amboss/AMBOSS-1_….html",
    "ssp": "Douleur Abdominale",           # None si non rattache
    "diagnostic": "Cholecystite aigue",    # None si non resolu
    "confiance": "premier-dd",             # explicite | premier-dd | diagnostic-travail | absent
    "sections": {"a": [Ligne, ...], "e": [...], "m": [...]},
}

# Une ligne, deux formes exactement
("titre", None,  "Autres symptomes associes", None)      # sous-titre de section
("item",  "a3",  "Symptomes B associes", ["Fievre", "Variation de poids"])
```

---

## Structure des fichiers

| Fichier | Responsabilité |
|---|---|
| `scripts/memento/lib_yaml.py` | Lecteur YAML minimal, deux formes seulement |
| `scripts/memento/lib_extraction.py` | HTML → cas ; JSON AZYGOS → cas |
| `scripts/memento/lib_ssp.py` | Rattachement cas → SSP, spécialité, priorité |
| `scripts/memento/lib_diagnostic.py` | Cascade de résolution du diagnostic |
| `scripts/memento/lib_fusion.py` | Normalisation, appariement, marquage |
| `scripts/memento/lib_rendu.py` | Rendu Markdown / callouts Obsidian |
| `scripts/memento/build_memento.py` | Orchestration |
| `scripts/memento/check_couverture.py` | Tout cas est extrait et rattaché, ou listé |
| `scripts/memento/check_referentiel.py` | Écart au corpus officiel |
| `scripts/memento/check_fusion.py` | Idempotence, non-régression, comptages |
| `docs/ecos-diagnostics.yaml` | Table curée : cas → diagnostic + confiance |
| `docs/ecos-vocabulaire.yaml` | Table curée : libellé brut → forme canonique, par SSP |

`scripts/build_obsidian_memento.py` reste en place et fonctionnel jusqu'à la tâche 8, où `build_memento.py` le remplace.

---

## ÉTAPE 1 — Généraliser l'extraction

### Task 1: Lecteur YAML minimal

**Files:**
- Create: `scripts/memento/lib_yaml.py`
- Create: `scripts/memento/check_yaml.py`

**Interfaces:**
- Consumes: rien
- Produces: `lire_plat(chemin) -> dict[str, str]`, `lire_groupe(chemin) -> dict[str, dict[str, str]]`

- [ ] **Step 1: Écrire le checker qui échoue**

Créer `scripts/memento/check_yaml.py` :

```python
"""Verifie le lecteur YAML minimal sur des cas construits. Sortie 1 si ecart."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml

PLAT = '''# commentaire ignore
"RESCOS-12b": Trouble panique
AMBOSS-1: "Cholecystite aigue"

GERMAN-5: Contusion   # commentaire de fin de ligne
'''

GROUPE = '''"Douleur Thoracique":
  "Caracterisation de la douleur": Caracterisation de la douleur
  Douleurs: Caracterisation de la douleur
"Fatigue":
  "Formule sanguine complete": FSC
'''


def ecrire(texte):
    f = tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False, encoding="utf8")
    f.write(texte)
    f.close()
    return Path(f.name)


def main():
    ecarts = []
    plat = lib_yaml.lire_plat(ecrire(PLAT))
    attendu = {"RESCOS-12b": "Trouble panique", "AMBOSS-1": "Cholecystite aigue",
               "GERMAN-5": "Contusion"}
    if plat != attendu:
        ecarts.append(f"lire_plat\n    attendu : {attendu}\n    obtenu  : {plat}")

    groupe = lib_yaml.lire_groupe(ecrire(GROUPE))
    attendu = {"Douleur Thoracique": {"Caracterisation de la douleur": "Caracterisation de la douleur",
                                      "Douleurs": "Caracterisation de la douleur"},
               "Fatigue": {"Formule sanguine complete": "FSC"}}
    if groupe != attendu:
        ecarts.append(f"lire_groupe\n    attendu : {attendu}\n    obtenu  : {groupe}")

    if lib_yaml.lire_plat(Path("/inexistant.yaml")) != {}:
        ecarts.append("un fichier absent doit rendre un dictionnaire vide")

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — lecteur YAML conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Lancer le checker pour vérifier qu'il échoue**

Run: `python3 scripts/memento/check_yaml.py`
Expected: `ModuleNotFoundError: No module named 'lib_yaml'`

- [ ] **Step 3: Écrire le lecteur**

Créer `scripts/memento/lib_yaml.py` :

```python
"""Lecteur YAML minimal — PyYAML n'est pas disponible dans cet environnement.

Deux formes SEULEMENT sont acceptees, celles des deux tables curees du projet :

    cle: valeur                      -> lire_plat
    groupe:                          -> lire_groupe
      cle: valeur

Tout le reste du YAML (listes, ancres, multilignes, imbrication profonde) est
hors perimetre et leve une erreur explicite plutot que d'etre mal interprete.
"""
import re

LIGNE = re.compile(r'^(?P<indent>\s*)(?P<cle>"[^"]+"|[^:#]+?)\s*:\s*(?P<val>.*?)\s*$')


def _valeur(brut):
    """Retire le commentaire de fin de ligne et les guillemets."""
    if not brut.startswith('"'):
        brut = brut.split("#")[0].strip()
    return brut.strip().strip('"')


def _cle(brut):
    return brut.strip().strip('"')


def _lignes(chemin):
    try:
        texte = open(chemin, encoding="utf8").read()
    except FileNotFoundError:
        return
    for numero, ligne in enumerate(texte.splitlines(), 1):
        if not ligne.strip() or ligne.lstrip().startswith("#"):
            continue
        m = LIGNE.match(ligne)
        if not m:
            raise ValueError(f"{chemin}:{numero} — ligne non reconnue : {ligne!r}")
        yield numero, len(m.group("indent")), _cle(m.group("cle")), _valeur(m.group("val"))


def lire_plat(chemin):
    """`cle: valeur` sur un seul niveau."""
    out = {}
    for numero, indent, cle, val in _lignes(chemin):
        if indent:
            raise ValueError(f"{chemin}:{numero} — indentation inattendue")
        out[cle] = val
    return out


def lire_groupe(chemin):
    """`groupe:` puis `cle: valeur` indentes."""
    out, courant = {}, None
    for numero, indent, cle, val in _lignes(chemin):
        if indent == 0:
            if val:
                raise ValueError(f"{chemin}:{numero} — un groupe ne porte pas de valeur")
            courant = out.setdefault(cle, {})
        else:
            if courant is None:
                raise ValueError(f"{chemin}:{numero} — entree hors groupe")
            courant[cle] = val
    return out
```

- [ ] **Step 4: Lancer le checker pour vérifier qu'il passe**

Run: `python3 scripts/memento/check_yaml.py`
Expected: `OK — lecteur YAML conforme`

- [ ] **Step 5: Commit**

```bash
git add scripts/memento/lib_yaml.py scripts/memento/check_yaml.py
git commit -m "Dote le projet memento d'un lecteur YAML minimal

PyYAML n'est pas installe et le depot n'a jamais parse obsidian-mapping.yaml
avec une bibliotheque. Les deux tables curees a venir sont en YAML pour rester
editables a la main ; ce lecteur en couvre les deux seules formes utilisees et
leve une erreur explicite sur tout le reste, plutot que d'interpreter de
travers."
```

---

### Task 2: Extraction HTML commune, sans régression

**Files:**
- Create: `scripts/memento/lib_extraction.py`
- Create: `scripts/memento/check_fusion.py`
- Modify: `scripts/build_obsidian_memento.py` (importe désormais la lib)

**Interfaces:**
- Consumes: rien
- Produces: `lire_html(chemin) -> dict` (structure pivot, `ssp`/`diagnostic` à `None`), `propre(fragment) -> str`, `SYNTHESE` (regex)

- [ ] **Step 1: Figer l'empreinte de non-régression**

Run:
```bash
md5 -q "docs/obsidian-memento/Mémento ECOS — Grilles officielles.md" > /tmp/memento-ref.md5
cat /tmp/memento-ref.md5
```
Noter la valeur : elle est recopiée en dur à l'étape suivante.

- [ ] **Step 2: Écrire le checker de non-régression, qui échoue**

Créer `scripts/memento/check_fusion.py` — remplacer `EMPREINTE` par la valeur relevée :

```python
"""Non-regression et idempotence des mementos. Sortie 1 si ecart."""
import hashlib
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OFFICIEL = REPO / "docs" / "obsidian-memento" / "Mémento ECOS — Grilles officielles.md"
EMPREINTE = "REMPLACER_PAR_LA_VALEUR_RELEVEE"


def md5(chemin):
    return hashlib.md5(chemin.read_bytes()).hexdigest()


def main():
    ecarts = []
    if not OFFICIEL.exists():
        print("ECHEC — le memento officiel a disparu")
        return 1

    avant = md5(OFFICIEL)
    if avant != EMPREINTE:
        ecarts.append(f"le memento officiel a change\n    attendu : {EMPREINTE}\n    obtenu  : {avant}")

    subprocess.run([sys.executable, str(REPO / "scripts" / "build_obsidian_memento.py")],
                   check=True, capture_output=True)
    if md5(OFFICIEL) != avant:
        ecarts.append("le generateur n'est pas idempotent")

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — memento officiel inchange, generateur idempotent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 3: Lancer le checker pour vérifier qu'il échoue**

Run: `python3 scripts/memento/check_fusion.py`
Expected: `ECHEC — 1 ecart(s)` avec `attendu : REMPLACER_PAR_LA_VALEUR_RELEVEE`

- [ ] **Step 4: Remplacer `EMPREINTE` par la valeur relevée et vérifier que le checker passe**

Run: `python3 scripts/memento/check_fusion.py`
Expected: `OK — memento officiel inchange, generateur idempotent`

- [ ] **Step 5: Extraire la logique de lecture dans la lib**

Créer `scripts/memento/lib_extraction.py` en y **déplaçant sans les modifier** les fonctions `propre`, `sections`, `items` de `scripts/build_obsidian_memento.py`, et en ajoutant l'enveloppe :

```python
"""Lecture d'une grille -> structure de cas pivot.

Les fonctions `propre`, `sections` et `items` viennent de
`scripts/build_obsidian_memento.py`, ou elles ont ete eprouvees sur les neuf
grilles officielles. Elles sont deplacees ici sans modification : le memento
officiel doit rester identique a l'octet pres.
"""
import html as H
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

SYNTHESE = re.compile(r"en g[ée]n[ée]ral", re.I)

# [copier ici propre(), sections(), items() a l'identique depuis
#  scripts/build_obsidian_memento.py, ainsi que NOMENCLATURE, FUSIONS,
#  REDONDANTS, sans_accent() et harmonise() dont elles dependent]


def identifiant(chemin):
    """« AMBOSS-1 » depuis un nom de fichier de grille."""
    nom = Path(chemin).name
    m = re.match(r"([A-Z]+-\d+[a-z]?)", nom)
    return m.group(1) if m else Path(chemin).stem[:40]


def lire_html(chemin):
    """Grille HTML -> structure de cas pivot (ssp et diagnostic a None)."""
    chemin = Path(chemin)
    texte = unicodedata.normalize("NFC", chemin.read_text(encoding="utf8", errors="replace"))
    corps = texte[texte.index("<body"):]
    return {
        "id": identifiant(chemin),
        "corpus": chemin.parent.name,
        "fichier": str(chemin.relative_to(REPO)),
        "ssp": None,
        "diagnostic": None,
        "confiance": "absent",
        "sections": {p: items(b) for p, b in sections(corps).items()},
    }
```

- [ ] **Step 6: Faire pointer le générateur existant sur la lib**

Dans `scripts/build_obsidian_memento.py`, remplacer les définitions de `propre`, `sections`, `items`, `harmonise`, `sans_accent`, `NOMENCLATURE`, `FUSIONS`, `REDONDANTS`, `SYNTHESE` par :

```python
sys.path.insert(0, str(Path(__file__).parent / "memento"))
from lib_extraction import (propre, sections, items, harmonise,  # noqa: E402
                            sans_accent, SYNTHESE, NOMENCLATURE,
                            FUSIONS, REDONDANTS)
```

- [ ] **Step 7: Vérifier qu'aucune régression n'est introduite**

Run: `python3 scripts/memento/check_fusion.py`
Expected: `OK — memento officiel inchange, generateur idempotent`

- [ ] **Step 8: Vérifier l'extraction sur un cas de chaque corpus**

Run:
```bash
python3 -c "
import sys; sys.path.insert(0,'scripts/memento')
import lib_extraction as L
for f in ['cases/amboss/AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS.html',
          'cases/rescos/RESCOS-58b - Rectorragies - Grille ECOS.html']:
    c = L.lire_html(f)
    print(c['id'], c['corpus'], {k: len(v) for k, v in c['sections'].items()})
"
```
Expected: deux lignes, chacune avec des sections non vides.

- [ ] **Step 9: Commit**

```bash
git add scripts/memento/lib_extraction.py scripts/memento/check_fusion.py scripts/build_obsidian_memento.py
git commit -m "Extrait la lecture des grilles dans une bibliotheque

La logique eprouvee sur les neuf grilles officielles va servir aux 257 autres :
elle est deplacee dans scripts/memento/lib_extraction.py sans une modification,
et le generateur existant l'importe. check_fusion.py fige l'empreinte du memento
officiel — il doit rester identique a l'octet pres a chaque etape suivante."
```

---

### Task 3: Lecteur AZYGOS (JSON)

**Files:**
- Modify: `scripts/memento/lib_extraction.py`
- Create: `scripts/memento/check_azygos.py`

**Interfaces:**
- Consumes: `lire_html`, structure pivot de la tâche 2
- Produces: `lire_azygos(chemin_json) -> dict` (même structure pivot)

- [ ] **Step 1: Écrire le checker qui échoue**

Créer `scripts/memento/check_azygos.py` :

```python
"""Verifie l'extraction AZYGOS depuis .azygos-extraction/. Sortie 1 si ecart."""
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L

REPO = Path(__file__).resolve().parents[2]
ONGLETS = {"Anamnèse": "a", "Examen clinique": "e", "Diagnostic": "m", "Procédure": "m"}


def main():
    fichiers = sorted(glob.glob(str(REPO / ".azygos-extraction" / "*.json")))
    if not fichiers:
        print("ECHEC — .azygos-extraction/ est vide ou absent")
        return 1

    ecarts, sans_items, longs = [], [], []
    for f in fichiers:
        cas = L.lire_azygos(f)
        if not cas["id"].startswith("AZYGOS"):
            ecarts.append(f"{f}: identifiant inattendu {cas['id']}")
        total = sum(len(v) for v in cas["sections"].values())
        if total == 0:
            sans_items.append(cas["id"])
        for lignes in cas["sections"].values():
            for genre, _, titre, _ in lignes:
                if genre == "item" and len(titre.split()) > 12:
                    longs.append(f"{cas['id']}: {titre[:60]}")

    if sans_items:
        ecarts.append(f"{len(sans_items)} extraction(s) sans aucun item : {sans_items[:5]}")
    if longs:
        ecarts.append(f"{len(longs)} titre(s) de plus de 12 mots — le pave didactique "
                      f"n'a pas ete separe : {longs[:3]}")

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print(f"OK — {len(fichiers)} extractions AZYGOS, granularite conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Lancer le checker pour vérifier qu'il échoue**

Run: `python3 scripts/memento/check_azygos.py`
Expected: `AttributeError: module 'lib_extraction' has no attribute 'lire_azygos'`

- [ ] **Step 3: Écrire le lecteur AZYGOS**

Ajouter à `scripts/memento/lib_extraction.py` :

```python
import json

# Les onglets AZYGOS, ramenes aux trois sections du memento. « Diagnostic »
# porte les examens complementaires, « Procedure » le raisonnement et le
# traitement : les deux alimentent le management.
ONGLETS_AZYGOS = {"Anamnèse": "a", "Examen clinique": "e",
                  "Diagnostic": "m", "Procédure": "m"}


def lire_azygos(chemin):
    """Extraction JSON AZYGOS -> structure de cas pivot.

    Le HTML d'AZYGOS fond le libelle court et le paragraphe didactique dans un
    meme `detail-text` de 100 a 250 mots. Le JSON garde la separation : les
    `label` sont les items, les paragraphes vivent a part dans `infos` et ne
    sont pas repris.
    """
    chemin = Path(chemin)
    donnees = json.loads(chemin.read_text(encoding="utf8"))
    numero = donnees["meta"].get("numero")
    sections_out = {}
    for onglet, prefixe in ONGLETS_AZYGOS.items():
        lignes = sections_out.setdefault(prefixe, [])
        for groupe in donnees["onglets"].get(onglet, []):
            if not isinstance(groupe, dict):
                continue
            nom = (groupe.get("groupe") or "").strip()
            if nom:
                lignes.append(("titre", None, nom, None))
            for rang, item in enumerate(groupe.get("items", [])):
                titre = (item.get("label") or "").strip()
                if not titre:
                    continue
                cid = f"{prefixe}{len(lignes) + 1}"
                sous = [v.strip() for v in item.get("valeurs", []) if v and v.strip()]
                lignes.append(("item", cid, titre, harmonise(sous)))
    return {
        "id": f"AZYGOS-{numero}" if numero else donnees["meta"]["id"][:8],
        "corpus": "azygos",
        "fichier": str(chemin.relative_to(REPO)),
        "ssp": None,
        "diagnostic": None,
        "confiance": "absent",
        "sections": {k: v for k, v in sections_out.items() if v},
    }
```

- [ ] **Step 4: Rattacher chaque JSON à son numéro AZYGOS**

Les JSON sont nommés par UUID et `meta` ne porte pas le numéro. Écrire la correspondance une fois pour toutes, par le titre :

Run:
```bash
python3 -c "
import json, glob, re, unicodedata, os
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()
html = {}
for p in glob.glob('cases/azygos/*.html'):
    m = re.match(r'(AZYGOS-\d+)_-_(.+?)_-_', os.path.basename(p))
    if m: html[norm(m.group(2))] = m.group(1)
lignes = []
for f in sorted(glob.glob('.azygos-extraction/*.json')):
    t = json.load(open(f))['meta']['titre']
    lignes.append((os.path.basename(f), html.get(norm(t), 'INCONNU'), t))
manquants = [l for l in lignes if l[1] == 'INCONNU']
print(f'{len(lignes)-len(manquants)}/{len(lignes)} apparies')
for l in manquants: print('   INCONNU :', l[2])
open('docs/azygos-fichiers.yaml','w',encoding='utf8').write(
    '# UUID du JSON .azygos-extraction -> identifiant de grille\n' +
    ''.join(f'{a}: {b}\n' for a, b, _ in sorted(lignes)))
"
```
Expected: un décompte d'appariement et `docs/azygos-fichiers.yaml` écrit. Les `INCONNU` restants sont complétés à la main dans le fichier.

- [ ] **Step 5: Faire lire cette table par `lire_azygos`**

Remplacer le calcul de `numero` par :

```python
_FICHIERS_AZYGOS = None


def _numero_azygos(nom_fichier):
    global _FICHIERS_AZYGOS
    if _FICHIERS_AZYGOS is None:
        import lib_yaml
        _FICHIERS_AZYGOS = lib_yaml.lire_plat(REPO / "docs" / "azygos-fichiers.yaml")
    return _FICHIERS_AZYGOS.get(nom_fichier)
```

et dans `lire_azygos` : `identifiant = _numero_azygos(chemin.name) or donnees["meta"]["id"][:8]`, utilisé tel quel comme `"id"`.

- [ ] **Step 6: Lancer le checker pour vérifier qu'il passe**

Run: `python3 scripts/memento/check_azygos.py`
Expected: `OK — 49 extractions AZYGOS, granularite conforme`

Si des titres de plus de 12 mots sont signalés, c'est que des `valeurs` ont été prises pour des labels : corriger `lire_azygos`, pas le checker.

- [ ] **Step 7: Vérifier la non-régression**

Run: `python3 scripts/memento/check_fusion.py`
Expected: `OK — memento officiel inchange, generateur idempotent`

- [ ] **Step 8: Commit**

```bash
git add scripts/memento/lib_extraction.py scripts/memento/check_azygos.py docs/azygos-fichiers.yaml
git commit -m "Lit AZYGOS depuis son extraction JSON

Les grilles HTML d'AZYGOS fondent le libelle court et le paragraphe didactique
dans un meme detail-text de 100 a 250 mots, inexploitable en case a cocher. Les
49 fichiers de .azygos-extraction/ gardent la separation : les label sont les
items, les paragraphes restent dans infos et ne sont pas repris.

Le checker refuse tout titre de plus de douze mots — c'est le signe que le pave
a de nouveau ete pris pour un item."
```

---

### Task 4: Rattachement SSP et rapport de couverture

**Files:**
- Create: `scripts/memento/lib_ssp.py`
- Create: `scripts/memento/check_couverture.py`
- Create: `docs/ecos-ssp-complements.yaml`

**Interfaces:**
- Consumes: structure pivot
- Produces: `rattachements() -> dict[str, str]` (id de cas → nom de SSP), `specialite(ssp) -> str`, `priorite(ssp) -> str`, `CORPUS = ("rescos", "amboss", "german", "azygos")`

- [ ] **Step 1: Écrire le checker qui échoue**

Créer `scripts/memento/check_couverture.py` :

```python
"""Tout cas en perimetre est extrait et rattache, ou nomme. Sortie 1 si ecart."""
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L
import lib_ssp

REPO = Path(__file__).resolve().parents[2]


def main():
    rattache = lib_ssp.rattachements()
    total, sans_ssp, sans_items = 0, [], []
    for corpus in lib_ssp.CORPUS:
        motif = (str(REPO / ".azygos-extraction" / "*.json") if corpus == "azygos"
                 else str(REPO / "cases" / corpus / "*.html"))
        for f in sorted(glob.glob(motif)):
            cas = L.lire_azygos(f) if corpus == "azygos" else L.lire_html(f)
            total += 1
            if cas["id"] not in rattache:
                sans_ssp.append(f"{cas['id']} ({corpus})")
            if not sum(len(v) for v in cas["sections"].values()):
                sans_items.append(f"{cas['id']} ({corpus})")

    print(f"{total} grilles lues · {total - len(sans_ssp)} rattachees a une SSP")
    if sans_items:
        print(f"\nECHEC — {len(sans_items)} grille(s) sans aucun item extrait :")
        for x in sans_items:
            print("   ", x)
        return 1
    if sans_ssp:
        print(f"\nECHEC — {len(sans_ssp)} grille(s) sans rattachement SSP :")
        for x in sans_ssp:
            print("   ", x)
        print("\n  Completer docs/ecos-ssp-complements.yaml.")
        return 1
    print("OK — toutes les grilles sont extraites et rattachees")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Lancer le checker pour vérifier qu'il échoue**

Run: `python3 scripts/memento/check_couverture.py`
Expected: `ModuleNotFoundError: No module named 'lib_ssp'`

- [ ] **Step 3: Écrire `lib_ssp.py`**

```python
"""Rattachement d'un cas a sa SSP, et metadonnees de la page SSP du coffre.

Deux sources, dans cet ordre :
  1. docs/obsidian-mapping.yaml — la curation validee du 2026-07-23, qui
     rattache 616 grilles a 116 pages. Elle n'est PAS modifiee ici.
  2. docs/ecos-ssp-complements.yaml — les rattachements manquants, notamment
     les 39 grilles RESCOS ajoutees apres la curation et les 49 AZYGOS.
"""
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml

REPO = Path(__file__).resolve().parents[2]
COFFRE = Path.home() / "Documents/Damien/Medecine/Obsidian/SSP ECOS"
CORPUS = ("rescos", "amboss", "german", "azygos")


def _identifiant(nom_fichier):
    m = re.match(r"([A-Z]+-\d+[a-z]?)", Path(nom_fichier).name)
    return m.group(1) if m else None


def rattachements():
    """id de cas -> nom de SSP (sans le prefixe « SSP — » ni l'extension)."""
    out = {}
    page = None
    texte = (REPO / "docs" / "obsidian-mapping.yaml").read_text(encoding="utf8")
    for ligne in texte.splitlines():
        m = re.match(r'\s*"SSP ECOS/SSP — (.+)\.md":', ligne)
        if m:
            page = m.group(1)
            continue
        m = re.search(r'file:\s*"cases/(\w[\w-]*)/([^"]+)"', ligne)
        if m and page and m.group(1) in CORPUS:
            cid = _identifiant(m.group(2))
            if cid:
                out[cid] = page
    out.update(lib_yaml.lire_plat(REPO / "docs" / "ecos-ssp-complements.yaml"))
    return out


def _champ(ssp, champ, defaut=""):
    fichier = COFFRE / f"SSP — {ssp}.md"
    if not fichier.exists():
        return defaut
    m = re.search(rf"^{champ}:\s*(.+)$", fichier.read_text(encoding="utf8"), re.M)
    return m.group(1).strip() if m else defaut


def specialite(ssp):
    return _champ(ssp, "specialite", "Non classé")


def priorite(ssp):
    return _champ(ssp, "priorite", "Standard")
```

- [ ] **Step 4: Créer la table de compléments, vide**

```bash
printf '# Rattachements SSP absents de docs/obsidian-mapping.yaml.\n# Forme : IDENTIFIANT: Nom exact de la page SSP (sans « SSP — » ni « .md »)\n' > docs/ecos-ssp-complements.yaml
```

- [ ] **Step 5: Lancer le checker et lire la liste des manquants**

Run: `python3 scripts/memento/check_couverture.py`
Expected: `ECHEC` avec la liste nominative des grilles sans SSP — attendu : les 39 RESCOS et les 49 AZYGOS.

- [ ] **Step 6: Compléter la table**

Pour chaque grille listée, ajouter une ligne à `docs/ecos-ssp-complements.yaml`. Le nom de SSP doit correspondre **exactement** à une page existante du coffre — vérifier avec :

```bash
ls "$HOME/Documents/Damien/Medecine/Obsidian/SSP ECOS/" | sed 's/^SSP — //;s/\.md$//'
```

Les neuf grilles officielles ont déjà leur SSP, déclarée dans `scripts/build_obsidian_memento.py` (table `CAS`) : la recopier.

- [ ] **Step 7: Lancer le checker pour vérifier qu'il passe**

Run: `python3 scripts/memento/check_couverture.py`
Expected: `OK — toutes les grilles sont extraites et rattachees`

- [ ] **Step 8: Commit**

```bash
git add scripts/memento/lib_ssp.py scripts/memento/check_couverture.py docs/ecos-ssp-complements.yaml
git commit -m "Rattache les 257 grilles a leur SSP

Le mapping cure de juillet ne couvre que 41 des 80 grilles RESCOS et ignore
AZYGOS. Les rattachements manquants vont dans une table de complements plutot
que dans le mapping, qui reste la curation validee d'origine.

check_couverture.py refuse toute grille non rattachee et la nomme : aucune ne
peut disparaitre en silence d'un memento."
```

---

### Task 5: Rapport d'écart au référentiel officiel

**Files:**
- Create: `scripts/memento/check_referentiel.py`

**Interfaces:**
- Consumes: `lib_extraction`, `lib_ssp`
- Produces: `docs/superpowers/rapport-referentiel-memento.md`

- [ ] **Step 1: Écrire le rapport**

```python
"""Mesure l'ecart des grilles non officielles au corpus officiel.

Les neuf grilles officielles font autorite sur ce qu'est un item de memento
(spec § referentiel). Ce rapport ne bloque rien : il NOMME ce qui s'en ecarte,
pour qu'une relecture decide. Sortie 0 sauf erreur de lecture.
"""
import glob
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L
import lib_ssp

REPO = Path(__file__).resolve().parents[2]
SORTIE = REPO / "docs" / "superpowers" / "rapport-referentiel-memento.md"
OFFICIELLES = {"RESCOS-9b", "RESCOS-12b", "RESCOS-57b", "RESCOS-58b", "RESCOS-63b",
               "RESCOS-67b", "RESCOS-68b", "RESCOS-69b", "RESCOS-70b"}


def cle(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return " ".join(sorted(m for m in t.replace("'", " ").split() if len(m) > 3))


def tous_les_cas():
    for corpus in lib_ssp.CORPUS:
        motif = (str(REPO / ".azygos-extraction" / "*.json") if corpus == "azygos"
                 else str(REPO / "cases" / corpus / "*.html"))
        for f in sorted(glob.glob(motif)):
            yield L.lire_azygos(f) if corpus == "azygos" else L.lire_html(f)


def main():
    reference, autres = set(), []
    for cas in tous_les_cas():
        for lignes in cas["sections"].values():
            for genre, _, titre, sous in lignes:
                if genre != "item":
                    continue
                if cas["id"] in OFFICIELLES:
                    reference.add(cle(titre))
                    for s in sous:
                        reference.add(cle(s))
                else:
                    autres.append((cas["id"], cas["corpus"], titre))

    orphelins = [(i, c, t) for i, c, t in autres if cle(t) not in reference]
    par_corpus = Counter(c for _, c, _ in orphelins)
    total = len(autres)

    lignes = ["# Écart au référentiel officiel — mémentos", "",
              f"{len(reference)} formes canoniques tirées des neuf grilles officielles.",
              f"{total} items non officiels, dont **{len(orphelins)} sans répondant** "
              f"({100 * len(orphelins) // max(total, 1)} %).", "",
              "| Corpus | Items orphelins |", "|---|---|"]
    for c, n in par_corpus.most_common():
        lignes.append(f"| {c} | {n} |")
    lignes += ["", "## Les 60 libellés orphelins les plus fréquents", ""]
    for titre, n in Counter(t for _, _, t in orphelins).most_common(60):
        lignes.append(f"- `{titre}` — {n}×")

    SORTIE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{len(orphelins)}/{total} items sans répondant officiel "
          f"→ {SORTIE.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Produire le rapport**

Run: `python3 scripts/memento/check_referentiel.py`
Expected: une ligne de décompte et le fichier écrit.

- [ ] **Step 3: Lire le rapport et en tirer les premières entrées de vocabulaire**

Ouvrir `docs/superpowers/rapport-referentiel-memento.md`. Les libellés orphelins fréquents sont les candidats prioritaires du vocabulaire canonique (tâche 10). **Ne rien corriger maintenant** : le rapport est un constat d'étape.

- [ ] **Step 4: Commit**

```bash
git add scripts/memento/check_referentiel.py docs/superpowers/rapport-referentiel-memento.md
git commit -m "Mesure l'ecart des grilles non officielles au referentiel

Un item sans repondant dans les neuf grilles officielles n'est pas supprime —
neuf SSP ne peuvent pas tout prevoir — mais il est nomme. Le rapport donne la
part d'orphelins par corpus et les soixante libelles les plus frequents : ce
sont les premieres entrees du vocabulaire canonique."
```

---

## ÉTAPE 2 — Résoudre le diagnostic

### Task 6: Cascade de résolution et table curée

**Files:**
- Create: `scripts/memento/lib_diagnostic.py`
- Create: `scripts/memento/check_diagnostic.py`
- Create: `docs/ecos-diagnostics.yaml`

**Interfaces:**
- Consumes: structure pivot, `lib_yaml`
- Produces: `resoudre(cas, html_brut=None) -> (str | None, str)` rendant `(diagnostic, confiance)` ; `charger_table() -> dict[str, str]`

- [ ] **Step 1: Écrire le checker qui échoue**

```python
"""Couverture et coherence de la resolution du diagnostic. Sortie 1 si ecart."""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_diagnostic

SEUIL = 90  # part minimale de cas dont le diagnostic est resolu


def main():
    table = lib_diagnostic.charger_table()
    if not table:
        print("ECHEC — docs/ecos-diagnostics.yaml est vide ou absent")
        return 1

    confiances = Counter(v.split(" | ")[1] if " | " in v else "absent" for v in table.values())
    resolus = sum(n for c, n in confiances.items() if c != "absent")
    part = 100 * resolus // len(table)
    print(f"{len(table)} cas · {resolus} diagnostics resolus ({part} %)")
    for c, n in confiances.most_common():
        print(f"   {c:20s} {n}")

    vides = [k for k, v in table.items() if not v.split(" | ")[0].strip()]
    if vides:
        print(f"\nECHEC — {len(vides)} entree(s) sans diagnostic : {vides[:8]}")
        return 1
    if part < SEUIL:
        print(f"\nECHEC — couverture {part} % sous le seuil de {SEUIL} %")
        return 1
    print("\nOK — table de diagnostics complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Lancer le checker pour vérifier qu'il échoue**

Run: `python3 scripts/memento/check_diagnostic.py`
Expected: `ModuleNotFoundError: No module named 'lib_diagnostic'`

- [ ] **Step 3: Écrire la cascade**

```python
"""Resolution du diagnostic d'un cas, par cascade a trois niveaux.

Aucun champ ne porte le diagnostic. On tente, du plus fiable au moins :

  1. explicite          — critere « Hypothese diagnostique : X » du management
  2. premier-dd         — premiere entree du bloc pedagogique dd-category
  3. diagnostic-travail — label « Diagnostic de travail » du JSON AZYGOS

La table docs/ecos-diagnostics.yaml est CUREE : une valeur corrigee a la main
doit survivre a une reexecution. La cascade ne remplit que les entrees absentes.
"""
import html as H
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml

REPO = Path(__file__).resolve().parents[2]
TABLE = REPO / "docs" / "ecos-diagnostics.yaml"

EXPLICITE = re.compile(r"(?:hypoth[èe]se diagnostique|diagnostic principal|"
                       r"diagnostic de suspicion)\s*[:\-–]\s*(.+)", re.I)


def _texte(fragment):
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", H.unescape(fragment)).strip()


def resoudre(cas, html_brut=None):
    """(diagnostic, confiance). `html_brut` est requis pour le niveau 2."""
    for lignes in cas["sections"].values():
        for genre, _, titre, _ in lignes:
            if genre != "item":
                continue
            m = EXPLICITE.search(titre)
            if m and len(m.group(1).split()) <= 8:
                return m.group(1).strip(" .:"), "explicite"

    if html_brut:
        i = html_brut.find("dd-category")
        if i >= 0:
            bloc = _texte(html_brut[i:i + 1200])
            bloc = re.sub(r"^.*?Diagnostics diff[ée]rentiels [àa] consid[ée]rer\s*", "", bloc)
            m = re.match(r"(?:[^A-ZÉÀ]*\([^)]*\)\s*)?([A-ZÉÀ][^•]{3,60}?)\s+Arguments", bloc)
            if m:
                return m.group(1).strip(" .:"), "premier-dd"

    if cas["corpus"] == "azygos":
        for lignes in cas["sections"].values():
            for genre, _, titre, sous in lignes:
                if genre == "item" and "diagnostic de travail" in titre.lower() and sous:
                    return sous[0].strip(" ."), "diagnostic-travail"

    return None, "absent"


def charger_table():
    return lib_yaml.lire_plat(TABLE)
```

- [ ] **Step 4: Écrire le générateur de table**

Ajouter à `lib_diagnostic.py` un `main` qui remplit la table **sans écraser les valeurs existantes** :

```python
def ecrire_table():
    """Complete la table sans jamais ecraser une valeur deja presente."""
    import glob
    import lib_extraction as L
    import lib_ssp

    existant = charger_table()
    out = dict(existant)
    for corpus in lib_ssp.CORPUS:
        motif = (str(REPO / ".azygos-extraction" / "*.json") if corpus == "azygos"
                 else str(REPO / "cases" / corpus / "*.html"))
        for f in sorted(glob.glob(motif)):
            if corpus == "azygos":
                cas, brut = L.lire_azygos(f), None
            else:
                cas = L.lire_html(f)
                brut = Path(f).read_text(encoding="utf8", errors="replace")
            if cas["id"] in existant:
                continue
            diag, confiance = resoudre(cas, brut)
            out[cas["id"]] = f"{diag or ''} | {confiance}"

    lignes = ["# Diagnostic de chaque cas — TABLE CUREE.",
              "# Forme : IDENTIFIANT: Diagnostic | confiance",
              "# confiance : explicite | premier-dd | diagnostic-travail | absent",
              "# Une valeur corrigee a la main n'est jamais ecrasee par une reexecution.",
              ""]
    for cid in sorted(out, key=lambda x: (x.split("-")[0], int(re.search(r"\d+", x).group()))):
        lignes.append(f"{cid}: {out[cid]}")
    TABLE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{len(out)} entrees -> {TABLE.relative_to(REPO)}")


if __name__ == "__main__":
    ecrire_table()
```

- [ ] **Step 5: Produire la table**

Run: `python3 scripts/memento/lib_diagnostic.py`
Expected: `257 entrees -> docs/ecos-diagnostics.yaml`

- [ ] **Step 6: Lancer le checker et relire**

Run: `python3 scripts/memento/check_diagnostic.py`

Si la couverture est sous 90 %, ouvrir la table et **compléter à la main** les entrées `| absent`, en s'aidant du bloc « Diagnostics différentiels » de la grille concernée. Corriger aussi toute valeur `premier-dd` visiblement fausse (un diagnostic de plus de huit mots, une phrase, un fragment de titre). Relancer le checker jusqu'au vert.

- [ ] **Step 7: Commit**

```bash
git add scripts/memento/lib_diagnostic.py scripts/memento/check_diagnostic.py docs/ecos-diagnostics.yaml
git commit -m "Resout le diagnostic de chaque cas par cascade

Aucun champ ne le porte : on lit le critere « Hypothese diagnostique » quand il
existe, sinon la premiere entree du bloc pedagogique dd-category — present dans
40/40 AMBOSS, 77/88 GERMAN, 59/80 RESCOS — sinon le « Diagnostic de travail »
du JSON AZYGOS.

Le champ confiance rend chaque valeur relisible, et une correction manuelle
n'est jamais ecrasee : la table est curee, pas regeneree."
```

---

## ÉTAPE 3 — Fusionner

### Task 7: Normalisation et appariement (socle A)

**Files:**
- Create: `scripts/memento/lib_fusion.py`
- Create: `scripts/memento/check_appariement.py`

**Interfaces:**
- Consumes: `lib_yaml`
- Produces: `canonique(titre, ssp=None) -> str`, `apparier(cas_list, prefixe) -> list[dict]` rendant `[{"titre": str, "sous": list[str], "cas": set[str]}]`

- [ ] **Step 1: Écrire le checker qui échoue**

```python
"""Comportement de l'appariement sur des cas construits. Sortie 1 si ecart."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_fusion

A = {"id": "A", "sections": {"a": [("item", "a1", "1. Caractérisation de la douleur",
                                    ["Localisation", "Irradiation"])]}}
B = {"id": "B", "sections": {"a": [("item", "a1", "Caractérisation de la Douleur",
                                    ["Localisation", "Facteurs déclenchants"])]}}
C = {"id": "C", "sections": {"a": [("item", "a1", "Anamnèse familiale", [])]}}


def main():
    ecarts = []
    fusion = lib_fusion.apparier([A, B, C], "a")

    titres = [f["titre"] for f in fusion]
    if len(titres) != 2:
        ecarts.append(f"attendu 2 items fusionnes, obtenu {len(titres)} : {titres}")

    douleur = next((f for f in fusion if "douleur" in f["titre"].lower()), None)
    if not douleur:
        ecarts.append("les deux libelles « Caracterisation de la douleur » n'ont pas fusionne")
    else:
        if douleur["cas"] != {"A", "B"}:
            ecarts.append(f"cas portes attendus {{A, B}}, obtenu {douleur['cas']}")
        sous = {s["titre"] for s in douleur["sous"]}
        if sous != {"Localisation", "Irradiation", "Facteurs déclenchants"}:
            ecarts.append(f"sous-items mal fusionnes : {sous}")
        loc = next(s for s in douleur["sous"] if s["titre"] == "Localisation")
        if loc["cas"] != {"A", "B"}:
            ecarts.append("« Localisation » devrait etre porte par A et B")
        irr = next(s for s in douleur["sous"] if s["titre"] == "Irradiation")
        if irr["cas"] != {"A"}:
            ecarts.append("« Irradiation » devrait n'etre porte que par A")

    if lib_fusion.canonique("1. Caractérisation de la douleur") != lib_fusion.canonique("Caractérisation de la Douleur"):
        ecarts.append("numerotation et casse devraient etre neutralisees")

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — appariement conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Lancer le checker pour vérifier qu'il échoue**

Run: `python3 scripts/memento/check_appariement.py`
Expected: `ModuleNotFoundError: No module named 'lib_fusion'`

- [ ] **Step 3: Écrire la fusion**

```python
"""Appariement des items entre grilles d'une meme SSP.

SOCLE A — normalisation lexicale, sans curation : minuscules, accents,
numerotation et ponctuation retires ; les mots de trois lettres ou moins sont
ecartes ; l'ordre des mots restants est neutralise. Deux libelles de meme
signature sont le meme item.

COUCHE B — docs/ecos-vocabulaire.yaml donne, par SSP, la forme canonique d'un
libelle brut. Elle n'est consultee que si elle porte une entree : la couche B
corrige le socle A la ou il echoue, elle ne le remplace pas.

Le libelle affiche est celui du premier cas rencontre, sauf si la couche B en
impose un autre.
"""
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml

REPO = Path(__file__).resolve().parents[2]
_VOCABULAIRE = None


def _table():
    global _VOCABULAIRE
    if _VOCABULAIRE is None:
        _VOCABULAIRE = lib_yaml.lire_groupe(REPO / "docs" / "ecos-vocabulaire.yaml")
    return _VOCABULAIRE


def signature(titre):
    """Cle d'appariement du socle A."""
    t = re.sub(r"^\d+\.\s*", "", titre)
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    mots = [m for m in re.split(r"[^a-z0-9]+", t) if len(m) > 3]
    return " ".join(sorted(mots)) or t.strip()


def canonique(titre, ssp=None):
    """Forme canonique d'un libelle : couche B si elle en porte une, sinon le titre nu."""
    nu = re.sub(r"^\d+\.\s*", "", titre).strip()
    if ssp:
        return _table().get(ssp, {}).get(nu, nu)
    return nu


def _fusionner(entrees, ssp):
    """[(titre, sous, id_cas)] -> [{titre, sous, cas}] apparies par signature."""
    groupes = {}
    for titre, sous, cid in entrees:
        cle = signature(canonique(titre, ssp))
        g = groupes.setdefault(cle, {"titre": canonique(titre, ssp), "sous": {}, "cas": set()})
        g["cas"].add(cid)
        for s in sous:
            cle_s = signature(canonique(s, ssp))
            gs = g["sous"].setdefault(cle_s, {"titre": canonique(s, ssp), "cas": set()})
            gs["cas"].add(cid)
    return [{"titre": g["titre"], "cas": g["cas"], "sous": list(g["sous"].values())}
            for g in groupes.values()]


def apparier(cas_list, prefixe, ssp=None):
    """Items d'une section, apparies entre tous les cas fournis."""
    entrees = []
    for cas in cas_list:
        for genre, _, titre, sous in cas["sections"].get(prefixe, []):
            if genre == "item":
                entrees.append((titre, sous or [], cas["id"]))
    return _fusionner(entrees, ssp)
```

- [ ] **Step 4: Créer la table de vocabulaire, vide**

```bash
printf '# Vocabulaire canonique, par SSP. Couche B de l'"'"'appariement.\n# Forme :\n#   "Douleur Thoracique":\n#     "Douleurs": Caractérisation de la douleur\n' > docs/ecos-vocabulaire.yaml
```

- [ ] **Step 5: Lancer le checker pour vérifier qu'il passe**

Run: `python3 scripts/memento/check_appariement.py`
Expected: `OK — appariement conforme`

- [ ] **Step 6: Commit**

```bash
git add scripts/memento/lib_fusion.py scripts/memento/check_appariement.py docs/ecos-vocabulaire.yaml
git commit -m "Apparie les items entre grilles d'une meme SSP

Socle A : signature lexicale — accents, numerotation, casse et ordre des mots
neutralises, mots de trois lettres et moins ecartes. « 1. Caracterisation de la
douleur » et « Caracterisation de la Douleur » deviennent le meme item, et
chaque item retient l'ensemble des cas qui le portent.

Couche B : le vocabulaire cure corrige le socle la ou il echoue, sans le
remplacer. Sa table est creee vide ; elle se remplira a l'etape 4."
```

---

### Task 8: Rendu fusionné, anamnèse et status marqués

**Files:**
- Create: `scripts/memento/lib_rendu.py`
- Create: `scripts/memento/build_memento.py`

**Interfaces:**
- Consumes: `apparier`, `lib_ssp`, `lib_diagnostic`
- Produces: `encadre(genre, entete, items, diagnostics_total) -> str | None`, `marque(item, diagnostics_total, diag_par_cas) -> str`

- [ ] **Step 1: Écrire le checker du marquage**

Ajouter à `scripts/memento/check_appariement.py`, avant `main` :

```python
import lib_rendu


def verifier_marquage():
    ecarts = []
    diag = {"A": "STEMI", "B": "Péricardite", "C": "Embolie"}
    partout = {"titre": "Localisation", "cas": {"A", "B", "C"}}
    partiel = {"titre": "Soulagement en antéflexion", "cas": {"B"}}
    deux = {"titre": "Facteurs déclenchants", "cas": {"A", "B"}}

    if lib_rendu.marque(partout, 3, diag) != "Localisation":
        ecarts.append("un item porte par tous les cas ne doit pas etre suffixe")
    if lib_rendu.marque(partiel, 3, diag) != "Soulagement en antéflexion *(Péricardite)*":
        ecarts.append(f"suffixe simple errone : {lib_rendu.marque(partiel, 3, diag)}")
    attendu = "Facteurs déclenchants *(Péricardite, STEMI)*"
    if lib_rendu.marque(deux, 3, diag) != attendu:
        ecarts.append(f"suffixe multiple errone : {lib_rendu.marque(deux, 3, diag)}")

    quatre = {"titre": "Dyspnée", "cas": {"A", "B", "C", "D"}}
    d4 = dict(diag, D="Pneumothorax", E="Angor")
    if lib_rendu.marque(quatre, 5, d4) != "Dyspnée *(4 diagnostics)*":
        ecarts.append(f"abreviation au-dela de 3 non appliquee : {lib_rendu.marque(quatre, 5, d4)}")
    return ecarts
```

et dans `main`, après les vérifications d'appariement : `ecarts += verifier_marquage()`.

- [ ] **Step 2: Lancer le checker pour vérifier qu'il échoue**

Run: `python3 scripts/memento/check_appariement.py`
Expected: `ModuleNotFoundError: No module named 'lib_rendu'`

- [ ] **Step 3: Écrire le rendu**

```python
"""Rendu Markdown des mementos — callouts Obsidian, cases a cocher imbriquees.

La charte est celle du memento des neuf grilles officielles : legende, titre de
specialite, encadres 📋 / 🩺 / 🔬 / 💊, numerotation repartant a 1 dans chaque
encadre.
"""

LEGENDE = """> [!info] Légende
>
> - 📋 = Anamnèse — ce qu'il faut absolument avoir demandé
> - 🩺 = Status — le geste ou le signe qui fait la différence
> - 🔬 = Management : examens complémentaires
> - 💊 = Management : prise en charge attendue
> - 🚨 = urgence
> - 🚩 = red flag à ne jamais rater
> - ⭐️ = SSP ou diagnostic fréquemment rencontré à l'ECOS"""

SEUIL_ABREGE = 3   # au-dela, on compte au lieu d'enumerer


def marque(item, diagnostics_total, diag_par_cas):
    """Suffixe un item des diagnostics qui le portent, s'il n'est pas universel."""
    diags = sorted({diag_par_cas[c] for c in item["cas"] if c in diag_par_cas})
    if not diags or len(diags) >= diagnostics_total:
        return item["titre"]
    if len(diags) > SEUIL_ABREGE:
        return f"{item['titre']} *({len(diags)} diagnostics)*"
    return f"{item['titre']} *({', '.join(diags)})*"


def encadre(genre, entete, items, diagnostics_total, diag_par_cas):
    """Un callout dont la liste est numerotee a partir de 1."""
    if not items:
        return None
    out = [f"> [!{genre}] {entete}"]
    for numero, item in enumerate(items, 1):
        out.append(f"> - [ ] **{numero}. {marque(item, diagnostics_total, diag_par_cas)}**")
        for sous in item["sous"]:
            out.append(f"> \t- [ ] {marque(sous, diagnostics_total, diag_par_cas)}")
    return "\n".join(out)
```

- [ ] **Step 4: Lancer le checker pour vérifier qu'il passe**

Run: `python3 scripts/memento/check_appariement.py`
Expected: `OK — appariement conforme`

- [ ] **Step 5: Écrire l'orchestration**

Créer `scripts/memento/build_memento.py` : pour chaque SSP, charger ses cas, résoudre leurs diagnostics depuis la table, appeler `apparier` sur `a` puis `e`, rendre les deux encadrés, puis (tâche 9) le management. Écrire `docs/obsidian-memento/Mémento — <SSP>.md`. Reprendre le frontmatter et l'ordre par spécialité de `scripts/build_obsidian_memento.py`.

- [ ] **Step 6: Générer et inspecter une SSP à plusieurs cas**

Run: `python3 scripts/memento/build_memento.py && sed -n '1,60p' "docs/obsidian-memento/Mémento — Douleur Thoracique.md"`
Expected: un encadré 📋 dont les items communs sont nus et les items partiels suffixés d'un diagnostic.

- [ ] **Step 7: Vérifier la non-régression du mémento officiel**

Run: `python3 scripts/memento/check_fusion.py`
Expected: `OK — memento officiel inchange, generateur idempotent`

- [ ] **Step 8: Commit**

```bash
git add scripts/memento/lib_rendu.py scripts/memento/build_memento.py scripts/memento/check_appariement.py
git commit -m "Fusionne anamnese et status, en marquant le specifique

Un item porte par tous les cas d'une SSP reste nu ; un item partiel est suffixe
des diagnostics qui le portent — « Soulagement en anteflexion *(Pericardite)* ».
Au-dela de trois, on compte plutot que d'enumerer.

Le surlignage ==…== a ete ecarte : il colore sans dire pourquoi, depend du theme
et ne survit pas a l'export."
```

---

### Task 9: Management commun et sous-blocs par diagnostic

**Files:**
- Modify: `scripts/memento/lib_fusion.py`
- Modify: `scripts/memento/build_memento.py`
- Modify: `scripts/memento/check_appariement.py`

**Interfaces:**
- Consumes: `apparier`
- Produces: `scinder_management(cas_list, diag_par_cas, ssp) -> (commun, {diagnostic: items})`

- [ ] **Step 1: Écrire le checker qui échoue**

Ajouter à `check_appariement.py` :

```python
def verifier_management():
    ecarts = []
    m = lambda cid, titres: {"id": cid, "sections": {"m": [("item", f"m{i}", t, [])
                                                          for i, t in enumerate(titres, 1)]}}
    cas = [m("A", ["Hypothèses diagnostiques", "Aspirine + P2Y12"]),
           m("B", ["Hypothèses diagnostiques", "AINS et colchicine"])]
    diag = {"A": "STEMI", "B": "Péricardite"}
    commun, propres = lib_fusion.scinder_management(cas, diag, None)

    if [c["titre"] for c in commun] != ["Hypothèses diagnostiques"]:
        ecarts.append(f"le commun devrait etre le seul item partage : {[c['titre'] for c in commun]}")
    if set(propres) != {"STEMI", "Péricardite"}:
        ecarts.append(f"sous-blocs attendus STEMI et Pericardite : {sorted(propres)}")
    if [i["titre"] for i in propres.get("STEMI", [])] != ["Aspirine + P2Y12"]:
        ecarts.append("le sous-bloc STEMI est faux")
    return ecarts
```

et `ecarts += verifier_management()` dans `main`.

- [ ] **Step 2: Lancer le checker pour vérifier qu'il échoue**

Run: `python3 scripts/memento/check_appariement.py`
Expected: `AttributeError: module 'lib_fusion' has no attribute 'scinder_management'`

- [ ] **Step 3: Écrire la scission**

Ajouter à `lib_fusion.py` :

```python
def scinder_management(cas_list, diag_par_cas, ssp=None):
    """Management -> (items communs a tous les diagnostics, {diagnostic: items propres}).

    Un item porte par TOUS les diagnostics de la SSP est commun. Les autres
    vont dans le sous-bloc de chaque diagnostic qui les porte — un item partage
    par deux diagnostics sur cinq apparait donc dans deux sous-blocs.
    """
    apparies = apparier(cas_list, "m", ssp)
    diagnostics = {diag_par_cas[c["id"]] for c in cas_list if c["id"] in diag_par_cas}

    commun, propres = [], {d: [] for d in diagnostics}
    for item in apparies:
        porteurs = {diag_par_cas[c] for c in item["cas"] if c in diag_par_cas}
        if porteurs and porteurs == diagnostics:
            commun.append(item)
        else:
            for d in porteurs:
                propres[d].append(item)
    return commun, {d: v for d, v in propres.items() if v}
```

- [ ] **Step 4: Lancer le checker pour vérifier qu'il passe**

Run: `python3 scripts/memento/check_appariement.py`
Expected: `OK — appariement conforme`

- [ ] **Step 5: Câbler la scission dans l'orchestration**

Dans `build_memento.py`, remplacer l'encadré management unique par : un `> [!success] 💊 Management — commun` avec `commun`, puis un `> [!success] 💊 — si <diagnostic>` par entrée de `propres`, triés par nom de diagnostic.

- [ ] **Step 6: Générer et inspecter**

Run: `python3 scripts/memento/build_memento.py && grep -A2 "💊" "docs/obsidian-memento/Mémento — Douleur Thoracique.md" | head -30`
Expected: un bloc commun suivi d'un sous-bloc par diagnostic.

- [ ] **Step 7: Vérifier la non-régression**

Run: `python3 scripts/memento/check_fusion.py && python3 scripts/memento/check_couverture.py`
Expected: les deux `OK`.

- [ ] **Step 8: Commit**

```bash
git add scripts/memento/lib_fusion.py scripts/memento/build_memento.py scripts/memento/check_appariement.py
git commit -m "Scinde le management en commun et sous-blocs par diagnostic

L'anamnese d'une SSP est presque superposable d'un cas a l'autre ; son
management ne l'est pas. Un item porte par tous les diagnostics reste commun,
les autres vont dans le sous-bloc de chacun des diagnostics qui les portent —
un item partage par deux diagnostics sur cinq apparait donc deux fois, ce qui
est le comportement voulu."
```

---

## ÉTAPE 4 — Curer

### Task 10: Vocabulaire canonique des dix grosses SSP

**Files:**
- Modify: `docs/ecos-vocabulaire.yaml`
- Create: `scripts/memento/report_doublons.py`

**Interfaces:**
- Consumes: `lib_fusion`, `build_memento`
- Produces: `docs/superpowers/rapport-doublons-memento.md`

- [ ] **Step 1: Écrire le détecteur de doublons**

```python
"""Signale, par SSP, les items que le socle A n'a pas apparies mais qui se
ressemblent. Ce sont les candidats du vocabulaire canonique. Sortie 0.
"""
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento

REPO = Path(__file__).resolve().parents[2]
SORTIE = REPO / "docs" / "superpowers" / "rapport-doublons-memento.md"
SEUIL = 0.72


def main():
    lignes = ["# Doublons candidats — vocabulaire canonique", "",
              "Paires d'items d'une même SSP que le socle A n'a pas appariés",
              f"mais dont la similarité dépasse {SEUIL}.", ""]
    total = 0
    for ssp, cas in sorted(build_memento.par_ssp().items()):
        if len(cas) < 2:
            continue
        titres = sorted({i["titre"] for p in ("a", "e", "m")
                         for i in build_memento.lib_fusion.apparier(cas, p, ssp)})
        paires = [(a, b) for n, a in enumerate(titres) for b in titres[n + 1:]
                  if SequenceMatcher(None, a.lower(), b.lower()).ratio() > SEUIL]
        if paires:
            total += len(paires)
            lignes.append(f"## {ssp} — {len(cas)} cas")
            lignes += [f"- `{a}`  ⟷  `{b}`" for a, b in paires] + [""]
    SORTIE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{total} paires candidates -> {SORTIE.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Produire le rapport**

Run: `python3 scripts/memento/report_doublons.py`
Expected: un décompte et le fichier écrit.

- [ ] **Step 3: Curer la première SSP**

Ouvrir le rapport, prendre **Douleur Abdominale** (17 cas). Pour chaque paire réellement synonyme, ajouter au `docs/ecos-vocabulaire.yaml` :

```yaml
"Douleur Abdominale":
  "Douleurs": Caractérisation de la douleur
  "Caractérisation des douleurs": Caractérisation de la douleur
```

Le libellé de droite doit être, quand il existe, **celui d'une des neuf grilles officielles**.

- [ ] **Step 4: Régénérer et mesurer le gain**

Run: `python3 scripts/memento/build_memento.py && python3 scripts/memento/report_doublons.py`
Expected: le nombre de paires candidates de Douleur Abdominale a baissé.

- [ ] **Step 5: Commit**

```bash
git add docs/ecos-vocabulaire.yaml docs/superpowers/rapport-doublons-memento.md scripts/memento/report_doublons.py
git commit -m "Cure le vocabulaire de Douleur Abdominale

Le socle A n'apparie que les libelles de meme signature lexicale. Le rapport de
doublons expose les paires qu'il rate ; le vocabulaire canonique les rabat sur
une forme unique, celle des grilles officielles quand elle existe."
```

- [ ] **Step 6: Répéter pour les neuf autres SSP à 4 cas et plus**

Douleur Thoracique (11), Toux Chronique (8), Œil Rouge (7), Fatigue (6), Lombalgies (6), Céphalée (5), Diarrhée (5), et les deux à 4 cas. Un commit par SSP, même forme de message.

Le critère d'arrêt est fonctionnel : on cure tant que le mémento d'une SSP contient des doublons **visibles à la lecture**, pas au-delà.

---

## ÉTAPE 5 — Étendre

### Task 11: AZYGOS dans les mémentos, et décision sur usmle / triage

**Files:**
- Modify: `docs/ecos-ssp-complements.yaml`
- Modify: `docs/superpowers/specs/2026-08-15-mementos-par-ssp-design.md`

**Interfaces:**
- Consumes: toute la chaîne
- Produces: les mémentos incluant AZYGOS

- [ ] **Step 1: Vérifier que `.azygos-extraction/` est versionné**

Run: `git check-ignore -v .azygos-extraction && echo "IGNORE — a corriger" || echo "versionnable"`

S'il est ignoré : la chaîne dépend d'un dossier absent d'un clone frais. Le versionner (`git add -f .azygos-extraction`) ou recopier les champs utiles dans le dépôt. **Ne pas continuer sans avoir tranché.**

- [ ] **Step 2: Rattacher les 49 AZYGOS à leur SSP**

Run: `python3 scripts/memento/check_couverture.py`

Pour chaque AZYGOS listé, ajouter sa ligne à `docs/ecos-ssp-complements.yaml`. Le titre AZYGOS est la plainte (« Douleurs au genou », « Syncope »), qui correspond directement à une page SSP.

- [ ] **Step 3: Régénérer et vérifier**

Run: `python3 scripts/memento/build_memento.py && python3 scripts/memento/check_couverture.py && python3 scripts/memento/check_fusion.py`
Expected: les trois `OK`.

- [ ] **Step 4: Relire une SSP où AZYGOS rejoint un autre corpus**

Ouvrir le mémento d'une SSP portant à la fois un AZYGOS et un RESCOS ou GERMAN. Vérifier que leurs items ont fusionné plutôt que de se juxtaposer ; sinon, c'est du vocabulaire à curer (tâche 10).

- [ ] **Step 5: Trancher le sort d'usmle et triage**

Les deux corpus (44 + 40 grilles) figurent au mapping SSP mais hors périmètre initial. Décider avec l'utilisateur, puis **consigner la décision** dans la section « Périmètre » de la spec.

- [ ] **Step 6: Commit**

```bash
git add docs/ecos-ssp-complements.yaml docs/obsidian-memento/ docs/superpowers/specs/2026-08-15-mementos-par-ssp-design.md
git commit -m "Integre AZYGOS aux mementos par SSP

Les 49 grilles AZYGOS rejoignent les mementos par leur extraction JSON. Leur
titre est la plainte, qui correspond directement a une page SSP du coffre.

La spec consigne la decision prise sur usmle et triage."
```

---

## Auto-revue du plan

**Couverture de la spec.** Chaque section a sa tâche : le référentiel officiel → tâches 2 et 5 ; le périmètre et le trou des 39 RESCOS → tâche 4 ; la cascade de diagnostic → tâche 6 ; socle A et couche B → tâches 7 et 10 ; le marquage par suffixe → tâche 8 ; le management scindé → tâche 9 ; AZYGOS depuis le JSON → tâche 3 ; les quatre critères de vérification → `check_fusion` (idempotence, non-régression), `check_couverture` (couverture), `check_referentiel` (conformité) ; le risque du dossier non versionné → tâche 11 step 1.

**Cohérence des signatures.** `lire_html` et `lire_azygos` rendent la même structure pivot. `apparier(cas_list, prefixe, ssp)` est appelée avec trois arguments partout après la tâche 7 ; le checker de la tâche 7 l'appelle avec deux, `ssp` valant `None` par défaut. `marque(item, diagnostics_total, diag_par_cas)` garde ses trois paramètres des tâches 8 et 9.

**Ce que le plan ne fait pas** et qui reste à décider en cours de route : le seuil d'abréviation du suffixe est posé à trois sans mesure ; le seuil de similarité des doublons à 0,72 sans mesure. Les deux se règlent à la lecture du premier rendu réel, tâches 8 et 10.
