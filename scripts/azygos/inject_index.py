"""Insère le corpus azygos dans index.html (onglet, styles, cartes).

Idempotent : relancer le script remplace le bloc existant au lieu de le
dupliquer. Repère les points d'insertion sur les entrées « casecos », dernier
corpus déclaré avant celui-ci.

    python3 scripts/azygos/inject_index.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_azygos as lib  # noqa: E402

INDEX = lib.RACINE / "index.html"

# Violet : seule teinte encore libre parmi les six corpus existants.
COULEUR = "#7c3aed"
FOND_CLAIR = "#ede9fe"
TEXTE = "#6d28d9"

# Les spécialités Azygos vers la nomenclature `data-system` de la page.
SYSTEMES = {
    "Médecine interne": "Médecine générale",
    "Chirurgie": "Gastro-entérologie",
    "Neurologie": "Neurologie",
    "Pédiatrie": "Pédiatrie",
    "Gynécologie & obstétrique": "Gynécologie",
    "ORL": "ORL",
    "Ophtalmologie": "Ophtalmologie",
    "Dermatologie": "Dermatologie",
    "Psychiatrie": "Psychiatrie",
    "Orthopédie": "Rhumatologie",
}

DEBUT = "<!-- azygos:début -->"
FIN = "<!-- azygos:fin -->"


def styles() -> str:
    return f"""      {DEBUT}
      .tab[data-cat="azygos"].active {{
        background: {COULEUR};
      }}
      .section-header .badge.azygos {{
        background: {FOND_CLAIR};
        color: {TEXTE};
      }}
      .azygos .num {{
        background: {FOND_CLAIR};
        color: {TEXTE};
      }}
      .azygos .cat-tag {{
        background: {FOND_CLAIR};
        color: {TEXTE};
      }}
      .cat-bar-fill.azygos {{
        background: {COULEUR};
      }}
      {FIN}
"""


def onglet() -> str:
    return f"""          {DEBUT}
          <button
            class="tab"
            data-cat="azygos"
            role="tab"
            aria-selected="false"
          >
            Azygos
          </button>
          {FIN}
"""


def cartes(cas: list[dict]) -> str:
    lignes = [f"      {DEBUT}", '      <div class="section" data-section="azygos">',
              '        <div class="section-header">',
              '          <span class="badge azygos">AZYGOS</span>',
              f"          <h2>Cas 1–{len(cas)}</h2>",
              '          <span class="count"></span>', "        </div>",
              '        <div class="grid">']
    for n, c in enumerate(cas, start=1):
        fichier = lib.nom_fichier(f"AZYGOS-{n}", c["titre"], c.get("patient", ""))
        systeme = SYSTEMES.get(c["specialite"], "Médecine générale")
        lignes += [
            "          <a",
            '            class="card azygos"',
            f'            data-system="{lib.echappe(systeme)}"',
            f'            href="cases/azygos/{fichier}"',
            f'            ><span class="num">{n}</span>',
            '            <div class="info">',
            f'              <div class="title">{lib.echappe(c["titre"])}</div>',
            f'              <div class="sub">{lib.echappe(c.get("patient", ""))}</div>',
            "            </div>",
            '            <span class="cat-tag">AZY</span></a',
            "          >",
        ]
    lignes += ["        </div>", "      </div>", f"      {FIN}"]
    return "\n".join(lignes) + "\n"


def insere(texte: str, bloc: str, ancre: str) -> str:
    """Remplace un bloc azygos existant, sinon l'insère après l'ancre."""
    motif = re.compile(re.escape(DEBUT) + r".*?" + re.escape(FIN) + r"\n", re.S)
    if motif.search(texte):
        # Un seul bloc à la fois : on ne remplace que celui qui suit l'ancre.
        debut = texte.index(ancre) + len(ancre)
        suite = motif.sub(bloc.lstrip(" "), texte[debut:], count=1)
        return texte[:debut] + suite
    return texte.replace(ancre, ancre + bloc, 1)


def main() -> None:
    inventaire = json.loads(
        (Path(__file__).parent / "inventaire.json").read_text(encoding="utf-8")
    )
    texte = INDEX.read_text(encoding="utf-8")
    avant = len(texte)

    # Purge d'une injection précédente pour rester idempotent.
    # On retire les lignes entières (indentation comprise) pour que deux
    # exécutions successives produisent un fichier identique à l'octet près.
    texte = re.sub(
        r"[ \t]*" + re.escape(DEBUT) + r".*?" + re.escape(FIN) + r"\n",
        "",
        texte,
        flags=re.S,
    )

    texte = texte.replace(
        '      .tab[data-cat="casecos"].active {\n        background: #0d9488;\n      }\n',
        '      .tab[data-cat="casecos"].active {\n        background: #0d9488;\n      }\n'
        + styles(),
        1,
    )
    texte = texte.replace(
        '          <button\n            class="tab"\n            data-cat="casecos"\n',
        onglet() + '          <button\n            class="tab"\n            data-cat="casecos"\n',
        1,
    )
    texte = texte.replace(
        '      <div class="no-results" id="noResults">',
        cartes(inventaire["cas"]) + '      <div class="no-results" id="noResults">',
        1,
    )

    # Le corpus doit aussi être connu du JavaScript : sans cela les cartes
    # existent dans le DOM mais aucun filtre ni compteur ne les voit. Ces
    # ajouts-là ne peuvent pas porter de marqueur HTML (on est dans du code),
    # d'où la garde explicite qui préserve l'idempotence.
    for ancre, ajout in [
        (
            '          if (card.classList.contains("casecos")) return "casecos";\n',
            '          if (card.classList.contains("azygos")) return "azygos";\n',
        ),
        ('            "casecos",\n', '            "azygos",\n'),
        ('            casecos: "CasECOS",\n', '            azygos: "Azygos",\n'),
    ]:
        if ajout not in texte:
            texte = texte.replace(ancre, ancre + ajout, 1)

    INDEX.write_text(texte, encoding="utf-8")
    print(f"index.html : {avant} → {len(texte)} octets")
    for cle in ('data-cat="azygos"', 'data-section="azygos"', 'class="card azygos"'):
        print(f"  {texte.count(cle):>3} × {cle}")


if __name__ == "__main__":
    main()
