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
