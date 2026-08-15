#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere un memento Obsidian par SSP, en fusionnant les cas de cette SSP.

    python3 scripts/memento/build_memento.py            # lot prioritaire
    python3 scripts/memento/build_memento.py --lot tout  # toutes les SSP

Un fichier « Mémento — <SSP>.md » par SSP dans docs/obsidian-memento/, a cote
du memento des neuf grilles officielles, qui reste la reference de forme et le
test de non-regression de la chaine (check_fusion.py l'epingle par md5).

CE QUE CE GENERATEUR PRODUIT AUJOURD'HUI : les encadres 📋 anamnese et 🩺
status, fusionnes entre tous les cas de la SSP. Le management (🔬 / 💊) suivra,
avec ses sous-blocs par diagnostic ; `encadre()` et `marque()` sont deja
partages avec lui via lib_rendu.

LE MARQUAGE DU SPECIFIQUE repose sur le diagnostic de chaque cas, lu dans
docs/ecos-diagnostics.yaml puis ramene a la categorie de la table des
priorites par docs/ecos-diagnostics-alias.yaml. Sans cet alias, « Fracture de
l'humerus » et « Fracture de la tete radiale » resteraient deux diagnostics
distincts la ou la table des priorites n'en voit qu'un, et un item commun aux
deux serait marque comme specifique a tort.

DETERMINISME : aucune date, aucun aleatoire, et tout ensemble est trie avant
d'etre ecrit (le champ `cas` rendu par lib_fusion.apparier() est un `set`,
dont l'ordre d'iteration depend de PYTHONHASHSEED).
"""
import glob
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_diagnostic                                    # noqa: E402
import lib_extraction as L                               # noqa: E402
import lib_fusion                                        # noqa: E402
import lib_rendu                                         # noqa: E402
import lib_ssp                                           # noqa: E402
import lib_yaml                                          # noqa: E402
from check_couverture import HORS_PERIMETRE              # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SORTIE = REPO / "docs" / "obsidian-memento"
ALIAS = REPO / "docs" / "ecos-diagnostics-alias.yaml"
PREFIXE = "Mémento — "        # nomme les fichiers de CE generateur, eux seuls

# « AMBOSS-1 » < « AMBOSS-10 » : le numero se compare en entier, pas en
# chaine. Le reste (« b », « -2 ») departage les grilles de meme numero.
_RANG = re.compile(r"^([A-Za-z]+)-(\d+)(.*)$")

ENTETE = """> [!warning] Mémento dérivé de grilles NON officielles
> Ces items viennent de grilles d'entraînement (RESCOS, AMBOSS, GERMAN,
> AZYGOS) qu'aucun jury n'a validées. Seul le mémento des neuf grilles
> officielles fait autorité — [[Mémento ECOS — Grilles officielles]].
>
> **Anamnèse et status sont fusionnés entre tous les cas de la SSP.** Un item
> porté par tous les diagnostics reste nu ; un item porté par une partie
> d'entre eux est suffixé des diagnostics concernés — au-delà de trois, ils
> sont comptés plutôt qu'énumérés. Un diagnostic entre parenthèses n'est donc
> pas une consigne : c'est la trace du cas qui apporte l'item."""


def rang(cid):
    """Cle de tri naturelle d'un identifiant de grille."""
    m = _RANG.match(cid)
    return (m.group(1), int(m.group(2)), m.group(3)) if m else (cid, 0, "")


