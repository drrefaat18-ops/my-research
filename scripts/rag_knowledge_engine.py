import os
import sys
import json
import re
import math
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

VAULT_ROOT = Path(r"d:\vault\my research")
QC_DIR = VAULT_ROOT / "07 - Automated QC & Audits"
QC_DIR.mkdir(parents=True, exist_ok=True)

TARGET_DIRS = [
    "01 - Rationale & Study Design",
    "02 - Molecular Axis & Mechanisms",
    "03 - Collective Literature Matrix",
    "04 - Experimental Protocols & Pilot",
    "05 - Comparators Benchmarking",
    "06 - Thesis Defense & Publishing"
]

def tokenize(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\u0600-\u06FF\-]+', ' ', text)
    tokens = text.split()
    return [t for t in tokens if len(t) > 2]

class KnowledgeEngine:
    def __init__(self):
        self.documents = []
        self.chunks = []
        self.inverted_index = {}
        self.doc_lengths = []
        self.avg_doc_length = 0
        self.graph_nodes = []
        self.graph_edges = []

    def build_index(self):
        print("Indexing Obsidian Second Brain Vault...")
        chunk_id = 0
        
        for dir_name in TARGET_DIRS:
            target_dir = VAULT_ROOT / dir_name
            if not target_dir.exists():
                continue
                
            for root, _, files in os.walk(target_dir):
                for f in files:
                    if f.endswith(".md"):
                        file_path = Path(root) / f
                        rel_path = file_path.relative_to(VAULT_ROOT).as_posix()
                        
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as md_f:
                            content = md_f.read()
                            
                        # Extract frontmatter if any
                        is_pilot = "pilot" in rel_path.lower() or "pilot_data: true" in content or "sample_size: \"n=2\"" in content
                        
                        # Graph Node
                        self.graph_nodes.append({
                            "id": file_path.stem,
                            "label": file_path.stem.replace("-", " "),
                            "path": rel_path,
                            "is_pilot": is_pilot
                        })
                        
                        # Extract Wikilinks for Graph Edges
                        wikilinks = re.findall(r'\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]', content)
                        for target in wikilinks:
                            clean_target = Path(target).stem
                            self.graph_edges.append({
                                "source": file_path.stem,
                                "target": clean_target,
                                "relation": "links_to"
                            })
                            
                        # Split into structural chunks by header (## or ###)
                        sections = re.split(r'(?m)^(?=##\s+)', content)
                        for sec in sections:
                            sec_clean = sec.strip()
                            if len(sec_clean) < 30:
                                continue
                                
                            tokens = tokenize(sec_clean)
                            if not tokens:
                                continue
                                
                            chunk_info = {
                                "chunk_id": chunk_id,
                                "file": rel_path,
                                "stem": file_path.stem,
                                "text": sec_clean[:1200],
                                "is_pilot": is_pilot,
                                "tokens": tokens
                            }
                            self.chunks.append(chunk_info)
                            self.doc_lengths.append(len(tokens))
                            
                            # Update inverted index
                            counts = Counter(tokens)
                            for t, c in counts.items():
                                if t not in self.inverted_index:
                                    self.inverted_index[t] = []
                                self.inverted_index[t].append((chunk_id, c))
                                
                            chunk_id += 1
                            
        self.avg_doc_length = sum(self.doc_lengths) / max(1, len(self.doc_lengths))
        print(f"Indexing complete! Total Nodes: {len(self.graph_nodes)}, Total Edges: {len(self.graph_edges)}, Total Chunks: {len(self.chunks)}")
        
        # Save graph manifest
        graph_manifest = {
            "nodes": self.graph_nodes,
            "edges": self.graph_edges,
            "total_nodes": len(self.graph_nodes),
            "total_edges": len(self.graph_edges)
        }
        with open(QC_DIR / "knowledge_graph.json", "w", encoding="utf-8") as gf:
            json.dump(graph_manifest, gf, indent=2, ensure_ascii=False)

    def bm25_search(self, query: str, top_k: int = 5, filter_pilot: bool = True):
        q_tokens = tokenize(query)
        if not q_tokens:
            return []
            
        N = len(self.chunks)
        k1 = 1.5
        b = 0.75
        scores = [0.0] * N
        
        for t in q_tokens:
            if t in self.inverted_index:
                postings = self.inverted_index[t]
                df = len(postings)
                idf = math.log((N - df + 0.5) / (df + 0.5) + 1.0)
                
                for cid, freq in postings:
                    doc_len = self.doc_lengths[cid]
                    num = freq * (k1 + 1.0)
                    denom = freq + k1 * (1.0 - b + b * (doc_len / self.avg_doc_length))
                    scores[cid] += idf * (num / denom)
                    
        # Apply metadata filtering penalty or boost
        ranked = []
        for cid, sc in enumerate(scores):
            if sc > 0:
                chunk = self.chunks[cid]
                # If filter_pilot is True and query is not specifically asking about pilot, demote or warn
                if chunk["is_pilot"] and not any(p in query.lower() for p in ["pilot", "preliminary", "n=2"]):
                    sc *= 0.1 # Heavily demote unprompted pilot chunks
                ranked.append((cid, sc, chunk))
                
        ranked.sort(key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    def query(self, user_query: str):
        results = self.bm25_search(user_query, top_k=5)
        print(f"\n=======================================================")
        print(f"🔎 RAG QUERY: '{user_query}'")
        print(f"=======================================================\n")
        
        if not results:
            print("No matching knowledge chunks found in the vault.")
            return
            
        for rank, (cid, score, chunk) in enumerate(results, start=1):
            print(f"--- [Match #{rank} | Relevance Score: {score:.3f}] ---")
            print(f"📁 Source: [[{chunk['stem']}]] ({chunk['file']})")
            if chunk["is_pilot"]:
                print("⚠️ [WARNING: QUARANTINED PILOT OBSERVATION - n=2]")
            print(f"{chunk['text']}\n")

if __name__ == "__main__":
    engine = KnowledgeEngine()
    engine.build_index()
    
    if len(sys.argv) > 1:
        q = " ".join(sys.argv[1:])
        engine.query(q)
    else:
        # Run test verification queries
        engine.query("How does m-PEA act as a steroid-sparing agent with prednisolone?")
        engine.query("What are the doses of the 7 treatment groups in the protocol?")
        engine.query("Why was AA model chosen instead of CIA?")
