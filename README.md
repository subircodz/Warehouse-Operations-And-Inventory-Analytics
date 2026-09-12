# Warehouse Operations & Inventory Analytics

<p align="center">
    <img src="assets/banner.png" alt="Project Banner" width="100%">
</p>

> **A flagship Data Analytics Capstone Project demonstrating how a real business problem is approached using a structured, business-first analytics methodology.**

This repository showcases a Warehouse Operations & Inventory Analytics case study developed using the **Data Analytics Project Methodology (DAPM) v0.2.1**.

The verified implementation currently reaches **Exploratory Data Analysis (EDA)**. Business Insights, Recommendations and Executive Summary remain separate reporting phases and are not marked complete until their corresponding artifacts exist.

---

# What This Project Demonstrates

- Project Planning
- Business Understanding
- Stakeholder Analysis
- Business Requirements
- Data Discovery
- Data Profiling
- Data Cleaning
- Data Validation
- Exploratory Data Analysis

---

# Project Preview

## WAVE - Warehouse Analytics Validation Engine

<p align="center">
    <img src="assets/wave_banner.png" alt="WAVE Initializing" width="100%">
</p>

WAVE is the Python validation engine developed specifically for this project. It validates business identifiers, referential integrity and business rules before analytical processing begins.

## WAVE Validation Report

<p align="center">
    <img src="assets/validation.png" alt="Validation Summary" width="100%">
</p>

## Source Data

<p align="center">
    <img src="assets/dataset.png" alt="Warehouse Dataset" width="100%">
</p>

---

# Skills Demonstrated

## Business Analysis

- Business Understanding
- Stakeholder Analysis
- Requirement Gathering
- Business Process Analysis
- Analytical Thinking

## Data Analytics

- Data Discovery
- Data Profiling
- Data Cleaning
- Data Validation
- Exploratory Data Analysis
- Structured analytical reporting

## Software Engineering

- Python
- Pandas
- SQL
- MariaDB
- Microsoft Excel
- Modular Python Architecture
- Configuration-Driven Design
- Validation Engine Development
- Git
- GitHub

---

# Project Methodology

This project follows the **Data Analytics Project Methodology (DAPM) v0.2.1**.

## Project Workflow

```text
Project Brief
        │
        ▼
Business Understanding
        │
        ▼
Stakeholder Analysis
        │
        ▼
Business Requirements
        │
        ▼
Data Discovery
        │
        ▼
Data Profiling
        │
        ▼
Data Cleaning
        │
        ▼
Data Validation
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Business Insights       ⏳
        │
        ▼
Business Recommendations ⏳
        │
        ▼
Executive Summary       ⏳
```

## Project Principles

- Business before Technology
- Observe before Cleaning
- Clean before Validation
- Validate before Analysis
- Evidence before Recommendation

---

# Project Status Legend

| Status | Meaning |
|:------:|---------|
| ✅ | Completed |
| 🚧 | In Progress |
| ⏳ | Planned / Not yet documented |

---

# Project Documentation

| Phase | Status | Documentation |
|------|:------:|-------------|
| 01 · Project Brief | ✅ | [01_PROJECT_BRIEF.md](docs/01_PROJECT_BRIEF.md) |
| 02 · Business Understanding | ✅ | [02_BUSINESS_UNDERSTANDING.md](docs/02_BUSINESS_UNDERSTANDING.md) |
| 03 · Stakeholder Analysis | ✅ | [03_STAKEHOLDER_ANALYSIS.md](docs/03_STAKEHOLDER_ANALYSIS.md) |
| 04 · Business Requirements | ✅ | [04_BUSINESS_REQUIREMENTS.md](docs/04_BUSINESS_REQUIREMENTS.md) |
| 05 · Data Discovery | ✅ | [05_DATA_DISCOVERY.md](docs/05_DATA_DISCOVERY.md) |
| 06 · Data Profiling | ✅ | [06_DATA_PROFILING.md](docs/06_DATA_PROFILING.md) |
| 07 · Data Cleaning | ✅ | [07_DATA_CLEANING.md](docs/07_DATA_CLEANING.md) |
| 08 · Data Validation | ✅ | [08_DATA_VALIDATION.md](docs/08_DATA_VALIDATION.md) |
| 09 · Exploratory Data Analysis | ✅ | [09_EDA_REPORT.md](docs/09_EDA_REPORT.md) |
| 10 · Business Insights | ⏳ | Dedicated business-insight artifact not yet present. |
| 11 · Recommendations | ⏳ | Dedicated recommendation artifact not yet present. |
| 12 · Executive Summary | ⏳ | Dedicated executive-summary artifact not yet present. |

---

# Project Artifacts

| Document | Status | Purpose |
|----------|:------:|---------|
| [Project Summary](docs/PROJECT_SUMMARY.md) | ✅ | High-level overview of the verified project state. |
| [Observations Register](docs/OBSERVATIONS.md) | 🚧 | Records verified observations throughout the project lifecycle. |
| [Analytical Thinking Register](docs/14_ANALYTICAL_THINKING.md) | 🚧 | Records assumptions, hypotheses and analytical decisions. |
| [Phase Checklist](docs/15_PHASE_CHECKLIST.md) | ✅ | Tracks the verified DAPM phase status. |
| [Project Journal](docs/PROJECT_JOURNAL.md) | 🚧 | Records the chronological engineering and analytical journey. |

---

# Project Architecture

```text
                    Warehouse Dataset
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Spreadsheet         SQL Validation      WAVE (Python)
 Validation           & Validation          Engine
        │               Profiling             │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                  Clean & Trusted Data
                           │
                           ▼
                  Exploratory Analysis
                           │
                           ▼
              Business Reporting       ⏳
```

---

# Current Phase

## **EDA Complete — Business Reporting Pending**

The verified analytical implementation currently reaches the **Exploratory Data Analysis** phase. Inventory and product analysis modules are implemented and return structured analytical results.

The next phases are Business Insights, Recommendations and Executive Summary. These should only be marked complete after the corresponding business-facing artifacts are created and reviewed.

---

# Repository Structure

```text
Warehouse-Operations-And-Inventory-Analytics/
│
├── assets/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── src/
│   ├── 01-spreadsheet/
│   ├── 02-sql/
│   └── 03-python/
│       ├── analysis/
│       ├── preparation/
│       ├── readers/
│       ├── validators/
│       ├── reports/
│       ├── visualization/
│       ├── tests/
│       ├── utils/
│       ├── output/
│       ├── docs/
│       ├── models/
│       ├── screenshots/
│       ├── config.py
│       ├── main.py
│       └── README.md
└── README.md
```

---

# About this Repository

This repository is designed as a flagship portfolio project. It demonstrates more than technical implementation: it shows how a Data Analyst approaches a real business problem through business understanding, data preparation, validation and structured analysis.

The project combines business analysis, analytical thinking and software engineering into a single case study.

---

# License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.
