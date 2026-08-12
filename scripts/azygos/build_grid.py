"""Rend une grille ECOS du corpus azygos à partir d'un JSON d'extraction.

Usage :
    python3 scripts/azygos/build_grid.py <uuid> <numero>

Le fichier produit suit le gabarit du dépôt : mêmes classes CSS, même
`window.caseConfig`, même chaîne scoring.js / persistence.js. Aucun JS n'est
écrit par cas.
"""

from __future__ import annotations

import base64
import io
import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_azygos as lib  # noqa: E402
import lexique_semantique as lex  # noqa: E402

from PIL import Image  # noqa: E402

QUALITE_JPEG = 82
LARGEUR_MAX = 900


# --------------------------------------------------------------------------
# Paramètres vitaux
# --------------------------------------------------------------------------

MOTIFS_VITAUX = [
    ("TA", r"(\d{2,3}/\d{2,3})\s*mmHg", lambda m: f"{m} mmHg"),
    ("FC", r"(?:fréquence cardiaque|FC|pouls|Puls)\D{0,6}(\d{2,3})", lambda m: f"{m} bpm"),
    ("FR", r"(?:fréquence respiratoire|FR)\D{0,6}(\d{1,2})", lambda m: f"{m}/min"),
    ("SpO₂", r"SpO2\D{0,4}(\d{2,3})\s*%", lambda m: f"{m}%"),
    ("T°", r"(\d{2}[.,]\d)\s*°C", lambda m: f"{m}°C"),
]


def extrait_vitaux(texte: str) -> list[tuple[str, str]]:
    """Reconstruit la grille de paramètres vitaux du gabarit.

    Azygos livre les vitaux en une seule phrase libre ; le gabarit attend des
    cases séparées. Ce qui n'est pas reconnu reste visible dans le critère
    « Paramètres vitaux » de la section examen — rien n'est perdu.
    """
    out = []
    for etiquette, motif, fmt in MOTIFS_VITAUX:
        m = re.search(motif, texte, re.I)
        if m:
            out.append((etiquette, fmt(m.group(1))))
    if not any(e == "T°" for e, _ in out) and re.search(r"apyrétique|afébrile", texte, re.I):
        out.append(("T°", "afébrile"))
    return out


# --------------------------------------------------------------------------
# Images
# --------------------------------------------------------------------------

def image_en_base64(url: str, destination: Path) -> tuple[str, dict] | tuple[None, None]:
    """Télécharge, recompresse en JPEG et renvoie la data URI + le manifeste.

    Les URL Supabase sont signées et expirent en une heure : le téléchargement
    doit avoir lieu pendant la session d'extraction.
    """
    # Le fichier déjà recompressé fait foi : les signatures Supabase expirent en
    # une heure, or une reconstruction du corpus peut survenir bien plus tard.
    if destination.exists():
        donnees = destination.read_bytes()
        img = Image.open(io.BytesIO(donnees))
        print(f"    ↺ image en cache {destination.name}")
    else:
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                brut = r.read()
        except Exception as exc:  # noqa: BLE001
            print(f"    ⚠ échec du téléchargement : {exc}")
            return None, None

        img = Image.open(io.BytesIO(brut)).convert("RGB")
        if img.width > LARGEUR_MAX:
            img = img.resize(
                (LARGEUR_MAX, round(img.height * LARGEUR_MAX / img.width)), Image.LANCZOS
            )
        tampon = io.BytesIO()
        img.save(tampon, format="JPEG", quality=QUALITE_JPEG, optimize=True)
        donnees = tampon.getvalue()

        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(donnees)

    import hashlib

    manifeste = {
        "nom": destination.name,
        "sha256": hashlib.sha256(donnees).hexdigest(),
        "octets": len(donnees),
        "dimensions": f"{img.width}x{img.height}",
        "source": url.split("?")[0],
    }
    return "data:image/jpeg;base64," + base64.b64encode(donnees).decode(), manifeste


# --------------------------------------------------------------------------
# Rendu des sections notées
# --------------------------------------------------------------------------

