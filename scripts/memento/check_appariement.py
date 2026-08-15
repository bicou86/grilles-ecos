"""Comportement de l'appariement sur des cas construits. Sortie 1 si ecart."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_fusion
import lib_rendu

A = {"id": "A", "sections": {"a": [("item", "a1", "1. Caractérisation de la douleur",
                                    ["Localisation", "Irradiation"])]}}
B = {"id": "B", "sections": {"a": [("item", "a1", "Caractérisation de la Douleur",
                                    ["Localisation", "Facteurs déclenchants"])]}}
C = {"id": "C", "sections": {"a": [("item", "a1", "Anamnèse familiale", [])]}}


def verifier_marquage():
    ecarts = []
    diag = {"A": "STEMI", "B": "Péricardite", "C": "Embolie"}
    partout = {"titre": "Localisation", "cas": {"A", "B", "C"}}
    partiel = {"titre": "Soulagement en antéflexion", "cas": {"B"}}
    deux = {"titre": "Facteurs déclenchants", "cas": {"A", "B"}}

    if lib_rendu.marque(partout, 3, diag) != "Localisation":
        ecarts.append("un item porte par tous les cas ne doit pas etre suffixe")
    if lib_rendu.marque(partiel, 3, diag) != "Soulagement en antéflexion *(Péricardite)*":
        ecarts.append(f"suffixe simple errone : {lib_rendu.marque(partiel, 3, diag)}")
    attendu = "Facteurs déclenchants *(Péricardite, STEMI)*"
    if lib_rendu.marque(deux, 3, diag) != attendu:
        ecarts.append(f"suffixe multiple errone : {lib_rendu.marque(deux, 3, diag)}")

    quatre = {"titre": "Dyspnée", "cas": {"A", "B", "C", "D"}}
    d4 = dict(diag, D="Pneumothorax", E="Angor")
    if lib_rendu.marque(quatre, 5, d4) != "Dyspnée *(4 diagnostics)*":
        ecarts.append(f"abreviation au-dela de 3 non appliquee : {lib_rendu.marque(quatre, 5, d4)}")
    return ecarts


def verifier_elision():
    """Un sous-item herite de la portee de son parent : il ne la repete pas.

    Le suffixe n'est reaffiche sur un sous-item que s'il DIFFERE de celui du
    parent — c'est le seul cas ou il apprend quelque chose. Les deux items
    ci-dessous couvrent les deux sens : portee identique (elidee) et portee
    plus etroite que celle du parent (conservee).
    """
    ecarts = []
    diag = {"A": "STEMI", "B": "Péricardite", "C": "Embolie"}
    items = [
        {"titre": "Frottement péricardique", "cas": {"B"},
         "sous": [{"titre": "Auscultation en antéflexion", "cas": {"B"}}]},
        {"titre": "Caractérisation de la douleur", "cas": {"A", "B"},
         "sous": [{"titre": "Irradiation", "cas": {"A"}}]},
    ]
    attendu = "\n".join([
        "> [!note] 📋 Anamnèse",
        "> - [ ] **1. Frottement péricardique *(Péricardite)***",
        "> \t- [ ] Auscultation en antéflexion",
        "> - [ ] **2. Caractérisation de la douleur *(Péricardite, STEMI)***",
        "> \t- [ ] Irradiation *(STEMI)*",
    ])
    rendu = lib_rendu.encadre("note", "📋 Anamnèse", items, 3, diag)
    if rendu != attendu:
        ecarts.append("suffixe herite mal elide — obtenu :\n" + str(rendu))
    return ecarts


def main():
    ecarts = []
    fusion = lib_fusion.apparier([A, B, C], "a")

    titres = [f["titre"] for f in fusion]
    if len(titres) != 2:
        ecarts.append(f"attendu 2 items fusionnes, obtenu {len(titres)} : {titres}")

    douleur = next((f for f in fusion if "douleur" in f["titre"].lower()), None)
    if not douleur:
        ecarts.append("les deux libelles « Caracterisation de la douleur » n'ont pas fusionne")
    else:
        # Les ensembles sont TRIES avant affichage : le repr d'un set de
        # chaines depend de PYTHONHASHSEED, et deux executions d'une meme
        # regression afficheraient sinon le meme ecart dans deux ordres
        # differents — illisible a comparer, et faussement instable.
        if douleur["cas"] != {"A", "B"}:
            ecarts.append(f"cas portes attendus {{A, B}}, obtenu {sorted(douleur['cas'])}")
        sous = {s["titre"] for s in douleur["sous"]}
        if sous != {"Localisation", "Irradiation", "Facteurs déclenchants"}:
            ecarts.append(f"sous-items mal fusionnes : {sorted(sous)}")
        loc = next(s for s in douleur["sous"] if s["titre"] == "Localisation")
        if loc["cas"] != {"A", "B"}:
            ecarts.append("« Localisation » devrait etre porte par A et B")
        irr = next(s for s in douleur["sous"] if s["titre"] == "Irradiation")
        if irr["cas"] != {"A"}:
            ecarts.append("« Irradiation » devrait n'etre porte que par A")

    # La neutralisation porte sur la CLE d'appariement, pas sur le libelle
    # affiche : `canonique()` rend un libelle destine a etre lu, dont la casse
    # et les accents sont ceux du premier cas rencontre (les verifications de
    # sous-items ci-dessus l'exigent : leurs libelles y sont compares au
    # caractere pres). C'est `signature(canonique(...))` qui doit rapprocher
    # les deux libelles.
    if (lib_fusion.signature(lib_fusion.canonique("1. Caractérisation de la douleur"))
            != lib_fusion.signature(lib_fusion.canonique("Caractérisation de la Douleur"))):
        ecarts.append("numerotation et casse devraient etre neutralisees")

    ecarts += verifier_marquage()
    ecarts += verifier_elision()

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — appariement conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
