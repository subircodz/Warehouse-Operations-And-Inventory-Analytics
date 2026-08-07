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
    clean_duplicates,
    clean_text,
    clean_range
)

console = Console()


def cleaning_phase(workbook: dict[str, DataFrame]) -> list:

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

    # ==========================================================
    # Clean duplicates.
    # ==========================================================

    console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Duplicate Cleaning[/]")
    console.print("[white]=[/]" * 60)
    duplicates_result = clean_duplicates(workbook)
    summary = duplicates_result.summary
    if summary["duplicates_removed"] == 0:
        console.print("[yellow]No duplicate records found.[/]")
        console.print("[white]-[/]" * 60)
    else:
        for worksheet, count in duplicates_result.data.items():
            console.print(f"[cyan]► Worksheet : {worksheet}[/]")
            console.print("[white]-[/]" * 60)
            console.print(f"{'Duplicates Removed':<25}: {count}")
    console.print("[bright_blue]ℹ️  Duplicates Cleaning Summary[/]")
    console.print("[white]-[/]" * 60)
    console.print(
            f"{'Worksheets Modified':<25}: "
            f"{summary['worksheets_modified']}"
        )
    console.print(
            f"{'Duplicates removed':<25}: "
            f"{summary['duplicates_removed']}"
        )
    console.print("[white]=[/]" * 60)
    console.print("[green]✅ Duplicates Cleaning Completed.[/]\n")

    # ==========================================================
    # Text Standardization
    # ==========================================================

    console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Text Standardization[/]")
    console.print("[white]=[/]" * 60)
    clean_text_result = clean_text(workbook)
    summary = clean_text_result.summary
    if not clean_text_result.data:
        console.print("[yellow]No text standardization required.[/]")
        console.print("[white]-[/]" * 60)
    else:
        for worksheet, worksheet_result in clean_text_result.data.items():
            console.print(f"[cyan]► Worksheet : {worksheet}[/]")
            console.print("[white]-[/]" * 60)
            for column, action in worksheet_result.items():
                console.print(
                    f"    ✔ {column:<25} : {action}"
                )
            console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Text Standardization Summary[/]")
    console.print("[white]-[/]" * 60)
    console.print(
        f"{'Worksheets Modified':<25}: "
        f"{summary['worksheets_modified']}"
    )
    console.print(
        f"{'Columns Modified':<25}: "
        f"{summary['columns_modified']}"
    )
    console.print("[white]=[/]" * 60)
    console.print("[green]✅ Text Standardization Completed.[/]\n")

    # ==========================================================
    # Numeric Range Cleaning
    # ==========================================================
    console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Numeric Range Cleaning[/]")
    console.print("[white]=[/]" * 60)
    clean_numeric_range = clean_range(workbook)
    for worksheet, result in clean_numeric_range.data.items():
        console.print(f"[cyan]► Worksheet : {worksheet}[/]")
        console.print("[white]-[/]" * 60)
        for column, data in result.items():
            console.print(
                 f"    ✔ {column:<25} : {data}"
            )
        console.print("[white]=[/]" * 60)
    summary = clean_numeric_range.summary
    console.print("[bright_blue]ℹ️  Numeric Range Cleaning Summary[/]")
    console.print("[white]-[/]" * 60)
    console.print(
        f"{'Worksheets Modified':<25}: "
        f"{summary['worksheets_modified']}"
    )
    console.print(
        f"{'Columns Modified':<25}: "
        f"{summary['columns_modified']}"
    )
    console.print(
            f"{'Values Corrected':<25}: "
            f"{summary['values_corrected']}"
        )
    console.print("[white]=[/]" * 60)
    console.print("[green]✅ Numeric Range Cleaning Completed.[/]\n")
            


    return cleaning_results