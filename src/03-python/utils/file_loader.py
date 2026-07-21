from pathlib import Path


def load_data(source: src): # type: ignore
    """
    Load a dataset from the given source.

    Parameters
    ----------
    source : str
        Path to the dataset.

    Raises
    ------
    FileNotFoundError
        If the source file does not exist.
    """

    if not Path(source).exists():
        raise FileNotFoundError(f"Source file not found: {source}")