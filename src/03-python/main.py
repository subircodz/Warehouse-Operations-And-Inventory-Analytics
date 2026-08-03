"""
Application Entry Point

This module initializes the Warehouse Operations &
Inventory Analytics validation application.

Author: Subir Sutradhar
"""
from config import WORKBOOK_PATH
from phases.profiling_phase import profiling_phase
from phases.validation_phase import validation_phase
from utils.banner import display_banner
from utils.file_loader import load_data
from utils.icons import SUCCESS, INFO


def main() -> None:

    wave_results = {
    "data_profiling": [],
    "data_cleaning": [],
    "data_validation": [],
    "eda": [],
    "business_insights": [],
    }

    # =================================
    # Display the banner
    # =================================
    display_banner()

    # =================================
    # Validation Results
    # =================================
    print(f"{INFO}  Loading workbook...")

    # =================================
    # Load the file
    # =================================
    workbook = load_data(WORKBOOK_PATH)
    print(f"{SUCCESS} Workbook '{WORKBOOK_PATH.name}' loaded successfully.")

    # =================================
    # Profiling Phase
    # =================================

    wave_results["data_profiling"] = profiling_phase(workbook)

    # =================================
    # Validation Phase
    # =================================

    wave_results["data_validation"] = validation_phase(workbook)

    

if __name__ == "__main__":
    main()