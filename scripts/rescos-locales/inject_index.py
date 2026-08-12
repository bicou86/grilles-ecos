"""Insère le corpus rescos-locales dans index.html (onglet, styles, cartes).

Idempotent : relancer le script remplace le bloc existant au lieu de le
dupliquer. Même patron que `scripts/azygos/inject_index.py`, dont il reprend la
mécanique des marqueurs et les trois ancres JavaScript ; il s'en écarte sur un
point : l'inventaire n'est pas un fichier JSON mais **les grilles elles-mêmes**.
Ce corpus a été importé, pas généré — il n'existe aucune source structurée dont
les cartes pourraient être dérivées. Titre et description patient sont donc lus
dans chaque `<title>` et dans le `👤` du bandeau, c'est-à-dire dans ce que la
page affiche réellement, et non dans une copie qui pourrait en diverger.

    python3 scripts/rescos-locales/inject_index.py
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib  # noqa: E402

RACINE = Path(__file__).resolve().parents[2]
INDEX = RACINE / "index.html"

# Bordeaux : seule famille de teintes encore libre parmi les sept corpus
# déclarés (bleu, ambre, vert, rose, marine, sarcelle, violet).
COULEUR = "#9f1239"
FOND_CLAIR = "#ffe4e6"
TEXTE = "#9f1239"

DEBUT = "<!-- rescos-locales:début -->"
FIN = "<!-- rescos-locales:fin -->"

# Classement par mots-clés, PREMIÈRE correspondance gagnante : l'ordre est donc
# significatif. Les motifs les plus spécifiques passent avant les génériques —
# « douleur thoracique » avant « douleur », « toux » après « BPCO ».
SYSTEMES: list[tuple[str, str]] = [
    ("Urgences", r"urgence|polytraumatis|choc (septique|anaphylactique|h[ée]morragique)|"
                 r"arr[êe]t cardio|intoxication|r[ée]animation|triage"),
    ("Cardiologie", r"thoracique|stemi|nstemi|infarctus|coronar|insuffisance cardiaque|"
                    r"fibrillation|palpitation|souffle|valv|p[ée]ricard|hypertension|syncope|drs"),
    ("Vasculaire", r"dissection aortique|an[ée]vrisme|aomi|claudication|art[ée]riopathie|"
                   r"tvp|thrombose|embolie pulmonaire|veineu|varice|isch[ée]mie aigu"),
    ("Pneumologie", r"bpco|asthme|pneumonie|dyspn[ée]e|pneumothorax|pleur|respiratoire|"
                    r"tuberculose|covid|apn[ée]e|h[ée]moptysie"),
    ("Gastro-entérologie", r"abdomin|digestif|diarrh|constipation|rectorragie|h[ée]matoch[ée]zie|"
                           r"m[ée]l[ée]na|diverticul|cirrhose|h[ée]patite|transaminase|ict[èe]re|"
                           r"pancr[ée]atite|ulc[èe]re|crohn|c[œo]liaque|gastro|colique h[ée]patique|"
                           r"vomissement|dysphagie|appendicite|hernie|occlusion|colorectal|"
                           r"[ée]pigastr|reflux|h[ée]morro"),
    ("Neurologie", r"neurolog|avc|c[ée]phal[ée]|migraine|[ée]pilep|convuls|guillain|"
                   r"scl[ée]rose en plaques|parkinson|d[ée]mence|alzheimer|m[ée]ningite|"
                   r"h[ée]morragie sous-arachno[ïi]|par[ée]sie|paralysie|vertige|tremblement|"
                   r"canal carpien|hernie discale|myasth|confusion|coma|[ée]quilibre"),
    ("Psychiatrie", r"psy|d[ée]pression|d[ée]pressif|anxi|panique|suicid|anorexie|boulimie|"
                    r"bipolaire|maniaque|schizophr|psychotique|addiction|alcool|tabac|"
                    r"entretien motivationnel|tdah|autisme|insomnie|stress post|borderline|"
                    r"obsessionnel|deuil"),
    ("Pédiatrie", r"p[ée]diatr|nourrisson|enfant|adolescent|fillette|gar[çc]on de \d|"
                  r"fille de \d|b[ée]b[ée]|croissance|vaccin.*enfant|convulsion f[ée]brile"),
    ("Gynécologie", r"gyn[ée]colog|grossesse|obst[ée]tr|contraception|post-partum|"
                    r"m[ée]norragie|m[ée]trorragie|pelvien|sein|m[ée]nopause|pr[ée]-?[ée]clampsie|"
                    r"accouchement|st[ée]rilit"),
    ("Urologie/Néphrologie", r"urolog|n[ée]phro|urinaire|mictionnel|dysurie|h[ée]maturie|"
                             r"lithiase|colique n[ée]phr[ée]tique|prostate|r[ée]nal|scrotal|"
                             r"testicul|incontinence"),
    ("Rhumatologie", r"rhumato|articul|arthrite|arthrose|lombalgie|dos|rachis|goutte|"
                     r"fracture|entorse|tendin|coiffe|[ée]paule|genou|hanche|poignet|"
                     r"cheville|ost[ée]oporose|polymyalgia|spondyl|msq|s[ée]miologie|"
                     r"boiterie|traumatisme (ms|mi)|coxarthrose|lupus|myalgie"),
    ("Dermatologie", r"dermato|cutan|[ée]ruption|acn[ée]|psoriasis|urticaire|zona|"
                     r"prurit|stevens-johnson|[ée]ryth[èe]me|l[ée]sion.*peau|m[ée]lanome"),
    ("ORL", r"orl|otite|otorrh|surdit|otoscl[ée]rose|angine|amygdal|sinusite|"
            r"[ée]pistaxis|dysphonie|acouph|cou\b|thyro[ïi]d.*nodule|mal au cou"),
    ("Ophtalmologie", r"ophtalmo|[œo]il|oculaire|vision|visuel|amaurose|diplopie|"
                      r"conjonctiv|glaucome|r[ée]tin"),
    ("Endocrinologie", r"endocrin|diab[èe]te|glyc[ée]mie|thyro[ïi]d|hypothyro|hyperthyro|"
                       r"ob[ée]sit|cholest[ée]rol|acidoc[ée]tose|hyponatr[ée]mie|surr[ée]nal"),
    ("Hématologie/Oncologie", r"h[ée]matolog|oncolog|cancer|tumeur|an[ée]mie|leuc[ée]mie|"
                              r"lymphome|adénopathie|coagul|thrombop|palliati|bbn|"
                              r"annonce.*mauvaise"),
    ("Gériatrie", r"g[ée]riatr|chute|personne [âa]g[ée]e|ems|polym[ée]dication|"
                  r"polypathologie|sujet [âa]g[ée]|d[ée]pendance"),
    ("Médecine générale", r"."),  # filet — jamais vide
]


def _norm(txt: str) -> str:
    """Minuscules sans accents, pour que les motifs n'aient pas à les gérer."""
    plat = unicodedata.normalize("NFD", txt.lower())
    return "".join(c for c in plat if unicodedata.category(c) != "Mn")


