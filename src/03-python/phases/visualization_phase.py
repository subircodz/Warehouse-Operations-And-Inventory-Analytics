"""
Phase 10 — Visualization

Generates business-focused Matplotlib charts from the validated workbook.

Author: Subir Sutradhar
"""

from pathlib import Path

from rich.console import Console

from config import OUTPUT_DIRECTORY
from visualization import generate_visualizations


console = Console()


def visualization_phase(workbook: dict) -> list[str]:
    """Run Phase 10 and return the generated chart paths."""
    output_directory = OUTPUT_DIRECTORY / "visualizations"

    console.print("[white]=" * 60)
    console.print("[bright_blue]📊  Phase 10 — Matplotlib Visualizations[/]")
    console.print("[white]=" * 60)

    chart_paths = generate_visualizations(
        workbook,
        Path(output_directory),
    )

    for chart_path in chart_paths:
        console.print(f"[green]✔ Generated:[/] {chart_path}")

    console.print(f"[green]✔ Phase 10 completed:[/] {len(chart_paths)} visualizations generated.")
    console.print("[white]=" * 60)

    return chart_paths
