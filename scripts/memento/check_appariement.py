"""Comportement de l'appariement sur des cas construits. Sortie 1 si ecart.

Une seule verification part du corpus reel et non de cas construits :
`verifier_attendus_du_corpus()`. Elle garde la jointure entre le libelle de
diagnostic de la table de priorites et celui que la table des diagnostics
resout, parce qu'aucun cas construit ne peut la surveiller.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction
import lib_fusion
import lib_rendu
import lib_ssp

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
            '<div class="detail-text criteria-detail">Foie de taille normale</div>'
            '<div class="detail-text criteria-detail">Rate normale non palpable</div>'
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
    # valeur chiffree et constat de normalite : reponses dans les DEUX sections
    for section in ("a", "e"):
        for libelle in ("TA 138/85 mmHg", "Murmure vésiculaire normal",
                        "Température 36.5°C"):
            if not lib_extraction.reponse_patient(libelle, section):
                ecarts.append(f"reponse non reconnue en {section} : {libelle!r}")
    # negation : une reponse en ANAMNESE, un signe cherche en STATUS
    for libelle in ("Pas de voyage récent", "Absence de fièvre",
                    "Pas d'hépatite connue"):
        if not lib_extraction.reponse_patient(libelle, "a"):
            ecarts.append(f"negation d'anamnese non reconnue : {libelle!r}")
    for libelle in ("Pas de frottement péricardique", "Pas de galop",
                    "Pas de splénomégalie", "Pas d'angiomes stellaires"):
        if lib_extraction.reponse_patient(libelle, "e"):
            ecarts.append(f"signe cherche a l'examen ecarte a tort : {libelle!r}")
    # epargnes : seuil entre parentheses, echelle introduite par « : », et
    # « Sans… », volontairement hors du motif
    for libelle in ("Interprétation du test (chute ≥20/10 mmHg)",
                    "Normal: 0.9-1.3", "Classe I: Activités quotidiennes normales",
                    "Sans correction", "Bêtabloquant (bisoprolol 5mg/j)",
                    "Localisation"):
        if lib_extraction.reponse_patient(libelle, "a"):
            ecarts.append(f"libelle legitime ecarte a tort : {libelle!r}")
    return ecarts


def _cas_m(cid, titres):
    """Un cas construit reduit a sa section management."""
    return {"id": cid, "sections": {"m": [("item", f"m{i}", t, [])
                                          for i, t in enumerate(titres, 1)]}}


def verifier_management():
    """Le management se scinde en partage et en sous-blocs par diagnostic.

    Ce bloc ETEND celui du brief (deux cas, deux diagnostics, aucun attendu)
    des situations que les decisions successives ont introduites : un
    diagnostic attendu sans grille, un diagnostic dont tout le management est
    partage, et surtout LE SEUIL A DEUX (ronde 1) — un item porte par deux
    diagnostics sur trois monte dans le partage au lieu d'etre recopie dans
    deux sous-blocs.
    """
    ecarts = []
    cas = [_cas_m("A", ["Hypothèses diagnostiques", "Aspirine + P2Y12"]),
           _cas_m("B", ["Hypothèses diagnostiques", "AINS et colchicine"])]
    diag = {"A": "STEMI", "B": "Péricardite"}
    partage, propres = lib_fusion.scinder_management(cas, diag, None)

    if [c["titre"] for c in partage] != ["Hypothèses diagnostiques"]:
        ecarts.append(f"le partage devrait etre le seul item commun : {[c['titre'] for c in partage]}")
    if set(propres) != {"STEMI", "Péricardite"}:
        ecarts.append(f"sous-blocs attendus STEMI et Pericardite : {sorted(propres)}")
    if [i["titre"] for i in propres.get("STEMI", [])] != ["Aspirine + P2Y12"]:
        ecarts.append("le sous-bloc STEMI est faux")

    # UN DIAGNOSTIC ATTENDU SANS GRILLE reste un sous-bloc, vide : c'est la
    # lacune de revision que le memento doit nommer, pas taire.
    partage, propres = lib_fusion.scinder_management(
        cas, diag, None, ["STEMI", "Péricardite", "Dissection aortique"])
    if propres.get("Dissection aortique") != []:
        ecarts.append("un diagnostic attendu sans grille doit produire un sous-bloc vide : "
                      f"{propres.get('Dissection aortique')!r}")
    if [c["titre"] for c in partage] != ["Hypothèses diagnostiques"]:
        ecarts.append("les attendus ne doivent pas changer le partage")

    # UN DIAGNOSTIC DONT TOUT LE MANAGEMENT EST PARTAGE rend une liste vide,
    # elle aussi : c'est au rendu de distinguer les trois vides, en lisant
    # `diag_par_cas` et les sections. Sans cette entree, le generateur ne
    # pourrait pas dire « tout figure dans le partage » plutot que « aucune
    # grille ».
    tout_partage = [_cas_m("A", ["Filet de sécurité"]), _cas_m("B", ["Filet de sécurité"])]
    _, propres = lib_fusion.scinder_management(tout_partage, diag, None, ["STEMI"])
    if propres.get("STEMI") != [] or propres.get("Péricardite") != []:
        ecarts.append(f"un diagnostic entierement partage doit rendre une liste vide : {propres}")

    # LE SEUIL EST DEUX, PAS TOUS. Un item porte par deux diagnostics sur
    # trois monte dans le partage ; l'ancienne regle (« porte par TOUS ») le
    # recopiait dans les deux sous-blocs, et ne se declenchait que sur 2 des
    # 23 SSP a plusieurs diagnostics.
    trois = [_cas_m("A", ["Anticoagulation"]), _cas_m("B", ["Anticoagulation"]),
             _cas_m("C", ["Corticoïdes"])]
    d3 = {"A": "STEMI", "B": "Péricardite", "C": "Embolie"}
    partage, propres = lib_fusion.scinder_management(trois, d3, None)
    if [c["titre"] for c in partage] != ["Anticoagulation"]:
        ecarts.append(f"un item porte par 2 diagnostics sur 3 doit monter dans le partage : {partage}")
    if propres.get("STEMI") != [] or propres.get("Péricardite") != []:
        ecarts.append("un item monte dans le partage ne doit plus etre recopie dans les sous-blocs")
    if [i["titre"] for i in propres.get("Embolie", [])] != ["Corticoïdes"]:
        ecarts.append("un item propre a un seul diagnostic doit rester dans son sous-bloc")

    # AUCUN ITEM NE DOIT DISPARAITRE quand aucune grille porteuse n'a de
    # diagnostic resolu : la formule du brief (`if porteurs and ...`) l'aurait
    # laisse tomber dans le vide — ni partage, ni sous-bloc. C'est aussi la
    # raison pour laquelle le test s'ecrit `len(porteurs) != 1` et non `>= 2`.
    orphelin = [_cas_m("A", ["Réévaluation à 48 h"])]
    partage, propres = lib_fusion.scinder_management(orphelin, {}, None)
    if [c["titre"] for c in partage] != ["Réévaluation à 48 h"]:
        ecarts.append(f"un item sans diagnostic porteur a ete perdu : {partage} / {propres}")
    return ecarts


def verifier_marque_partage():
    """Dans l'encadre partage, le suffixe NOMME les diagnostics, sans abreger.

    `marque()` compte au-dela de trois diagnostics (« *(8 diagnostics)* ») :
    appliquee au partage, elle effacerait exactement l'information que les
    huit sous-blocs recopies portaient. Elle se rabat aussi sur un compte de
    grilles des que les porteurs ne sont pas EXACTEMENT toutes les grilles des
    diagnostics concernes — 47 des 92 items partages du corpus.
    """
    ecarts = []
    cas = ["A", "B", "C", "D", "E"]
    diag = {"A": "STEMI", "B": "Péricardite", "C": "Embolie",
            "D": "Pneumothorax", "E": "Angor"}

    def rendu(titre, porteurs):
        return lib_rendu.marque_partage({"titre": titre, "cas": set(porteurs)}, cas, diag)

    if rendu("Antalgie", "ABCDE") != "Antalgie":
        ecarts.append("un item porte par toutes les grilles doit rester nu")

    # quatre diagnostics : `marque()` aurait ecrit « *(4 diagnostics)* »
    attendu = "Oxygène *(Embolie · Pneumothorax · Péricardite · STEMI — 4 grilles sur 5)*"
    if rendu("Oxygène", "ABCD") != attendu:
        ecarts.append(f"abreviation non levee dans le partage : {rendu('Oxygène', 'ABCD')}")
    if lib_rendu.marque({"titre": "Oxygène", "cas": set("ABCD")}, cas, diag) \
            != "Oxygène *(4 diagnostics)*":
        ecarts.append("marque() ne doit PAS changer : elle abrege toujours au-dela de trois")

    # porteurs qui ne couvrent pas toutes les grilles d'un diagnostic :
    # `marque()` se tairait sur les noms, `marque_partage()` les donne.
    diag2 = {"A": "STEMI", "B": "STEMI", "C": "Embolie"}
    cas2 = ["A", "B", "C"]
    item = {"titre": "Héparine", "cas": {"A", "C"}}
    if lib_rendu.marque_partage(item, cas2, diag2) != "Héparine *(Embolie · STEMI — 2 grilles sur 3)*":
        ecarts.append(f"noms perdus dans le partage : {lib_rendu.marque_partage(item, cas2, diag2)}")
    if lib_rendu.marque(item, cas2, diag2) != "Héparine *(2 grilles sur 3)*":
        ecarts.append("marque() ne doit PAS changer : elle refuse de nommer ici")

    # aucun diagnostic a nommer : repli explicite sur `marque()`
    if lib_rendu.marque_partage({"titre": "Suivi", "cas": {"A"}}, cas2, {}) != "Suivi *(1 grille sur 3)*":
        ecarts.append("sans diagnostic resolu, le partage doit se replier sur marque()")
    return ecarts


def verifier_restriction():
    """Dans un sous-bloc, le compte de grilles est celui du diagnostic.

    Sans restriction, « 3 grilles sur 2 » : `marque()` comparerait des
    porteurs comptes sur toute la SSP a un denominateur compte sur le seul
    diagnostic. La restriction retire aussi les sous-items qu'aucune grille du
    diagnostic ne porte — un sous-item a « 0 grille sur 2 » ne veut rien dire.
    """
    ecarts = []
    items = [{"titre": "Anticoagulation", "cas": {"A", "B", "C"},
              "sous": [{"titre": "HBPM", "cas": {"A"}},
                       {"titre": "Relais AVK", "cas": {"C"}}]}]
    vue = lib_fusion.restreindre(items, ["A", "B"])
    if len(vue) != 1 or vue[0]["cas"] != {"A", "B"}:
        ecarts.append(f"restriction des porteurs erronee : {vue}")
    elif [s["titre"] for s in vue[0]["sous"]] != ["HBPM"]:
        ecarts.append(f"sous-item hors diagnostic non retire : {vue[0]['sous']}")
    if lib_fusion.restreindre(items, ["Z"]) != []:
        ecarts.append("un item qu'aucune grille cible ne porte doit disparaitre de la vue")
    # l'original n'est pas modifie : la meme liste sert plusieurs sous-blocs
    if items[0]["cas"] != {"A", "B", "C"} or len(items[0]["sous"]) != 2:
        ecarts.append("restreindre() a modifie les items d'origine")

    rendu = lib_rendu.encadre("success", "💊", vue, ["A", "B"], {"A": "TVP", "B": "TVP"})
    if rendu != "> [!success] 💊\n> - [ ] **1. Anticoagulation**\n> \t- [ ] HBPM *(1 grille sur 2)*":
        ecarts.append("marquage errone dans un sous-bloc restreint :\n" + str(rendu))
    return ecarts


def verifier_restriction_au_point_d_appel():
    """Retirer `restreindre()` de `blocs_management` doit faire echouer un controle.

    Le bloc precedent teste la FONCTION ; celui-ci teste son APPEL. Sans lui,
    supprimer `lib_fusion.restreindre(...)` dans `build_memento` passait tous
    les controles : le decoupage a deux diagnostics n'envoie dans un sous-bloc
    que des items dont tous les porteurs diagnostiques valent ce
    diagnostic-la, si bien que la restriction y est l'identite… SAUF quand une
    grille SANS diagnostic resolu porte le meme item. C'est ce cas-la, le seul
    qui subsiste, que le montage ci-dessous reproduit : STEMI a DEUX grilles,
    une seule porte « Coronarographie », et une troisieme grille sans
    diagnostic la porte aussi. Sans restriction : « 2 grilles sur 2 », ce qui
    est faux.
    """
    import build_memento as B

    ecarts = []
    cas = [_cas_m("A", ["Aspirine"]),
           _cas_m("B", ["Aspirine", "Coronarographie"]),
           _cas_m("C", ["Coronarographie"])]
    obtenu = B.blocs_management(cas, ["A", "B", "C"], {"A": "STEMI", "B": "STEMI"}, None, ())
    attendu = ["> [!success] 💊 Management — si STEMI\n"
               "> - [ ] **1. Aspirine**\n"
               "> - [ ] **2. Coronarographie *(1 grille sur 2)***"]
    if obtenu != attendu:
        ecarts.append("restriction non appliquee au point d'appel — obtenu :\n"
                      + "\n\n".join(obtenu))
    return ecarts


def verifier_mention():
    """Un encadre sans item rend sa mention, et rien si aucune n'est fournie."""
    ecarts = []
    if lib_rendu.encadre("success", "💊 — si X", [], ["A"], {}) is not None:
        ecarts.append("un encadre vide sans mention doit rester absent")
    attendu = "> [!success] 💊 — si X\n> *rien à dire*"
    obtenu = lib_rendu.encadre("success", "💊 — si X", [], ["A"], {}, mention="*rien à dire*")
    if obtenu != attendu:
        ecarts.append(f"mention mal rendue : {obtenu!r}")
    return ecarts


