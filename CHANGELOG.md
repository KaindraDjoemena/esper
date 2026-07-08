# Changelog

All notable changes to this project will be documented in this file.

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
