#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte les blocs pédagogiques `resume`, `theorie` et `presentation` dans une grille.

Pourquoi ce script existe. Vingt grilles du dépôt n'ont aucun contenu pédagogique
— ni résumé, ni points théoriques, ni fiche de présentation. Il ne leur manque pas
du balisage mais du texte, et ce texte doit être écrit à la main.

Le principe qui gouverne tout le reste : **le contenu est rédigé en texte brut,
jamais en HTML.** Chaque grille reçoit un module sous `scripts/peda/contenu/`, où
l'auteur écrit des phrases et des listes. Ce script les passe par
`lexique_semantique.colorise()`, fabrique le HTML et l'insère. Trois conséquences
voulues :

  * le contenu se relit sans balises, donc une erreur médicale se voit ;
  * le balisage sémantique est produit par la MÊME règle que le reste du dépôt,
    au lieu d'être posé à la main span par span ;
  * une correction se fait dans le texte, et la régénération la reporte.

Les titres de section échappent à la colorisation : aucun corpus ne colorise ses
titres, et le faire ici créerait une divergence visible.

Usage
-----
    inject_peda_blocks.py NOM_DU_MODULE               # injecte dans la grille déclarée
    inject_peda_blocks.py NOM_DU_MODULE --cible F     # injecte dans une copie (test)
    inject_peda_blocks.py NOM_DU_MODULE --dry         # affiche le HTML, n'écrit rien
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENU = Path(__file__).parent / "contenu"

sys.path.insert(0, str(REPO / "scripts" / "azygos"))
import lexique_semantique as lex  # noqa: E402

ANCRE = "<!-- COMMENTAIRE GÉNÉRAL -->"

#: Le bloc injecté ne porte AUCUN marqueur de commentaire, et c'est délibéré.
#: `lib_rescos_locales.BLOCKS` découpe les grilles par équilibrage des `<div>`,
#: avec une queue attendue que `bounds_anomalies()` vérifie. Un
#: `<!-- peda:début -->` glissé entre la fin d'un bloc et cette queue la rend
#: méconnaissable : essayé, et `check_invariants` a immédiatement signalé deux
#: blocs devenus invisibles — `presentation` finissant sur « …</div>
#: <!-- peda:fin --><!-- COMMENTAIR » et `annexe-image` sur « …</div>
#: <!-- peda:début --><div ». C'est exactement l'angle mort que ce contrôle
#: existe pour attraper.
#:
#: L'idempotence se passe donc de marqueur : le bloc commence toujours par
#: `<div class="resume">` et court jusqu'à l'ancre. Aucune des 20 grilles
#: visées n'a de `resume` préexistant — c'est même la raison pour laquelle
#: elles sont visées.
OUVERTURE = '<div class="resume">'

#: Les trois familles de sections du bloc `resume`, dans l'ordre du gabarit.
#: La classe suffixe colore la bordure gauche ; elle suit le sens de la section.
FAMILLES = {
    "anamnese": "section-anamnese",
    "examen": "section-examen",
    "management": "section-management",
}


def _t(texte: str) -> str:
    """Texte de contenu : colorisé et échappé par le lexique."""
    return lex.colorise(texte)


def _titre(texte: str) -> str:
    """Titre de section : échappé, jamais colorisé."""
    return (texte.replace("&", "&amp;").replace("<", "&lt;")
                 .replace(">", "&gt;").replace('"', "&quot;"))


def _famille(titre: str) -> str:
    """Devine la famille d'une section de résumé à partir de son intitulé."""
    plat = titre.lower()
    if "anamnèse" in plat or "anamnese" in plat:
        return FAMILLES["anamnese"]
    if "examen" in plat or "diagnostic" in plat or "clinique" in plat:
        return FAMILLES["examen"]
    if "prise en charge" in plat or "traitement" in plat or "suivi" in plat:
        return FAMILLES["management"]
    return ""


