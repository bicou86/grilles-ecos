"""Rejoue les mutations du vocabulaire canonique sur les SSP du lot 2. Sortie 1 si ecart.

POURQUOI UN CONTROLE ET NON UN BANC JETABLE. `check_vocabulaire.py` porte neuf
proprietes, mais rien ne prouvait qu'elles MORDENT sur les SSP entrees en
perimetre avec le lot 2 : la suite de mutations de la tache 10 avait ete batie
sur des fixtures du lot 1, et un controle qui ne trouve aucun temoin passe au
vert sans rien examiner. Ce fichier fige les mutations, pour qu'elles soient
rejouables par un successeur au lieu d'etre racontees dans un rapport.

LA DIXIEME LIGNE DU TABLEAU EST LA PLUS UTILE, et elle garde ce banc lui-meme.
Le premier banc filtrait les ecarts sur le prefixe « SSP / « cle » » ; or
`collisions()` ecrit « SSP — RAPPROCHEMENT ABUSIF : … ». Le banc a donc affiche
« PASSE » sur une collision que le garde-fou avait bel et bien detectee, puis
a etiquete « propriete 7 » deux refus qui etaient des collisions. La propriete
`etiquette` verifie que chaque mutation est refusee POUR LE BON MOTIF, pas
seulement refusee : un refus « propriete 7 » se lit « inoffensif », un refus
« propriete 8 » se lit « cela aurait efface une distinction ».

DETERMINISME : mutations declarees en dur et triees, aucune date, aucun
aleatoire. Cout mesure : ~0,4 s par mutation.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento                                      # noqa: E402
import check_vocabulaire                                  # noqa: E402
import lib_vocabulaire                                    # noqa: E402
import lib_yaml                                           # noqa: E402

# (motif attendu, SSP, cle, valeur, cle a retirer d'abord)
#   "collision" -> propriete 8, la table confondrait deux libelles qu'une
#                  grille distingue. C'est le refus GRAVE.
#   "inerte"    -> propriete 7, l'entree ne rapprocherait rien.
#   "cle"       -> propriete 3, la cle n'existe pas dans cette SSP.
#   "cible"     -> propriete 4, la forme canonique est inventee.
#   "chaine"    -> propriete 5, la cle est deja la cible d'une autre entree.
MUTATIONS = [
    # Collisions sur des SSP du LOT 2, avec temoin intra-grille.
    ("collision", "Douleurs Articulaires",
     "1-3 petites articulations: 2 points", ">10 articulations: 5 points", None),
    # Fusion INDIRECTE : German-63 ne porte pas « Antécédents familiaux », mais
    # la table y aliase deja son « Anamnèse familiale ».
    ("collision", "Ménopause", "Cancers familiaux", "Antécédents familiaux", None),
    ("collision", "Douleur d'Épaule", "Rotation externe", "Rotation interne", None),
    # Les deux que le premier banc avait etiquetees « propriete 7 » a tort :
    # elles sont AUSSI inertes, et c'est ce qui masquait la collision.
    ("collision", "Neuropathie Périphérique", "Tabac", "Tabagisme", None),
    ("collision", "Rectorragies & Hémorragie Digestive Basse",
     "Médicaments", "Médicaments actuels", None),
    # Inertes : sous-items de parents differents, l'entree ne reunirait rien.
    ("inerte", "Neuropathie Périphérique",
     "Opérations antérieures", "Antécédents chirurgicaux", None),
    # CETTE LIGNE A CHANGE DE FIXTURE LE 2026-08-16, et le motif du changement
    # vaut d'etre garde. Elle portait « Médicaments » -> « Médicaments actuels »
    # sur AVP, inerte parce que les deux libelles vivaient sous des parents
    # differents. La curation en masse a reuni ces parents : la mutation est
    # devenue une entree VALIDE, donc plus une mutation du tout, et le banc
    # signalait « NON DETECTEE » — a juste titre. Une fixture de propriete 7
    # depend de la table qu'elle observe ; celle-ci la remplace sur la meme SSP
    # et garde exactement le meme piege : deux libelles qu'un relecteur
    # rapprocherait sans hesiter, et qui ne se rencontrent jamais.
    ("inerte", "AVP (Accident de la Voie Publique)",
     "Radiographie du bassin", "Radiographie du bassin de face", None),
    ("inerte", "Adénopathie", "Habitudes de vie", "Habitudes", None),
    # Fautes de saisie, sur des SSP du lot 2.
    ("cle", "Dysphagie", "Anamnese familiale", "Antécédents familiaux", None),
    ("cible", "Hématurie", "Tabac", "Consommation tabagique", "Tabac"),
    # Declaree « chaine » a la premiere redaction : elle l'est, mais elle
    # collisionne AUSSI, et la regle de gravite l'a signale. C'est la troisieme
    # etiquette que ce banc corrige apres l'avoir sous-estimee.
    ("collision", "Syndrome Métabolique",
     "Antécédents médicaux personnels", "Antécédents familiaux", None),
    # Une vraie chaine, sans collision : « Habitudes de vie » est deja la cle
    # d'une entree de Hématurie, la viser comme CIBLE ferait A->B et B->C.
    ("chaine", "Hématurie", "Habitudes et mode de vie", "Habitudes de vie", None),
]

MOTIFS = {
    "collision": lambda e: "RAPPROCHEMENT ABUSIF" in e,
    "inerte": lambda e: "ne rapproche aucune grille" in e,
    "cle": lambda e: "aucune grille de cette SSP ne porte ce libellé" in e,
    "cible": lambda e: "la forme canonique n'est portée par aucune grille" in e,
    "chaine": lambda e: "canonique() ne chaîne pas" in e,
}

# GRAVITE, ET C'EST ELLE QUI EST COMPAREE — pas la simple presence du motif
# declare. Cinq des mutations produisent DEUX ecarts : elles collisionnent ET
# sont inertes. Un banc qui se contentait de « le motif declare figure parmi
# les ecarts » acceptait donc d'etiqueter « inerte » une vraie collision —
# verifie par mutation de ce fichier meme, elle passait au vert. Or c'est
# exactement l'erreur a ne pas refaire : « inerte » se lit « inoffensif »,
# « collision » se lit « cela aurait efface une distinction ».
GRAVITE = {"collision": 3, "cle": 2, "cible": 2, "chaine": 2, "inerte": 1}


def concerne(ecart, ssp, cle):
    """Tout ecart qui NOMME la SSP et la cle, quelle que soit sa forme.

    Et non le seul prefixe « SSP / « cle » » : c'est precisement l'erreur que
    ce banc a commise, `collisions()` ecrivant sous une autre forme.
    """
    return ssp in ecart and cle in ecart


def main():
    base = lib_yaml.lire_groupe(check_vocabulaire.TABLE)
    groupes = build_memento.par_ssp(None)
    inventaire = lib_vocabulaire.libelles_par_ssp(groupes)

    ecarts = []
    temoin = check_vocabulaire.verifier(base, inventaire, groupes)
    if temoin:
        ecarts.append(f"TEMOIN ROUGE — la table livree produit {len(temoin)} "
                      f"ecart(s) : {temoin[0][:120]}")

    for attendu, ssp, cle, valeur, retire in MUTATIONS:
        table = {s: dict(e) for s, e in base.items()}
        if retire:
            table.get(ssp, {}).pop(retire, None)
        table.setdefault(ssp, {})[cle] = valeur
        vus = [e for e in check_vocabulaire.verifier(table, inventaire, groupes)
               if concerne(e, ssp, cle)]
        ou = f"{ssp} / « {cle} » → « {valeur} »"
        if not vus:
            ecarts.append(f"NON DETECTEE — {ou} (motif attendu : {attendu})")
            continue
        observes = {nom for nom, test in MOTIFS.items() if any(test(e) for e in vus)}
        if not observes:
            ecarts.append(f"MOTIF INCONNU — {ou} : {vus[0][:110]}")
        else:
            pire = max(observes, key=lambda n: (GRAVITE[n], n))
            if pire != attendu:
                ecarts.append(f"MOTIF SOUS-ESTIME — {ou} : déclaré « {attendu} », "
                              f"le plus grave observé est « {pire} » "
                              f"(tous : {sorted(observes)})")

    if ecarts:
        print(f"ÉCHEC — {len(ecarts)} écart(s) sur {len(MUTATIONS)} mutations :")
        for e in ecarts:
            print("  ", e)
        return 1
    collisions = sum(1 for m in MUTATIONS if m[0] == "collision")
    print(f"OK — {len(MUTATIONS)} mutations du vocabulaire détectées avec le bon "
          f"motif (dont {collisions} collisions), témoin vert")
    return 0


if __name__ == "__main__":
    sys.exit(main())
