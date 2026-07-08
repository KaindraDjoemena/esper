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
git clone https://github.com/YOUR_USERNAME/esper.git ~/.gemini/esper

# 3. Run the installation script to configure your AI bootstrap files
cd ~/.gemini/esper
.\install.ps1
```

### macOS / Linux (Bash / Zsh)
```bash
# 1. Create the .gemini directory if it doesn't exist
mkdir -p ~/.gemini

# 2. Clone the repository
git clone https://github.com/YOUR_USERNAME/esper.git ~/.gemini/esper

# 3. Run the installation script to configure your AI bootstrap files
cd ~/.gemini/esper
./install.sh
```