def systeme(titre: str) -> str:
    plat = _norm(titre)
    for nom, motif in SYSTEMES:
        if re.search(_norm(motif), plat):
            return nom
    return "Médecine générale"


def echappe(txt: str) -> str:
    return html.escape(txt, quote=True)


def lit(path: Path) -> tuple[str, str]:
    """Renvoie (titre affiché, description patient) lus DANS la grille."""
    texte = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<title>(.*?)</title>", texte, re.S)
    titre = html.unescape(m.group(1)).strip() if m else path.stem
    titre = re.sub(r"\s*[-–]\s*(Grille ECOS|Feuille porte)\s*$", "", titre).strip()

    m = re.search(r"<p[^>]*>\s*👤\s*(.*?)</p>", texte, re.S)
    if m:
        sub = re.sub(r"<[^>]+>", "", html.unescape(m.group(1)))
        sub = re.sub(r"\s+", " ", sub).strip(" .")
    else:
        sub = "Feuille porte" if "Feuille porte" in path.stem else "RESCOS local"
    if len(sub) > 120:
        sub = sub[:117].rstrip() + "…"
    return titre, sub


def styles() -> str:
    return f"""      {DEBUT}
      .tab[data-cat="rescos-locales"].active {{
        background: {COULEUR};
      }}
      .section-header .badge.rescos-locales {{
        background: {FOND_CLAIR};
        color: {TEXTE};
      }}
      .rescos-locales .num {{
        background: {FOND_CLAIR};
        color: {TEXTE};
      }}
      .rescos-locales .cat-tag {{
        background: {FOND_CLAIR};
        color: {TEXTE};
      }}
      .cat-bar-fill.rescos-locales {{
        background: {COULEUR};
      }}
      {FIN}
"""


