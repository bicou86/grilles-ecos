"""Liste les paires d'items quasi identiques entre blocs pedagogiques."""
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

THRESHOLD = 0.72


def pairs_for(path):
    html = path.read_text(encoding="utf-8")
    items = []
    for name, _, _ in lib.BLOCKS:
        seg = lib.block_segment(html, name)
        if seg:
            items += [(name, t) for t in lib.list_items(seg)]
    out = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            b1, t1 = items[i]
            b2, t2 = items[j]
            if b1 == b2:
                continue
            ratio = SequenceMatcher(None, t1, t2).ratio()
            if ratio > THRESHOLD:
                out.append((round(ratio, 2), b1, t1, b2, t2))
    return sorted(out, reverse=True)


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    grand = 0
    for path in lib.grids():
        if only and only not in path.name:
            continue
        found = pairs_for(path)
        grand += len(found)
        if found:
            print(f"\n=== {path.name} — {len(found)} paire(s) ===")
            for ratio, b1, t1, b2, t2 in found:
                print(f"  [{ratio}] {b1} <-> {b2}")
                print(f"      A: {t1[:100]}")
                print(f"      B: {t2[:100]}")
    print(f"\nTOTAL : {grand} paire(s) quasi identiques")


if __name__ == "__main__":
    main()
