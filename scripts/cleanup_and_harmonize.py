import os
import re
from pathlib import Path

VAULT_ROOT = Path(r"d:\vault\my research")
studies_dir = VAULT_ROOT / "03 - Collective Literature Matrix" / "Studies"

# Keep the deep overhaul files (they have the exact scientific paper titles)
keep_files = [
    "Study-01-Palmitoylethanolamide-and-luteolin-ameliorate-deve.md",
    "Study-02-A-novel-composite-formulation-of-palmitoylethanola.md",
    "Study-03-Anti-inflammatory-activity-of-palmitoylethanolamid.md",
    "Study-04-Selective-amplification-of-glucocorticoid-anti-inf.md",
    "Study-05-Benefits-of-combining-piperine-with-prednisolone-i.md",
    "Study-06-Salvianolate-Ameliorates-Osteopenia-and-Improves-B.md",
    "Study-07-Micronized-ultramicronized-palmitoylethanolamide-d.md",
    "Study-08-The-anti-inflammatory-effects-of-palmitoylethanola.md",
    "Study-09-Palmitoylethanolamide-dampens-neuroinflammation-an.md",
    "Study-10-Effect-of-palmitoylethanolamide-on-inflammatory-an.md",
    "Study-11-Antioxidant-and-Angiostatic-Effect-of-Spirulina-pl.md",
    "Study-12-Effect-of-Losartan-in-Complete-Freund-s-Adjuvant-I.md",
    "Study-13-The-anti-inflammatory-effects-of-palmitoylethanola.md"
]

for f in studies_dir.glob("*.md"):
    if f.name not in keep_files:
        print(f"Removing old version: {f.name}")
        f.unlink()

# Fix Main-Protocol-7-Groups.md dosing strings
proto_file = VAULT_ROOT / "04 - Experimental Protocols & Pilot" / "Main-Protocol-7-Groups.md"
pt = proto_file.read_text(encoding="utf-8")
pt = pt.replace("m-PEA 50 mg/kg + Prednisolone 5 mg/kg", "m-PEA + Prednisolone (50 + 5 mg/kg)")
pt = pt.replace("m-PEA 100 mg/kg + Prednisolone 5 mg/kg", "m-PEA + Prednisolone (100 + 5 mg/kg)")
pt = pt.replace("m-PEA 200 mg/kg + Prednisolone 5 mg/kg", "m-PEA + Prednisolone (200 + 5 mg/kg)")
proto_file.write_text(pt, encoding="utf-8")

print("Cleanup and protocol dosing formatting complete.")
