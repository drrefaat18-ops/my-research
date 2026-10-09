"""Add an empty '✍️ جملتك:' box at the end of every '### جملة' block in a brief file.

Idempotent: blocks that already have a box are skipped.
Usage: python scripts/add_boxes.py "08 - RA Repurposing Review/4.1b-PPAR-agonists.md"
"""
import sys

BOX = ["**✍️ جملتك:**", "```", "", "```", ""]


def add_boxes(lines):
    out, block = [], None  # block = lines of the current '### جملة' block

    def flush():
        if block is not None and not any("✍️ جملتك" in l for l in block):
            while block and block[-1] == "":
                block.pop()
            block.extend([""] + BOX)
        out.extend(block or [])

    for line in lines:
        if line.startswith("#"):
            flush()
            block = [line] if line.startswith("### جملة") else None
            if block is None:
                out.append(line)
        elif block is not None:
            block.append(line)
        else:
            out.append(line)
    flush()
    return out


if __name__ == "__main__":
    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    new = add_boxes(lines)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(new))
    print(f"boxes: {sum('✍️ جملتك' in l for l in new)} / blocks: {sum(l.startswith('### جملة') for l in new)}")
