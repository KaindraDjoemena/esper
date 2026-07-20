---
name: Initialization
---

<esper_module type="workflow">
<purpose>
Bootstrap a new project with Esper context by creating the required `.esper/` directory structure and tracking files.
</purpose>
<when_to_use>
<item>when an agent starts working in a project that has no `.esper/` directory yet</item>
<item>when initializing a new repository for Esper compatibility</item>
</when_to_use>
<instructions>
<execution_steps>
<step>Detect existing context: Check if `.esper/` already exists in the project root. If yes, skip initialization and notify the user — do not overwrite existing state.</step>
<step>Create directory scaffold: Create the following structure in the project root:
  - `.esper/shared_context/notes/`
  - `.esper/shared_context/checkpoints/`
  - `.esper/scratch/`
</step>
<step>Create `notes-manifest.md`: Create `.esper/shared_context/notes-manifest.md` and initialize it with a markdown table header: `| Date | Title | Tags | File |` and a horizontal rule below.</step>
<step>Create `checkpoints/index.md`: Create `.esper/shared_context/checkpoints/index.md` and initialize it with a header `# Checkpoint Index` and a markdown table: `| Date | Slug | Summary |`.</step>
<step>Update `.gitignore`: Check if a `.gitignore` exists. If yes, check if `.esper/` is already listed — if not, append it. If no `.gitignore` exists, create one with `.esper/` as the first entry. CRITICAL: Always ask user for explicit confirmation before modifying `.gitignore`.</step>
<step>Summarize: Report what was created and remind the user that:
  - `.esper/shared_context/notes/` is for `esp-note` drops
  - `.esper/shared_context/checkpoints/` is for `esp-cpt` snapshots
  - `.esper/` is gitignored and local-only by default
</step>
</execution_steps>
</instructions>
<dependencies>
<required>
</required>
</dependencies>
</esper_module>
