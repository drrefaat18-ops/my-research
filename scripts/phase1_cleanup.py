"""
Phase 1: Foundation Clean-up
- Deletes orphaned zero-byte files from vault root
- Removes duplicate Paper- notes from Papers/ folder
- Removes Sheet8 (5) duplicate from Excel files
- Removes Study-13 duplicate note
- Removes redundant PEA/my stuff duplicate directory
"""
import pathlib, re, shutil, openpyxl

VAULT = pathlib.Path('d:/vault/my research')
SOURCES = VAULT / '00-Sources'

print("=== PART 1: Remove Orphaned Root Files ===")
for f in VAULT.glob('Study-*.md'):
    print(f"Deleting root orphan: {f.name} ({f.stat().st_size} bytes)")
    f.unlink()

print("\n=== PART 2: Deduplicate Paper Notes ===")
papers_dir = VAULT / '03 - Collective Literature Matrix' / 'Papers'
paper_notes = list(papers_dir.glob('Paper-*.md'))

from collections import defaultdict
by_50 = defaultdict(list)
for p in paper_notes:
    key = p.stem[6:56]
    by_50[key].append(p)

for key, files in by_50.items():
    if len(files) > 1:
        # Sort by filename length (keep the longest, most descriptive one)
        sorted_files = sorted(files, key=lambda x: (len(x.name), x.stat().st_size), reverse=True)
        canonical = sorted_files[0]
        duplicates = sorted_files[1:]
        print(f"Keeping canonical: {canonical.name}")
        for dup in duplicates:
            print(f"  Removing duplicate: {dup.name}")
            dup.unlink()

print("\n=== PART 3: Remove Sheet8 (5) duplicate from Excel ===")
for xlsx_path in SOURCES.rglob('*.xlsx'):
    try:
        wb = openpyxl.load_workbook(xlsx_path)
        if 'Sheet8 (5)' in wb.sheetnames:
            print(f"Removing Sheet8 (5) from {xlsx_path.name}")
            wb.remove(wb['Sheet8 (5)'])
            wb.save(xlsx_path)
    except Exception as e:
        print(f"Error handling {xlsx_path}: {e}")

print("\n=== PART 4: Remove Study-13 duplicate note ===")
s13 = VAULT / '03 - Collective Literature Matrix' / 'Studies' / 'Study-13-The-anti-inflammatory-effects-of-palmitoylethanola.md'
if s13.exists():
    print(f"Deleting duplicate Study-13: {s13.name}")
    s13.unlink()

print("\n=== PART 5: Remove PEA/my stuff redundant duplicate directory ===")
pea_my_stuff = SOURCES / 'PEA' / 'my stuff'
if pea_my_stuff.exists():
    print(f"Removing redundant clone directory: {pea_my_stuff}")
    shutil.rmtree(pea_my_stuff)

print("\nPart 1 complete.")
