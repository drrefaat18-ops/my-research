"""Give every ==highlighted== paragraph in paper .md files an Obsidian block id,
then write a clickable "key sentences" section into each dictation brief.
Usage: python link_highlights.py <review_dir> [Tag ...]   (no tags = all papers)
"""
import glob
import os
import re
import sys

START, END = "<!-- key-sentences:start -->", "<!-- key-sentences:end -->"


def tag_blocks(path, tag):
    lines = open(path, encoding="utf-8").read().split("\n")
    out, n = [], 0
    for i, line in enumerate(lines):
        if "==" in line and re.search(r"==[^=]+==", line):
            m = re.search(r"\s\^([\w-]+)$", line)
            if m:
                bid = m.group(1)
            else:
                n += 1
                bid = f"{tag.lower()}-{n}"
                while f"^{bid}" in "\n".join(lines):
                    n += 1
                    bid = f"{tag.lower()}-{n}"
                lines[i] = line + f" ^{bid}"
            for h in re.findall(r"==([^=]+)==", lines[i]):
                out.append((bid, h))
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return out


def section(tags, index):
    rows = [START, "## 🔗 الجمل المهمة في الأبحاث (اضغط على الجملة تروح لمكانها)", ""]
    for t in tags:
        if index.get(t):
            rows.append(f"**{t}**")
            for bid, h in index[t]:
                alias = h.replace("[", "(").replace("]", ")").replace("|", "/")  # brackets break wikilink aliases
                rows.append(f"- [[papers/{t}#^{bid}|{alias[:90]}{'…' if len(alias) > 90 else ''}]]")
            rows.append("")
    return "\n".join(rows + [END])


if __name__ == "__main__":
    review = sys.argv[1]
    papers = os.path.join(review, "papers")
    only = set(sys.argv[2:])
    index = {}
    for p in glob.glob(os.path.join(papers, "*.md")):
        t = os.path.basename(p)[:-3]
        if only and t not in only:
            continue
        index[t] = tag_blocks(p, t)
    for brief in glob.glob(os.path.join(review, "[0-9]*-*.md")):
        text = open(brief, encoding="utf-8").read()
        tags = [t for t in dict.fromkeys(re.findall(r"`\[([A-Za-z]+\d{4}[a-z]?)\]`", text)) if index.get(t)]
        if not tags:
            continue
        text = re.sub(re.escape(START) + ".*?" + re.escape(END) + r"\n?", "", text, flags=re.S)
        anchor = "\n---\n\n## ✍️"
        new = section(tags, index)
        text = text.replace(anchor, "\n" + new + "\n" + anchor, 1) if anchor in text else text + "\n\n" + new + "\n"
        open(brief, "w", encoding="utf-8").write(text)
        print(os.path.basename(brief), "→", ", ".join(f"{t}({len(index[t])})" for t in tags))
