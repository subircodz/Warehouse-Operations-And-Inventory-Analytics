import pytest

from utils.file_loader import load_data


def test_load_data_raises_file_not_found_error_for_missing_source():
    with pytest.raises(FileNotFoundError):
        load_data("warehouse.xlsx")