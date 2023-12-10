import os
import sys


def resource_path(relative_path: str) -> str:
    """Get the absolute path to a resource for PyInstaller"""
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller creates a temporary folder and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
