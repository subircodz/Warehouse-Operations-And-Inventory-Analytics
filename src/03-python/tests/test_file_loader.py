import pytest

from utils.file_loader import load_data

# source file missing case
def test_load_data_raises_file_not_found_error_for_missing_source():
    with pytest.raises(FileNotFoundError):
        load_data("warehouse.xlsx")

# Invalid file type
def test_load_data_raises_value_error_for_unsupported_extension():
    with pytest.raises(ValueError, match="Unsupported file type"):
        load_data("warehouse.pdf")