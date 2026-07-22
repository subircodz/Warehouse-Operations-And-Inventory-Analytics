# ANALYTICAL THINKING

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Document:** Analytical Thinking Register  
> **Status:** 🚧 In Progress

---

## Purpose

This document captures analytical ideas, working hypotheses, and engineering decisions throughout the Data Analytics Project Methodology (DAPM).

The entries recorded here represent the current understanding of the business and help guide subsequent analytical activities. They are exploratory in nature and should not be interpreted as validated findings.

Every assumption documented in this register must be verified using evidence collected during the later phases of the project.

---

# Phase 1 – Business Understanding

## Initial Analytical Focus

| Business Problem | Analytical Focus | Potential Data Sources |
|------------------|------------------|------------------------|
| Stockouts | Current Stock, Stock Status | Goods Received, Goods Dispatched |
| Overstock | Inventory Age, Inventory Turnover | Inventory Records, Dispatch Records |
| Delayed Deliveries | Delivery Delay, On-Time Delivery | Orders, Dispatch, Delivery |
| Inventory Mismatch | Stock Difference | Physical Count, System Stock |
| Customer Complaints | Complaint Count, Return Rate | Complaints, Returns |

---

## Potential Business Dimensions

The following business dimensions are expected to support filtering, grouping, and summarising business information during analysis.

- Product
- Category
- Warehouse
- Customer
- Date

---

# Phase 2 – Stakeholder Analysis

## Stakeholder Information Requirements

| Stakeholder | Information Required |
|--------------|----------------------|
| Inventory Manager | Current Stock, Stock Status, Reorder Alerts |
| Procurement Team | Reorder Level, Supplier Lead Time, Demand Trends |
| Warehouse Manager | Storage Utilisation, Inventory Movement |
| Logistics Team | Dispatch Status, Delivery Performance |
| Sales Team | Product Availability |
| Customer Support | Delayed Orders, Incorrect Deliveries |
| Finance | Inventory Value, Carrying Cost |

---

## Engineering Decisions

- Different stakeholders require different business views of the same operational data.
- Business metrics should be calculated once and reused across multiple reports and dashboards.
- Dashboards should be organised around business functions rather than individual datasets.
- Business logic should remain independent of the reporting or visualisation layer.

---

# Phase 3 – Business Requirements

## Engineering Decisions

- A common analytics layer should generate reusable business metrics.
- Shared calculations should minimise duplication across reports and dashboards.
- Dataset discovery should prioritise the tables and columns required to satisfy business requirements.
- Business metrics should be defined before dashboard development begins.
- Reporting requirements should drive data modelling, not the other way around.

---

# Phase 4 – Data Discovery

## Engineering Decisions

- The SQL database will serve as the primary analytical data source whenever available.
- Excel reports will be used to verify business calculations where required.
- CSV exports provide an alternative data source for Spreadsheet and Python validation.
- Original datasets must remain unchanged throughout the project.
- Data Validation must be completed before any cleaning or transformation activities.

---

## Engineering Principles

The following principles should be followed throughout the analytical lifecycle.

- Record observations before forming conclusions.
- Separate assumptions from verified facts.
- Validate every hypothesis using evidence.
- Design reusable business metrics.
- Keep business logic independent of presentation layers.
- Preserve raw data throughout the project lifecycle.

---

## Validation Reminder

Entries in this document represent analytical thinking rather than verified findings.

Every hypothesis, assumption, and engineering decision should be validated using evidence collected during subsequent DAPM phases before being treated as a business insight or recommendation.

---

## Phase Summary

The Analytical Thinking Register documents the reasoning process followed during the project.

Maintaining this document separately from the Observation Register helps distinguish verified facts from analytical assumptions, providing a transparent record of the decision-making process throughout the DAPM lifecycle.

---

## Navigating Documents

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