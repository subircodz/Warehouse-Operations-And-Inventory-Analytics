
-- ======================================================================
-- Source: referential_integrity_validation.sql
-- ======================================================================

-- ======================================================
-- REFERENTIAL INTEGRITY VALIDATION
-- PROJECT : SwiftMove Logistics Analytics
-- AUTHOR  : Subir Sutradhar
-- PURPOSE : Validate relationships between master and
--           transactional tables.
-- ======================================================

-- ======================================================
-- VALIDATION 1
-- Inventory records with missing Product ID
-- ======================================================

SELECT
    COUNT(*) AS missing_product_id
FROM
    inventory
WHERE
    product_id IS NULL;


-- ======================================================
-- VALIDATION 2
-- Products table with missing Primary Key
-- Expected Result : 0
-- ======================================================

SELECT
    COUNT(*) AS missing_primary_key
FROM
    products
WHERE
    product_id IS NULL;


-- ======================================================
-- VALIDATION 3
-- Orphan Inventory Records
--
-- Business Question:
-- Does every Product ID recorded in Inventory
-- exist in the Products master table?
-- ======================================================

SELECT
    COUNT(*) AS orphan_inventory_records
FROM
    inventory i
LEFT JOIN
    products p
ON
    i.product_id = p.product_id
WHERE
    i.product_id IS NOT NULL
AND
    p.product_id IS NULL;


-- ======================================================
-- OPTIONAL INVESTIGATION
-- View orphan inventory records
-- ======================================================

SELECT
    i.inventory_id,
    i.product_id,
    p.product_id AS matched_product
FROM
    inventory i
LEFT JOIN
    products p
ON
    i.product_id = p.product_id
WHERE
    i.product_id IS NOT NULL
AND
    p.product_id IS NULL;


-- ======================================================
-- VALIDATION 4
-- Products without Suppliers
--
-- Business Question:
-- Is every product assigned to a supplier?
-- ======================================================

SELECT
    COUNT(*) AS products_without_supplier
FROM
    products p
LEFT JOIN
    suppliers s
ON
    p.supplier_id = s.supplier_id
WHERE
    p.supplier_id IS NOT NULL
AND
    s.supplier_id IS NULL;


-- ======================================================
-- VALIDATION 5
-- Suppliers supplying no Products
--
-- Business Question:
-- Which suppliers exist but are not supplying
-- any products?
-- ======================================================

SELECT
    COUNT(*) AS unused_suppliers
FROM
    suppliers s
LEFT JOIN
    products p
ON
    s.supplier_id = p.supplier_id
WHERE
    p.product_id IS NULL;


-- ======================================================
-- VALIDATION 6
-- Warehouses without Inventory
--
-- Business Question:
-- Which warehouses currently have no inventory?
-- ======================================================

SELECT
    COUNT(*) AS empty_warehouses
FROM
    warehouses w
LEFT JOIN
    inventory i
ON
    w.warehouse_id = i.warehouse_id
WHERE
    i.inventory_id IS NULL;


-- ======================================================
-- OPTIONAL INVESTIGATION
-- View warehouses with no inventory
-- ======================================================

SELECT
    w.warehouse_id,
    w.warehouse_name
FROM
    warehouses w
LEFT JOIN
    inventory i
ON
    w.warehouse_id = i.warehouse_id
WHERE
    i.inventory_id IS NULL;

