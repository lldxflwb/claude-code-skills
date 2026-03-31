#!/usr/bin/env bash
# Update Agent SDK documentation
# Wrapper script that calls the Python updater
#
# Usage: bash skills/agent-sdk/scripts/update-docs.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Claude Agent SDK Documentation Updater ==="
echo ""

python3 "$SCRIPT_DIR/update-docs.py"
