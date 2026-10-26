"""Failure library runner: replays every real failure as a regression case (PRINCIPLES 14).

One JSON file per failure in harness/evals/ (any name ending .json):
  {"id": "E001", "title": "what went wrong", "date": "YYYY-MM-DD", "origin": "where it was caught",
   "cmd": ["python", "harness/gate.py", "{case_dir}/bad-note.md"],   # {case_dir} = harness/evals/<id>/
   "stdin": "optional text", "exit": 1, "expect": ["substring the output must contain"], "absent": ["must not contain"]}
Put the failing input next to it in harness/evals/<id>/ (the bad output that slipped through once).
Run after every harness change and at step-done. Exit 1 if any case fails. Stdlib only.
Usage: python harness/evals.py [-q]   |   python harness/evals.py --selftest
TEMPLATE: copy to harness/evals.py; call main(quiet=True) from the step-done check.
"""
import glob, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)   # TEMPLATE: project root = parent of harness/


def run_case(c, evals_dir):
    case_dir = os.path.join(evals_dir, c["id"])
    cmd = [a.replace("{case_dir}", case_dir) for a in c["cmd"]]
    r = subprocess.run(cmd, cwd=ROOT, input=c.get("stdin", ""), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=120)
    out = r.stdout + r.stderr
    miss = [] if c.get("exit") is None or r.returncode == c["exit"] else [f"exit {r.returncode}, want {c['exit']}"]
    miss += [f"missing '{e}'" for e in c.get("expect", []) if e not in out]
    miss += [f"unexpected '{a}'" for a in c.get("absent", []) if a in out]
    return miss, out


def main(quiet=False, evals_dir=os.path.join(HERE, "evals")):
    cases = [json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(evals_dir, "*.json")))]
    failed = 0
    for c in cases:
        try:
            miss, out = run_case(c, evals_dir)
        except Exception as e:
            miss, out = [f"crash {e!r}"], ""
        failed += bool(miss)
        if miss or not quiet:
            print(f"{c['id']} {'FAIL' if miss else 'pass'}  {c['title']}"
                  + (f"  -- {'; '.join(miss)} | got: {out.strip()[:200]}" if miss else ""))
    print(f"EVALS: known failures {len(cases)} | pass {len(cases) - failed} | still failing {failed}")
    return 1 if failed else 0


def selftest():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "E001"))
    open(os.path.join(d, "E001", "bad.txt"), "w", encoding="utf-8").write("Launch date: Sep 18")
    ok = {"id": "E001", "title": "check flags an unsourced date", "cmd": [sys.executable, "-c",
          "import sys; t=open(sys.argv[1]).read(); print('unsourced date' if 'Sep' in t else 'ok'); sys.exit('Sep' in t)",
          "{case_dir}/bad.txt"], "exit": 1, "expect": ["unsourced date"]}
    bad = dict(ok, id="E002", expect=["something else"])
    os.makedirs(os.path.join(d, "E002"))
    open(os.path.join(d, "E002", "bad.txt"), "w", encoding="utf-8").write("Sep")
    for c in (ok, bad):
        json.dump(c, open(os.path.join(d, c["id"] + ".json"), "w", encoding="utf-8"))
    assert run_case(ok, d)[0] == [] and run_case(bad, d)[0] == ["missing 'something else'"]
    assert main(quiet=True, evals_dir=d) == 1
    print("evals selftest ok")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    sys.exit(main("-q" in sys.argv))
