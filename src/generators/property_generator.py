from services.property_service import PropertyService
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-properties.json"


def generate_properties_json(output_dir: str | None = None) -> None:
    """Generate JSON file for all item properties."""
    service = PropertyService()
    properties = service.get_all()

    entries = []
    for prop in properties:
        entries.append(
            {
                "id": prop.name,
                "name": prop.name,
                "description": prop.description or "",
                "source_reference": build_source_reference(prop),
            }
        )

    result = {
        "label": "Properties",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
