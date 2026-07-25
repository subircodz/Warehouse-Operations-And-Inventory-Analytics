"""
Referential Identifier Validator

This module validates that every foreign key
value in a child worksheet exists in its
corresponding parent worksheet.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from config import REFERENTIAL_INTEGRITY_RULES
from models.validation_result import ValidationResult


def validate_referential_identifier(
    workbook: dict[str, DataFrame]
) -> ValidationResult:
    """
    Function to validate that every foreign key in
    in a child worksheet exist in the parent worksheet.

    Args:
        workbook: dict[str, DataFrame]
        Dictionary containing names of worksheet and 
        pandas DataFrame.

    Returns:
        ValidationResult
    """

    overall_result = {}

    for rule in REFERENTIAL_INTEGRITY_RULES:

        result = {
            "overall_validation": 0,
            "valid": 0,
            "invalid": 0,
            "invalid_row_list": []
        }

        # ==============================
        # Read configuration
        # ==============================

        parent_worksheet = rule["parent_worksheet"]
        parent_column = rule["parent_column"]

        child_worksheet = rule["child_worksheet"]
        child_column = rule["child_column"]

        # ==============================
        # Read worksheets
        # ==============================

        parent_df = workbook[parent_worksheet]
        child_df = workbook[child_worksheet]

        # ==============================
        # Read columns
        # ==============================

        parent_column_data = parent_df[parent_column]
        child_column_data = child_df[child_column]

        # ==============================
        # Build lookup
        # ==============================

        parent_ids = set(parent_column_data)

        # ==============================
        # Validate child identifiers
        # ==============================

        for row_number, child_id in enumerate(child_column_data, start=2):

            result["overall_validation"] += 1

            if child_id in parent_ids:
                result["valid"] += 1
            else:
                result["invalid"] += 1
                result["invalid_row_list"].append(row_number)

        relationship_name = (
            f"{child_worksheet}.{child_column} -> "
            f"{parent_worksheet}.{parent_column}"
        )

        overall_result[relationship_name] = result


    return ValidationResult(
        validation_name="Referential Integrity Validation",
        status="PASS",
        data=overall_result
    )