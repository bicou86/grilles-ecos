"""Bascule les 156 grilles notees de rescos-locales sur `cases/scoring.js`.

POURQUOI CETTE BASCULE, ET PAS UN REPORT DE CORRECTIONS
========================================================
Les 156 grilles notees embarquaient chacune leur copie du moteur de calcul —
une seule variante, empreinte SHA-256 `c3e2534e…` sur 156 — et cette variante
est la MEME FOURCHE PERIMEE de `cases/scoring.js` que celle de RESCOS-7 et
RESCOS-9, avec les MEMES SIX MANQUES :

  1. la garde `if (missingEl)` ;
  2. l'APPEL de `saveToRegistry()` ;
  3. la DEFINITION de `saveToRegistry()` ;
  4. le chargeur dynamique de `srs.js` ;
  5. la detection du mode circuit et le retour a `exam.html` ;
  6. `createNavBar()` / `createCircuitNav()`.

Le manque n° 1 se realisait a chaque calcul : le `<div id="missingItems">` que
le moteur adressait sans garde est COMMENTE dans les 156 grilles (verifie hors
commentaire HTML : 156/156). D'ou 13 446 `TypeError` en navigateur, et surtout
`ecos_registry` vide sur 0/165 — aucun score ne remontait au tableau de bord.

Le lot r7 a tranche pour la bascule sur RESCOS-7 et RESCOS-9 ; ce script
applique le meme arbitrage a l'echelle du corpus. Reporter six corrections dans
156 copies reconduirait le mecanisme de derive que ce defaut realise deja.

CE QUE LE SCRIPT FAIT, EXACTEMENT
==================================
Par grille notee, et rien d'autre :

  * il remplace le PREMIER des deux `<script>` en ligne — celui qui porte le
    moteur — par un `<script>` de configuration `window.caseConfig` suivi de
    `<script src="../scoring.js"></script>`. Le second `<script>` (l'appel
    final a `colorPatientResponses()`) est laisse INTACT : `cases/scoring.js`
    le porte aussi en fin de fichier, et RESCOS-7/9 le conservent de meme ;
  * il transpose le bareme SANS LE RECALCULER. Forme declarative (154
    grilles) : les trois membres droits `maxScores = …`, `coef = …`,
    `sectionInfo = …` sont repris VERBATIM. Forme imperative (2 grilles,
    RESCOS-63 et « RESCOS-64 station double 2 ») : reconstruite dans l'ordre
    des `sectionInfo.push({…})`, chaque champ recopie tel quel ;
  * il deplace `.timer-container` de `top: 20px` a `top: 70px` et ajoute les
    regles `.case-nav-bar` dans le `<style>` en ligne. C'est la CONTREPARTIE
    du manque n° 6 : `createNavBar()` insere desormais une barre en
    `position: fixed; top: 20px; left: 20px` — exactement la place qu'occupait
    le minuteur. Les deux gestes sont recopies de `cases/case-styles.css`
    (lignes 1209-1221 et 3630-3698), ou le projet a deja resolu la meme
    collision pour les trois autres corpus. Les quatre classes ajoutees sont
    verifiees ABSENTES des 156 feuilles de style en ligne : l'ajout ne peut
    rien ecraser.

CE QU'IL NE FAIT PAS
=====================
  * il ne touche AUCUN chiffre du bareme (`maxScores`, `coef`, `count`,
    `prefix`, `label`, `scoreId`, `isComm` sont recopies) — la correction du
    coefficient de RESCOS-63 est un geste SEPARE ;
  * il ne charge ni `case-styles.css`, ni `persistence.js`, ni
    `theme-sync.js` : aucun des six manques ne les concerne, et les 165
    feuilles de style en ligne restent la mise en page de ce corpus ;
  * il ne touche pas aux 9 feuilles porte — 0 critere, 0 `<input>`,
    0 `<script>` : elles n'ont pas de bareme, et c'est correct.

Idempotent : une grille deja basculee est laissee telle quelle.

Usage :
    python3 scripts/rescos-locales/apply_shared_engine.py --check   # sans ecrire
    python3 scripts/rescos-locales/apply_shared_engine.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib
from check_reachability import _CFG_END, _CFG_START, engine_source, is_door_sheet

SCRIPT_RE = re.compile(r"<script\b[^>]*>(.*?)</script>", re.S)

# Recopie de `cases/case-styles.css` lignes 3630-3698, a l'indentation des
# feuilles de style en ligne de ce corpus (8 espaces au premier niveau).
NAV_CSS = """
        /* === NAVIGATION BAR (createNavBar de ../scoring.js) === */
        .case-nav-bar {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1001;
            display: flex;
            align-items: center;
            gap: 0;
            background: white;
            border: 2px solid #2c5aa0;
            border-radius: 30px;
            padding: 4px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            font-family: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
        }
        .case-nav-bar a,
        .case-nav-bar span {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 6px 14px;
            border-radius: 24px;
            font-size: 0.78rem;
            font-weight: 600;
            text-decoration: none;
            color: #2c5aa0;
            transition: all 0.2s;
            white-space: nowrap;
        }
        .case-nav-bar a:hover { background: #dbeafe; }
        .case-nav-bar .nav-back { background: #2c5aa0; color: white; }
        .case-nav-bar .nav-back:hover { background: #1e40af; color: white; }
        .case-nav-bar .nav-position {
            font-size: 0.72rem;
            color: #64748b;
            padding: 6px 8px;
            cursor: default;
        }
        .case-nav-bar .nav-arrow { padding: 6px 10px; font-size: 0.95rem; }
        .case-nav-bar .nav-arrow.disabled { opacity: 0.3; pointer-events: none; }
        @media (max-width: 639px) {
            .case-nav-bar {
                top: auto;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                right: auto;
            }
        }
    """

NAV_MARK = "/* === NAVIGATION BAR (createNavBar de ../scoring.js) === */"
TIMER_RE = re.compile(r"(\.timer-container\s*\{[^}]*?top:\s*)20px(\s*;)")


def config_region(html):
    """Le texte de la region de configuration du moteur embarque."""
    js = engine_source(html)
    a = js.find(_CFG_START)
    b = js.find(_CFG_END, a) if a >= 0 else -1
    return js[a:b] if a >= 0 and b > 0 else ""


def build_case_config(html):
    """Le `<script>` de configuration, transpose du moteur embarque.

    Forme declarative : les trois membres droits sont repris VERBATIM, sans
    reformatage — ce qui rend la transposition verifiable au caractere pres.
    Forme imperative : reconstruite dans l'ordre des `push`, chaque champ
    recopie tel quel entre accolades.
    """
    cfg = config_region(html)
    if not cfg:
        raise ValueError("region de configuration introuvable")

    m_max = re.search(r"maxScores\s*=\s*(\{[^}]*\})\s*;", cfg)
    if m_max:                                       # forme declarative
        m_coef = re.search(r"coef\s*=\s*(\{[^}]*\})\s*;", cfg)
        m_sect = re.search(r"sectionInfo\s*=\s*(\[.*?\])\s*;", cfg, re.S)
        if not (m_coef and m_sect):
            raise ValueError("forme declarative incomplete")
        max_scores, coef, sections = m_max.group(1), m_coef.group(1), m_sect.group(1)
    else:                                           # forme imperative
        pairs = re.findall(r'maxScores\["(\w+)"\]\s*=\s*(\d+)\s*;', cfg)
        coefs = re.findall(r'coef\["(\w+)"\]\s*=\s*([\d.]+)\s*;', cfg)
        blobs = re.findall(r"sectionInfo\.push\((\{[^}]*\})\)\s*;", cfg)
        if not (pairs and coefs and blobs):
            raise ValueError("forme imperative incomplete")
        max_scores = "{" + ", ".join(f"{k}: {v}" for k, v in pairs) + "}"
        coef = "{" + ", ".join(f"{k}: {v}" for k, v in coefs) + "}"
        sections = ("[\n                "
                    + ",\n                ".join(blobs)
                    + "\n            ]")

    return ("<script>\nwindow.caseConfig = {\n"
            f"    maxScores: {max_scores},\n"
            f"    coef: {coef},\n"
            f"    sectionInfo: {sections}\n"
            "};\n</script>\n"
            '<script src="../scoring.js"></script>')


def transform(html):
    """(nouveau HTML, liste des gestes) — ou (html, []) si rien a faire."""
    steps = []
    scripts = list(SCRIPT_RE.finditer(html))
    if len(scripts) == 2 and "function calculateScores()" in scripts[0].group(1):
        replacement = build_case_config(html)
        html = html[:scripts[0].start()] + replacement + html[scripts[0].end():]
        steps.append("moteur embarque -> ../scoring.js + window.caseConfig")

    html, n = TIMER_RE.subn(r"\g<1>70px\g<2>", html)
    if n:
        steps.append(f".timer-container top 20px -> 70px ({n})")

    if NAV_MARK not in html:
        m = re.search(r"</style>", html)
        if m:
            html = html[:m.start()] + NAV_CSS + html[m.start():]
            steps.append("regles .case-nav-bar ajoutees")
    return html, steps


def main():
    check = "--check" in sys.argv
    touched = doors = skipped = 0
    for path in lib.grids():
        html = path.read_text(encoding="utf-8")
        if is_door_sheet(lib.strip_base64(html)):
            doors += 1
            continue
        new, steps = transform(html)
        if not steps:
            skipped += 1
            continue
        touched += 1
        if not check:
            path.write_text(new, encoding="utf-8")
        print(f"{path.name}\n    {' | '.join(steps)}")
    verb = "a transformer" if check else "transformees"
    print(f"\n{touched} grille(s) {verb}, {skipped} deja a jour, "
          f"{doors} feuille(s) porte laissee(s) intacte(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
