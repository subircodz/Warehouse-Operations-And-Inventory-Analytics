# CSV

This folder contains CSV files provided by the client during the **Data Discovery** phase.

CSV files are commonly exported from operational systems and are frequently used for SQL, Python, Spreadsheet, and BI analysis.

## Typical Contents

- Product master
- Customer master
- Inventory
- Orders
- Deliveries
- Returns

## Example

- `products.csv`
- `inventory.csv`
- `sales_orders.csv`

> These files are considered **read-only source data**.

---

## DAPM Rule

Files in this folder represent the original data received from the client.

Do **not** modify these files directly. Any cleaned, transformed, or derived datasets should be stored separately under `data/processed/`.