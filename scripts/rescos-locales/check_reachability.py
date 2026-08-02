"""Verifie que le bareme declare est ATTEIGNABLE par le calcul. Sortie 1 si ecart.

Usage :
    python3 scripts/rescos-locales/check_reachability.py [GRILLE_FILTRE]

Exemples :
    python3 scripts/rescos-locales/check_reachability.py           # les 165
    python3 scripts/rescos-locales/check_reachability.py RESCOS-63 # une grille


LA DECISION D'ARCHITECTURE : VERIFIER L'EQUIVALENCE, PUIS SIMULER UN SEUL MODELE
================================================================================
Les trois corpus precedents partageaient `cases/scoring.js`. La simulation
d'AMBOSS (`section_max`, `orphan_criteria`, `check_one`) rejoue CE fichier, et
le rejouer suffisait parce qu'il n'y en avait qu'un.

A l'inventaire (`l2`), AUCUNE grille ne chargeait `cases/scoring.js` (0/165) :
les 156 grilles notees embarquaient chacune leur propre copie du moteur. Deux
voies s'offraient :

  (a) simuler le moteur de CHAQUE grille — c'est-a-dire extraire et interpreter
      156 programmes JavaScript en Python ;
  (b) VERIFIER D'ABORD que les 156 moteurs sont equivalents a un modele connu,
      puis simuler ce modele unique.

VOIE (b) RETENUE, sur trois arguments.

1. **L'equivalence est un fait mesure, pas une hypothese.** Les 156 moteurs sont
   IDENTIQUES entre eux, octet pour octet, hors du bloc de configuration : une
   seule empreinte SHA-256 apres masquage de la region de configuration et du
   drapeau `isNewFormat`. Une seule variante sur 156.

2. **La voie (a) porterait le risque qu'elle pretend ecarter.** Un interpreteur
   JavaScript ecrit en Python serait lui-meme un modele, non verifie, de 156
   programmes ; ses divergences seraient invisibles. La voie (b) transforme au
   contraire la question « sont-ils tous pareils ? » en PRECONDITION VERIFIEE a
   chaque passage : `engine_fingerprint()` est recalculee pour chaque grille et
   comparee a `REFERENCE_ENGINE`. Une grille future dont le moteur derive d'un
   octet est signalee et son verdict est un ECHEC, pas un silence.

3. **Le modele a simuler est deja ecrit et deja eprouve.** Le `diff` du moteur
   embarque contre `cases/scoring.js` ne touche PAS la boucle de calcul : elle
   est identique ligne pour ligne (meme traitement des cases de detail, meme
   repli sur les radios, meme table communication A=4..E=0, meme ponderation par
   `coef`, meme `max > 0 ? (score/max)*100 : 0`). Les differences sont ailleurs
   — voir ci-dessous. `section_max` et `orphan_criteria` d'AMBOSS s'appliquent
   donc au caractere pres, sans copie.

Ce que ce script NE fait pas : prouver l'absence d'exception a l'execution.
Aucune analyse statique ne le peut. C'est l'objet de `browser_probe.js`, et son
verdict est accablant — voir plus bas.


AUDIT DES 156 MOTEURS EMBARQUES — RESULTAT
===========================================
**Une seule variante.** 156/156, empreinte `c3e2534e…`. Deux formes seulement de
DECLARATION du bareme, a l'interieur de `calculateScores()` :
  * declarative (154 grilles) : `maxScores = {anamnese: 29, …};`
    `sectionInfo = [{key: "anamnese", prefix: "a", count: 8, …}, …];`
  * imperative (2 grilles — RESCOS-63, RESCOS-64 station double 2) :
    `maxScores["anamnese"] = 29;` `sectionInfo.push({…});`, avec
    `isNewFormat = true`. C'est exactement la forme de RESCOS-7 et RESCOS-9.
Le drapeau `isNewFormat` est declare et JAMAIS lu, dans les deux formes : mort,
comme dans les copies de RESCOS-7 et RESCOS-9.

**Ce sont la meme fourche perimee que RESCOS-7 et RESCOS-9.** Le `diff` contre
`cases/scoring.js` rend exactement les six manques que le lot r7 avait releves :

  1. la garde `if (missingEl)` — ABSENTE ;
  2. l'APPEL de `saveToRegistry()` — ABSENT ;
  3. la DEFINITION de `saveToRegistry()` — ABSENTE ;
  4. le chargeur dynamique de `srs.js` — ABSENT ;
  5. la detection du mode circuit et le retour a `exam.html` en fin de
     minuteur — ABSENTS ;
  6. `createNavBar()` / `createCircuitNav()` — ABSENTS.

**Et ils levent tous une exception.** Mesure en navigateur (`browser_probe.js`,
Chrome for Testing, 165 grilles) : **13 446 exceptions**
`TypeError: Cannot read properties of null (reading 'style')`, **156 grilles sur
156**, au chargement PUIS a chaque clic. La cause est le manque n° 1 combine a
un fait du HTML : le `<div class="missing-items" id="missingItems">` que le
moteur adresse sans garde est **commente** dans les 156 grilles
(`<!-- ÉLÉMENTS MANQUANTS (MASQUÉS) -->`). `getElementById` rend `null`, et la
derniere instruction de `calculateScores()` echoue — a chaque appel.

**Consequence directe, mesuree : `ecos_registry` reste vide sur 0/165.** Aucune
grille de ce corpus ne fait remonter son score au tableau de bord. C'est le
defaut de RESCOS-7 et RESCOS-9, a l'echelle du corpus entier.

Le bareme reste NEANMOINS calculable et calcule : l'exception survient APRES
l'ecriture des scores de section, du total et de la note. Le navigateur affiche
bien 100 % et la note A sur 155 des 156 grilles. C'est pourquoi ce script
s'applique sans reserve — la simulation porte sur la partie du moteur qui
s'execute correctement.


ETAT DEPUIS LE LOT `l3` : LES 156 MOTEURS ONT ETE REMPLACES PAR LE FICHIER PARTAGE
===================================================================================
`apply_shared_engine.py` a bascule les 156 grilles sur
`<script src="../scoring.js">` avec un bareme transpose en `window.caseConfig`,
comme r7 l'avait fait sur RESCOS-7 et RESCOS-9. Les six manques disparaissent
avec la fourche ; mesure en navigateur apres bascule : **0 exception** sur les
165 grilles, **156/165 ecrivant `ecos_registry`** (les 9 restantes sont les
feuilles porte, qui n'ont pas de score).

Ce script lit donc DEUX etats du corpus, et c'est deliberement conserve :

  * `window.caseConfig` + `<script src="../scoring.js">` — l'etat courant. Son
    empreinte de moteur est le marqueur `SHARED_ENGINE`, non un SHA : le
    fichier partage est suivi par `git` comme n'importe quel autre et toute
    modification apparait a son `diff`. C'etait precisement l'argument qui
    justifiait le SHA tant que le moteur etait noye dans 170 000 caracteres de
    HTML ; il tombe avec la bascule.
  * le moteur embarque et ses deux formes de declaration — l'etat d'avant.
    La branche est conservee parce qu'elle DECRIT ce que le corpus a porte et
    parce qu'elle est la seule chose qui distinguerait une grille future
    reimportee du vault d'une grille deja basculee.


LES 9 GRILLES SANS `calculateScores` : LES FEUILLES PORTE
==========================================================
Ce sont les 9 fichiers « … - Feuille porte.html », la consigne remise au
candidat devant la station : intitule, contexte, taches, duree. Elles ne portent
AUCUN critere (0 `criteria-row`, 0 `<input>`, 0 `<script>`, 0 `maxScores`) et
**n'ont donc pas de bareme**. Ce n'est pas un defaut : une feuille porte ne se
note pas. Elles sont explicitement RECONNUES et non pas ignorees en silence —
voir `is_door_sheet()` — pour qu'une grille notee qui perdrait son `<script>` ne
puisse pas se glisser dans la meme categorie.


POURQUOI CE CONTROLE EST DISTINCT DE check_invariants.py
=========================================================
`check_invariants.py` compare l'etat courant a un snapshot : il repond a « le
bareme est-il le meme qu'hier ? », jamais a « le bareme est-il juste ? ». Un
bareme faux depuis l'origine reste vert indefiniment — c'est ce qui s'est
produit sur AMBOSS-9.

Ce script ne compare rien a un passe : il simule le remplissage complet et exige
que le total tombe sur `maxScores[key]` ET sur le denominateur affiche au
candidat, et que le pourcentage global fasse 100 %.

QUATRE ECARTS DETECTES, dont un propre a ce corpus :
  * `count` trop grand — un critere promis par `count` mais absent de la page
    rapporte 0. Signale « ABSENT ».
  * sous-item ORPHELIN — un critere hors de la sequence `prefix1..prefixN`,
    cochable mais jamais calcule (AMBOSS-9 : `a12b`).
  * `maxScores` et le `<span class="score">` qui divergent l'un de l'autre.
  * section VIDE mais PONDEREE (RESCOS-12 et RESCOS-13) — `count: 0`,
    `maxScores: 0`, coefficient conserve.
  * **somme des coefficients differente de 1** — ecart INEDIT, propre a ce
    corpus : RESCOS-63 declare deux sections a `coef: 0.25` et rien d'autre.
    La somme fait 0,5, le global plafonne donc a **50 %** meme grille
    parfaitement remplie, sans qu'aucune section ne soit en ecart. Les quatre
    controles precedents restent muets ; `coef_sum_anomaly()` le nomme.
"""
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib

