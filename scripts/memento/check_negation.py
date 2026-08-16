"""Le detecteur de negation asymetrique, garde par temoin et par mutation. Sortie 1 si ecart.

CE QUE CE BANC EXISTE POUR EMPECHER. La ronde 1 de curation a produit cinq
entrees dont la forme canonique retenue etait la forme NEGATIVE — « Hepatomegalie »
-> « Pas d'hepatomegalie » — et il a fallu les inverser a la main. TROIS
mecanismes regardaient exactement la sans rien voir : la liste `ANTONYMES` de
`report_doublons` ne connait ni « pas » ni « sans » ; `lib_cle.MOTS_VIDES` ne les
efface pas ; et aucune grille ne portant les deux libelles, la propriete 8 de
`check_vocabulaire` n'avait pas de temoin. `lib_vocabulaire.negation()` ferme
l'angle mort ; ce fichier garde `negation()`.

TROIS FACONS DONT UN DETECTEUR DE CE GENRE MEURT EN SILENCE, et une propriete
contre chacune :

  1. IL CESSE DE VOIR. Les temoins sont des paires REELLES du corpus, dont les
     deux libelles sont verifies presents dans leur SSP a chaque execution. Un
     temoin qui disparait du corpus est signale comme tel, et non silencieusement
     saute — sans quoi le banc se viderait au fil des extractions.
  2. IL VOIT PARTOUT. Les contre-epreuves exigent None la ou il ne doit rien y
     avoir : deux libelles qui nient TOUS LES DEUX (l'ecart n'est alors pas la
     negation), et deux libelles qui ne nient ni l'un ni l'autre.
  3. IL EST DECORATIF. C'est le defaut que ce projet a paye trois fois — une
     propriete sans temoin passe au vert sans rien examiner. La MUTATION PAR MOT
     retire chaque mot de la liste tour a tour et exige qu'un temoin cesse d'etre
     detecte : un mot que rien n'exerce est un mot qui ne garde rien, et le banc
     le refuse. C'est ce test qui a fait retirer « ni » et « negatif » de la
     liste (voir `lib_vocabulaire.NEGATIONS_MOTS`).

LA COLONNE « CANDIDATE » N'EST PAS DECORATIVE NON PLUS. Elle dit, pour chaque
temoin, si le rapport de doublons proposerait VRAIMENT cette paire (similarite
au-dessus du seuil). Un mot dont tous les temoins sont sous le seuil est garde,
mais le lecteur doit savoir qu'il ne garde aujourd'hui que du futur : deux des
sept mots sont dans ce cas, et le banc le DIT au lieu de le taire.

DETERMINISME : temoins declares en dur et tries, aucune date, aucun aleatoire.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_vocabulaire                                    # noqa: E402
import report_doublons                                    # noqa: E402

# (mot canonique attendu, SSP, libelle qui NIE, libelle qui AFFIRME)
# Les deux libelles sont reels et portes par une grille de cette SSP.
TEMOINS = [
    # LES CINQ DE LA RONDE 1, celles que la chaine n'a pas vues et qu'il a fallu
    # inverser a la main. Ce sont les temoins qui comptent le plus : ils nomment
    # le defaut au lieu de le decrire.
    ("pas", "Douleur Thoracique",
     "Pas d'hépatomégalie", "Hépatomégalie"),
    ("pas", "Douleur Thoracique",
     "Pas de turgescence jugulaire", "Turgescence jugulaire"),
    ("pas", "Œdèmes des Membres Inférieurs",
     "Pas de reflux hépato-jugulaire", "Reflux hépato-jugulaire"),
    ("non", "Amaurose & Perte Brutale de Vision",
     "Non ophtalmologiques", "Antécédents ophtalmologiques"),
    ("non", "Toux", "Productive ou non", "Productive ou sèche"),
    # « non » sur une meme grille, a 0,94 de similarite : le cas le plus net du
    # corpus, et celui ou l'inversion serait la plus tentante.
    ("non", "Dysfonction Érectile",
     "Prise en charge non médicamenteuse", "Prise en charge médicamenteuse"),
    # « sans » -> jeton « san » : le piege du singulier grossier. Sans ce
    # temoin, une liste ecrite en jetons a la main resterait verte a tort.
    ("san", "Œil Rouge & Douleur Oculaire", "Sans correction", "Avec correction"),
    ("absence", "Fatigue", "Absence de soutien social", "Soutien social"),
    ("jamai", "Douleur Thoracique", "Jamais au repos", "Angor au repos"),
    # LES DEUX TEMOINS MINCES, et ils sont declares comme tels. « aucun » et
    # « aucune » n'apparaissent qu'une poignee de fois dans le corpus, jamais sur
    # une paire que le rapport proposerait : leur echelle de cotation
    # (RESCOS-69) et une phrase longue (RESCOS-70b) sont tout ce qu'il y a. Ils
    # gardent les deux mots contre la disparition, pas contre une fusion abusive
    # imminente — la colonne « candidate » le dit a chaque execution.
    ("aucun", "Douleur d'Épaule", "Aucun", "Un"),
    ("aucune", "Parésie - AVC",
     "Reconnaît qu'aucune imagerie / laboratoire de routine n'est nécessaire "
     "dans la forme typique (examens ciblés seulement si atypie)",
     "Reconnaît une paralysie faciale PÉRIPHÉRIQUE et la distingue d'une "
     "atteinte centrale (atteinte du front)"),
]

# (motif, libelle, libelle) — doivent rendre None.
CONTRE_EPREUVES = [
    # LES DEUX COTES NIENT : l'ecart est ailleurs que dans la negation, et
    # signaler ici enverrait le relecteur chercher une inversion qui n'existe
    # pas. Paire reelle : RESCOS-36 (Douleur Thoracique) porte les deux.
    ("les deux côtés nient", "Pas de turgescence jugulaire", "Pas d'hépatomégalie"),
    ("les deux côtés nient", "Pas de fièvre", "Pas de frissons"),
    # AUCUN DES DEUX NE NIE. Le premier couple est la paire d'antonymes que
    # `antonymie()` garde deja (hyper/hypo) : les deux filtres ne doivent pas se
    # marcher dessus.
    ("aucun des deux ne nie", "Signes d'hyperthyroïdie", "Signes d'hypothyroïdie"),
    ("aucun des deux ne nie", "Palpation abdominale", "Inspection abdominale"),
    # LE MOT NEGATIF EST DANS LES DEUX, A L'ACCORD PRES : « négatifs » et
    # « négative » se reduisent au meme jeton que leur singulier, donc l'accord
    # ne doit pas creer d'asymetrie. (Mot hors liste depuis le comptage, la
    # contre-epreuve reste vraie et le restera s'il y revient.)
    ("aucun des deux ne nie", "Critères d'Ottawa négatifs", "Critère d'Ottawa négatif"),
]


def adossement(inventaire):
    """Propriete 1 : chaque libelle de chaque temoin existe encore dans sa SSP."""
    ecarts = []
    for mot, ssp, neg, pos in TEMOINS:
        connus = inventaire.get(ssp)
        if connus is None:
            ecarts.append(f"TÉMOIN DISPARU — « {ssp} » n'est plus une SSP du corpus "
                          f"(témoin du mot « {mot} »)")
            continue
        for libelle in (neg, pos):
            if libelle not in connus:
                ecarts.append(f"TÉMOIN DISPARU — {ssp} : aucune grille ne porte plus "
                              f"« {libelle} » (témoin du mot « {mot} »)")
    return ecarts


def detection():
    """Proprietes 2 et 3 : le detecteur trouve, et le rapport le DIT."""
    ecarts = []
    for mot, ssp, neg, pos in TEMOINS:
        for a, b in ((neg, pos), (pos, neg)):
            vu = lib_vocabulaire.negation(a, b)
            if vu != mot:
                ecarts.append(f"NON DÉTECTÉE — {ssp} : « {a} » ⟷ « {b} » — attendu "
                              f"« {mot} », obtenu {vu!r}")
        marque = report_doublons.signal_negation(neg, pos)
        if not marque or mot not in marque:
            ecarts.append(f"NON AFFICHÉE — {ssp} : « {neg} » ⟷ « {pos} » — le rapport "
                          f"n'imprime pas le mot « {mot} » : {marque[:80]!r}")
    return ecarts


def contre_epreuves():
    """Propriete 4 : le detecteur se tait la ou il n'y a rien."""
    ecarts = []
    for motif, a, b in CONTRE_EPREUVES:
        for x, y in ((a, b), (b, a)):
            vu = lib_vocabulaire.negation(x, y)
            if vu is not None:
                ecarts.append(f"FAUX POSITIF — « {x} » ⟷ « {y} » ({motif}) : le "
                              f"détecteur rend « {vu} » au lieu de rien")
    return ecarts


