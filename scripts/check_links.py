"""Check every [[papers/X#^id|...]] link in dictation briefs: file exists, id exists,
the block is highlighted and short. Prints each target block so facts can be eyeballed.
Usage: python check_links.py <review_dir> <brief.md> [...]
Exit 1 if any link is broken.
"""
import os
import re
import sys

LINK = re.compile(r"\[\[papers/([^#|\]]+)#\^([\w-]+)(?:\|[^\]]*)?\]\]")


def blocks(path):
    text = open(path, encoding="utf-8").read()
    res = {}
    for para in re.split(r"\n[ \t]*\n", text):
        for bid in re.findall(r"[ \t]\^([\w-]+)[ \t]*$", para, re.M):
            res.setdefault(bid, []).append(para.strip())
    return res


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # Windows console chokes on ✅
    review, briefs = sys.argv[1], sys.argv[2:]
    cache, bad = {}, 0
    for b in briefs:
        for n, line in enumerate(open(b, encoding="utf-8"), 1):
            for tag, bid in LINK.findall(line):
                p = os.path.join(review, "papers", tag + ".md")
                if not os.path.exists(p):
                    print(f"❌ {os.path.basename(b)}:{n} missing paper {tag}")
                    bad += 1
                    continue
                cache.setdefault(p, blocks(p))
                hit = cache[p].get(bid)
                if not hit:
                    print(f"❌ {os.path.basename(b)}:{n} {tag}#^{bid} id not found")
                    bad += 1
                elif len(hit) > 1:
                    print(f"❌ {os.path.basename(b)}:{n} {tag}#^{bid} id duplicated")
                    bad += 1
                else:
                    blk = hit[0]
                    warn = "" if "==" in blk and len(blk) <= 600 else "  ⚠️ not highlighted or block too long"
                    print(f"✅ {os.path.basename(b)}:{n} {tag}#^{bid}{warn}\n    {blk[:300]}")
                    bad += bool(warn)
    print("broken/weak:", bad)
    sys.exit(1 if bad else 0)
