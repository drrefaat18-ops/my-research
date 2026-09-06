import os
import re
from pathlib import Path

VAULT_ROOT = Path(r"d:\vault\my research")

# 1. Map Study IDs to exact filenames
studies_dir = VAULT_ROOT / "03 - Collective Literature Matrix" / "Studies"
study_map = {}
for sf in studies_dir.glob("*.md"):
    # Extract Study-XX
    m = re.match(r'(Study-\d{2})', sf.stem)
    if m:
        study_map[m.group(1)] = sf.stem

print("Study map:", study_map)

# 2. Fix Home-Index.md
home_file = VAULT_ROOT / "Home-Index.md"
if home_file.exists():
    content = home_file.read_text(encoding="utf-8")
    
    # Replace ASCII diagram links with plain text
    content = content.replace("[[000-Index-Home]]", "`Home-Index`")
    content = content.replace("[[01 - Rationale]]", "`01 - Rationale`")
    content = content.replace("[[02 - Mechanisms]]", "`02 - Mechanisms`")
    content = content.replace("[[03 - Literature Matrix]]", "`03 - Literature Matrix`")
    content = content.replace("[[04 - Protocols]]", "`04 - Protocols`")
    content = content.replace("[[05 - Comparators]]", "`05 - Comparators`")
    content = content.replace("[[06 - Defense & Pub]]", "`06 - Defense & Pub`")
    
    # Replace study links with exact filenames
    for s_id, exact_stem in study_map.items():
        # Match [[Study-XX...|Label]] or [[Study-XX...]]
        content = re.sub(rf'\[\[{s_id}[^\]\|]*(\|[^\]]+)?\]\]', rf'[[{exact_stem}\1]]', content)
        
    home_file.write_text(content, encoding="utf-8")
    print("Fixed Home-Index.md")

# 3. Fix all files referencing [[000-Index-Home]]
for mf in VAULT_ROOT.rglob("*.md"):
    if ".obsidian" in mf.as_posix() or ".system_generated" in mf.as_posix():
        continue
    c = mf.read_text(encoding="utf-8", errors="ignore")
    if "000-Index-Home" in c or "[[Note]]" in c:
        c = c.replace("[[000-Index-Home]]", "[[Home-Index]]")
        c = c.replace("[[01-Atlas/000-Index-Home]]", "[[Home-Index]]")
        c = c.replace("[[Note]]", "[[Home-Index]]")
        mf.write_text(c, encoding="utf-8")

print("Link remediation completed.")
