"""
Unique Value Profiling Module

This module profiles unique values of 
each column in a workbook.

Author: Subir Sutradhar
"""
from pandas import DataFrame
from models.validation_result import WaveResult

def profile_unique_values(
        workbook: dict[str, DataFrame]
        ) -> dict[str, dict[str, int]]:
    """
    Profiles the unique values in every column
    of each worksheet in a workbook.

    Args:
        workbook: A dictionary of worksheet and 
        pandas DataFrame

    Returns:
        Dictionary containing worksheet names and
        the unique value count for every column.

    Raises:
        TypeError
    """
    if not isinstance(workbook, dict):
        raise TypeError("Expected workbook to be a dictionary.")
    overall_result: dict[str, dict[str, int]] = {}
    col_count = 0
    for worksheet, dataframe in workbook.items():
        result: dict[str, int] = {}
        for column in dataframe:
            col_count += 1
            result[column] = int(dataframe[column].nunique())
        overall_result[worksheet] = result
    return WaveResult(
        validation_name="Unique Value Profiler",
        data=overall_result,
        summary={
            "worksheets": len(workbook),
            "total_unique": col_count
        }
    )