def canonique_diagnostic(nom, alias):
    """Le libelle sous lequel DEUX cas portent le meme diagnostic.

    L'alias reconcilie le libelle precis d'une grille (« AOMI stade IIb »)
    avec la categorie de la table des priorites (« AOMI ») : sans lui, le
    marquage produirait des variantes qui devraient se rejoindre. La cible
    d'un alias est reprise telle quelle, c'est un libelle cure.

    A defaut d'alias, l'initiale est mise en majuscule. Ce n'est pas une
    coquetterie : la table des diagnostics porte vingt libelles a initiale
    minuscule, dont « embolie pulmonaire » (RESCOS-35), qui resterait sinon un
    huitieme diagnostic de Douleur Thoracique a cote de l'« Embolie
    pulmonaire » d'AMBOSS-12 et de German-31 — et tout item commun aux trois
    serait marque comme specifique. Verifie sur les 234 libelles de la table :
    c'est le SEUL rapprochement que cette regle provoque. L'alias est retente
    sur la forme majusculee, pour qu'une entree ecrite dans un sens ou dans
    l'autre porte de la meme facon.
    """
    nom = nom.strip()
    if nom in alias:
        return alias[nom]
    hausse = nom[:1].upper() + nom[1:]
    return alias.get(hausse, hausse)


def _table_diagnostics():
    """id de cas -> (diagnostic canonique ou None, confiance).

    Un cas dont la table ne nomme aucun diagnostic rend None : `marque()` le
    traite alors comme n'apportant aucun diagnostic, ce qui laisse nu un item
    qu'il est seul a porter. C'est le comportement voulu — un suffixe vide
    serait pire qu'une absence de suffixe.

    Une seule lecture pour les deux champs : les separer en deux fonctions
    relirait la table deux fois et ouvrirait la porte a deux lectures
    divergentes de la meme ligne.
    """
    alias = lib_yaml.lire_plat(ALIAS)
    out = {}
    for cid, valeur in lib_diagnostic.charger_table().items():
        nom, _, confiance = valeur.rpartition(" | ")
        nom = nom.strip()
        out[cid] = (canonique_diagnostic(nom, alias) if nom else None,
                    confiance.strip() or "absent")
    return out


def tous_les_cas():
    """Les cas des quatre corpus, hors perimetre exclu, dans un ordre stable."""
    for corpus in lib_ssp.CORPUS:
        motif = (str(REPO / ".azygos-extraction" / "*.json") if corpus == "azygos"
                 else str(REPO / "cases" / corpus / "*.html"))
        for f in sorted(glob.glob(motif)):
            cas = L.lire_azygos(f) if corpus == "azygos" else L.lire_html(f)
            if cas["id"] not in HORS_PERIMETRE:
                yield cas


def par_ssp(lot=None):
    """SSP -> ses cas, enrichis de `ssp`, `diagnostic` et `confiance`.

    Point d'entree partage : le rapport de doublons et le rendu du management
    partent tous deux de ce regroupement, pour qu'un cas ne puisse pas etre
    compte ici et manquer la. `lot` restreint aux SSP donnees (None = toutes).
    Les cas d'une SSP sont tries par identifiant : l'ordre des items fusionnes
    en decoule, et il doit etre reproductible.
    """
    table = _table_diagnostics()
    rattache = lib_ssp.rattachements()
    groupes = {}
    for cas in tous_les_cas():
        ssp = rattache.get(cas["id"])
        if ssp is None or (lot is not None and ssp not in lot):
            continue
        cas["ssp"] = ssp
        cas["diagnostic"], cas["confiance"] = table.get(cas["id"], (None, "absent"))
        groupes.setdefault(ssp, []).append(cas)
    for cas_list in groupes.values():
        cas_list.sort(key=lambda c: rang(c["id"]))
    return groupes


def lien(cas):
    """Lien file:// vers la grille d'origine, comme dans le memento officiel."""
    return f"file://{REPO / cas['fichier']}".replace(" ", "%20")


def inventaire(cas_list):
    """L'encadre qui nomme les grilles fusionnees et leur diagnostic."""
    entete = ("La seule grille de cette SSP" if len(cas_list) == 1
              else f"Les {len(cas_list)} grilles fusionnées")
    out = [f"> [!abstract] {entete}"]
    for cas in cas_list:
        diag = cas["diagnostic"] or "diagnostic non résolu"
        out.append(f"> - **{cas['id']}** — {diag} `{cas['confiance']}` · "
                   f"[grille](<{lien(cas)}>)")
    return "\n".join(out)


