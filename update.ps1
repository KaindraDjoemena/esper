$ErrorActionPreference = "Stop"

Write-Host "Pulling latest Esper updates..."
git pull origin main

Write-Host "Updating bootstrap configuration..."
.\install.ps1

Write-Host "Esper update complete!"
