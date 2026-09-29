"""Make every ==highlight== in a paper .md its own Obsidian block with its own ^id,
so a [[paper#^id]] link lands exactly on that sentence (not the top of a long paragraph).
Also unwraps junk highlights (empty / punctuation only). Idempotent.
Usage: python isolate_blocks.py <paper.md> [...]
"""
import re
import sys

HL = re.compile(r"==((?:(?!\n\s*\n).)+?)==", re.S)
ID = re.compile(r"[ \t]+\^([\w-]+)[ \t]*$", re.M)


def process(path):
    tag = path.replace("\\", "/").split("/")[-1][:-3].lower()
    text = open(path, encoding="utf-8").read()
    front = ""
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4) + 5
        front, text = text[:end], text[end:]
    nums = [int(n) for n in re.findall(rf"\^{re.escape(tag)}-(\d+)\b", text)]
    nxt = [max(nums, default=0)]

    def new_id():
        nxt[0] += 1
        return f"{tag}-{nxt[0]}"

    out, skipped = [], 0
    for para in re.split(r"\n[ \t]*\n", text):
        # junk highlights → plain text
        para = HL.sub(lambda m: m.group(0) if re.search(r"\w{2}", m.group(1)) else m.group(1), para)
        if not HL.search(para):
            out.append(para)
            continue
        lines = para.split("\n")
        if all(l.lstrip().startswith("|") for l in lines if l.strip()):
            out.append(para)  # ponytail: markdown tables can't hold inner block ids; left as-is
            skipped += 1
            continue
        quote = all(l.startswith(">") for l in lines if l.strip())
        body = "\n".join(re.sub(r"^>\s?", "", l) for l in lines) if quote else para
        old = ID.findall(body)
        body = ID.sub("", body)
        pieces, pos = [], 0
        for i, m in enumerate(HL.finditer(body)):
            pre = body[pos:m.start()].strip()
            if pre:
                pieces.append(pre)
            bid = old[i] if i < len(old) else new_id()
            pieces.append("==" + " ".join(m.group(1).split()) + f"== ^{bid}")
            pos = m.end()
        post = body[pos:].strip()
        if post:
            pieces.append(post)
        if quote:
            pieces = ["\n".join("> " + l for l in p.split("\n")) for p in pieces]
        out.append("\n\n".join(pieces))
    open(path, "w", encoding="utf-8").write(front + "\n\n".join(out))
    return skipped


if __name__ == "__main__":
    for p in sys.argv[1:]:
        s = process(p)
        print(p, "ok" + (f" ({s} table highlight(s) left unsplit)" if s else ""))
