"""
Numeric Range Cleaning

This module cleans numeric values that fall
outside the configured business range.

Author: Subir Sutradhar
"""

from pandas import DataFrame

from config import NUMERIC_RANGE_RULES
from models.validation_result import WaveResult


def clean_range(
    workbook: dict[str, DataFrame]
) -> WaveResult:
    """
    Cleans numeric values that violate the
    configured minimum value.

    Args:
        workbook: Dictionary containing worksheet
        names and pandas DataFrame.

    Returns:
        WaveResult
    """

    overall_result = {}
    worksheets_modified = 0
    columns_modified = 0
    values_corrected = 0
    for worksheet, dataframe in workbook.items():
        worksheet_result = {}
        for column in dataframe.columns:
            if column not in NUMERIC_RANGE_RULES:
                continue
            minimum_value = NUMERIC_RANGE_RULES[column]["min"]
            replacement_value = NUMERIC_RANGE_RULES[column]["replacement"]
            mask = dataframe[column] < minimum_value
            corrected_count = int(mask.sum())
            if corrected_count == 0:
                continue
            dataframe.loc[mask, column] = replacement_value
            worksheet_result[column] = corrected_count
            columns_modified += 1
            values_corrected += corrected_count

        if worksheet_result:
            overall_result[worksheet] = worksheet_result
            worksheets_modified += 1

    return WaveResult(
        validation_name="Numeric Range Cleaning",
        status="COMPLETED",
        data=overall_result,
        summary={
            "worksheets_modified": worksheets_modified,
            "columns_modified": columns_modified,
            "values_corrected": values_corrected
        }
    )