"""
Missing Values Validation

This module validates the missing values
in each worksheet.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from models.validation_result import ValidationResult

def validate_missing_values(workbook: dict[str, DataFrame]) -> ValidationResult:
    """
    Find and count the missing values in each worksheet

    Arg:
        workbook: dict[str, DataFrame]
        Dictionary containing worksheet name and
        pandas Dataframe.
    
    Return:
        dict[str, int]
        Dictionary containing worksheet name and
        missing values count.
    """
    missing_count: dict[str, int] = {}

    for worksheet_name, dataframe in workbook.items():
        col = dataframe.isnull().sum()
        total_missing = col.values.sum()
        missing_count[worksheet_name] = int(total_missing)

    return ValidationResult(
            validation_name="Missing Value Validation",
            status="PASS",
            data=missing_count
        )