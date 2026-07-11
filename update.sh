#!/bin/bash
set -e

echo "Pulling latest Esper updates..."
git pull origin main

echo "Updating bootstrap configuration..."
./install.sh

echo "Esper update complete!"
