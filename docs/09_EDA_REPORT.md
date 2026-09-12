# EXPLORATORY DATA ANALYSIS

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Phase:** 09 – Exploratory Data Analysis  
> **Status:** ✅ Completed

---

## Purpose

The EDA phase analyses the trusted data to identify inventory distribution, inventory value, product characteristics and operational observations that can support later business interpretation.

---

## Implemented Analysis

### Inventory Analysis

The Python analysis includes:

- Total inventory quantity
- Inventory distribution by warehouse
- Inventory monetary value
- Inventory value by warehouse
- Inventory value by product
- Inventory held against inactive products

### Product Analysis

The Python analysis includes:

- Total product count
- Active and inactive product counts
- Minimum, maximum, average and median product price
- Product price range and standard deviation
- Extreme price observations
- Weighted average inventory cost by product
- Estimated product margin and margin percentage
- Products without corresponding inventory-cost records
- Positive, negative and zero estimated-margin groups
- Active and inactive products with negative estimated margins

---

## Engineering Implementation

EDA is implemented through reusable Python modules under `src/03-python/analysis/` rather than being limited to ad-hoc notebook calculations.

The inventory analysis module returns structured analysis results, while the product analysis module produces both summary metrics and findings for downstream reporting.

---

## Phase Outcome

The EDA implementation is complete and represents the latest verified analytical phase in the repository.

Business Insights, Recommendations and Executive Summary are intentionally not marked complete here because corresponding final-phase documentation/artifacts are not currently present in the repository.

---

## Navigation

| Document | Link |
|----------|------|
| Data Validation | [08_DATA_VALIDATION.md](08_DATA_VALIDATION.md) |
| Project Summary | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |
| Phase Checklist | [15_PHASE_CHECKLIST.md](15_PHASE_CHECKLIST.md) |
| Project README | [README.md](../README.md) |
