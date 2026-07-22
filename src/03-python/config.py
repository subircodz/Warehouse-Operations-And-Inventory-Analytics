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