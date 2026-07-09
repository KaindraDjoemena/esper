# Esper

Esper is a modular engineering operating system for AI coding assistants. 

Rather than relying on a single monolithic system prompt, Esper decomposes engineering knowledge into small, focused modules with clearly defined responsibilities. These modules are composed together at runtime to guide reasoning, reduce oversight, and improve consistency across engineering tasks.

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

## Persistent Memory (Context)

Esper supports state persistence via the `shared_context/` module. 
- **Global Context** (`~/.gemini/esper/shared_context/`) acts as the framework's meta-knowledge base.
- **Project Context** (`<project-root>/.esper/shared_context/`) is generated dynamically by agent skills (e.g., checkpoints, notes, mapping). You should add `.esper/` to your project's `.gitignore` to prevent memory contamination in your public git history.

## Available Skills

Esper also supports modular skills that extend its capabilities (e.g., auditing, scaffolding, orchestration). These are maintained in a separate repository to prevent dependency hell.

You can clone the skills repository into your `.gemini/antigravity-cli/skills/` directory:

```bash
git clone https://github.com/KaindraDjoemena/esper-skills.git ~/.gemini/antigravity-cli/skills
```

Once cloned, agents can invoke these skills on demand to perform complex workflows.