def vignette(texte: str) -> str:
    """Bulle d'information clinique, ouverte au survol ou au focus.

    Sans JavaScript : `:hover` couvre le pointeur, `:focus-within` couvre le
    tactile et le clavier (l'élément est focusable). La bulle est masquée à
    l'impression — l'annexe théorique en reprend l'intégralité.
    """
    if not texte:
        return ""
    return (
        '<span class="info-vignette" tabindex="0" role="button"'
        ' aria-label="Information complémentaire">'
        '<span class="info-vignette-marque" aria-hidden="true">i</span>'
        f'<span class="info-vignette-bulle" role="tooltip">{lib.echappe(texte)}</span>'
        "</span>"
    )


def rend_libelle(item: dict) -> str:
    """Compose le libellé d'un détail, vignette de sous-groupe comprise.

    Un sous-groupe (« Dynamique temporelle ») a sa propre justification, qui
    porte sur l'ensemble du bloc. Elle s'affiche donc collée à son nom, et
    seulement sur le premier enfant — la répéter sur chacun serait du bruit.
    """
    label = item["label"]
    info_sg = item.get("info_sous_groupe")
    if " · " not in label:
        return lib.echappe(label)

    gauche, droite = label.split(" · ", 1)
    # « Antécédents · Antécédents » : le préfixe n'apporte rien et disparaît —
    # mais sa vignette, elle, porte du contenu et doit survivre.
    if gauche.strip().lower() == droite.strip().lower():
        return lib.echappe(droite) + vignette(info_sg or "")
    if info_sg:
        return (
            f'<span class="detail-sous-groupe">{lib.echappe(gauche)}'
            f"{vignette(info_sg)}</span> · {lib.echappe(droite)}"
        )
    return lib.echappe(label)


def rend_detail(cle: str, prefixe: str, index: int, item: dict, img_html: str) -> str:
    valeur = " — ".join(item.get("valeurs") or [])
    reponse = (
        f' <span class="patient-response">[{lib.echappe(valeur)}]</span>' if valeur else ""
    )
    return f"""<div class="detail-row">
    <div class="detail-text criteria-detail">{rend_libelle(item)}{reponse}{vignette(item.get("info", ""))}{img_html}</div>
    <div class="detail-checkboxes">
        <label class="detail-checkbox"><input type="checkbox" id="{cle}-detail-{index}" value="1" onchange="updateDetailScore('{cle}', '{prefixe}')" /></label>
    </div>
</div>"""


def rend_critere(prefixe: str, n: int, groupe: dict, images: dict,
                 infos: dict) -> tuple[str, int]:
    cle = f"{prefixe}{n}"
    details = lib.aplatit(groupe, infos)
    morceaux = []
    for i, item in enumerate(details):
        # Les images vivent dans l'annexe « Iconographie clinique » (convention
        # du dépôt : .images-wrapper). Ici on ne pose qu'un renvoi, pour ne pas
        # faire exploser la hauteur des lignes de la grille notée.
        cle_img = item["label"].split(" · ")[-1].strip()
        renvoi = (
            ' <span class="criteria-detail-note">(voir iconographie)</span>'
            if cle_img in images
            else ""
        )
        morceaux.append(rend_detail(cle, prefixe, i, item, renvoi))

    corps = "".join(morceaux)
    return (
        f"""<div class="criteria-row" id="criteria-{cle}">
    <div>
        <div class="criteria-text">{n}. {lib.echappe(groupe["groupe"])} <button class="comment-button" onclick="toggleComment('{cle}')" title="Ajouter un commentaire">📝</button></div>
<div class="details-with-checkboxes">{corps}</div>        <div class="criterion-comment-section" id="comment-section-{cle}">
            <textarea class="comment-textarea" id="comment-{cle}" placeholder="Commentaire sur ce critère..." oninput="updateCommentButton('{cle}'); autoResizeTextarea(this);"></textarea>
        </div>
    </div>
    <div class="checkbox-group"></div>
    <div class="checkbox-group"></div>
    <div class="checkbox-group"></div>
    <div class="points-display" id="points-{cle}">0</div>
</div>""",
        len(details),
    )