def rend_resume(c: dict) -> str:
    """Bloc `resume` : sections à sous-sections, points clés, check-list."""
    out = ['<div class="resume">',
           f'<h3 class="resume-main-title">📚 🔥 {_titre(c["titre_resume"])}</h3>',
           '<div class="resume-content">']

    for titre, sous_sections in c["resume"]:
        classe = _famille(titre)
        out.append(f'<div class="resume-section{" " + classe if classe else ""}">')
        out.append(f'<h4 class="section-title">{_titre(titre)}</h4>')
        for sous_titre, puces in sous_sections:
            out.append('<div class="resume-subsection">')
            out.append(f'<h5 class="subsection-title">{_titre(sous_titre)}</h5>')
            out.append('<ul class="resume-subsection-points">')
            out += [f"<li>{_t(p)}</li>" for p in puces]
            out.append("</ul>")
            out.append("</div>")
        out.append("</div>")

    if c.get("points_cles"):
        out.append('<div class="resume-section">')
        out.append('<h4 class="section-title">✅ Points clés ECOS</h4>')
        out.append('<ul class="resume-points">')
        # Le premier point de chaque paire est mis en avant : c'est la
        # convention des corpus denses (german, amboss), où `highlight`
        # signale ce qu'il faut retenir si on ne retient qu'une chose.
        for i, p in enumerate(c["points_cles"]):
            classe = "resume-bullet highlight" if i % 3 == 0 else "resume-bullet"
            out.append(f'<li class="{classe}">{_t(p)}</li>')
        out.append("</ul>")
        out.append("</div>")

    if c.get("checklist"):
        out.append('<div class="resume-section">')
        out.append('<h4 class="section-title">📋 Check-list rapide ECOS</h4>')
        for sous_titre, puces in c["checklist"]:
            out.append('<div class="resume-subsection">')
            out.append(f'<h5 class="subsection-title">{_titre(sous_titre)}</h5>')
            out.append('<ul class="resume-subsection-points">')
            out += [f"<li>{_t(p)}</li>" for p in puces]
            out.append("</ul>")
            out.append("</div>")
        out.append("</div>")

    out += ["</div>", "</div>"]
    return "\n".join(out)


def rend_theorie(c: dict) -> str:
    """Bloc `theorie` : une section par notion structurante du cas."""
    out = ['<div class="annexe-item annexe-theorie">',
           '    <div class="annexe-title">Points théoriques et pratiques</div>',
           '    <div class="annexe-theorie-content">']
    for titre, chapeau, puces in c["theorie"]:
        out.append('        <div class="theorie-section">')
        out.append(f"            <h4>{_titre(titre)}</h4>")
        if chapeau:
            out.append(f"            <p>{_t(chapeau)}</p>")
        if puces:
            out.append("            <ul>")
            out += [f"                <li>{_t(p)}</li>" for p in puces]
            out.append("            </ul>")
        out.append("        </div>")
    out += ["    </div>", "</div>"]
    return "\n".join(out)


def rend_presentation(c: dict) -> str:
    """Bloc `presentation` : checklist, version longue, SBAR, mnémo, questions."""
    p = c["presentation"]
    out = ['<div class="presentation-patient">',
           f'    <h3 class="presentation-main-title">📑 Fiche ECOS – Cas : '
           f'{_titre(c["titre_cas"])}</h3>',
           '    <div class="presentation-content">']

    out.append('        <div class="presentation-section section-checklist">')
    out.append('            <h4 class="presentation-section-title">'
               '🧩 Checklist mentale (présentation systématisée)</h4>')
    out.append('            <ul class="presentation-points">')
    out += [f"                <li>{_t(x)}</li>" for x in p["checklist_mentale"]]
    out.append("            </ul>")
    if p.get("mnemo"):
        nom, lignes = p["mnemo"]
        out.append('<div class="mnemo-box">')
        out.append(f'    <div class="mnemo-title">💡 👉 Mnémo {_titre(nom)}</div>')
        out.append('    <ul class="mnemo-items">')
        out += [f"        <li>{_t(x)}</li>" for x in lignes]
        out.append("    </ul>")
        out.append("</div>")
    out.append("        </div>")

    out.append('        <div class="presentation-section section-longue">')
    out.append('            <h4 class="presentation-section-title">'
               '🎤 Version longue (≈2-3 min)</h4>')
    out.append('            <div class="presentation-content">'
               + "".join(f"<p>{_t(x)}</p>" for x in p["version_longue"]) + "</div>")
    out.append("        </div>")

    sbar = p["sbar"]
    libelles = {"S": "S (Situation)", "B": "B (Background)",
                "A": "A (Assessment)", "R": "R (Recommendation)"}
    out.append('        <div class="presentation-section section-express">')
    out.append('            <h4 class="presentation-section-title">'
               '⚡ Version express (SBAR, 30 sec)</h4>')
    out.append('            <div class="presentation-content">'
               + "".join(f"<p>{libelles[k]} : {_t(sbar[k])}</p>" for k in "SBAR")
               + "</div>")
    out.append("        </div>")

    if p.get("questions"):
        out.append('        <div class="presentation-section section-questions">')
        out.append('            <h4 class="presentation-section-title">'
                   "❓ Questions probables de l'examinateur (avec réponses orales)</h4>")
        out.append('            <div class="presentation-subsection">')
        out.append("                <h5>Ce que l'examinateur demandera</h5>")
        out.append('                <div class="qa-container">')
        for i, (question, reponse) in enumerate(p["questions"], start=1):
            out.append('                <div class="presentation-qa">')
            out.append('                    <div class="presentation-question">')
            out.append(f'                        <span class="q-number">Q{i}</span>')
            out.append(f'                        <span class="q-text">{_t(question)}</span>')
            out.append("                    </div>")
            out.append(f'                    <div class="presentation-reponse text">'
                       f"{_t(reponse)}</div>")
            out.append("                </div>")
        out.append("                </div>")
        out.append("            </div>")
        out.append("        </div>")

    out += ["    </div>", "</div>"]
    return "\n".join(out)


