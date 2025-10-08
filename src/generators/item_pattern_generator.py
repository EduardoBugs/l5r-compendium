from services.factory import ServiceFactory
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-item-patterns.json"


def generate_item_patterns_json(output_dir: str | None = None) -> None:
    """Generate JSON file for all Item Patterns."""
    service = ServiceFactory.get_service("item_patterns")
    patterns = service.get_all()

    entries = [
        {
            "id": pattern.foundry_id,
            "name": pattern.name,
            "description": pattern.description or "",
            "source_reference": build_source_reference(pattern),
        }
        for pattern in patterns
    ]

    result = {
        "label": "Item Patterns",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
