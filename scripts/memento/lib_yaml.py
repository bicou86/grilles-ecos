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

# Un '#' n'introduit un commentaire que s'il est isole par des espaces (ou en
# debut/fin de valeur) — sinon c'est un caractere ordinaire, comme dans
# "Grade #3 sur 4".
_COMMENTAIRE = re.compile(r'(?:^|(?<=\s))#(?=\s|$)')


def _valeur(brut, chemin, numero):
    """Nettoie une valeur : retire les guillemets ou le commentaire de fin de ligne."""
    if brut.startswith('"'):
        fin = brut.find('"', 1)
        if fin == -1:
            raise ValueError(f"{chemin}:{numero} — guillemet non fermé dans la valeur : {brut!r}")
        valeur, reste = brut[1:fin], brut[fin + 1:].strip()
        if reste and not reste.startswith("#"):
            raise ValueError(
                f"{chemin}:{numero} — caractères inattendus après la valeur quotée : {reste!r}"
            )
        return valeur
    m = _COMMENTAIRE.search(brut)
    if m:
        brut = brut[:m.start()]
    return brut.strip()


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
        cle = _cle(m.group("cle"))
        if not cle:
            raise ValueError(f"{chemin}:{numero} — clé vide")
        val = _valeur(m.group("val"), chemin, numero)
        yield numero, len(m.group("indent")), cle, val


def _poser(table, cle, val, chemin, numero, ou=""):
    """Ecrit `cle` dans `table`, et REFUSE d'ecraser une cle deja posee.

    UNE CLE DUPLIQUEE DISPARAISSAIT EN SILENCE : `table[cle] = val` ecrase, si
    bien que deux entrees de meme cle ne laissaient que la seconde, sans un
    mot. C'est exactement la classe de panne muette que ces tables curees
    existent pour fermer — une entree ecrite, relue, commitee, et sans effet.
    Le lecteur est strict partout ailleurs (indentation, guillemet non ferme,
    ligne non reconnue) ; il l'est ici aussi.
    """
    if cle in table:
        raise ValueError(f"{chemin}:{numero} — clé « {cle} » déjà définie{ou} : "
                         f"la première valeur ({table[cle]!r}) serait perdue")
    table[cle] = val


def lire_plat(chemin):
    """`cle: valeur` sur un seul niveau."""
    out = {}
    for numero, indent, cle, val in _lignes(chemin):
        if indent:
            raise ValueError(f"{chemin}:{numero} — indentation inattendue")
        _poser(out, cle, val, chemin, numero)
    return out


def lire_groupe(chemin):
    """`groupe:` puis `cle: valeur` indentes (un seul niveau)."""
    out, courant, indent_enfant, nom_groupe = {}, None, None, None
    for numero, indent, cle, val in _lignes(chemin):
        if indent == 0:
            if val:
                raise ValueError(f"{chemin}:{numero} — un groupe ne porte pas de valeur")
            if cle in out:
                raise ValueError(f"{chemin}:{numero} — groupe « {cle} » déjà ouvert plus "
                                 "haut : rassemblez ses entrées en un seul bloc")
            courant = out.setdefault(cle, {})
            nom_groupe = cle
            indent_enfant = None
        else:
            if courant is None:
                raise ValueError(f"{chemin}:{numero} — entrée hors groupe")
            if indent_enfant is None:
                indent_enfant = indent
            elif indent != indent_enfant:
                raise ValueError(
                    f"{chemin}:{numero} — profondeur d'indentation incohérente "
                    "(un seul niveau est permis)"
                )
            _poser(courant, cle, val, chemin, numero, f" dans « {nom_groupe} »")
    return out
