"""Fige l'extraction AZYGOS locale en une source versionnee du depot. Sortie 0/1.

    python3 scripts/memento/fige_azygos.py            # ecrit docs/azygos-grilles/
    python3 scripts/memento/fige_azygos.py --verifie  # ne compare que, n'ecrit rien

POURQUOI. La chaine des mementos lisait `.azygos-extraction/*.json`, un dossier
IGNORE PAR GIT : un clone frais ne pouvait pas reconstruire les mementos, et
`check_azygos.py` y echouait des la premiere ligne. Le brief de la tache 11
offrait deux issues, `git add -f` ou recopier les champs utiles. La premiere est
ecartee sur une raison concrete : les 49 fichiers bruts portent 43 URL signees
Supabase dont la query-string contient un JWT. Les versionner reviendrait a
commiter 43 jetons dans un historique irreversible — et, accessoirement, chaque
re-extraction en produirait de nouveaux, si bien que le diff d'une mise a jour
serait noye dans du bruit de jeton.

CE QUE LE MIROIR GARDE, ET RIEN DE PLUS : `meta` (url de provenance, id, titre)
et, par onglet, le nom de groupe et le `label` de chaque item. C'est exactement
ce que `lire_azygos()` et `classifie_onglets()` lisent. Sont laisses au brut :

  - `images` — les URL signees, avec leurs jetons ;
  - `infos` — les paves didactiques d'AZYGOS, que `lire_azygos` ne reprend
    deja pas (docstring de `lire_azygos`), et dont le miroir n'a que faire ;
  - `valeurs` des items — les reponses du·de la patient·e, pas des criteres ;
  - `ordre`, `nbInfos` — de l'affichage.

1,46 Mo bruts deviennent 0,29 Mo, sans jeton, sans texte pedagogique tiers :
il ne reste que les libelles de criteres, c'est-a-dire ce que `cases/*.html`
versionne deja pour les trois autres corpus.

TOUS LES NOMS D'ONGLET SONT CONSERVES, y compris ceux qu'ONGLETS_AZYGOS_EXCLUS
ecarte. C'est deliberement redondant : `classifie_onglets()` signale les onglets
INCONNUS, et un miroir qui n'aurait garde que les onglets reconnus rendrait ce
garde-fou VIDE — il passerait au vert sans jamais avoir rien a examiner.

LA FIDELITE EST PROUVEE, PAS SUPPOSEE : le script compare `lire_azygos(brut)` et
`lire_azygos(miroir)` sur les 49 fichiers, au champ `fichier` pres (qui est le
chemin, et qui change par construction). `check_azygos.py` rejoue la meme
comparaison quand le brut est present.

DETERMINISME : l'ordre des onglets est celui du fichier brut et il compte —
`lire_azygos` empile les sections dans cet ordre. Aucun tri de cle, aucune date.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L                                # noqa: E402

REPO = Path(__file__).resolve().parents[2]
BRUT = REPO / ".azygos-extraction"
MIROIR = REPO / "docs" / "azygos-grilles"


def projette(donnees):
    """Le sous-ensemble du JSON brut que la chaine des mementos lit reellement."""
    meta = donnees.get("meta", {})
    onglets = {}
    for nom, groupes in donnees.get("onglets", {}).items():
        garde = []
        for groupe in groupes:
            if not isinstance(groupe, dict):
                continue
            garde.append({
                "groupe": groupe.get("groupe", ""),
                "items": [{"label": item.get("label", "")}
                          for item in groupe.get("items", [])],
            })
        onglets[nom] = garde
    return {
        "meta": {cle: meta[cle] for cle in ("url", "id", "titre") if cle in meta},
        "onglets": onglets,
    }


def rendu(donnees):
    """Le texte exact ecrit dans le miroir, pour ecrire et comparer par le meme chemin."""
    return json.dumps(donnees, ensure_ascii=False, indent=1, sort_keys=False) + "\n"


def _sans_chemin(cas):
    return {cle: valeur for cle, valeur in cas.items() if cle != "fichier"}


def traite(verifie):
    """(ecarts, nombre de bruts, nombre de fichiers reecrits).

    `verifie=True` ne touche a rien et se contente de comparer — c'est la forme
    qu'appelle check_azygos.py, qui ne doit jamais reecrire une source pendant
    qu'il la controle.
    """
    bruts = sorted(BRUT.glob("*.json"))
    if not bruts:
        return [f"{BRUT.name}/ est vide ou absent ; rejouer scripts/azygos/extract.js "
                "(cf. PROCEDURE-azygos.md)"], 0, 0

    MIROIR.mkdir(parents=True, exist_ok=True)
    ecarts, ecrits = [], 0
    for source in bruts:
        cible = MIROIR / source.name
        texte = rendu(projette(json.loads(source.read_text(encoding="utf8"))))
        if verifie:
            if not cible.exists():
                ecarts.append(f"{source.name} : absent du miroir")
                continue
            if cible.read_text(encoding="utf8") != texte:
                ecarts.append(f"{source.name} : miroir different du brut")
                continue
        else:
            if not cible.exists() or cible.read_text(encoding="utf8") != texte:
                cible.write_text(texte, encoding="utf8")
                ecrits += 1
        # La preuve : le cas pivot doit etre le meme des deux cotes.
        if cible.exists() and _sans_chemin(L.lire_azygos(source)) != \
                _sans_chemin(L.lire_azygos(cible)):
            ecarts.append(f"{source.name} : le cas pivot differe entre brut et miroir")

    orphelins = sorted(p.name for p in MIROIR.glob("*.json")
                       if not (BRUT / p.name).exists())
    if orphelins:
        ecarts.append(f"{len(orphelins)} fichier(s) du miroir sans brut correspondant : "
                      f"{orphelins[:5]}")
    return ecarts, len(bruts), ecrits


def main():
    argv = sys.argv[1:]
    if argv and argv != ["--verifie"]:
        print(f"Argument non reconnu : {' '.join(argv)}\n"
              "Usage : fige_azygos.py [--verifie]")
        return 1
    verifie = bool(argv)

    ecarts, total, ecrits = traite(verifie)
    if ecarts:
        print("ÉCHEC —", len(ecarts), "écart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    action = "vérifiés" if verifie else f"figés ({ecrits} réécrit(s))"
    print(f"OK — {total} fichiers AZYGOS {action}, cas pivot identique au brut")
    return 0


if __name__ == "__main__":
    sys.exit(main())
