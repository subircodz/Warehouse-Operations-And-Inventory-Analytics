"""
Data Validation Phase

This module performs all data validation activities.
It dispatches the workbook to the required validation
modules, collects their results, displays the validation
report on the console, and returns the overall validation
results to the application.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from rich.console import Console
from rich.table import Table

from validators import (
    validate_referential_identifier,
    validate_business_identifier,
    extract_referential_exceptions
)

console = Console()


def validation_phase(
    workbook: dict[str, DataFrame]
) -> list:
    """
    Executes the complete data validation phase.

    This function dispatches the workbook to every
    validation module, collects their results,
    displays validation reports on the console,
    and returns the overall validation results.

    Args:
        workbook:
            Dictionary containing worksheet names
            and their corresponding pandas DataFrames.

    Returns:
        list:
            List containing validation results
            returned by each validation module.
    """

    validation_results: list = []

    # ==========================================================
    # Referential Integrity Validation
    # ==========================================================

    console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Referential Integrity Validation[/]")
    console.print("[white]=[/]" * 60)

    referential_result = validate_referential_identifier(workbook)

    validation_results.append(referential_result)

    passed = 0
    failed = 0

    for relationship, result in referential_result.data.items():

        status = "PASS" if result["invalid"] == 0 else "FAIL"

        if status == "PASS":
            passed += 1
        else:
            failed += 1

        console.print(f"[cyan]► {relationship}[/]")
        console.print("[white]-[/]" * 60)

        console.print(
            f"{'Overall Records Checked':<28}: "
            f"{result['overall_validation']:,}"
        )

        console.print(
            f"{'Valid References':<28}: "
            f"{result['valid']:,}"
        )

        console.print(
            f"{'Invalid References':<28}: "
            f"{result['invalid']:,}"
        )
        if status == "PASS":
            console.print(
                f"{'Status':<28}: "
                f"[green]{status}[/]"
            )
        else:
            console.print(
                f"{'Status':<28}: "
                f"[red]{status}[/]"
            )

        if result["invalid"] > 0:
            console.print()
            console.print("[yellow]Invalid Rows[/]")
            console.print(", ".join(map(str, result["invalid_row_list"])))

        console.print("[white]-[/]" * 60)

    console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Referential Integrity Summary[/]")
    console.print("[white]-[/]" * 60)

    console.print(f"{'Relationships Checked':<28}: {passed + failed}")
    console.print(f"{'Passed':<28}: {passed}")
    console.print(f"{'Failed':<28}: {failed}")

    console.print("[white]=[/]" * 60)
    console.print("[green]✅ Referential Integrity Validation Completed.[/]\n")

    # ==========================================================
    # Extract invalid rows
    # ==========================================================
    extract_referential_rows_result = extract_referential_exceptions(workbook, referential_result)
    table = Table(title="Referential Integrity Exceptions")

    for column in extract_referential_rows_result.columns:
        table.add_column(column)

    for row in extract_referential_rows_result.itertuples(index=False):
        table.add_row(*[str(value) for value in row])

    console.print(table)

    # ==========================================================
    # Business Identifier Validation
    # ==========================================================

    console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Business Identifier Validation[/]")
    console.print("[white]=[/]" * 60)
    business_identifier_result = validate_business_identifier(workbook)
    validation_results.append(business_identifier_result)
    worksheet_count = 0
    for worksheet, result in business_identifier_result.data.items():
        worksheet_count+=1
        console.print(f"[cyan]► {worksheet}[/]")
        console.print("[white]-[/]" * 60)
        for status, counts in result.items():
            console.print(
                            f"    ✔ {status:<25} : "
                            f"{counts}"
                        )
    console.print("[white]=[/]" * 60)
    console.print("[bright_blue]ℹ️  Business Identifier Validation Summary[/]")
    console.print("[white]-[/]" * 60)

    console.print(f"{'Worksheets validated':<28}: {worksheet_count}")


    console.print("[white]=[/]" * 60)
    console.print("[green]✅ Business Identifier Validation Completed.[/]\n")

    return validation_results