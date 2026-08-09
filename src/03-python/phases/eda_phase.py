"""
EDA Phase

This module orchestrates EDA
and presents the analysis results.

Author: Subir Sutradhar
"""

from rich.console import Console
from rich.table import Table

from analysis import (
    analyze_inventory,
    analyze_product
)


console = Console()


def eda_phase(workbook):
    result = []

    # ==========================================================
    # Run Inventory Analysis
    # ==========================================================

    inventory_result = analyze_inventory(
        workbook
    )

    result.append(inventory_result)

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


    # =======================================================
    # Product analyze header
    # =======================================================

    console.print(
        "[white]=[/]" * 60
    )
    console.print(
        "[bright_blue]ℹ️  Product EDA[/]"
    )
    console.print(
        "[white]=[/]" * 60
    )
    product_result = analyze_product(workbook)
    result.append(product_result)
    product_catalogue_table = Table(
        title="Product Catalogue Summary",
        border_style="blue"
    )
    product_catalogue_table.add_column("Metric")
    product_catalogue_table.add_column("Value")
    product_catalogue_table.add_row(
        "Total Products",
        f"{product_result.data["total_products"]}"
    )
    product_catalogue_table.add_row(
            "Active Products",
            f"{product_result.data["active_products"]}"
        )
    product_catalogue_table.add_row(
                "Inactive Products",
                f"{product_result.data["inactive_products"]}"
            )
    console.print(product_catalogue_table)

    # ===============================================
    # Product Price Analysis
    # ===============================================

    product_price_analysis = Table(
            title="Product Price Analysis",
            border_style="blue"
        )
    product_price_analysis.add_column("Metric")
    product_price_analysis.add_column("Value")
    product_price_analysis.add_row(
        "Minimum Price",
        f"Rs. {(product_result.data["price_analysis"]["minimum_price"]):,.2f}"
    )
    product_price_analysis.add_row(
            "Maximum Price",
            f"Rs. {(product_result.data["price_analysis"]["maximum_price"]):,.2f}"
        )
    product_price_analysis.add_row(
            "Average Price",
            f"Rs. {(product_result.data["price_analysis"]["average_price"]):,.2f}"
        )
    product_price_analysis.add_row(
            "Median Price",
            f"Rs. {(product_result.data["price_analysis"]["median_price"]):,.2f}"
        )
    product_price_analysis.add_row(
            "Price Range",
            f"Rs. {(product_result.data["price_analysis"]["price_range"]):,.2f}"
        )
    product_price_analysis.add_row(
        "Standard Deviation",
        f"Rs. {(product_result.data["price_analysis"]["standard_deviation"]):,.2f}"
    )
 
    console.print(product_price_analysis)

    # ============================================
    # Extreme Price
    # ============================================

    extreme_price_analysis = Table(
        title="Extreme Price Observations",
        border_style="blue"
    )
    extreme_price_analysis.add_column("Metric")
    extreme_price_analysis.add_column("Count")
    extreme_price_analysis.add_row(
        "Minimum Price (Rs. 0)",
        str(product_result.data["extreme_prices"]["minimum_price_count"])
    )
    extreme_price_analysis.add_row(
            "Maximum Price",
            str(product_result.data["extreme_prices"]["maximum_price_count"])
        )
    console.print(extreme_price_analysis)

    # ============================================
    # Findings
    # ============================================

    console.print("[underline yellow]Findings[/]")
    console.print()
    findings = product_result.data["findings"]
    for idx, finding in enumerate(findings, start=1):
        console.print(f"    {idx}. {finding}")
    console.print()
    return result