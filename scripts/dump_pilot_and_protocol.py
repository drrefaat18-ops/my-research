import pathlib, pypdf, docx

VAULT = pathlib.Path('d:/vault/my research')
SOURCES = VAULT / '00-Sources'

# 1. Dump Protocol.pdf
protocol_pdfs = list(SOURCES.rglob('Protocol.pdf'))
if protocol_pdfs:
    reader = pypdf.PdfReader(protocol_pdfs[0])
    text = []
    for i, page in enumerate(reader.pages):
        text.append(f'=== PAGE {i+1} ===\n' + page.extract_text())
    (VAULT / 'scripts/protocol_dump.txt').write_text('\n\n'.join(text), encoding='utf-8')
    print('Dumped Protocol.pdf:', len(reader.pages), 'pages')

# 2. Dump Blood work final.pdf
bw_pdfs = list(SOURCES.rglob('Blood work final.pdf'))
if bw_pdfs:
    reader = pypdf.PdfReader(bw_pdfs[0])
    text = []
    for i, page in enumerate(reader.pages):
        text.append(f'=== PAGE {i+1} ===\n' + page.extract_text())
    (VAULT / 'scripts/blood_work_dump.txt').write_text('\n\n'.join(text), encoding='utf-8')
    print('Dumped Blood work final.pdf')

# 3. Dump WBC final.pdf
wbc_pdfs = list(SOURCES.rglob('WBC final.pdf'))
if wbc_pdfs:
    reader = pypdf.PdfReader(wbc_pdfs[0])
    text = []
    for i, page in enumerate(reader.pages):
        text.append(f'=== PAGE {i+1} ===\n' + page.extract_text())
    (VAULT / 'scripts/wbc_dump.txt').write_text('\n\n'.join(text), encoding='utf-8')
    print('Dumped WBC final.pdf')

# 4. Dump researcher DOCX files
docx_files = {
    'pilot.docx': list(SOURCES.rglob('pilot.docx')),
    'AA vs CIA.docx': list(SOURCES.rglob('AA vs CIA.docx')),
    'GR and PPAR-a.docx': list(SOURCES.rglob('GR and PPAR-a.docx')),
    'PEA summary.docx': list(SOURCES.rglob('PEA summary.docx')),
    'Rational choices.docx': list(SOURCES.rglob('Rational choices.docx')),
}

for name, files in docx_files.items():
    if files:
        doc = docx.Document(files[0])
        lines = []
        for p in doc.paragraphs:
            if p.text.strip():
                lines.append(p.text.strip())
        for t in doc.tables:
            for row in t.rows:
                row_str = ' | '.join(c.text.strip() for c in row.cells if c.text.strip())
                if row_str:
                    lines.append(f'[TABLE] {row_str}')
        out_name = f'scripts/{name.replace(" ", "_").replace("-", "_")}.txt'
        (VAULT / out_name).write_text('\n'.join(lines), encoding='utf-8')
        print(f'Dumped {name}: {len(lines)} lines')