def verifier_sous_blocs():
    """Les cinq sortes de sous-bloc 💊, rendues au caractere pres.

    Trois SSP construites, parce que les mentions ne peuvent pas toutes
    coexister : des qu'un diagnostic ne cote aucun management, plus aucun de
    ses items ne peut monter dans le partage, donc personne n'est « tout
    partage ». C'est le piege qu'une premiere version a paye — elle renvoyait
    AZYGOS-4 (HypoTA orthostatique, sans section management) vers « l'encadre
    ci-dessus », qui n'existait pas.
    """
    import build_memento as B

    # CINQ GRILLES, QUATRE PORTEUSES DE L'ITEM PARTAGE : le montage est choisi
    # pour que `marque()` et `marque_partage()` DIVERGENT visiblement sur cette
    # ligne — la premiere abrege en « *(4 diagnostics)* », la seconde les
    # nomme. Avec un item porte par toutes les grilles, les deux rendaient un
    # libelle nu et retirer `marquage=` du point d'appel passait inapercu.
    # « Péricardite » avant « Pneumothorax » verifie au passage le tri sans
    # accent : trie sur les points de code, « é » passerait apres « n ».
    ecarts = []
    cas = [_cas_m("A", ["Hypothèses diagnostiques", "Aspirine + P2Y12"]),
           _cas_m("B", ["Hypothèses diagnostiques", "AINS et colchicine"]),
           _cas_m("C", ["Hypothèses diagnostiques"]),
           _cas_m("D", ["Hypothèses diagnostiques", "Drainage thoracique"]),
           _cas_m("E", ["Test d'effort"])]
    diag = {"A": "STEMI", "B": "Péricardite", "C": "Embolie",
            "D": "Pneumothorax", "E": "Angor"}
    attendu = [
        "> [!success] 💊 Management — partagé par plusieurs diagnostics\n"
        "> - [ ] **1. Hypothèses diagnostiques "
        "*(Embolie · Pneumothorax · Péricardite · STEMI — 4 grilles sur 5)***",
        "> [!success] 💊 Management — si Angor\n> - [ ] **1. Test d'effort**",
        f"> [!success] 💊 Management — si Dissection aortique\n> {B.SANS_GRILLE}",
        f"> [!success] 💊 Management — si Embolie\n> {B.TOUT_PARTAGE}",
        "> [!success] 💊 Management — si Péricardite\n> - [ ] **1. AINS et colchicine**",
        "> [!success] 💊 Management — si Pneumothorax\n> - [ ] **1. Drainage thoracique**",
        "> [!success] 💊 Management — si STEMI\n> - [ ] **1. Aspirine + P2Y12**",
    ]
    obtenu = B.blocs_management(cas, ["A", "B", "C", "D", "E"], diag, None,
                                ["STEMI", "Péricardite", "Dissection aortique"])
    if obtenu != attendu:
        ecarts.append("sous-blocs 💊 errones — obtenu :\n" + "\n\n".join(obtenu))

    # UN DIAGNOSTIC DOCUMENTE PAR UNE AUTRE SSP n'est pas un trou du corpus :
    # le sous-bloc y renvoie. La SSP porteuse qui n'aura pas de memento dans
    # cette execution est NOMMEE, pas liee — un lien non resolu proposerait de
    # creer une page vide au premier clic.
    obtenu = B.blocs_management(
        cas, ["A", "B", "C", "D", "E"], diag, "Douleur Thoracique", ["Dissection aortique"],
        ailleurs={"Dissection aortique": {"Douleur Abdominale": 3, "Amaurose": 1},
                  "STEMI": {"Douleur Thoracique": 1}},
        rendues={"Douleur Abdominale"})
    renvois = ("[[Mémento — Douleur Abdominale]] (3 grilles) · "
               "« Amaurose » (1 grille, hors lot)")
    attendu_renvoi = ("> [!success] 💊 Management — si Dissection aortique\n> "
                      + B.AILLEURS.format(renvois=renvois))
    if attendu_renvoi not in obtenu:
        ecarts.append("renvoi vers la SSP qui documente le diagnostic errone — obtenu :\n"
                      + "\n\n".join(obtenu))

    # UNE GRILLE SANS SECTION MANAGEMENT (le cas AZYGOS-4) : son diagnostic
    # garde un sous-bloc, qui dit pourquoi il est vide sans renvoyer vers un
    # encadre inexistant.
    muet = [_cas_m("A", ["Aspirine + P2Y12"]), {"id": "B", "sections": {}}]
    obtenu = B.blocs_management(muet, ["A", "B"], {"A": "STEMI", "B": "HypoTA"}, None, ())
    # Aucun encadre partage ici : aucun item n'est porte par deux diagnostics.
    attendu = [
        f"> [!success] 💊 Management — si HypoTA\n> {B.SANS_MANAGEMENT}",
        "> [!success] 💊 Management — si STEMI\n> - [ ] **1. Aspirine + P2Y12**",
    ]
    if obtenu != attendu:
        ecarts.append("sous-bloc d'un diagnostic sans management errone — obtenu :\n"
                      + "\n\n".join(obtenu))
    return ecarts


