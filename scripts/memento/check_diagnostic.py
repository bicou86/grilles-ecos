"""Couverture et coherence de la resolution du diagnostic. Sortie 1 si ecart."""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_diagnostic

SEUIL = 90  # part minimale de cas dont le diagnostic est resolu (plancher, pas cible)


def _corpus(cid):
    """Prefixe de corpus d'un identifiant de cas ('AMBOSS-12' -> 'AMBOSS')."""
    return cid.split("-")[0]


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
