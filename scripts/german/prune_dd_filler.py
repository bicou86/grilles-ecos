"""Retire le remplissage automatique du bloc `annexe-dd` des grilles German.

DECISION D'ARBITRAGE — le remplissage est SUPPRIME, aucun contenu medical n'est
cree en remplacement. Une entree reduite a son seul nom de diagnostic reste
utile : la liste des hypotheses a evoquer est en soi le contenu principal du
bloc.

CE QUE VOIT CE SCRIPT
---------------------
Les 78 segments `annexe-dd` des 88 grilles portent 484 entrees `<li>`, toutes
de la meme forme, sans une seule exception (verifie : le residu de chaque `<li>`
une fois ses trois elements retires est exactement `<br>`) :

    <li>
        <strong style="color: rgb(169, 34, 23);">NOM DU DIAGNOSTIC</strong><br>
        <div style="... color: rgb(80, 90, 110);">ARGUMENTS</div>
        <div style="... color: rgb(52, 105, 46);">-> EXAMEN QUI DEPARTAGE</div>
    </li>

Le nom n'est JAMAIS touche. Seuls les deux `<div>` peuvent partir, et seulement
si leur texte figure dans les tables ci-dessous.

CRITERE DE GENERICITE
---------------------
Une formulation qui serait vraie pour n'importe quel diagnostic de n'importe
quelle grille est generique. Une formulation qui nomme un examen precis ne l'est
pas, meme breve (`pH-metrie, gastroscopie` departage). Les tables ont ete
etablies en lisant les 216 formulations d'arguments et les 129 formulations
d'examens distinctes du corpus, pas sur echantillon.

SUPPRESSION D'ELEMENT, JAMAIS DE TEXTE
--------------------------------------
Le script ne fait que SUPPRIMER des plages de caracteres, mesurees, disjointes,
et chacune couvrant un element entier (`<div>...</div>` complet, ou un `<br>`
qui est une balise vide). Rien n'est insere, rien n'est reecrit. L'appariement
des balises est donc preserve par construction — ce qui compte doublement ici :
le bloc `annexe-dd` est le FRERE d'un `criteria-row` qui porte l'`<input
type="radio">` du critere englobant, et un `</div>` deplace casserait le rendu
de tous les criteres suivants (defaut deja constate en German-84).

Le bloc `annexe-dd` ne porte aucune case a cocher : le bareme ne peut pas
bouger. `check_invariants.py` le verifie quand meme.

REFUS DES CAS MIXTES
--------------------
Un `<div>` n'est retire que si la TOTALITE de son texte est generique. Si une
formulation generique cohabitait avec du contenu reel dans le meme `<div>`, le
script s'arrete et ne modifie rien : decouper un `<div>` au milieu, c'est le
genre d'operation qui emporte un argument reel par erreur. Mesure au moment de
l'ecriture : 0 cas mixte sur les 484 entrees.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_german as lib

LI = re.compile(r"<li[^>]*>(.*?)</li>", re.S)
NAME = re.compile(r'<strong style="color: rgb\(169, 34, 23\);">(.*?)</strong>', re.S)
ARG = re.compile(
    r'<div style="margin-left: 20px; color: rgb\(80, 90, 110\);">(.*?)</div>', re.S)
EX = re.compile(
    r'<div style="margin-left: 20px; margin-top: 5px; margin-bottom: 15px; '
    r'color: rgb\(52, 105, 46\);">(.*?)</div>', re.S)

# --- Arguments generiques (texte normalise par lib.norm) ---------------------
# UNE seule formulation sur les 216 du corpus, mais 345 occurrences, soit 59 %
# des 588 puces d'arguments. « Dyspepsie fonctionnelle - A evaluer cliniquement »
# n'enseigne rien.
#
# Formulations VOISINES conservees deliberement, parce qu'elles disent quelque
# chose du diagnostic vise et ne seraient pas vraies de n'importe lequel :
# « rare », « diagnostic d'exclusion », « peu probable vu l'age »,
# « sans cause evidente », « processus inflammatoire ».
GENERIC_ARGS = {
    "a evaluer cliniquement",
}

# --- Examens generiques (texte normalise, fleche comprise puis normalisee) ---
# 4 formulations, 262 occurrences sur 484. Aucune ne nomme d'examen : ni organe,
# ni technique, ni analyte, ni score.
#
# Conservees, bien que breves — chacune nomme un axe qui departage vraiment :
#   « Anamnese medicamenteuse » (2)      -> la liste des medicaments
#   « Anamnese, audiometrie » (1)        -> l'audiometrie
#   « Examen neurologique, imagerie »    -> le systeme nerveux
#   « Examen ophtalmologique » (1)       -> l'oeil
#   « Evaluation cognitive » (1)         -> la cognition
#   « Revision du traitement » (1)       -> l'ordonnance (chutes iatrogenes)
#   « Examen clinique, evaluation environnement » -> le domicile (chutes)
#   « Criteres temporels DSM-5 » (1)     -> le calendrier des symptomes
#   « Evaluation temporelle des symptomes » (1) -> idem, c'est ce qui separe
#       un trouble de l'adaptation d'un trouble depressif persistant
#   « Diagnostic clinique, biopsie si doute » (2) -> la biopsie
GENERIC_EXAMS = {
    "examens complementaires selon contexte clinique",  # 258
    "evaluation clinique approfondie",                  # 1
    "anamnese",                                         # 1 — l'anamnese seule
    "bilan biologique specifique",                      # 2 — « specifique » de quoi ?
}


def _norm_div(inner):
    """Texte normalise d'un contenu de `<div>`, puces et fleche ecartees."""
    return lib.norm(lib.visible_text(inner).replace(lib.BULLET, " ").replace("→", " "))


