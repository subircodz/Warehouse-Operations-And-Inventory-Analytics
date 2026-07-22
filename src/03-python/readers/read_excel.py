"""
This module is responsible for reading
Microsoft Excel workbooks.

Author: Subir Sutradhar
"""

import pandas as pd


def read_excel(source: str) -> dict:
    """
    Read an Excel workbook.

    Args:
        source (str):
            Path to the Excel workbook.

    Returns:
        dict:
            Dictionary containing worksheet names
            and their corresponding DataFrames.
    """

    workbook = pd.read_excel(
        source,
        sheet_name=None
    )

    return workbook