_amboss = lib.amboss_module("check_reachability")
section_max = _amboss.section_max
orphan_criteria = _amboss.orphan_criteria

# Empreinte du moteur embarque, configuration masquee. Les 156 grilles notees
# la portaient, toutes, jusqu'a la bascule du lot `l3`. Une divergence d'un
# octet fait echouer la grille : le modele simule ci-dessous ne la decrirait
# plus. Conservee : c'est ce qui distinguerait une grille reimportee du vault.
REFERENCE_ENGINE = "c3e2534eefd493b31bb3a8f785daf9c464912a0ce693466e9d5180ab3e7daa77"

# Empreinte des grilles qui chargent le moteur PARTAGE. Un marqueur et non un
# SHA : `cases/scoring.js` est un fichier suivi par `git`, dont toute
# modification apparait a son propre `diff` — voir l'entete.
SHARED_ENGINE = "shared:cases/scoring.js"

# Les 165 grilles vivent dans `cases/rescos-locales/`, soit exactement deux
# niveaux sous la racine, comme `cases/rescos/` : `../scoring.js` resout donc
# sur `cases/scoring.js`, et les `../../index.html` / `../../exam.html` que le
# moteur partage construit resolvent sur la racine du depot.
SHARED_SRC = re.compile(r'<script[^>]+src="\.\./scoring\.js"')

