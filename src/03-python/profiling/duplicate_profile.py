"""
Duplicate Profiling Module

This module profiles duplicate records in each worksheet
of a workbook and returns the total number of duplicate
records found in every worksheet.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from models.validation_result import WaveResult

def profile_duplicates(workbook: dict[str, DataFrame]) -> dict[str, int]:
    """
    Profiles duplicate records in each worksheet.

    Args:
        workbook: Dictionary containing worksheet names
            and their corresponding pandas DataFrames.

    Returns:
        Dictionary containing worksheet names and the
        total duplicate records found in each worksheet.

    Raises:
        TypeError: If workbook is not a dictionary.
    """
    if not isinstance(workbook, dict):
        raise TypeError("Expected workbook to be a dictionary.")
    result: dict[str, int] = {}
    total_duplicates = 0
    for worksheet, dataframe in workbook.items():
        duplicates = int(dataframe.duplicated().sum())
        total_duplicates += int(duplicates)
        result[worksheet] = duplicates
    return WaveResult(
        validation_name="Duplicate Profiling",
        data=result,
        summary={
        "worksheets_checked": len(workbook),
        "total_duplicates": total_duplicates
        }
    )