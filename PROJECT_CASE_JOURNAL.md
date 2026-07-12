# PROJECT_CASE_JOURNAL

> **Case Study:** Warehouse Operations & Inventory Analytics
> **Status:** 🟢 In Progress  
> **Methodology:** Data Analytics Project Methodology (DAPM)  

---

# Purpose of this Journal

This journal documents the complete journey of this case study from the initial business problem through business understanding, modelling, design decisions, implementation, analysis, and final reporting.

Unlike the README, this document is intended to evolve throughout the project. It records important discussions, assumptions, design decisions, challenges, lessons learned, and the reasoning behind technical and business choices.

---

# Case Study Timeline

| Phase                                    | Status      |
| ---------------------------------------- | ----------- |
| Phase 0 - Project Vision                 | ✅ Completed |
| Phase 1 - Business Understanding         | ✅ Completed |
| Phase 2 - Business Modelling             | ✅ Completed |
| Phase 3 - Business Requirements Analysis | ⏳ Pending   |
| Phase 4 - Data Discovery                 | ⏳ Pending   |
| Phase 5 - Solution Architecture          | ⏳ Pending   |
| Phase 6 - Spreadsheet Design             | ⏳ Pending   |
| Phase 7 - Database Design                | ⏳ Pending   |
| Phase 8 - Implementation                 | ⏳ Pending   |
| Phase 9 - Data Validation                | ⏳ Pending   |
| Phase 10 - Data Preparation              | ⏳ Pending   |
| Phase 11 - Feature Engineering           | ⏳ Pending   |
| Phase 12 - Exploratory Data Analysis     | ⏳ Pending   |
| Phase 13 - Business Analysis             | ⏳ Pending   |
| Phase 14 - Investigation                 | ⏳ Pending   |
| Phase 15 - Visualization                 | ⏳ Pending   |
| Phase 16 - Business Reporting            | ⏳ Pending   |
| Phase 17 - Portfolio Review              | ⏳ Pending   |

---

# Phase 0 — Project Vision

## Business Problem

Warehouses generate large volumes of operational data every day. Without proper analysis, organizations struggle to understand inventory movement, supplier performance, stock shortages, returns, defects, and overall warehouse efficiency.

This case study aims to model a realistic warehouse environment and transform operational data into meaningful business insights.

---

## Objectives

* Learn business modelling from a warehouse perspective.
* Design a professional analytics workflow.
* Build a relational database using MariaDB.
* Integrate Spreadsheet, SQL, Python, Pandas, Matplotlib and Seaborn.
* Apply business-first thinking before technical implementation.
* Produce a portfolio-quality case study.

---

## Expected Outcome

Develop an end-to-end warehouse analytics solution that demonstrates both business understanding and technical implementation.

---

# Phase 1 — Business Understanding

## Initial Business Discussion

The following business questions were explored before any technical design.

### Who decides to buy inventory?

Retail Store

### Who places the purchase order?

Retail Store

### Who supplies the products?

Warehouse

### Who receives the products?

Purchaser

### Who verifies quantity and quality?

Both supplier and purchaser.

### Where is inventory stored?

* Before delivery → Warehouse
* After delivery → Retail Store

### How is stock replenished?

Based on previous sales trends, inventory movement, manufacturing output and retailer demand.

### What happens when a customer places an order?

Employees prepare the requested products and inventory decreases accordingly.

### What happens if inventory is unavailable?

The retailer waits until stock becomes available.

### What happens if fewer products are delivered than ordered?

Poor customer satisfaction and reduced trust between supplier and retailer.

---

# Phase 2 — Business Modelling

## Initial Entity Discovery

The following business entities were identified during discussion.

### Candidate Entities

* Product
* Supplier
* Customer
* Purchase Order
* Invoice
* Returns
* Defects
* Employee
* Warehouse
* Department
* Category

---

## Important Design Discussion

One of the earliest modelling discussions focused on the design of Purchase Orders.

Initial assumption:

> Purchase Order alone may be sufficient.

Discussion explored:

* Multiple products within a single purchase order.
* Database granularity.
* One business document versus multiple business facts.
* Header and line-item modelling.
* Relational database design considerations.

No implementation decision has been finalized yet. The discussion will continue during the database design phase.

---

## Important Learning

A business entity and a database table are not always identical.

Business concepts must first be understood before deciding how they should be represented in a relational database.

---

# Design Principles Established

The following principles will be followed throughout this project.

* Business-first thinking.
* Professional folder organization.
* Modular architecture.
* Configuration-driven design.
* Type hints.
* Proper documentation.
* Small reusable functions.
* Clean Git history.
* Meaningful commit messages.
* Continuous documentation.
* Professional storytelling.
* Evidence-driven development.

---

# Lessons Learned So Far

* Understanding the business is more important than writing code.
* Business modelling should happen before database design.
* Database decisions should be justified, not memorized.
* Challenging architectural decisions improves understanding.
* Documentation should evolve alongside the project.
* The README will summarize the project; this journal will preserve its complete journey.

---

# Pending Next Phase

## Phase 3 — Business Requirements Analysis

Next objective:

Determine what business decisions stakeholders want to make, identify analytical questions, define KPIs, and establish the business value that the analytics solution should provide.

---

## Journal Revision History

### Version 0.1

* Project initialized.
* Business understanding documented.
* Business modelling discussions recorded.
* Initial methodology established.
* Journal structure created.
