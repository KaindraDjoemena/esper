import argparse
import json
from pathlib import Path

DB_PATH = Path(".esper/shared_context/knowledge_graph.json")

def load_graph():
    if not DB_PATH.exists():
        return {"nodes": {}, "edges": []}
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_graph(graph):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DB_PATH, "w") as f:
        json.dump(graph, f, indent=2)

def add_node(node_id, node_type, properties=None):
    graph = load_graph()
    graph["nodes"][node_id] = {
        "type": node_type,
        "properties": properties or {}
    }
    save_graph(graph)
    print(f"Added node: {node_id}")

def add_edge(source, target, relation, properties=None):
    graph = load_graph()
    graph["edges"].append({
        "source": source,
        "target": target,
        "relation": relation,
        "properties": properties or {}
    })
    save_graph(graph)
    print(f"Added edge: {source} -> {target} ({relation})")

def query(node_id=None, relation=None):
    graph = load_graph()
    results = []
    for edge in graph["edges"]:
        if node_id and (edge["source"] != node_id and edge["target"] != node_id):
            continue
        if relation and edge["relation"] != relation:
            continue
        results.append(edge)
    
    print(json.dumps(results, indent=2))
    return results

def main():
    parser = argparse.ArgumentParser(description="Esper Semantic Knowledge Graph")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_node_parser = subparsers.add_parser("add_node")
    add_node_parser.add_argument("node_id")
    add_node_parser.add_argument("node_type")
    add_node_parser.add_argument("--properties", type=json.loads, default={})

    add_edge_parser = subparsers.add_parser("add_edge")
    add_edge_parser.add_argument("source")
    add_edge_parser.add_argument("target")
    add_edge_parser.add_argument("relation")
    add_edge_parser.add_argument("--properties", type=json.loads, default={})

    query_parser = subparsers.add_parser("query")
    query_parser.add_argument("--node_id", help="Query edges connected to this node")
    query_parser.add_argument("--relation", help="Query edges with this relation")

    args = parser.parse_args()

    if args.command == "add_node":
        add_node(args.node_id, args.node_type, args.properties)
    elif args.command == "add_edge":
        add_edge(args.source, args.target, args.relation, args.properties)
    elif args.command == "query":
        query(args.node_id, args.relation)

if __name__ == "__main__":
    main()
