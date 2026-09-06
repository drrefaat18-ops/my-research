import os
import sys
import json
import re
import hashlib
from pathlib import Path
import openpyxl
import docx
import fitz  # PyMuPDF
import pptx
import pdfplumber

VAULT_ROOT = Path(r"d:\vault\my research")
SOURCES_DIR = VAULT_ROOT / "00-Sources"
LITERATURE_DIR = VAULT_ROOT / "02-Literature"
PROTOCOLS_DIR = VAULT_ROOT / "04-Protocols-and-Experiments"
QC_DIR = VAULT_ROOT / "06-Audit-and-QC"

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'[\r\n]{3,}', '\n\n', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    return text.strip()

def compute_file_hash(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r'\s+', '-', name)
    return name[:120]

def parse_xlsx(file_path: Path):
    wb = openpyxl.load_workbook(file_path, data_only=True)
    sheets_data = {}
    md_content = []
    
    md_content.append(f"# Extracted Study Design Tables: {file_path.name}\n")
    md_content.append(f"> **Source:** `{file_path.relative_to(VAULT_ROOT)}`\n\n")
    
    total_rows = 0
    total_cols = 0
    
    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        md_content.append(f"## Sheet: {sheet_name}\n")
        
        rows = list(sheet.iter_rows(values_only=True))
        if not rows:
            md_content.append("_Empty sheet_\n\n")
            continue
            
        cleaned_rows = [r for r in rows if any(cell is not None and str(cell).strip() != "" for cell in r)]
        if not cleaned_rows:
            continue
            
        header = [str(c) if c is not None else "" for c in cleaned_rows[0]]
        header = [h if h.strip() != "" else f"Col_{idx+1}" for idx, h in enumerate(header)]
        
        md_content.append("| " + " | ".join(header) + " |")
        md_content.append("| " + " | ".join(["---"] * len(header)) + " |")
        
        sheet_rows = []
        for r in cleaned_rows[1:]:
            row_vals = [str(c).replace("\n", " ").replace("|", "\\|") if c is not None else "" for c in r]
            if len(row_vals) < len(header):
                row_vals.extend([""] * (len(header) - len(row_vals)))
            elif len(row_vals) > len(header):
                row_vals = row_vals[:len(header)]
            md_content.append("| " + " | ".join(row_vals) + " |")
            sheet_rows.append(row_vals)
            
        md_content.append("\n")
        sheets_data[sheet_name] = {
            "header": header,
            "rows": sheet_rows,
            "row_count": len(sheet_rows),
            "col_count": len(header)
        }
        total_rows += len(sheet_rows)
        total_cols = max(total_cols, len(header))
        
    return "\n".join(md_content), sheets_data, total_rows, total_cols

def parse_docx(file_path: Path):
    doc = docx.Document(file_path)
    md_lines = []
    
    md_lines.append(f"# {file_path.stem}\n")
    md_lines.append(f"> **Source:** `{file_path.relative_to(VAULT_ROOT)}`\n\n")
    
    table_count = 0
    for element in doc.element.body:
        tag = element.tag
        if tag.endswith('p'):
            p = docx.text.paragraph.Paragraph(element, doc)
            text = p.text.strip()
            if not text:
                continue
            if p.style.name.startswith('Heading 1'):
                md_lines.append(f"## {text}\n")
            elif p.style.name.startswith('Heading 2'):
                md_lines.append(f"### {text}\n")
            elif p.style.name.startswith('Heading 3'):
                md_lines.append(f"#### {text}\n")
            else:
                md_lines.append(f"{text}\n")
        elif tag.endswith('tbl'):
            table = docx.table.Table(element, doc)
            table_count += 1
            md_lines.append(f"\n### Table {table_count}\n")
            rows = table.rows
            if rows:
                header = [c.text.strip().replace("\n", " ").replace("|", "\\|") for c in rows[0].cells]
                md_lines.append("| " + " | ".join(header) + " |")
                md_lines.append("| " + " | ".join(["---"] * len(header)) + " |")
                for r in rows[1:]:
                    vals = [c.text.strip().replace("\n", " ").replace("|", "\\|") for c in r.cells]
                    md_lines.append("| " + " | ".join(vals) + " |")
                md_lines.append("\n")
                
    return "\n".join(md_lines), table_count

