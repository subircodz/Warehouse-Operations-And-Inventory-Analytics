# Spreadsheet Validation

> **Module:** Data Validation – Spreadsheet  
> **Status:** ✅ Completed

---

## Purpose

Spreadsheet validation provides the first assessment of the raw warehouse dataset before SQL- and Python-based validation.

This stage focuses on identifying visible data quality issues using spreadsheet functions and manual inspection. No data is modified during this process.

---

# Dataset

**Source Workbook**

`data/raw/excel/Warehouse_Reports.xlsx`

The workbook contains the following worksheets.

| Worksheet | Description |
|-----------|-------------|
| Warehouses | Warehouse master data |
| Suppliers | Supplier master data |
| Products | Product master data |
| Inventory | Current inventory records |

---

# Validation Scope

Each worksheet was reviewed independently to assess basic data quality.

The following validation checks were performed:

- Total records
- Missing values
- Duplicate records
- Identifier validation

No changes were made to the source dataset during this phase.

---

# Spreadsheet Features Used

| Feature | Purpose |
|----------|---------|
| COUNTA() | Count total records |
| COUNTBLANK() | Count missing values |
| COUNTIF() | Detect duplicate records |
| Formulas | Validate identifier values |
| Dashboard | Consolidate validation results |

---

# Validation Dashboard

A validation dashboard was created within the workbook to consolidate the results from all worksheets.

The dashboard summarises:

- Total worksheets
- Total records
- Missing values
- Duplicate records
- Identifier validation results

The dashboard provides a single view of the overall data quality across the workbook.
---

# Validation Findings

The validation identified the following data quality issues:

- Missing values
- Duplicate records
- Invalid identifiers

These findings have been intentionally preserved for subsequent SQL validation, Python validation, and Data Preparation.

---

# Deliverables

| Deliverable | Description |
|-------------|-------------|
| Warehouse_Reports.xlsx | Source workbook |
| Validation Dashboard | Summary of validation results |
| Supporting Screenshots | Dashboard preview |

---

# Validation Dashboard

<p align="center">
    <img src="screenshots/warehouse.png" width="100%">
</p>

---

# Next Phase

Proceed to SQL Validation to verify relational integrity, uniqueness constraints, and business rules using SQL queries.

---

## Navigation

| Document | Link |
|----------|------|
| Data Validation | [06_DATA_VALIDATION.md](../../docs/06_DATA_VALIDATION.md) |
| SQL Validation | [README.md](../02-sql/README.md) |
| Python Validation | [README.md](../03-python/README.md) |
| Data Discovery | [05_DATA_DISCOVERY.md](../../docs/05_DATA_DISCOVERY.md) |