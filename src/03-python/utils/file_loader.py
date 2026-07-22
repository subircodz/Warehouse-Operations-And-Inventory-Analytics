"""
This module is responsible for loading
supported data files.

Author: Subir Sutradhar
"""

from pathlib import Path

from readers.read_excel import read_excel


SUPPORTED_EXTENSIONS = {
    ".xlsx": read_excel,
}


def load_data(source):
    """
    Load a supported dataset.

    Args:
        source (str | Path):
            Path to the dataset.

    Returns:
        object:
            Loaded dataset.

    Raises:
        FileNotFoundError:
            If the source file does not exist.

        ValueError:
            If the file type is not supported.
    """

    source = Path(source)

    if not source.exists():
        raise FileNotFoundError(
            f"Source file not found: {source}"
        )

    extension = source.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    reader = SUPPORTED_EXTENSIONS[extension]

    return reader(source)