"""Cle canonique d'un libelle d'item de memento — source unique.

Sert a comparer deux libelles au-dela des differences de mise en forme
(accents, casse, ordre des mots, pluriel simple) sans fusionner des libelles
cliniquement distincts. Utilisee par `check_referentiel.py` (tache 5, ecart
au referentiel officiel) et par `signature()` (tache 7, fusion inter-grilles)
: une seule regle, importee des deux cotes, plutot que deux copies qui
divergeraient au premier correctif.

Version anterieure (abandonnee) : un token etait retenu s'il faisait plus de
trois lettres. Cette regle produisait de vraies collisions verifiees sur le
corpus — « Reflexes MI » et « Reflexes MS » partageaient la meme cle parce
que « MI »/« MS » font deux lettres, alors que « Allergie » et « Allergies »
n'en partageaient pas, un pluriel de trois lettres significatives franchissant
le seuil dans un sens et pas l'autre. Remplacee ici par une liste explicite
de mots vides (MOTS_VIDES) : plus aucun sigle court n'est efface, seul un mot
grammatical nomme l'est.
"""
import re
import unicodedata

# Mots vides francais : jamais porteurs de sens clinique a eux seuls, retires
# de la cle quelle que soit leur longueur. Liste FERMEE et courte a dessein :
# tout le reste est garde tel quel, y compris un sigle de deux lettres
# (MI, MS, VS, ORL, TSH...) qui porte precisement le sens clinique.
# "a"/"d"/"l" couvrent les elisions (preposition a accentuee, d', l') une
# fois les accents retires et l'apostrophe eclatee en deux tokens par la
# tokenisation.
MOTS_VIDES = {"de", "du", "des", "la", "le", "les", "et", "ou", "un", "une",
              "au", "aux", "en", "sur", "par", "a", "d", "l"}

_TOKEN = re.compile(r"[a-z0-9]+")


def _singulier(mot):
    """Retire un 's' final simple sur un token de plus de trois lettres.

    Volontairement grossier, PAS un stemmer : rejoint "allergies"/"allergie",
    mais ne rejoint ni "statut"/"status" (graphies distinctes, pas un
    pluriel), ni les pluriels irreguliers ("cheval"/"chevaux"). Le seuil de
    trois lettres protege les tokens courts ou un 's' final est le mot
    lui-meme, pas une marque de pluriel (ex. "vis" ne doit pas devenir "vi").
    """
    if len(mot) > 3 and mot.endswith("s"):
        return mot[:-1]
    return mot


def cle(texte):
    """Forme canonique d'un libelle de memento.

    Pipeline : minuscule, accents retires (NFD), tokenise sur toute
    ponctuation ou espace (apostrophe et slash inclus), mots vides
    francais retires (MOTS_VIDES, quelle que soit leur longueur), pluriel
    simple neutralise sur le reste (_singulier), tokens restants tries pour
    ignorer l'ordre du libelle source. Deux libelles qui ne different que
    par la casse, les accents, un mot vide ou un pluriel simple obtiennent
    la meme cle ; deux libelles qui different par un sigle, une localisation
    anatomique ou un mot de contenu (ex. "mode") restent distincts.
    """
    t = unicodedata.normalize("NFD", texte.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    tokens = [_singulier(m) for m in _TOKEN.findall(t) if m not in MOTS_VIDES]
    return " ".join(sorted(tokens))
