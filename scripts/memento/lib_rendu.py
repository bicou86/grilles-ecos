"""Rendu Markdown des mementos — callouts Obsidian, cases a cocher imbriquees.

La charte est celle du memento des neuf grilles officielles : legende, titre de
specialite, encadres 📋 / 🩺 / 🔬 / 💊, numerotation repartant a 1 dans chaque
encadre.

MARQUAGE DU SPECIFIQUE. Un item porte par TOUTES LES GRILLES de la SSP reste
nu ; sinon il est suffixe de ce qui le porte — les diagnostics quand ils
discriminent exactement, le compte de grilles sinon. La regle porte sur les
grilles et non sur les diagnostics : deux grilles peuvent partager un
diagnostic, et un item present dans une seule des deux n'est pas pour autant
un item de ce diagnostic. Voir `marque()` pour l'invariant complet.

Le surlignage ==…== d'Obsidian a ete ecarte : il colore sans dire pourquoi,
depend du theme et ne survit pas a l'export. Le suffixe est greppable et
lisible en clair.

DETERMINISME. `lib_fusion.apparier()` rend des groupes dont le champ `cas` est
un `set` : son ordre d'iteration depend de PYTHONHASHSEED. Tout parcours d'un
`cas` fait ici passe donc par `sorted()` — sans quoi deux executions
produiraient des suffixes dans deux ordres differents, et les fichiers
cesseraient d'etre idempotents.
"""

import re

# LA LEGENDE DES MEMENTOS PAR SSP N'EST PLUS CELLE DU MEMENTO OFFICIEL : elle
# ne porte qu'un 💊, la ou l'officiel partage le management en 🔬 (examens) et
# 💊 (prise en charge). Ce partage n'existe pas dans les grilles ; le memento
# officiel le declare A LA MAIN, critere par critere (table EXAMENS de
# scripts/build_obsidian_memento.py, pour 57 lignes de management sur
# 9 grilles). A 252 grilles et 1 988 items de management, il faudrait le
# deviner — et un motif lexical essaye sur le seul echantillon etiquete qui
# existe (ces 9 grilles) laisse AU MOINS 5 erreurs SEMANTIQUES sur 57 lignes,
# dans les deux sens : « Propose un dosage des anticorps anti-TPO » (un
# examen) tombe en 💊, « Suivi : prevoir un controle biologique dans
# 6-8 semaines » (un suivi) en 🔬. Motif non optimise — un motif plus soigne
# corrigerait des erreurs de frontiere de mot, pas celles-la, qui tiennent au
# SENS de la ligne et qu'aucune liste de mots-cles ne tranche.
# Une erreur de rangement ne se voit pas a la lecture, contrairement a un
# suffixe faux : le lecteur croit l'encadre 🔬 exhaustif et ne cherche pas
# l'examen ailleurs. Le cout est reel et assume : le lecteur d'un memento par
# SSP trie lui-meme examens et traitement dans l'encadre 💊.
LEGENDE = """> [!info] Légende
>
> - 📋 = Anamnèse — ce qu'il faut absolument avoir demandé
> - 🩺 = Status — le geste ou le signe qui fait la différence
> - 💊 = Management — examens complémentaires **et** prise en charge
> - 🚨 = urgence
> - 🚩 = red flag à ne jamais rater
> - ⭐️ = SSP ou diagnostic fréquemment rencontré à l'ECOS"""

SEUIL_ABREGE = 3   # au-dela, on compte au lieu d'enumerer

# SEPARATEUR ENTRE DIAGNOSTICS D'UN MEME SUFFIXE. La virgule etait ambigue :
# « *(Fracture du membre superieur (humerus, tete radiale))* » se lit comme
# deux diagnostics alors qu'il n'y en a qu'un, et 885 lignes portent un
# libelle a virgule ou a parenthese. Cette ambiguite a fait tomber trois
# regexes d'analyse successives, dont deux des miennes. Le point median ne
# figure dans aucun libelle de diagnostic de la table (verifie sur les 194) et
# le projet l'emploie deja comme separateur dans ecos-priorites-2026.yaml.
SEPARATEUR = " · "

