"""
Business visualizations for Warehouse Operations & Inventory Analytics.

The module deliberately uses Matplotlib directly so that every chart is
reproducible from the validated workbook without depending on a notebook.

Author: Subir Sutradhar
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd



def _save_figure(figure, output_path: Path) -> str:
    """Save a figure and release its Matplotlib resources."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.tight_layout()
    figure.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(figure)
    return str(output_path)



def _currency_axis(axis) -> None:
    """Format an axis with compact rupee-denominated values."""
    axis.ticklabel_format(axis="y", style="plain")
    axis.set_ylabel("Value (Rs.)")



def plot_inventory_quantity_by_warehouse(
    workbook: dict[str, pd.DataFrame],
    output_directory: Path,
) -> str:
    """Show total inventory quantity held by warehouse."""
    inventory = workbook["inventory"]
    warehouses = workbook["warehouses"]

    data = (
        inventory.groupby("warehouse_id", as_index=False)["quantity"]
        .sum()
        .merge(
            warehouses[["warehouse_id", "warehouse_name"]],
            on="warehouse_id",
            how="left",
        )
        .sort_values("quantity", ascending=False)
    )

    figure, axis = plt.subplots(figsize=(9, 5))
    axis.bar(data["warehouse_name"].fillna("Unmapped"), data["quantity"])
    axis.set_title("Inventory Quantity by Warehouse")
    axis.set_xlabel("Warehouse")
    axis.set_ylabel("Quantity")
    axis.tick_params(axis="x", rotation=25)

    for index, value in enumerate(data["quantity"]):
        axis.text(index, value, f"{value:,.0f}", ha="center", va="bottom")

    return _save_figure(
        figure,
        output_directory / "01_inventory_quantity_by_warehouse.png",
    )



def plot_inventory_value_by_warehouse(
    workbook: dict[str, pd.DataFrame],
    output_directory: Path,
) -> str:
    """Show monetary inventory exposure by warehouse."""
    inventory = workbook["inventory"].copy()
    warehouses = workbook["warehouses"]

    inventory["inventory_value"] = (
        inventory["quantity"] * inventory["unit_cost"]
    )

    data = (
        inventory.groupby("warehouse_id", as_index=False)["inventory_value"]
        .sum()
        .merge(
            warehouses[["warehouse_id", "warehouse_name"]],
            on="warehouse_id",
            how="left",
        )
        .sort_values("inventory_value", ascending=False)
    )

    figure, axis = plt.subplots(figsize=(9, 5))
    axis.bar(
        data["warehouse_name"].fillna("Unmapped"),
        data["inventory_value"],
    )
    axis.set_title("Inventory Value by Warehouse")
    axis.set_xlabel("Warehouse")
    axis.tick_params(axis="x", rotation=25)
    _currency_axis(axis)

    for index, value in enumerate(data["inventory_value"]):
        axis.text(index, value, f"Rs. {value:,.0f}", ha="center", va="bottom")

    return _save_figure(
        figure,
        output_directory / "02_inventory_value_by_warehouse.png",
    )



def plot_top_products_by_inventory_value(
    workbook: dict[str, pd.DataFrame],
    output_directory: Path,
    top_n: int = 10,
) -> str:
    """Show the products with the greatest inventory value exposure."""
    inventory = workbook["inventory"].copy()
    products = workbook["products"]

    inventory["inventory_value"] = (
        inventory["quantity"] * inventory["unit_cost"]
    )

    data = (
        inventory.groupby("product_id", as_index=False)["inventory_value"]
        .sum()
        .merge(
            products[["product_id", "product_name"]],
            on="product_id",
            how="left",
        )
        .sort_values("inventory_value", ascending=False)
        .head(top_n)
        .sort_values("inventory_value")
    )

    labels = data["product_name"].fillna(data["product_id"].astype(str))

    figure, axis = plt.subplots(figsize=(10, 6))
    axis.barh(labels, data["inventory_value"])
    axis.set_title(f"Top {top_n} Products by Inventory Value")
    axis.set_xlabel("Inventory Value (Rs.)")

    for index, value in enumerate(data["inventory_value"]):
        axis.text(value, index, f"  Rs. {value:,.0f}", va="center")

    return _save_figure(
        figure,
        output_directory / "03_top_products_by_inventory_value.png",
    )



