
-- ======================================================================
-- Source: find_total_records.sql
-- ======================================================================

-- ---------------------------------------
-- FIND TOTAL RECORDS IN EACH TABLE
-- AUTHOR: SUBIR SUTRADHAR
-- ---------------------------------------

SHOW TABLES;

SELECT COUNT(*) AS total_warehouses
FROM warehouses;

SELECT COUNT(*) AS total_suppliers
FROM suppliers;

SELECT COUNT(*) AS total_products
FROM products;

SELECT COUNT(*) AS total_inventory
FROM inventory;

SELECT 'Warehouses' AS table_name, COUNT(*) AS records FROM warehouses
UNION ALL
SELECT 'Suppliers', COUNT(*) FROM suppliers
UNION ALL
SELECT 'Products', COUNT(*) FROM products
UNION ALL
SELECT 'Inventory', COUNT(*) FROM inventory;



