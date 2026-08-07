"""
Clean Duplicates Module

This module takes a workbook and cleans
all duplicates found, and returns WaveResult
Object.

Author: Subir Sutradhar
"""

from models.validation_result import WaveResult
from pandas import DataFrame

def clean_duplicates(workbook: dict[str, DataFrame]) -> WaveResult:
    """
    Cleans duplicates in a workbook and returns a 
    summarized result of total duplicates removed 
    in each sheet.

    Args:
        workbook

    Returns:
        WaveResult
    """
    duplicates_count = 0
    worksheet_count = 0
    result = {}
    for worksheet, data in workbook.items():
        total = int(data.duplicated().sum())
        if total > 0:
            data.drop_duplicates(inplace=True)
            duplicates_count += total
            worksheet_count += 1
            result[worksheet] = total
    return WaveResult(
        validation_name="Clean Duplicates",
        status="COMPLETED",
        data=result,
        summary={
            "worksheets_modified" : worksheet_count,
            "duplicates_removed": duplicates_count
        }
    )