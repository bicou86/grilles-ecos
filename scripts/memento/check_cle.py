"""Verifie lib_cle.cle() sur des cas construits, notamment ceux qui ont fait
echouer l'ancien seuil "mots de plus de trois lettres". Sortie 1 si ecart.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib_cle import cle


def main():
    ecarts = []

    # Cas 1 (critique) : deux localisations anatomiques distinctes ne
    # doivent jamais fusionner. L'ancien seuil de longueur effacait "MI"/"MS"
    # (deux lettres) et rendait les deux libelles identiques.
    a, b = cle("Réflexes MI"), cle("Réflexes MS")
    if a == b:
        ecarts.append(f"'Réflexes MI' et 'Réflexes MS' ne doivent PAS avoir la meme cle "
                       f"(obtenu la meme : {a!r})")

    # Cas 2 (critique) : un pluriel simple doit fusionner avec son singulier.
    # "Allergies" est le libelle orphelin le plus frequent du rapport tache 5
    # (111 occurrences) precisement parce que ce cas etait rate avant.
    a, b = cle("Allergie"), cle("Allergies")
    if a != b:
        ecarts.append(f"'Allergie' et 'Allergies' doivent avoir la meme cle "
                       f"(obtenu {a!r} et {b!r})")

    # Cas 3 (important) : "Habitudes de vie" vs "Habitudes et mode de vie".
    # Decision retenue : ils restent DISTINCTS. "mode" est un mot de contenu,
    # pas un mot vide grammatical — MOTS_VIDES ne le retire pas — donc les
    # deux libelles portent une information differente et ne doivent pas
    # fusionner. (L'ancien seuil de longueur les fusionnait par accident,
    # car "de" et "vie" faisaient tous deux trois lettres ou moins.)
    a, b = cle("Habitudes de vie"), cle("Habitudes et mode de vie")
    if a == b:
        ecarts.append(f"'Habitudes de vie' et 'Habitudes et mode de vie' ne doivent PAS "
                       f"avoir la meme cle — 'mode' est un mot de contenu (obtenu la "
                       f"meme : {a!r})")

    # Cas 4 (important) : trois examens regionaux distincts, seulement
    # differencies par un complement de moins de quatre lettres dans
    # l'ancienne regle ("cou", "dos") ou un sigle ("ORL").
    c1, c2, c3 = cle("Examen ORL"), cle("Examen du cou"), cle("Examen du dos")
    if len({c1, c2, c3}) != 3:
        ecarts.append(f"'Examen ORL', 'Examen du cou', 'Examen du dos' doivent produire "
                       f"trois cles distinctes (obtenu {c1!r}, {c2!r}, {c3!r})")

    # Cas 5 (mineur) : casse, accent et ordre des mots sont neutralises.
    a, b = cle("Début / Durée"), cle("Début / durée")
    if a != b:
        ecarts.append(f"'Début / Durée' et 'Début / durée' doivent avoir la meme cle "
                       f"(obtenu {a!r} et {b!r})")

    # Cas 6 (mineur) : un sigle court reste significatif et distinct d'un
    # autre sigle court — pas seulement pour MI/MS (cas 1), verifie aussi sur
    # des sigles de laboratoire.
    a, b = cle("VS"), cle("CRP")
    if a == b:
        ecarts.append(f"'VS' et 'CRP' ne doivent PAS avoir la meme cle (obtenu {a!r})")

    if ecarts:
        print("ÉCHEC —", len(ecarts), "écart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — lib_cle.cle() conforme (collisions/non-collisions attendues)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
