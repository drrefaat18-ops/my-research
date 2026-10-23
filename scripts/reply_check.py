"""Stop hook: Claude's reply must not mix Arabic and English on one line (user preference,
confirmed lesson; Arabic/English on one line scrambles word order on the user's screen).

A line with Arabic letters may not also hold a Latin word (2+ letters), whether plain, in
backticks or in a link. English goes on its own line or in a fenced code block; table cells
are checked one by one. Findings -> exit 2 once, so Claude rewrites the reply; on the retry
(stop_hook_active) it never blocks again. A crash never blocks (exit 0).

Usage: registered as a Stop hook in .claude/settings.json.
    python scripts/reply_check.py --check reply.txt    |    python scripts/reply_check.py --demo
"""
import json, re, sys

ARABIC = re.compile(r"[؀-ۿ]")
LATIN = re.compile(r"[A-Za-z]{2,}")


def mixed(text):
    """Lines (or table cells) that hold Arabic and a Latin word together."""
    out, fence = [], False
    for ln in text.splitlines():
        if ln.lstrip().startswith(("```", "~~~")):
            fence = not fence
            continue
        if fence:
            continue
        ln = re.sub(r"\]\(<[^>]*>\)|\]\([^)]*\)", "]", ln)  # link targets are not shown on screen
        cells = ln.strip().strip("|").split("|") if ln.lstrip().startswith("|") else [ln]
        out += [c.strip() for c in cells if ARABIC.search(c) and LATIN.search(c)]
    return out


def last_reply(transcript_path):
    """Text Claude wrote since the user's last real prompt (tool results are not prompts)."""
    texts = []
    for raw in open(transcript_path, encoding="utf-8"):
        try:
            e = json.loads(raw)
        except ValueError:
            continue
        msg = e.get("message") or {}
        content = msg.get("content")
        if e.get("type") == "user":
            real = isinstance(content, str) or any(
                isinstance(b, dict) and b.get("type") == "text" for b in content or [])
            if real:
                texts = []
        elif e.get("type") == "assistant" and isinstance(content, list):
            texts += [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
    return "\n".join(texts)


def demo():
    reply = ("Picked inline role: research-synthesist\n"
             "الخطوة الجاية هي ١٩.\n"
             "الملف اتعدل: `cite_check.py`\n"
             "```\npython scripts/evals.py\n```\n"
             "| الفحص | النتيجة |\n|---|---|\n| ledger | تمام |\n"
             "شغلت evals وطلعت صفر\n"
             "[ملف الخطة](<D:\\vault\\my research\\START-HERE.md>)\n")
    got = mixed(reply)
    assert got == ["الملف اتعدل: `cite_check.py`", "شغلت evals وطلعت صفر"], got
    print("demo ok")


def main():
    if sys.argv[1:] == ["--demo"]:
        return demo()
    if sys.argv[1:2] == ["--check"]:  # a saved reply as plain text (evals)
        bad = mixed(open(sys.argv[2], encoding="utf-8").read())
        print("\n".join(f"mixed: {b}" for b in bad) or "reply clean")
        return 1 if bad else 0
    ev = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    if ev.get("hook_event_name") != "Stop" or ev.get("stop_hook_active"):
        return 0
    bad = mixed(last_reply(ev.get("transcript_path", "")))
    if not bad:
        return 0
    sys.stderr.reconfigure(encoding="utf-8")
    sys.stderr.write("reply_check: your reply mixes Arabic and English on one line (user can't read it: "
                     "RTL/LTR scrambles). Send the reply again with every English word, file name, "
                     "command or tag on its own line or in a code block:\n"
                     + "\n".join(f"  - {b[:100]}" for b in bad[:8]) + "\n")
    return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        sys.exit(main())
    except Exception as e:  # ponytail: never block the session on a hook bug; say so instead
        print(f"reply_check error (skipped): {e!r}", file=sys.stderr)
        sys.exit(0)
