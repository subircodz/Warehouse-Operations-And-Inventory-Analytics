/*
============================================================
Duplicate Record Validation
Project : Warehouse Operations & Inventory Analytics
Purpose : Identify duplicate records across business tables.
============================================================
*/

-- =========================================================
-- Products
-- Duplicate Product IDs
-- =========================================================

SELECT
    product_id,
    COUNT(*) AS duplicate_count
FROM products
GROUP BY product_id
HAVING COUNT(*) > 1;


-- =========================================================
-- Suppliers
-- Duplicate Supplier IDs
-- =========================================================

SELECT
    supplier_id,
    COUNT(*) AS duplicate_count
FROM suppliers
GROUP BY supplier_id
HAVING COUNT(*) > 1;


-- =========================================================
-- Warehouses
-- Duplicate Warehouse IDs
-- =========================================================

SELECT
    warehouse_id,
    COUNT(*) AS duplicate_count
FROM warehouses
GROUP BY warehouse_id
HAVING COUNT(*) > 1;


-- =========================================================
-- Inventory
-- Duplicate Inventory Records
-- (Product + Warehouse should normally be unique)
-- =========================================================

SELECT
    product_id,
    warehouse_id,
    COUNT(*) AS duplicate_count
FROM inventory
GROUP BY
    product_id,
    warehouse_id
HAVING COUNT(*) > 1;


-- =========================================================
-- Shipments
-- Duplicate Shipment IDs
-- =========================================================

SELECT
    shipment_id,
    COUNT(*) AS duplicate_count
FROM shipments
GROUP BY shipment_id
HAVING COUNT(*) > 1;


-- =========================================================
-- Customers
-- Duplicate Customer IDs
-- =========================================================

SELECT
    customer_id,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- =========================================================
-- Customer Complaints
-- Duplicate Complaint IDs
-- =========================================================

SELECT
    complaint_id,
    COUNT(*) AS duplicate_count
FROM customer_complaints
GROUP BY complaint_id
HAVING COUNT(*) > 1;