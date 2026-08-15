#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere un memento Obsidian par SSP, en fusionnant les cas de cette SSP.

    python3 scripts/memento/build_memento.py            # lot prioritaire
    python3 scripts/memento/build_memento.py --lot tout  # toutes les SSP

Un fichier « Mémento — <SSP>.md » par SSP dans docs/obsidian-memento/, a cote
du memento des neuf grilles officielles, qui reste la reference de forme et le
test de non-regression de la chaine (check_fusion.py l'epingle par md5).
check_mementos.py, lui, garde ces fichiers-ci : il les regenere et compare.

CE QUE CE GENERATEUR PRODUIT : les encadres 📋 anamnese et 🩺 status, fusionnes
entre tous les cas de la SSP, puis le management 💊, qui ne se fusionne PAS —
la prise en charge depend du diagnostic. Il se scinde en un encadre commun et
un sous-bloc par diagnostic (voir `blocs_management`).

UN SEUL ENCADRE 💊, pas le partage 🔬 / 💊 du memento officiel : celui-ci est
declare a la main, critere par critere, et ne se devine pas a 252 grilles.
Le raisonnement et son cout sont en tete de lib_rendu, au-dessus de LEGENDE.

LE MARQUAGE porte sur les GRILLES et non sur les diagnostics — voir
lib_rendu.marque() pour l'invariant. Deux grilles portent le meme diagnostic
apres passage par docs/ecos-diagnostics-alias.yaml, puis apres reconciliation
des variantes de casse et d'accent (`ZONA` et `Zona` sont un seul diagnostic).

DETERMINISME : aucune date, aucun aleatoire, et tout ensemble est trie avant
d'etre ecrit (le champ `cas` rendu par lib_fusion.apparier() est un `set`,
dont l'ordre d'iteration depend de PYTHONHASHSEED).
"""
import glob
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_diagnostic                                    # noqa: E402
import lib_extraction as L                               # noqa: E402
import lib_fusion                                        # noqa: E402
import lib_rendu                                         # noqa: E402
import lib_ssp                                           # noqa: E402
import lib_yaml                                          # noqa: E402
from check_couverture import HORS_PERIMETRE              # noqa: E402
from lib_extraction import sans_accent                   # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SORTIE = REPO / "docs" / "obsidian-memento"
ALIAS = REPO / "docs" / "ecos-diagnostics-alias.yaml"
PRIORITES = REPO / "docs" / "ecos-priorites-2026.yaml"
PREFIXE = "Mémento — "
TYPE = "memento-ecos-ssp"     # marque d'appartenance, dans le frontmatter

# « AMBOSS-1 » < « AMBOSS-10 » : le numero se compare en entier, pas en
# chaine. Le reste (« b », « -2 ») departage les grilles de meme numero.
_RANG = re.compile(r"^([A-Za-z]+)-(\d+)(.*)$")

# Le frontmatter d'un memento produit ici. Sert de marque d'appartenance a
# `nettoyer()` : le NOM d'un fichier ne prouve rien (« Mémento — Toux (mes
# notes).md » est exactement le nom qu'un humain choisirait), le type declare,
# lui, n'est ecrit que par ce generateur.
# Le « (?!---\n) » interdit de franchir la fermeture du frontmatter : sans lui,
# une note qui a SON PROPRE frontmatter et cite `type: memento-ecos-ssp` plus
# bas — dans un bloc de code documentant la convention — serait reconnue comme
# produite ici, donc effacee.
_LIGNE = r"(?:(?!---\n).*\n)"
_TYPE_DECLARE = re.compile(rf"\A---\n{_LIGNE}*?type:\s*{TYPE}\s*\n{_LIGNE}*?---\n")

ENTETE_NON_OFFICIEL = """> [!warning] Mémento dérivé de grilles NON officielles
> Ces items viennent de grilles d'entraînement (RESCOS, AMBOSS, GERMAN,
> AZYGOS) qu'aucun jury n'a validées. Seul le mémento des neuf grilles
> officielles fait autorité — [[Mémento ECOS — Grilles officielles]]."""

ENTETE_MIXTE = """> [!warning] Mémento mixte — {n} grille{s} officielle{s}, {autres} non officielles
> **{officielles}** fait partie des **neuf grilles officielles** et fait donc
> autorité ; elle est signalée ⭐️ dans l'encadré ci-dessous. Les {autres}
> autres sont des grilles d'entraînement (RESCOS, AMBOSS, GERMAN, AZYGOS)
> qu'aucun jury n'a validées."""

CONVENTION = """>
> **Comment lire les suffixes.** Anamnèse et status sont fusionnés entre
> toutes les grilles de la SSP. Le suffixe décrit quelles grilles portent
> **cette formulation-là** :
>
> - un item **nu** : **toutes** les grilles de la SSP portent cette
>   formulation ;
> - `*(Diagnostic)*` : exactement toutes les grilles de ce diagnostic la
>   portent, et elles seules — au-delà de trois, ils sont comptés ;
> - `*(n grilles sur m)*` : une partie des grilles la porte, que les
>   diagnostics ne suffisent pas à désigner sans mentir ;
> - un **sous-item nu** hérite de la portée de son parent — il ne répète pas
>   son suffixe. Seul un sous-item dont la portée **diffère** du parent en
>   porte un.
>
> **Le management, lui, ne fusionne pas.** La prise en charge dépend du
> diagnostic : l'encadré 💊 se scinde en un bloc **commun** — ce que tous les
> diagnostics de la SSP partagent — puis un bloc **par diagnostic**. Un item
> porté par deux diagnostics sur cinq figure donc dans **deux** sous-blocs.
> À l'intérieur d'un sous-bloc, `*(n grilles sur m)*` compte les grilles **de
> ce diagnostic-là**, pas celles de la SSP.
>
> Un sous-bloc existe pour **chacun des diagnostics attendus de la SSP**
> (docs/ecos-priorites-2026.yaml), y compris ceux qu'aucune grille du corpus
> ne documente : ce sous-bloc vide est un **trou de révision** à combler
> ailleurs, pas un défaut du mémento.
>
> ⚠️ **Le suffixe parle des formulations, pas du contenu clinique.** Le
> rapprochement entre grilles est encore purement lexical : deux grilles qui
> disent la même chose autrement (« Motif de consultation » et « Motif de
> consultation principal », « Allergies » et « Allergies connues ») donnent
> **deux items distincts**, chacun marqué comme partiel. Un `*(1 grille sur 2)*`
> ne veut donc pas dire que l'autre grille néglige la question — seulement
> qu'elle l'écrit autrement. Tant que le vocabulaire canonique n'est pas
> rempli, lisez les libellés voisins ensemble."""


def rang(cid):
    """Cle de tri naturelle d'un identifiant de grille."""
    m = _RANG.match(cid)
    return (m.group(1), int(m.group(2)), m.group(3)) if m else (cid, 0, "")