def rend_section(cle: str, prefixe: str, libelle: str, groupes: list[dict], images: dict,
                 infos: dict, score_id: str | None = None) -> tuple[str, int, int]:
    lignes, total = [], 0
    for n, g in enumerate(groupes, start=1):
        html_critere, pts = rend_critere(prefixe, n, g, images, infos)
        lignes.append(html_critere)
        total += pts
    ident = score_id or f"{cle}Score"
    corps = "\n".join(lignes)
    return (
        f"""        <div class="section">
            <div class="section-header">
                <span>{libelle} (25%)</span>
                <span class="score">Score : <span id="{ident}">0</span>/{total}</span>
            </div>
            <div class="section-content">
                <div class="header-row">
                    <div>Critères</div>
                    <div>Oui</div>
                    <div>±</div>
                    <div>Non</div>
                    <div>Points</div>
                </div>
{corps}
            </div>
        </div>""",
        total,
        len(groupes),
    )


def rend_communication(dimensions: list[dict]) -> tuple[str, int]:
    lignes = []
    for n, dim in enumerate(dimensions, start=1):
        cle = f"c{n}"
        radios = "\n".join(
            f"""                    <div class="checkbox-group">
                        <input type="radio" name="{cle}" value="{niveau}" data-criteria="{lib.echappe(dim["label"])}" onchange="updateScore('communication', this)" />
                    </div>"""
            for niveau in lib.NIVEAUX_COMM
        )
        desc = " ".join(dim.get("valeurs") or [])
        lignes.append(
            f"""                <div class="communication-section" id="criteria-{cle}">
                    <div>
                        <div class="communication-text">{n}. {lib.echappe(dim["label"])} <button class="comment-button" onclick="toggleComment('{cle}')" title="Ajouter un commentaire">📝</button></div>
                        <div class="communication-desc">{lib.echappe(desc)}</div>
                        <div class="criterion-comment-section" id="comment-section-{cle}">
                            <textarea class="comment-textarea" id="comment-{cle}" placeholder="Commentaire sur ce critère..." oninput="updateCommentButton('{cle}'); autoResizeTextarea(this);"></textarea>
                        </div>
                    </div>
{radios}
                </div>"""
        )
    total = len(dimensions) * 4
    corps = "\n".join(lignes)
    return (
        f"""        <div class="section">
            <div class="section-header">
                <span>Communication (25%)</span>
                <span class="score">Score : <span id="communicationScore">0</span>/{total}</span>
            </div>
            <div class="section-content">
                <div class="header-row communication-header">
                    <div>Critères</div>
                    <div>A</div>
                    <div>B</div>
                    <div>C</div>
                    <div>D</div>
                    <div>E</div>
                </div>
{corps}
            </div>
        </div>""",
        total,
    )


def rend_images(images: dict, descriptions: dict) -> str:
    """Rend le bloc iconographique au balisage exact des corpus existants.

    `.images-wrapper` est un frère du bloc `.annexes`, pas un de ses enfants :
    c'est un conteneur flex qui aligne les planches côte à côte.
    """
    if not images:
        return ""
    items = []
    for n, (label, uri) in enumerate(images.items(), start=1):
        desc = descriptions.get(label, "")
        bloc_desc = (
            f'    <div class="annexe-description">{lib.echappe(desc)}</div>\n' if desc else ""
        )
        items.append(
            f'<div class="annexe-item" data-image-id="img{n}">\n'
            f'    <div class="annexe-title">{lib.echappe(label)}</div>\n'
            f"{bloc_desc}"
            f'    <div class="annexe-image">\n'
            f'        <img src="{uri}" alt="{lib.echappe(label)}" loading="lazy">\n'
            f"    </div>\n</div>"
        )
    return '<div class="images-wrapper">\n' + "\n".join(items) + "\n</div>"


