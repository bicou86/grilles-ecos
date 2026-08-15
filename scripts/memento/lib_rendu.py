"""Rendu Markdown des mementos — callouts Obsidian, cases a cocher imbriquees.

La charte est celle du memento des neuf grilles officielles : legende, titre de
specialite, encadres 📋 / 🩺 / 🔬 / 💊, numerotation repartant a 1 dans chaque
encadre.

MARQUAGE DU SPECIFIQUE. Un item porte par tous les diagnostics de la SSP reste
nu ; un item partiel est suffixe des diagnostics qui le portent. Le surlignage
==…== d'Obsidian a ete ecarte : il colore sans dire pourquoi, depend du theme
et ne survit pas a l'export. Le suffixe est greppable et lisible en clair.

DETERMINISME. `lib_fusion.apparier()` rend des groupes dont le champ `cas` est
un `set` : son ordre d'iteration depend de PYTHONHASHSEED. Tout parcours d'un
`cas` fait ici passe donc par `sorted()` — sans quoi deux executions
produiraient des suffixes dans deux ordres differents, et les fichiers
cesseraient d'etre idempotents.
"""

LEGENDE = """> [!info] Légende
>
> - 📋 = Anamnèse — ce qu'il faut absolument avoir demandé
> - 🩺 = Status — le geste ou le signe qui fait la différence
> - 🔬 = Management : examens complémentaires
> - 💊 = Management : prise en charge attendue
> - 🚨 = urgence
> - 🚩 = red flag à ne jamais rater
> - ⭐️ = SSP ou diagnostic fréquemment rencontré à l'ECOS"""

SEUIL_ABREGE = 3   # au-dela, on compte au lieu d'enumerer


def marque(item, diagnostics_total, diag_par_cas):
    """Suffixe un item des diagnostics qui le portent, s'il n'est pas universel."""
    diags = sorted({diag_par_cas[c] for c in item["cas"] if c in diag_par_cas})
    if not diags or len(diags) >= diagnostics_total:
        return item["titre"]
    if len(diags) > SEUIL_ABREGE:
        return f"{item['titre']} *({len(diags)} diagnostics)*"
    return f"{item['titre']} *({', '.join(diags)})*"


def encadre(genre, entete, items, diagnostics_total, diag_par_cas):
    """Un callout dont la liste est numerotee a partir de 1."""
    if not items:
        return None
    out = [f"> [!{genre}] {entete}"]
    for numero, item in enumerate(items, 1):
        out.append(f"> - [ ] **{numero}. {marque(item, diagnostics_total, diag_par_cas)}**")
        for sous in item["sous"]:
            out.append(f"> \t- [ ] {marque(sous, diagnostics_total, diag_par_cas)}")
    return "\n".join(out)
