"""Identifiant() propre sur les quatre corpus. Sortie 1 si ecart."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction

REPO = Path(__file__).resolve().parents[2]
CORPUS = ["amboss", "german", "rescos", "azygos"]
LONGUEUR_MAX = 12


def suspect(ident):
    """Un underscore, un espace ou une longueur excessive trahit un
    identifiant qui a recupere le tronc du nom de fichier au lieu du
    prefixe de corpus."""
    return "_" in ident or " " in ident or len(ident) > LONGUEUR_MAX


def main():
    ecarts, total = [], 0
    for corpus in CORPUS:
        dossier = REPO / "cases" / corpus
        if not dossier.is_dir():
            continue
        for fichier in sorted(dossier.glob("*.html")):
            total += 1
            ident = lib_extraction.identifiant(fichier)
            if suspect(ident):
                ecarts.append(f"{fichier.relative_to(REPO)} -> {ident!r}")

    print(f"{total} grille(s) vérifiée(s) sur {len(CORPUS)} corpus")
    if ecarts:
        print("ÉCHEC —", len(ecarts), "identifiant(s) suspect(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — tous les identifiants sont propres")
    return 0


if __name__ == "__main__":
    sys.exit(main())