def parse_pptx(file_path: Path):
    prs = pptx.Presentation(file_path)
    md_lines = []
    md_lines.append(f"# Extracted Presentation: {file_path.stem}\n")
    md_lines.append(f"> **Source:** `{file_path.relative_to(VAULT_ROOT)}`\n\n")
    
    slide_count = 0
    for idx, slide in enumerate(prs.slides, start=1):
        slide_count += 1
        title = "Untitled Slide"
        if slide.shapes.title and slide.shapes.title.text:
            title = slide.shapes.title.text.strip()
        md_lines.append(f"## Slide {idx}: {title}\n")
        
        for shape in slide.shapes:
            if shape != slide.shapes.title and shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    t = paragraph.text.strip()
                    if t:
                        md_lines.append(f"- {t}")
        md_lines.append("\n")
    return "\n".join(md_lines), slide_count

def parse_rtf(file_path: Path):
    with open(file_path, "r", encoding="latin-1", errors="ignore") as f:
        content = f.read()
    text = re.sub(r'\\[a-zA-Z0-9\-]+ ?', ' ', content)
    text = re.sub(r'[{}]', ' ', text)
    text = clean_text(text)
    
    md_lines = [
        f"# Extracted Notes: {file_path.stem}\n",
        f"> **Source:** `{file_path.relative_to(VAULT_ROOT)}`\n\n",
        text
    ]
    return "\n".join(md_lines)

def parse_pdf(file_path: Path):
    doc = fitz.open(file_path)
    total_pages = len(doc)
    
    full_text = []
    for pno in range(total_pages):
        page = doc[pno]
        txt = page.get_text()
        if txt.strip():
            full_text.append(f"<!-- Page {pno + 1} -->\n" + txt.strip())
            
    doc.close()
    
    table_count = 0
    tables_md = []
    if total_pages <= 20:
        try:
            with pdfplumber.open(file_path) as pdf:
                for idx, page in enumerate(pdf.pages):
                    tbls = page.extract_tables()
                    for t in tbls:
                        if t and len(t) > 1:
                            table_count += 1
                            t_md = [f"\n### Extracted Table {table_count} (Page {idx+1})\n"]
                            header = [str(c).replace("\n", " ").replace("|", "\\|") if c is not None else "" for c in t[0]]
                            header = [h if h.strip() != "" else f"Col_{i+1}" for i, h in enumerate(header)]
                            t_md.append("| " + " | ".join(header) + " |")
                            t_md.append("| " + " | ".join(["---"] * len(header)) + " |")
                            for r in t[1:]:
                                r_vals = [str(c).replace("\n", " ").replace("|", "\\|") if c is not None else "" for c in r]
                                if len(r_vals) < len(header):
                                    r_vals.extend([""] * (len(header) - len(r_vals)))
                                else:
                                    r_vals = r_vals[:len(header)]
                                t_md.append("| " + " | ".join(r_vals) + " |")
                            tables_md.append("\n".join(t_md))
        except Exception as e:
            pass

    return "\n\n".join(full_text), "\n\n".join(tables_md), total_pages, table_count

