"""Propose les entrees de vocabulaire d'une SSP non encore curee. Sortie 0.

    python3 scripts/memento/propose_vocabulaire.py

AUCUNE FAMILLE NOUVELLE. Ce script n'invente rien : il applique aux SSP qui
n'ont pas encore d'entree les familles de synonymes DEJA ADJUGEES ET RELUES en
tache 10. Une famille nouvelle est un jugement clinique neuf, qu'aucun controle
ne peut rattraper quand les grilles sont disjointes ; une famille deja adjugee
est un jugement deja rendu. Chaque application reste jugee SEPAREMENT par les
neuf proprietes de check_vocabulaire.

LES ORDRES DE PREFERENCE SONT DECLARES A LA MAIN, ET C'EST LE POINT DELICAT.
Une premiere version les DERIVAIT d'un comptage (« est cible souvent, cle
rarement »). Un comptage encode des frequences, pas du sens : il mettait
« Antecedents medicaux » devant « Antecedents medicaux personnels » — trois
entrees inversees — et remontait « Antecedents familiaux cardiovasculaires » en
TETE de sa famille, ce qui l'aurait propage partout alors que c'est un
RETRECISSEMENT local a HTA. Cinq familles sont declarees non propageables.

LE FILTRE DE REFUS PORTE SUR TOUT ECART NOMMANT LA SSP ET LA CLE, et non sur le
seul prefixe « SSP / « cle » » : `collisions()` ecrit sous une autre forme
(« SSP — RAPPROCHEMENT ABUSIF »), si bien que la premiere redaction classait
une collision en « ecart etranger » — donc la CONSERVAIT — des lors qu'elle
n'etait pas aussi inerte. Le motif affiche est desormais LE PLUS GRAVE des
motifs observes, pour la meme raison qu'en tete de
check_mutations_vocabulaire.py.

CE SCRIPT NE PROPOSE QUE : la decision reste humaine, et chaque proposition
doit etre relue sur les grilles avant d'entrer dans docs/ecos-vocabulaire.yaml.
Il ne l'ecrit pas.

DETERMINISME : tout est trie, aucune date, aucun aleatoire.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento                                      # noqa: E402
import check_vocabulaire                                  # noqa: E402
import lib_ssp                                            # noqa: E402
import lib_vocabulaire                                    # noqa: E402
import lib_yaml                                           # noqa: E402

# Du plus retenu au moins retenu. La cible est le premier membre PRESENT dans la
# SSP ; les autres presents deviennent des cles.
ORDRES = [
    ["Anamnèse gynécologique", "Anamnèse gynécologique (si applicable)"],
    ["Anamnèse sociale", "Situation sociale"],
    ["Antécédents chirurgicaux", "Opérations antérieures"],
    ["Antécédents familiaux", "Anamnèse familiale"],
    ["Antécédents médicaux personnels", "Antécédents médicaux", "Antécédents personnels"],
    ["Auscultation pulmonaire", "Examen pulmonaire - Auscultation"],
    ["Caractérisation de la toux", "Caractéristiques de la toux"],
    ["Diagnostic principal", "Diagnostic principal évoqué", "Diagnostic principal suspecté"],
    ["Diagnostics différentiels", "Diagnostics différentiels évoqués",
     "Évoque un diagnostic différentiel cohérent", "Diagnostics différentiels (au moins 2-3)"],
    ["Examen abdominal", "Examen abdominal complet"],
    ["Examens biologiques", "Laboratoire"],
    ["Examens complémentaires", "Examens complémentaires proposés"],
    ["Examens complémentaires urgents", "Examens complémentaires en urgence"],
    ["Habitudes et mode de vie", "Habitudes", "Habitudes de vie"],
    ["Motif de consultation principal", "Motif de consultation", "Motif principal"],
    ["Médicaments actuels", "Médication actuelle", "Médicaments"],
    ["Palpation des ganglions lymphatiques", "Palpation des aires ganglionnaires"],
    ["Palpation des pouls périphériques", "Pouls périphériques"],
    ["Planification du suivi", "Plan de suivi"],
    ["Signes vitaux", "Paramètres vitaux"],
    ["Symptômes associés", "Symptômes actuels", "Symptômes d'accompagnement"],
    ["Symptômes digestifs", "Anamnèse digestive"],
    ["Symptômes généraux", "Anamnèse générale"],
    ["Tabagisme", "Tabac"],
    ["Toucher rectal", "Evoque un toucher rectal", "Toucher rectal si indiqué",
     "Évoque le toucher rectal"],
]

# NON PROPAGEABLES, et pourquoi.
#   Antihypertenseurs (prescrits)      — « prescrits » distingue prescrit et pris ;
#   Antécédents familiaux CV           — retrecissement local a HTA (tache 10 §3-1) ;
#   Auscultation cardiaque (rythme...) — la parenthese est un axe de contenu ;
#   Plusieurs mesures / Au moins 2     — seuil de cotation local a HTA ;
#   Médicaments -> Traitements actuels — « traitement » deborde « medicament »
#                                        (non medicamenteux) : axe de contenu.

table = lib_yaml.lire_groupe(check_vocabulaire.TABLE)
groupes = build_memento.par_ssp(None)
lot1 = lib_ssp.lot_prioritaire()
inventaire = lib_vocabulaire.libelles_par_ssp(groupes)
perimetre = sorted(s for s, v in groupes.items()
                   if s not in lot1 and len(v) >= 2 and s not in table)

propositions = {}
for ssp in perimetre:
    for ordre in ORDRES:
        presents = [m for m in ordre if m in inventaire[ssp]]
        if len(presents) < 2:
            continue
        cible = presents[0]
        for k in presents[1:]:
            propositions.setdefault(ssp, {})[k] = cible

print(f"{sum(len(v) for v in propositions.values())} propositions brutes sur "
      f"{len(propositions)} SSP")

courant = {s: dict(e) for s, e in propositions.items()}
tour = 0
while True:
    tour += 1
    essai = {s: dict(e) for s, e in table.items()}
    for s, e in courant.items():
        essai.setdefault(s, {}).update(e)
    ecarts = check_vocabulaire.verifier(essai, inventaire, groupes)
    # TOUT ecart qui NOMME la SSP et la cle — voir le docstring.
    miens = [(s, k, e) for e in ecarts for s, ent in courant.items() for k in ent
             if s in e and k in e]
    autres = [e for e in ecarts
              if not any(s in e and k in e
                         for s, ent in courant.items() for k in ent)]
    if not miens:
        print(f"tour {tour} : aucun refus. Ecarts etrangers : {len(autres)}")
        for e in autres[:10]:
            print("   ⚠", e[:180])
        break
    print(f"tour {tour} : {len(miens)} refus")
    # LE PLUS GRAVE DES MOTIFS, pas le premier vu : cinq refus du lot 2
    # collisionnent ET sont inertes, et « inerte » se lit « inoffensif ».
    for s, k in sorted({(s, k) for s, k, _ in miens}):
        siens = [e for _s, _k, e in miens if (_s, _k) == (s, k)]
        if any("RAPPROCHEMENT ABUSIF" in e for e in siens):
            motif = "COLLISION (propriete 8) — aurait effacé une distinction"
        elif any("ne rapproche aucune grille" in e for e in siens):
            motif = "inerte (propriete 7)"
        else:
            motif = siens[0][:150]
        print(f"   ⛔ {s} / « {k} » — {motif}")
        courant[s].pop(k, None)
    courant = {s: e for s, e in courant.items() if e}

print(f"\n=== RETENUES : {sum(len(v) for v in courant.values())} entrees sur "
      f"{len(courant)} SSP ===")
for s in sorted(courant):
    print(f'"{s}":   [{len(groupes[s])} grilles]')
    for k in sorted(courant[s]):
        porteurs_k = sorted(inventaire[s][k])
        porteurs_v = sorted(inventaire[s][courant[s][k]])
        print(f'  "{k}": "{courant[s][k]}"')
        print(f'        {k!r} : {porteurs_k}')
        print(f'        {courant[s][k]!r} : {porteurs_v}')
