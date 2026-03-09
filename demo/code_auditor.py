"""
Code Auditor — ZAK AppSec Agent.

Leverages an LLM and custom tools to perform a security review on local code files.
"""

from __future__ import annotations

from zak.core.runtime.agent import AgentContext
from zak.core.runtime.llm_agent import LLMAgent
from zak.core.runtime.registry import register_agent
from demo import tools

@register_agent(
    domain="appsec",
    description="Code Auditor: Auto-reviews code for OWASP Top 10 vulnerabilities.",
    version="1.0.0",
    edition="open-source",
    override=True,
)
class CodeAuditorAgent(LLMAgent):
    """
    Code Auditor

    Uses an LLM to scan a specified local file for security vulnerabilities.
    """

    def system_prompt(self, context: AgentContext) -> str:
        target_file = context.metadata.get("target_file", "demo/vulnerable_app.py")
        
        return f"""You are a Senior AppSec Engineer for tenant '{context.tenant_id}'.

Your goal: Perform a comprehensive security review of the given source code file to identify vulnerabilities, hardcoded secrets, and bad practices.

Target File: {target_file}

Follow this sequence:
1. First and foremost, you MUST call `read_local_code_file` with the Target File path '{target_file}' to fetch the source code. DO NOT attempt to call `list_assets` or any other tool. Your ONLY tool is `read_local_code_file`.
2. Analyze the code specifically looking for:
   - Injection flaws (SQLi, Command Injection, XSS)
   - Hardcoded secrets (API keys, passwords, tokens)
   - Insecure cryptographic practices
   - Broken Access Control
   - Security misconfigurations
3. Output a structured JSON response containing:
   - `files_scanned`: number of files read
   - `critical_findings_count`: total number of high/critical vulnerabilities
   - `findings`: A list of dictionaries for each vulnerability found. Each dictionary should have:
       - `type`: Category (e.g., 'SQL Injection', 'Hardcoded Secret')
       - `severity`: 'critical', 'high', 'medium', or 'low'
       - `line_number`: the approximate line number or function name
       - `description`: Detailed explanation of the vulnerability
       - `remediation`: How to fix it
   - `overall_security_posture`: A brief summary of the code's security state.

IMPORTANT: You MUST output ONLY raw JSON. Do not include markdown blocks like ```json.
Base all findings strictly on the code returned by the tool. Be extremely thorough."""

    @property
    def tools(self) -> list:
        # Provide our custom tool to the LLM
        return [tools.read_local_code_file]