def verifier_tri_clinique():
    """Les sous-blocs se trient sans accent ni casse, pas sur les points de code.

    `sorted()` brut placait « Pyélonéphrite » avant « Péritonite » et « DMLA »
    avant « Décollement de rétine » : neuf mementos sur trente-deux mal ranges,
    et l'ordre compte precisement la ou il y a vingt boites a parcourir.
    """
    import build_memento as B

    ecarts = []
    noms = ["Pyélonéphrite", "Péritonite", "DMLA", "Décollement de rétine",
            "MICI (Crohn / RCUH)", "Maladie cœliaque"]
    attendu = ["Décollement de rétine", "DMLA", "Maladie cœliaque",
               "MICI (Crohn / RCUH)", "Péritonite", "Pyélonéphrite"]
    obtenu = sorted(noms, key=B.tri_clinique)
    if obtenu != attendu:
        ecarts.append(f"tri des diagnostics errone : {obtenu}")
    return ecarts


def verifier_renvoi_hors_lot():
    """Un diagnostic que seules des SSP HORS LOT documentent doit rester un renvoi.

    L'index des porteuses se calcule sur le CORPUS ENTIER, le rendu sur le
    LOT : le remplacer par un index du lot seul transformerait en « trou de
    revision » huit diagnostics que le corpus documente bel et bien — le
    « Fracture du bassin (hemorragique) » de « Chute & Évaluation
    Geriatrique » n'est porte que par « AVP (Accident de la Voie Publique) »,
    qui n'est pas du lot prioritaire.

    LE CONTROLE NE FIGE AUCUN LIBELLE DE DONNEE : il recalcule les couples
    (SSP, diagnostic) concernes depuis le corpus et exige que le memento rendu
    ne leur oppose pas la mention « aucune grille du corpus ». S'il n'en existe
    aucun un jour, le controle est vide et le dit — il ne devient pas faussement
    vert sur une propriete qu'il ne verifie plus.
    """
    import build_memento as B

    ecarts = []
    lot = lib_ssp.lot_prioritaire()
    tous = B.par_ssp(None)
    attendus = B.diagnostics_attendus()
    ailleurs = B.documente_ailleurs(tous)
    docs, _, _ = B.documents(lot)

    couples = []
    for ssp in sorted(docs):
        documentes = {c["diagnostic"] for c in tous[ssp] if c["diagnostic"]}
        for diagnostic in sorted(attendus.get(ssp, ())):
            porteuses = {s for s in ailleurs.get(diagnostic, ()) if s != ssp}
            if diagnostic not in documentes and porteuses and not porteuses & set(lot):
                couples.append((ssp, diagnostic, sorted(porteuses)))

    for ssp, diagnostic, porteuses in couples:
        bloc = f"> [!success] 💊 Management — si {diagnostic}\n> "
        texte = docs[ssp]
        if bloc + B.SANS_GRILLE in texte:
            ecarts.append(f"{ssp} — si {diagnostic} : annonce un trou du corpus alors que "
                          f"{porteuses} le documente(nt)")
        elif bloc not in texte or porteuses[0] not in texte.split(bloc)[1][:400]:
            ecarts.append(f"{ssp} — si {diagnostic} : le renvoi ne nomme pas {porteuses}")
    if not couples:
        ecarts.append("aucun couple (SSP, diagnostic documente seulement hors lot) — "
                      "ce controle ne verifie plus rien, le relire")
    return ecarts


