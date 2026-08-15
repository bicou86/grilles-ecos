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
