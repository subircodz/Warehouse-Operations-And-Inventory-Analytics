"""
Missing Value Cleaning Module

This module replaces missing values in object
columns with 'UNKNOWN'. Numeric and datetime
columns are intentionally left unchanged for
manual business review.

Author: Subir Sutradhar
"""

from pandas import DataFrame

from models.validation_result import WaveResult


def fill_missing_values(
    workbook: dict[str, DataFrame]
) -> WaveResult:
    """
    Replaces missing values in object columns
    with 'UNKNOWN'.

    Numeric and datetime columns are skipped
    intentionally.

    Args:
        workbook:
            Dictionary containing worksheet names
            and pandas DataFrames.

    Returns:
        WaveResult
    """

    overall_result = {}

    worksheets_modified = 0
    columns_modified = 0
    cells_updated = 0

    for worksheet, dataframe in workbook.items():

        worksheet_result = {}

        for column in dataframe.columns:

            total_missing = int(dataframe[column].isna().sum())

            if total_missing == 0:
                continue

            if dataframe[column].dtype == "object":

                dataframe[column] = dataframe[column].fillna("UNKNOWN")

                worksheet_result[column] = {
                    "action": "Filled with UNKNOWN",
                    "updated": total_missing,
                }

                columns_modified += 1
                cells_updated += total_missing

        if worksheet_result:
            overall_result[worksheet] = worksheet_result
            worksheets_modified += 1

    return WaveResult(
        validation_name="Missing Value Cleaning",
        status="COMPLETED",
        data=overall_result,
        summary={
            "worksheets_modified": worksheets_modified,
            "columns_modified": columns_modified,
            "cells_updated": cells_updated,
            "strategy": "Filled object columns with UNKNOWN",
        },
    )