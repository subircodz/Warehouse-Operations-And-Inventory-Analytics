"""
Inventory Analysis Module

This module performs exploratory data analysis
on the inventory worksheet.

Author: Subir Sutradhar
"""

from pandas import DataFrame

from models.validation_result import WaveResult


def analyze_inventory(
    workbook: dict[str, DataFrame]
) -> WaveResult:
    """
    Performs exploratory analysis on the inventory
    worksheet.

    Args:
        workbook:
            Dictionary containing worksheet names
            and pandas DataFrames.

    Returns:
        WaveResult:
            Inventory analysis results.
    """

    inventory = workbook["inventory"]

    # ==========================================================
    # Q1: How much inventory do we have?
    # ==========================================================

    total_quantity = inventory["quantity"].sum()

    # ==========================================================
    # Q2: How is inventory distributed across warehouses?
    # ==========================================================

    inventory_distribution = (
        inventory
        .groupby(
            "warehouse_id",
            as_index=False
        )["quantity"]
        .sum()
    )

    inventory_distribution = (
        inventory_distribution.merge(
            workbook["warehouses"][
                [
                    "warehouse_id",
                    "warehouse_name",
                    "state"
                ]
            ],
            on="warehouse_id",
            how="left"
        )
    )

    # ==========================================================
    # Q3: What is the monetary value of the inventory?
    # ==========================================================

    inventory_value = (
        inventory["quantity"] *
        inventory["unit_cost"]
    )

    total_monetary_value = inventory_value.sum()

    # ==========================================================
    # Q4: What is the inventory value by warehouse?
    # ==========================================================

    inventory_value_by_warehouse = (
        inventory
        .assign(
            inventory_value=inventory_value
        )
        .groupby(
            "warehouse_id",
            as_index=False
        )["inventory_value"]
        .sum()
    )

    inventory_value_by_warehouse = (
        inventory_value_by_warehouse.merge(
            workbook["warehouses"][
                [
                    "warehouse_id",
                    "warehouse_name"
                ]
            ],
            on="warehouse_id",
            how="left"
        )
    )

    # ==========================================================
    # Q5: Which products contribute most to inventory value?
    # ==========================================================

    inventory_value_by_product = (
        inventory
        .assign(
            inventory_value=inventory_value
        )
        .groupby(
            "product_id",
            as_index=False
        )["inventory_value"]
        .sum()
        .sort_values(
            by="inventory_value",
            ascending=False
        )
    )

    inventory_value_by_product = (
        inventory_value_by_product.merge(
            workbook["products"][
                [
                    "product_id",
                    "product_name",
                    "brand",
                    "status"
                ]
            ],
            on="product_id",
            how="left"
        )
    )

    # ==========================================================
    # Q6: Are inactive products still holding inventory?
    # ==========================================================

    inactive_products = (
        inventory_value_by_product[
            inventory_value_by_product["status"] == "INACTIVE"
        ]
        .sort_values(
            by="inventory_value",
            ascending=False
        )
    )

    # ==========================================================
    # Return analysis results
    # ==========================================================

    return WaveResult(
        validation_name="Inventory EDA",
        status="COMPLETED",
        data={
            "inventory_distribution": (
                inventory_distribution
            ),
            "inventory_value_by_warehouse": (
                inventory_value_by_warehouse
            ),
            "inventory_value_by_product": (
                inventory_value_by_product
            ),
            "inactive_products": (
                inactive_products
            ),
        },
        summary={
            "total_quantity": int(
                total_quantity
            ),
            "total_monetary_value": float(
                total_monetary_value
            ),
        }
    )