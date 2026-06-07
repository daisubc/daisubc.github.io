#!/bin/bash
# Double-click this file on your Mac to start Inbox Triage.
# It builds the web app (first run only) and serves everything from one address.
set -e
cd "$(dirname "$0")"

echo "==> Checking the local AI (Ollama)..."
if ! command -v ollama >/dev/null 2>&1; then
  echo "    Ollama is not installed. Get it from https://ollama.com, then run this again."
  read -r -p "Press Return to close." _; exit 1
fi
# Make sure the model is present (downloads once).
ollama list | grep -q "llama3.1" || { echo "    Downloading the model (one time)..."; ollama pull llama3.1; }

echo "==> Building the web app (first time can take a few minutes)..."
cd frontend
npm install
npm run build
cd ..

echo "==> Starting the app on http://localhost:8000 ..."
cd backend
[ -d .venv ] || python3 -m venv .venv
source .venv/bin/activate
pip install -q -r requirements.txt

echo ""
echo "============================================================"
echo " The app is now running."
echo "   • On this Mac: open  http://localhost:8000"
echo "   • To use it on your iPad: start your secure link (ngrok),"
echo "     then open the https://... address it gives you."
echo " Keep this window open while you use the app. Close it to stop."
echo "============================================================"
echo ""
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
