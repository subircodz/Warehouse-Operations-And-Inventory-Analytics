"""
Worksheet discovery module.

This module takes a workbook and finds out 
worksheet names and calucaltes the total 
worksheets present in the workbook

Suthor: Subir Sutradhar
"""
from pandas import DataFrame
def worksheet_discovery(workbook: dict[str, DataFrame]) -> dict[list, int]:
    """
    Retuns total worksheet count and worksheet names.

    Args:
        workbook: dict[str, DataFrame]
    
    Returns:
        dict[list, int]
    """
    return {
    "worksheet_names": list(workbook.keys()),
    "worksheet_count": len(workbook.keys())
}