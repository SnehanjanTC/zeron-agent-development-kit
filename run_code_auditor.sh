#!/bin/bash

# Ensure we're in the project root
if [[ ! -d "demo" ]]; then
  echo "Error: Please run this script from the zeron-agent-development-kit root directory."
  exit 1
fi

export PYTHONPATH="${PYTHONPATH}:$(pwd)"

echo "======================================================"
echo "    ZAK Code Auditor Agent | AppSec Demonstration     "
echo "======================================================"
echo ""

# Check for LLM Provider API Key
if [[ -z "${OPENAI_API_KEY}" ]]; then
  echo "WARNING: OPENAI_API_KEY is not set."
  echo "Please enter your OpenAI API Key to run the LLM (it will not be saved):"
  read -s API_KEY
  export OPENAI_API_KEY="$API_KEY"
  echo "Key initialized."
  echo ""
fi

# Activate virtual environment
if [[ -f "venv/bin/activate" ]]; then
  source venv/bin/activate
else
  echo "Error: Virtual environment not found. Please setup 'venv' first."
  exit 1
fi

echo ">> Validating Agent Definition..."
zak validate demo/code-auditor.yaml

echo ""
echo ">> Target file for code review: demo/vulnerable_app.py"
echo ">> Running the Code Auditor Agent using LLM ReAct..."
echo ""

# We pass target_file via metadata into the context
zak run demo/code-auditor.yaml --tenant demo_acme
