# PROJECT_CASE_JOURNAL

> **Case Study:** Warehouse Operations & Inventory Analytics
> **Status:** 🟢 In Progress
> **Methodology:** Data Analytics Project Methodology (DAPM)

---

# Purpose of this Journal

This journal documents the complete development of the **Warehouse Operations & Inventory Analytics** case study, beginning with business understanding and continuing through solution design, implementation, analysis, and reporting.

Unlike the README, which presents the final outcome of the project, this journal serves as a chronological record of the project's evolution. It captures business observations, assumptions, design decisions, investigations, challenges, lessons learned, and the reasoning behind both business and technical choices.

The purpose of maintaining this journal is to document not only *what* was built, but also *why* specific decisions were made throughout the project. This provides evidence of the analytical thinking, problem-solving approach, and decision-making process followed during the case study.

---

# Case Study Timeline

| Phase                                    | Status        |
| ---------------------------------------- | ------------- |
| Phase 0 – Project Vision                 | ✅ Completed   |
| Phase 1 – Business Understanding         | ✅ Completed   |
| Phase 2 – Business Modelling             | ✅ Completed   |
| Phase 3 – Business Requirements Analysis | ⏳ In Progress |
| Phase 4 – Data Discovery                 | ⏳ Pending     |
| Phase 5 – Solution Architecture          | ⏳ Pending     |
| Phase 6 – Spreadsheet Design             | ⏳ Pending     |
| Phase 7 – Database Design                | ⏳ Pending     |
| Phase 8 – Implementation                 | ⏳ Pending     |
| Phase 9 – Data Validation                | ⏳ Pending     |
| Phase 10 – Data Preparation              | ⏳ Pending     |
| Phase 11 – Feature Engineering           | ⏳ Pending     |
| Phase 12 – Exploratory Data Analysis     | ⏳ Pending     |
| Phase 13 – Business Analysis             | ⏳ Pending     |
| Phase 14 – Investigation                 | ⏳ Pending     |
| Phase 15 – Visualization                 | ⏳ Pending     |
| Phase 16 – Business Reporting            | ⏳ Pending     |
| Phase 17 – Portfolio Review              | ⏳ Pending     |

# Phase 0 — Project Vision

## Business Problem

Warehouses generate large volumes of operational data every day. Without proper analysis, organizations struggle to monitor inventory movement, supplier performance, stock shortages, product returns, defects, and overall operational efficiency.

The objective of this case study is to model a realistic warehouse environment and transform operational data into meaningful business insights that support informed decision-making.

---

## Objectives

The primary objectives of this case study are to:

* Understand warehouse operations from a business perspective.
* Develop a structured business analysis methodology before implementation.
* Design a relational database using MariaDB.
* Integrate Spreadsheet, SQL, Python, Pandas, Matplotlib, and Seaborn into a single analytical workflow.
* Apply business-first thinking throughout the project lifecycle.
* Build a portfolio-quality end-to-end analytics solution.

---

## Expected Outcome

The expected outcome of this project is a complete warehouse analytics solution that demonstrates both business understanding and technical implementation while following professional software engineering and data analytics practices.

---

# Phase 1 — Business Understanding

## Initial Business Exploration

Before designing the solution, I conducted an initial exploration of warehouse operations to understand how products move through the business, identify the stakeholders involved, and establish the operational processes that the analytics solution must support.

---

## Business Observations

### Inventory Procurement

* Inventory purchasing decisions are initiated by the retail store.
* Purchase orders are created by the retail store based on business demand.

---

### Product Supply

* Products are supplied by the warehouse.
* The purchaser is responsible for receiving the delivered products.

---

### Quality Verification

* Product quantity and quality are verified jointly by both the supplier and the purchaser to ensure that deliveries match the purchase order.

---

### Inventory Storage

Inventory follows two primary storage stages:

* Before delivery, products remain in the warehouse.
* After delivery, products become part of the retailer's inventory.

---

### Inventory Replenishment

Inventory replenishment decisions are influenced by several operational factors, including:

* Historical sales trends.
* Inventory movement.
* Manufacturing output.
* Demand from retail stores.

---

### Customer Order Fulfilment

When a customer places an order:

* Warehouse employees prepare the requested products.
* Inventory is dispatched.
* Available stock decreases accordingly.

---

### Stock Unavailability

If requested inventory is unavailable, the retail store must wait until stock is replenished.

This highlights the importance of maintaining appropriate inventory levels.

---

### Short Deliveries

If fewer products are delivered than originally ordered:

* Customer satisfaction decreases.
* Trust between the supplier and retailer is negatively affected.
* Operational delays may occur while shortages are resolved.

---

## Analyst Reflection

This initial exploration helped establish a clear understanding of how inventory flows through the warehouse environment before any technical design decisions were considered.

Rather than focusing immediately on database tables or code, I first identified the operational processes that the analytics solution must represent. This approach ensures that future technical decisions remain aligned with real business requirements.

# Phase 2 — Business Modelling

## Objective

Identify the core business entities before database design.

## Outcome

Identified candidate entities:

- Product
- Supplier
- Customer
- Purchase Order
- Employee
- Warehouse

## Key Decisions

- Database design postponed until business requirements are understood.
- Candidate entities identified but not finalized.

## Key Learnings

- Business entities are not necessarily database tables.
- Business modelling should precede database design.

## Status

✅ Completed

# Phase 3 — Business Requirements Analysis

## Objective

Identify the business decisions made by key stakeholders and determine the information required to support those decisions before designing the database or developing analytical solutions.

## Stakeholder

**Warehouse Manager**

## Outcome

The Warehouse Manager's responsibilities, decision-making process, and information requirements were identified.

### Primary Responsibilities

* Manage day-to-day warehouse operations.
* Receive inventory from suppliers.
* Monitor inventory movement.
* Coordinate warehouse staff.
* Ensure timely order dispatch.

### Business Decisions

* Can new orders be fulfilled with the available inventory?
* Is additional inventory required?
* Are enough employees available for today's workload?
* Which orders should be prioritized?

### Information Required

* Product-wise current stock.
* Stock by warehouse location.
* Products below the safety stock level.
* Employee attendance.
* Orders scheduled for dispatch.
* Incoming purchase orders.

## Key Decisions

* Business requirements will drive the database design.
* Each stakeholder will be analyzed independently before implementation.
* Technical implementation will begin only after stakeholder requirements are documented.

## Key Learnings

* Stakeholders make business decisions, not technical decisions.
* Business questions determine the information that must be collected.
* Information requirements should be identified before designing the database.

## Status

✅ Phase 3 (Warehouse Manager) Completed

# Phase 4 — Data Discovery

## Objective

Identify the data required to answer the business questions identified during the Business Requirements Analysis phase.

## Outcome

The core datasets required for the warehouse analytics solution were identified.

### Required Business Data

* Product master data
* Supplier information
* Customer information
* Employee information
* Warehouse information
* Purchase orders
* Customer orders
* Inventory transactions
* Stock levels
* Returns
* Defects

### Data Sources

* Warehouse Management System (WMS)
* Enterprise Resource Planning (ERP) System
* Spreadsheet records
* Purchase and sales documents

## Key Decisions

* Master data and transactional data will be stored separately.
* Data collection requirements will be finalized before database design.
* The identified datasets will form the basis of the relational database schema.

## Key Learnings

* Business questions determine what data needs to be collected.
* Collecting unnecessary data increases complexity without adding business value.
* Data should be identified based on business requirements rather than technical convenience.

## Deliverable

* Initial data requirements documented.

## Status

✅ Phase 4 Completed