def rend_scenario(c: dict) -> str:
    """Bloc `scenario` : le rôle jouable du patient simulé.

    Il n'est pas optionnel. `lib_rescos_locales.BLOCKS` définit la fin du bloc
    `presentation` comme STRICTEMENT `<div class="annexe-item annexe-scenario">`,
    sans alternative — et la mesure le confirme : sur les 58 grilles du corpus
    qui portent une fiche de présentation, 58 ont un scénario juste après. Une
    `presentation` livrée seule rend le bloc invisible au découpage, ce que
    `bounds_anomalies()` signale aussitôt.
    """
    out = ['<div class="annexe-item annexe-scenario">',
           '    <div class="annexe-title">Scénario du patient simulé</div>',
           '    <div class="annexe-scenario-content">']
    for titre, entrees in c["scenario"]:
        out.append('        <div class="scenario-section">')
        out.append(f"            <h4>{_titre(titre)}</h4>")
        out.append('            <div class="property-group">')
        for etiquette, valeur in entrees:
            if etiquette:
                out.append(f"                <p><strong>{_titre(etiquette)} :</strong> "
                           f"{_t(valeur)}</p>")
            else:
                out.append(f"                <p>{_t(valeur)}</p>")
        out.append("            </div>")
        out.append("        </div>")
    out += ["    </div>", "</div>"]
    return "\n".join(out)


def _equilibre(bloc: str, quoi: str) -> str:
    ouv, ferm = len(re.findall(r"<div\b", bloc)), len(re.findall(r"</div>", bloc))
    if ouv != ferm:
        raise SystemExit(f"{quoi} déséquilibré : {ouv} <div> pour {ferm} </div>. "
                         "Un découpage par équilibrage casserait sur tout le corpus.")
    return bloc


def rend(c: dict) -> tuple[str, str]:
    """Renvoie (bloc_resume, bloc_annexes) — ils s'insèrent à deux endroits.

    Le corpus range ses annexes dans un unique `<div class="annexes">` suivi
    d'un `annexes-grid`, et beaucoup de grilles en ont déjà un, avec leurs
    images. En créer un second casserait l'ordre attendu : le `resume` se pose
    donc avant celui qui existe, et les trois annexes à l'intérieur de sa
    grille, devant les images.
    """
    resume = _equilibre(rend_resume(c) + "\n", "bloc resume")
    annexes = _equilibre("\n".join([
        rend_theorie(c),
        rend_presentation(c),
        rend_scenario(c),
    ]) + "\n", "blocs annexes")
    return resume, annexes


ANNEXES = '<div class="annexes">'
GRILLE_ANNEXES = '<div class="annexes-grid">'
THEORIE = '<div class="annexe-item annexe-theorie">'
IMAGES = '<div class="images-wrapper">'


def _ancre_annexes(html: str) -> str | None:
    """Ce devant quoi les trois annexes se posent, dans une grille qui en a déjà.

    Insertion et retrait DOIVENT viser la même chaîne, sans quoi le retrait
    emporte les espaces d'origine et l'inversibilité tombe — c'est ce que le
    contrôle a signalé à la première version, qui insérait après
    `annexes-grid` mais retirait jusqu'à `images-wrapper`.
    """
    if IMAGES in html:
        return IMAGES
    if GRILLE_ANNEXES in html:
        return None  # structure d'annexes vide : cas non rencontré, à instruire
    return None


#: Signature de la coquille d'annexes que CE script fabrique. Elle permet au
#: retrait de savoir, sans ambiguïté, s'il doit défaire une structure créée ici
#: ou seulement le contenu glissé dans une structure préexistante.
#:
#: Le besoin est apparu sur trois cas de figure distincts, rencontrés dans les
#: 19 grilles : Psy-Vignette 10 a `annexes` + `annexes-grid` + `images-wrapper` ;
#: Psy-Vignette 1 et 7 n'ont rien ; la grille Diabète a un `images-wrapper`
#: SANS conteneur `annexes`. Déduire la branche de retrait de la seule présence
#: de `images-wrapper` échouait sur le troisième.
COQUILLE = ANNEXES + "\n<h3>Annexes</h3>\n" + GRILLE_ANNEXES + "\n"


