# PROJECT CASE JOURNAL

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Document:** Project Case Journal  
> **Status:** 🚧 Business Reporting Pending

---

# Purpose

The Project Case Journal records the journey of the Warehouse Operations & Inventory Analytics project from start to finish.

Unlike the individual DAPM phase documents, this journal provides a chronological record of important decisions, implementation progress, challenges and lessons learned.

---

# Project Timeline

| Phase | Status |
|--------|:------:|
| 01 — Project Brief | ✅ Completed |
| 02 — Business Understanding | ✅ Completed |
| 03 — Stakeholder Analysis | ✅ Completed |
| 04 — Business Requirements | ✅ Completed |
| 05 — Data Discovery | ✅ Completed |
| 06 — Data Profiling | ✅ Completed |
| 07 — Data Cleaning | ✅ Completed |
| 08 — Data Validation | ✅ Completed |
| 09 — Exploratory Data Analysis | ✅ Completed |
| 10 — Business Insights | ⏳ Pending |
| 11 — Recommendations | ⏳ Pending |
| 12 — Executive Summary | ⏳ Pending |

---

# Journal Entries

## 13 July 2026 — Business Understanding

- Studied the warehouse business scenario.
- Understood the end-to-end warehouse workflow.
- Identified major operational challenges.
- Documented business objectives and analytical scope.

**Outcome:** Business context established successfully.

## 15 July 2026 — Stakeholder Analysis

- Identified key business stakeholders.
- Documented responsibilities and information requirements.
- Considered reporting needs by business function.

**Outcome:** Stakeholder expectations were established before reporting requirements were defined.

## 16 July 2026 — Business Requirements

- Documented reporting requirements.
- Identified business metrics.
- Listed management dashboard requirements.
- Defined reporting expectations.

**Outcome:** Business objectives were converted into measurable analytical requirements.

## 17 July 2026 — Data Discovery

- Identified available business systems and datasets.
- Verified data availability.
- Mapped datasets to business requirements.

**Outcome:** Required source datasets were identified.

## 28 July 2026 — DAPM Refactoring

The Data Analytics Project Methodology was redesigned based on practical experience gained while developing WAVE.

Key changes included:

- Separating Data Discovery from Data Profiling.
- Introducing Data Profiling before Data Cleaning.
- Positioning Data Validation after Data Cleaning.
- Reorganising project artifacts for maintainability.

**Outcome:** DAPM v0.2.1 became the reference methodology for the project.

## Late July / Early August 2026 — Data Profiling and Cleaning

The project progressed beyond the original documentation checkpoint.

Completed implementation work included:

- Data profiling and summary reporting.
- Missing-value handling.
- Duplicate cleaning.
- Text standardisation.
- Numeric-range cleaning.
- Cleaning-order refactoring.
- Allowed-value and referential-integrity handling.

**Outcome:** Data Cleaning was completed and the project moved to validation.

## Early August 2026 — Data Validation

Validation was completed across Spreadsheet, SQL and Python/WAVE implementations.

**Outcome:** The data was ready for analytical processing.

## 10 August 2026 — Exploratory Data Analysis

The EDA phase was completed.

The Python analysis layer now includes:

- Inventory quantity and warehouse distribution analysis.
- Inventory monetary value analysis.
- Inventory value by warehouse and product.
- Inactive-product inventory exposure analysis.
- Product catalogue and active/inactive status analysis.
- Product price analysis.
- Weighted average inventory cost analysis.
- Estimated margin analysis.
- Identification of products requiring further investigation.

**Outcome:** The latest verified implementation phase is EDA.

---

# Current State

The previous documentation stopped at Data Profiling even though the implementation had already progressed through Data Cleaning, Data Validation and EDA.

The documentation has now been reconciled with the implementation.

The remaining work is business-facing reporting:

1. Business Insights
2. Recommendations
3. Executive Summary

These phases should be based on the completed analytical evidence.

---

# Lessons Learned

- Understanding the business before analysing data improves analytical decisions.
- Data Discovery and Data Profiling are separate activities.
- Cleaning should precede validation.
- Modular engineering makes analytical processing easier to maintain.
- Analytical findings should be converted into business decisions only after the evidence is understood.

---

# Next Entry

The next journal entry should document the creation and review of the **Business Insights** phase.
