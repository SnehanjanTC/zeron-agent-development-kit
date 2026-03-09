# ZAK Code Auditor Demo

This demo showcases how to build a custom LLM-powered AppSec agent with the Zeron Agent Development Kit.

The **Code Auditor Agent** is designed to act as a Senior AppSec Engineer. It is given a custom tool (`read_local_code_file`) that allows it to read test files from the `demo` directory and scan them for security vulnerabilities like SQL injection and hardcoded secrets.

## Contents
* `code-auditor.yaml`: The ZAK declarative schema for the agent, using `reasoning.mode: llm_react`.
* `code_auditor.py`: The agent class definition containing the system prompt.
* `tools.py`: The custom `@zak_tool` used by the agent to read local files safely.
* `vulnerable_app.py`: A deliberate vulnerable Python application for the agent to scan.
* `../run_code_auditor.sh`: A helper bash script to execute the agent.

## How to Run

Because this agent operates in `llm_react` mode, it uses ZAK's underlying LLM integrations. By default, it requires `OPENAI_API_KEY`.

1. From the project root, ensure you have installed with LLM dependencies:
   ```bash
   pip install -e ".[llm]"
   ```

2. Run the demo script (it will prompt for your API key if not set):
   ```bash
   ./run_code_auditor.sh
   ```

## What Happens During Execution
1. ZAK validates the agent schema.
2. The agent initializes and is handed the `read_local_code_file` tool.
3. The LLM decides to execute the tool to read `demo/vulnerable_app.py`.
4. The tool returns the source code exactly as-is.
5. The LLM analyzes the source code and produces a structured JSON output of findings, which ZAK logs to the terminal.
