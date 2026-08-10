"""
Product Analysis Module

Analyzes product catalogue size, product status,
and product price characteristics.

Author: Subir Sutradhar
"""

from pandas import DataFrame

from models.validation_result import WaveResult


def analyze_product(
    workbook: dict[str, DataFrame]
) -> WaveResult:
    """
    Analyze the products worksheet.

    Args:
        workbook: Dictionary containing worksheet names
        and pandas DataFrames.

    Returns:
        WaveResult containing product analysis results.
    """

    df_products = workbook["products"]
    df_inventory = workbook["inventory"]

    # ==========================================================
    # Product Count
    # ==========================================================

    total_products = len(df_products)

    # ==========================================================
    # Product Status
    # ==========================================================

    df_products_active = df_products.loc[
        df_products["status"] == "ACTIVE"
    ]

    df_products_inactive = df_products.loc[
        df_products["status"] == "INACTIVE"
    ]

    active_products = len(df_products_active)
    inactive_products = len(df_products_inactive)

    # ==========================================================
    # Product Price Analysis
    # ==========================================================

    minimum_price = df_products["unit_price"].min()
    maximum_price = df_products["unit_price"].max()
    average_price = df_products["unit_price"].mean()
    median_price = df_products["unit_price"].median()
    price_std = df_products["unit_price"].std()

    price_range = maximum_price - minimum_price

    # ==========================================================
    # Extreme Price Observations
    # ==========================================================

    minimum_price_count = df_products.loc[
        df_products["unit_price"] == minimum_price
    ].shape[0]

    maximum_price_count = df_products.loc[
        df_products["unit_price"] == maximum_price
    ].shape[0]

    # ==========================================================
    # Weighted Average Cost by Product
    # ==========================================================

    df_inventory["inventory_cost_value"] = (
        df_inventory["unit_cost"] * df_inventory["quantity"]
    )

    weighted_cost_by_product = (
        df_inventory
        .groupby("product_id", as_index=False)
        .agg(
            total_quantity=("quantity", "sum"),
            total_inventory_cost=("inventory_cost_value", "sum")
        )
    )

    weighted_cost_by_product["weighted_average_cost"] = (
        weighted_cost_by_product["total_inventory_cost"]
        / weighted_cost_by_product["total_quantity"]
    )

    products_with_cost = df_products.merge(
    weighted_cost_by_product[
        [
            "product_id",
            "weighted_average_cost"
        ]
    ],
    on="product_id",
    how="left"
    )

    products_with_cost["estimated_margin"] = (
    products_with_cost["unit_price"]
    - products_with_cost["weighted_average_cost"]
    )


    products_with_cost["estimated_margin_percentage"] = (
    products_with_cost["estimated_margin"]
    / products_with_cost["unit_price"]
    ) * 100

    orphaned_products = products_with_cost.loc[
    products_with_cost["weighted_average_cost"].isna()]

    orphaned_product_count = len(orphaned_products)

    products_in_catalogue = len(df_products)

    products_with_inventory_cost = (
        products_in_catalogue - orphaned_product_count
    )

    products_without_inventory_cost = orphaned_product_count

    negative_margin_products = products_with_cost.loc[
    products_with_cost["estimated_margin"] < 0
    ]
    negative_amount = negative_margin_products["estimated_margin"].sum()

    positive_margin_products = products_with_cost.loc[
        products_with_cost["estimated_margin"] > 0
        ]
    positive_amount = positive_margin_products["estimated_margin"].sum()

    zero_margin_products = products_with_cost.loc[
    products_with_cost["estimated_margin"] == 0
    ]

    negative_margin_items = (
    products_with_cost.loc[products_with_cost["estimated_margin"] < 0]
        .sort_values(
            by="estimated_margin"
        ).reset_index()
    )
    negative_margin_products = products_with_cost.loc[
        products_with_cost["estimated_margin"] < 0
    ]

    negative_active = negative_margin_products.loc[
        negative_margin_products["status"] == "ACTIVE"
    ]

    negative_inactive = negative_margin_products.loc[
        negative_margin_products["status"] == "INACTIVE"
    ]

    # TODO
    # Future Product Analysis
    # -----------------------

    # 1. Investigate active products with negative estimated margins.
    # 2. Investigate the ₹999,999 extreme price observation.
    # 3. Investigate products with ₹0 selling price.
    # 4. Analyse margin by brand.
    # 5. Analyse margin by product category.
    # 6. Analyse inventory exposure of inactive products.
    # 7. Investigate the 64 products without inventory records.
    # 8. Add visual analysis in the reporting/dashboard phase.

    # ==========================================================
    # Findings
    # ==========================================================

    findings = []

    if maximum_price > 2500:
        findings.append(
            "Product catalogue contains an extreme high-price observation "
            f"of Rs. {maximum_price:,.2f}."
        )

    if average_price > median_price:
        findings.append(
            "Average product price is higher than the median, "
            "indicating a right-skewed price distribution."
        )

    if price_std > average_price:
        findings.append(
            "Product price standard deviation is substantially higher "
            "than the average product price, indicating high price variation."
        )

    if orphaned_product_count > 0:
        finding = (
            f"{orphaned_product_count} products in the product master "
            "have no corresponding inventory records, so estimated "
            "margin cannot be calculated for these products."
        )
    findings.append(
        f"Products in catalogue          : {products_in_catalogue:,}"
    )
    findings.append(
        f"Products with inventory cost   : {products_with_inventory_cost:,}"
    )
    findings.append(
        f"Products without inventory cost: {products_without_inventory_cost:,}"
    )

    findings.append(finding)
    findings.append(
        f"Products with negative margin  : {len(negative_margin_products)} ( Rs. {negative_amount:,.2f} )"
    )
    findings.append(
            f"Products with positive margin  : {len(positive_margin_products)} ( Rs. {positive_amount:,.2f} )"
        )
    findings.append(
            f"Products with zero margin  : {len(zero_margin_products)}"
        )
    findings.append(
        f"Active products with negative margin: {len(negative_active)}"
    )
    findings.append(
            f"Inactive products with negative margin: {len(negative_inactive)}"
        )
    findings.append(
                f"Negative estimated margins are not limited to inactive products. {len(negative_active)} active products are currently showing negative estimated margins based on the weighted average inventory cost which requires pricing and inventory cost review"
            )
    findings.append(
            f"Investigation is required to understand why {len(negative_inactive)} inactive products have negative estimated margins"
        )
    # ==========================================================
    # Return Analysis Result
    # ==========================================================

    return WaveResult(
        validation_name="Product Analysis",
        status="COMPLETED",
        data={
            "total_products": total_products,
            "active_products": active_products,
            "inactive_products": inactive_products,
            "price_analysis": {
                "minimum_price": minimum_price,
                "maximum_price": maximum_price,
                "average_price": average_price,
                "median_price": median_price,
                "price_range": price_range,
                "standard_deviation": price_std,
            },
            "extreme_prices": {
                "minimum_price_count": minimum_price_count,
                "maximum_price_count": maximum_price_count,
            },
            "findings": findings,
        },
        summary={
            "total_products": total_products,
            "active_products": active_products,
            "inactive_products": inactive_products,
        },
    )