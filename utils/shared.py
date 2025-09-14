import tomllib
from pathlib import Path


def get_app_version() -> str:
    """
    Try to get the app version:
    1. From installed package metadata (fastproxy)
    2. Fallback to pyproject.toml
    """
    pyproject = Path(__file__).parent.parent / "pyproject.toml"
    try:
        with open(pyproject, "rb") as py_f:
            data = tomllib.load(py_f)
            return data["project"]["version"]
    except Exception:
        return "0.0.0"
