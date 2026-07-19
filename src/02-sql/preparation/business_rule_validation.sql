-- ======================================================
-- BUSINESS RULE VALIDATION
-- PROJECT : SwiftMove Logistics Analytics
-- AUTHOR  : Subir Sutradhar
-- PURPOSE : Validate relationships between master and
--           transactional tables.
-- ======================================================

SELECT COUNT(*) AS negative_quantity
FROM inventory
WHERE quantity < 0;

SELECT COUNT(*) AS negative_unit_cost
FROM inventory
WHERE unit_cost < 0;

SELECT COUNT(*) AS negative_product_price
FROM products
WHERE unit_price < 0;

SELECT COUNT(*) AS negative_reorder_level
FROM inventory
WHERE reorder_level < 0;

SELECT DISTINCT status
FROM products;

SELECT DISTINCT status
FROM suppliers;

SELECT sku, COUNT(*)
FROM products
GROUP BY sku
HAVING COUNT(*) > 1;

SELECT supplier_code, COUNT(*)
FROM suppliers
GROUP BY supplier_code
HAVING COUNT(*) > 1;

SELECT warehouse_code, COUNT(*)
FROM warehouses
GROUP BY warehouse_code
HAVING COUNT(*) > 1;

SELECT
    warehouse_id,
    product_id,
    batch_number,
    COUNT(*)
FROM inventory
GROUP BY
    warehouse_id,
    product_id,
    batch_number
HAVING COUNT(*) > 1;



