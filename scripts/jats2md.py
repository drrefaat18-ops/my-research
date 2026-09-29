"""Convert Europe PMC JATS full-text XML to readable Markdown.
Usage: python jats2md.py <in.xml> <out.md> <pmcid>
"""
import re
import sys
import xml.etree.ElementTree as ET


def text(el):
    # ponytail: flattens inline markup (italics, xrefs); fine for reading, not for re-publishing
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def walk(sec, depth, out):
    title = sec.find("title")
    if title is not None:
        out.append(f"\n{'#' * min(depth, 6)} {text(title)}\n")
    for child in sec:
        if child.tag == "p":
            out.append(text(child) + "\n")
        elif child.tag == "sec":
            walk(child, depth + 1, out)
        elif child.tag in ("fig", "table-wrap"):
            label, cap = text(child.find("label")), text(child.find("caption"))
            out.append(f"> **{label}** {cap}\n")


def convert(xml_path, md_path, pmcid):
    root = ET.parse(xml_path).getroot()
    meta = root.find(".//article-meta")
    out = [f"# {text(meta.find('.//article-title'))}\n"]
    authors = [f"{text(c.find('.//surname'))} {text(c.find('.//given-names'))}"
               for g in meta.findall(".//contrib-group")
               if g.get("content-type", "author") == "author"
               for c in g.findall("contrib")
               if c.get("contrib-type", "author") == "author" and c.find(".//surname") is not None]
    journal = text(root.find(".//journal-title"))
    year = text(meta.find(".//pub-date/year"))
    doi = text(meta.find(".//article-id[@pub-id-type='doi']"))
    out.append(f"**Authors:** {', '.join(authors)}  \n**Journal:** {journal} ({year})  \n"
               f"**DOI:** {doi}  \n**PDF:** https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/\n")
    abstract = meta.find("abstract")
    if abstract is not None:
        out.append("\n## Abstract\n")
        walk(abstract, 3, out)
    body = root.find("body")
    if body is not None:
        for sec in body:
            if sec.tag == "sec":
                walk(sec, 2, out)
            elif sec.tag == "p":
                out.append(text(sec) + "\n")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    convert(*sys.argv[1:4])
