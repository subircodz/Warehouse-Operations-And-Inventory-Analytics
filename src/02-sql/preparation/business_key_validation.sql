-- ---------------------------------------
-- BUSINESS KEY VALIDATION
-- AUTHOR: SUBIR SUTRADHAR
-- ---------------------------------------

SHOW TABLES;

DESC products;

-- Check for UNIQUE SUPPLIER

SELECT
    COUNT(*) AS total_products,
    COUNT(DISTINCT product_id) AS unique_product_ids,
    COUNT(DISTINCT sku) AS unique_skus,
    COUNT(DISTINCT supplier_id) AS unique_supplier
FROM products;


-- FIND DUPLICATES IN INVENTORY

DESC inventory;

SELECT
    warehouse_id,
    product_id,
    batch_number,
    COUNT(*) AS duplicate_count
FROM inventory
GROUP BY
    warehouse_id,
    product_id,
    batch_number
HAVING COUNT(*) > 1;

-- FIND DUPLICATE IN SUPPLIERS

DESC suppliers;

SELECT 
	supplier_code, 
	COUNT(*) AS duplicate_supplier
FROM 
	suppliers
GROUP BY
	supplier_code
HAVING 
	COUNT(*) > 1;

-- FIND DUPLICATE WAREHOUSES
DESC warehouses;

SELECT 
	warehouse_code,
	warehouse_name,
	warehouse_type,
	COUNT(*) AS duplicate_warehouse
FROM
	warehouses
GROUP BY 
	warehouse_code ,
	warehouse_name ,
	warehouse_type 
HAVING 
	COUNT(*) > 1;

DESC warehouses;