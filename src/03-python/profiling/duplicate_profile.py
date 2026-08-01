"""
Duplicate Profiling Module

This module profiles duplicate records in each worksheet
of a workbook and returns the total number of duplicate
records found in every worksheet.

Author: Subir Sutradhar
"""

from pandas import DataFrame


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
    for worksheet, dataframe in workbook.items():
        result[worksheet] = int(dataframe.duplicated().sum())
    return result