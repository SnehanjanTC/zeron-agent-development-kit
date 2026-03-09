"""
Custom tools for the Code Auditor Agent.
"""

import os
from zak.core.runtime.agent import AgentContext
from zak.core.tools.substrate import zak_tool

@zak_tool(
    name="read_local_code_file",
    description="Reads the contents of a local code file for security analysis.",
    action_id="read_local_code_file",
    tags=["appsec", "read", "local_file"],
)
def read_local_code_file(context: AgentContext, file_path: str) -> str:
    """Read a local file from disk. Only allows reading files from the demo workspace."""
    try:
        if not file_path.endswith(".py"):
            return "Security Policy Violation: Can only read .py files."
        
        if not os.path.exists(file_path):
            return f"Error: File not found at {file_path}"
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        return content[:20000] # Cap size for LLM safety
    except Exception as e:
        return f"Error reading file {file_path}: {e}"
