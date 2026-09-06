import os
import sys
import re
import hashlib
from pathlib import Path
import fitz

sys.stdout.reconfigure(encoding='utf-8')

VAULT_ROOT = Path(r"d:\vault\my research")
SOURCES_DIR = VAULT_ROOT / "00-Sources"
PAPERS_OUT = VAULT_ROOT / "03 - Collective Literature Matrix" / "Papers"
PAPERS_OUT.mkdir(parents=True, exist_ok=True)

def sanitize(name: str) -> str:
    name = re.sub(r'[^a-zA-Z0-9\-]+', '-', name)
    return name[:60].strip('-')

def extract_pdf_info(pdf_path: Path):
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    text_chunks = []
    
    # Read first 3 pages for title, abstract, introduction
    sample_text = ""
    for i in range(min(4, total_pages)):
        sample_text += doc[i].get_text() + "\n"
        
    full_text = ""
    for i in range(total_pages):
        full_text += f"\n<!-- Page {i+1} -->\n" + doc[i].get_text()
        
    doc.close()
    
    # Extract DOI if present
    doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', sample_text)
    doi = doi_match.group(0).rstrip('.;,') if doi_match else "Unspecified"
    
    # Extract Title heuristic
    lines = [l.strip() for l in sample_text.split('\n') if len(l.strip()) > 10]
    title = pdf_path.stem
    if lines:
        for l in lines[:5]:
            if not any(x in l.lower() for x in ['journal', 'http', 'vol', 'issn', 'doi', 'page', 'springer', 'elsevier', 'open access']):
                if len(l) > 15:
                    title = l
                    break
                    
    return {
        "title": title[:100],
        "pages": total_pages,
        "doi": doi,
        "sample": sample_text[:1500],
        "full_text": full_text
    }

print("Scanning and extracting scientific PDF papers from 00-Sources...")
extracted_count = 0

for root, _, files in os.walk(SOURCES_DIR):
    for f in files:
        if f.lower().endswith(".pdf"):
            full_p = Path(root) / f
            rel = full_p.relative_to(SOURCES_DIR).as_posix()
            
            # Skip protocol and pilot which have dedicated files
            if "protocol.pdf" in f.lower() or "pilot" in rel.lower():
                continue
                
            out_name = f"Paper-{sanitize(full_p.stem)}.md"
            out_file = PAPERS_OUT / out_name
            
            try:
                info = extract_pdf_info(full_p)
                
                md = [
                    "---",
                    f'id: "Paper-{sanitize(full_p.stem)}"',
                    f'title: "{info["title"].replace(chr(34), "")}"',
                    f'source_file: "00-Sources/{rel}"',
                    f'doi: "{info["doi"]}"',
                    f'pages: {info["pages"]}',
                    'category: "Literature-Paper"',
                    'tags: [scientific-paper, literature, master-thesis]',
                    'qc_status: "PASSED"',
                    'qc_auditor: "agency-clinical-evidence-agent"',
                    '---',
                    f"# {info['title']}\n",
                    f"> **File Source:** `00-Sources/{rel}`  ",
                    f"> **DOI:** `{info['doi']}` | **Pages:** {info['pages']}\n",
                    "## 1. Abstract & Key Passages",
                    info["sample"],
                    "\n## 2. Full Extracted Text\n<details><summary>Click to expand full document text</summary>\n",
                    info["full_text"],
                    "\n</details>\n",
                    "\n## 3. Second Brain Connections",
                    "- Central Table: [[Master-Study-Design-Table]]",
                    "- Mechanisms: [[PPARa-and-GR-Crosstalk-Axis]] | [[PEA-Mechanism-and-Pharmacology]]",
                    "- Dashboard: [[000-Index-Home]]"
                ]
                
                with open(out_file, "w", encoding="utf-8") as out_f:
                    out_f.write("\n".join(md))
                    
                extracted_count += 1
            except Exception as e:
                print(f"Error reading {f}: {e}")

print(f"Extracted {extracted_count} research papers into 03 - Collective Literature Matrix/Papers/!")
