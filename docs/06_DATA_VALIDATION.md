# DATA VALIDATION

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Phase:** 5 – Data Validation  
> **Status:** 🚧 In Progress

---

## Project Information

| Field | Details |
|--------|---------|
| Phase | Data Validation |
| Version | 1.0 |
| Status | In Progress |

---

## Purpose

The Data Validation phase evaluates the quality of the collected datasets before they are used for data preparation, exploratory data analysis, and business reporting.

The same dataset is validated using three independent approaches. Each approach focuses on different aspects of data quality while collectively providing a comprehensive assessment of the dataset.

---

## Validation Approach

The validation process consists of three complementary stages.

| Validation Method | Primary Focus | Status |
|-------------------|---------------|:------:|
| Spreadsheet | Visual inspection and worksheet-level validation | ✅ Completed |
| SQL | Relational integrity, business rules, and data consistency | ✅ Completed |
| Python (Pandas) | Automated validation and quality assessment | 🚧 In Progress |

Each validation stage analyses the same source dataset using techniques best suited to the selected technology.

---

## Validation Workflow

```text
                    Raw Dataset
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
    Spreadsheet         SQL          Python
     Validation      Validation     Validation
          │              │              │
          └──────────────┼──────────────┘
                         │
                         ▼
              Consolidated Validation Findings
                         │
                         ▼
                  Data Preparation
```

---

## Validation Artifacts

The following validation artefacts are maintained throughout this phase.

| Artifact | Purpose |
|----------|---------|
| Spreadsheet Validation | Visual inspection and worksheet-level validation |
| SQL Validation | Business rule verification and relational integrity checks |
| Python Validation | Automated validation using Pandas |
| Consolidated Validation Summary | Combined findings from all validation activities |

---

## Current Progress

| Validation Stage | Status |
|------------------|:------:|
| Spreadsheet Validation | ✅ Completed |
| SQL Validation | ✅ Completed |
| Python Validation | 🚧 In Progress |

---

## Scope

This phase focuses on identifying data quality issues before any transformation is performed.

The following activities are included:

- Missing value analysis
- Duplicate detection
- Data type validation
- Business rule validation
- Referential integrity checks
- Data consistency verification

The following activities are intentionally excluded:

- Data cleaning
- Data transformation
- Feature engineering
- Exploratory Data Analysis (EDA)
- Business insight generation

These activities belong to later phases of the project.

---

## Phase Summary

Data validation establishes confidence in the quality and reliability of the available datasets before analytical work begins.

Using Spreadsheet, SQL, and Python provides multiple perspectives on the same dataset, allowing validation findings to be compared and consolidated before moving to the Data Preparation phase.

---

## Navigation

| Document | Link |
|----------|------|
| Spreadsheet Validation | [Spreadsheet Validation](../src/01-spreadsheet/README.md) |
| SQL Validation | [SQL Validation](../src/02-sql/README.md) |
| Python Validation | [Python Validation](../src/03-python/README.md) |
| Data Discovery | [05_DATA_DISCOVERY.md](05_DATA_DISCOVERY.md) |
| Data Preparation | *Available in the next phase* |

## Navigating Phase Documents

| Document | Link |
|----------|------|
| PROJECT_BRIEF | [01_PROJECT_BRIEF.md](01_PROJECT_BRIEF.md) |
| BUSINESS_UNDERSTANDING | [02_BUSINESS_UNDERSTANDING.md](02_BUSINESS_UNDERSTANDING.md) |
| STAKEHOLDER_ANALYSIS | [03_STAKEHOLDER_ANALYSIS.md](03_STAKEHOLDER_ANALYSIS.md) |
| BUSINESS_REQUIREMENTS | [04_BUSINESS_REQUIREMENTS.md](04_BUSINESS_REQUIREMENTS.md) |
| DATA_DISCOVERY | [05_DATA_DISCOVERY.md](05_DATA_DISCOVERY.md) |
| DATA_VALIDATION | [06_DATA_VALIDATION.md](06_DATA_VALIDATION.md) |
| DATA_PREPARATION | [07_DATA_PREPARATION.md](07_DATA_PREPARATION.md) |
| EDA_REPORT | [08_EDA_REPORT.md](08_EDA_REPORT.md) |
| BUSINESS_INSIGHTS | [09_BUSINESS_INSIGHTS.md](09_BUSINESS_INSIGHTS.md) |
| RECOMMENDATIONS | [10_RECOMMENDATIONS.md](10_RECOMMENDATIONS.md) |
| EXECUTIVE_SUMMARY | [11_EXECUTIVE_SUMMARY.md](11_EXECUTIVE_SUMMARY.md) |
| PROJECT_SUMMARY | [12_PROJECT_SUMMARY.md](12_PROJECT_SUMMARY.md) |
| OBSERVATIONS | [13_OBSERVATIONS.md](13_OBSERVATIONS.md) |
| ANALYTICAL_THINKING | [14_ANALYTICAL_THINKING.md](14_ANALYTICAL_THINKING.md) |
| PHASE_CHECKLIST | [15_PHASE_CHECKLIST.md](15_PHASE_CHECKLIST.md) |
| PROJECT README | [PROJECT README](../README.md) |