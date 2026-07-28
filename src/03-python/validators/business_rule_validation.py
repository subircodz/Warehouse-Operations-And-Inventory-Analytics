"""
Business rule validator module

This module takes a workbook, loops through
every sheet and checks for invalid values
in business specific columns.

Author: Subir Sutradhar
"""

from pandas import DataFrame

def validate_business_rules(workbook: dict[str, DataFrame]):
    
    pass