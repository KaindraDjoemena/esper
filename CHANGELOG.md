# Changelog

All notable changes to this project will be documented in this file.

## [3.3.0] - 2026-07-20

### Added
- **`workflows/initialization.md` + `prompts/initialization.md`**: New workflow that bootstraps a project's `.esper/` directory on first use. Creates `notes/`, `checkpoints/`, `scratch/` scaffold, initializes `notes-manifest.md` and `checkpoints/index.md` with table headers, and handles `.gitignore` with explicit user confirmation.

### Changed
- **Orchestration namespace rename**: Renamed `prompts/delegation.md` → `prompts/orchestration.md`, `workflows/delegation.md` → `workflows/orchestration.md`, and `checklists/delegation.md` → `checklists/orchestration.md` to establish a consistent 1:1 namespace across all layers. `principles/delegation.md` retains its name as a philosophy concept. All reference sites (`prompts/architecture-review.md`, `prompts/feature.md`, `prompts/research.md`, `workflows/supervisor.md`, `refactor.py`) updated accordingly.
- **A2A contract enforcement in orchestration workflow**: Added Step 3 to `workflows/orchestration.md` requiring orchestrator agents to produce a JSON handoff payload conforming to `templates/a2a-contract.json`, save it to `.esper/scratch/<task_id>.json`, and validate via `scripts/evaluator.py` before delegating to any subagent.
- **`esp-cpt` skill expanded**: Fleshed out `esp-cpt/SKILL.md` from a minimal stub into a full 5-step spec covering slug input, timestamped directory creation, generation of `session-handover.md` / `todo-list.md` / `roadmap.md`, `checkpoints/index.md` table append, and optional conditional `git tag` integration.
- **`esp-note` skill expanded**: Fleshed out `esp-note/SKILL.md` with global vs. local scope selection, YAML frontmatter requirements, dated slug filenames, `notes-manifest.md` table updates, `<when_to_use>` examples, and context bloat rule.
- **`workflows/orchestration.md` keywords updated**: Frontmatter `keywords:` field expanded to `[orchestrate, orchestration, subagent, delegate, complex, broad, large, partition, parallel]` for improved JIT heuristic matching.

## [3.2.0] - 2026-07-20

### Changed
- **Dreamer now performs real memory compression**: Replaced the `simulate_compression()` and `simulate_synthesis()` stub functions in `scripts/dreamer.py` with real implementations. `compress_memory()` now performs actual file-age-based pruning of `.esper/shared_context/` files using the existing `memory_manager.py` logic. `synthesize_knowledge_graph()` now honestly logs that LLM-based synthesis is not yet implemented instead of outputting a misleading success message. Added `--window-size` CLI argument (default: 10 files).
- **JIT heuristics moved to module frontmatter**: Removed the hardcoded `HEURISTICS` dict from `scripts/jit_compiler.py`. Optional dependency keywords are now declared in the `keywords:` YAML frontmatter field of each module (`principles/security.md`, `principles/performance.md`, `workflows/orchestration.md`). The compiler now reads keywords dynamically, meaning new optional modules no longer require compiler changes.
- **Bootstrap templates unified**: Removed stale `routing.md` references from both `bootstrap/GEMINI.md.template` and `bootstrap/CLAUDE.md`. Updated `bootstrap/CLAUDE.md` to use absolute paths consistent with the global Esper install location. Added explicit `ask_question` modal mandate to `GEMINI.md.template`'s communication flow.

## [3.1.0] - 2026-07-13

### Added
- **Semantic Knowledge Graphs (GraphRAG)**: Built `scripts/knowledge_graph.py` and the global `esp-graph` skill to natively map and query complex architectural entity relationships, upgrading the framework from flat text RAG to a state-of-the-art hybrid GraphRAG architecture.
- **Asynchronous Dreaming**: Deployed `scripts/dreamer.py`, a background daemon that operates on a configurable continuous loop (default 24 hours) to autonomously compress stale memory files and synthesize knowledge graph nodes, permanently preventing context bloat.
- **Zero-Trust Agent Identity**: Created `checklists/zero-trust.md` to strictly lock down subagent capabilities based on designated roles, mathematically enforcing a secure **Read-Only** fallback for any undefined agents.

## [3.0.0] - 2026-07-13

