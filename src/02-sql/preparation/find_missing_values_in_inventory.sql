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