"""
Worksheet Discovery Module

This module discovers all worksheets available
in the workbook.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from models.validation_result import WaveResult


def worksheet_discovery(workbook: dict[str, DataFrame]) -> WaveResult:
    """
    Discover all worksheets present in the workbook.

    Args:
        workbook: Dictionary containing worksheet names and DataFrames.

    Returns:
        WaveResult
    """

    return WaveResult(
        validation_name="Worksheet Discovery",
        data={
            "worksheet_names": list(workbook.keys()),
            "worksheet_count": len(workbook)
        }
    )