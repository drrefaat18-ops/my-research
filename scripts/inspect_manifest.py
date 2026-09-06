import csv
import json

def main():
    with open('skills_manifest.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        skills = list(reader)
    print(f"Total skills/agents in manifest: {len(skills)}")
    
    # Categorize agents relevant to scientific research, pharmacology, data quality, QC, audit, documentation, etc.
    scientific_agents = []
    qc_audit_agents = []
    analytics_data_agents = []
    writing_doc_agents = []
    strategy_management_agents = []
    all_agents = []

    for s in skills:
        name = s['Name']
        desc = s['Description']
        all_agents.append(name)
        lower_desc = desc.lower() + " " + name.lower()
        if any(k in lower_desc for k in ['clinical', 'evidence', 'health', 'medical', 'pharma', 'bio', 'experiment']):
            scientific_agents.append((name, desc))
        elif any(k in lower_desc for k in ['audit', 'qa', 'quality', 'tester', 'review', 'compliance', 'reality-checker']):
            qc_audit_agents.append((name, desc))
        elif any(k in lower_desc for k in ['data', 'statistician', 'analytics', 'database', 'extraction', 'consolidation']):
            analytics_data_agents.append((name, desc))
        elif any(k in lower_desc for k in ['writer', 'document', 'technical-writer', 'notes', 'summary']):
            writing_doc_agents.append((name, desc))
        elif any(k in lower_desc for k in ['orchestrat', 'coordinator', 'project-manager', 'operations', 'architect']):
            strategy_management_agents.append((name, desc))

    print(f"\n--- Scientific & Research Agents ({len(scientific_agents)}) ---")
    for name, desc in scientific_agents:
        print(f"  - {name}: {desc[:80]}")

    print(f"\n--- QC & Audit Agents ({len(qc_audit_agents)}) ---")
    for name, desc in qc_audit_agents:
        print(f"  - {name}: {desc[:80]}")

    print(f"\n--- Analytics & Data Agents ({len(analytics_data_agents)}) ---")
    for name, desc in analytics_data_agents:
        print(f"  - {name}: {desc[:80]}")

    print(f"\n--- Writing & Documentation Agents ({len(writing_doc_agents)}) ---")
    for name, desc in writing_doc_agents:
        print(f"  - {name}: {desc[:80]}")

    print(f"\n--- Strategy & Management Agents ({len(strategy_management_agents)}) ---")
    for name, desc in strategy_management_agents:
        print(f"  - {name}: {desc[:80]}")

if __name__ == '__main__':
    main()