_SCRIPT = re.compile(r"<script\b[^>]*>(.*?)</script>", re.S)
_ISNEW = re.compile(r"const isNewFormat = (?:true|false);")
_CFG_START = "// Configuration pour le "
_CFG_END = "// Calcul des scores pour chaque section"


def engine_source(html):
    """Le JavaScript embarque d'une grille, blocs concatenes — "" si aucun."""
    return "\n".join(_SCRIPT.findall(html))


def engine_fingerprint(html):
    """SHA-256 du moteur embarque, region de configuration masquee.

    Deux grilles au bareme different mais au moteur identique rendent la meme
    empreinte : c'est precisement ce qu'on veut geler — la LOGIQUE, pas les
    chiffres, qui sont geles ailleurs (`snapshot_invariants.py`).

    Le masquage couvre les DEUX formes de declaration : la region va du
    commentaire `// Configuration pour le …` (« format traditionnel » ou
    « nouveau format ») jusqu'au commentaire `// Calcul des scores …`, qui les
    suit dans les deux cas. `isNewFormat` est masque a part : c'est un drapeau
    mort, dont la valeur suit la forme de declaration sans rien commander.

    Une grille qui charge le moteur PARTAGE rend le marqueur `SHARED_ENGINE` :
    elle n'a plus de moteur a elle, et le fichier partage est suivi par `git`.
    """
    if SHARED_SRC.search(html):
        return SHARED_ENGINE
    js = engine_source(html)
    if not js:
        return None
    a = js.find(_CFG_START)
    b = js.find(_CFG_END, a) if a >= 0 else -1
    masked = (js[:a] + "/*CONFIG*/" + js[b:]) if a >= 0 and b > 0 else js
    return hashlib.sha256(_ISNEW.sub("/*ISNEW*/", masked).encode()).hexdigest()


def is_door_sheet(html):
    """Vrai pour une FEUILLE PORTE : consigne de station, sans bareme.

    Reconnue par la conjonction de trois faits, et non par le nom du fichier :
    la classe `feuille-porte`, l'absence de tout `<script>`, l'absence de tout
    critere note. Une grille notee qui perdrait son moteur ne pourrait donc pas
    se faire passer pour une feuille porte et echapper au controle.
    """
    return ('class="feuille-porte"' in html
            and not engine_source(html)
            and 'class="criteria-row"' not in html)


