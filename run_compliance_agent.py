#!/usr/bin/env python3
"""
ZAK — ISO 27001 + SOC 2 Compliance Agent Runner
================================================

Runs the compliance agent for any organisation. Prompts for org details
interactively, or accepts them as command-line arguments.

Usage (interactive):
    python run_compliance_agent.py

Usage (non-interactive / CI):
    python run_compliance_agent.py \\
        --org "Acme Corp" \\
        --industry "SaaS" \\
        --size "mid-size" \\
        --tenant "acme" \\
        --output "./compliance_output" \\
        --provider anthropic \\
        --model claude-sonnet-4-6

Requirements:
    pip install anthropic          # if using Anthropic (recommended)
    pip install openai             # if using OpenAI
    export ANTHROPIC_API_KEY=...   # or OPENAI_API_KEY
"""

from __future__ import annotations

import argparse
import os
import sys
import textwrap
from datetime import date
from pathlib import Path

# ── Make sure zak package is importable from project root ──────────────────
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="ZAK ISO 27001 + SOC 2 Compliance Agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(__doc__ or ""),
    )
    p.add_argument("--org",      default=None, help="Organisation name")
    p.add_argument("--industry", default=None, help="Industry / sector")
    p.add_argument("--size",     default=None, help="Organisation size (e.g. mid-size, startup, enterprise)")
    p.add_argument("--tenant",   default=None, help="Tenant / namespace ID")
    p.add_argument("--output",   default=None, help="Output directory for policy docs and gap report")
    p.add_argument("--provider", default="anthropic", choices=["anthropic", "openai", "google"], help="LLM provider")
    p.add_argument("--model",    default=None, help="LLM model name (defaults to provider's recommended model)")
    p.add_argument("--yaml",     default="agents/iso27001-soc2-compliance.yaml", help="Path to agent YAML")
    p.add_argument("--dry-run",  action="store_true", help="Validate YAML only, don't run the agent")
    return p.parse_args()


def prompt_if_missing(args: argparse.Namespace) -> argparse.Namespace:
    """Interactively prompt for any missing required fields."""
    console.print()
    console.print(Panel.fit(
        "[bold cyan]ZAK — ISO 27001 + SOC 2 Compliance Agent[/bold cyan]\n"
        "[dim]Generates a gap report and complete policy documentation[/dim]",
        border_style="cyan",
    ))
    console.print()

    if not args.org:
        args.org = Prompt.ask("[bold]Organisation name[/bold]", default="My Organisation")
    if not args.industry:
        args.industry = Prompt.ask("[bold]Industry / sector[/bold]", default="Technology")
    if not args.size:
        args.size = Prompt.ask(
            "[bold]Organisation size[/bold]",
            default="mid-size",
            choices=["startup", "mid-size", "enterprise"],
        )
    if not args.tenant:
        safe = args.org.lower().replace(" ", "_").replace(".", "")[:20]
        args.tenant = Prompt.ask("[bold]Tenant ID[/bold] (namespace for audit logs)", default=safe)
    if not args.output:
        default_out = f"./compliance_output/{args.tenant}"
        args.output = Prompt.ask("[bold]Output directory[/bold]", default=default_out)

    return args


def check_api_key(provider: str) -> None:
    """Warn if the expected API key env var is missing."""
    key_map = {
        "anthropic": "ANTHROPIC_API_KEY",
        "openai":    "OPENAI_API_KEY",
        "google":    "GOOGLE_API_KEY",
    }
    env_var = key_map.get(provider, "API_KEY")
    if not os.environ.get(env_var):
        console.print(
            f"\n[yellow]⚠  {env_var} is not set.[/yellow]\n"
            f"   Export it before running:  export {env_var}=your-key-here\n"
        )
        sys.exit(1)


