"""
Missing Value Profiling Module.

This module profiles missing values for each column
in every worksheet of a workbook.

Author: Subir Sutradhar
"""
from pandas import DataFrame
from models.validation_result import WaveResult

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

    total_missing = 0
    columns_affected = 0

    for worksheet, dataframe in workbook.items():

        result = {}

        for column in dataframe:

            missing = int(dataframe[column].isna().sum())

            if missing > 0:
                result[column] = missing
                total_missing += missing
                columns_affected += 1

        overall_result[worksheet] = result

    return WaveResult(
        validation_name="Missing Value Profiling",

        data=overall_result,

        summary={
            "worksheets_checked": len(workbook),
            "columns_affected": columns_affected,
            "total_missing_values": total_missing
        }
    )