def verifier_attendus_du_corpus():
    """Aucun diagnostic attendu ne double un diagnostic observe par la graphie.

    Les deux libelles viennent de deux tables differentes : `diagnostics` dans
    docs/ecos-priorites-2026.yaml pour les attendus, docs/ecos-diagnostics.yaml
    (via docs/ecos-diagnostics-alias.yaml) pour les observes. S'ils ne
    different que par la CASSE ou les ACCENTS, le memento afficherait DEUX
    sous-blocs pour un seul diagnostic, dont l'un annoncerait faussement
    qu'aucune grille ne le documente. Aucun cas construit ne peut surveiller
    cette jointure : elle se verifie sur le corpus, ce que fait ce bloc.

    Une divergence reelle de vocabulaire (« MICI (Crohn / RCUH) » contre
    « Rectocolite ulcero-hemorragique ») n'est PAS un ecart ici : elle se
    corrige dans docs/ecos-diagnostics-alias.yaml, et le sous-bloc vide la
    signale au lecteur. Seule la graphie est gardee.
    """
    import build_memento

    ecarts = []
    attendus = build_memento.diagnostics_attendus()
    normalise = lambda t: lib_extraction.sans_accent(t).lower()
    for ssp, cas_list in build_memento.par_ssp(None).items():
        observes = {c["diagnostic"] for c in cas_list if c["diagnostic"]}
        vus = {normalise(d): d for d in observes}
        for attendu in sorted(attendus.get(ssp, ())):
            jumeau = vus.get(normalise(attendu))
            if jumeau is not None and jumeau != attendu:
                ecarts.append(f"{ssp} : « {attendu} » (priorités) et « {jumeau} » (corpus) "
                              "ne different que par la graphie")
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
    ecarts += verifier_management()
    ecarts += verifier_marque_partage()
    ecarts += verifier_restriction()
    ecarts += verifier_restriction_au_point_d_appel()
    ecarts += verifier_mention()
    ecarts += verifier_sous_blocs()
    ecarts += verifier_tri_clinique()
    ecarts += verifier_renvoi_hors_lot()
    ecarts += verifier_attendus_du_corpus()

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — appariement conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
