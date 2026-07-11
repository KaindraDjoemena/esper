# Changelog

All notable changes to this project will be documented in this file.

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
