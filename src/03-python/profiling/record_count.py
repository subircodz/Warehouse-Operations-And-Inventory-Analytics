"""
Record Count Validation

This module validates the total number of records
available in each worksheet.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from models.validation_result import WaveResult


def profile_record_count(workbook: dict[str, DataFrame]) -> WaveResult:
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
    total_records = 0
    for worksheet_name, dataframe in workbook.items():
        total_records += int(len(dataframe))
        record_counts[worksheet_name] = len(dataframe)

    return WaveResult(
        validation_name="Record Count Profiler",
        data=record_counts,
        summary={
            "worksheets": len(workbook),
            "total_records": total_records
        }
    )