"""
Display the application startup banner.

This module contains utility functions responsible for
displaying the startup banner and project information
for the Warehouse Analytics Validation Engine (WAVE).

Author: Subir Sutradhar
"""
from .icons import PACKAGE
from config import ENVIRONMENT

def display_banner():
    """
    Display the application banner and project metadata.

    Returns:
        None
    """
    banner = fr"""
 /$$      /$$  /$$$$$$  /$$    /$$ /$$$$$$$$
| $$  /$ | $$ /$$__  $$| $$   | $$| $$_____/
| $$ /$$$| $$| $$  \ $$| $$   | $$| $$
| $$/$$ $$ $$| $$$$$$$$|  $$ / $$/| $$$$$
| $$$$_  $$$$| $$__  $$ \  $$ $$/ | $$__/
| $$$/ \  $$$| $$  | $$  \  $$$/  | $$
| $$/   \  $$| $$  | $$   \  $/   | $$$$$$$$
|__/     \__/|__/  |__/    \_/    |________/

============================================================
      {PACKAGE} Warehouse Analytics Validation Engine
============================================================

Project      : Warehouse Operations & Inventory Analytics
Version      : 0.2.1
Methodology  : DAPM Framework v0.2.1
Environment  : {ENVIRONMENT}
Python       : 3.13.7
Workbook     : Warehouse_Reports.xlsx
Author       : Subir Sutradhar

============================================================
"""
    print(banner)                    