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