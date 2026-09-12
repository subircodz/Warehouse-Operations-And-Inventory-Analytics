# PHASE 10 — VISUALIZATION

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Phase:** 10 — Visualization  
> **Status:** ✅ Completed

---

## Purpose

This phase converts the completed EDA results into reproducible, business-focused visualizations using **Matplotlib**.

The goal is not to create charts for decoration. Each visualization is designed to answer an analytical question and provide evidence for the Business Insights phase.

---

## Visualization Technology

- Python
- Pandas
- Matplotlib
- Headless rendering through the `Agg` backend

No Seaborn dependency is required.

---

## Implemented Visualizations

| Chart | Business Question |
|---|---|
| Inventory Quantity by Warehouse | How much physical inventory is held by each warehouse? |
| Inventory Value by Warehouse | Where is monetary inventory exposure concentrated? |
| Top Products by Inventory Value | Which products account for the largest inventory-value exposure? |
| Inactive Inventory Exposure | Which inactive products still tie up inventory value? |
| Product Price Distribution | How are product selling prices distributed? |
| Estimated Margin Distribution | How are estimated product margins distributed, including negative margins? |

---

## Engineering Design

Visualizations are implemented as reusable functions under:

```text
src/03-python/visualization/
├── __init__.py
└── matplotlib_visualizations.py
```

The phase orchestration is implemented in:

```text
src/03-python/phases/visualization_phase.py
```

Charts are written to:

```text
src/03-python/output/visualizations/
```

The visualization phase is also connected to `main.py`, so running the application generates the complete chart set from the loaded workbook.

---

## Reproducibility

The charts are generated directly from the validated workbook rather than manually edited images. This makes the visualization layer repeatable whenever the underlying trusted dataset changes.

---

## Phase Outcome

Phase 10 is complete when the six business-focused Matplotlib visualizations can be generated successfully from the validated workbook.

The next phase is **Business Insights**, where the visual evidence will be interpreted against the original business requirements.

---

## Navigation

| Document | Link |
|---|---|
| EDA Report | [09_EDA_REPORT.md](09_EDA_REPORT.md) |
| Business Insights | [11_BUSINESS_INSIGHTS.md](11_BUSINESS_INSIGHTS.md) |
| Phase Checklist | [15_PHASE_CHECKLIST.md](15_PHASE_CHECKLIST.md) |
| Project Summary | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |
