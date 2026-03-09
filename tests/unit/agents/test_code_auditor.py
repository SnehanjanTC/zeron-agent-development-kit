"""
Unit tests for the Code Auditor agent.
"""

from unittest.mock import MagicMock


from zak.agents.code_auditor.agent import CodeAuditorAgent
from zak.core.runtime.agent import AgentContext
from zak.core.tools.builtins import read_local_code_file


def test_code_auditor_system_prompt() -> None:
    """Test that the system prompt includes the tenant ID and target file."""
    agent = CodeAuditorAgent()
    
    mock_dsl = MagicMock()
    context = AgentContext(
        tenant_id="test_tenant",
        trace_id="test_trace",
        environment="test",
        dsl=mock_dsl,
        metadata={"target_file": "src/main.py"}
    )
    
    prompt = agent.system_prompt(context)
    
    assert "test_tenant" in prompt
    assert "src/main.py" in prompt
    assert "read_local_code_file" in prompt


def test_code_auditor_tools() -> None:
    """Test that the agent exposes exactly the right tools."""
    agent = CodeAuditorAgent()
    tools = agent.tools
    
    assert len(tools) == 1
    assert tools[0] == read_local_code_file
