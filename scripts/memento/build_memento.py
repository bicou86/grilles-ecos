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
la prise en charge depend du diagnostic. Il se decoupe en un sous-bloc par
diagnostic, precede d'un encadre pour les items qu'au moins deux diagnostics
partagent (voir `blocs_management` et `lib_fusion.scinder_management`).

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
> diagnostic : l'encadré 💊 se découpe en **un sous-bloc par diagnostic**,
> `💊 Management — si <diagnostic>`. À l'intérieur d'un sous-bloc,
> `*(n grilles sur m)*` compte les grilles **de ce diagnostic-là**, pas celles
> de la SSP.
>
> Quand un item est porté par **deux diagnostics ou plus**, il n'est pas
> recopié dans chaque sous-bloc : il remonte dans un encadré
> `💊 Management — partagé par plusieurs diagnostics`, en tête, où son suffixe
> **nomme les diagnostics concernés** — `*(Angor · STEMI — 3 grilles sur 12)*`
> se lit « au moins une grille d'Angor et une de STEMI le portent, 3 des
> 12 grilles de la SSP au total ». ⚠️ **Cet encadré se lit *avec* le sous-bloc
> de votre diagnostic, pas à sa place.** Il est absent quand aucun item n'est
> partagé, ce qui arrive souvent : le rapprochement entre grilles reste
> purement lexical, et deux grilles qui prescrivent la même chose autrement ne
> se rejoignent pas.
>
> Un sous-bloc existe pour **chacun des diagnostics attendus de la SSP**
> (docs/ecos-priorites-2026.yaml), y compris ceux qu'aucune grille de la SSP
> ne documente. Ce sous-bloc vide dit alors laquelle des deux situations
> s'applique : soit une **autre SSP** documente ce diagnostic, et il y renvoie ;
> soit le corpus l'ignore, et c'est un **trou de révision** à combler ailleurs.
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

# LA MENTION PRECEDENTE ETAIT FAUSSE POUR UN TIERS DES SOUS-BLOCS VIDES : elle
# disait « aucune grille du CORPUS » alors que le corpus documente bel et bien
# le diagnostic, sous un libelle identique, dans une AUTRE SSP. L'etudiant
# lisait « Dyspnée — si Embolie pulmonaire : trou de révision » et concluait
# qu'il n'y avait rien a reviser, ratant quatre grilles rangees sous
# « Douleur Thoracique » et « Douleur du Membre Inférieur ». Le renvoi
# transforme le faux cul-de-sac en lien utile.
AILLEURS = ("*Aucune grille de cette SSP ne documente ce diagnostic* — mais le "
            "corpus le documente ailleurs : {renvois}.")

TOUT_PARTAGE = ("*Aucun item propre à ce diagnostic* — tout son management "
                "figure dans l'encadré partagé ci-dessus.")

SANS_MANAGEMENT = ("*La ou les grilles de ce diagnostic ne cotent aucun item de "
                   "management* — elles s'arrêtent à l'anamnèse et au status.")


def tri_clinique(nom):
    """Cle de tri d'un libelle francais : accents et casse neutralises.

    `sorted()` brut trie sur les points de code : « Pyélonéphrite » passait
    avant « Péritonite » (é > é ? non : « e » < « é »), « DMLA » avant
    « Décollement de rétine », et « Maladie cœliaque » apres « MICI ». Neuf
    mementos sur trente-deux etaient concernes, et l'ordre compte precisement
    la ou il y a vingt boites a parcourir. Le libelle brut departage a
    egalite, pour que le tri reste total et donc reproductible.
    """
    return (sans_accent(nom).lower(), nom)


def documente_ailleurs(groupes):
    """diagnostic -> {SSP: nombre de grilles}, sur TOUT le corpus.

    Sert a ne plus annoncer « aucune grille du corpus » quand une autre SSP
    documente le meme diagnostic, sous le meme libelle. Se calcule sur le
    corpus entier et non sur le lot : la question posee est « ce diagnostic
    existe-t-il quelque part », pas « dans le lot du jour ». C'est le RENDU
    qui decide de lier ou de simplement nommer, selon que la SSP porteuse
    aura, ou non, un memento a l'issue de cette execution.
    """
    out = {}
    for ssp, cas_list in groupes.items():
        for cas in cas_list:
            if cas["diagnostic"]:
                porteuses = out.setdefault(cas["diagnostic"], {})
                porteuses[ssp] = porteuses.get(ssp, 0) + 1
    return out


def renvois(porteuses, rendues):
    """« [[Mémento — Dyspnée]] (3 grilles) · « Fièvre » (1 grille, hors lot) ».

    Une SSP qui n'aura pas de memento a l'issue de cette execution est NOMMEE
    mais pas liee : un lien Obsidian non resolu promet une page qui n'existe
    pas, et proposerait de la creer vide au premier clic.
    """
    parts = []
    for ssp in sorted(porteuses, key=lambda s: (-porteuses[s],) + tri_clinique(s)):
        n = porteuses[ssp]
        grilles = f"{n} grille{'s' if n > 1 else ''}"
        parts.append(f"[[{PREFIXE}{ssp}]] ({grilles})" if ssp in rendues
                     else f"« {ssp} » ({grilles}, hors lot)")
    return lib_rendu.SEPARATEUR.join(parts)


