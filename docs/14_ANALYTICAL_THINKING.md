# ANALYTICAL_THINKING

> **Purpose:** Quick analytical notes captured after Business Understanding. These ideas are preliminary and will be validated in later DAPM phases.

| Business Problem    | Think About                       | Possible Data Required              |
| ------------------- | --------------------------------- | ----------------------------------- |
| Stockouts           | Current Stock, Stock Status       | Goods Received, Goods Dispatched    |
| Overstock           | Inventory Age, Inventory Turnover | Inventory Records, Dispatch Records |
| Delayed Deliveries  | Delivery Delay, On-Time Delivery  | Orders, Dispatch, Delivery          |
| Inventory Mismatch  | Stock Difference                  | Physical Count, System Stock        |
| Customer Complaints | Complaint Count, Return Rate      | Complaints, Returns                 |

## Possible Dimensions

* Product
* Category
* Warehouse
* Customer
* Date

## Phase 2

### Decision Makers

| Stakeholder | Information Likely Needed |
|--------------|--------------------------|
| Inventory Manager | Current Stock, Stock Status, Reorder Alerts |
| Procurement Team | Reorder Level, Supplier Lead Time, Demand |
| Warehouse Manager | Storage Utilization, Inventory Movement |
| Logistics Team | Dispatch Status, Delivery Performance |
| Sales Team | Product Availability |
| Customer Support | Delayed Orders, Incorrect Deliveries |
| Finance | Inventory Value, Carrying Cost |


## Validation Reminder

The metrics and data requirements above are initial thoughts only and must be validated during the subsequent DAPM phases before implementation.

---

---

## Phase 3 – Business Requirements

### Analytical Thinking

- Stakeholders consume different business information but rely on a common operational dataset.
- A shared analytics layer can generate reusable metrics for multiple stakeholders.
- Dashboard design should be role-based rather than data-source-based.
- Common metrics should be calculated once and reused across multiple reports and dashboards.
- Data discovery should focus on identifying tables and columns required to satisfy stakeholder requirements.

---

### Navigating Documents

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
