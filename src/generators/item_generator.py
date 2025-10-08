from services.item_service import ItemService
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-items.json"


def generate_items_json(output_dir: str | None = None) -> None:
    """
    Generate JSON file for all items.
    """
    service = ItemService()
    items = service.get_all()

    entries = []
    for item in items:
        entries.append(
            {
                "id": item.name,
                "name": item.name,
                "description": item.description or "",
                "source_reference": build_source_reference(item),
            }
        )

    result = {
        "label": "Items",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
