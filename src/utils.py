import os
from pathlib import Path


def from_current_file(path: str) -> Path:
    """Makes path relative to the current file

    Args:
        path (str): filesystem path

    Returns:
        Path: path relative to the current file
    """
    dirname = os.path.dirname(__file__)
    return Path(os.path.join(dirname, path)).absolute()