def canonique_diagnostic(nom, alias):
    """Alias cure d'abord, initiale en majuscule a defaut."""
    nom = nom.strip()
    if nom in alias:
        return alias[nom]
    hausse = nom[:1].upper() + nom[1:]
    return alias.get(hausse, hausse)


def reconcilie_orthographe(formes, alias):
    """forme -> forme retenue, quand plusieurs ne different que par la graphie.

    Deux libelles qui ne different que par la CASSE ou les ACCENTS nomment le
    meme diagnostic : aucun couple de diagnostics distincts ne se distingue par
    cela seul, si bien que le rapprochement ne peut pas se tromper. C'est ce
    que la seule mise en majuscule de l'initiale ratait — « ZONA » (RESCOS-68b)
    restait un diagnostic separe de « Zona » (RESCOS-68, AMBOSS-40) et
    Éruption Cutanée annoncait huit diagnostics au lieu de sept.

    La forme retenue est, dans l'ordre : une cible d'alias (libelle cure), sinon
    la graphie majoritaire, sinon la plus accentuee (une variante desaccentuee
    est une degradation), sinon la premiere par ordre alphabetique.
    """
    cibles = set(alias.values())
    groupes = {}
    for forme in formes:
        groupes.setdefault(sans_accent(forme), set()).add(forme)

    def accents(f):
        return sum(1 for c in f if sans_accent(c) != c.lower())

    out = {}
    for variantes in groupes.values():
        curees = sorted(f for f in variantes if f in cibles)
        retenue = curees[0] if curees else sorted(
            variantes, key=lambda f: (-formes[f], -accents(f), f))[0]
        for f in variantes:
            out[f] = retenue
    return out


