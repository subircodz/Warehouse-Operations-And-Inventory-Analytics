"""
Data Profiling Module.

This module profiles a workbook by dispatching it to the
appropriate profiling modules, collecting their results,
and returning the combined profiling results to the main
application.

Author: Subir Sutradhar
"""

from profiling.worksheet_discovery import worksheet_discovery
from profiling.record_count import profile_record_count
from profiling.column_profile import column_discovery
from profiling.datatype_profile import profile_datatype
from profiling.missing_value_profile import profile_missing_value
from utils.icons import INFO, SUCCESS
from pandas import DataFrame


def profiling_phase(workbook: dict[str, DataFrame]) -> list:
    """
    Profiles the workbook by dispatching it to the
    appropriate profiling modules, collecting their
    results, and returning the combined profiling
    results.

    Args:
        workbook: Dictionary containing worksheet
            names and their corresponding DataFrames.

    Returns:
        list: Collection of profiling results.
    """

    profiling_results = []

    # ==========================================================
    # Worksheet Discovery
    # ==========================================================
    worksheet_result = worksheet_discovery(workbook)

    print("=" * 60)
    print("Worksheets Found")
    print("=" * 60)

    for worksheet in worksheet_result.data["worksheet_names"]:
        print(f"✓ {worksheet}")

    print("=" * 60)
    print(f"{INFO}  Total Worksheets : {worksheet_result.data['worksheet_count']}")
    print(f"{SUCCESS} Worksheet Discovery Completed.\n")

    profiling_results.append(worksheet_result)

    # ==========================================================
    # Record Count Profiling
    # ==========================================================
    record_count_result = profile_record_count(workbook)

    print("=" * 60)
    print(f"{INFO}  Record Count Profiling")
    print("=" * 60)

    print(f"{'Worksheet':<25}{'Records':>15}")
    print("-" * 60)

    for worksheet, count in record_count_result.data.items():
        print(f"{worksheet:<25}{count:>15,}")

    print("-" * 60)

    total_records = sum(record_count_result.data.values())

    print(f"{INFO}  Total Worksheets : {len(record_count_result.data)}")
    print(f"{INFO}  Total Records    : {total_records:,}")
    print(f"{SUCCESS} Record Count Profiling Completed.\n")

    profiling_results.append(record_count_result)

    # ==========================================================
    # Column Discovery
    # ==========================================================
    column_result = column_discovery(workbook)

    print("=" * 60)
    print(f"{INFO}  Column Discovery")
    print("=" * 60)

    for worksheet, columns in column_result.data.items():

        print(f"► Worksheet : {worksheet}")
        print("-" * 60)

        for column in columns:
            print(f"    ✔ {column}")

        print("-" * 60)

    print(f"{SUCCESS} Column Discovery Completed.\n")

    profiling_results.append(column_result)

    # ==========================================================
    # Datatype Profiling
    # ==========================================================
    datatype_result = profile_datatype(workbook)
    print("=" * 60)
    print(f"{INFO}  Datatype Profiling")
    print("=" * 60)
    for worksheet, datatypes in datatype_result.data.items():
        print(f"► Worksheet : {worksheet}")
        print("-" * 60)
        for column, dtype in datatypes.items():
            print(f"    ✔ {column:<25} : {dtype}")
        print("-" * 60)
    print(f"{SUCCESS} Datatype Profiling Completed.\n")
    profiling_results.append(datatype_result)

    # ==========================================================
    # Missing Value Profiling
    # ==========================================================

    missing_value_result = profile_missing_value(workbook)
    print("=" * 60)
    print(f"{INFO}  Missing Value Profiling")
    overall_missing = 0
    column_count = 0
    print("=" * 60)
    for worksheet, data in missing_value_result.items():
        print(f"► Worksheet : {worksheet}")
        print("-" * 60)
        for column, missing in data.items():
            print(f"    ✔ {column:<25} : {missing}")
            overall_missing += int(missing)
            column_count += 1
        print("=" * 60)
    print(f"{INFO}  Missing Value Summary")
    print("-" * 60)
    print(f"Worksheets affected  : {len(workbook.keys())}")
    print(f"Columns affected     : {column_count}")
    print(f"Total Missing Values : {overall_missing}")
    print("=" * 60)    
    print(f"{SUCCESS} Missing Value Profiling Completed.\n")

    