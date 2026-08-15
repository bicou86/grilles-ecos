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
import io
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "memento"))
from lib_extraction import (propre, sections, items, harmonise,  # noqa: E402
                            sans_accent, SYNTHESE, NOMENCLATURE,
                            FUSIONS, REDONDANTS)

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

LEGENDE = """> [!info] Légende
>
> - 📋 = Anamnèse — ce qu'il faut absolument avoir demandé
> - 🩺 = Status — le geste ou le signe qui fait la différence
> - 🔬 = Management : examens complémentaires
> - 💊 = Management : prise en charge attendue
> - 🚨 = urgence
> - 🚩 = red flag à ne jamais rater
> - ⭐️ = SSP ou diagnostic fréquemment rencontré à l'ECOS"""


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
    # PAS DE MENAGE PAR GLOB ici. Ce script partage desormais SORTIE avec
    # scripts/memento/build_memento.py, qui y ecrit un memento par SSP :
    # un `SORTIE.glob("*.md")` les effacerait tous a chaque execution — et
    # check_fusion.py relance ce script a chaque controle. Ce generateur
    # n'ecrit qu'un fichier, de nom constant, que l'ecriture finale remplace :
    # il n'a aucune sortie obsolete a balayer. La sortie produite est
    # inchangee, a l'octet pres (empreinte epinglee par check_fusion.py).

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