# Glyphes decoratifs herites des grilles (⊕ = aggravant, ⊖ = soulageant) : ils
# doublent un libelle qui dit deja la meme chose (« ⊕ Facteurs aggravants »).
_GLYPHES = re.compile(r"[⊕⊖⊗⊘]")

# Libelle redige a la troisieme personne, adresse a l'examinateur·rice plutot
# qu'au candidat·e (« L'étudiant évoque le toucher rectal »). Un memento
# s'adresse a celui qui revise : on retire l'apostrophe de l'enonciateur.
_TIERS = re.compile(r"^L[e’']\s*(?:étudiant|candidat|examinateur)[e·s]*\s+", re.I)


def nettoie_libelle(titre):
    """Libelle d'affichage : sans glyphe decoratif ni enonciateur a la 3e personne."""
    titre = _GLYPHES.sub(" ", titre)
    titre = _TIERS.sub("", titre)
    titre = re.sub(r"\s+", " ", titre).strip(" -–—/")
    return titre[:1].upper() + titre[1:] if titre else titre


def _porteurs_attendus(diags, diag_par_cas):
    """Tous les cas dont le diagnostic figure dans `diags`."""
    return {c for c, d in diag_par_cas.items() if d in diags}


def marque(item, cas_ssp, diag_par_cas):
    """Suffixe un item de ce qui le porte, si toutes les grilles ne le portent pas.

    L'INVARIANT : la marque ne doit jamais permettre de conclure quelque chose
    de faux sur les grilles qui portent l'item. Trois formes, dans cet ordre :

      - NU              toutes les grilles de la SSP portent l'item. Pas
                        « tous les diagnostics » : une SSP peut compter trois
                        grilles de pneumonie, et un item porte par une seule
                        d'entre elles n'est pas un item de la pneumonie.
      - *(Diagnostic…)* les porteurs sont EXACTEMENT toutes les grilles de ces
                        diagnostics-la. Le lecteur peut donc conclure « propre
                        a ce diagnostic » sans se tromper. Au-dela de trois
                        diagnostics, on compte au lieu d'enumerer.
      - *(n grilles sur m)*  les diagnostics ne discriminent pas : les
                        porteurs sont un sous-ensemble strict des grilles d'un
                        diagnostic, ou l'une d'elles n'a pas de diagnostic
                        resolu. Nommer le diagnostic mentirait ; le compte,
                        lui, est vrai et dit au lecteur que la couverture est
                        partielle. C'est la forme qui rend le marquage utile
                        sur une SSP a diagnostic unique, ou l'ancienne regle
                        se taisait completement.

    `cas_ssp` est l'ensemble des identifiants de grille de la SSP.
    """
    porteurs = set(item["cas"])
    if porteurs >= set(cas_ssp):
        return item["titre"]
    diags = {diag_par_cas[c] for c in porteurs if c in diag_par_cas}
    fidele = (len(diags) > 0
              and all(c in diag_par_cas for c in porteurs)
              and _porteurs_attendus(diags, diag_par_cas) & set(cas_ssp) == porteurs)
    if fidele:
        if len(diags) > SEUIL_ABREGE:
            return f"{item['titre']} *({len(diags)} diagnostics)*"
        return f"{item['titre']} *({SEPARATEUR.join(sorted(diags))})*"
    pluriel = "s" if len(porteurs) > 1 else ""
    return f"{item['titre']} *({len(porteurs)} grille{pluriel} sur {len(cas_ssp)})*"