def memento(ssp, cas_list):
    """Le document Markdown complet d'une SSP."""
    diag_par_cas = {c["id"]: c["diagnostic"] for c in cas_list if c["diagnostic"]}
    total = len(set(diag_par_cas.values()))
    specialite = lib_ssp.specialite(ssp)
    etoile = " ⭐️" if lib_ssp.priorite(ssp) in ("Top 18", "Haut rendement") else ""

    anamnese = lib_rendu.encadre("note", "📋 Anamnèse",
                                 lib_fusion.apparier(cas_list, "a", ssp), total, diag_par_cas)
    status = lib_rendu.encadre("tip", "🩺 Status",
                               lib_fusion.apparier(cas_list, "e", ssp), total, diag_par_cas)

    corps = [f"# {specialite}", "",
             f"## {ssp}{etoile}", "",
             f"*{len(cas_list)} grille{'s' if len(cas_list) > 1 else ''} · "
             f"{total} diagnostic{'s' if total > 1 else ''} distinct"
             f"{'s' if total > 1 else ''}* — [[SSP — {ssp}]]", "",
             inventaire(cas_list), ""]
    for bloc in (anamnese, status):
        if bloc:
            corps += [bloc, ""]

    return f"""---
aliases:
  - "Mémento {ssp}"
type: memento-ecos-ssp
ssp: "{ssp}"
specialite: "{specialite}"
cas: {len(cas_list)}
diagnostics: {total}
tags:
  - ecos/memento
  - ecos/grille-non-officielle
cssclasses:
  - skill-ecos
---

{lib_rendu.LEGENDE}

{ENTETE}

{chr(10).join(corps).rstrip()}
"""


def nettoyer():
    """Efface les mementos par SSP de la passe precedente, ceux-la seuls.

    La comparaison se fait sur le nom normalise en NFC : le nom d'un fichier
    ecrit ici porte des accents composes, et un glob litteral echouerait sur un
    nom que le systeme de fichiers aurait rendu decompose. Le memento des neuf
    grilles officielles (« Mémento ECOS — … ») ne porte pas ce prefixe et n'est
    jamais touche.
    """
    for vieux in SORTIE.glob("*.md"):
        if unicodedata.normalize("NFC", vieux.name).startswith(PREFIXE):
            vieux.unlink()


def main():
    tout = "--lot" in sys.argv and "tout" in sys.argv
    lot = None if tout else lib_ssp.lot_prioritaire()
    groupes = par_ssp(lot)

    SORTIE.mkdir(parents=True, exist_ok=True)
    nettoyer()
    items = sous_items = ecrits = 0
    for ssp in sorted(groupes):
        # Une barre oblique ferait un sous-dossier au lieu d'un fichier ; un
        # guillemet double casserait le frontmatter, ou les valeurs sont
        # quotees. Aucune SSP n'en porte aujourd'hui — le jour ou l'une en
        # portera, elle doit etre nommee, pas ecrite de travers en silence.
        if "/" in ssp or '"' in ssp:
            print(f"IGNORÉE — le nom de SSP « {ssp} » contient / ou \"")
            continue
        doc = memento(ssp, groupes[ssp])
        items += doc.count("> - [ ] **")
        sous_items += doc.count("> \t- [ ] ")
        cible = SORTIE / unicodedata.normalize("NFC", f"{PREFIXE}{ssp}.md")
        cible.write_text(doc, encoding="utf8")
        ecrits += 1

    cas = sum(len(v) for v in groupes.values())
    print(f"lot {'complet' if lot is None else 'prioritaire'} · "
          f"{ecrits} SSP · {cas} grilles · {items} items · {sous_items} sous-items "
          f"→ {SORTIE.relative_to(REPO)}/{PREFIXE}*.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
