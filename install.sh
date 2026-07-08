#!/bin/bash
set -e

# Get the absolute path of the directory this script is in
ESPER_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# The root .gemini directory
GEMINI_PATH="$(dirname "$ESPER_PATH")"

echo "Installing Esper from $ESPER_PATH to $GEMINI_PATH"

# Replace the placeholder and save to root .gemini
sed "s|{{ESPER_PATH}}|$ESPER_PATH|g" "$ESPER_PATH/bootstrap/GEMINI.md.template" > "$GEMINI_PATH/GEMINI.md"
echo "Successfully generated GEMINI.md"

# Copy CLAUDE.md
cp "$ESPER_PATH/bootstrap/CLAUDE.md" "$GEMINI_PATH/CLAUDE.md"
echo "Successfully copied CLAUDE.md"

# Copy root README
cp "$ESPER_PATH/bootstrap/README.md" "$GEMINI_PATH/README.md"
echo "Successfully copied root README.md"

echo "Esper installation complete!"