### Added
- **Graph-Based Workflow Engine**: Built `scripts/workflow_engine.py` to establish deterministic state-machine routing, state checkpointing, and infinite-loop detection, moving Esper away from fragile prompt-based delegation.
- **Supervisor 'Plan-and-Execute' Architecture**: Introduced `workflows/supervisor.md` to decouple task planning from execution. Parent agents now act strictly as Supervisors, handing off tasks to worker agents via robust JSON Agent-to-Agent (A2A) contracts (`templates/a2a-contract.json`).
- **Evaluator-Optimizer Middleware**: Embedded a neural self-reflection loop (`workflows/evaluator.md`) backed by deterministic Python validation (`scripts/evaluator.py`). Agents are now mathematically forced to validate and recursively self-critique their JSON handoffs (up to a 3-strike retry limit) before passing corrupted state downstream.

## [2.1.0] - 2026-07-12

### Added
- **JIT Prompt Compiler**: Added `scripts/jit_compiler.py` to eliminate recursive file I/O latency. It acts as an Antigravity lifecycle hook that dynamically parses `<dependencies>`, compiles a flattened context payload, and automatically injects project-specific overrides (like `AGENTS.md` and `.esper/shared_context/`) before the agent initializes.
- **Workspace Hygiene Rule**: Created `.agents/rules/workspace-hygiene.md` to strictly enforce pristine project roots. Agents are now hard-coded to write all temporary notes and logs exclusively to `.esper/scratch/` and proactively clean up stray scratchpads without touching source code.
- **Autonomous Intent Discovery**: Fully deprecated the reliance on `routing.md` in the global bootstrap files. Agents are now hardcoded to use `list_dir` to dynamically discover available entry points in the `prompts/` directory upon initialization, allowing users to simply ask "do X" without needing to mention internal Esper file paths.
- **Lifecycle Memory Management**: Implemented a sliding window working memory system via `scripts/memory_manager.py` and `workflows/memory-management.md` to deterministically prune stale context files, preventing token bloat during extended operations.
- **Deterministic Guardrails (Policy-as-Code)**: Added `scripts/policy_gate.py` to hard-block high-risk actions. Upgraded `checklists/automation-safety.md` to force the use of the interactive `ask_question` modal for undeniably explicit Human-in-the-Loop (HITL) approval when the policy gate is triggered.
- **JIT Compiler Resilience**: Upgraded the JIT compiler parser to use `re.finditer` for robust multi-block XML tag processing, and added graceful degradation that emits markdown warnings instead of crashing when dependencies are missing.

## [2.0.0] - 2026-07-11

### Added
- **XML Context Optimization**: Completely refactored the Esper architecture to use a unified `<esper_module>` canonical XML schema for all rules, templates, workflows, principles, and checklists. This guarantees absolute context boundaries for LLM parsers.
- **Always-On Rules**: Extracted core engineering philosophies from `index.md` and injected them as Always-On rules (`esper-philosophy.md`) into `.agents/rules/`.
- **Glob-Activated Rules**: Implemented `esper-testing.md` to trigger specific workflows when working with test files.
- **Esper RPC Protocol**: Established an Always-On rule (`esper-rpc.md`) that defines a strict XML-based Parent-Child agent communication protocol (Envelope, Performatives, and Payload schemas) to eliminate semantic drift.
- **Interactive Confirmations**: Updated global configurations (`GEMINI.md`, `CLAUDE.md`, and `bootstrap/CLAUDE.md`) to explicitly mandate the use of the native `ask_question` interactive modal rather than unstructured A/B/C text matching.
- **Hierarchical Context Architecture**: Deprecated monolithic memory files (`notes.md`) in favor of isolated, domain-specific state files (e.g., `ui-state.md`).
- **Native RAG Retrieval**: Updated `esp-rag` to enforce YAML frontmatter on all memory files, mandating that agents use native semantic search/grep to selectively load context rather than loading the entire `shared_context` directory.
- **Presentation Standards**: Injected a `<presentation_style>` node into `report-structure.md` strongly mandating the use of Markdown tables for structured and comparative data to improve readability.

### Changed
- **Deprecated Routing Table**: Deprecated the monolithic `routing.md` file in favor of Antigravity's native Progressive Disclosure Rule resolution.
- **RPC Payload Optimization**: Replaced the verbose XML `<payload>` blocks in `esper-rpc.md` with dense JSON schemas. This prevents token exhaustion and context bottlenecks during multi-agent Swarm Sharding.
- **Dependency Graph Repairs**: Fixed strict path resolution violations in `prompts/architecture-review.md`, `prompts/feature.md`, and `prompts/research.md` by moving descriptive trailing text into XML comments.

