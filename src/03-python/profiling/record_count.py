"""
Record Count Validation

This module validates the total number of records
available in each worksheet.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from models.validation_result import ValidationResult


def validate_record_count(workbook: dict[str, DataFrame]) -> ValidationResult:
    """
    Count the total number of records in each worksheet.

    Args:
    workbook : dict[str, DataFrame]
        Dictionary containing worksheet names and DataFrames.

    Returns:
    dict[str, int]
        Dictionary containing worksheet names
        and their respective record counts.

    """

    record_counts: dict[str, int] = {}

    for worksheet_name, dataframe in workbook.items():
        record_counts[worksheet_name] = len(dataframe)

    return ValidationResult(
        validation_name="Record Count Validation",
        status="PASS",
        data=record_counts
    )