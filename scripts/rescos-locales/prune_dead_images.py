"""Retire les references d'image MORTES du corpus `cases/rescos-locales`.

CE QUE SONT CES REFERENCES
===========================
92 balises `<img>` sur 35 grilles pointent un fichier qui n'existe pas :

  * **75** un chemin ABSOLU du poste de l'auteur
    (`/Users/…/Documents/-Medecine/-EXAMEN_FEDERAL/…/html/images/…`) ;
  * **17** un chemin relatif sans racine dans le depot — `bbn/…` (9) et
    `decision-partagee/…` (8).

Elles sont invisibles au `grep` (rien ne distingue un chemin mort d'un chemin
vivant) et se detectent au **404**, dans `browser_probe.js`. Les 11 autres
images du corpus sont en base64 : elles vivent dans le fichier et ne sont PAS
concernees.

AUCUNE NE PEUT ETRE RE-POINTEE
===============================
Le depot compte 45 fichiers image. Confrontation des 92 noms de base contre ces
45, par egalite exacte, puis par egalite apres normalisation (accents, casse,
ponctuation), puis par ressemblance : **0 correspondance**. La meilleure
ressemblance de nom est de 0,62 et porte sur deux sujets differents
(« algorithme paracetamol » contre `neuro-algorithme-horton.png`). Aucun
repertoire `bbn/`, `decision-partagee/` ni `images/` n'existe dans le depot.

CE QUE LE SCRIPT RETIRE, ET CE QU'IL GARDE
===========================================
Les 92 balises sont TOUTES dans la meme structure, verifiee une par une :

    <div class="annexe-item">
        <div class="annexe-title">Radiographie du thorax</div>
        <div class="annexe-description">Radiographie thoracique montrant des
            contusions pulmonaires bilaterales et un pneumothorax gauche</div>
        <div class="annexe-image">
            <img src="…" alt="…" />
        </div>
    </div>

92 sur 92 : un `annexe-item` nu, **un** `annexe-title`, **une**
`annexe-description`, **une** `<img>`. La legende porte donc l'information
seule — elle nomme l'examen et enonce ce qu'il montre. Le script retire le seul
`<div class="annexe-image">` et laisse l'`annexe-item`, son titre et sa
description INTACTS. Aucun item de contenu ne disparait
(`check_no_loss.py` : 0), et le nombre de segments du bloc `annexe-image` —
compte des `annexe-item` nus — ne bouge pas.

Le geste retire une icone brisee, pas du contenu. Il ne FABRIQUE rien : aucune
image n'est inventee, aucune legende n'est reecrite.

Idempotent. Ne touche jamais une `<img>` en base64.

Usage :
    python3 scripts/rescos-locales/prune_dead_images.py --check
    python3 scripts/rescos-locales/prune_dead_images.py
    python3 scripts/rescos-locales/prune_dead_images.py --list   # inventaire TSV
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib

ROOT = Path(__file__).resolve().parents[2]

# Le `<div class="annexe-image">` et son unique `<img>`, avec l'espacement qui
# le precede — le remplacement rend la seule fin de ligne, ce qui recolle la
# description a la fermeture de l'`annexe-item`.
WRAPPER = re.compile(
    r'\s*<div class="annexe-image">\s*<img\b[^>]*>\s*</div>(\s*)', re.S)

IMG_SRC = re.compile(r'<img\b[^>]*\bsrc="([^"]*)"')


def dead_refs(html):
    """[(src, debut, fin), ...] des `<img>` dont le fichier n'existe pas.

    Une `data:` URI n'est pas une reference : l'image est dans le fichier.
    Un chemin est resolu relativement a `cases/rescos-locales/` pour les
    chemins relatifs, et tel quel pour les chemins absolus.
    """
    out = []
    for m in IMG_SRC.finditer(html):
        src = m.group(1)
        if src.startswith("data:"):
            continue
        target = Path(src) if src.startswith("/") else lib.CASES / src
        if not target.exists():
            out.append((src, m.start(), m.end()))
    return out


def transform(html):
    """(nouveau HTML, [src retires])."""
    removed = []
    while True:
        dead = {start for _, start, _ in dead_refs(html)}
        if not dead:
            return html, removed
        for w in WRAPPER.finditer(html):
            inner = IMG_SRC.search(w.group(0))
            if not inner or (w.start() + inner.start()) not in dead:
                continue
            removed.append(inner.group(1))
            html = html[:w.start()] + w.group(1) + html[w.end():]
            break
        else:                       # une `<img>` morte hors de la structure
            for src, _, _ in dead_refs(html):
                if src not in removed:
                    raise ValueError(f"<img> morte hors de annexe-image : {src}")
            return html, removed


def main():
    check = "--check" in sys.argv
    if "--list" in sys.argv:
        print("grille\tsrc")
        for path in lib.grids():
            for src, _, _ in dead_refs(path.read_text(encoding="utf-8")):
                print(f"{path.name}\t{src}")
        return 0

    grids = total = 0
    for path in lib.grids():
        html = path.read_text(encoding="utf-8")
        new, removed = transform(html)
        if not removed:
            continue
        grids += 1
        total += len(removed)
        if not check:
            path.write_text(new, encoding="utf-8")
        print(f"{path.name} — {len(removed)} reference(s) morte(s)")
        for src in removed:
            print(f"    {src}")
    verb = "a retirer" if check else "retirees"
    print(f"\n{total} reference(s) morte(s) {verb} sur {grids} grille(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
