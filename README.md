# Esper

Esper is a modular engineering operating system for AI coding assistants. 

Rather than relying on a single monolithic system prompt, Esper decomposes engineering knowledge into small, focused modules with clearly defined responsibilities. These modules are powered by a highly optimized canonical XML schema (`<esper_module>`) and adhere strictly to Antigravity's Progressive Disclosure architecture using native Rules. They are dynamically composed together at runtime to guide reasoning, reduce oversight, and improve consistency across engineering tasks.

## Installation

To use Esper with your AI assistants, clone this repository into your `.gemini` directory and run the setup script to configure the necessary bootstrap files.

### Windows (PowerShell)

```powershell
# 1. Create the .gemini directory if it doesn't exist
New-Item -ItemType Directory -Force -Path ~/.gemini

# 2. Clone the repository
git clone https://github.com/KaindraDjoemena/esper.git ~/.gemini/esper

# 3. Run the installation script to configure your AI bootstrap files
cd ~/.gemini/esper
.\install.ps1
```

### macOS / Linux (Bash / Zsh)

```bash
# 1. Create the .gemini directory if it doesn't exist
mkdir -p ~/.gemini

# 2. Clone the repository
git clone https://github.com/KaindraDjoemena/esper.git ~/.gemini/esper

# 3. Run the installation script to configure your AI bootstrap files
cd ~/.gemini/esper
./install.sh
```

## Updating Esper

Because Esper's bootstrap files (`GEMINI.md`, `CLAUDE.md`) are copied to your root directory during installation, a simple `git pull` is not enough to fully update the framework. You must use the included update scripts to pull the latest changes and re-sync the bootstrap files:

### Windows (PowerShell)
```powershell
cd ~/.gemini/esper
.\update.ps1
```

### macOS / Linux
```bash
cd ~/.gemini/esper
./update.sh
```

## Global vs Local Installations

Esper natively supports being installed globally (across your entire machine) or locally (within a specific project repository). It is fully compatible with both the **Antigravity CLI** and the **Antigravity IDE**.

- **Global Installation**: Install Esper to your home directory (`~/.gemini/esper`). The AI will use these rules for every project you work on. Global skills should be shared across environments and stored in `~/.gemini/config/skills/`.
- **Local Installation**: Clone Esper directly into a project directory (e.g., `<your-project>/.gemini/esper`). Run the install script from there, and Esper will only operate within that specific project. Local project-specific skills should be stored in `<your-project>/.agents/skills/`.

Upon initialization, Esper will automatically greet you and announce whether it is running from a Local or Global configuration, providing its exact file path and confirming whether you are in the CLI or IDE.

## Persistent Memory (Context)

Esper supports state persistence via a **Hierarchical Context Structure** within the `shared_context/` module. 

To prevent context window bloat, Esper enforces decentralized, domain-specific memory files (e.g., `ui-state.md`, `auth-state.md`) paired with YAML frontmatter, rather than relying on a monolithic `notes.md`. Agents utilize **Native RAG (Retrieval-Augmented Generation)** via semantic search to selectively load only the context they need for their current objective.

- **Global Context** (`~/.gemini/esper/shared_context/`) acts as the framework's meta-knowledge base.
- **Project Context** (`<project-root>/.esper/shared_context/`) is generated dynamically by agent skills. You should add `.esper/` to your project's `.gitignore` to prevent memory contamination in your public git history.
- **Workspace Hygiene**: Agents are strictly governed by `.agents/rules/workspace-hygiene.md` to keep your root directory clean. All temporary AI scratchpads and diagnostic files are sandboxed within `.esper/scratch/`.
- **Lifecycle Memory Management**: A sliding-window deterministic pruning system (`memory_manager.py`) runs dynamically during long conversations to proactively "forget" stale files and prevent token exhaustion.
- **Semantic Knowledge Graphs (GraphRAG)**: Esper utilizes a native Python engine (`knowledge_graph.py`) to map complex entity relationships, bridging standard RAG with architectural dependency mapping.
- **Asynchronous Dreaming**: A background daemon (`dreamer.py`) runs in a continuous loop to automatically compress stale memory and synthesize insights, ensuring your context window remains pristine without manual intervention.

## Multi-Agent Orchestration

Esper natively supports state-of-the-art **Graph-Based Orchestration** utilizing a Supervisor "Plan-and-Execute" architecture.
- **State Machine Routing**: A deterministic Python workflow engine (`workflow_engine.py`) securely manages subagent routing, infinite-loop detection, and state checkpoints.
- **Agent-to-Agent (A2A) Contracts**: Tasks are decoupled from conversational contexts and routed to specialized execution subagents via strict JSON data contracts.
- **Evaluator-Optimizer Loops**: A hybrid neuro-symbolic middleware (`evaluator.py`) mathematically forces agents to recursively self-critique and refine their JSON handoffs (up to a 3-strike limit) before passing data downstream, guaranteeing pipeline integrity.

## Governance & Security

Esper operates on a strict **Zero-Trust Identity** model. Subagent permissions are locked down based on explicit roles via `checklists/zero-trust.md`. If a subagent is spawned without a defined role, it is mathematically sandboxed into a **Read-Only** fallback state, ensuring it cannot accidentally mutate source code.

Furthermore, Esper enforces **Deterministic Guardrails** using Policy-as-Code. A Python policy gate (`policy_gate.py`) intercepts high-risk operations (e.g., bulk edits or source code deletions) and halts them without crashing the workflow. Agents are forced by `checklists/automation-safety.md` to trigger an interactive Human-in-the-Loop (HITL) modal to request explicit user approval before proceeding.

## Available Skills

Esper also supports modular skills that extend its capabilities (e.g., auditing, scaffolding, orchestration). These are maintained in a separate repository to prevent dependency hell.

You can clone the skills repository into your Antigravity skills directory. Alternatively, **your AI agent can autonomously install them for you** simply by asking it to do so.

If installing manually, simply clone the repository directly into your global configuration skills directory:

```bash
git clone https://github.com/KaindraDjoemena/esper-skills.git ~/.gemini/config/skills/esper-skills
```

Once installed, agents can invoke these skills on demand to perform complex workflows.

## Utility Scripts

Esper includes built-in Python utility scripts located in the `scripts/` directory to help maintain the framework:

- **`jit_compiler.py`**: A Just-In-Time compiler designed to be used as an Antigravity `pre-task` hook. It flattens Esper's recursive dependency graph into a single injected context payload, saving LLM tokens and instantly pulling in local project overrides (`AGENTS.md`).
- **`scan_dependencies.py`**: A graph-parsing tool that analyzes all Markdown files, tracking dependencies and inline links to flag broken references or orphaned modules, outputting the results as structured JSON.
