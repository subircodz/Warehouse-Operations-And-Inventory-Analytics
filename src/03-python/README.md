# Python Data Validation

> **Module:** Data Validation – Python  
> **Status:** 🚧 In Progress

---

## Purpose

Python validation automates the data quality checks performed during the Spreadsheet and SQL validation phases.

This module uses Python and Pandas to validate the warehouse dataset programmatically, providing a repeatable and scalable approach for assessing data quality.

No modifications are made to the source dataset during this phase.

---

# Dataset

The following datasets will be validated.

| Dataset | Description |
|----------|-------------|
| Warehouses | Warehouse master data |
| Suppliers | Supplier master data |
| Products | Product master data |
| Inventory | Inventory records |

---

# Validation Scope

The following validation checks will be implemented.

- Record count validation
- Missing value validation
- Duplicate record validation
- Identifier validation

Additional validation rules may be introduced as the project evolves.

---

# Validation Workflow

```text
Load Dataset
      │
      ▼
Record Count Validation
      │
      ▼
Missing Value Validation
      │
      ▼
Duplicate Validation
      │
      ▼
Identifier Validation
      │
      ▼
Generate Validation Report
```

---

# Project Structure

```text
03-python/
│
├── config.py                 # Project configuration
├── main.py                   # Entry point
├── requirements.txt          # Python dependencies
│
├── data/
│   └── raw/                  # Source datasets
│
├── tests/                    # Unit tests
│
├── utils/
│   ├── file_loader.py
│   ├── validators.py
│   └── report_generator.py
│
└── README.md
```

---

# Technologies

- Python
- Pandas
- Pytest

---

# Current Progress

The project structure has been created.

Current development focuses on:

- File loading
- Configuration management
- Unit testing
- Validation framework

Individual validation functions will be implemented incrementally.

---

# Planned Deliverables

| Deliverable | Status |
|-------------|:------:|
| File Loader | 🚧 |
| Validation Functions | ⏳ |
| Validation Report | ⏳ |
| Unit Tests | 🚧 |
| Documentation | 🚧 |

---

# Next Phase

Complete the validation functions and generate an automated validation report for all datasets.

---

## Navigation

| Document | Link |
|----------|------|
| Data Validation | [06_DATA_VALIDATION.md](../../docs/06_DATA_VALIDATION.md) |
| Spreadsheet Validation | [README.md](../01-spreadsheet/README.md) |
| SQL Validation | [README.md](../02-sql/README.md) |
| Data Discovery | [05_DATA_DISCOVERY.md](../../docs/05_DATA_DISCOVERY.md) |