def onglet() -> str:
    return f"""          {DEBUT}
          <button
            class="tab"
            data-cat="rescos-locales"
            role="tab"
            aria-selected="false"
          >
            Locales
          </button>
          {FIN}
"""


def cartes(grilles: list[Path]) -> str:
    lignes = [f"      {DEBUT}",
              '      <div class="section" data-section="rescos-locales">',
              '        <div class="section-header">',
              '          <span class="badge rescos-locales">LOCALES</span>',
              f"          <h2>Cas 1–{len(grilles)}</h2>",
              '          <span class="count"></span>', "        </div>",
              '        <div class="grid">']
    for n, path in enumerate(grilles, start=1):
        titre, sub = lit(path)
        lignes += [
            "          <a",
            '            class="card rescos-locales"',
            f'            data-system="{echappe(systeme(path.stem))}"',
            f'            href="cases/rescos-locales/{quote(path.name)}"',
            f'            ><span class="num">{n}</span>',
            '            <div class="info">',
            f'              <div class="title">{echappe(titre)}</div>',
            f'              <div class="sub">{echappe(sub)}</div>',
            "            </div>",
            '            <span class="cat-tag">LOC</span></a',
            "          >",
        ]
    lignes += ["        </div>", "      </div>", f"      {FIN}"]
    return "\n".join(lignes) + "\n"


def main() -> None:
    grilles = sorted(lib.grids(), key=lambda p: p.name)
    texte = INDEX.read_text(encoding="utf-8")
    avant = len(texte)

    # Purge d'une injection précédente : lignes entières, indentation comprise,
    # pour que deux exécutions successives rendent le même fichier à l'octet.
    texte = re.sub(r"[ \t]*" + re.escape(DEBUT) + r".*?" + re.escape(FIN) + r"\n",
                   "", texte, flags=re.S)

    ancre_style = ('      .tab[data-cat="casecos"].active {\n'
                   "        background: #0d9488;\n      }\n")
    assert ancre_style in texte, "ancre CSS introuvable"
    texte = texte.replace(ancre_style, ancre_style + styles(), 1)

    ancre_onglet = ('          <button\n            class="tab"\n'
                    '            data-cat="casecos"\n')
    assert ancre_onglet in texte, "ancre onglet introuvable"
    texte = texte.replace(ancre_onglet, onglet() + ancre_onglet, 1)

    ancre_grille = '      <div class="no-results" id="noResults">'
    assert ancre_grille in texte, "ancre section introuvable"
    texte = texte.replace(ancre_grille, cartes(grilles) + ancre_grille, 1)

    # Le corpus doit aussi être connu du JavaScript : sans cela les cartes
    # existent dans le DOM mais aucun filtre ni compteur ne les voit. Le test
    # de classe doit passer AVANT celui de « casecos » ? Non : les jetons de
    # classe sont exacts, `contains("rescos")` est faux pour « rescos-locales ».
    for ancre, ajout in [
        ('          if (card.classList.contains("casecos")) return "casecos";\n',
         '          if (card.classList.contains("rescos-locales"))\n'
         '            return "rescos-locales";\n'),
        ('            "casecos",\n', '            "rescos-locales",\n'),
        ('            casecos: "CasECOS",\n', '            "rescos-locales": "Locales",\n'),
    ]:
        if ajout not in texte:
            assert ancre in texte, f"ancre JS introuvable : {ancre!r}"
            texte = texte.replace(ancre, ancre + ajout, 1)

    INDEX.write_text(texte, encoding="utf-8")
    print(f"index.html : {avant} → {len(texte)} octets")
    for cle in ('data-cat="rescos-locales"', 'data-section="rescos-locales"',
                'class="card rescos-locales"'):
        print(f"  {texte.count(cle):>4} × {cle}")

    repartition: dict[str, int] = {}
    for p in grilles:
        repartition[systeme(p.stem)] = repartition.get(systeme(p.stem), 0) + 1
    print("  systèmes :", ", ".join(
        f"{k} {v}" for k, v in sorted(repartition.items(), key=lambda kv: -kv[1])))


if __name__ == "__main__":
    main()