def rend_theorie(data: dict) -> str:
    """Rassemble les « Informations complémentaires » en annexe pédagogique.

    Chaque bulle justifie un item de la grille : pourquoi cette question, ce
    qu'oriente telle réponse. Prises isolément ce sont des notes de survol ;
    remises dans l'ordre de la consultation, elles forment le fil du
    raisonnement clinique du cas — d'où cette relecture linéaire, qui sert
    aussi de version imprimable des bulles.
    """
    infos = data.get("infos") or {}
    if not infos:
        return ""
    sections = []
    for onglet in data.get("ordre") or []:
        groupes = data["onglets"].get(onglet)
        if not groupes:
            continue
        lignes = []
        for groupe in groupes:
            for item in lib.aplatit(groupe, infos):
                # La justification du sous-groupe précède celles de ses items :
                # elle donne le cadre dans lequel les suivantes se lisent.
                if item.get("info_sous_groupe"):
                    lignes.append(
                        f'<li class="theorie-sous-groupe">'
                        f"<strong>{lex.colorise(item['label_sous_groupe'])}</strong> — "
                        f"{lex.colorise(item['info_sous_groupe'])}</li>"
                    )
                if not item.get("info"):
                    continue
                label = item["label"]
                if " · " in label:
                    g, d = label.split(" · ", 1)
                    if g.strip().lower() == d.strip().lower():
                        label = d
                lignes.append(
                    f"<li><strong>{lex.colorise(label)}</strong> — "
                    f"{lex.colorise(item['info'])}</li>"
                )
        if lignes:
            sections.append(
                f'<div class="theorie-section">\n'
                f"    <h4>{lib.echappe(lib.nettoie_onglet(onglet))}</h4>\n"
                f'    <ul>{"".join(lignes)}</ul>\n'
                f"</div>"
            )
    if not sections:
        return ""
    return (
        '<div class="annexe-item annexe-theorie">'
        '<div class="annexe-title">Raisonnement clinique — pourquoi chaque item compte</div>'
        '<div class="annexe-theorie-content">' + "".join(sections) + "</div></div>"
    )


def rend_annexes(prep: dict, infos: dict, notes: list[str], theorie: str = "") -> str:
    blocs = []
    if theorie:
        blocs.append(theorie)
    if prep["focus"]:
        items = "".join(f"<li>{lex.colorise(f)}</li>" for f in prep["focus"])
        blocs.append(
            '<div class="annexe-item annexe-expert">'
            '<div class="annexe-title">Focus du cas</div>'
            f'<div class="annexe-expert-content"><ul>{items}</ul></div></div>'
        )
    if prep["resume"]:
        paras = "".join(f"<p>{lex.colorise(p)}</p>" for p in prep["resume"])
        blocs.append(
            '<div class="annexe-item annexe-theorie">'
            '<div class="annexe-title">Synthèse du cas</div>'
            f'<div class="annexe-expert-content">{paras}</div></div>'
        )
    if prep["akdp"]:
        paras = "".join(f"<p>{lex.colorise(p)}</p>" for p in prep["akdp"])
        blocs.append(
            '<div class="annexe-item annexe-theorie">'
            '<div class="annexe-title">Aperçu AKDP</div>'
            f'<div class="annexe-expert-content">{paras}</div></div>'
        )
    if notes:
        paras = "".join(f"<p>{lib.echappe(p)}</p>" for p in notes)
        blocs.append(
            '<div class="annexe-item annexe-theorie">'
            '<div class="annexe-title">Modalités de la station</div>'
            f'<div class="annexe-expert-content">{paras}</div></div>'
        )
    if not blocs:
        return ""
    return (
        '<div class="annexes">\n<h3>Annexes</h3>\n<div class="annexes-grid">\n'
        + "\n".join(blocs)
        + "\n</div>\n</div>"
    )


# --------------------------------------------------------------------------
# Assemblage
# --------------------------------------------------------------------------