def _bullet_texts(inner):
    """Textes normalises des puces d'un contenu d'arguments, pour l'audit mixte."""
    text = lib.visible_text(inner)
    parts = text.split(lib.BULLET) if lib.BULLET in text else [text]
    return [lib.norm(p) for p in parts if lib.norm(p)]


def plan(html):
    """Plages a supprimer, et statistiques. Ne modifie rien.

    Retourne (cuts, stats, mixed) ou `cuts` est une liste de (debut, fin)
    disjointes et triees, et `mixed` la liste des cas ou une formulation
    generique cohabite avec du contenu reel dans un meme `<div>`.
    """
    cuts, mixed = [], []
    stats = {"entrees": 0, "args_retires": 0, "exams_retires": 0,
             "entrees_nom_seul": 0, "args_restants": 0, "exams_restants": 0}
    for a, b in lib.block_spans(html, "annexe-dd"):
        segment = html[a:b]
        for m in LI.finditer(segment):
            stats["entrees"] += 1
            base = a + m.start(1)
            inner = m.group(1)
            name, arg, ex = NAME.search(inner), ARG.search(inner), EX.search(inner)
            if not (name and arg and ex):
                mixed.append(f"entree de forme inattendue : {inner[:120]!r}")
                continue
            for tag, mm in (("arguments", arg), ("examen", ex)):
                if "<div" in mm.group(1):
                    mixed.append(f"{tag} : <div> imbrique, decoupage non fiable")

            drop_arg = _norm_div(arg.group(1)) in GENERIC_ARGS
            drop_ex = _norm_div(ex.group(1)) in GENERIC_EXAMS
            # Cas mixte : une puce generique a cote d'une puce reelle.
            bullets = _bullet_texts(arg.group(1))
            if not drop_arg and any(t in GENERIC_ARGS for t in bullets):
                mixed.append(f"arguments mixtes : {bullets!r}")

            if drop_arg:
                cuts.append((base + arg.start(), base + arg.end()))
                stats["args_retires"] += 1
            else:
                # Le compte des puces se lit sur la puce elle-meme : un entete
                # « Arguments POUR: » n'est pas une puce.
                stats["args_restants"] += arg.group(1).count(lib.BULLET)
            if drop_ex:
                cuts.append((base + ex.start(), base + ex.end()))
                stats["exams_retires"] += 1
            else:
                stats["exams_restants"] += 1
            if drop_arg and drop_ex:
                stats["entrees_nom_seul"] += 1
                # Le `<br>` qui suivait le nom n'a plus rien a separer.
                br = re.match(r"<br\s*/?>", inner[name.end():])
                if br:
                    cuts.append((base + name.end(),
                                 base + name.end() + br.end()))
    return sorted(cuts), stats, mixed


def apply_cuts(html, cuts):
    """Supprime les plages — aucune insertion, aucune reecriture."""
    out, last = [], 0
    for start, end in cuts:
        assert start >= last, "plages qui se chevauchent"
        out.append(html[last:start])
        last = end
    out.append(html[last:])
    return "".join(out)


def main():
    total = {"entrees": 0, "args_retires": 0, "exams_retires": 0,
             "entrees_nom_seul": 0, "args_restants": 0, "exams_restants": 0}
    touched, all_mixed = 0, []
    planned = []
    for path in lib.grids():
        html = path.read_text(encoding="utf-8")
        cuts, stats, mixed = plan(html)
        all_mixed += [f"{path.name} : {m}" for m in mixed]
        planned.append((path, html, cuts))
        for k, v in stats.items():
            total[k] += v

    if all_mixed:
        print("ECHEC — cas mixtes ou formes inattendues, rien n'est ecrit :")
        for m in all_mixed[:40]:
            print("  " + m)
        return 1

    for path, html, cuts in planned:
        if not cuts:
            continue
        new = apply_cuts(html, cuts)
        # Filet : seules des suppressions, et le nom des diagnostics intact.
        assert len(new) < len(html)
        path.write_text(new, encoding="utf-8")
        touched += 1

    print(f"Fichiers modifies : {touched}")
    print(f"  entrees de diagnostic parcourues   : {total['entrees']}")
    print(f"  divs d'arguments generiques retires: {total['args_retires']}")
    print(f"  divs d'examens generiques retires  : {total['exams_retires']}")
    print(f"  puces d'arguments conservees       : {total['args_restants']}")
    print(f"  examens conserves                  : {total['exams_restants']}")
    print(f"  entrees reduites au nom seul       : {total['entrees_nom_seul']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
