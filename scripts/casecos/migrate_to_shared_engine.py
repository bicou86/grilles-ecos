"""Bascule les grilles CasECOS de leur moteur embarque vers `cases/scoring.js`.

Usage :
    python3 scripts/casecos/migrate_to_shared_engine.py --dry-run [FILTRE]
    python3 scripts/casecos/migrate_to_shared_engine.py --apply   [FILTRE]

CE QUE FAIT LA BASCULE
----------------------
Chaque grille portait QUATRE blocs `<script>`, dans cet ordre invariable
(mesure : 198/198 la meme signature) :

  1. `<script src="../theme-sync.js">`          — inchange
  2. le MOTEUR embarque, ~726 lignes                    — remplace
  3. un rappel de `colorPatientResponses()`             — supprime
  4. la barre de navigation entre cas, IIFE             — supprimee

Le bloc 2 devient un `window.caseConfig` au format des trois autres corpus,
suivi de `<script src="../scoring.js">`. Le bloc 3 est la QUEUE EXACTE de
`cases/scoring.js` (les cinq memes lignes, au caractere pres) : le conserver le
ferait jouer deux fois. Le bloc 4 est le substitut local de `createNavBar()`,
que `cases/scoring.js` appelle desormais : le conserver afficherait DEUX barres
de navigation superposees. Le `<style>` de `.case-nav-bar` qui le precede est
CONSERVE — les grilles CasECOS ne chargent pas `cases/case-styles.css` (elles
portent tout leur CSS en ligne), il est donc leur seule source de mise en forme
pour la barre que `createNavBar()` construit.

Enfin `<script src="../persistence.js">` est ajoute avant `</body>`, comme dans
les 253 autres grilles du depot qui chargent `scoring.js`.

`srs.js` n'est ajoute nulle part, et c'est l'alignement sur les autres corpus :
AUCUNE grille du depot ne le charge par une balise (0/40 AMBOSS, 0/88 German,
0/41 RESCOS). C'est `cases/scoring.js` qui l'injecte lui-meme, par un
`document.createElement('script')` en tete de fichier.

LE PIEGE DE LA CONFIGURATION
----------------------------
Le litteral a convertir est PRECEDE d'une declaration vide (`let maxScores = {};`)
qu'un motif naif capture a sa place. Ce script ne cherche donc pas `maxScores`
mais la ligne-repere `// Configuration pour le format traditionnel`, et prend le
bloc CONTIGU qui la suit. Le resultat est verifie : les valeurs relues du fichier
ecrit doivent etre identiques a celles lues avant l'ecriture.

`scores = {anamnese: 0, examen: 0, management: 0, communication: 0}` n'est PAS
reporte dans `caseConfig` : `cases/scoring.js` porte ce meme litteral en dur
(ligne 110) et il est inerte — la boucle affecte `scores[section.key] = ...`
pour chaque section avant toute lecture. Le script verifie tout de meme que la
grille porte bien ce litteral-la et refuse de convertir sinon.

TOUT EST VERIFIE AVANT ECRITURE, RIEN N'EST SUPPOSE
---------------------------------------------------
Chaque grille doit satisfaire les huit assertions de `convert()`. Une seule qui
tombe et la grille est laissee INTACTE, avec son motif d'echec. Le script est
idempotent : une grille deja basculee est comptee « deja convertie » et sautee.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_casecos as lib

SCRIPT_OPEN = re.compile(r"<script(\s[^>]*)?>")

CFG_HEAD = "            // Configuration pour le format traditionnel\n"
CFG_END = "\n            ];\n"

# Litteral inerte, porte en dur par `cases/scoring.js` (ligne 110).
SCORES_LITERAL = "{anamnese: 0, examen: 0, management: 0, communication: 0}"

# Queue de `cases/scoring.js`, recopiee dans le 3e bloc `<script>` des grilles.
BLOCK3 = """    <script>
        // Appel final pour s'assurer que tout est coloré
        // Forcer la coloration finale
        if (window.colorPatientResponses) {
            window.colorPatientResponses();
        }
    </script>
