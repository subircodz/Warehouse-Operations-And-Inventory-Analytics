"""
Business Identifier Validator

This module validates the business identifier
in specified worksheets.

Author: Subir Sutradhar
"""

from pandas import DataFrame
from config import IDENTIFIER_PATTERNS
from models.validation_result import WaveResult

def validate_business_identifier(workbook: dict[str, DataFrame]) -> WaveResult:
    """
    Counts the total records validated in each worksheet
    and returns the total valid, invalid and list of row 
    numbers of the invalid identifier.

    Args:
        workbook: dict[str, DataFrame]
        A dictionary containing the worksheet name and 
        pandas DataFrame.

    Returns:
        WaveResult
        An object containing name, rows and a dictionary of 
        dictionary.
    """
    records_checked = {}
    for worksheet, dataframe in workbook.items():
        if worksheet in IDENTIFIER_PATTERNS:
            result = {
                    "overall_validation" : 0,
                    "valid" : 0,
                    "invalid" : 0,
                    "invalid_row_list" : []
                }
            col_name = IDENTIFIER_PATTERNS[worksheet]["column"]
            prefix = IDENTIFIER_PATTERNS[worksheet]["prefix"]
            numeric_length = IDENTIFIER_PATTERNS[worksheet]["numeric_length"]


            for idx, value in enumerate(dataframe[col_name], start=2):
                row = idx
                identifier = str(value)
                id_prefix = identifier[:len(prefix)]
                id_num_part = identifier[len(prefix):]
                result["overall_validation"] += 1
                if id_prefix == prefix and len(id_num_part) == numeric_length and id_num_part.isdigit():
                    result["valid"] += 1
                else:
                    result["invalid"] += 1
                    result["invalid_row_list"].append(row)
            records_checked[worksheet] = result


    return WaveResult(
            validation_name="Business identifier validation",
            status="PASS",
            data=records_checked
        )