def _table_diagnostics():
    """id de cas -> (diagnostic canonique ou None, confiance).

    Un cas dont la table ne nomme aucun diagnostic rend None : `marque()` le
    traite alors comme n'apportant aucun diagnostic, ce qui empeche toute
    conclusion par diagnostic sur un item qu'il porte.
    """
    alias = lib_yaml.lire_plat(ALIAS)
    brut = {}
    for cid, valeur in lib_diagnostic.charger_table().items():
        nom, _, confiance = valeur.rpartition(" | ")
        nom = nom.strip()
        brut[cid] = (canonique_diagnostic(nom, alias) if nom else None,
                     confiance.strip() or "absent")
    formes = Counter(d for d, _ in brut.values() if d)
    graphie = reconcilie_orthographe(formes, alias)
    return {cid: (graphie.get(d, d), c) for cid, (d, c) in brut.items()}


def diagnostics_attendus():
    """SSP -> les diagnostics que la table de priorites 2026 attend d'elle.

    Lus dans le champ `diagnostics`, dont le SEPARATEUR EST LE POINT MEDIAN et
    non la virgule : plusieurs libelles portent virgules et parentheses
    (« Fracture du membre supérieur (humérus, tête radiale) »), qu'une
    decoupe a la virgule scinderait en trois faux diagnostics.

    L'union par SSP, et non la derniere plainte lue : deux plaintes distinctes
    peuvent viser la meme page SSP, et leurs listes se completent alors. Aucun
    cas de ce genre dans la table du 2026-08-16 ; l'union coute une ligne et
    ne se trompera pas le jour ou il s'en presentera un.

    Ces libelles ne passent PAS par `canonique_diagnostic()` : la table des
    alias les prend deja pour CIBLES (elle traduit le libelle precis d'un cas
    vers celui d'ici), et aucun n'est par ailleurs une de ses cles — verifie.
    check_appariement.verifier_attendus_du_corpus() garde la jointure.
    """
    out = {}
    for champs in lib_yaml.lire_groupe(PRIORITES).values():
        ssp = champs.get("ssp", "?").strip()
        if not ssp or ssp == "?":
            continue
        noms = {d.strip() for d in champs.get("diagnostics", "").split("·")}
        out.setdefault(ssp, set()).update(n for n in noms if n)
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


def entete(cas_list):
    """L'avertissement de tete, selon que la SSP fusionne ou non une officielle.

    « Aucun jury n'a valide ces grilles » est FAUX des qu'une des neuf
    officielles est fusionnee — quatre mementos du lot prioritaire sont dans
    ce cas (Toux, Fatigue, Éruption Cutanée, Parésie - AVC), neuf en lot
    complet. Le lecteur y ecarterait comme non valide un item qui vient
    precisement du referentiel.
    """
    off = [c for c in cas_list if c["id"] in lib_ssp.OFFICIELLES]
    if not off:
        return ENTETE_NON_OFFICIEL + "\n" + CONVENTION
    bloc = ENTETE_MIXTE.format(
        officielles=", ".join(c["id"] for c in off),
        n=len(off), s="s" if len(off) > 1 else "",
        autres=len(cas_list) - len(off))
    return bloc + "\n" + CONVENTION


def inventaire(cas_list):
    """L'encadre qui nomme les grilles fusionnees et leur diagnostic."""
    titre = ("La seule grille de cette SSP" if len(cas_list) == 1
             else f"Les {len(cas_list)} grilles fusionnées")
    out = [f"> [!abstract] {titre}"]
    for cas in cas_list:
        officielle = " ⭐️ **officielle**" if cas["id"] in lib_ssp.OFFICIELLES else ""
        diag = cas["diagnostic"] or "diagnostic non résolu"
        out.append(f"> - **{cas['id']}**{officielle} — {diag} `{cas['confiance']}` · "
                   f"[grille](<{lien(cas)}>)")
    return "\n".join(out)


def _nettoie(groupe):
    """Applique le nettoyage des libelles a un groupe apparie et a ses sous-items."""
    groupe["titre"] = lib_rendu.nettoie_libelle(groupe["titre"])
    for sous in groupe["sous"]:
        sous["titre"] = lib_rendu.nettoie_libelle(sous["titre"])
    return groupe


SANS_GRILLE = ("*Aucune grille du corpus ne documente ce diagnostic* — il est "
               "pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**")

