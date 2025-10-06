from services.boon_service import get_boons
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-celestial-implement-boons.json"


def generate_boons_json(output_dir: str | None = None) -> None:
    """Generate JSON file for all Boons."""
    boons = get_boons()

    entries = []
    for boon in boons:
        entries.append(
            {
                "id": f"{boon.name} [{boon.boon_type}]" if boon.boon_type else boon.name,
                "name": f"{boon.name} [{boon.boon_type}]" if boon.boon_type else boon.name,
                "description": boon.description or "",
                "source_reference": build_source_reference(boon),
            }
        )

    result = {
        "label": "Celestial Implement Boons",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
