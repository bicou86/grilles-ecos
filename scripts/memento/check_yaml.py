"""Verifie le lecteur YAML minimal sur des cas construits. Sortie 1 si ecart."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml

PLAT = '''# commentaire ignore
"RESCOS-12b": Trouble panique
AMBOSS-1: "Cholecystite aigue"

GERMAN-5: Contusion   # commentaire de fin de ligne
'''

GROUPE = '''"Douleur Thoracique":
  "Caracterisation de la douleur": Caracterisation de la douleur
  Douleurs: Caracterisation de la douleur
"Fatigue":
  "Formule sanguine complete": FSC
'''


def ecrire(texte):
    f = tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False, encoding="utf8")
    f.write(texte)
    f.close()
    return Path(f.name)


def attend_erreur(fonction, *args):
    """Appelle `fonction(*args)` et rend le message si ValueError est levee, sinon None."""
    try:
        fonction(*args)
    except ValueError as e:
        return str(e)
    return None


def main():
    ecarts = []
    plat = lib_yaml.lire_plat(ecrire(PLAT))
    attendu = {"RESCOS-12b": "Trouble panique", "AMBOSS-1": "Cholecystite aigue",
               "GERMAN-5": "Contusion"}
    if plat != attendu:
        ecarts.append(f"lire_plat\n    attendu : {attendu}\n    obtenu  : {plat}")

    groupe = lib_yaml.lire_groupe(ecrire(GROUPE))
    attendu = {"Douleur Thoracique": {"Caracterisation de la douleur": "Caracterisation de la douleur",
                                      "Douleurs": "Caracterisation de la douleur"},
               "Fatigue": {"Formule sanguine complete": "FSC"}}
    if groupe != attendu:
        ecarts.append(f"lire_groupe\n    attendu : {attendu}\n    obtenu  : {groupe}")

    if lib_yaml.lire_plat(Path("/inexistant.yaml")) != {}:
        ecarts.append("un fichier absent doit rendre un dictionnaire vide")

    # Cas 1 (critique) : valeur quotee suivie d'un commentaire de fin de
    # ligne — le guillemet fermant doit borner la valeur, pas le commentaire.
    plat = lib_yaml.lire_plat(ecrire('AMBOSS-1: "Cholecystite aigue" # commentaire\n'))
    attendu = {"AMBOSS-1": "Cholecystite aigue"}
    if plat != attendu:
        ecarts.append(f"valeur quotee + commentaire\n    attendu : {attendu}\n    obtenu  : {plat}")

    # Cas 2 (important) : un '#' non isole par des espaces fait partie de la
    # valeur, ce n'est pas un commentaire.
    plat = lib_yaml.lire_plat(ecrire("GERMAN-9: Grade #3 sur 4\n"))
    attendu = {"GERMAN-9": "Grade #3 sur 4"}
    if plat != attendu:
        ecarts.append(f"diese non isole\n    attendu : {attendu}\n    obtenu  : {plat}")

    # Cas 3 (important) : un troisieme niveau d'indentation dans un groupe
    # doit lever plutot que d'etre aplati dans le groupe courant.
    message = attend_erreur(
        lib_yaml.lire_groupe,
        ecrire('"Groupe":\n  "Sub1": val\n    "Sub2": val2\n'),
    )
    if message is None:
        ecarts.append("un troisieme niveau d'indentation aurait du lever ValueError")

    # Cas 4 (important) : une cle vide est une faute de saisie, pas une
    # entree valide.
    message = attend_erreur(lib_yaml.lire_plat, ecrire('"": valeur\n'))
    if message is None:
        ecarts.append("une cle vide aurait du lever ValueError")

    # Cas 5 (mineur) : un guillemet ouvrant non ferme doit lever plutot que
    # d'etre silencieusement retire.
    message = attend_erreur(lib_yaml.lire_plat, ecrire('CLE: "valeur non fermee\n'))
    if message is None:
        ecarts.append("un guillemet non ferme aurait du lever ValueError")

    # Cas 6 (mineur) : les messages d'erreur sont des sorties utilisateur et
    # doivent etre accentues (ex. "entree" -> "entrée").
    message = attend_erreur(lib_yaml.lire_groupe, ecrire('  "Sub": valeur\n'))
    if message is None or "entrée hors groupe" not in message:
        ecarts.append(
            f"message d'erreur non accentue pour une entree hors groupe : {message!r}"
        )

    # Cas 7 (CRITIQUE) : une cle dupliquee disparaissait en silence — la
    # seconde ecrasait la premiere sans un mot. C'est la panne muette meme que
    # ces tables curees existent pour fermer : une entree ecrite, relue,
    # commitee, et sans effet. Les trois formes doivent lever.
    message = attend_erreur(
        lib_yaml.lire_plat, ecrire("AMBOSS-1: Cholecystite\nAMBOSS-1: Appendicite\n"))
    if message is None or "Cholecystite" not in message:
        ecarts.append(
            f"une clé dupliquée à plat aurait dû lever, en nommant la valeur perdue : {message!r}")

    message = attend_erreur(
        lib_yaml.lire_groupe,
        ecrire('"Toux":\n  "Tabac": Tabagisme\n  "Tabac": Noxes\n'))
    if message is None or "Toux" not in message:
        ecarts.append(
            f"une clé dupliquée dans un groupe aurait dû lever, en nommant le groupe : {message!r}")

    message = attend_erreur(
        lib_yaml.lire_groupe,
        ecrire('"Toux":\n  "Tabac": Tabagisme\n"Toux":\n  "Alcool": Noxes\n'))
    if message is None:
        ecarts.append("un groupe rouvert plus bas aurait dû lever ValueError")

    # Cas 8 (important) : deux cles DISTINCTES dans un meme groupe restent
    # valides — le refus du doublon ne doit pas interdire un groupe normal.
    groupe = lib_yaml.lire_groupe(
        ecrire('"Toux":\n  "Tabac": Tabagisme\n  "Alcool": Noxes\n'))
    attendu = {"Toux": {"Tabac": "Tabagisme", "Alcool": "Noxes"}}
    if groupe != attendu:
        ecarts.append(f"groupe a deux cles distinctes\n    attendu : {attendu}\n"
                      f"    obtenu  : {groupe}")

    if ecarts:
        print("ÉCHEC —", len(ecarts), "écart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — lecteur YAML conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
