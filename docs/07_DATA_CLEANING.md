# DATA CLEANING

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Phase:** 07 – Data Cleaning  
> **Status:** ✅ Completed

---

## Purpose

The Data Cleaning phase corrects the data-quality issues identified during profiling while preserving the original raw datasets.

Cleaning was implemented as a controlled, modular process so that each transformation has a clear purpose and can be reviewed independently.

---

## Cleaning Activities

The implementation includes the following completed cleaning activities:

- Missing-value handling
- Duplicate-record removal
- Text standardisation
- Numeric-range cleaning
- Allowed-value handling
- Referential-integrity exception handling
- Cleaning-order refactoring to keep transformations deterministic

The raw source data remains preserved separately from processed outputs.

---

## Engineering Approach

Cleaning logic is implemented as reusable Python modules rather than as one large transformation script. The cleaning sequence was refactored so that each operation is performed at the appropriate stage and downstream validation does not duplicate rules already enforced during cleaning.

---

## Phase Outcome

The cleaning implementation was completed and subsequently followed by the Data Validation phase.

The project therefore no longer considers Data Cleaning a pending phase.

---

## Navigation

| Document | Link |
|----------|------|
| Data Profiling | [06_DATA_PROFILING.md](06_DATA_PROFILING.md) |
| Data Validation | [08_DATA_VALIDATION.md](08_DATA_VALIDATION.md) |
| Exploratory Data Analysis | [09_EDA_REPORT.md](09_EDA_REPORT.md) |
| Project README | [README.md](../README.md) |
