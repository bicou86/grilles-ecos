"""Les mementos par SSP commites sont ceux que le generateur produit. Sortie 1 si ecart.

check_fusion.py epingle le memento des neuf grilles officielles ; personne ne
gardait les 33 autres. Un changement de lib_rendu, lib_cle ou lib_extraction
commite sans regeneration les rendait silencieusement obsoletes, tous les
autres verificateurs restant verts.

Deux proprietes verifiees, dans cet ordre :

  1. FIDELITE — le contenu commite est exactement ce que
     `build_memento.py` (sans argument, donc les 88 SSP depuis l'ouverture du
     lot 2) produit aujourd'hui. C'est la propriete qui attrape le « modifie
     sans regenerer ».
  2. IDEMPOTENCE — deux executions consecutives donnent des fichiers
     identiques.

PAS D'EMPREINTE FIGEE ici, contrairement a check_fusion.py, et c'est
delibere : le memento officiel ne doit JAMAIS changer, alors que ceux-ci ont
vocation a evoluer (le management arrive, le vocabulaire canonique se remplit).
Une constante a mettre a jour a chaque evolution legitime ne garderait rien —
elle serait mise a jour par reflexe. La fidelite au generateur, elle, reste
vraie quoi qu'il arrive au contenu.
"""
import hashlib
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento                                     # noqa: E402

REPO = Path(__file__).resolve().parents[2]


def empreintes():
    """chemin relatif -> md5, pour les seuls mementos par SSP presents."""
    out = {}
    for f in sorted(build_memento.SORTIE.glob("*.md")):
        texte = f.read_text(encoding="utf8")
        if build_memento._TYPE_DECLARE.search(texte):
            out[f.name] = hashlib.md5(f.read_bytes()).hexdigest()
    return out


def generer():
    r = subprocess.run([sys.executable, str(Path(__file__).parent / "build_memento.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("ECHEC — le generateur s'est arrete :")
        print(r.stdout or r.stderr)
        sys.exit(1)


def compare(avant, apres, quoi):
    ecarts = []
    for nom in sorted(set(avant) - set(apres)):
        ecarts.append(f"{quoi} : « {nom} » n'est plus produit")
    for nom in sorted(set(apres) - set(avant)):
        ecarts.append(f"{quoi} : « {nom} » est produit mais absent du dépôt")
    for nom in sorted(set(avant) & set(apres)):
        if avant[nom] != apres[nom]:
            ecarts.append(f"{quoi} : « {nom} » diffère")
    return ecarts


def main():
    avant = empreintes()
    if not avant:
        print("ECHEC — aucun mémento par SSP dans docs/obsidian-memento/ ;\n"
              "  lancer python3 scripts/memento/build_memento.py")
        return 1

    generer()
    apres = empreintes()
    ecarts = compare(avant, apres, "contenu commité obsolète")

    generer()
    encore = empreintes()
    ecarts += compare(apres, encore, "générateur non idempotent")

    if ecarts:
        print(f"ECHEC — {len(ecarts)} écart(s) :")
        for e in ecarts[:40]:
            print("  ", e)
        if len(ecarts) > 40:
            print(f"   … et {len(ecarts) - 40} autre(s)")
        print("\n  Régénérer : python3 scripts/memento/build_memento.py")
        return 1
    print(f"OK — {len(apres)} mémentos par SSP fidèles au générateur, "
          "génération idempotente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
