# DATA PROFILING

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Phase:** 06 – Data Profiling  
> **Status:** 🚧 In Progress

---

# Project Information

| Field | Details |
|--------|---------|
| Phase | Data Profiling |
| Version | 1.0 |
| Status | In Progress |

---

# Purpose

The purpose of the Data Profiling phase is to understand the structure, characteristics and overall quality of the available datasets before making any changes.

No data is cleaned, corrected or validated during this phase.

The objective is to observe and document the current condition of the data.

---

# Datasets Profiled

| Dataset | Status |
|----------|:------:|
| Warehouses | ⏳ |
| Suppliers | ⏳ |
| Products | ⏳ |
| Inventory | ⏳ |

---

# Profiling Metrics

The following observations will be collected for every dataset.

## Dataset Overview

- Number of records
- Number of columns
- Column names
- Data types
- Memory usage

---

## Data Completeness

- Missing values
- Blank values
- Null percentage

---

## Data Uniqueness

- Duplicate records
- Duplicate business identifiers
- Duplicate combinations (if applicable)

---

## Value Distribution

- Distinct values
- Most frequent values
- Least frequent values
- Frequency distribution (where applicable)

---

## Business Identifier Overview

- Identifier format
- Prefix used
- Numeric length
- Identifier uniqueness

> Business identifiers are **observed only** during profiling. They are validated later during the Data Validation phase.

---

## Relationship Discovery

Identify how datasets are related.

Examples:

| Parent Dataset | Child Dataset | Relationship |
|---------------|---------------|--------------|
| Suppliers | Products | supplier_id |
| Products | Inventory | product_id |
| Warehouses | Inventory | warehouse_id |

Relationships are documented during profiling but validated later.

---

## Data Quality Observations

Record any observations without correcting them.

Example observations:

- Mixed letter casing
- Unexpected values
- Blank cells
- Duplicate records
- Suspicious identifiers
- Inconsistent spellings
- Unexpected data types

---

# Profiling Summary

After profiling every dataset, summarise:

- Overall dataset health
- Major observations
- Potential risks
- Areas requiring cleaning
- Areas requiring validation

---

# Deliverables

This phase produces:

- Dataset Profile
- Data Quality Observations
- Relationship Map
- Profiling Summary

These deliverables become the input for the Data Cleaning phase.

---

# Out of Scope

The following activities are **not performed** during Data Profiling.

- Data Cleaning
- Data Validation
- Business Rule Validation
- Referential Integrity Validation
- Exploratory Data Analysis
- Business Insights

---

# Phase Summary

The Data Profiling phase documents the current condition of the raw datasets.

The observations collected during this phase will guide the Data Cleaning phase by identifying data quality issues that require correction before validation and analysis.

---

# Next Phase

➡ **Data Cleaning**

The next phase focuses on correcting the data quality issues identified during Data Profiling while preserving business meaning and data integrity.