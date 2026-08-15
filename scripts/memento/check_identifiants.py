"""Identifiant() propre ET unique sur les quatre corpus. Sortie 1 si ecart."""
import sys
from collections import defaultdict
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
    # Un identifiant designe UN cas : toute la chaine aval l'utilise comme cle
    # (rattachement SSP, table des diagnostics, ensemble des cas qui portent un
    # item). Deux fichiers pour un meme identifiant fondent silencieusement
    # deux grilles en une — c'est ce qui arrivait aux deux moities de la
    # station double RESCOS-64. Ce checker doit donc echouer sur un doublon,
    # pas seulement sur un identifiant mal forme.
    fichiers_par_ident = defaultdict(list)
    for corpus in CORPUS:
        dossier = REPO / "cases" / corpus
        if not dossier.is_dir():
            continue
        for fichier in sorted(dossier.glob("*.html")):
            total += 1
            ident = lib_extraction.identifiant(fichier)
            fichiers_par_ident[ident].append(fichier.relative_to(REPO))
            if suspect(ident):
                ecarts.append(f"{fichier.relative_to(REPO)} -> {ident!r}")

    doublons = {i: f for i, f in sorted(fichiers_par_ident.items()) if len(f) > 1}

    print(f"{total} grille(s) vérifiée(s) sur {len(CORPUS)} corpus — "
          f"{len(fichiers_par_ident)} identifiant(s) distinct(s)")
    if ecarts:
        print("ÉCHEC —", len(ecarts), "identifiant(s) suspect(s) :")
        for e in ecarts:
            print("  ", e)
    if doublons:
        print("ÉCHEC —", len(doublons), "identifiant(s) porté(s) par plusieurs fichiers :")
        for ident, fichiers in doublons.items():
            print(f"   {ident} :")
            for f in fichiers:
                print(f"      {f}")
    if ecarts or doublons:
        return 1
    print("OK — tous les identifiants sont propres et uniques")
    return 0


if __name__ == "__main__":
    sys.exit(main())
