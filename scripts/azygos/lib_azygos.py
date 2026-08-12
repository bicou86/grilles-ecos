"""Outils communs du corpus azygos.

Le corpus est produit à partir du mode apprentissage d'azygos.ch, extrait via
Chrome DevTools (voir extract.js). Chaque cas donne un JSON brut dans
.azygos-extraction/<uuid>.json ; ce module le normalise puis le rend au gabarit
de grille du dépôt.

Contrat de conversion retenu :
  - un groupe Azygos  -> un critère noté ;
  - un item du groupe -> un détail à 1 point ;
  - les 4 dimensions OFSP -> la section communication, notée A..E.
"""

from __future__ import annotations

import html
import json
import re
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
EXTRACTION = RACINE / ".azygos-extraction"
SORTIE = RACINE / "cases" / "azygos"
IMAGES = RACINE / "cases" / "img" / "azygos"

# Les onglets cliniques alimentent les quatre sections notées du gabarit.
# Leurs intitulés varient selon le format du poste — « Statut clinique » mais
# aussi « Partie 1 / Status clinique », « Partie 2 / Présentation de cas »… — on
# classe donc par mot-clé plutôt que par égalité stricte.
SECTIONS = [
    ("anamnese", "a", "Anamnèse"),
    ("examen", "e", "Examen clinique"),
    ("management", "m", "Management"),
    ("communication", "c", "Communication"),
]

ONGLETS_FIXES = {"Infos du cas", "Préparation", "Tableau de bord"}


def classe_onglet(nom: str) -> str:
    """Range un onglet clinique dans l'une des quatre sections notées."""
    n = unicodedata.normalize("NFD", nom.lower())
    n = "".join(c for c in n if not unicodedata.combining(c))
    if "communication" in n:
        return "communication"
    if "anamnese" in n:
        return "anamnese"
    # « Statut clinique », « Status clinique », « État clinique », « Examen
    # clinique » : quatre libellés pour la même chose selon le cas.
    if "status" in n or "statut" in n or "etat clinique" in n or "examen clinique" in n:
        return "examen"
    # Diagnostic, Procédure, Prise en charge, Présentation de cas…
    return "management"

# Azygos note de 0 (Insuffisant) à 4 (Très bien) ; le gabarit note de A (4) à
# E (0). L'échelle est la même, seul l'étiquetage change.
NIVEAUX_COMM = ["A", "B", "C", "D", "E"]


def echappe(txt: str) -> str:
    return html.escape(txt or "", quote=True)


def nom_fichier(corpus_id: str, titre: str, description: str) -> str:
    """Reproduit la convention de nommage du dépôt.

    Les accents sont décomposés (NFD) et tout caractère non alphanumérique
    devient « _ » — d'où les « Ce_phale_e » du corpus existant.
    """
    def morceau(s: str) -> str:
        s = unicodedata.normalize("NFD", s)
        s = "".join(c if (c.isascii() and c.isalnum()) else "_" for c in s)
        return re.sub(r"_+", "_", s).strip("_")

    parties = [corpus_id, morceau(titre)]
    if description:
        parties.append(morceau(description))
    parties.append("Grille_ECOS")
    return "_-_".join(parties) + ".html"


def nettoie_onglet(nom: str) -> str:
    """« Partie 1\\nStatus clinique » -> « Partie 1 · Status clinique »."""
    return " · ".join(p.strip() for p in nom.split("\n") if p.strip())


def aplatit(groupe: dict, infos: dict | None = None) -> list[dict]:
    """Supprime les doublons parent/enfant des groupes repliables.

    Un item porteur de `nbEnfants = N` est un en-tête : sa valeur n'est que la
    concaténation des N items qui le suivent. On le retire et on préfixe ses
    enfants de son intitulé, ce qui conserve l'information sans la compter deux
    fois dans le barème.
    """
    items = groupe["items"]
    infos = infos or {}

    def enrichi(it: dict, label: str) -> dict:
        return {**it, "label": label, "info": infos.get(it.get("cle", ""), "")}

    sortie: list[dict] = []
    i = 0
    while i < len(items):
        it = items[i]
        n = it.get("nbEnfants") or 0
        if n > 0:
            # L'en-tête de sous-groupe porte SA PROPRE « Information
            # complémentaire », distincte de celles de ses enfants : elle
            # justifie le sous-groupe entier (pourquoi explorer la dynamique
            # temporelle, pas seulement pourquoi demander la date de début).
            # L'en-tête n'étant pas rendu comme une ligne à part, on rattache
            # son texte au PREMIER enfant, qui l'affiche à côté du préfixe.
            info_sg = infos.get(it.get("cle", ""), "")
            # `nbEnfants` est déduit du nombre de libellés dans le conteneur ;
            # sur des sous-groupes imbriqués il surestime. On s'arrête donc au
            # premier en-tête rencontré plutôt que de l'avaler comme enfant —
            # sinon sa propre justification serait perdue avec lui.
            j, rang = i + 1, 0
            while j < len(items) and rang < n and not (items[j].get("nbEnfants") or 0):
                ligne = enrichi(items[j], f"{it['label']} · {items[j]['label']}")
                if info_sg and rang == 0:
                    ligne["info_sous_groupe"] = info_sg
                    ligne["label_sous_groupe"] = it["label"]
                sortie.append(ligne)
                j += 1
                rang += 1
            if rang == 0:
                # En-tête sans enfant exploitable : on le rend comme un item à
                # part entière, faute de quoi son contenu disparaîtrait.
                sortie.append(enrichi(it, it["label"]))
            i = j
        else:
            sortie.append(enrichi(it, it["label"]))
            i += 1
    return sortie


def charge(uuid: str) -> dict:
    return json.loads((EXTRACTION / f"{uuid}.json").read_text(encoding="utf-8"))


def infos_cas(data: dict) -> dict:
    """Lit les métadonnées de l'onglet « Infos du cas ».

    Les lignes arrivent en paires étiquette/valeur : SPÉCIALITÉ, Dermatologie,
    DIFFICULTÉ, Facile, …
    """
    lignes = data["onglets"].get("Infos du cas", [])
    cles = {
        "SPÉCIALITÉ": "specialite",
        "DIFFICULTÉ": "difficulte",
        "FORMAT": "format",
        "DURÉE": "duree",
        "DIAGNOSTIC": "diagnostic",
    }
    out: dict[str, str] = {}
    for i, l in enumerate(lignes):
        if l in cles and i + 1 < len(lignes):
            out[cles[l]] = lignes[i + 1]
    return out


def preparation(data: dict) -> dict:
    """Découpe l'onglet « Préparation » en résumé, focus et aperçu AKDP."""
    lignes = data["onglets"].get("Préparation", [])
    res: dict[str, list[str]] = {"resume": [], "focus": [], "akdp": [], "notes": []}
    courant = "resume"
    for l in lignes:
        if l == "Focus du cas":
            courant = "focus"
            continue
        if l.startswith("Aperçu AKDP"):
            courant = "akdp"
            continue
        if l.startswith("Libération des résultats"):
            courant = "notes"
            continue
        # Les longues phrases du résumé sont les seules à dépasser 120 signes.
        if courant == "resume" and len(l) < 60:
            continue
        res[courant].append(l)
    return res
