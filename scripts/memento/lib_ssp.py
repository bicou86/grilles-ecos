"""Rattachement d'un cas a sa SSP, et metadonnees de la page SSP du coffre.

Trois sources :
  1. docs/obsidian-mapping.yaml — la curation validee du 2026-07-23, qui
     rattache 616 grilles a 116 pages. Elle n'est PAS modifiee ici.
  2. docs/ecos-ssp-complements.yaml — les rattachements manquants, notamment
     les grilles RESCOS ajoutees apres la curation et les grilles AZYGOS.
  3. docs/ecos-ssp-alias.yaml — reconciliation, appliquee en dernier sur le
     resultat des deux sources precedentes, entre le nom de page du coffre
     et le nom de SSP de la table de priorites 2026 quand les deux
     vocabulaires divergent (une page renommee depuis la curation).

L'identifiant de cas est calcule par lib_extraction.identifiant() — la meme
fonction que celle utilisee pour lire les grilles, pour ne jamais diverger
d'elle. Ne pas la recopier ici.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml
from lib_extraction import identifiant

REPO = Path(__file__).resolve().parents[2]
COFFRE = Path.home() / "Documents/Damien/Medecine/Obsidian/SSP ECOS"
CORPUS = ("rescos", "amboss", "german", "azygos")

# LES NEUF GRILLES OFFICIELLES (entrainements federaux 2025-2026). Elles font
# autorite sur ce qu'est un item de memento, servent de test de non-regression
# et sont les seules validees par un jury — un memento par SSP qui en fusionne
# une doit le dire, sous peine de faire ecarter comme non valide un item qui
# vient precisement du referentiel. Source unique : rapport_referentiel.py
# et build_memento.py lisent cette liste, aucun des deux n'en garde de copie.
OFFICIELLES = {"RESCOS-9b", "RESCOS-12b", "RESCOS-57b", "RESCOS-58b", "RESCOS-63b",
               "RESCOS-67b", "RESCOS-68b", "RESCOS-69b", "RESCOS-70b"}


def rattachements():
    """id de cas -> nom de SSP (sans le prefixe « SSP — » ni l'extension).

    Le coffre range aussi des pages « Skills ECOS/... » (SPIKES, decision
    partagee...) au meme niveau que les pages SSP. Une entree de page qui
    n'est pas une SSP doit remettre `page` a None : sinon ses grilles
    (ex. RESCOS-7, une station BBN sous « Skills ECOS/Skills — Annonce
    Mauvaise Nouvelle ») se retrouveraient rattachees a la derniere SSP
    croisee plus haut dans le fichier au lieu de rester non rattachees.
    """
    out = {}
    page = None
    texte = (REPO / "docs" / "obsidian-mapping.yaml").read_text(encoding="utf8")
    for ligne in texte.splitlines():
        m = re.match(r'  "([^"]+)":\s*$', ligne)
        if m:
            m2 = re.match(r"SSP ECOS/SSP — (.+)\.md$", m.group(1))
            page = m2.group(1) if m2 else None
            continue
        m = re.search(r'file:\s*"cases/(\w[\w-]*)/([^"]+)"', ligne)
        if m and page and m.group(1) in CORPUS:
            cid = identifiant(m.group(2))
            if cid:
                out[cid] = page
    out.update(lib_yaml.lire_plat(REPO / "docs" / "ecos-ssp-complements.yaml"))

    # L'alias s'applique en dernier, quelle que soit la source (mapping ou
    # complements) : une meme page renommee doit se reconcilier de la meme
    # facon partout, pas seulement pour les rattachements issus du mapping.
    alias = lib_yaml.lire_plat(REPO / "docs" / "ecos-ssp-alias.yaml")
    return {cid: alias.get(ssp, ssp) for cid, ssp in out.items()}


CHAMPS_COFFRE = ("specialite", "priorite")
INSTANTANE = REPO / "docs" / "ecos-ssp-coffre.yaml"
_INSTANTANE = None


def champ_texte(texte, champ):
    """La valeur d'un champ dans le texte d'une page SSP, ou None.

    SOURCE UNIQUE de la regle de lecture, partagee par le lecteur et par
    fige_coffre.py qui produit l'instantane. Une copie divergerait au premier
    correctif et l'instantane cesserait de valoir la page sans que rien ne le
    dise. La recherche porte sur TOUT le fichier et non sur le seul
    frontmatter, et rend la PREMIERE occurrence : c'est le comportement
    d'origine, conserve tel quel pour que l'instantane reproduise a l'octet ce
    que le coffre donnait.
    """
    m = re.search(rf"^{champ}:\s*(.+)$", texte, re.M)
    return m.group(1).strip() if m else None


def _instantane():
    """SSP -> {champ: valeur}, lu du DEPOT et non du coffre.

    POURQUOI PAS LE COFFRE. `specialite()` et `priorite()` decident du
    frontmatter `specialite:` et de l'etoile ⭐️ des mementos : ils entrent donc
    dans les octets de 74 des 89 fichiers VERSIONNES. Les lire dans
    ~/Documents/... rendait le depot non reproductible — et pire,
    check_mementos.py appelle le generateur, si bien qu'un clone frais
    REECRIVAIT les 74 fichiers en version degradee avant de les declarer en
    ecart. Meme remede qu'AZYGOS : le depot porte l'instantane, le coffre
    reste la source de RAFRAICHISSEMENT (fige_coffre.py).

    Une SSP absente de l'instantane est une page absente du coffre ; un champ
    absent de son groupe est un champ absent de la page. Les deux rendent le
    defaut, comme avant.
    """
    global _INSTANTANE
    if _INSTANTANE is None:
        _INSTANTANE = lib_yaml.lire_groupe(INSTANTANE)
    return _INSTANTANE


def pages_connues():
    """Les noms de SSP pour lesquels le coffre avait une page au dernier figeage."""
    return set(_instantane())


def _champ(ssp, champ, defaut=""):
    return _instantane().get(ssp, {}).get(champ) or defaut


def specialite(ssp):
    return _champ(ssp, "specialite", "Non classé")


def priorite(ssp):
    return _champ(ssp, "priorite", "Standard")


def lot_prioritaire():
    """Les SSP du lot 1 — celles que la table de priorites 2026 designe."""
    table = lib_yaml.lire_groupe(REPO / "docs" / "ecos-priorites-2026.yaml")
    return {champs["ssp"] for champs in table.values() if champs.get("ssp", "?") != "?"}