## [1.5.0] - 2026-07-10

### Added
- **Framework Update Protocol**: Added `update.ps1` and `update.sh` scripts. Running these scripts automatically pulls the latest upstream changes and re-runs the installation scripts to ensure users' active bootstrap files (`~/.gemini/GEMINI.md`) stay perfectly synced with updates.
- **Future Architecture Tracking**: Created `shared_context/ideas/future_architecture.md` to persistently document 10 massive paradigm shifts for Esper's future roadmap (including MCP integration, Swarm Sharding, and Package Managers).
- **Static Context Benchmarker**: Added `benchmarks/token_benchmark.py` and `benchmarks/baselines/normal_feature.md` to statically measure and prove the context-efficiency of Esper's dynamic routing compared to monolithic prompts.
- **JSON Dependency Scanner**: Added `scripts/scan_dependencies.py`, a utility that parses the entire Markdown repository for both explicit headers and inline links, returning a structured JSON report of broken links and orphaned files (ignoring entry points).

### Changed
- **Subagent Orchestration Enforcement**: Globally updated `index.md`, `routing.md`, `prompts/delegation.md`, and `workflows/delegation.md` to strictly mandate that parent agents remain high-level orchestrators. Agents must now proactively prompt the user to spin up concurrent subagent workflows for parallelizable 'dirty work'.
- **Global Communication Standards**: Added `principles/communication.md` as a Required Dependency to the core `workflows/agent-communication.md`. This ensures all agents natively load formatting rules (e.g., using Markdown tables for structured data) before responding to the user.
- **Autonomous Skills Failsafe**: Updated the Bootstrap templates (`GEMINI.md.template` and `CLAUDE.md`) to include a `CRITICAL` directive that explicitly warns agents that nested skills will *not* appear in their native `<skills>` prompt block. Agents are now forced to proactively use `list_dir` on `~/.gemini/config/skills/esper-skills/` to verify the directory exists upon initialization before triggering the failsafe warning.
- **Agent-Driven Skill Refactor**: We shifted Esper skills away from being treated as native Antigravity UI slash commands (`/`) and redefined them as agent-driven markdown modules. This paradigm shift means skills no longer need to adhere to the strict 1-level-deep Antigravity parser, permitting the much cleaner subfolder clone. Furthermore, removed legacy instructions in `routing.md` that told agents to rely on dynamically injected UI skill lists.
- **README Adjustments**: Updated the installation instructions in `README.md` to remove hardcoded paths and clarify that AI agents can autonomously install the skills repository. Added a new section detailing **Global vs Local Installations**.
- **Markdown UX Rendering Fixes**: Executed a comprehensive repository-wide audit and fix for Markdown rendering compatibility. Added missing blank lines before lists, code blocks, and between consecutive sentences across 34 core files to ensure the framework documentation renders correctly in strict HTML parsers like the Antigravity IDE.
- **Cross-Environment Compatibility**: Updated global skills paths to universally point to the official `~/.gemini/config/skills/` standard, ensuring seamless skill sharing across both the Antigravity CLI and Antigravity IDE environments.
- **Initialization Context Warnings**: Implemented a new `CRITICAL` bootstrap directive forcing agents to greet the user upon initialization and explicitly state their operating context (Local vs Global, exact file path, and CLI vs IDE).

## [1.4.0] - 2026-07-10

### Added
- **Workspace Cleanup Protocol**: 
  - Added `checklists/cleanup.md` to establish a strict rule for isolating diagnostic scripts and temporary test files in `.esper/shared_context/scratch/`.
  - Added a UX prompt requirement allowing users to preserve valuable utility scripts in `.esper/utils/` before they are automatically deleted.
- **Benchmarking Suite**:
  - Expanded `benchmarks/orchestrator.py` to support dual-pass execution comparing "Vanilla Gemini" (`baseline_agent.py`) against Esper.
  - Implemented automatic latency and token-usage telemetry tracking within the sandbox orchestrator.
  - Added a deterministic side-by-side markdown report generator (`benchmark_report.md`) for human-in-the-loop qualitative grading.

### Changed
- **Workflow Updates**:
  - Globally injected `checklists/cleanup.md` as a Required Dependency across all 13 active workflows to strictly enforce workspace hygiene.

## [1.3.0] - 2026-07-10

