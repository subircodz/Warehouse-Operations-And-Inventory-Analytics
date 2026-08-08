"""
Text Cleaning Module

This module cleans text in every
required column, strips whitespaces,
standardizes case, and applies
configured value replacements.

Author: Subir Sutradhar
"""

from config import (
    TEXT_STANDARDIZATION_RULES,
    TEXT_REPLACEMENT_RULES
)
from models.validation_result import WaveResult
from pandas import DataFrame


def clean_text(
    workbook: dict[str, DataFrame]
) -> WaveResult:

    overall_result = {}
    worksheets_modified = 0
    columns_modified = 0

    for worksheet, dataframe in workbook.items():

        worksheet_result = {}

        for column in dataframe.columns:

            column_modified = False

            # ==========================================
            # Strip + case standardization
            # ==========================================

            if column in TEXT_STANDARDIZATION_RULES:

                rule = TEXT_STANDARDIZATION_RULES[column]

                dataframe[column] = dataframe[column].str.strip()

                if rule == "title":
                    dataframe[column] = dataframe[column].str.title()
                    worksheet_result[column] = "Title Case"

                elif rule == "upper":
                    dataframe[column] = dataframe[column].str.upper()
                    worksheet_result[column] = "Upper Case"

                elif rule == "lower":
                    dataframe[column] = dataframe[column].str.lower()
                    worksheet_result[column] = "Lower Case"

                column_modified = True

            # ==========================================
            # Value replacement
            # ==========================================

            if column in TEXT_REPLACEMENT_RULES:

                dataframe[column] = dataframe[column].replace(
                    TEXT_REPLACEMENT_RULES[column]
                )

                if column in worksheet_result:
                    worksheet_result[column] += " | Value Replacement"
                else:
                    worksheet_result[column] = "Value Replacement"

                column_modified = True

            # ==========================================
            # Count column only once
            # ==========================================

            if column_modified:
                columns_modified += 1

        # ==============================================
        # Store worksheet result
        # ==============================================

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