def blocs_management(cas_list, cas_ssp, diag_par_cas, ssp, attendus,
                     ailleurs=None, rendues=()):
    """Les encadres 💊 d'une SSP : le partage, puis un sous-bloc par diagnostic.

    CINQ SORTES DE SOUS-BLOCS, et le lecteur doit pouvoir les distinguer :

      - avec items       le management propre au diagnostic ;
      - sans grille      attendu de la SSP, et introuvable dans TOUT le
                         corpus. Le sous-bloc reste, et le dit : c'est une
                         lacune de revision, pas un defaut du memento
                         (decision de l'auteur du 2026-08-15) ;
      - ailleurs         attendu ici, mais documente sous le meme libelle par
                         une AUTRE SSP. Le sous-bloc renvoie vers elle plutot
                         que d'annoncer un cul-de-sac qui n'existe pas ;
      - sans management  des grilles de cette SSP documentent le diagnostic,
                         mais aucune ne cote d'item de management (AZYGOS-4,
                         HypoTA orthostatique, s'arrete au status). NE PAS
                         confondre avec le suivant : renvoyer vers « l'encadre
                         partage ci-dessus » designerait un encadre qui, dans
                         ce cas-la, n'existe pas ;
      - tout partage     le diagnostic est documente, ses grilles cotent bien
                         du management, mais chacun de ses items est aussi
                         porte par un autre diagnostic. L'encadre partage
                         existe alors forcement, et les contient.

    IL N'Y A PLUS D'ENCADRE 💊 SANS TITRE. Depuis le seuil a deux, un item
    porte par un seul diagnostic va dans le sous-bloc de ce diagnostic — y
    compris quand la SSP n'en compte qu'un. L'encadre de tete ne recoit donc
    que du partage, et ne peut plus presenter comme general un contenu qui ne
    l'est pas.

    Chaque sous-bloc est marque sur les GRILLES DE SON DIAGNOSTIC, via
    `lib_fusion.restreindre()` : « 2 grilles sur 3 » y compte les grilles de
    ce diagnostic, pas celles de la SSP. Le partage, lui, se marque sur toute
    la SSP et nomme ses diagnostics (`lib_rendu.marque_partage`).
    """
    ailleurs = ailleurs or {}
    partage, propres = lib_fusion.scinder_management(cas_list, diag_par_cas, ssp, attendus)
    documentes = set(diag_par_cas.values())
    cotes = {diag_par_cas[c["id"]] for c in cas_list if c["id"] in diag_par_cas
             and any(genre == "item" for genre, _, _, _ in c["sections"].get("m", []))}

    blocs = []
    bloc = lib_rendu.encadre("success", "💊 Management — partagé par plusieurs diagnostics",
                             [_nettoie(g) for g in partage], cas_ssp, diag_par_cas,
                             marquage=lib_rendu.marque_partage)
    if bloc:
        blocs.append(bloc)

    for diagnostic in sorted(documentes | set(attendus), key=tri_clinique):
        items = [_nettoie(g) for g in propres.get(diagnostic, [])]
        cas_diag = sorted(c for c, d in diag_par_cas.items() if d == diagnostic)
        mention = None
        if not items:
            porteuses = {s: n for s, n in ailleurs.get(diagnostic, {}).items() if s != ssp}
            if diagnostic in cotes:
                mention = TOUT_PARTAGE
            elif diagnostic in documentes:
                mention = SANS_MANAGEMENT
            elif porteuses:
                mention = AILLEURS.format(renvois=renvois(porteuses, rendues))
            else:
                mention = SANS_GRILLE
        bloc = lib_rendu.encadre("success", f"💊 Management — si {diagnostic}",
                                 lib_fusion.restreindre(items, cas_diag),
                                 cas_diag, diag_par_cas, mention=mention)
        if bloc:
            blocs.append(bloc)
    return blocs


