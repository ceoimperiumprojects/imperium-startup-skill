#!/usr/bin/env bash
# Setup script for founder-kb CLI (optional power layer)
# Installs the semantic search tool over 10 startup books (2,019 chunks)

set -e

REPO_URL="https://github.com/ceoimperiumprojects/founder-ai-mentor.git"
INSTALL_DIR="/tmp/founder-ai-mentor"

echo "🔧 Setting up founder-kb CLI..."
echo ""

# Step 1: Clone or update repo
if [ -d "$INSTALL_DIR" ]; then
    echo "✓ Repository already exists at $INSTALL_DIR"
    cd "$INSTALL_DIR"
    git pull --quiet 2>/dev/null || echo "  (offline mode — using existing files)"
else
    echo "→ Cloning founder-ai-mentor..."
    git clone "$REPO_URL" "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

# Step 2: Install
echo "→ Installing founder-kb..."
pip install -e . --quiet 2>/dev/null || pip install -e . --break-system-packages --quiet 2>/dev/null || {
    echo ""
    echo "⚠ Installation failed. Try:"
    echo "  pip install -e $INSTALL_DIR --break-system-packages"
    echo "  OR use a virtual environment:"
    echo "  python -m venv ~/.founder-kb-venv && source ~/.founder-kb-venv/bin/activate && pip install -e $INSTALL_DIR"
    exit 1
}

# Step 3: Validate
echo ""
echo "→ Validating installation..."
if command -v founder-kb &> /dev/null; then
    echo ""
    founder-kb stats
    echo ""
    echo "✅ founder-kb installed successfully!"
    echo ""
    echo "Usage:"
    echo "  founder-kb search \"how to validate a startup idea\""
    echo "  founder-kb sources"
    echo "  founder-kb search \"negotiation tactics\" --source never-split-the-difference"
    echo "  founder-kb --json search \"pricing strategy\" | jq"
else
    echo "⚠ founder-kb command not found in PATH."
    echo "  Try: source ~/.profile && founder-kb stats"
    exit 1
fi
