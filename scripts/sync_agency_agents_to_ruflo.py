import os
import re
import json
import shutil
import sqlite3
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path(r"d:\vault\my research")
USER_AGENTS_DIR = Path(r"C:\Users\ET\.claude\agents")
GEMINI_SKILLS_DIR = Path(r"C:\Users\ET\.gemini\config\skills")
PROJECT_AGENTS_DIR = VAULT_ROOT / ".claude" / "agents"
CLAUDE_FLOW_STORE = VAULT_ROOT / ".claude-flow" / "agents" / "store.json"
SWARM_DIR = VAULT_ROOT / ".swarm"
QC_DIR = VAULT_ROOT / "07 - Automated QC & Audits"

PROJECT_AGENTS_DIR.mkdir(parents=True, exist_ok=True)
QC_DIR.mkdir(parents=True, exist_ok=True)
SWARM_DIR.mkdir(parents=True, exist_ok=True)

def parse_frontmatter(content):
    meta = {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if m:
        fm_text = m.group(1)
        for line in fm_text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
        body = content[m.end():].strip()
    else:
        body = content.strip()
    return meta, body

def determine_agent_type(name, desc):
    text = (name + " " + desc).lower()
    if any(k in text for k in ['orchestrat', 'coordinator', 'lead', 'manager', 'chief', 'steward', 'director']):
        return "coordinator"
    elif any(k in text for k in ['audit', 'qa', 'reality-checker', 'tester', 'test', 'review', 'evaluator', 'guard']):
        return "reviewer"
    elif any(k in text for k in ['statistician', 'data', 'analyst', 'database', 'metrics', 'benchmarker', 'quant']):
        return "analyst"
    elif any(k in text for k in ['writer', 'document', 'author', 'copywriter', 'content', 'notes', 'curator']):
        return "documenter"
    elif any(k in text for k in ['developer', 'coder', 'engineer', 'architect', 'builder', 'scripter']):
        return "coder"
    elif any(k in text for k in ['researcher', 'clinical', 'evidence', 'scientist', 'anthropologist', 'historian', 'geographer']):
        return "researcher"
    else:
        return "researcher"

def main():
    print("=== Synchronizing All Agency Agents into Ruflo & Project .claude/agents ===")
    
    # 1. Read existing user agents from C:\Users\ET\.claude\agents
    agent_files = list(USER_AGENTS_DIR.glob("*.md"))
    print(f"Found {len(agent_files)} agent definitions in {USER_AGENTS_DIR}")
    
    # 2. Read existing Gemini agency skills if any missing
    gemini_agency_dirs = [d for d in GEMINI_SKILLS_DIR.glob("agency-*") if d.is_dir()]
    print(f"Found {len(gemini_agency_dirs)} agency skills in {GEMINI_SKILLS_DIR}")
    
    agents_catalog = {}
    
    # Process user agents
    for af in agent_files:
        try:
            content = af.read_text(encoding="utf-8", errors="ignore")
            meta, body = parse_frontmatter(content)
            base_stem = af.stem
            
            # Destination in project
            dest_file = PROJECT_AGENTS_DIR / af.name
            dest_file.write_text(content, encoding="utf-8")
            
            # Also create agency- prefixed link/copy if not present
            agency_name = base_stem if base_stem.startswith("agency-") else f"agency-{base_stem}"
            agency_file = PROJECT_AGENTS_DIR / f"{agency_name}.md"
            if not agency_file.exists():
                agency_file.write_text(content, encoding="utf-8")
                
            name = meta.get("name", base_stem)
            desc = meta.get("description", "")
            if not desc:
                # Extract first paragraph
                lines = [l.strip() for l in body.splitlines() if l.strip() and not l.startswith("#")]
                desc = lines[0] if lines else "Specialized agency agent"
                
            agent_type = determine_agent_type(name, desc)
            
            agents_catalog[agency_name] = {
                "id": agency_name,
                "canonical_name": name,
                "file_name": af.name,
                "agent_type": agent_type,
                "description": desc,
                "color": meta.get("color", "blue"),
                "emoji": meta.get("emoji", "🤖"),
                "source": "user_claude_agents"
            }
        except Exception as e:
            print(f"Error reading {af}: {e}")
            
    # Process any Gemini agency skills not yet in catalog
    for gd in gemini_agency_dirs:
        agency_name = gd.name
        if agency_name not in agents_catalog:
            skill_md = gd / "SKILL.md"
            if skill_md.exists():
                try:
                    content = skill_md.read_text(encoding="utf-8", errors="ignore")
                    meta, body = parse_frontmatter(content)
                    
                    dest_file = PROJECT_AGENTS_DIR / f"{agency_name}.md"
                    dest_file.write_text(content, encoding="utf-8")
                    
                    name = meta.get("name", agency_name)
                    desc = meta.get("description", "")
                    if not desc:
                        lines = [l.strip() for l in body.splitlines() if l.strip() and not l.startswith("#")]
                        desc = lines[0] if lines else "Specialized agency agent"
                    agent_type = determine_agent_type(name, desc)
                    
                    agents_catalog[agency_name] = {
                        "id": agency_name,
                        "canonical_name": name,
                        "file_name": f"{agency_name}.md",
                        "agent_type": agent_type,
                        "description": desc,
                        "color": "teal",
                        "emoji": "⚡",
                        "source": "gemini_skills"
                    }
                except Exception as e:
                    print(f"Error processing {skill_md}: {e}")
                    
    total_agents = len(agents_catalog)
    print(f"Total compiled Agency Agents: {total_agents}")
    print(f"Files written to {PROJECT_AGENTS_DIR}: {len(list(PROJECT_AGENTS_DIR.glob('*.md')))}")
    
    # 3. Update Ruflo Agent Store (.claude-flow/agents/store.json)
    store_data = {"agents": {}}
    if CLAUDE_FLOW_STORE.exists():
        try:
            store_data = json.load(open(CLAUDE_FLOW_STORE, "r", encoding="utf-8"))
            if "agents" not in store_data:
                store_data["agents"] = {}
        except Exception:
            store_data = {"agents": {}}
            
    now_iso = datetime.now().isoformat()
    for aid, ainfo in agents_catalog.items():
        # Register in store if not present
        store_key = f"ruflo-{aid}"
        store_data["agents"][store_key] = {
            "agentId": store_key,
            "name": ainfo["canonical_name"],
            "alias": aid,
            "agentType": ainfo["agent_type"],
            "status": "idle",
            "health": 1,
            "taskCount": 0,
            "config": {
                "provider": "anthropic",
                "name": ainfo["canonical_name"],
                "role": aid,
                "task": ainfo["description"][:200],
                "timeout": 300,
                "autoTools": True
            },
            "createdAt": now_iso,
            "model": "sonnet",
            "modelRoutedBy": "router",
            "provider": "anthropic",
            "description": ainfo["description"],
            "emoji": ainfo.get("emoji", "🤖")
        }
        
    CLAUDE_FLOW_STORE.parent.mkdir(parents=True, exist_ok=True)
    with open(CLAUDE_FLOW_STORE, "w", encoding="utf-8") as f:
        json.dump(store_data, f, indent=2, ensure_ascii=False)
    print(f"Updated {CLAUDE_FLOW_STORE} with {len(store_data['agents'])} registered agents.")
    
    # 4. Save Registry JSON in 07 - Automated QC & Audits
    registry_file = QC_DIR / "agency_agents_full_registry.json"
    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(agents_catalog, f, indent=2, ensure_ascii=False)
    print(f"Saved complete registry to {registry_file}")
    
    # 5. Populate Ruflo SQLite memory DB if it exists (.swarm/memory.db)
    db_path = SWARM_DIR / "memory.db"
    if db_path.exists():
        try:
            conn = sqlite3.connect(str(db_path))
            cur = conn.cursor()
            # Check tables
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [r[0] for r in cur.fetchall()]
            print("Existing SQLite tables in memory.db:", tables)
            
            if "memory_entries" in tables:
                cur.execute("DELETE FROM memory_entries WHERE namespace = 'agency-agents';")
                now_ms = int(datetime.now().timestamp() * 1000)
                for aid, ainfo in agents_catalog.items():
                    content = f"Agent Name: {ainfo['canonical_name']} | ID: {aid} | Type: {ainfo['agent_type']} | Description: {ainfo['description']}"
                    meta_json = json.dumps(ainfo, ensure_ascii=False)
                    tags_json = json.dumps([ainfo['agent_type'], "agency-agent", aid], ensure_ascii=False)
                    cur.execute("""
                        INSERT INTO memory_entries (id, key, namespace, content, type, tags, metadata, status, created_at, updated_at)
                        VALUES (?, ?, 'agency-agents', ?, 'semantic', ?, ?, 'active', ?, ?)
                    """, (f"mem_{aid}", f"agent:{aid}", content, tags_json, meta_json, now_ms, now_ms))
                conn.commit()
                print(f"Successfully indexed {len(agents_catalog)} agents into memory_entries table in memory.db")
            conn.close()
        except Exception as e:
            print(f"Note on SQLite indexing: {e}")
            
    print("\n[SUCCESS] Ruflo and Claude Code are now 100% synchronized with all Agency Agents!")

if __name__ == "__main__":
    main()
