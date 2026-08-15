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

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — lecteur YAML conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