def marque_partage(item, cas_ssp, diag_par_cas):
    """Suffixe de l'encadre 💊 partage : les diagnostics SOUS LESQUELS l'item apparait.

    POURQUOI UNE SECONDE REGLE plutot que `marque()`. L'encadre partage
    remplace la recopie d'un meme item dans plusieurs sous-blocs ; ce qu'il
    doit rendre au lecteur, c'est precisement la liste que ces sous-blocs
    portaient. Or `marque()` ne la donne pas :

      - au-dela de SEUIL_ABREGE elle compte (« *(8 diagnostics)* »), ce qui
        efface l'information meme que le regroupement devait preserver ;
      - quand les porteurs ne sont pas EXACTEMENT toutes les grilles des
        diagnostics concernes — la moitie des items partages du corpus — elle
        se rabat sur « n grilles sur m » et ne nomme plus rien.

    CE QUE LE SUFFIXE AFFIRME ICI, et rien de plus : au moins une grille de
    chacun des diagnostics nommes porte cet item. Il n'affirme PAS que toutes
    les grilles de ces diagnostics le portent — c'est la difference avec
    `marque()`, et c'est pourquoi le compte de grilles est imprime dans le
    meme suffixe : « *(Angor · STEMI — 3 grilles sur 12)* » ne peut pas se
    lire comme « les grilles d'Angor et de STEMI, toutes ».

    Un item porte par TOUTES les grilles de la SSP reste nu, comme partout
    ailleurs. Un item qu'aucun diagnostic ne porte (aucune grille porteuse
    n'a de diagnostic resolu) retombe sur `marque()` : il n'y a rien a nommer.
    """
    porteurs = set(item["cas"])
    if porteurs >= set(cas_ssp):
        return item["titre"]
    diags = sorted({diag_par_cas[c] for c in porteurs if c in diag_par_cas})
    if not diags:
        return marque(item, cas_ssp, diag_par_cas)
    pluriel = "s" if len(porteurs) > 1 else ""
    return (f"{item['titre']} *({SEPARATEUR.join(diags)} — "
            f"{len(porteurs)} grille{pluriel} sur {len(cas_ssp)})*")


def _suffixe(item, rendu):
    """La part de suffixe d'un libelle rendu — vide si l'item est nu.

    Deduite du rendu plutot que recalculee : `marque()` reste la seule regle
    de marquage, et il ne peut pas y avoir deux facons de fabriquer un
    suffixe qui divergeraient un jour l'une de l'autre.
    """
    return rendu[len(item["titre"]):]


def encadre(genre, entete, items, cas_ssp, diag_par_cas, mention=None, marquage=None):
    """Un callout dont la liste est numerotee a partir de 1.

    UN SOUS-ITEM HERITE DE LA PORTEE DE SON PARENT et ne la repete pas : son
    suffixe n'est reaffiche que s'il DIFFERE de celui du parent, seul cas ou
    il apprend quelque chose (un sous-item plus etroit que l'item qui le
    porte). Sans cette elision, un item specifique a un diagnostic recopiait
    le meme suffixe sur chacun de ses sous-items — quatre repetitions d'une
    information deja lue une ligne plus haut, qui noyaient les rares lignes
    ou le suffixe disait vraiment quelque chose.

    `mention` est le texte que rend un encadre SANS AUCUN ITEM. Sans elle, un
    encadre vide reste absent, comme avant ; avec elle, il subsiste pour dire
    pourquoi il est vide — c'est ce qui permet au sous-bloc d'un diagnostic
    qu'aucune grille ne documente d'exister quand meme.

    `marquage` remplace `marque()` — c'est `marque_partage()` dans l'encadre
    💊 partage, et rien d'autre. L'elision du suffixe herite, elle, ne change
    pas : elle compare deux suffixes produits par LA MEME regle, quelle
    qu'elle soit.
    """
    marquage = marquage or marque
    if not items:
        return f"> [!{genre}] {entete}\n> {mention}" if mention else None
    out = [f"> [!{genre}] {entete}"]
    for numero, item in enumerate(items, 1):
        rendu = marquage(item, cas_ssp, diag_par_cas)
        out.append(f"> - [ ] **{numero}. {rendu}**")
        herite = _suffixe(item, rendu)
        for sous in item["sous"]:
            rendu_sous = marquage(sous, cas_ssp, diag_par_cas)
            if _suffixe(sous, rendu_sous) == herite:
                rendu_sous = sous["titre"]
            out.append(f"> \t- [ ] {rendu_sous}")
    return "\n".join(out)
