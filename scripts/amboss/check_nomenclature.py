"""Detecte les termes non suisses. Sortie 1 si presents."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

# Termes bannis et leur remplacement attendu.
# CBC et BMP : exclus uniquement quand ils servent de cle de glossaire
# (« CBC : ... », « BMP : ... »), immediatement suivis de « : ». Ce cas
# traduit les abreviations d'un schema anglophone dont l'image (base64)
# n'est pas modifiee : l'abreviation d'origine doit rester lisible en cle
# pour que le lecteur puisse relier la legende au schema (ex. AMBOSS-33,
# « BMP : chimie sanguine (panel metabolique de base) »). Le lookahead ne
# joue que dans ce cas precis ; un CBC ou BMP employe ailleurs comme terme
# medical (hors position de cle de glossaire) reste detecte normalement.
BANNED = {
    r"\bNFS\b": "FSC",
    r"\bCBC\b(?! : )": "FSC",
    r"\bBMP\b(?! : )": "chimie sanguine",
    r"\bVicodin\b": "Tramadol (Tramal®)",
    r"\bTylenol\b": "Paracetamol (Dafalgan®)",
    r"\bTums\b": "Antiacides (Rennie®)",
    r"\bmg/dL\b": "unites SI",
    # g/dL : hemoglobine (et proteines) — les laboratoires suisses rendent en g/L,
    # facteur x10 (Hb 11.2 g/dL -> 112 g/L). Le vault ecrit uniformement g/L
    # (« Hb < 70 g/L », « Hb F < 120 / H < 130 g/L »). Le motif ne peut pas
    # attraper mg/dL ni ng/dL : dans « mg/dL » comme dans « ng/dL » il n'y a pas
    # de frontiere de mot entre la lettre de prefixe et le « g ».
    r"\bg/dL\b": "g/L (x10)",
    # ng/mL : pas de facteur unique, l'analyte decide —
    #   troponine T   -> ng/L  (x1000 ; 0.08 ng/mL = 80 ng/L)
    #   D-dimeres     -> µg/L  (x1 ; 1 ng/mL = 1 µg/L, preserve le seuil 500 et
    #                    la regle age-ajustee « age x 10 », definie en µg/L)
    #   ferritine     -> µg/L  (x1)
    # Ne peut pas attraper pg/mL ni U/mL : « ng/mL » n'y est pas sous-chaine.
    r"\bng/mL\b": "ng/L ou µg/L selon l'analyte",
    # pg/mL : pas de facteur unique non plus —
    #   vitamine B12 -> pmol/L (x0,738 ; 320 pg/mL = 236 pmol/L)
    #   BNP / NT-proBNP -> ng/L (x1 ; 1 pg/mL = 1 ng/L), comme le vault
    # Ne peut pas attraper ng/mL ni mg/mL : « pg/mL » n'y est pas sous-chaine.
    r"\bpg/mL\b": "pmol/L ou ng/L selon l'analyte",
    # /mm³ : numerations (leucocytes, plaquettes) -> G/L, x0,001.
    # La barre oblique est indispensable au motif : elle borne le sens « par
    # mm³ » (une concentration) et laisse passer un volume ecrit « 5 mm³ ».
    # Sans risque de faux positif base64 : « ³ » n'appartient pas a l'alphabet
    # base64, ce motif ne peut pas tomber dans un blob d'image.
    r"/mm³": "G/L (x0,001)",
    r"\b911\b": "144",
    r"\bSAMU\b": "144",
}

# EXCEPTION — NE JAMAIS BANNIR « mg/mL ».
# Deux occurrences dans AMBOSS-18 : « PC20 = 4 mg/mL » et « PC20 < 8 mg/mL ».
# C'est la concentration de methacholine inhalee lors du test de provocation
# bronchique, dont mg/mL est l'unite internationale correcte — ce n'est pas une
# valeur de laboratoire rendue par un automate, il n'y a donc rien a convertir
# en SI. Une passe future qui ajouterait r"\bmg/mL\b" a BANNED corromprait le
# seuil diagnostique de l'asthme. Meme raisonnement pour toute unite de dose ou
# de concentration administree (mg/kg, µg/bouffee, mg/mL) : la regle SI vise les
# resultats de laboratoire, pas les posologies.
# Pas de regle sur 112 : le corpus ne contient aucun numero d'urgence 112.
# La seule occurrence est « Score Global 0/112 » dans AMBOSS-8 — un total de
# bareme. La remplacer corromprait la grille.


def main():
    total = 0
    for path in lib.grids():
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        for pattern, repl in BANNED.items():
            hits = re.findall(pattern, html)
            if hits:
                total += len(hits)
                print(f"  {path.name}: {len(hits)}x {pattern} -> attendu {repl}")
    if total:
        print(f"\nECHEC — {total} terme(s) non suisse(s) restant(s)")
        return 1
    print("OK — aucun terme non suisse detecte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
