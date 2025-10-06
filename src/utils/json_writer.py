import json
import os
from typing import Any

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Default output directory for generated JSON files
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output")


def ensure_output_dir(output_dir: str) -> None:
    """
    Ensure the output directory exists.

    If the directory does not exist, it will be created.
    """
    os.makedirs(output_dir, exist_ok=True)


def write_json(data: Any, filename: str, output_dir: str | None = None) -> str:
    """
    Write a JSON file to the specified output directory.

    Args:
        data (Any): The Python object (dict, list, etc.) to serialize as JSON.
        filename (str): The name of the file to write (e.g., "l5r5e.core-bonds.json").
        output_dir (str | None): Optional. Output directory path. If not provided,
                                 uses the default OUTPUT_DIR from .env.

    Returns:
        str: The full file path of the generated JSON file.
    """
    # Use the default output directory if none is provided
    output_dir = output_dir or OUTPUT_DIR

    # Make sure the output directory exists
    ensure_output_dir(output_dir)

    # Construct the full file path
    filepath = os.path.join(output_dir, filename)

    # Write JSON file with UTF-8 encoding and pretty formatting
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON file generated successfully: {filepath}")
    return filepath
