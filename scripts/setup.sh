#!/bin/bash
set -euo pipefail
echo "Setting up GCP Architecture Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
