---
name: Delegation
---

# Delegation Workflow

## Purpose

Coordinate complex engineering tasks by planning, decomposing, delegating, and integrating work across multiple agents.

## When to Use

- implementing large features
- performing broad architectural reviews
- conducting extensive parallel research
- executing multi-phase implementation plans

## Workflow

### 1. Plan and Decompose
Identify if the task is too large for sequential execution. Decompose the task into independent, non-overlapping subtasks. Assign **Specialized Roles** by providing each subagent with a specific prompt as its entry point (e.g., assign `prompts/research.md` to create a Researcher, or `prompts/code-review.md` to create a Reviewer). Always use subagents for 'dirty work' (like bulk file editing) or 'research' (like sweeping directories) to keep the main chat context clean.

### 2. Package Context
For each subtask, prepare the specific context the subagent will need:
- The exact objective
- The required dependencies (workflows, templates)
- Existing evidence and constraints
Exclude unnecessary context to preserve reasoning quality.

### 3. Delegate and Execute
Invoke the subagents with their partitioned tasks and packaged context. Ensure each subagent has a clear, isolated responsibility.

### 4. Validate
When a subagent completes its task, validate its output:
- Are the conclusions supported by evidence?
- Were the constraints respected?
- Are there any new assumptions or unresolved questions introduced?

### 5. Integrate and Review
Synthesize the validated findings or code from all subagents into the primary task using a clear **Merge Strategy**:
- For code: Ensure that merged changes from different agents do not create logical contradictions, syntax errors, or overlapping modifications.
- For reports: Synthesize findings into a single, unified narrative. Do not simply append subagent reports together.
Perform a final review to ensure the integrated result forms a cohesive, working solution that satisfies the original intent.

## Required Dependencies

- checklists/delegation.md
- workflows/revision.md
- checklists/automation-safety.md

## Canonical Sources

- principles/delegation.md