"""

SCORING_TAG = '<script src="../scoring.js"></script>'
PERSISTENCE_TAG = '<script src="../persistence.js"></script>'


class Refus(Exception):
    """Une assertion de conversion est tombee : la grille reste intacte."""


def script_blocks(html):
    """(debut_balise, debut_corps, fin_corps, fin_balise, attributs) par `<script>`."""
    out = []
    for m in SCRIPT_OPEN.finditer(html):
        close = html.find("</script>", m.end())
        if close < 0:
            raise Refus("<script> non ferme")
        out.append((m.start(), m.end(), close, close + len("</script>"),
                    (m.group(1) or "").strip()))
    return out


def read_config(engine):
    """(debut, fin, maxScores, coef, sectionInfo) — textes VERBATIM du litteral.

    Cherche la ligne-repere plutot que `maxScores`, pour ne pas tomber sur la
    declaration vide qui la precede (voir l'entete).
    """
    i = engine.find(CFG_HEAD)
    if i < 0:
        raise Refus("ligne-repere de configuration absente")
    j = engine.find(CFG_END, i)
    if j < 0:
        raise Refus("fin de sectionInfo introuvable")
    j += len(CFG_END)
    body = engine[i:j]

    def one(name, opener, closer):
        m = re.search(r"\n\s*" + name + r" = (" + re.escape(opener) + r".*?"
                      + re.escape(closer) + r");\n", body, re.S)
        if not m:
            raise Refus(f"litteral {name} illisible")
        return m.group(1)

    scores = one("scores", "{", "}")
    if scores != SCORES_LITERAL:
        raise Refus(f"litteral scores inattendu : {scores!r}")
    return i, j, one("maxScores", "{", "}"), one("coef", "{", "}"), \
        one("sectionInfo", "[", "]")


def config_script(max_scores, coef, section_info):
    """Bloc `window.caseConfig`, au format exact des corpus AMBOSS / RESCOS.

    Sans indentation d'ouverture : le texte qui precede la balise remplacee la
    porte deja (`    <script>`), et l'ajouter la doublerait.
    """
    return ("<script>\n"
            "window.caseConfig = {\n"
            f"    maxScores: {max_scores},\n"
            f"    coef: {coef},\n"
            f"    sectionInfo: {section_info}\n"
            "};\n"
            "</script>\n")


def convert(html):
    """Rend le HTML basculé, ou leve `Refus`. `None` si deja converti."""
    if SCORING_TAG in html:
        return None

    blocks = script_blocks(html)
    if len(blocks) != 4:
        raise Refus(f"{len(blocks)} blocs <script>, 4 attendus")
    if 'src="../theme-sync.js"' not in blocks[0][4]:
        raise Refus("le 1er bloc n'est pas theme-sync.js")
    if any("src=" in b[4] for b in blocks[1:]):
        raise Refus("un des blocs 2-4 porte un src=")

    engine = html[blocks[1][1]:blocks[1][2]]
    if "function calculateScores()" not in engine:
        raise Refus("le 2e bloc ne porte pas calculateScores()")
    if any("function calculateScores()" in html[b[1]:b[2]] for b in blocks[2:]):
        raise Refus("un autre bloc porte aussi calculateScores()")

    _, _, max_scores, coef, section_info = read_config(engine)

    # 1. le moteur -> caseConfig + scoring.js
    out = (html[:blocks[1][0]]
           + config_script(max_scores, coef, section_info)
           + SCORING_TAG
           + html[blocks[1][3]:])

    # 2. le rappel de coloration (queue de scoring.js) -> supprime
    if out.count(BLOCK3) != 1:
        raise Refus("bloc de rappel de coloration introuvable ou multiple")
    out = out.replace(BLOCK3, "")

    # 3. la barre de navigation locale -> supprimee (createNavBar la construit)
    nav = re.search(r"<script>\n\(function\(\) \{\n  var caseIndex.*?\}\)\(\);\n"
                    r"</script>\n", out, re.S)
    if not nav:
        raise Refus("bloc de barre de navigation introuvable")
    if "ecos_case_index" not in nav.group(0):
        raise Refus("le bloc capture n'est pas la barre de navigation")
    out = out[:nav.start()] + out[nav.end():]

    # 4. persistence.js avant </body>
    if out.count("</body>") != 1:
        raise Refus(f"{out.count('</body>')} balises </body>, 1 attendue")
    out = out.replace("</body>", PERSISTENCE_TAG + "\n</body>")

    # Controle de sortie : plus aucun moteur embarque, les trois balises voulues.
    if "function calculateScores()" in out:
        raise Refus("un moteur embarque subsiste apres conversion")
    for tag in (SCORING_TAG, PERSISTENCE_TAG, "window.caseConfig"):
        if out.count(tag) != 1:
            raise Refus(f"{tag} present {out.count(tag)} fois, 1 attendu")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="ecrit les fichiers")
    ap.add_argument("--dry-run", action="store_true", help="n'ecrit rien")
    ap.add_argument("filtre", nargs="?", default=None)
    args = ap.parse_args()
    if args.apply == args.dry_run:
        print("Choisir --apply OU --dry-run.")
        return 2

    done = skipped = 0
    refus = []
    for path in lib.grids():
        if not lib.matches(path, args.filtre):
            continue
        html = path.read_text(encoding="utf-8")
        try:
            out = convert(html)
        except Refus as e:
            refus.append((path.name, str(e)))
            continue
        if out is None:
            skipped += 1
            continue
        if args.apply:
            path.write_text(out, encoding="utf-8")
        done += 1

    print(f"{'converties' if args.apply else 'convertibles'} : {done}")
    if skipped:
        print(f"deja converties : {skipped}")
    if refus:
        print(f"REFUS : {len(refus)}")
        for n, e in refus:
            print(f"  {n}\n    {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
