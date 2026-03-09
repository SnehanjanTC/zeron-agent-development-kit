import os
import json
from ulid import ULID
from zak.core.dsl.parser import load_agent_yaml
from zak.core.runtime.agent import AgentContext
from zak.core.runtime.executor import AgentExecutor
from zak.tenants.context import TenantRegistry
from demo.code_auditor import CodeAuditorAgent

def generate_report():
    yaml_path = "demo/code-auditor.yaml"
    tenant = "zeron.one"
    env = "staging"
    
    # Setup
    dsl = load_agent_yaml(yaml_path)
    trace_id = str(ULID())
    
    registry = TenantRegistry()
    if not registry.exists(tenant):
        registry.register(tenant_id=tenant, name=tenant)
        
    context = AgentContext(
        tenant_id=tenant,
        trace_id=trace_id,
        dsl=dsl,
        environment=env,
        metadata={"target_file": "demo/vulnerable_app.py"}
    )
    
    agent = CodeAuditorAgent()
    executor = AgentExecutor()
    
    # Run the agent
    print("Running Code Auditor agent...")
    result = executor.run(agent, context)
    
    if result.success:
        print("Agent ran successfully! Generating Markdown report...")
        
        # The LLM outputs the final JSON string in the 'summary' key
        try:
            report_data = json.loads(result.output.get("summary", "{}"))
        except json.JSONDecodeError:
            print("Warning: Could not parse LLM output as JSON. Using Raw string.")
            report_data = {"overall_security_posture": result.output.get("summary", "")}
        
        # Create markdown content
        md_content = f"# Code Auditor Security Report\n\n"
        md_content += f"**Target File**: `demo/vulnerable_app.py`\n"
        md_content += f"**Tenant**: `{tenant}`\n"
        md_content += f"**Generated Trace ID**: `{trace_id}`\n\n"
        
        md_content += f"### Summary\n"
        md_content += f"- **Files Scanned**: {report_data.get('files_scanned', 1)}\n"
        md_content += f"- **Critical Findings**: {report_data.get('critical_findings_count', 0)}\n"
        md_content += f"- **Overall Posture**: {report_data.get('overall_security_posture', 'N/A')}\n\n"
        
        md_content += f"### Vulnerability Findings\n\n"
        
        findings = report_data.get("findings", [])
        if not findings:
            md_content += "No vulnerabilities found.\n"
        else:
            for i, f in enumerate(findings, 1):
                md_content += f"#### {i}. {f.get('type', 'Unknown Vulnerability')}\n"
                md_content += f"- **Severity**: `{f.get('severity', 'none').upper()}`\n"
                md_content += f"- **Location**: {f.get('line_number', 'unknown')}\n"
                md_content += f"- **Description**: {f.get('description', 'N/A')}\n"
                md_content += f"- **Remediation**: {f.get('remediation', 'N/A')}\n\n"
                
        # Write to file
        output_file = "demo/code_auditor_report.md"
        with open(output_file, "w") as f:
            f.write(md_content)
        print(f"Report written to: {output_file}")
        
    else:
        print("Agent run failed!")
        for error in result.errors:
            print(f"- {error}")

if __name__ == "__main__":
    generate_report()
