#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -q -r requirements.txt

echo "Starting Tic Tac Toe web app at http://localhost:8080"
exec gunicorn web_app:app --bind "0.0.0.0:${PORT:-8080}" --reload
