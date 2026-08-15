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


def lot_prioritaire():
    """Les SSP du lot 1 — celles que la table de priorites 2026 designe."""
    table = lib_yaml.lire_groupe(REPO / "docs" / "ecos-priorites-2026.yaml")
    return {champs["ssp"] for champs in table.values() if champs.get("ssp", "?") != "?"}
