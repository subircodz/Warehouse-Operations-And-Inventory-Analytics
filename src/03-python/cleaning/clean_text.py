"""
Text Cleaning Module

This module cleans the text in every 
required column, strips whitespaces and
standardizes it.

Author: Subir Sutradhar
"""

from config import TEXT_STANDARDIZATION_RULES
from models.validation_result import WaveResult
from pandas import DataFrame


def clean_text(
    workbook: dict[str, DataFrame]
) -> WaveResult:
    """
    Standardizes text columns based on
    configured business rules.

    Args:
        workbook: Dictionary containing worksheet
        names and pandas DataFrame.

    Returns:
        WaveResult
    """

    overall_result = {}
    worksheets_modified = 0
    columns_modified = 0
    for worksheet, dataframe in workbook.items():
        worksheet_result = {}
        for column in dataframe.columns:
            if column not in TEXT_STANDARDIZATION_RULES:
                continue

            rule = TEXT_STANDARDIZATION_RULES[column]
            if rule == "title":
                dataframe[column] = dataframe[column].str.strip().str.title()
                worksheet_result[column] = "Title Case"
            elif rule == "upper":
                dataframe[column] = dataframe[column].str.strip().str.upper()
                worksheet_result[column] = "Upper Case"
            elif rule == "lower":
                dataframe[column] = dataframe[column].str.strip().str.lower()
                worksheet_result[column] = "Lower Case"
            columns_modified += 1
        if worksheet_result:
            overall_result[worksheet] = worksheet_result
            worksheets_modified += 1

    return WaveResult(
        validation_name="Text Standardization",
        status="COMPLETED",
        data=overall_result,
        summary={
            "worksheets_modified": worksheets_modified,
            "columns_modified": columns_modified
        }
    )