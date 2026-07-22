"""
Application Entry Point

This module initializes the Warehouse Operations &
Inventory Analytics validation application.

Author: Subir Sutradhar
"""
from config import WORKBOOK_PATH
from utils.banner import display_banner
from utils.file_loader import load_data


def main() -> None:

    # =================================
    # Display the banner
    # =================================
    display_banner()

    print("[INFO] Loading workbook...")

    # =================================
    # Load the file
    # =================================
    workbook = load_data(WORKBOOK_PATH)

    print(f"[SUCCESS] Workbook '{WORKBOOK_PATH.name}' loaded successfully.")

    # =================================
    # Count worksheets
    # =================================
    
    worksheet_count = len(workbook)
    print(f"[INFO] Worksheets found: {worksheet_count}")

    # =================================
    # Display worksheet names
    # =================================
    print("\nAvailable Worksheets")

    for worksheet in workbook.keys():
        print(f"  • {worksheet}")

if __name__ == "__main__":
    main()