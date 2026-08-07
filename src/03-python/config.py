from pathlib import Path

# ========================================
# Application Information
# ========================================

PROJECT_NAME = "Warehouse Operations & Inventory Analytics"

APPLICATION_NAME = "Warehouse Analytics Validation Engine"

APPLICATION_SHORT_NAME = "WAVE"

VERSION = "0.1.0"

AUTHOR = "Subir Sutradhar"

METHODOLOGY = "DAPM Framework v0.1.1"

# ====================================
# Project Directories
# ====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATA_DIRECTORY = PROJECT_ROOT / "data"

RAW_DATA_DIRECTORY = DATA_DIRECTORY / "raw"

# ====================================
# Workbook Path
# ====================================
EXCEL_DIRECTORY = RAW_DATA_DIRECTORY / "excel"

WORKBOOK_PATH = EXCEL_DIRECTORY / "Warehouse_Reports.xlsx"

# ====================================
# Python Root
# ====================================

PYTHON_ROOT = PROJECT_ROOT / "src" / "03-python"

# ====================================
# Output Directories
# ====================================

OUTPUT_DIRECTORY = PYTHON_ROOT / "output"

SCREENSHOTS = PYTHON_ROOT / "screenshots"

# SCREENSHOT_DIRECTORY

# LOG_LEVEL

# ENCODING

ENVIRONMENT = "Development"

# ====================================
# BUSINESS Identifiers
# ====================================


IDENTIFIER_PATTERNS = {
    "products": {
        "column": "sku",
        "prefix": "SKU",
        "numeric_length": 5
    },

    "suppliers": {
        "column": "supplier_code",
        "prefix": "SUP",
        "numeric_length": 4
    },

    "warehouses": {
        "column": "warehouse_code",
        "prefix": "WH",
        "numeric_length": 3
    }
}

# ====================================
# Refertila rules
# ====================================

REFERENTIAL_INTEGRITY_RULES = [
    {
        "parent_worksheet": "suppliers",
        "parent_column": "supplier_id",
        "child_worksheet": "products",
        "child_column": "supplier_id",
    },
    {
        "parent_worksheet": "products",
        "parent_column": "product_id",
        "child_worksheet": "inventory",
        "child_column": "product_id",
    },
    {
        "parent_worksheet": "warehouses",
        "parent_column": "warehouse_id",
        "child_worksheet": "inventory",
        "child_column": "warehouse_id",
    },
]


# ================================================
# Business rules
# ================================================

BUSINESS_RULES = {
    "inventory": {
        "column": ["quantity", "reorder", "unit_cost"]
    },

    "products": {
        "column": ["unit_price", "status"]
    }
}

# ================================================
# Text standardization rules
# ================================================
TEXT_STANDARDIZATION_RULES = {
    "city": "title",
    "state": "title",
    "supplier_name": "title",
    "warehouse_name": "title",
    "product_name": "title",
    "brand": "title",
    "category": "title",
    "status": "upper",
    "email": "lower",
    "warehouse_code": None,
    "supplier_code": None,
    "sku": None,
    "gst_number": None,
}