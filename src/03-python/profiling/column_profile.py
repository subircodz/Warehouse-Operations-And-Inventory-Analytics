"""
Column Profiling Module

This module takes a workbook and finds out
all the columns in each worksheet

Author: Subir Sutradhar
"""
from models.validation_result import WaveResult
from pandas import DataFrame
def column_discovery(workbook: dict[str, DataFrame]) -> WaveResult:
    """
    Takes a workbook and extracts all the columns in 
    each worksheet and returns an object.

    Args:
        workbook: dict[str, DataFrame]

    Returns:
        WaveResult
    """
    result = {}
    for worksheet, dataframe in workbook.items():
        # columns = []
        # for cols in dataframe.keys():
        #     columns.append(cols)
        columns = list(dataframe.columns)
        result[worksheet] = columns
    return WaveResult(
        validation_name="Column Discovery",
        data=result
    )