def parse_config(html):
    """maxScores, coef, sectionInfo et denominateurs affiches — les trois formes.

    Tente d'abord `window.caseConfig` (l'etat courant des 156 grilles notees),
    puis, sur une grille encore a l'ancien etat, la forme declarative (154
    grilles) et la forme imperative (RESCOS-63 et RESCOS-64 station double 2).
    Les denominateurs affiches (`<span class="score">`) sont lus de la meme
    facon dans les trois cas : ce sont des chaines litterales du HTML.

    NOTE — pourquoi `parse_config` d'AMBOSS n'est pas reutilisee ici alors que
    `scripts/rescos/` la reutilisait : elle lit `maxScores: {…}` n'importe ou
    dans le fichier. Sur RESCOS elle tombait sur le `window.caseConfig`, un
    objet unique. Ici la meme chaine apparait DANS `calculateScores()`, precedee
    de la declaration `let maxScores = {};` — le premier `maxScores: {` du
    fichier est le bon, mais s'appuyer sur cet ordre serait fragile. La lecture
    est donc bornee a la region de configuration, delimitee par ses deux
    commentaires.
    """
    js = engine_source(html)
    a = js.find(_CFG_START)
    b = js.find(_CFG_END, a) if a >= 0 else -1
    cfg = js[a:b] if a >= 0 and b > 0 else ""

    spans = {k: int(v) for k, v in re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html)}

    # Forme `window.caseConfig` — bornee au bloc lui-meme, pour la meme raison
    # que ci-dessous : `let maxScores = {};` traine ailleurs dans le corpus.
    m = re.search(r"window\.caseConfig\s*=\s*\{(.*?)\n\};", js, re.S)
    if m:
        cc = m.group(1)
        mm = re.search(r"maxScores:\s*\{([^}]*)\}", cc)
        max_scores = {k: int(v) for k, v in
                      re.findall(r"(\w+):\s*(\d+)", mm.group(1))} if mm else {}
        mm = re.search(r"coef:\s*\{([^}]*)\}", cc)
        coef = {k: float(v) for k, v in
                re.findall(r"(\w+):\s*([\d.]+)", mm.group(1))} if mm else {}
        mm = re.search(r"sectionInfo:\s*\[(.*?)\]", cc, re.S)
        blobs = re.findall(r"\{[^{}]*\}", mm.group(1) if mm else "")
        return max_scores, coef, _sections(blobs), spans

    m = re.search(r"maxScores\s*=\s*\{([^}]*)\}", cfg)
    if m:
        max_scores = {k: int(v) for k, v in re.findall(r"(\w+):\s*(\d+)", m.group(1))}
        m = re.search(r"coef\s*=\s*\{([^}]*)\}", cfg)
        coef = {k: float(v) for k, v in re.findall(r"(\w+):\s*([\d.]+)", m.group(1))} if m else {}
        m = re.search(r"sectionInfo\s*=\s*\[(.*?)\];", cfg, re.S)
        blobs = re.findall(r"\{[^{}]*\}", m.group(1) if m else "")
    else:
        max_scores = {k: int(v) for k, v in
                      re.findall(r'maxScores\["(\w+)"\]\s*=\s*(\d+)', cfg)}
        coef = {k: float(v) for k, v in
                re.findall(r'coef\["(\w+)"\]\s*=\s*([\d.]+)', cfg)}
        blobs = re.findall(r"sectionInfo\.push\(\{([^}]*)\}\)", cfg)

    return max_scores, coef, _sections(blobs), spans


def _sections(blobs):
    """Les `sectionInfo[]` lus d'une liste de litteraux `{…}`, forme commune."""
    sections = []
    for blob in blobs:
        key = re.search(r'key:\s*"(\w+)"', blob)
        prefix = re.search(r'prefix:\s*"(\w+)"', blob)
        count = re.search(r"count:\s*(\d+)", blob)
        if not (key and prefix and count):
            continue
        score_id = re.search(r'scoreId:\s*"(\w+)"', blob)
        sections.append({
            "key": key.group(1),
            "prefix": prefix.group(1),
            "count": int(count.group(1)),
            # scoreId: section.scoreId || section.key + "Score"
            "scoreId": score_id.group(1) if score_id else key.group(1) + "Score",
            "isComm": re.search(r"isComm:\s*true", blob) is not None,
        })
    return sections


