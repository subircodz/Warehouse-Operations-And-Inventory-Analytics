"""
Missing Value Profiling Module.

This module profiles missing values for each column
in every worksheet of a workbook.

Author: Subir Sutradhar
"""
from pandas import DataFrame

def profile_missing_value(workbook: dict[str, DataFrame]) -> dict[str, dict[str, int]]:
    """
    Profiles missing values in each worksheet and
    returns the total missing values for every column.

    Args:
        workbook: Dictionary containing worksheet names
            and their corresponding pandas DataFrames.

    Returns:
        dict

    Raises:
        TypeError
    """
    if not isinstance(workbook, dict):
        raise TypeError("Expected workbook to be a dictionary.")
    overall_result = {}
    for worksheet, dataframe in workbook.items():
        result = {}
        for column in dataframe:
            total_missing = dataframe[column].isna().sum()
            if total_missing:
                result[column] = total_missing
        overall_result[worksheet] = result
    return overall_result
            