def run_agent(args: argparse.Namespace) -> None:
    """Load the YAML, build context, and execute the agent."""
    # Late imports so errors surface cleanly
    from zak.core.dsl.parser import load_agent_yaml, validate_agent
    from zak.core.runtime.agent import AgentContext
    from zak.core.runtime.registry import AgentRegistry

    # Import the agent + tools so they self-register
    import zak.agents.compliance.iso27001_soc2_agent   # noqa: F401
    import zak.agents.compliance.compliance_tools       # noqa: F401

    yaml_path = Path(args.yaml)
    if not yaml_path.exists():
        console.print(f"[red]✗  Agent YAML not found: {yaml_path}[/red]")
        sys.exit(1)

    # ── Parse and validate YAML ────────────────────────────────────────────
    console.print(f"\n[dim]▶  Validating [cyan]{yaml_path}[/cyan]...[/dim]")
    validation = validate_agent(str(yaml_path))
    if not validation.valid:
        console.print(f"[red]✗  Invalid YAML: {validation.errors}[/red]")
        sys.exit(1)
    console.print("[green]✅ YAML is valid[/green]")
    dsl = load_agent_yaml(str(yaml_path))

    if args.dry_run:
        console.print("\n[dim]Dry-run complete — agent not executed.[/dim]")
        return

    # ── Patch the DSL with the chosen LLM provider/model ──────────────────
    if args.model and hasattr(dsl, "reasoning") and dsl.reasoning and dsl.reasoning.llm:
        dsl.reasoning.llm.model = args.model  # type: ignore[union-attr]
    if args.provider and hasattr(dsl, "reasoning") and dsl.reasoning and dsl.reasoning.llm:
        dsl.reasoning.llm.provider = args.provider  # type: ignore[union-attr]

    # ── Prepare output directory ───────────────────────────────────────────
    out_dir = str(Path(args.output).resolve())
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    # ── Print run summary ──────────────────────────────────────────────────
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Key",   style="dim")
    table.add_column("Value", style="bold white")
    table.add_row("Organisation", args.org)
    table.add_row("Industry",     args.industry)
    table.add_row("Size",         args.size)
    table.add_row("Tenant",       args.tenant)
    table.add_row("LLM Provider", args.provider)
    table.add_row("Frameworks",   "ISO/IEC 27001:2022 + SOC 2 TSC")
    table.add_row("Output",       out_dir)
    console.print(Panel(table, title="[bold]Run Configuration[/bold]", border_style="cyan"))
    console.print()

    # ── Build context ──────────────────────────────────────────────────────
    import uuid
    context = AgentContext(
        tenant_id=args.tenant,
        trace_id=str(uuid.uuid4()),
        dsl=dsl,
        environment="production",
        metadata={
            "org_name":   args.org,
            "industry":   args.industry,
            "org_size":   args.size,
            "output_dir": out_dir,
            "today":      date.today().isoformat(),
        },
    )

    # ── Resolve and run the agent ──────────────────────────────────────────
    registry = AgentRegistry.get()
    agent_cls = None
    for reg in registry.all_registrations_unfiltered():
        if reg.class_name == "ISO27001SOC2Agent":
            agent_cls = reg.agent_class
            break
    if agent_cls is None:
        console.print("[red]✗  Could not find ISO27001SOC2Agent in the registry.[/red]")
        sys.exit(1)

    agent = agent_cls()

    console.print("[bold cyan]▶  Running compliance agent…[/bold cyan]")
    console.print("[dim]   This will take a few minutes — the agent generates full policy documents.[/dim]\n")

    agent.pre_run(context)
    result = agent.execute(context)
    agent.post_run(context, result)

    # ── Results ────────────────────────────────────────────────────────────
    if result.success:
        console.print("\n[bold green]✅ Compliance run complete![/bold green]\n")

        # List output files
        from pathlib import Path as P
        out_files = sorted(P(out_dir).glob("*.md"))
        if out_files:
            file_table = Table(title="Generated Files", show_header=True)
            file_table.add_column("File", style="cyan")
            file_table.add_column("Size")
            for f in out_files:
                size = f"{f.stat().st_size / 1024:.1f} KB"
                file_table.add_row(f.name, size)
            console.print(file_table)
            console.print(f"\n[dim]All files saved to:[/dim] [bold]{out_dir}[/bold]\n")
        else:
            console.print(f"[dim]Output directory:[/dim] [bold]{out_dir}[/bold]")

        # Print summary from agent
        summary = result.output.get("summary", "")
        if summary:
            console.print(Panel(
                summary[:2000] + ("…" if len(summary) > 2000 else ""),
                title="[bold]Agent Summary[/bold]",
                border_style="green",
            ))
    else:
        console.print("\n[bold red]✗  Agent run failed:[/bold red]")
        for err in result.errors:
            console.print(f"  [red]• {err}[/red]")
        sys.exit(1)


def main() -> None:
    args = parse_args()
    args = prompt_if_missing(args)

    if not args.dry_run:
        check_api_key(args.provider)

    run_agent(args)


if __name__ == "__main__":
    main()