def empty_weighted_sections(html):
    """Sections declarees vides mais conservant un coefficient non nul.

    Retourne [(key, coef), ...]. Leur pourcentage vaut 0 quoi qu'il arrive et
    leur part de coefficient est definitivement perdue : c'est la cause exacte
    d'un « global < 100 % » sans aucun ecart de section (RESCOS-12, RESCOS-13).
    """
    max_scores, coef, sections, _ = parse_config(html)
    return [(s["key"], coef.get(s["key"], 0)) for s in sections
            if s["count"] == 0 and not max_scores.get(s["key"])
            and coef.get(s["key"], 0)]


def coef_sum_anomaly(html):
    """Somme des coefficients si elle s'ecarte de 1 — None sinon.

    Ecart INEDIT, propre a ce corpus. Toutes sections parfaitement remplies, le
    global vaut la somme des `coef` : si elle ne fait pas 1, le candidat ne peut
    pas atteindre 100 % et rien dans la page ne le dit.
    """
    _, coef, sections, _ = parse_config(html)
    if not sections:
        return None
    total = sum(coef.get(s["key"], 0) for s in sections)
    return None if abs(total - 1.0) < 1e-9 else total


def check_one(path):
    """(ok, lignes) — verdict d'une grille et son detail lisible."""
    html = lib.strip_base64(path.read_text(encoding="utf-8"))

    if is_door_sheet(html):
        return True, ["    feuille porte — consigne de station, sans bareme (attendu)"]

    fingerprint = engine_fingerprint(html)
    if fingerprint is None:
        return False, ["    aucun <script> : ni moteur embarque, ni feuille porte"]
    if fingerprint not in (SHARED_ENGINE, REFERENCE_ENGINE):
        return False, [
            "    MOTEUR INCONNU — ni le moteur partage, ni la fourche embarquee",
            f"      empreinte {fingerprint[:16]}… au lieu de {SHARED_ENGINE} "
            f"ou {REFERENCE_ENGINE[:16]}…",
            "      la simulation ci-dessous ne la decrit plus : relire son <script>"]

    max_scores, coef, sections, spans = parse_config(html)
    lines, ok, global_pct = [], True, 0.0

    if not sections:
        return False, ["    sectionInfo introuvable ou illisible"]

    for section in sections:
        key = section["key"]
        total, detail, missing = section_max(html, section)
        declared = max_scores.get(key)
        span = spans.get(section["scoreId"])
        ecart = not (total == declared == span)
        ok = ok and not ecart and not missing
        lines.append(
            f'    {key:<14} atteignable={total:<4} maxScores={declared}'
            f'  affiche=/{span}{"   <<< ECART" if ecart else ""}')
        if missing:
            lines.append(
                f'      count={section["count"]} promet {len(missing)} critere(s) '
                f'que la page ne porte pas : {", ".join(missing)}')
        if declared:
            global_pct += (total / declared) * coef.get(key, 0)
        lines.append(f"      {' · '.join(detail)}" if detail else "      (aucun critere)")

    orphans = orphan_criteria(html, sections)
    if orphans:
        ok = False
        lines.append(f"    critere(s) hors sequence, jamais calcule(s) : {', '.join(orphans)}")

    pct = round(global_pct * 100)
    lines.append(f"    global si tout est coche : {pct} %")
    if pct != 100:
        ok = False
        for key, c in empty_weighted_sections(html):
            lines.append(
                f"    section VIDE mais PONDEREE : {key} (count=0, maxScores=0) "
                f"garde coef={c} — {round(c * 100)} % du score global sont "
                f"inatteignables par construction")
        bad_sum = coef_sum_anomaly(html)
        if bad_sum is not None:
            lines.append(
                f"    somme des coefficients = {bad_sum} au lieu de 1 — le global "
                f"plafonne a {round(bad_sum * 100)} % quoi que fasse le candidat")
    return ok, lines


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    checked = bad = doors = 0
    for path in lib.grids():
        if only and only not in path.name:
            continue
        checked += 1
        ok, lines = check_one(path)
        if lines and lines[0].startswith("    feuille porte"):
            doors += 1
        if not ok:
            bad += 1
        if not ok or only:
            print(f'{path.name}  {"OK" if ok else "ECART"}')
            print("\n".join(lines))

    if only and checked == 0:
        print(f"Aucune grille ne correspond au filtre {only!r}.")
        return 1
    if bad:
        print(f"\nECHEC — {bad} grille(s) sur {checked} au bareme inatteignable")
        return 1
    print(f"\nOK — {checked} grille(s) ({doors} feuille(s) porte sans bareme, "
          f"{checked - doors} notee(s)), bareme atteignable a 100 % sur chaque section")
    return 0


if __name__ == "__main__":
    sys.exit(main())
