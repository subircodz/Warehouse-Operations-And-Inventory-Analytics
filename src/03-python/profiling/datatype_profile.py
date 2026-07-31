"""
Datatype Profiling Module

This module takes a workbook and finds out the 
datatype of each column in every worksheets.

Author: Subir Sutradhar
"""

from models.validation_result import WaveResult
from pandas import DataFrame

def profile_datatype(workbook: dict[str, DataFrame]) -> WaveResult:
    """
    Function to find out the datatype of columns
    in each worksheet of a workbook.

    Args: 
        workbook: dict[str, DataFrame]

    Returns:
        WaveResult
    """
    if not isinstance(workbook, dict):
        raise TypeError("Expected workbook to be a dictionary.")
    overall_result = {}
    for worksheet, dataframe in workbook.items():
        result = {}
        for column_name in dataframe:
            result[column_name] = str(dataframe[column_name].dtype)
        overall_result[worksheet] = result
    return WaveResult(
        validation_name="Data Type Profiling",
        data=overall_result
    )