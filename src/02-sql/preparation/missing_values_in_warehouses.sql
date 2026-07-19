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