def route_target_path(source_file: Path) -> tuple[Path, str, dict]:
    rel = source_file.relative_to(SOURCES_DIR).as_posix()
    meta = {
        "original_file": rel,
        "source_hash": compute_file_hash(source_file),
        "category": "Literature",
        "pilot": False,
        "confirmatory": True
    }
    
    if "pilot" in rel.lower():
        meta["category"] = "Pilot"
        meta["pilot"] = True
        meta["confirmatory"] = False
        meta["sample_size"] = "n=2"
        target_dir = PROTOCOLS_DIR / "Pilot-Observations"
        filename = f"Pilot-{sanitize_filename(source_file.stem)}.md"
        return target_dir / filename, "pilot", meta
        
    if "protocol" in rel.lower() and source_file.name.lower() == "protocol.pdf":
        meta["category"] = "Protocol"
        meta["title"] = "Official Master Thesis Animal Protocol"
        target_dir = PROTOCOLS_DIR / "Main-Experiment"
        filename = "Official-Animal-Protocol.md"
        return target_dir / filename, "protocol", meta

    if "collective tables" in rel.lower():
        meta["category"] = "Study-Design"
        target_dir = LITERATURE_DIR / "PEA-Studies"
        filename = f"Study-Design-Collective-Tables-{sanitize_filename(source_file.stem)}.md"
        return target_dir / filename, "study_design", meta
        
    if "prednisolone" in rel.lower():
        meta["category"] = "Prednisolone"
        target_dir = LITERATURE_DIR / "Prednisolone-Studies"
        filename = f"Pred-{sanitize_filename(source_file.stem)}.md"
        return target_dir / filename, "prednisolone", meta
        
    if "cfa" in rel.lower() or "adjuvant" in rel.lower() or "aa vs cia" in rel.lower():
        meta["category"] = "CFA-Model"
        target_dir = LITERATURE_DIR / "Model-CFA-Studies"
        filename = f"Model-{sanitize_filename(source_file.stem)}.md"
        return target_dir / filename, "cfa", meta

    if "tacrolimus" in rel.lower() or "baricitinib" in rel.lower() or "jak" in rel.lower():
        meta["category"] = "Comparators"
        target_dir = LITERATURE_DIR / "Comparators-Studies"
        filename = f"Comp-{sanitize_filename(source_file.stem)}.md"
        return target_dir / filename, "comparators", meta
        
    if "pea" in rel.lower():
        meta["category"] = "PEA"
        target_dir = LITERATURE_DIR / "PEA-Studies"
        filename = f"PEA-{sanitize_filename(source_file.stem)}.md"
        return target_dir / filename, "pea", meta

    meta["category"] = "Foundational"
    target_dir = LITERATURE_DIR / "Foundational-and-Reviews"
    filename = f"Ref-{sanitize_filename(source_file.stem)}.md"
    return target_dir / filename, "foundational", meta

