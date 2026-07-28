# DATA DISCOVERY

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Phase:** 05 – Data Discovery  
> **Status:** ✅ Completed

---

# Project Information

| Field | Details |
|--------|---------|
| Phase | Data Discovery |
| Version | 2.0 |
| Status | Completed |

---

# Purpose

After understanding the business and documenting stakeholder requirements, the next step is to identify the datasets available for analysis.

The objective of this phase is to discover every available data source, understand its business purpose and verify that the required information exists before assessing data quality.

At this stage, the focus is **understanding the data**, not validating or cleaning it.

---

# Available Data Sources

Warehouse operations rely on data generated from multiple business systems.

The following data sources have been identified for this project.

| Source | Business Purpose |
|---------|------------------|
| Warehouse Management System (WMS) | Stores warehouse operations, inventory movement and storage information. |
| Enterprise Resource Planning (ERP) | Stores procurement, supplier and inventory transaction data. |
| CSV Exports | Operational data exported from business systems. |
| Microsoft Excel Reports | Business reports maintained by operational teams. |

---

# Available Datasets

The following datasets were identified during the discovery process.

| Dataset | Business Purpose |
|----------|------------------|
| Warehouses | Stores warehouse information. |
| Suppliers | Stores supplier details. |
| Products | Stores product master information. |
| Inventory | Stores inventory availability across warehouses. |

These datasets provide the foundation for answering the business questions identified during the Business Requirements phase.

---

# Data Availability

The required business data is available in multiple formats.

| Data Source | Status |
|-------------|--------|
| SQL Database | ✅ Available |
| CSV Files | ✅ Available |
| Microsoft Excel Workbook | ✅ Available |

---

# Activities Completed

The following activities were completed during the Data Discovery phase.

- Identified all available business datasets.
- Documented the available data sources.
- Verified dataset accessibility.
- Understood the business purpose of each dataset.
- Confirmed that the required business information is available for analysis.

---

# Out of Scope

The following activities are **not performed** during the Data Discovery phase.

- Data Profiling
- Data Quality Assessment
- Missing Value Analysis
- Duplicate Detection
- Data Cleaning
- Business Rule Validation
- Referential Integrity Validation
- Exploratory Data Analysis

These activities will be performed in the subsequent DAPM phases.

---

# Key Findings

The Data Discovery phase established the following observations.

- Business data is available from multiple operational systems.
- Each dataset supports one or more business functions.
- The identified datasets are sufficient to answer the business requirements documented earlier.
- No assumptions were made regarding data quality during this phase.

---

# Phase Summary

The available business datasets have been successfully identified and documented.

The business purpose of each dataset is now understood, providing a clear foundation for the next phase, where the structure and quality of the raw data will be examined.

---

# Next Phase

➡ **Data Profiling**

The next phase focuses on understanding the structure and characteristics of the raw datasets by examining record counts, data types, value distributions and overall data quality before any cleaning or validation activities begin.