def memento(ssp, cas_list, attendus=(), ailleurs=None, rendues=()):
    """Le document Markdown complet d'une SSP."""
    cas_ssp = sorted(c["id"] for c in cas_list)
    diag_par_cas = {c["id"]: c["diagnostic"] for c in cas_list if c["diagnostic"]}
    documentes = set(diag_par_cas.values())
    total = len(documentes)
    attendus_sans_grille = len(set(attendus) - documentes)
    specialite = lib_ssp.specialite(ssp)
    etoile = " ⭐️" if lib_ssp.priorite(ssp) in ("Top 18", "Haut rendement") else ""

    blocs = []
    for genre, titre, prefixe in (("note", "📋 Anamnèse", "a"), ("tip", "🩺 Status", "e")):
        groupes = [_nettoie(g) for g in lib_fusion.apparier(cas_list, prefixe, ssp)]
        bloc = lib_rendu.encadre(genre, titre, groupes, cas_ssp, diag_par_cas)
        if bloc:
            blocs += [bloc, ""]
    for bloc in blocs_management(cas_list, cas_ssp, diag_par_cas, ssp, attendus,
                                 ailleurs, rendues):
        blocs += [bloc, ""]

    # LE TITRE DE NIVEAU 1 EST LA SSP, pas la specialite : un fichier ne porte
    # qu'une SSP, la specialite n'y groupe rien, et 11 des 33 SSP n'ont pas
    # encore de page dans le coffre — elles affichaient « # Non classé ».
    #
    # « N diagnostics documentes » ET « M attendus sans grille » : le seul
    # compte des documentes mentait par omission, un memento annoncant
    # « 2 diagnostics distincts » au-dessus d'une section 💊 qui en aligne cinq.
    ligne = [f"{len(cas_list)} grille{'s' if len(cas_list) > 1 else ''}",
             f"{total} diagnostic{'s' if total > 1 else ''} documenté{'s' if total > 1 else ''}"]
    if attendus_sans_grille:
        ligne.append(f"{attendus_sans_grille} attendu"
                     f"{'s' if attendus_sans_grille > 1 else ''} sans grille")
    if specialite != "Non classé":
        ligne.insert(0, specialite)
    corps = [f"# {ssp}{etoile}", "", "*" + " · ".join(ligne) + f"* — [[SSP — {ssp}]]", "",
             inventaire(cas_list), ""] + blocs

    champs = [f'aliases:\n  - "Mémento {ssp}"', f"type: {TYPE}", f'ssp: "{ssp}"']
    if specialite != "Non classé":
        champs.append(f'specialite: "{specialite}"')
    champs.append(f"cas: {len(cas_list)}")
    champs.append(f"diagnostics: {total}")
    champs.append(f"attendus_sans_grille: {attendus_sans_grille}")
    tags = ["  - ecos/memento"]
    if any(c["id"] in lib_ssp.OFFICIELLES for c in cas_list):
        tags.append("  - ecos/grille-officielle")
    tags.append("  - ecos/grille-non-officielle")
    champs.append("tags:\n" + "\n".join(tags))
    champs.append("cssclasses:\n  - skill-ecos")

    return (f"---\n{chr(10).join(champs)}\n---\n\n{lib_rendu.LEGENDE}\n\n"
            f"{entete(cas_list)}\n\n{chr(10).join(corps).rstrip()}\n")


def documents(lot):
    """SSP -> son memento Markdown, pour le lot demande (None = toutes).

    Assemble tout ce que le rendu d'une SSP demande de connaitre des AUTRES :
    `documente_ailleurs` renvoie un sous-bloc vide vers la SSP qui porte le
    diagnostic, et `rendues` dit si ce renvoi peut devenir un lien.

    SEAM PARTAGE AVEC LES CONTROLES, et c'est sa raison d'etre : le cablage
    « l'index se calcule sur le CORPUS ENTIER, le rendu sur le LOT » ne se
    verifie pas depuis `blocs_management`, qui recoit l'index tout fait. Une
    mutation remplacant `par_ssp(None)` par `par_ssp(lot)` passait tous les
    controles tout en transformant en faux trou de revision les diagnostics
    que seules des SSP hors lot documentent.

    Rend aussi le regroupement et les SSP ecartees, dont l'appelant a besoin
    pour son compte rendu.
    """
    tous = par_ssp(None)
    groupes = tous if lot is None else {s: v for s, v in tous.items() if s in lot}
    attendus = diagnostics_attendus()
    ailleurs = documente_ailleurs(tous)

    # Une barre oblique ferait un sous-dossier ; un guillemet double casserait
    # le frontmatter, ou les valeurs sont quotees. Les SSP ecartees le sont
    # AVANT le rendu, pour que `rendues` — qui decide si un renvoi devient un
    # lien ou un simple nom — ne promette pas un fichier qui ne sera pas ecrit.
    ignorees = sorted(s for s in groupes if "/" in s or '"' in s)
    rendues = {s for s in groupes if s not in ignorees}
    docs = {ssp: memento(ssp, groupes[ssp], attendus.get(ssp, ()), ailleurs, rendues)
            for ssp in sorted(rendues)}
    return docs, groupes, ignorees


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
    # TOUT EST CONSTRUIT AVANT D'EFFACER QUOI QUE CE SOIT : une exception a la
    # vingtieme SSP laissait sinon 33 fichiers effaces et 19 reecrits.
    docs, groupes, ignorees = documents(lot)

    SORTIE.mkdir(parents=True, exist_ok=True)
    nettoyer()
    for ssp, doc in docs.items():
        cible = SORTIE / unicodedata.normalize("NFC", f"{PREFIXE}{ssp}.md")
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
