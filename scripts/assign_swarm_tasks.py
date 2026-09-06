import subprocess
import json
import re

AGENT_TASKS = [
    {
        "name": "agency-agents-orchestrator",
        "agent_id": "agent-1788697182188-z8ewvg",
        "type": "custom",
        "desc": "Autonomous pipeline management, task delegation, and cross-agent dependency orchestration"
    },
    {
        "name": "agency-clinical-evidence-agent",
        "agent_id": "agent-1788697185021-53j5kv",
        "type": "research",
        "desc": "Clinical credibility, pharmacological mechanisms (PEA, PPAR-alpha, FAAH, Cox-2, Celecoxib), and arthritis translation"
    },
    {
        "name": "agency-statistician",
        "agent_id": "agent-1788697187705-63gvrf",
        "type": "testing",
        "desc": "Rigorous quantitative analysis, sample size verification, pilot n=2 quarantine alerts, and benchmark statistical tables"
    },
    {
        "name": "agency-evidence-collector",
        "agent_id": "agent-1788697190086-yud5mn",
        "type": "testing",
        "desc": "Zero-hallucination citation verification against 29 PDF papers and 5 Word documents with exact textual evidence"
    },
    {
        "name": "agency-reality-checker",
        "agent_id": "agent-1788697192730-j50chh",
        "type": "review",
        "desc": "Adversarial audit gatekeeper, rejecting false QC passes and certifying 100% resolution of all 23 gap issues"
    },
    {
        "name": "agency-model-qa-specialist",
        "agent_id": "agent-1788697195018-l92hbr",
        "type": "review",
        "desc": "End-to-end model audit, verifying methodological reproducibility, calculation accuracy, and experimental parameters"
    },
    {
        "name": "agency-zk-steward",
        "agent_id": "agent-1788697197384-5bs0oq",
        "type": "documentation",
        "desc": "Luhmann Zettelkasten knowledge stewardship, bidirectional wikilink graph integrity, atomic notes, and folder indexing"
    },
    {
        "name": "agency-data-engineer",
        "agent_id": "agent-1788697199636-9pzibu",
        "type": "implementation",
        "desc": "Multi-format data pipeline ETL, validating 1-to-1 parity across Excel sheets, Word extracts, and PDF tables"
    },
    {
        "name": "agency-codebase-archaeologist",
        "agent_id": "agent-1788697204989-j277xs",
        "type": "review",
        "desc": "Multi-session drift detection, detecting orphaned root files, redundant mirror directories, and stale notes"
    },
    {
        "name": "agency-test-results-analyzer",
        "agent_id": "agent-1788697208069-2eqc0i",
        "type": "testing",
        "desc": "Automated QC metric evaluation, executing 4-gate master QC and dynamic 9-category gap audit"
    },
    {
        "name": "agency-multi-agent-systems-architect",
        "agent_id": "agent-1788697210556-hrmw0q",
        "type": "custom",
        "desc": "Hierarchical mesh coordination, inter-agent communication protocols, and swarm consensus verification"
    },
    {
        "name": "agency-database-optimizer",
        "agent_id": "agent-1788697213530-omauyo",
        "type": "optimization",
        "desc": "Excel workbook normalization, deduplication of sheets, and structured matrix indexing"
    },
    {
        "name": "agency-workflow-optimizer",
        "agent_id": "agent-1788697216059-bs9gvy",
        "type": "optimization",
        "desc": "Automated verification loop optimization and continuous quality control pipeline"
    },
    {
        "name": "clean-code-guard",
        "agent_id": "agent-1788697218810-wytqwn",
        "type": "review",
        "desc": "Code quality, syntax safety, and script reliability for all python extraction and audit utilities"
    }
]

def run_cmd(cmd_list):
    try:
        res = subprocess.run(cmd_list, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running {' '.join(cmd_list)}: {e.stderr.strip()}")
        return None

def main():
    print("=== Creating and Assigning Swarm Tasks ===")
    records = []
    for item in AGENT_TASKS:
        t_cmd = ["cmd.exe", "/c", "ruflo", "task", "create", "-t", item["type"], "-d", f"[{item['name']}] {item['desc']}"]
        tout = run_cmd(t_cmd)
        task_id = None
        if tout:
            match = re.search(r"task-\d+-[a-z0-9]+", tout)
            if match:
                task_id = match.group(0)
        
        print(f"Created task: {task_id} for {item['name']}")
        if task_id and item["agent_id"]:
            a_cmd = ["cmd.exe", "/c", "ruflo", "task", "assign", task_id, "--agent", item["agent_id"]]
            aout = run_cmd(a_cmd)
            print(f"  -> Assigned to {item['agent_id']}")
        
        records.append({
            "name": item["name"],
            "agent_id": item["agent_id"],
            "task_id": task_id,
            "type": item["type"],
            "description": item["desc"],
            "status": "in_progress"
        })
    
    with open("07 - Automated QC & Audits/swarm_tasks_registry.json", "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)
    print("\nSaved tasks registry to 07 - Automated QC & Audits/swarm_tasks_registry.json")

if __name__ == '__main__':
    main()
