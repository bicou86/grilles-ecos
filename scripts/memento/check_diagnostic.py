"""Couverture et coherence de la resolution du diagnostic. Sortie 1 si ecart."""
import glob
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_diagnostic
import lib_extraction
import lib_ssp
import lib_yaml

REPO = Path(__file__).resolve().parents[2]
ALIAS = REPO / "docs" / "ecos-diagnostics-alias.yaml"

SEUIL = 90  # part minimale de cas dont le diagnostic est resolu (plancher, pas cible)

# Confiances dont la valeur SORT du bloc de diagnostics differentiels, ou a
# ete posee a la main en le corrigeant : ce sont celles que la grille peut
# contredire. Les autres viennent deja d'une source dediee (explicite,
# corrige, diagnostic-travail) ou ont ete validees par l'auteur (confirme).
A_CONFRONTER = ("dd-principal", "premier-dd", "enonce")

# Mots trop generiques pour valoir corroboration : « aigue », « droite »,
# « probable » se retrouvent dans deux diagnostics sans rapport. Le seuil de
# quatre lettres ecarte deja les mots-outils ; cette liste retire les
# qualificatifs cliniques qui, eux, sont longs mais ne nomment rien.
QUALIFICATIFS = {
    "aigu", "aigue", "aigus", "aigues", "chronique", "chroniques", "gauche",
    "droit", "droite", "bilateral", "bilaterale", "probable", "probablement",
    "possible", "primaire", "primitif", "secondaire", "severe", "legere",
    "modere", "moderee", "avec", "sans", "dans", "chez", "pour", "plus",
    "cette", "elle", "etre", "principal", "principale", "diagnostic",
    "diagnostics", "suspicion", "hypothese", "patient", "patiente", "stade",
    "forte", "type", "sur", "une", "des", "les", "par", "non", "aux",
    # Tetes de libelle qui ne nomment rien a elles seules : sans elles,
    # « Maladie cœliaque » et « maladie de Parkinson idiopathique » se
    # corroboraient sur le mot « maladie » (mesure : 1 rapprochement abusif
    # sur 22 au temoin croise, 0 une fois ces mots retires ; le temoin
    # positif reste a 22 sur 22).
    "maladie", "maladies", "syndrome", "syndromes", "trouble", "troubles",
}


def _corpus(cid):
    """Prefixe de corpus d'un identifiant de cas ('AMBOSS-12' -> 'AMBOSS')."""
    return cid.split("-")[0]


def _mots(t):
    """Mots porteurs d'un libelle, sans accents ni apostrophe typographique."""
    t = unicodedata.normalize("NFD", t.lower().replace("’", "'"))
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return [m for m in re.findall(r"[a-z0-9]+", t)
            if len(m) >= 4 and m not in QUALIFICATIFS]


def corrobore(valeur, temoin):
    """Le terme partage par la valeur et l'enonce de la grille, ou None.

    Egalite exacte pour les mots courts ; prefixe de six lettres pour les
    longs, ce qui rapproche « ovaire » et « ovarien », « cancer du poumon »
    et « cancer bronchopulmonaire », sans rapprocher « cholecystite » de
    « choledocholithiase » (elles divergent des la sixieme lettre) ni
    « nephretique » de « pyelonephrite ».

    Ce n'est PAS une preuve d'equivalence clinique, et ce n'est pas ce qu'on
    lui demande : la propriete cherche la CONTRADICTION — aucun terme commun
    entre la valeur retenue et ce que la grille enonce d'elle-meme.
    """
    a, b = _mots(valeur), _mots(temoin)
    for x in a:
        for y in b:
            if x == y:
                return x
            if len(x) >= 6 and len(y) >= 6 and x[:6] == y[:6]:
                return f"{x} / {y}"
    return None


def fichiers_par_cas():
    """id de cas -> chemin de la grille HTML. AZYGOS exclu (JSON, pas d'enonce)."""
    out = {}
    for corpus in lib_ssp.CORPUS:
        if corpus == "azygos":
            continue
        for f in sorted(glob.glob(lib_extraction.motif(corpus))):
            out.setdefault(lib_extraction.identifiant(f), f)
    return out


# TEMOIN POSITIF de l'instrument. Les valeurs GERMAN de confiance « corrige »
# viennent d'une source dediee et relue ; on demande a l'extracteur d'enonces,
# PRIVE de cette source (corpus=None, donc sans le bloc corrige qui la
# produit), de ne contredire aucune d'elles. Mesure du jour : 22 grilles
# portent un enonce exploitable, 22 corroborent, 0 contredit. Le plancher est
# la pour que l'instrument ne puisse pas devenir vert en ne trouvant plus
# rien — c'est exactement ainsi qu'un controle passe sans rien examiner.
TEMOIN_MINIMUM = 15