def plot_inactive_inventory_exposure(
    workbook: dict[str, pd.DataFrame],
    output_directory: Path,
    top_n: int = 10,
) -> str:
    """Show inventory value tied to inactive products."""
    inventory = workbook["inventory"].copy()
    products = workbook["products"]

    inventory["inventory_value"] = (
        inventory["quantity"] * inventory["unit_cost"]
    )

    data = (
        inventory.groupby("product_id", as_index=False)["inventory_value"]
        .sum()
        .merge(
            products[["product_id", "product_name", "status"]],
            on="product_id",
            how="left",
        )
    )
    data = (
        data.loc[data["status"] == "INACTIVE"]
        .sort_values("inventory_value", ascending=False)
        .head(top_n)
        .sort_values("inventory_value")
    )

    figure, axis = plt.subplots(figsize=(10, 6))

    if data.empty:
        axis.text(0.5, 0.5, "No inactive products hold inventory", ha="center", va="center")
        axis.set_axis_off()
    else:
        labels = data["product_name"].fillna(data["product_id"].astype(str))
        axis.barh(labels, data["inventory_value"])
        axis.set_title(f"Top {top_n} Inactive Products by Inventory Value")
        axis.set_xlabel("Inventory Value (Rs.)")

        for index, value in enumerate(data["inventory_value"]):
            axis.text(value, index, f"  Rs. {value:,.0f}", va="center")

    return _save_figure(
        figure,
        output_directory / "04_inactive_inventory_exposure.png",
    )



def plot_product_price_distribution(
    workbook: dict[str, pd.DataFrame],
    output_directory: Path,
) -> str:
    """Show the distribution of product selling prices."""
    prices = workbook["products"]["unit_price"].dropna()

    figure, axis = plt.subplots(figsize=(9, 5))
    axis.hist(prices, bins=30)
    axis.set_title("Product Unit Price Distribution")
    axis.set_xlabel("Unit Price (Rs.)")
    axis.set_ylabel("Number of Products")

    return _save_figure(
        figure,
        output_directory / "05_product_price_distribution.png",
    )



def plot_estimated_margin_distribution(
    workbook: dict[str, pd.DataFrame],
    output_directory: Path,
) -> str:
    """Show estimated product margin after matching inventory cost."""
    inventory = workbook["inventory"].copy()
    products = workbook["products"]

    inventory["inventory_cost_value"] = (
        inventory["unit_cost"] * inventory["quantity"]
    )

    cost = (
        inventory.groupby("product_id", as_index=False)
        .agg(
            total_quantity=("quantity", "sum"),
            total_inventory_cost=("inventory_cost_value", "sum"),
        )
    )
    cost["weighted_average_cost"] = (
        cost["total_inventory_cost"] / cost["total_quantity"]
    )

    data = products.merge(
        cost[["product_id", "weighted_average_cost"]],
        on="product_id",
        how="left",
    )
    data["estimated_margin"] = (
        data["unit_price"] - data["weighted_average_cost"]
    )
    margins = data["estimated_margin"].dropna()

    figure, axis = plt.subplots(figsize=(9, 5))
    axis.hist(margins, bins=30)
    axis.axvline(0, linestyle="--", linewidth=1)
    axis.set_title("Estimated Product Margin Distribution")
    axis.set_xlabel("Estimated Margin (Rs. per unit)")
    axis.set_ylabel("Number of Products")

    return _save_figure(
        figure,
        output_directory / "06_estimated_margin_distribution.png",
    )



def generate_visualizations(
    workbook: dict[str, pd.DataFrame],
    output_directory: Path,
) -> list[str]:
    """Generate the complete Phase 10 Matplotlib visualization set."""
    output_directory.mkdir(parents=True, exist_ok=True)

    return [
        plot_inventory_quantity_by_warehouse(workbook, output_directory),
        plot_inventory_value_by_warehouse(workbook, output_directory),
        plot_top_products_by_inventory_value(workbook, output_directory),
        plot_inactive_inventory_exposure(workbook, output_directory),
        plot_product_price_distribution(workbook, output_directory),
        plot_estimated_margin_distribution(workbook, output_directory),
    ]
