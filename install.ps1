$ErrorActionPreference = "Stop"

# Get the absolute path of the directory this script is in (e.g., C:/Users/KD/.gemini/esper)
$EsperPath = (Get-Item -Path ".\").FullName.Replace("\", "/")
# The root .gemini directory
$GeminiPath = (Get-Item -Path "..\").FullName.Replace("\", "/")

Write-Host "Installing Esper from $EsperPath to $GeminiPath"

# Read the template and replace the placeholder
$TemplateContent = Get-Content -Path "$EsperPath/bootstrap/GEMINI.md.template" -Raw
$ConfiguredContent = $TemplateContent -replace "\{\{ESPER_PATH\}\}", $EsperPath

# Write to the root .gemini directory
Set-Content -Path "$GeminiPath/GEMINI.md" -Value $ConfiguredContent
Write-Host "Successfully generated GEMINI.md"

# Copy CLAUDE.md
Copy-Item -Path "$EsperPath/bootstrap/CLAUDE.md" -Destination "$GeminiPath/CLAUDE.md" -Force
Write-Host "Successfully copied CLAUDE.md"

# Copy root README
Copy-Item -Path "$EsperPath/bootstrap/README.md" -Destination "$GeminiPath/README.md" -Force
Write-Host "Successfully copied root README.md"

Write-Host "Esper installation complete!"