TOUT_COMMUN = ("*Aucun item propre à ce diagnostic* — tout son management "
               "figure dans l'encadré commun ci-dessus.")

SANS_MANAGEMENT = ("*La ou les grilles de ce diagnostic ne cotent aucun item de "
                   "management* — elles s'arrêtent à l'anamnèse et au status.")


def blocs_management(cas_list, cas_ssp, diag_par_cas, ssp, attendus):
    """Les encadres 💊 d'une SSP : le commun, puis un sous-bloc par diagnostic.

    QUATRE SORTES DE SOUS-BLOCS, et le lecteur doit pouvoir les distinguer :

      - avec items       le management propre au diagnostic ;
      - sans grille      le diagnostic est attendu de la SSP mais aucune grille
                         ne le documente. Le sous-bloc reste, et le dit : c'est
                         une lacune de revision, pas un defaut du memento
                         (decision de l'auteur du 2026-08-15) ;
      - sans management  des grilles documentent le diagnostic, mais aucune ne
                         cote d'item de management (AZYGOS-4, HypoTA
                         orthostatique, s'arrete au status). NE PAS confondre
                         avec le suivant : dire « tout figure dans le commun »
                         renverrait le lecteur vers un encadre qui, dans ce
                         cas-la, peut ne pas exister du tout ;
      - tout commun      le diagnostic est documente, ses grilles cotent bien
                         du management, mais rien ne lui est propre. L'encadre
                         commun existe alors forcement, et le contient.

    Le dernier cas n'est rendu qu'a partir de DEUX diagnostics documentes : en
    dessous, « commun » ne distingue rien et le sous-bloc repeterait l'encadre
    qui le precede immediatement.

    Chaque sous-bloc est marque sur les GRILLES DE SON DIAGNOSTIC, via
    `lib_fusion.restreindre()` : « 2 grilles sur 3 » y compte les grilles de
    ce diagnostic, pas celles de la SSP. Le commun, lui, se marque sur toute
    la SSP, comme l'anamnese et le status.
    """
    commun, propres = lib_fusion.scinder_management(cas_list, diag_par_cas, ssp, attendus)
    documentes = set(diag_par_cas.values())
    cotes = {diag_par_cas[c["id"]] for c in cas_list if c["id"] in diag_par_cas
             and any(genre == "item" for genre, _, _, _ in c["sections"].get("m", []))}
    titre = ("💊 Management — commun aux diagnostics" if len(documentes) > 1
             else "💊 Management")

    blocs = []
    bloc = lib_rendu.encadre("success", titre, [_nettoie(g) for g in commun],
                             cas_ssp, diag_par_cas)
    if bloc:
        blocs.append(bloc)

    for diagnostic in sorted(documentes | set(attendus)):
        items = [_nettoie(g) for g in propres.get(diagnostic, [])]
        cas_diag = sorted(c for c, d in diag_par_cas.items() if d == diagnostic)
        mention = None
        if not items:
            if diagnostic not in documentes:
                mention = SANS_GRILLE
            elif diagnostic not in cotes:
                mention = SANS_MANAGEMENT
            elif len(documentes) < 2:
                continue
            else:
                mention = TOUT_COMMUN
        bloc = lib_rendu.encadre("success", f"💊 Management — si {diagnostic}",
                                 lib_fusion.restreindre(items, cas_diag),
                                 cas_diag, diag_par_cas, mention=mention)
        if bloc:
            blocs.append(bloc)
    return blocs


