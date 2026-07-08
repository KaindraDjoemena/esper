---
name: Retrieval Philosophy
---

# Retrieval Philosophy

## Purpose

Define how engineering knowledge should be discovered, retrieved, and composed by agents to minimize context overhead.

## Core Philosophy

Esper scales through retrieval, not accumulation. Context should be earned, not assumed.

## Principles

1. **Knowledge is Discoverable, Not Preloaded**: Agents should discover knowledge via `routing.md` and explicit module relationships. Never load the entire workspace eagerly.
2. **Context is Earned**: Do not load modules "just in case." Only load a module when there is concrete evidence that the task requires it.
3. **Incremental Discovery**: Start with the absolute minimum set of required modules. Expand context iteratively as the investigation uncovers new requirements or complexities.
4. **Progressive Disclosure**: Read interfaces, signatures, and documentation first. Only read deep implementations if the interface is insufficient to answer the current question.
5. **Retrieval Stopping Conditions**: Stop gathering context as soon as you have enough evidence to formulate a testable hypothesis or a viable alternative. Only resume retrieval if the hypothesis is disproven.
6. **Context Pruning**: Actively discard or deprioritize information that proves irrelevant during investigation to avoid polluting reasoning.
7. **Canonical Sources**: Do not duplicate definitions. If a module requires understanding a concept (like "Severity"), it should reference the canonical source. Load the canonical source only if you actually need to apply that concept.
8. **Minimize Overhead**: Favor modular composition over monolithic context. The smaller the active context, the sharper the reasoning.

## Canonical Sources

- principles/engineering.md
