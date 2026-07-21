from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".xlsx" : "read_excel"
}
def load_data(source: str):
    """
    Load a dataset from the given source.

    Parameters
    ----------
    source : str
        Path to the dataset.

    Raises
    ------
    ValueError
        If invalid file type passed.
    FileNotFoundError
        If the source file does not exist.
    """
   
    
    if Path(source).suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {source}")
    
    if not Path(source).exists():
        raise FileNotFoundError(f"Source file not found: {source}")