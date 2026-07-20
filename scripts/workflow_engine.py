import os
import json
from typing import Dict, Any, Callable, List

class WorkflowEngine:
    def __init__(self, context_dir: str = ".esper/shared_context/checkpoints/"):
        self.nodes = {}
        self.edges = {}
        self.context_dir = context_dir
        self.max_steps = 100
        
        if not os.path.exists(self.context_dir):
            os.makedirs(self.context_dir)

    def add_node(self, name: str, handler: Callable[[Dict[str, Any]], Dict[str, Any]]):
        self.nodes[name] = handler

    def add_edge(self, from_node: str, to_node: str, condition: Callable[[Dict[str, Any]], bool] = lambda _: True):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, condition))

    def _save_checkpoint(self, state: Dict[str, Any], step: int):
        filepath = os.path.join(self.context_dir, f"checkpoint_{step}.json")
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)

    def run(self, initial_state: Dict[str, Any], start_node: str) -> Dict[str, Any]:
        current_node = start_node
        state = initial_state
        step = 0
        visited = []

        while current_node and step < self.max_steps:
            visited.append(current_node)
            self._save_checkpoint(state, step)
            
            if current_node not in self.nodes:
                raise ValueError(f"Node {current_node} not found")
                
            state = self.nodes[current_node](state)
            step += 1
            
            next_node = None
            if current_node in self.edges:
                for target, condition in self.edges[current_node]:
                    if condition(state):
                        next_node = target
                        break
            
            if next_node is None:
                break
                
            current_node = next_node
            
        if step >= self.max_steps:
            raise RuntimeError(f"Infinite loop detected or max steps ({self.max_steps}) reached. Path: {visited}")
            
        self._save_checkpoint(state, step)
        return state
