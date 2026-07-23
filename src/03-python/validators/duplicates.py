"""
Duplicate Record Validation

This module validates the duplicate records
in each worksheet.

Author: Subir Sutradhar
"""
from pandas import DataFrame
from models.validation_result import ValidationResult

def validate_duplicates(workbook: dict[str, DataFrame]) -> ValidationResult:
    """
    Counts the duplicates found in each worksheet

    Args:
        workbook: dict[str, DataFrame]

        Dictionary containing worksheet name and
        pandas DataFrame.
    
    Returns:
        ValidationResult

        An object contaning name, status and DataFrame.
    """

    duplicates: dict[str, int] = {}

    for worksheet_name, dataframe in workbook.items():
        total_duplicates = dataframe.duplicated().sum()
        duplicates[worksheet_name] = int(total_duplicates)

    return ValidationResult(
        validation_name="Duplicate value validation",
        status="PASS",
        data=duplicates
    )


    