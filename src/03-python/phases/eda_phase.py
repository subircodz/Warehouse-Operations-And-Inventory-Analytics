"""
EDA Phase

This module orchestrates EDA
and presents the analysis results.

Author: Subir Sutradhar
"""

from rich.console import Console
from rich.table import Table

from analysis.inventory_analysis import (
    analyze_inventory
)


console = Console()


def eda_phase(workbook):

    # ==========================================================
    # Run Inventory Analysis
    # ==========================================================

    inventory_result = analyze_inventory(
        workbook
    )

    # ==========================================================
    # EDA Header
    # ==========================================================

    console.print(
        "[white]=[/]" * 60
    )

    console.print(
        "[bright_blue]ℹ️  Inventory EDA[/]"
    )

    console.print(
        "[white]=[/]" * 60
    )

    # ==========================================================
    # Summary
    # ==========================================================

    summary = inventory_result.summary

    console.print(
        f"[cyan]Total Inventory Quantity[/] : "
        f"{summary['total_quantity']:,}"
    )

    console.print(
        f"[cyan]Total Monetary Value[/]     : "
        f"Rs. {summary['total_monetary_value']:,.2f}"
    )

    console.print()

    # ==========================================================
    # Inventory Distribution by Warehouse
    # ==========================================================

    distribution_table = Table(
        title="Inventory Distribution by Warehouse"
    )

    distribution_table.add_column(
        "Warehouse ID"
    )

    distribution_table.add_column(
        "Warehouse"
    )

    distribution_table.add_column(
        "State"
    )

    distribution_table.add_column(
        "Quantity",
        justify="right"
    )

    for row in (
        inventory_result
        .data[
            "inventory_distribution"
        ]
        .itertuples(index=False)
    ):

        warehouse_name = (
            "UNMAPPED"
            if row.warehouse_name != row.warehouse_name
            else str(row.warehouse_name)
        )

        state = (
            "UNMAPPED"
            if row.state != row.state
            else str(row.state)
        )

        distribution_table.add_row(
            str(row.warehouse_id),
            warehouse_name,
            state,
            f"{row.quantity:,}"
        )

    console.print(
        distribution_table
    )

    console.print()

    # ==========================================================
    # Inventory Value by Warehouse
    # ==========================================================

    warehouse_value_table = Table(
        title="Inventory Value by Warehouse"
    )

    warehouse_value_table.add_column(
        "Warehouse ID"
    )

    warehouse_value_table.add_column(
        "Warehouse"
    )

    warehouse_value_table.add_column(
        "Inventory Value",
        justify="right"
    )

    for row in (
        inventory_result
        .data[
            "inventory_value_by_warehouse"
        ]
        .itertuples(index=False)
    ):

        warehouse_name = (
            "UNMAPPED"
            if row.warehouse_name != row.warehouse_name
            else str(row.warehouse_name)
        )

        warehouse_value_table.add_row(
            str(row.warehouse_id),
            warehouse_name,
            f"Rs. {row.inventory_value:,.2f}"
        )

    console.print(
        warehouse_value_table
    )

    console.print()

    # ==========================================================
    # Top Products by Inventory Value
    # ==========================================================

    top_products_table = Table(
        title="Top Products by Inventory Value"
    )

    top_products_table.add_column(
        "Product ID"
    )

    top_products_table.add_column(
        "Product"
    )

    top_products_table.add_column(
        "Brand"
    )

    top_products_table.add_column(
        "Status"
    )

    top_products_table.add_column(
        "Inventory Value",
        justify="right"
    )

    for row in (
        inventory_result
        .data[
            "inventory_value_by_product"
        ]
        .head(10)
        .itertuples(index=False)
    ):

        top_products_table.add_row(
            str(row.product_id),
            str(row.product_name),
            str(row.brand),
            str(row.status),
            f"Rs. {row.inventory_value:,.2f}"
        )

    console.print(
        top_products_table
    )

    console.print()

    # ==========================================================
    # Finding:
    # Inactive Products Holding Inventory
    # ==========================================================

    inactive_products = (
        inventory_result
        .data[
            "inactive_products"
        ]
    )

    if not inactive_products.empty:

        inactive_table = Table(
            title="Inactive Products Holding Inventory"
        )

        inactive_table.add_column(
            "Product ID"
        )

        inactive_table.add_column(
            "Product"
        )

        inactive_table.add_column(
            "Brand"
        )

        inactive_table.add_column(
            "Inventory Value",
            justify="right"
        )

        for row in (
            inactive_products
            .head(10)
            .itertuples(index=False)
        ):

            inactive_table.add_row(
                str(row.product_id),
                str(row.product_name),
                str(row.brand),
                f"Rs. {row.inventory_value:,.2f}"
            )

        console.print(
            inactive_table
        )

        console.print(
            "[yellow] Finding:[/] "
            "Inactive products are still holding inventory."
        )

    else:

        console.print(
            "[green]✔ Finding:[/] "
            "No inactive products are holding inventory."
        )

    console.print(
        "[white]=[/]" * 60
    )

    return inventory_result