def memento(ssp, cas_list, attendus=()):
    """Le document Markdown complet d'une SSP."""
    cas_ssp = sorted(c["id"] for c in cas_list)
    diag_par_cas = {c["id"]: c["diagnostic"] for c in cas_list if c["diagnostic"]}
    total = len(set(diag_par_cas.values()))
    specialite = lib_ssp.specialite(ssp)
    etoile = " ⭐️" if lib_ssp.priorite(ssp) in ("Top 18", "Haut rendement") else ""

    blocs = []
    for genre, titre, prefixe in (("note", "📋 Anamnèse", "a"), ("tip", "🩺 Status", "e")):
        groupes = [_nettoie(g) for g in lib_fusion.apparier(cas_list, prefixe, ssp)]
        bloc = lib_rendu.encadre(genre, titre, groupes, cas_ssp, diag_par_cas)
        if bloc:
            blocs += [bloc, ""]
    for bloc in blocs_management(cas_list, cas_ssp, diag_par_cas, ssp, attendus):
        blocs += [bloc, ""]

    # LE TITRE DE NIVEAU 1 EST LA SSP, pas la specialite : un fichier ne porte
    # qu'une SSP, la specialite n'y groupe rien, et 11 des 33 SSP n'ont pas
    # encore de page dans le coffre — elles affichaient « # Non classé ».
    ligne = [f"{len(cas_list)} grille{'s' if len(cas_list) > 1 else ''}",
             f"{total} diagnostic{'s' if total > 1 else ''} distinct{'s' if total > 1 else ''}"]
    if specialite != "Non classé":
        ligne.insert(0, specialite)
    corps = [f"# {ssp}{etoile}", "", "*" + " · ".join(ligne) + f"* — [[SSP — {ssp}]]", "",
             inventaire(cas_list), ""] + blocs

    champs = [f'aliases:\n  - "Mémento {ssp}"', f"type: {TYPE}", f'ssp: "{ssp}"']
    if specialite != "Non classé":
        champs.append(f'specialite: "{specialite}"')
    champs.append(f"cas: {len(cas_list)}")
    champs.append(f"diagnostics: {total}")
    tags = ["  - ecos/memento"]
    if any(c["id"] in lib_ssp.OFFICIELLES for c in cas_list):
        tags.append("  - ecos/grille-officielle")
    tags.append("  - ecos/grille-non-officielle")
    champs.append("tags:\n" + "\n".join(tags))
    champs.append("cssclasses:\n  - skill-ecos")

    return (f"---\n{chr(10).join(champs)}\n---\n\n{lib_rendu.LEGENDE}\n\n"
            f"{entete(cas_list)}\n\n{chr(10).join(corps).rstrip()}\n")


def nettoyer():
    """Efface les mementos produits par CE generateur, eux seuls.

    L'appartenance se lit dans le FRONTMATTER (`type: memento-ecos-ssp`), pas
    dans le nom : « Mémento — Toux (mes notes).md » est precisement le nom
    qu'une note ecrite a la main porterait, et un glob l'emporterait.

    La lecture est ancree sur le bloc de frontmatter, pas cherchee dans tout
    le fichier : une note qui DOCUMENTE la convention (« les mementos portent
    type: memento-ecos-ssp ») serait sinon supprimee parce qu'elle en parle.
    """
    for vieux in SORTIE.glob("*.md"):
        if _TYPE_DECLARE.search(vieux.read_text(encoding="utf8")):
            vieux.unlink()


def main():
    argv = sys.argv[1:]
    if argv and argv != ["--lot", "tout"]:
        print(f"Argument non reconnu : {' '.join(argv)}\n"
              "Usage : build_memento.py [--lot tout]")
        return 2
    lot = None if argv else lib_ssp.lot_prioritaire()
    groupes = par_ssp(lot)
    attendus = diagnostics_attendus()

    # TOUT EST CONSTRUIT AVANT D'EFFACER QUOI QUE CE SOIT : une exception a la
    # vingtieme SSP laissait sinon 33 fichiers effaces et 19 reecrits.
    docs, ignorees = {}, []
    for ssp in sorted(groupes):
        # Une barre oblique ferait un sous-dossier ; un guillemet double
        # casserait le frontmatter, ou les valeurs sont quotees.
        if "/" in ssp or '"' in ssp:
            ignorees.append(ssp)
            continue
        docs[SORTIE / unicodedata.normalize("NFC", f"{PREFIXE}{ssp}.md")] = memento(
            ssp, groupes[ssp], attendus.get(ssp, ()))

    SORTIE.mkdir(parents=True, exist_ok=True)
    nettoyer()
    for cible, doc in docs.items():
        cible.write_text(doc, encoding="utf8")

    for ssp in ignorees:
        print(f"IGNORÉE — le nom de SSP « {ssp} » contient / ou \"")
    items = sum(d.count("> - [ ] **") for d in docs.values())
    sous = sum(d.count("> \t- [ ] ") for d in docs.values())
    cas = sum(len(v) for v in groupes.values())
    print(f"lot {'complet' if lot is None else 'prioritaire'} · "
          f"{len(docs)} SSP · {cas} grilles · {items} items · {sous} sous-items "
          f"→ {SORTIE.relative_to(REPO)}/{PREFIXE}*.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
