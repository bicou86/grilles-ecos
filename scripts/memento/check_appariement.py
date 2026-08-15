"""Comportement de l'appariement sur des cas construits. Sortie 1 si ecart."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction
import lib_fusion
import lib_rendu

A = {"id": "A", "sections": {"a": [("item", "a1", "1. Caractérisation de la douleur",
                                    ["Localisation", "Irradiation"])]}}
B = {"id": "B", "sections": {"a": [("item", "a1", "Caractérisation de la Douleur",
                                    ["Localisation", "Facteurs déclenchants"])]}}
C = {"id": "C", "sections": {"a": [("item", "a1", "Anamnèse familiale", [])]}}


def verifier_marquage():
    """L'invariant : la marque ne doit rien laisser conclure de faux.

    Ce bloc REMPLACE la version du brief, qui raisonnait en nombre de
    diagnostics (`marque(item, diagnostics_total, diag)`). Cette regle-la
    rendait nu un item qu'une partie seulement des grilles portait des lors
    que tous les diagnostics etaient representes, et se taisait completement
    sur une SSP a diagnostic unique. Le parametre est desormais l'ensemble des
    GRILLES de la SSP.
    """
    ecarts = []
    # 4 grilles, 3 diagnostics : B et C portent tous deux la pericardite.
    cas = ["A", "B", "C", "D"]
    diag = {"A": "STEMI", "B": "Péricardite", "C": "Péricardite", "D": "Embolie"}

    def rendu(titre, porteurs, tous=cas, d=diag):
        return lib_rendu.marque({"titre": titre, "cas": set(porteurs)}, tous, d)

    if rendu("Localisation", "ABCD") != "Localisation":
        ecarts.append("un item porte par toutes les grilles doit rester nu")

    # exactement les deux grilles de pericardite -> le diagnostic est fidele
    attendu = "Soulagement en antéflexion *(Péricardite)*"
    if rendu("Soulagement en antéflexion", "BC") != attendu:
        ecarts.append(f"suffixe simple errone : {rendu('Soulagement en antéflexion', 'BC')}")

    # UNE SEULE des deux grilles de pericardite : nommer le diagnostic
    # laisserait croire que l'item est propre a la pericardite. Il ne l'est pas.
    if rendu("Frottement", "B") != "Frottement *(1 grille sur 4)*":
        ecarts.append(f"couverture partielle mal dite : {rendu('Frottement', 'B')}")

    attendu = "Facteurs déclenchants *(Péricardite · STEMI)*"
    if rendu("Facteurs déclenchants", "ABC") != attendu:
        ecarts.append(f"suffixe multiple errone : {rendu('Facteurs déclenchants', 'ABC')}")

    # au-dela de trois diagnostics fideles, on compte
    cas5 = ["A", "B", "C", "D", "E"]
    d5 = {"A": "STEMI", "B": "Péricardite", "C": "Embolie",
          "D": "Pneumothorax", "E": "Angor"}
    if rendu("Dyspnée", "ABCD", cas5, d5) != "Dyspnée *(4 diagnostics)*":
        ecarts.append(f"abreviation au-dela de 3 non appliquee : {rendu('Dyspnée', 'ABCD', cas5, d5)}")

    # SSP a diagnostic unique : le marquage doit rester parlant
    d1 = {"A": "HTA", "B": "HTA"}
    if rendu("Fond d'œil", "A", ["A", "B"], d1) != "Fond d'œil *(1 grille sur 2)*":
        ecarts.append(f"SSP a diagnostic unique muette : {rendu(chr(34)+chr(34), 'A', ['A','B'], d1)}")

    # grille sans diagnostic resolu : aucune conclusion par diagnostic
    d0 = {"A": "STEMI"}
    if rendu("Anamnèse familiale", "B", ["A", "B"], d0) != "Anamnèse familiale *(1 grille sur 2)*":
        ecarts.append("un porteur sans diagnostic ne doit pas etre nomme")
    return ecarts


def verifier_elision():
    """Un sous-item herite de la portee de son parent : il ne la repete pas."""
    ecarts = []
    cas = ["A", "B", "C"]
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
        "> - [ ] **2. Caractérisation de la douleur *(Péricardite · STEMI)***",
        "> \t- [ ] Irradiation *(STEMI)*",
    ])
    rendu = lib_rendu.encadre("note", "📋 Anamnèse", items, cas, diag)
    if rendu != attendu:
        ecarts.append("suffixe herite mal elide — obtenu :\n" + str(rendu))
    return ecarts


def verifier_invariant_sous_items():
    """Le filtre des reponses ne vide JAMAIS un item de tous ses sous-items.

    Garantie STRUCTURELLE, pas heuristique : quand toute l'enumeration se lit
    comme une reponse, c'est qu'elle EST l'information que l'item annonce
    (« Recherche de signes d'insuffisance hepatocellulaire » suivi de ses six
    signes). Le bloc HTML ci-dessous est celui, minimal, que `items()` sait
    lire ; ses trois sous-criteres sont tous des reponses.
    """
    ecarts = []
    bloc = ('<div class="criteria-row" id="criteria-e1">'
            '<div class="criteria-text">Signes d\'hypertension portale<button>'
            '</button></div>'
            '<div class="detail-text criteria-detail">Pas d\'ascite</div>'
            '<div class="detail-text criteria-detail">Pas de splénomégalie</div>'
            '<div class="detail-text criteria-detail">Circulation collatérale normale</div>')
    lignes = lib_extraction.items(bloc)
    if not lignes:
        return ["le bloc de controle n'a produit aucun item"]
    _, _, titre, sous = lignes[0]
    if len(sous) != 3:
        ecarts.append(f"l'item a ete vide de ses sous-items : {titre!r} -> {sous}")
    return ecarts


def verifier_nettoyage():
    """Glyphes decoratifs et enonciateur a la 3e personne sont retires."""
    ecarts = []
    for brut, attendu in (("⊕ Facteurs aggravants", "Facteurs aggravants"),
                          ("Facteurs soulageants ⊖", "Facteurs soulageants"),
                          ("L'étudiant évoque le toucher rectal",
                           "Évoque le toucher rectal"),
                          ("Localisation", "Localisation")):
        obtenu = lib_rendu.nettoie_libelle(brut)
        if obtenu != attendu:
            ecarts.append(f"nettoyage errone : {brut!r} -> {obtenu!r}")
    return ecarts


def verifier_reponses_patient():
    """Les reponses du·de la patient·e ne sont pas des sous-criteres a cocher."""
    ecarts = []
    for libelle in ("TA 138/85 mmHg", "Pas de turgescence jugulaire",
                    "Murmure vésiculaire normal", "Absence de fièvre",
                    "Température 36.5°C"):
        if not lib_extraction.reponse_patient(libelle):
            ecarts.append(f"reponse non reconnue : {libelle!r}")
    # epargnes : seuil entre parentheses, echelle introduite par « : », et
    # « Sans… », volontairement hors du motif
    for libelle in ("Interprétation du test (chute ≥20/10 mmHg)",
                    "Normal: 0.9-1.3", "Classe I: Activités quotidiennes normales",
                    "Sans correction", "Bêtabloquant (bisoprolol 5mg/j)",
                    "Localisation"):
        if lib_extraction.reponse_patient(libelle):
            ecarts.append(f"libelle legitime ecarte a tort : {libelle!r}")
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
    ecarts += verifier_nettoyage()
    ecarts += verifier_reponses_patient()
    ecarts += verifier_invariant_sous_items()

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — appariement conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