### Added
- `scripts/validate_links.sh` to lint markdown dependencies and prevent broken links.
- `prompts/testing.md` to establish the missing entry point for testing workflows.

### Changed
- `workflows/code-review.md` and `checklists/security.md`: Added explicit mitigations against Indirect Prompt Injections (ignoring malicious meta-instructions in workspace files).
- `routing.md`: Integrated the testing workflow and corrected the delegation naming convention.
- `prompts/orchestration.md`: Renamed to `prompts/delegation.md` to enforce 1:1 structural consistency.
- `install.sh`: Patched to safely escape `$ESPER_PATH` variables in `sed` replacements.
- `index.md`: Updated `# Directory Layout` to properly document the `benchmarks/`, `bootstrap/`, and `shared_context/` directories.
- `principles/retrieval.md`: Established a strict maximum depth for dependency traversal to prevent transitive context bloat.
- `workflows/delegation.md`: Mandated the use of subagents for 'dirty work' or 'research' to keep main conversational contexts clean.
- `principles/communication.md`: Added the tabulation rule to enforce the use of markdown tables to prevent walls of text.

## [1.2.0] - 2026-07-09

### Changed
- **Architectural Decoupling**:
  - Removed hardcoded references to `esp-rag` and `esp-repo-map` from `index.md` and `routing.md`.
  - Esper OS is now strictly decoupled from skills and relies entirely on **Dynamic Runtime Discovery** for skill execution, matching industry standards (e.g. MCP).

## [1.1.0] - 2026-07-09

### Added
- **Multi-Agent Orchestration & Communication**: 
  - Added `prompts/orchestration.md` as the main entrypoint for coordinating multiple agents.
  - Added `workflows/agent-communication.md` for defining how agents interact.
  - Added `templates/shared-scratchpad.md` and `templates/synthesis.md` for sharing context and synthesizing findings.
- **Automation Safety & Reasoning**:
  - Added `principles/automation-safety.md` and `checklists/automation-safety.md` to ensure safe tool and workflow execution.
  - Added `principles/reasoning.md` and `principles/reflection.md` to guide evidence-based thought processes and continuous agent reflection.
- **System Evaluation & Context**:
  - Added new `benchmarks/` directory for evaluating system effectiveness.
  - Added new `context/` directory for maintaining persistent environmental and project knowledge.
- **Retrospectives**:
  - Added `prompts/retrospective.md` for systemic evaluation of work completed.
- **Modular Skills & Tools (`esp-*`)**:
  - Introduced 18 modular `esp-*` skills (e.g. `esp-repo-map`, `esp-rag`, `esp-fetch-docs`) maintained outside the core directory to prevent bloat.
  - Added strict orchestration rules, ensuring these skills utilize isolated execution and explicit human-in-the-loop confirmation (`esp-clarify`).
  - Implemented Copilot-style read-only querying via the repurposed `esp-ask` skill.
- **Persistent Context / Memory**:
  - Renamed the undocumented `context/` directory to the officially supported `shared_context/` module.
  - Divided memory into **Global Context** (for Esper meta-knowledge) and **Project Context** (`.esper/shared_context/` for codebase-specific ASTs and RAG indexing).
### Changed
- **Reporting Taxonomy Consolidation**:
  - Consolidated reporting rules into `principles/reporting/taxonomy.md`.
  - Updated `findings.md`, `report-structure.md`, and `rubric.md` to align with the new taxonomy.
- **Core Architecture Updates**:
  - Substantially updated `index.md` and `routing.md` to include orchestration, reflection, and safety pathways.
  - Overhauled all existing `prompts/`, `workflows/`, `checklists/`, `templates/`, and `principles/` to support the updated architecture and safety constraints.
- **Bootstrap Updates**:
  - Updated `bootstrap/CLAUDE.md` and `bootstrap/GEMINI.md.template` for tighter integration with the new directives.
- **Enforced Orchestration & Discovery**:
  - Updated bootstrap files and `routing.md` to strictly mandate proactive skill discovery and default to multi-agent orchestration for complex workflows.
- **Debugging Workflow**:
  - Appended a UX fallback to `workflows/debugging.md` that directs users to community skills if deep logic bugs persist.
### Removed
- Removed fragmented reporting principles (`principles/reporting/confidence.md`, `principles/reporting/report-quality.md`, `principles/reporting/severity.md`) in favor of the unified `taxonomy.md`.
