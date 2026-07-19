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