# TEMOIN NOMME de `corrobore()`. Un agregat ne dit pas si l'instrument
# distingue ce qu'il DOIT distinguer : ces couples-la, tires du corpus, le
# disent. Les cinq premiers sont des reformulations de la meme maladie et
# doivent se rapprocher ; les sept suivants sont les inversions que ce
# controle existe pour attraper, et deux voisinages de graphie qui ne doivent
# jamais passer (« cholangite »/« cholecystite », « zona »/« zone »).
PAIRES_TEMOIN_OUI = [
    ("Cancer du poumon", "cancer bronchopulmonaire (forte suspicion)"),
    ("Cancer de l'ovaire", "Suspicion de cancer ovarien précoce"),
    ("Maladie de Crohn", "maladie de Crohn iléo-colique"),
    ("Rupture de la coiffe des rotateurs", "rupture de la coiffe des rotateurs"),
    ("Périménopause probable", "une périménopause probable, que trois éléments"),
]
PAIRES_TEMOIN_NON = [
    ("Cholangite", "cholécystite aiguë lithiasique"),
    ("Cholécystite", "cholédocholithiase"),
    ("Pyélonéphrite aiguë", "colique néphrétique droite"),
    ("Phéochromocytome", "une périménopause probable"),
    ("Maladie cœliaque", "maladie de Parkinson idiopathique"),
    ("Hernie discale", "paralysie de Bell"),
    ("Zona (Herpes zoster)", "zone de conflit sous-acromial"),
]


def temoin_nomme():
    """Ecarts de `corrobore()` sur les couples temoins. Liste vide si conforme."""
    ecarts = []
    for valeur, enonce in PAIRES_TEMOIN_OUI:
        if not corrobore(valeur, enonce):
            ecarts.append(f"« {valeur} » et « {enonce} » devraient se corroborer")
    for valeur, enonce in PAIRES_TEMOIN_NON:
        terme = corrobore(valeur, enonce)
        if terme:
            ecarts.append(f"« {valeur} » et « {enonce} » ne devraient PAS se "
                          f"corroborer (rapprochés sur « {terme} »)")
    return ecarts


# PLAFOND DU TEMOIN CROISE. Le temoin positif ne voit qu'un sens de l'erreur :
# un extracteur devenu TROP LARGE (qui ramene tout le document au lieu de la
# seule presentation) continue de corroborer les bonnes valeurs et passe au
# vert, tout en cessant de pouvoir contredire quoi que ce soit. Mesure a
# l'appui : elargir ZONE_LONGUE a tout le <body> laisse le temoin positif a
# 22 sur 22. Le temoin croise apparie chaque valeur validee a l'enonce d'une
# AUTRE grille, ou elle n'a rien a faire : 0 rapprochement sur 22 aujourd'hui,
# 15 avec la meme mutation. Le plafond est en part pour ne pas dependre du
# nombre exact de grilles GERMAN.
#
# L'appariement est TOUTES PAIRES et non au seul voisin : 22 valeurs contre
# les 21 enonces des autres grilles, soit 462 confrontations dont aucune ne
# devrait aboutir. Mesure du jour : 4 sur 462 (0,9 %) — des voisinages de
# vocabulaire reels entre deux grilles differentes. Un instrument relache
# monte tout de suite : ramener le seuil de mot porteur de quatre lettres a
# une seule donne 16 sur 462 (3,5 %). Plafond a 2 %, soit un peu plus du
# double de la mesure, pour tolerer l'ajout d'une grille sans se declencher.
PLAFOND_CROISE = 0.02


def temoin_positif(parsed):
    """(corroborees, contredites, croisees_a_tort, total) sur GERMAN « corrige ».

    Les valeurs GERMAN « corrige » sont tirees d'une source dediee et relues.
    L'extracteur d'enonces, PRIVE de cette source (corpus=None, donc sans le
    bloc corrige qui la produit), doit :
      - retrouver chacune de ces valeurs la ou il repond   (temoin positif) ;
      - ne PAS retrouver la valeur de la grille VOISINE    (temoin croise).
    L'appariement au voisin est cyclique sur la liste triee : deterministe,
    sans horloge ni aleatoire.
    """
    fichiers = fichiers_par_cas()
    paires = []
    for cid in sorted(parsed):
        diag, conf = parsed[cid]
        if conf != "corrige" or _corpus(cid) != "German":
            continue
        chemin = fichiers.get(cid)
        if chemin is None:
            continue
        brut = Path(chemin).read_text(encoding="utf8", errors="replace")
        enonces = lib_diagnostic.hypotheses_enoncees(brut)
        if enonces:
            paires.append((cid, diag, enonces))

    corrobores, contredits, croises, confrontations = 0, [], [], 0
    for i, (cid, diag, enonces) in enumerate(paires):
        if any(corrobore(diag, e) for _, e in enonces):
            corrobores += 1
        else:
            contredits.append((cid, diag, enonces))
        for j, (autre, _, ailleurs) in enumerate(paires):
            if i == j:
                continue
            confrontations += 1
            if any(corrobore(diag, e) for _, e in ailleurs):
                croises.append((cid, diag, autre))
    return corrobores, contredits, croises, len(paires), confrontations


