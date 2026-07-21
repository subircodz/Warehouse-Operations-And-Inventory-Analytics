
-- ======================================================================
-- Source: missing_values_in_products.sql
-- ======================================================================

-- ==================================
-- MISSING VALUES IN PRODUCTS
-- AUTHOR: SUBIR SUTRADHAR
-- ===================================


SELECT
    COUNT(*) AS total_products,

    SUM(product_name IS NULL) AS missing_product_name,

    SUM(supplier_id IS NULL) AS missing_supplier,

    SUM(category IS NULL) AS missing_category,

    SUM(brand IS NULL) AS missing_brand,

    SUM(unit IS NULL) AS missing_unit,

    SUM(unit_price IS NULL) AS missing_unit_price,

    SUM(status IS NULL) AS missing_status

FROM products;



-- ======================================================================
-- Source: missing_values_in_suppliers.sql
-- ======================================================================

-- ==================================
-- MISSING VALUES IN SUPPLIERS
-- AUTHOR: SUBIR SUTRADHAR
-- ===================================


SHOW TABLES;

DESC suppliers;

SELECT 
	COUNT(*) AS total_suppliers,
	SUM(supplier_code IS NULL) AS missing_supplier_code,
	SUM(supplier_name IS NULL) AS missing_supplier_name,
	SUM(city IS NULL) AS missing_supplier_city,
	SUM(phone IS NULL) AS missing_phone,
	SUM(gst_number IS NULL) AS missing_gst_number,
	SUM(status IS NULL) AS missing_status
FROM suppliers;


-- ======================================================================
-- Source: missing_values_in_warehouses.sql
-- ======================================================================

-- ==================================
-- MISSING VALUES IN WAREHOUSES
-- AUTHOR: SUBIR SUTRADHAR
-- ===================================


DESC warehouses;

SELECT 
	COUNT(*) as total_warehouses,
	SUM(warehouse_name is NULL) as missing_warehouse_name,
	SUM(city is NULL) as missing_city,
	SUM(state is NULL) as missing_state,
	SUM(warehouse_type IS NULL) as missing_warehouse_type
FROM warehouses;


-- ======================================================================
-- Source: find_missing_values_in_inventory.sql
-- ======================================================================

-- ---------------------------------------
-- FIND MISSING VALUES IN INVENTORY TABLE
-- AUTHOR: SUBIR SUTRADHAR
-- ---------------------------------------

SHOW TABLES;

DESC inventory;


-- find_missing_values_in_inventory

SELECT 
	COUNT(*) AS total_inventory,
	SUM(warehouse_id IS NULL) AS missing_warehouse_id,
	SUM(product_id IS NULL) AS missing_product_id,
	SUM(batch_number IS NULL) AS missing_batch_number,
	SUM(reorder_level IS NULL) AS missing_reorder_level,
	SUM(unit_cost IS NULL) AS missing_unit_cost,
	SUM(last_stocked_date IS NULL) AS missing_last_stock_date
FROM inventory;

