from services.factory import ServiceFactory
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-armors.json"


def generate_armors_json(output_dir: str | None = None) -> None:
    """Generate a JSON file for all armor entries using ORM service."""
    service = ServiceFactory.get_service("armors")
    armors = service.get_all()

    entries = [
        {
            "id": armor.foundry_id,
            "name": armor.name,
            "description": armor.description or "",
            "source_reference": build_source_reference(armor),
        }
        for armor in armors
    ]

    result = {
        "label": "Armors",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
