"""Fige les champs du coffre Obsidian dont les mementos dependent. Sortie 0/1.

    python3 scripts/memento/fige_coffre.py            # ecrit docs/ecos-ssp-coffre.yaml
    python3 scripts/memento/fige_coffre.py --verifie  # ne compare que, n'ecrit rien

POURQUOI. `lib_ssp.specialite()` et `lib_ssp.priorite()` lisaient les pages
« SSP — *.md » du coffre Obsidian, sous ~/Documents/..., HORS DEPOT. Or ces deux
champs entrent dans les octets des mementos VERSIONNES : `specialite` au
frontmatter et en fil d'Ariane, `priorite` dans l'etoile ⭐️. Mesure, avec HOME
pointe sur un dossier vide : 74 des 89 mementos changent.

ET L'ECHEC ETAIT PIRE QU'UN ECHEC. `check_mementos.py` APPELLE le generateur
avant de comparer : sur un clone frais, il reecrivait les 74 fichiers en version
degradee — sans `specialite:`, sans etoile — puis les declarait en ecart. Un
utilisateur presse commitait la degradation.

C'est le meme defaut que celui d'AZYGOS, sur le meme axe, et il recoit le meme
remede : le DEPOT porte l'instantane, le COFFRE reste la source de
rafraichissement. La difference avec AZYGOS est qu'ici rien n'oblige a projeter
— aucun jeton, aucun texte tiers — mais l'instantane reste volontairement
limite aux DEUX champs que la chaine lit (`lib_ssp.CHAMPS_COFFRE`) : recopier
les red_flags, les alias et le reste ferait du depot un miroir du coffre, qu'il
faudrait alors maintenir.

TOUTES LES PAGES SONT FIGEES, y compris celles dont aucun champ n'est rempli et
celles qu'aucune grille ne rattache. La presence d'un groupe SIGNIFIE « la page
existe », et c'est une information que `check_priorites.py` consomme (« pages
SSP a creer »). Un instantane reduit aux SSP du corpus rendrait ce rapport-la
faux, et le rendrait faux en silence.

LA REGLE DE LECTURE N'EST PAS RECOPIEE : `lib_ssp.champ_texte()` est appelee
ici, pour que l'instantane ne puisse pas cesser de valoir la page sans que le
lecteur change de la meme facon.

DETERMINISME : pages triees, champs dans l'ordre de `lib_ssp.CHAMPS_COFFRE`,
aucune date, aucun aleatoire.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_ssp                                            # noqa: E402
import lib_yaml                                           # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SORTIE = lib_ssp.INSTANTANE
ENTETE = """\
# Instantané des champs du coffre Obsidian dont les mémentos dépendent.
#
# NE PAS ÉDITER À LA MAIN. Régénérer avec :
#     python3 scripts/memento/fige_coffre.py
#
# La source est « SSP ECOS/SSP — <nom>.md » dans le coffre, hors dépôt. Ce
# fichier existe pour que les 89 mémentos versionnés soient reproductibles sur
# une machine qui n'a pas le coffre — sans lui, 74 d'entre eux se régénéraient
# dégradés (ni « specialite: » au frontmatter, ni étoile ⭐️).
#
# Un groupe présent = la page existe dans le coffre. Un champ absent du groupe
# = le champ est absent de la page ; le lecteur rend alors son défaut
# (« Non classé » / « Standard »), exactement comme avant.
"""


def collecte():
    """SSP -> {champ: valeur}, lu du coffre. {} si le coffre est absent."""
    if not lib_ssp.COFFRE.is_dir():
        return None
    out = {}
    for page in sorted(lib_ssp.COFFRE.glob("SSP — *.md")):
        nom = page.name[len("SSP — "):-len(".md")]
        texte = page.read_text(encoding="utf8")
        champs = {}
        for champ in lib_ssp.CHAMPS_COFFRE:
            valeur = lib_ssp.champ_texte(texte, champ)
            if valeur:
                champs[champ] = valeur
        out[nom] = champs
    return out


def rendu(table):
    """Le texte exact du fichier, pour ecrire et comparer par le meme chemin."""
    lignes = [ENTETE.rstrip("\n")]
    for ssp in sorted(table):
        lignes.append(f'"{ssp}":')
        for champ in lib_ssp.CHAMPS_COFFRE:
            if champ in table[ssp]:
                lignes.append(f'  {champ}: "{table[ssp][champ]}"')
    return "\n".join(lignes) + "\n"


def traite(verifie):
    """(ecarts, nombre de pages). `verifie=True` ne touche a rien."""
    table = collecte()
    if table is None:
        return [f"le coffre est absent ({lib_ssp.COFFRE}) : impossible de "
                "rafraichir l'instantane"], 0
    texte = rendu(table)
    if not verifie:
        SORTIE.write_text(texte, encoding="utf8")
        return [], len(table)
    if not SORTIE.exists():
        return [f"{SORTIE.name} est absent du dépôt"], len(table)
    if SORTIE.read_text(encoding="utf8") != texte:
        # Nommer les SSP qui divergent : « le fichier differe » n'aide personne
        # a decider s'il faut rafraichir ou s'inquieter.
        avant = lib_yaml.lire_groupe(SORTIE)
        noms = sorted(set(avant) ^ set(table)) or \
            sorted(s for s in table if avant.get(s) != table[s])
        return [f"{SORTIE.name} ne correspond plus au coffre — "
                f"{len(noms)} SSP concernée(s) : {noms[:6]}"], len(table)
    return [], len(table)


def main():
    argv = sys.argv[1:]
    if argv and argv != ["--verifie"]:
        print(f"Argument non reconnu : {' '.join(argv)}\n"
              "Usage : fige_coffre.py [--verifie]")
        return 1
    verifie = bool(argv)
    ecarts, total = traite(verifie)
    if ecarts:
        print("ÉCHEC —", len(ecarts), "écart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print(f"OK — {total} pages SSP {'vérifiées' if verifie else 'figées'} "
          f"→ {SORTIE.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
