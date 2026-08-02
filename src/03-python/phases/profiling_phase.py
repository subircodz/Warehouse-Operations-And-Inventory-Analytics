"""
Data Profiling Module.

This module profiles a workbook by dispatching it to the
appropriate profiling modules, collecting their results,
and returning the combined profiling results to the main
application.

Author: Subir Sutradhar
"""

from profiling import (
    worksheet_discovery,
    profile_record_count,
    column_discovery,
    profile_datatype,
    profile_missing_value,
    profile_duplicates,
    profile_unique_values
)

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
    print(f"{INFO}  Missing Value Summary")
    print("-" * 60)
    print(f"Total Worksheets: {worksheet_result.summary['worksheet_count']}")
    print("=" * 60)  
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
    print("=" * 60)
    print(f"{INFO}  Record Count Summary")
    print("-" * 60)
    print(f"{INFO}  Total Worksheets : {record_count_result.summary['worksheets']}")
    print(f"{INFO}  Total Records    : {record_count_result.summary['total_records']:,}")
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
    print("=" * 60)
    print(f"{INFO}  Column Discovery Summary")
    print("-" * 60)
    print(f"{INFO}  Total Worksheets : {column_result.summary['worksheets_checked']}")
    print(f"{INFO}  Total Columns    : {column_result.summary['columns_profiled']}")
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
    print("=" * 60)
    for worksheet, data in missing_value_result.data.items():
        print(f"► Worksheet : {worksheet}")
        print("-" * 60)
        for column, missing in data.items():
            print(f"    ✔ {column:<25} : {missing}")
        print("=" * 60)
    print(f"{INFO}  Missing Value Summary")
    print("-" * 60)
    print(f"Worksheets checked   : {missing_value_result.summary['worksheets_checked']}")
    print(f"Columns affected     : {missing_value_result.summary['columns_affected']}")
    print(f"Total Missing Values : {missing_value_result.summary['total_missing_values']}")
    print("=" * 60)    
    print(f"{SUCCESS} Missing Value Profiling Completed.\n")
    profiling_results.append(missing_value_result)

    # ==========================================================
    # Duplicates Profiling
    # ==========================================================

    duplicate_result = profile_duplicates(workbook)
    print("=" * 60)
    print(f"{INFO}  Duplicates Profiling")
    print("=" * 60)
    for worksheet, duplicate_count in duplicate_result.data.items():
        print(f"    ✔ {worksheet:<25} : {duplicate_count}")
    print("=" * 60)
    print(f"{INFO}  Duplicates Profiling Summary")
    print("-" * 60)
    print(f"Worksheets checked  : {duplicate_result.summary["worksheets_checked"]}")
    print(f"Total Duplicates    : {duplicate_result.summary["total_duplicates"]}")
    print("=" * 60)    
    print(f"{SUCCESS} Duplicates Profiling Completed.\n")
    profiling_results.append(duplicate_result)

    # ==========================================================
    # Unique Values Profiling
    # ==========================================================

    unique_values_profiles = profile_unique_values(workbook)
    print("=" * 60)
    print(f"{INFO}  Unique Values Profiling")
    print("=" * 60)
    col_count = 0
    for worksheet, data in unique_values_profiles.data.items():
        print(f"► Worksheet : {worksheet}")
        print("-" * 60)
        for column, count in data.items():
            print(f"    ✔ {column:<25} : {count} unique")
            col_count+=1
        print("=" * 60)
    print(f"{INFO}  Unique Value Summary")
    print("-" * 60)
    print(f"Worksheets checked     : {unique_values_profiles.summary["worksheets"]}")
    print(f"Total Columns Profiled : {unique_values_profiles.summary["total_unique"]}")
    print("=" * 60)    
    print(f"{SUCCESS} Unique Values Profiling Completed.\n")
    profiling_results.append(unique_values_profiles)

    