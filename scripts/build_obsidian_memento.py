#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere le memento Obsidian des 9 grilles officielles, groupe par specialite.

    python3 scripts/build_obsidian_memento.py

Ce que le memento retient : les ITEMS des sections anamnese, status et
management — les questions a poser, les gestes a faire, les decisions a
prendre. Ce qu'il laisse : le bareme (seuils, points), les reponses du
patient, les consignes destinees a l'expert·e, et les lignes de synthese
(« Anamnese en general », « Management en general »), qui notent la maniere
et non un item a couvrir.

Idempotent : relance apres modification d'une grille, il reecrit un fichier
identique si la grille n'a pas bouge. C'est la raison d'etre de ce script
plutot que d'un fichier ecrit a la main — les neuf grilles vivent, et un
memento fige diverge en silence.

TROIS CHAMPS VIENNENT DU COFFRE, pas de la grille : `specialite` (le titre de
niveau 1), `priorite` (l'etoile ⭐️ des cas « Top 18 » et « Haut rendement ») et
le nom de la page SSP. Ils sont lus dans les pages `SSP ECOS/SSP — *.md` si le
coffre est accessible, et repris de la table ci-dessous sinon.

LE PARTAGE DU MANAGEMENT EN DEUX ENCADRES — 🔬 examens complementaires et
💊 prise en charge — n'existe pas dans les grilles : c'est une lecture, donc
elle est declaree explicitement, ligne par ligne, dans `EXAMENS`.

DEUX RATTACHEMENTS SONT DES APPROXIMATIONS assumees, faute de page SSP dediee :
RESCOS-70b (paralysie faciale peripherique) est rattache a « Parésie - AVC »,
dont son cas est precisement le diagnostic differentiel ; RESCOS-69b (fracture
de l'humerus apres altercation) suit le rattachement deja cure de RESCOS-69 a
« Douleur d'Épaule ».
"""
import html as H
import io
import re
import unicodedata
from pathlib import Path

REPO = Path("/Users/damienfulliquet/Developer/GitHub/grilles-ecos")
SORTIE = REPO / "docs" / "obsidian-memento"
COFFRE = Path("/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian/SSP ECOS")

# grille, SSP (page du coffre), specialite de repli, titre du cas, source
CAS = [
    ("RESCOS-68b - Eruption cutanée - Grille ECOS.html",
     "Éruption Cutanée", "Dermatologie",
     "Éruption cutanée — zona", "EF 2026 · Station 2"),
    ("RESCOS-58b - Rectorragies - Grille ECOS.html",
     "Rectorragies & Hémorragie Digestive Basse", "Gastro-Hépatologie",
     "Rectorragies — cancer rectal", "EF 2026 · Station 5"),
    ("RESCOS-67b - Fatigue - Grille ECOS.html",
     "Fatigue", "Médecine Interne",
     "Fatigue et baisse d'énergie — hypothyroïdie", "EF 2026 · Station 1"),
    ("RESCOS-69b - Traumatisme MS - Basketteur 25 ans - Grille ECOS.html",
     "Douleur d'Épaule", "Musculo-Squelettique",
     "Traumatisme du membre supérieur — fracture de l'humérus",
     "Entraînement fédéral 2025 · Station 6"),
    ("RESCOS-57b - Ralentissement - Consultation téléphonique - Grille ECOS.html",
     "Confusion - État Confusionnel Aigu", "Neurologie",
     "Ralentissement d'un résident d'EMS, consultation téléphonique — gastro-entérite",
     "Entraînement fédéral 2025 · Station 4"),
    ("RESCOS-70b - Paralysie faciale - Grille ECOS.html",
     "Parésie - AVC", "Neurologie",
     "Paralysie faciale — paralysie de Bell", "EF 2026 · Station 3"),
    ("RESCOS-9b_-_Boiterie_pe_diatrique_-_Fillette_de_2_ans_-_Grille_ECOS.html",
     "Boiterie de l'Enfant", "Pédiatrie",
     "Boiterie pédiatrique — arthrite septique de hanche", "S3 Pédiatrie 2025"),
    ("RESCOS-63b - Toux - Pédiatrie - Grille ECOS.html",
     "Toux Chronique", "Pneumologie",
     "Toux du nourrisson — coqueluche", "EF 2026 · Station 4"),
    ("RESCOS-12b_-_Crise_de_panique_-_Grille_ECOS.html",
     "Trouble Anxieux", "Psychiatrie",
     "Crise de panique — trouble panique", "EF 2026 · Station 6"),
]

# Lignes de management relevant des EXAMENS COMPLEMENTAIRES (🔬). Tout le
# reste de la section part dans la prise en charge (💊). Declare par
# identifiant de critere, pour que la lecture soit relisible ligne a ligne.
EXAMENS = {
    "RESCOS-9b": {"m3", "m4"},      # bilan sanguin · imagerie
    "RESCOS-12b": set(),
    "RESCOS-57b": set(),
    "RESCOS-58b": {"m1", "m5"},     # laboratoire · endoscopie et CT
    "RESCOS-63b": {"m3", "m4"},     # prise de sang · radiographie et ultrason
    "RESCOS-67b": {"m1", "m2", "m6"},  # laboratoire · tests thyroïdiens · anti-TPO
    "RESCOS-68b": {"m5", "m6"},     # frottis · dépistage immunologique
    "RESCOS-69b": {"m1"},           # radiographies ou CT
    "RESCOS-70b": {"m4"},           # pas d'imagerie de routine si forme typique
}

# Lignes de synthese : elles notent la maniere, pas un item a couvrir.
SYNTHESE = re.compile(r"en g[ée]n[ée]ral", re.I)

# HARMONISATION DE NOMENCLATURE. Les neuf grilles nomment les memes examens
# de trois facons ; un memento qui les compare a besoin d'un vocabulaire
# constant. Ces reecritures ne touchent QUE le memento : les grilles gardent
# le libelle de leur document officiel.
NOMENCLATURE = [
    (r"^Param[èe]tres inflammatoires \(VS ou CRP\)$", "VS / CRP"),
    (r"^Formule sanguine compl[èe]te$", "FSC"),
]

# Sous-items consecutifs a fondre en un seul (meme raison).
FUSIONS = [(["CRP", "VS"], "VS / CRP"), (["VS", "CRP"], "VS / CRP")]

# Un sous-titre qui repete le nom de son encadre n'apporte rien.
REDONDANTS = {"anamnese", "status", "management", "examen clinique"}


def sans_accent(t):
    t = unicodedata.normalize("NFD", t.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def harmonise(libelles):
    """Applique la table de nomenclature puis les fusions."""
    out = []
    for x in libelles:
        for motif, remplacement in NOMENCLATURE:
            x = re.sub(motif, remplacement, x)
        out.append(x)
    for suite, fusion in FUSIONS:
        i = 0
        while i <= len(out) - len(suite):
            if out[i:i + len(suite)] == suite:
                out[i:i + len(suite)] = [fusion]
            else:
                i += 1
    return out

LEGENDE = """> [!info] Légende
>
> - 📋 = Anamnèse — ce qu'il faut absolument avoir demandé
> - 🩺 = Status — le geste ou le signe qui fait la différence
> - 🔬 = Management : examens complémentaires
> - 💊 = Management : prise en charge attendue
> - 🚨 = urgence
> - 🚩 = red flag à ne jamais rater
> - ⭐️ = SSP ou diagnostic fréquemment rencontré à l'ECOS"""


def propre(frag):
    """Texte visible d'un fragment HTML, reponses du patient retirees.

    Deux formes coexistent : la reponse est le plus souvent dans un
    `<span class="patient-response">`, mais quelques lignes la portent en
    clair entre crochets dans le titre — RESCOS-63b, « Contage [2 grandes
    soeurs...] ». Les crochets sont la convention maison pour une reponse :
    les retirer dans les deux cas.
    """
    frag = re.sub(r'<span class="patient-response">.*?</span>', "", frag, flags=re.S)
    frag = re.sub(r"<[^>]+>", " ", frag)
    txt = re.sub(r"\s+", " ", H.unescape(frag)).strip()
    txt = re.sub(r"\s*\[[^\]]*\]", "", txt)
    return re.sub(r"\s+", " ", txt).strip(" :;·-").strip()


def sections(html):
    """Contenu de chaque section notee, indexe par prefixe de critere."""
    out = {}
    for m in re.finditer(r'<div class="section(?: [^"]*)?">(.*?)(?=<!--|\Z)', html, re.S):
        bloc = m.group(1)
        cids = re.findall(r'id="criteria-([aem])\d+"', bloc)
        if cids:
            out.setdefault(cids[0], bloc)
    return out


def items(bloc):
    """(sous-titre | critere) d'une section, dans l'ordre d'affichage."""
    lignes = []
    motif = re.compile(
        r'<div class="criteria-subheader">(.*?)</div>\s*(?=<div class="criteria-(?:row|subheader)")'
        r'|<div class="criteria-row" id="criteria-(\w+)">')
    positions = [(m.start(), m) for m in motif.finditer(bloc)]
    for i, (pos, m) in enumerate(positions):
        if m.group(1) is not None:
            # un sous-titre peut porter une precision imbriquee (la regle de
            # notation) : seul son intitule interesse le memento
            titre = propre(m.group(1).split("<div")[0])
            if (titre and not titre.lower().startswith("consigne")
                    and sans_accent(titre) not in REDONDANTS):
                lignes.append(("titre", None, titre, None))
            continue
        fin = positions[i + 1][0] if i + 1 < len(positions) else len(bloc)
        corps = bloc[pos:fin]
        t = re.search(r'class="criteria-text">(.*?)<button', corps, re.S)
        if not t:
            continue
        titre = propre(t.group(1))
        titre = re.sub(r"^\d+\.\s*", "", titre)
        if SYNTHESE.search(titre):
            continue
        sous = []
        s = re.search(r'class="sub-criteria">(.*?)</div>', corps, re.S)
        if s and propre(s.group(1)):
            sous.append(propre(s.group(1)))
        sous += [propre(d) for d in
                 re.findall(r'class="detail-text criteria-detail">(.*?)</div>', corps, re.S)]
        titre = harmonise([titre])[0]
        lignes.append(("item", m.group(2), titre, harmonise([x for x in sous if x])))
    return lignes


def encadre(genre, entete, lignes):
    """Un callout Obsidian dont la liste est numerotee a partir de 1."""
    if not any(k == "item" for k, _, _, _ in lignes):
        return None
    out = [f"> [!{genre}] {entete}"]
    numero = 0
    for k, _, titre, sous in lignes:
        if k == "titre":
            out += [">", f"> ##### {titre}"]
            continue
        numero += 1
        out.append(f"> - [ ] **{numero}. {titre}**")
        out += [f"> \t- [ ] {x}" for x in sous]
    return "\n".join(out)


def frontmatter(page, champ, defaut):
    """Champ du frontmatter d'une page SSP du coffre, si le coffre est la."""
    fichier = COFFRE / f"SSP — {page}.md"
    if not fichier.exists():
        return defaut
    m = re.search(rf"^{champ}:\s*(.+)$", fichier.read_text(encoding="utf8"), re.M)
    return m.group(1).strip() if m else defaut


def bloc_cas(fichier, page, specialite_defaut, titre, source):
    chemin = REPO / "cases" / "rescos" / fichier
    html = unicodedata.normalize("NFC", chemin.read_text(encoding="utf8"))
    secs = sections(html[html.index("<body"):])
    grille = fichier.split(" -")[0].split("_-_")[0]

    priorite = frontmatter(page, "priorite", "Standard")
    etoile = " ⭐️" if priorite in ("Top 18", "Haut rendement") else ""

    lien = f"file://{chemin}".replace(" ", "%20")
    out = [f"## {titre}{etoile}", "",
           f"*{grille} · {source}* — [grille interactive](<{lien}>) · [[SSP — {page}]]", ""]

    if "a" in secs:
        bloc = encadre("note", "📋 Anamnèse", items(secs["a"]))
        if bloc:
            out += [bloc, ""]
    if "e" in secs:
        bloc = encadre("tip", "🩺 Status", items(secs["e"]))
        if bloc:
            out += [bloc, ""]
    if "m" in secs:
        lignes = items(secs["m"])
        exam = EXAMENS[grille]
        labo = [l for l in lignes if l[0] == "item" and l[1] in exam]
        soin = [l for l in lignes if l[0] != "item" or l[1] not in exam]
        # dans l'encadre 🔬, le prefixe « Investigations complementaires - »
        # de la grille fait doublon avec l'entete — le retirer quand il reste
        # quelque chose (RESCOS-63b intitule ses deux lignes exactement
        # « Examens complémentaires », sans separateur : elles restent intactes)
        def sans_prefixe(t):
            t = re.sub(r"^(?:Investigations|Examens) compl[ée]mentaires\s*[-–]\s*", "", t)
            return t[:1].upper() + t[1:]   # ne PAS toucher au reste : FSC, VIH, CT…
        labo = [(k, cid, sans_prefixe(t) if k == "item" else t, sous)
                for k, cid, t, sous in labo]
        bloc = encadre("question", "🔬 Examens complémentaires", labo)
        if bloc:
            out += [bloc, ""]
        bloc = encadre("success", "💊 Management", soin)
        if bloc:
            out += [bloc, ""]
    return "\n".join(out).rstrip(), specialite_defaut


if __name__ == "__main__":
    SORTIE.mkdir(parents=True, exist_ok=True)
    for vieux in SORTIE.glob("*.md"):
        vieux.unlink()

    groupes, ordre = {}, []
    nb = 0
    for fichier, page, spec_defaut, titre, source in CAS:
        bloc, _ = bloc_cas(fichier, page, spec_defaut, titre, source)
        specialite = frontmatter(page, "specialite", spec_defaut)
        if specialite not in groupes:
            groupes[specialite] = []
            ordre.append(specialite)
        groupes[specialite].append(bloc)
        nb += bloc.count("- [ ] **")

    corps = []
    for specialite in ordre:
        corps.append(f"# {specialite}")
        corps.append("")
        corps.append("\n\n".join(groupes[specialite]))
        corps.append("")

    doc = f"""---
aliases:
  - Mémento ECOS
type: memento-ecos
source: 9 grilles d'évaluation officielles (entraînements fédéraux 2025-2026)
cas: {len(CAS)}
tags:
  - ecos/memento
  - ecos/grille-officielle
cssclasses:
  - skill-ecos
---

{LEGENDE}

> [!abstract] Ce que contient ce mémento
> Les items d'anamnèse, de status et de management des **neuf grilles
> d'évaluation officielles**, dans leur ordre, **sans barème ni réponses du·de
> la patient·e**. Les seuils (« au moins 3 = oui »), les points et les réponses
> restent dans la grille interactive, liée sous chaque titre.
>
> Quatre grilles ne cotent aucun status : leur encadré 🩺 est absent, ce n'est
> pas un oubli. Le partage du management en 🔬 et 💊 est une lecture, pas une
> distinction de la grille officielle.

{chr(10).join(corps).rstrip()}
"""
    cible = SORTIE / "Mémento ECOS — Grilles officielles.md"
    io.open(cible, "w", encoding="utf8").write(doc)
    print(f"{len(CAS)} cas, {nb} items, {len(ordre)} spécialités → {cible.relative_to(REPO)}")