def construit(uuid: str, numero: int, fiche: dict) -> Path:
    data = lib.charge(uuid)
    infos = lib.infos_cas(data)
    prep = lib.preparation(data)
    ident = f"AZYGOS-{numero}"
    titre = data["meta"]["titre"] or fiche["titre"]

    print(f"  → {ident} · {titre}")

    # Images : téléchargement + recompression
    images: dict[str, str] = {}
    manifeste: list[dict] = []
    for img in data.get("images", []):
        # Les accents sont retirés, pas remplacés : « cutanée » -> « cutanee ».
        sans_accent = unicodedata.normalize("NFKD", img["label"].lower())
        sans_accent = "".join(c for c in sans_accent if not unicodedata.combining(c))
        base = re.sub(r"[^a-z0-9]+", "-", sans_accent).strip("-")
        nom = f"azygos-{numero:02d}-{base}.jpg"
        uri, meta = image_en_base64(img["url"], lib.IMAGES / nom)
        if uri:
            images[img["label"]] = uri
            manifeste.append(meta)
            print(f"    ✓ image {nom} ({meta['dimensions']}, {meta['octets'] // 1024} Ko)")

    # Légendes de l'iconographie : la description clinique de l'item homonyme.
    descriptions: dict[str, str] = {}
    for onglet in data["onglets"].values():
        if not isinstance(onglet, list) or not onglet or not isinstance(onglet[0], dict):
            continue
        for g in onglet:
            for it in g.get("items", []):
                if it["label"] in images:
                    descriptions[it["label"]] = " — ".join(it.get("valeurs") or [])

    # Répartition des onglets cliniques dans les quatre sections notées.
    ordre = data.get("ordre") or [
        o for o in data["onglets"] if o not in lib.ONGLETS_FIXES
    ]
    par_section: dict[str, list] = {cle: [] for cle, _, _ in lib.SECTIONS}
    for nom_onglet in ordre:
        groupes = data["onglets"].get(nom_onglet)
        if not groupes:
            continue
        par_section[lib.classe_onglet(nom_onglet)].extend(groupes)

    corps, maxima, section_info = [], {}, []
    for cle, prefixe, libelle in lib.SECTIONS:
        if cle == "communication":
            # Les dimensions OFSP sont des items, pas des groupes ; un poste
            # double en expose deux séries (poste 1 et poste 2).
            dims = [it for g in par_section[cle] for it in g.get("items", [])]
            html_section, total = rend_communication(dims)
            nb = len(dims)
            entree = {"key": cle, "prefix": prefixe, "count": nb,
                      "label": libelle, "isComm": True}
        else:
            html_section, total, nb = rend_section(
                cle, prefixe, libelle, par_section[cle], images, data.get("infos", {}),
                score_id="statusScore" if cle == "examen" else None,
            )
            entree = {"key": cle, "prefix": prefixe, "count": nb, "label": libelle}
            if cle == "examen":
                entree["scoreId"] = "statusScore"
        corps.append(html_section)
        maxima[cle] = total
        section_info.append(entree)

    # Paramètres vitaux
    texte_vitaux = ""
    for g in data["onglets"].get("Statut clinique") or []:
        for it in g["items"]:
            if "vitaux" in it["label"].lower():
                texte_vitaux = " ".join(it.get("valeurs") or [])
    vitaux = extrait_vitaux(texte_vitaux)
    bloc_vitaux = ""
    if vitaux:
        cases = "".join(
            f"""                <div class="vital-sign">
                    <div class="vital-sign-label">{lib.echappe(e)}</div>
                    <div class="vital-sign-value">{lib.echappe(v)}</div>
                </div>
"""
            for e, v in vitaux
        )
        bloc_vitaux = (
            f'            <div class="vital-signs" style="grid-template-columns: repeat({len(vitaux)}, 1fr);">\n'
            f"{cases}            </div>\n"
        )

    total_general = sum(maxima.values())
    config = {
        "maxScores": maxima,
        "coef": {k: 0.25 for k in maxima},
        "sectionInfo": section_info,
    }

    descriptif = fiche.get("patient", "")
    fichier = lib.SORTIE / lib.nom_fichier(ident, titre, descriptif)
    titre_page = f"{ident} - {titre}" + (f" - {descriptif}" if descriptif else "")

    doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>{lib.echappe(titre_page)} - Grille ECOS</title>
    <link rel="stylesheet" href="../case-styles.css">
    <script src="../theme-sync.js"></script>
    <link rel="stylesheet" href="../mobile-responsive.css">