def mutation_par_mot():
    """Propriete 5 : retirer un mot de la liste doit faire tomber un temoin.

    LE TEST DU MOT DECORATIF. Il passe par le VRAI chemin d'appel — la constante
    du module est remplacee le temps de la mesure, exactement comme
    `check_vocabulaire.installee()` fait pour la table — plutot que par une copie
    du raisonnement, qui ne prouverait rien du code livre.
    """
    ecarts = []
    avant = lib_vocabulaire.NEGATIONS
    try:
        for mot in sorted(avant):
            lib_vocabulaire.NEGATIONS = frozenset(avant - {mot})
            tombes = [t for t in TEMOINS
                      if lib_vocabulaire.negation(t[2], t[3]) != t[0]]
            if not tombes:
                ecarts.append(f"MOT DÉCORATIF — retirer « {mot} » de NEGATIONS ne fait "
                              "échouer aucun témoin : ce mot ne garde rien, il faut "
                              "soit lui donner un témoin, soit le retirer de la liste")
    finally:
        lib_vocabulaire.NEGATIONS = avant
    return ecarts


def main():
    inventaire = lib_vocabulaire.inventaire()
    ecarts = (adossement(inventaire) + detection() + contre_epreuves()
              + mutation_par_mot())
    if ecarts:
        print(f"ÉCHEC — {len(ecarts)} écart(s) sur {len(TEMOINS)} témoins et "
              f"{len(CONTRE_EPREUVES)} contre-épreuves :")
        for e in ecarts:
            print("  ", e)
        return 1

    print(f"OK — {len(TEMOINS)} témoins réels du corpus détectés dans les deux sens et "
          f"affichés, {len(CONTRE_EPREUVES)} contre-épreuves muettes, "
          f"{len(lib_vocabulaire.NEGATIONS)} mots tous exercés par mutation")
    for mot in sorted(lib_vocabulaire.NEGATIONS):
        siens = [t for t in TEMOINS if t[0] == mot]
        candidates = sum(1 for t in siens
                         if report_doublons.similarite(t[2], t[3]) > report_doublons.SEUIL)
        etat = (f"{candidates} au-dessus du seuil du rapport" if candidates
                else "AUCUN au-dessus du seuil — garde le mot, ne garde pas une fusion")
        print(f"   « {mot} » : {len(siens)} témoin(s), {etat}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
