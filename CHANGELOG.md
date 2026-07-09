# Changelog

All notable changes to this project will be documented in this file.

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