</head>
<body class="revision-mode">
    <!-- MODE SELECTOR -->
    <div class="mode-selector">
        <button class="mode-button active" onclick="switchMode('revision')">🔍 Révision</button>
        <button class="mode-button" onclick="switchMode('exam')">📝 Examen</button>
    </div>

    <!-- BOUTONS RÉVISION (Mode Révision uniquement) -->
    <div class="revision-controls">
        <button class="lacune-button" onclick="identifyLacunes()">🎯 Identifier les lacunes</button>
        <button class="reset-revision-button" onclick="resetTimer()">↻ Reset</button>
    </div>

    <!-- MINUTEUR ECOS -->
    <div class="timer-container" id="timerContainer">
        <div class="timer-display" id="timerDisplay">{infos.get('duree', '13 min').split()[0]}:00</div>
        <div class="timer-controls">
            <button id="startBtn" class="timer-btn start-btn" onclick="startTimer()">▶ Démarrer</button>
            <button id="stopBtn" class="timer-btn stop-btn" onclick="stopTimer()" style="display: none;">⏸ Arrêter</button>
            <button id="resetBtn" class="timer-btn reset-btn" onclick="resetTimer()">↻ Reset</button>
        </div>
        <div class="timer-status" id="timerStatus" style="display: none;"></div>
    </div>

    <div class="container">
        <div class="header">
            <h1>Grille d'évaluation ECOS - {lib.echappe(ident)} - {lib.echappe(titre)}</h1>
    <div class="simulation-bar">
      <a href="https://ecos-sim.replit.app/simulation?station={ident}" class="btn-simulate" target="_blank" rel="noopener">
        &#x1FA7A; Simuler cette station avec Patient ECOS
      </a>
    </div>
            <p style="margin: 5px 0;">📍 {lib.echappe(fiche.get('cadre', ''))}</p>
            <p style="margin: 5px 0;">👤 {lib.echappe(descriptif)}</p>
            <p style="margin: 5px 0;">🏷️ {lib.echappe(infos.get('specialite', ''))} · {lib.echappe(infos.get('format', ''))} · {lib.echappe(infos.get('difficulte', ''))} · {lib.echappe(infos.get('duree', ''))}</p>
{bloc_vitaux}        </div>
{chr(10).join(corps)}
        <!-- TOTAUX -->
        <div class="total-sections">
            <div class="total-section">
                <div class="total-label">Score Global</div>
                <div class="total-body">
                    <div class="total-score" id="totalScore">0/{total_general}</div>
                </div>
            </div>
            <div class="total-section">
                <div class="total-label">% par Section</div>
                <div class="total-pourcent-body">
                    <div class="total-pourcent-sections">
                        <div class="total-pourcent-section">
                            <div class="total-section-label">Anamnèse</div>
                            <div class="pourcent-body">
                                <div class="total-pourcent-value"><span id="anamnese-percentage">0</span>%</div>
                            </div>
                        </div>
                        <div class="total-pourcent-section">
                            <div class="total-section-label">Examen clinique</div>
                            <div class="pourcent-body">
                                <div class="total-pourcent-value"><span id="examen-percentage">0</span>%</div>
                            </div>
                        </div>
                        <div class="total-pourcent-section">
                            <div class="total-section-label">Management</div>
                            <div class="pourcent-body">
                                <div class="total-pourcent-value"><span id="management-percentage">0</span>%</div>
                            </div>
                        </div>
                        <div class="total-pourcent-section">
                            <div class="total-section-label">Communication</div>
                            <div class="pourcent-body">
                                <div class="total-pourcent-value"><span id="communication-percentage">0</span>%</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="total-section">
                <div class="total-label">Note Globale</div>
                <div class="total-body">
                    <div class="total-note-globale" id="globalGrade">E</div>
                </div>
            </div>
        </div>
{rend_annexes(prep, infos, prep['notes'], rend_theorie(data))}
{rend_images(images, descriptions)}
        <!-- COMMENTAIRE GÉNÉRAL -->
        <div class="section-comment-section global">
            <h4 style="margin: 0 0 10px 0; color: #2c5aa0; font-size: 18px;">Commentaire général</h4>
            <textarea class="comment-textarea" id="comment-general" placeholder="Commentaire général sur l'évaluation..." oninput="updateGeneralComment(); autoResizeTextarea(this);"></textarea>
        </div>
    </div>
    <script>
window.caseConfig = {json.dumps(config, ensure_ascii=False, indent=4)};
</script>
<script src="../scoring.js"></script>
    <!-- BOUTON IMPRIMER EN PDF -->
    <button class="print-button" onclick="window.print()">🖨️ Imprimer en PDF</button>

<script src="../persistence.js"></script>
</body>
</html>
"""

    fichier.parent.mkdir(parents=True, exist_ok=True)
    fichier.write_text(doc, encoding="utf-8")
    if manifeste:
        (lib.IMAGES / f"_manifeste-{numero:02d}.json").write_text(
            json.dumps(manifeste, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    return fichier


def main() -> None:
    uuid, numero = sys.argv[1], int(sys.argv[2])
    inventaire = json.loads(
        (lib.RACINE / "scripts" / "azygos" / "inventaire.json").read_text(encoding="utf-8")
    )
    fiche = next(c for c in inventaire["cas"] if c["id"] == uuid)
    chemin = construit(uuid, numero, fiche)
    print(f"  ✓ {chemin.relative_to(lib.RACINE)} ({chemin.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
