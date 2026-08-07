"""
Data Cleaning Phase

This module dispatches the workbook to all
cleaning modules, collects their results and
returns the overall cleaning result.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from rich.console import Console

from cleaning import (
    fill_missing_values,
    clean_duplicates
)

console = Console()


def cleaning_phase(
    workbook: dict[str, DataFrame]
) -> list:

    cleaning_results = []

    # ==========================================================
    # Missing Value Cleaning
    # ==========================================================

    console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Missing Value Cleaning[/]")
    console.print("[white]=[/]" * 60)

    missing_value_result = fill_missing_values(workbook)

    cleaning_results.append(missing_value_result)

    for worksheet, data in missing_value_result.data.items():

        console.print(f"[cyan]► Worksheet : {worksheet}[/]")
        console.print("[white]-[/]" * 60)

        for column, result in data.items():

            console.print(
                f"    ✔ {column:<25} : "
                f"{result['action']} ({result['updated']})"
            )

        console.print("[white]=[/]" * 60)

    console.print("[bright_blue]ℹ️  Missing Value Cleaning Summary[/]")
    console.print("[white]-[/]" * 60)

    summary = missing_value_result.summary

    console.print(
        f"{'Worksheets Modified':<25}: "
        f"{summary['worksheets_modified']}"
    )

    console.print(
        f"{'Columns Modified':<25}: "
        f"{summary['columns_modified']}"
    )

    console.print(
        f"{'Cells Updated':<25}: "
        f"{summary['cells_updated']}"
    )

    console.print(
        f"{'Strategy Applied':<25}: "
        f"{summary['strategy']}"
    )

    console.print("[white]=[/]" * 60)
    console.print("[green]✅ Missing Value Cleaning Completed.[/]\n")

    return cleaning_results