def confrontation(parsed):
    """Valeurs tirees du differentiel que la grille contredit elle-meme.

    Renvoie (contredits, examinees, avec_temoin). Une grille est CONTREDITE
    quand elle nomme son diagnostic — « Mon hypothese principale est une
    cholecystite aigue lithiasique », « A (Assessment) : Suspicion de… », bloc
    « Diagnostic le plus probable », bloc corrige — et qu'aucun de ces
    enonces ne partage un terme avec la valeur retenue. C'est le defaut qui a
    donne « Cholangite » a une vignette de cholecystite (RESCOS-18) et
    « Pheochromocytome » a une perimenopause (German-6).

    Le libelle est confronte sous sa forme de la table ET sous son alias de
    docs/ecos-diagnostics-alias.yaml : la grille dit parfois « AOMI » la ou
    la table ecrit « Arteriopathie obliterante atheroscereuse », et l'alias
    est precisement la table curee qui sait que les deux se rejoignent.
    """
    alias = lib_yaml.lire_plat(ALIAS)
    fichiers = fichiers_par_cas()
    contredits, examinees, avec_temoin = [], 0, 0
    for cid in sorted(parsed):
        diag, conf = parsed[cid]
        if conf not in A_CONFRONTER or not diag:
            continue
        chemin = fichiers.get(cid)
        if chemin is None:
            continue
        examinees += 1
        brut = Path(chemin).read_text(encoding="utf8", errors="replace")
        enonces = lib_diagnostic.hypotheses_enoncees(brut, Path(chemin).parent.name)
        if not enonces:
            continue
        avec_temoin += 1
        formes = [diag] + ([alias[diag]] if diag in alias else [])
        if any(corrobore(f, e) for f in formes for _, e in enonces):
            continue
        contredits.append((cid, diag, conf, enonces))
    return contredits, examinees, avec_temoin


def _parse(v):
    """(diagnostic, confiance) depuis une valeur brute de la table.

    Un partition sur le premier "|", pas un split sur " | " : quand le
    diagnostic est vide, lib_yaml.lire_plat absorbe l'espace double qui
    separe alors la cle de la valeur ("cid:  | absent" -> val "| absent"),
    et un split sur le separateur a trois caracteres ne le retrouve plus.
    """
    diag, sep, conf = v.partition("|")
    return diag.strip(), (conf.strip() if sep else "absent")


