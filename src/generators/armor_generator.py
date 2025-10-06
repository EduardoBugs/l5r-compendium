from services.armor_service import get_armors
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-armors.json"


def generate_armors_json(output_dir: str | None = None) -> None:
    """
    Generate a JSON file for all armor entries, formatted for FoundryVTT.

    Args:
        output_dir (str | None): Directory to save the generated JSON file.
    """
    armors = get_armors()

    entries = []
    for armor in armors:
        entries.append(
            {
                "id": armor.id,
                "name": armor.name,
                "description": armor.description or "",
                "source_reference": build_source_reference(armor),
            }
        )

    result = {
        "label": "Armors",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
