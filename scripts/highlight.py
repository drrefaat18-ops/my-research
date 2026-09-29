"""Wrap key sentences in Obsidian ==highlights== inside paper .md files.
Usage: python highlight.py <phrases.json> <papers_dir>
phrases.json = {"Son2014": ["exact phrase 1", ...], ...}
Prints every phrase not found so it can be fixed (never edits anything else).
"""
import json
import os
import sys


def apply(text, phrase):
    if f"=={phrase}" in text:
        return text, True  # already highlighted
    i = text.find(phrase)
    if i < 0:
        return text, False
    return text[:i] + "==" + phrase + "==" + text[i + len(phrase):], True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        t, ok = apply("a b c", "b")
        assert ok and t == "a ==b== c" and apply(t, "b") == (t, True)
        print("self-check ok")
        sys.exit()
    phrases = json.load(open(sys.argv[1], encoding="utf-8"))
    for tag, items in phrases.items():
        path = os.path.join(sys.argv[2], tag + ".md")
        text = open(path, encoding="utf-8").read()
        done = 0
        for p in items:
            text, ok = apply(text, p)
            done += ok
            if not ok:
                print(f"MISS {tag}: {p[:80]}")
        open(path, "w", encoding="utf-8").write(text)
        print(f"{tag}: {done}/{len(items)}")
