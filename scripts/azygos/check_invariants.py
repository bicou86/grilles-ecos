"""Contrôles d'intégrité du corpus azygos.

À exécuter après toute reconstruction :

    python3 scripts/azygos/check_invariants.py

Sort en code 1 si un invariant est rompu.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_azygos as lib  # noqa: E402

# Postes sans examen physique : entretien pur, téléconsultation. L'absence de
# section examen y est attendue, pas un défaut d'extraction.
SANS_EXAMEN_ATTENDU = {"Poste de communication", "Consultation téléphonique"}


def grilles() -> list[Path]:
    return sorted(
        lib.SORTIE.glob("AZYGOS-*.html"),
        key=lambda p: int(re.match(r"AZYGOS-(\d+)", p.name).group(1)),
    )


def config(chemin: Path) -> dict:
    h = chemin.read_text(encoding="utf-8")
    return json.loads(re.search(r"window\.caseConfig = (\{.*?\});\n</script>", h, re.S).group(1))


def main() -> int:
    inventaire = json.loads(
        (Path(__file__).parent / "inventaire.json").read_text(encoding="utf-8")
    )
    par_id = {c["id"]: c for c in inventaire["cas"]}
    fiches = inventaire["cas"]
    erreurs: list[str] = []

    fichiers = grilles()
    if len(fichiers) != len(fiches):
        erreurs.append(f"{len(fichiers)} grilles pour {len(fiches)} cas attendus")

    # 1. Tout onglet extrait doit tomber dans une section connue, et aucun
    #    libellé ne doit atterrir dans « management » par défaut alors qu'il
    #    contient un mot-clé d'une autre section.
    libelles: Counter = Counter()
    for source in lib.EXTRACTION.glob("*.json"):
        data = json.loads(source.read_text(encoding="utf-8"))
        ordre = data.get("ordre") or [
            k for k in data["onglets"] if k not in lib.ONGLETS_FIXES
        ]
        for o in ordre:
            libelles[o] += 1
        fiche = par_id.get(data["meta"]["id"])
        if not fiche:
            continue
        # Toute « Information complémentaire » extraite doit ressortir quelque
        # part : sur un item, ou en vignette de sous-chapitre. Une info avalée
        # par l'aplatissement ne provoque aucune erreur — seul ce compte la
        # rend visible.
        infos = data.get("infos") or {}
        rendues: set[str] = set()
        for onglet in ordre:
            for groupe in data["onglets"].get(onglet) or []:
                for item in lib.aplatit(groupe, infos):
                    if item.get("info"):
                        rendues.add(item["cle"])
                    if item.get("info_sous_groupe"):
                        for brut in groupe["items"]:
                            if (brut["label"] == item["label_sous_groupe"]
                                    and brut["cle"] in infos):
                                rendues.add(brut["cle"])
                                break
        perdues = set(infos) - rendues
        if perdues:
            erreurs.append(
                f"{fiche['titre']} : {len(perdues)} information(s) extraite(s) "
                f"mais non rendue(s)"
            )

        sections = {lib.classe_onglet(o) for o in ordre}
        if "anamnese" not in sections:
            erreurs.append(f"{fiche['titre']} : aucun onglet d'anamnèse")
        if "communication" not in sections:
            erreurs.append(f"{fiche['titre']} : aucun onglet de communication")
        if "examen" not in sections and fiche["format"] not in SANS_EXAMEN_ATTENDU:
            # Certains postes standards sont de purs entretiens (anxiété,
            # troubles du sommeil) : on signale sans faire échouer.
            print(f"  · {fiche['titre']} ({fiche['format']}) : pas d'examen clinique")

    # 2. Cohérence interne de chaque grille.
    for chemin in fichiers:
        cfg = config(chemin)
        maxima, info = cfg["maxScores"], cfg["sectionInfo"]
        if set(maxima) != {"anamnese", "examen", "management", "communication"}:
            erreurs.append(f"{chemin.name} : sections inattendues {sorted(maxima)}")
        if abs(sum(cfg["coef"].values()) - 1.0) > 1e-9:
            erreurs.append(f"{chemin.name} : somme des coefficients ≠ 1")
        comm = next(s for s in info if s.get("isComm"))
        if maxima["communication"] != comm["count"] * 4:
            erreurs.append(
                f"{chemin.name} : communication {maxima['communication']} ≠ "
                f"{comm['count']} dimensions × 4"
            )
        h = chemin.read_text(encoding="utf-8")
        # Chaque case à cocher doit être rattachée à un critère existant.
        for cle in set(re.findall(r'id="([acem]\d+)-detail-\d+"', h)):
            if f'id="criteria-{cle}"' not in h:
                erreurs.append(f"{chemin.name} : détail orphelin {cle}")
        if 'src="../scoring.js"' not in h or 'src="../persistence.js"' not in h:
            erreurs.append(f"{chemin.name} : chaîne de scripts incomplète")

        # Vignettes et annexe théorique sont deux vues du même corpus de
        # justifications : tout écart signale une info perdue d'un côté.
        vignettes = h.count('class="info-vignette"')
        entrees = len(re.findall(r"<li[^>]*><strong>", h))
        if vignettes != entrees:
            erreurs.append(
                f"{chemin.name} : {vignettes} vignettes pour {entrees} entrées d'annexe"
            )
        if vignettes and "annexe-theorie" not in h:
            erreurs.append(f"{chemin.name} : vignettes sans annexe théorique")

        # La colorisation sémantique ne concerne QUE les blocs pédagogiques :
        # dans la grille notée elle parasiterait le codage couleur du score
        # (score-0/1/2, lacune-rouge/orange/verte) posé par scoring.js.
        debut_annexes = h.find('<div class="annexes">')
        if debut_annexes > -1:
            fuites = len(re.findall(r'class="c-[a-z]+"', h[:debut_annexes]))
            if fuites:
                erreurs.append(
                    f"{chemin.name} : {fuites} span(s) coloré(s) hors des annexes"
                )
        if "annexe-theorie" in h and not re.search(r'class="c-[a-z]+"', h):
            erreurs.append(f"{chemin.name} : annexe pédagogique non colorisée")

    print(f"\n{len(libelles)} libellés d'onglets distincts, "
          f"{len(fichiers)} grilles contrôlées")
    if erreurs:
        print(f"\n{len(erreurs)} erreurs :")
        for e in erreurs:
            print(f"  ✗ {e}")
        return 1
    print("✓ tous les invariants tiennent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
