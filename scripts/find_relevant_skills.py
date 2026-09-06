import csv, sys

with open('skills_manifest.csv', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    lines = []
    lines.append("Relevant Skills and Agents from skills_manifest.csv:")
    lines.append("="*60)
    for row in reader:
        name = row.get('Name', '')
        desc = row.get('Description', '')
        folder = row.get('Folder', '')
        keywords = ['clinical', 'pharma', 'evidence', 'qa', 'audit', 'obsidian', 'review', 'statistic', 'experiment', 'medical', 'second-brain', 'canvas', 'rag', 'reality', 'guard', 'orchestrator', 'pipeline', 'writer', 'document']
        if any(w in desc.lower() or w in name.lower() for w in keywords):
            lines.append(f"- **{name}** (`{folder}`): {desc}")

with open('scripts/manifest_review_agents.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(lines))

print(f"Wrote {len(lines)} matched agents to scripts/manifest_review_agents.txt")
