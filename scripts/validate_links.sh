#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ESPER_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$ESPER_ROOT"

echo "Validating markdown links..."
ERRORS=0

while IFS= read -r -d '' file; do
  # Extract linked paths
  links=$(awk '
    /^## (Required Dependencies|Canonical Sources)/ {flag=1; next}
    /^## / {flag=0}
    flag && /^- / {
      s = $0
      sub(/^[ \t]*- /, "", s)
      gsub(/`/, "", s)
      if (match(s, /\[.*\]\([^)]+\)/)) {
        sub(/.*\(/, "", s)
        sub(/\).*/, "", s)
      }
      sub(/\r$/, "", s)
      print s
    }
  ' "$file")

  for link in $links; do
    if [[ -n "$link" && ! -f "$link" ]]; then
      echo "❌ Broken link in ${file#./}: $link"
      ERRORS=$((ERRORS + 1))
    fi
  done
done < <(find . -type f -name "*.md" -print0)

if [ "$ERRORS" -gt 0 ]; then
  echo "Found $ERRORS broken links."
  exit 1
else
  echo "✅ All links are valid."
fi
