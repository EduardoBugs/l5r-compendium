from services.factory import ServiceFactory
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-celestial-implement-boons.json"


def generate_boons_json(output_dir: str | None = None) -> None:
    """Generate JSON file for all Celestial Implement Boons."""
    service = ServiceFactory.get_service("boons")
    boons = service.get_all()

    entries = [
        {
            "id": f"{boon.name}",
            "name": f"{boon.name}",
            "description": boon.description or "",
            "source_reference": build_source_reference(boon),
        }
        for boon in boons
    ]

    result = {
        "label": "Celestial Implement Boons",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
