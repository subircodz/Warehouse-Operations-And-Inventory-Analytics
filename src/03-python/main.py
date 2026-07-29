"""
Application Entry Point

This module initializes the Warehouse Operations &
Inventory Analytics validation application.

Author: Subir Sutradhar
"""
from config import WORKBOOK_PATH
from validators import (
    validate_missing_values,
    validate_duplicates,
    validate_business_identifier,
    validate_referential_identifier,
    validate_business_rules
    )
from profiling.worksheet_discovery import worksheet_discovery
from utils.banner import display_banner
from utils.file_loader import load_data
from utils.icons import SUCCESS, INFO


def main() -> None:

    validation_results = []

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
    # Count and Find worksheets
    # =================================
    worksheets = worksheet_discovery(workbook)
    # worksheet_count = len(worksheets)
    print("=" * 60)
    print("Worksheets Found")
    print("=" * 60)
    for worksheet in worksheets["worksheet_names"]:
        print(f"✓ {worksheet}")
    print("=" * 60)
    print(f"{INFO}  Total Worksheets : {worksheets['worksheet_count']}")
    print(f"{INFO}  Worksheet Discovery Completed.")


    # # =================================
    # # Display worksheet names
    # # =================================
    # print("\nAvailable Worksheets")

    # for worksheet in workbook.keys():
    #     print(f"  • {worksheet}")

    # # =================================
    # # Validate record count
    # # =================================

    # print(f"\n{INFO}  Validating record counts...")

    # record_count_result = validate_record_count(workbook)

    # print(f"{SUCCESS} Record count validation completed.\n")

    # print(record_count_result.validation_name)
    # print(record_count_result.status)

    # for worksheet, count in record_count_result.data.items():
    #     print(f"  • {worksheet:<15} : {count:,}")

    # validation_results.append(record_count_result)

    # # =================================
    # # Validate missing values
    # # =================================

    # print(f"\n{INFO}  Validating missing counts...")
    # missing_values_count = validate_missing_values(workbook)
    # print(f"{SUCCESS} Missing values count completed.\n")

    # print(missing_values_count.validation_name)
    # print(missing_values_count.status)

    # for worksheet_name, total in missing_values_count.data.items():
    #     print(f"  • {worksheet_name:<15} : {total:,}")

    # validation_results.append(missing_values_count)

    # # =================================
    # # Validate missing values
    # # =================================

    # print(f"\n{INFO}  Validating duplicates counts...")
    # duplicates_count = validate_duplicates(workbook)
    # print(f"{SUCCESS} Duplicates count completed.\n")
    # print(duplicates_count.validation_name)
    # print(duplicates_count.status)
    # for worksheet_name, count in duplicates_count.data.items():
    #     print(f"  • {worksheet_name:<15} : {count:,}")
    # validation_results.append(duplicates_count)

    # # =================================
    # # Business identifier validation
    # # =================================
    # print(f"\n{INFO}  Business identifier validation...")
    # business_identifier = validate_business_identifier(workbook)
    # print(f"{SUCCESS} Business identifier validation completed.\n")
    # print(business_identifier.validation_name)
    # print(business_identifier.status)
    # for worksheet_name, data in business_identifier.data.items():
    #     print(f"  • {worksheet_name} :")
    #     for status, result in data.items():
    #         print(f"    - {status:<20} : {result}")
    # validation_results.append(business_identifier)

    # # =================================
    # # Referential identifier validation
    # # =================================
    # print(f"\n{INFO}  Referential identifier validation...")
    # referential_validation = validate_referential_identifier(workbook)
    # print(f"{SUCCESS} Referential identifier validation completed.")
    # print(referential_validation.validation_name)
    # print(referential_validation.status)
    # for worksheet_name, data in referential_validation.data.items():
    #     print(f"  • {worksheet_name} :")
    #     for status, result in data.items():
    #         print(f"    - {status:<20} : {result}")
    # validation_results.append(referential_validation)

    # # =================================
    # # Business rules validation
    # # =================================

    # business_validation = validate_business_rules(workbook)

if __name__ == "__main__":
    main()