def _retire(html: str) -> str:
    """Défait une injection, en miroir exact des deux branches de `injecte`."""
    if OUVERTURE + "\n" in html or OUVERTURE in html:
        debut = html.find(OUVERTURE)
        if debut >= 0 and COQUILLE in html[debut:debut + 200000]:
            # Coquille fabriquée ici : le bloc a été posé d'un tenant.
            suite = _ancre_annexes(html) or ANCRE
            return re.sub(re.escape(OUVERTURE) + r".*?(?=" + re.escape(suite) + r")",
                          "", html, count=1, flags=re.S)
    # Structure préexistante : `resume` devant elle, les trois blocs dedans.
    html = re.sub(re.escape(OUVERTURE) + r".*?(?=" + re.escape(ANNEXES) + r")",
                  "", html, count=1, flags=re.S)
    suite = _ancre_annexes(html) or ANCRE
    return re.sub(re.escape(THEORIE) + r".*?(?=" + re.escape(suite) + r")",
                  "", html, count=1, flags=re.S)


def injecte(html: str, resume: str, annexes: str) -> tuple[str, str]:
    """Renvoie (html_modifié, état) — 'ok', 'remplacé', ou un motif d'échec."""
    if ANCRE not in html:
        return html, f"ancre {ANCRE!r} introuvable"

    etat = "ok"
    if OUVERTURE in html or THEORIE in html:
        html = _retire(html)
        etat = "remplacé"
        if OUVERTURE in html or THEORIE in html:
            return html, "un bloc subsiste après retrait — grille non prévue pour ce script"

    suite = _ancre_annexes(html)
    if ANNEXES in html and GRILLE_ANNEXES in html and suite:
        # La grille a déjà sa structure d'annexes : on s'y range plutôt que
        # d'en créer une seconde. Les trois blocs passent devant les images,
        # pour que `scenario` finisse sur `images-wrapper` comme le corpus
        # l'attend.
        sortie = html.replace(ANNEXES, resume + ANNEXES, 1)
        sortie = sortie.replace(suite, annexes + suite, 1)
    else:
        # Pas de conteneur d'annexes : on pose la structure complète, devant
        # les images si elles existent — sans quoi `scenario` finirait sur un
        # `images-wrapper` qu'il précéderait — sinon devant l'ancre.
        bloc = resume + COQUILLE + annexes + "</div>\n</div>\n"
        sortie = html.replace(suite or ANCRE, bloc + (suite or ANCRE), 1)

    # Contrôle d'inversibilité : retirer ce qu'on vient de poser doit redonner
    # l'entrée à l'octet près. C'est ce qui garantit qu'une seconde exécution
    # ne dérive pas, et que rien d'autre n'a bougé dans le fichier.
    if _retire(sortie) != html:
        return html, "strip-back non inversible"
    return sortie, etat


def charge(nom: str) -> dict:
    fichier = CONTENU / f"{nom.replace('-', '_')}.py"
    if not fichier.exists():
        raise SystemExit(f"contenu introuvable : {fichier}")
    spec = importlib.util.spec_from_file_location(fichier.stem, fichier)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CONTENU


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("module", help="nom du module de contenu, p. ex. psy_vignette_10")
    ap.add_argument("--cible", help="fichier à modifier (défaut : celui déclaré)")
    ap.add_argument("--dry", action="store_true", help="affiche le HTML sans écrire")
    args = ap.parse_args()

    contenu = charge(args.module)
    resume, annexes = rend(contenu)
    if args.dry:
        print(resume + annexes)
        return

    cible = Path(args.cible) if args.cible else REPO / "cases" / contenu["grille"]
    if not cible.exists():
        raise SystemExit(f"grille introuvable : {cible}")

    avant = cible.read_text(encoding="utf-8")
    apres, etat = injecte(avant, resume, annexes)
    if etat not in ("ok", "remplacé"):
        raise SystemExit(f"ÉCHEC — {etat}")
    cible.write_text(apres, encoding="utf-8")

    bloc = resume + annexes
    spans = len(re.findall(r'class="c-[a-z]+"', bloc))
    mots = len(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", bloc)).split())
    print(f"{cible.name} — {etat}")
    print(f"  {mots} mots, {spans} spans "
          f"({1000 * spans / mots:.0f} pour 1000 mots)")


if __name__ == "__main__":
    main()