def main():
    table = lib_diagnostic.charger_table()
    if not table:
        print("ECHEC — docs/ecos-diagnostics.yaml est vide ou absent")
        return 1

    parsed = {cid: _parse(v) for cid, v in table.items()}

    confiances = Counter(conf for _, conf in parsed.values())
    resolus = sum(n for c, n in confiances.items() if c != "absent")
    part = 100 * resolus // len(table)
    print(f"{len(table)} cas · {resolus} diagnostics résolus ({part} %)")
    for c, n in confiances.most_common():
        print(f"   {c:20s} {n}")

    print("\nPar corpus :")
    par_corpus = sorted({_corpus(cid) for cid in table})
    for corpus in par_corpus:
        confs = Counter(conf for cid, (_, conf) in parsed.items() if _corpus(cid) == corpus)
        total = sum(confs.values())
        detail = ", ".join(f"{c}={n}" for c, n in confs.most_common())
        print(f"   {corpus:8s} {total:3d} cas — {detail}")

    deduits = sorted(cid for cid, (_, conf) in parsed.items() if conf == "deduit")
    if deduits:
        print(f"\n{len(deduits)} diagnostic(s) « deduit » à relire :")
        for cid in deduits:
            print(f"   {cid}: {parsed[cid][0]}")

    # Signalement, pas un echec : une grille GERMAN dont le bloc diagnostic
    # porte plusieurs c-red sans formule assertive du corrige pour trancher
    # retombe sur le premier c-red (repli mecanique) — souvent correct, mais
    # a relire plutot qu'a accepter en silence (ronde de correction 2/5).
    # Une grille hors perimetre n'a pas de ligne dans la table : rien a relire.
    multi_cred = [(cid, n) for cid, n in lib_diagnostic.signalements_multi_cred()
                  if cid in parsed]
    if multi_cred:
        print(f"\n{len(multi_cred)} grille(s) GERMAN à c-red multiples sans "
              f"marqueur (repli sur le premier, à relire) :")
        for cid, n in multi_cred:
            print(f"   {cid} ({n} c-red) : {parsed[cid][0]}")

    # L'instrument avant la mesure : sur les valeurs GERMAN deja validees,
    # l'extracteur d'enonces doit corroborer et ne jamais contredire.
    ecarts_nommes = temoin_nomme()
    print(f"\nTémoin nommé — {len(PAIRES_TEMOIN_OUI)} couples à rapprocher, "
          f"{len(PAIRES_TEMOIN_NON)} à distinguer : {len(ecarts_nommes)} écart(s).")
    if ecarts_nommes:
        print("ECHEC — corrobore() ne fait plus la distinction attendue :")
        for e in ecarts_nommes:
            print(f"   {e}")
        return 1

    bons, faux, croises, total, confrontations = temoin_positif(parsed)
    print(f"Témoin positif — {bons}/{total} valeur(s) GERMAN « corrige » "
          f"retrouvée(s) par l'extracteur d'énoncés, {len(faux)} contredite(s) ; "
          f"témoin croisé : {len(croises)}/{confrontations} rapprochement(s) "
          f"avec l'énoncé d'une autre grille.")
    if faux:
        print("ECHEC — l'extracteur d'énoncés contredit des valeurs validées :")
        for cid, diag, enonces in faux:
            print(f"   {cid} — « {diag} » contre {enonces}")
        return 1
    if bons < TEMOIN_MINIMUM:
        print(f"ECHEC — {bons} témoin(s) seulement, plancher {TEMOIN_MINIMUM} : "
              "l'extracteur d'énoncés ne lit plus le corpus, le contrôle qui "
              "suit ne vérifierait rien.")
        return 1
    if confrontations and len(croises) > PLAFOND_CROISE * confrontations:
        print(f"ECHEC — {len(croises)}/{confrontations} valeurs retrouvées dans l'énoncé "
              f"d'une AUTRE grille (plafond {int(100 * PLAFOND_CROISE)} %) : "
              "l'extracteur ratisse trop large et ne peut plus contredire.")
        for cid, diag, voisin in croises[:8]:
            print(f"   « {diag} » ({cid}) retrouvé dans l'énoncé de {voisin}")
        return 1

    # Le diagnostic tire du differentiel est-il dementi par la grille ?
    contredits, examinees, avec_temoin = confrontation(parsed)
    print(f"\n{examinees} valeur(s) tirée(s) du différentiel confrontées à ce que "
          f"la grille énonce d'elle-même :")
    if not examinees:
        print("   AUCUNE — plus une seule valeur de confiance "
              f"{', '.join(A_CONFRONTER)} : ce contrôle n'examine plus rien, le relire.")
    elif not avec_temoin:
        print("   AUCUN TÉMOIN — aucune de ces grilles ne nomme son diagnostic "
              "ailleurs. Le contrôle est vert sans avoir rien pu comparer : "
              "vérifier que lib_diagnostic.hypotheses_enoncees() lit encore le corpus.")
    else:
        print(f"   {avec_temoin} portent un énoncé exploitable, "
              f"{examinees - avec_temoin} n'en portent aucun (non vérifiables).")

    if contredits:
        print(f"\nECHEC — {len(contredits)} diagnostic(s) contredit(s) par leur "
              "propre grille :")
        for cid, diag, conf, enonces in contredits:
            print(f"   {cid} — retenu « {diag} » ({conf}), or la grille énonce :")
            for source, texte in enonces:
                print(f"      {source} : « {texte[:160]} »")
        return 1

    vides = sorted(cid for cid, (diag, _) in parsed.items() if not diag)
    if vides:
        print(f"\nECHEC — {len(vides)} entrée(s) sans diagnostic : {vides[:8]}")
        return 1
    if part < SEUIL:
        print(f"\nECHEC — couverture {part} % sous le seuil de {SEUIL} %")
        return 1
    print("\nOK — table de diagnostics complète")
    return 0


if __name__ == "__main__":
    sys.exit(main())
