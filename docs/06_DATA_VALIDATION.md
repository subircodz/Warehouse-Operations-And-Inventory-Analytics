# Data Validation

## Objective

The objective of this phase is to evaluate the quality of the collected datasets before they are used for data cleaning, exploratory analysis, and business reporting.

Rather than relying on a single validation method, the same dataset is assessed using three independent analytical approaches. This provides multiple perspectives on the data and demonstrates practical proficiency with commonly used data analytics tools.

---

## Validation Strategy

The validation process is divided into three stages.

| Validation Method | Purpose | Status |
|-------------------|---------|:------:|
| Spreadsheet | Initial visual inspection and manual validation | ✅ Completed |
| SQL | Verify integrity, relationships, and business rules | ⏳ Pending |
| Python (Pandas) | Programmatic quality assessment and automation | ⏳ Pending |

Each stage validates the same source dataset using techniques appropriate to the selected tool.

---

## Validation Workflow

```text
                Raw Dataset
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
 Spreadsheet       SQL         Python
 Validation     Validation    Validation
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
            Consolidated Findings
                     │
                     ▼
             Data Cleaning Phase
```

---

## Validation Artifacts

| Artifact | Description |
|----------|-------------|
| Spreadsheet Validation | Visual inspection and worksheet-level validation |
| SQL Validation | Relational integrity and business rule validation |
| Python Validation | Automated validation using Pandas |

---

## Current Progress

| Validation Stage | Status |
|------------------|:------:|
| Spreadsheet Validation | ✅ Completed |
| SQL Validation | ⏳ Pending |
| Python Validation | ⏳ Pending |

---

## Deliverables

By the end of this phase, the following artifacts will be available:

- Spreadsheet Validation Report
- SQL Validation Report
- Python Validation Report
- Consolidated Data Validation Summary

---

## Navigation

| Document | Link |
|----------|------|
| Spreadsheet Validation | [Spreadsheet Validation](../src/01-spreadsheet/README.md) |
| SQL Validation | ⏳ [SQL Validation](02-sql/README.md) |
| Python Validation |  ⏳ [Python Validation](03-python/README.md) |
| Data Discovery | [Data Discovery](../05_DATA_DISCOVERY.md) |
| Data Cleaning | *Available in the next phase* |