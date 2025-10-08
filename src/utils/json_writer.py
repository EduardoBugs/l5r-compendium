import json
import os
from pathlib import Path
from typing import Any, Union

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Default output directory (from .env or fallback)
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "./output"))


def ensure_output_dir(output_dir: Union[str, Path, None]) -> Path:
    """
    Ensure the given output directory exists.

    Args:
        output_dir (Union[str, Path, None]): Directory to check or create.

    Returns:
        Path: The absolute Path object of the ensured directory.
    """
    path = Path(output_dir or OUTPUT_DIR)
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_json(data: Any, filename: str, output_dir: Union[str, Path, None] = None) -> Path:
    """
    Write JSON data to a file in the specified directory.

    Args:
        data (Any): Python object to serialize as JSON.
        filename (str): Filename (e.g. 'l5r5e.core-armors.json').
        output_dir (Union[str, Path, None]): Optional custom output directory.

    Returns:
        Path: The absolute path to the generated JSON file.
    """
    path = ensure_output_dir(output_dir)
    filepath = path / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    entry_count = 0
    if isinstance(data, dict) and "entries" in data:
        entries = data["entries"]
        entry_count = len(entries) if isinstance(entries, (list, dict)) else 0

    if entry_count:
        print(f"✅ JSON file generated: {filepath.resolve()} (with {entry_count} entries)")
    else:
        print(f"✅ JSON file generated: {filepath.resolve()}")

    return filepath.resolve()


def build_source_reference(entity: Any) -> dict[str, Union[str, int]]:
    """
    Build a standardized 'source_reference' dict for any ORM entity
    that has 'book_ref' and 'page' attributes.

    Example output:
        {
            "source": "Core Rulebook",
            "page": 123
        }

    Args:
        entity (Any): SQLAlchemy ORM instance with attributes 'book_ref' and 'page'.

    Returns:
        dict[str, Union[str, int]]: Standardized source reference dictionary.
    """
    book_name = getattr(getattr(entity, "book_ref", None), "babele_key", None)
    page = getattr(entity, "page", None)

    return {
        "source": book_name or "",
        "page": page or "",
    }