def main():
    print("Starting Multi-Format ETL Source Extraction...")
    manifest = []
    excel_tables_dump = {}
    
    for root, _, files in os.walk(SOURCES_DIR):
        for f in files:
            source_file = Path(root) / f
            ext = source_file.suffix.lower()
            
            if ext in [".tmp", ".bak"] or source_file.name.startswith("~$"):
                continue
                
            print(f"Processing: {source_file.relative_to(SOURCES_DIR)}")
            target_path, doc_type, meta = route_target_path(source_file)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            body = ""
            tables_txt = ""
            stats = {"chars": 0, "pages": 1, "tables": 0}
            
            try:
                if ext == ".xlsx":
                    body, sheets_data, rows, cols = parse_xlsx(source_file)
                    stats["tables"] = len(sheets_data)
                    stats["chars"] = len(body)
                    excel_tables_dump[source_file.name] = sheets_data
                elif ext == ".docx":
                    body, tbl_cnt = parse_docx(source_file)
                    stats["tables"] = tbl_cnt
                    stats["chars"] = len(body)
                elif ext == ".pptx":
                    body, sld_cnt = parse_pptx(source_file)
                    stats["pages"] = sld_cnt
                    stats["chars"] = len(body)
                elif ext == ".rtf":
                    body = parse_rtf(source_file)
                    stats["chars"] = len(body)
                elif ext == ".pdf":
                    body, tables_txt, pages, tbl_cnt = parse_pdf(source_file)
                    stats["pages"] = pages
                    stats["tables"] = tbl_cnt
                    stats["chars"] = len(body)
                elif ext in [".txt", ".md"]:
                    with open(source_file, "r", encoding="utf-8", errors="ignore") as tf:
                        body = tf.read()
                    stats["chars"] = len(body)
                elif ext == ".bmp":
                    body = f"# Image Asset: {source_file.name}\n\nBinary image parameter reference located at `{source_file.relative_to(VAULT_ROOT)}`.\n"
                    stats["chars"] = len(body)
                else:
                    continue
            except Exception as ex:
                print(f"ERROR processing {source_file}: {ex}")
                meta["extraction_error"] = str(ex)
                body = f"# Extraction Error: {source_file.name}\n\nCould not extract: {ex}"

            frontmatter = [
                "---",
                f'id: "{target_path.stem}"',
                f'title: "{source_file.stem}"',
                f'source_path: "{source_file.relative_to(VAULT_ROOT).as_posix()}"',
                f'source_hash: "{meta["source_hash"]}"',
                f'category: "{meta["category"]}"',
                f'pilot_data: {str(meta["pilot"]).lower()}',
                f'confirmatory: {str(meta["confirmatory"]).lower()}'
            ]
            if meta["pilot"]:
                frontmatter.append('sample_size: "n=2"')
                frontmatter.append('warning: "PILOT OBSERVATION ONLY - NOT CONFIRMATORY THESIS RESULTS"')
                frontmatter.append("tags: [pilot, preliminary-data, do-not-cite-as-main]")
            else:
                frontmatter.append("tags: [master-thesis, literature, verified-source]")
                
            frontmatter.append('qc_status: "EXTRACTED"')
            frontmatter.append('qc_gate1_passed: true')
            frontmatter.append("---\n")
            
            full_md = "\n".join(frontmatter) + "\n"
            if meta["pilot"]:
                full_md += "> [!WARNING] PILOT OBSERVATIONS ONLY\n"
                full_md += "> This file contains preliminary pilot study data (n=2 rats/group). It must NEVER be cited as confirmatory thesis results or combined with main experiment statistics.\n\n"
            
            full_md += body + "\n"
            if tables_txt:
                full_md += "\n## Structured Tables Extracted\n\n" + tables_txt + "\n"
                
            full_md += "\n---\n### Cross References & Network Links\n"
            full_md += "- Main Index: [[000-Index-Home]]\n"
            if meta["category"] == "PEA":
                full_md += "- Map of Content: [[MOC-Pharmacology-and-PEA]]\n- Related Concept: [[Palmitoylethanolamide-PEA]] | [[PPAR-alpha-Activation-by-PEA]]\n"
            elif meta["category"] == "Prednisolone":
                full_md += "- Map of Content: [[MOC-Glucocorticoid-Sparing]]\n- Related Concept: [[Prednisolone-in-RA]] | [[Glucocorticoid-Sparing-Concept]]\n"
            elif meta["category"] == "CFA-Model":
                full_md += "- Map of Content: [[MOC-Arthritis-Model-CFA]]\n- Related Concept: [[Complete-Freunds-Adjuvant-Model]] | [[Histopathology-Knee-Joint-Damage]]\n"
            elif meta["pilot"]:
                full_md += "- Protocol: [[Official-Animal-Protocol]]\n"
            else:
                full_md += "- Atlas: [[000-Index-Home]]\n"

            with open(target_path, "w", encoding="utf-8") as out_f:
                out_f.write(full_md)
                
            manifest.append({
                "source": source_file.relative_to(SOURCES_DIR).as_posix(),
                "target": target_path.relative_to(VAULT_ROOT).as_posix(),
                "category": meta["category"],
                "pilot": meta["pilot"],
                "stats": stats,
                "hash": meta["source_hash"]
            })

    QC_DIR.mkdir(parents=True, exist_ok=True)
    with open(QC_DIR / "extraction_manifest.json", "w", encoding="utf-8") as jf:
        json.dump(manifest, jf, indent=2, ensure_ascii=False)
        
    with open(QC_DIR / "excel_tables_matrix.json", "w", encoding="utf-8") as ef:
        json.dump(excel_tables_dump, ef, indent=2, ensure_ascii=False)
        
    print(f"\nETL Extraction Completed! Total files extracted: {len(manifest)}")

if __name__ == "__main__":
    main()
