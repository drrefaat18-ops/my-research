import subprocess
import json
import time

MANIFEST_AGENTS = [
    {
        "name": "agency-agents-orchestrator",
        "type": "coordinator",
        "task_desc": "Autonomous pipeline management, task delegation, and cross-agent dependency orchestration"
    },
    {
        "name": "agency-clinical-evidence-agent",
        "type": "researcher",
        "task_desc": "Clinical credibility, pharmacological mechanisms (PEA, PPAR-alpha, FAAH, Cox-2, Celecoxib), and arthritis translation"
    },
    {
        "name": "agency-statistician",
        "type": "analyst",
        "task_desc": "Rigorous quantitative analysis, sample size verification, pilot n=2 quarantine alerts, and benchmark statistical tables"
    },
    {
        "name": "agency-evidence-collector",
        "type": "tester",
        "task_desc": "Zero-hallucination citation verification against 29 PDF papers and 5 Word documents with exact textual evidence"
    },
    {
        "name": "agency-reality-checker",
        "type": "reviewer",
        "task_desc": "Adversarial audit gatekeeper, rejecting false QC passes and certifying 100% resolution of all 23 gap issues"
    },
    {
        "name": "agency-model-qa-specialist",
        "type": "reviewer",
        "task_desc": "End-to-end model audit, verifying methodological reproducibility, calculation accuracy, and experimental parameters"
    },
    {
        "name": "agency-zk-steward",
        "type": "analyst",
        "task_desc": "Luhmann Zettelkasten knowledge stewardship, bidirectional wikilink graph integrity, atomic notes, and folder indexing"
    },
    {
        "name": "agency-data-engineer",
        "type": "coder",
        "task_desc": "Multi-format data pipeline ETL, validating 1-to-1 parity across Excel sheets, Word extracts, and PDF tables"
    },
    {
        "name": "agency-technical-writer",
        "type": "writer",
        "task_desc": "Academic synthesis, comprehensive study documentation (>8,000 bytes/study), and deep mechanistic-to-thesis mapping"
    },
    {
        "name": "agency-codebase-archaeologist",
        "type": "reviewer",
        "task_desc": "Multi-session drift detection, detecting orphaned root files, redundant mirror directories, and stale notes"
    },
    {
        "name": "agency-test-results-analyzer",
        "type": "tester",
        "task_desc": "Automated QC metric evaluation, executing 4-gate master QC and dynamic 9-category gap audit"
    },
    {
        "name": "agency-multi-agent-systems-architect",
        "type": "coordinator",
        "task_desc": "Hierarchical mesh coordination, inter-agent communication protocols, and swarm consensus verification"
    },
    {
        "name": "agency-database-optimizer",
        "type": "analyst",
        "task_desc": "Excel workbook normalization, deduplication of sheets, and structured matrix indexing"
    },
    {
        "name": "agency-workflow-optimizer",
        "type": "coordinator",
        "task_desc": "Automated verification loop optimization and continuous quality control pipeline"
    },
    {
        "name": "clean-code-guard",
        "type": "reviewer",
        "task_desc": "Code quality, syntax safety, and script reliability for all python extraction and audit utilities"
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
    print("=== Spawning Manifest Swarm Agents into Ruflo ===")
    spawned_agents = []
    
    for agent in MANIFEST_AGENTS:
        print(f"Spawning {agent['name']} ({agent['type']})...")
        cmd = ["cmd.exe", "/c", "ruflo", "agent", "spawn", "-t", agent["type"], "-n", agent["name"], "--task", agent["task_desc"]]
        out = run_cmd(cmd)
        agent_id = None
        if out:
            for line in out.splitlines():
                if "ID" in line and "agent-" in line:
                    parts = [p.strip() for p in line.split("|") if p.strip()]
                    if len(parts) >= 2:
                        agent_id = parts[1]
                        break
        print(f"  -> Spawned: {agent_id or 'OK'}")
        
        # Create corresponding task
        task_cmd = ["cmd.exe", "/c", "ruflo", "task", "create", "-t", agent["type"], "-d", f"[{agent['name']}] {agent['task_desc']}"]
        tout = run_cmd(task_cmd)
        task_id = None
        if tout:
            for line in tout.splitlines():
                if "ID" in line and "task-" in line:
                    tparts = [p.strip() for p in line.split("|") if p.strip()]
                    if len(tparts) >= 2:
                        task_id = tparts[1]
                        break
        print(f"  -> Task created: {task_id or 'OK'}")
        
        # Assign task if both IDs found
        if agent_id and task_id:
            assign_cmd = ["cmd.exe", "/c", "ruflo", "task", "assign", task_id, "--agent", agent_id]
            run_cmd(assign_cmd)
            print(f"  -> Assigned {task_id} to {agent_id}")
            
        spawned_agents.append({
            "name": agent["name"],
            "type": agent["type"],
            "agent_id": agent_id,
            "task_id": task_id,
            "description": agent["task_desc"]
        })
        time.sleep(0.3)
        
    # Save swarm manifest state
    with open("07 - Automated QC & Audits/swarm_manifest_state.json", "w", encoding="utf-8") as f:
        json.dump(spawned_agents, f, indent=2)
    print("\nSaved swarm manifest state to 07 - Automated QC & Audits/swarm_manifest_state.json")

if __name__ == '__main__':
    main()
