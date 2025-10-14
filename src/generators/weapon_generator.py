from services.weapon_service import WeaponService
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-weapons.json"


def generate_weapons_json(output_dir: str | None = None) -> None:
    """Generate a single JSON file for all weapons."""
    service = WeaponService()
    weapons = service.get_all()

    entries = []
    for w in weapons:
        entries.append(
            {
                "id": w.name,
                "name": w.name,
                "category": w.category or "",
                "grip_1": w.grip_1 or "",
                "grip_2": w.grip_2 or "",
                "description": f"<blockquote>{w.description or ''}</blockquote>",
                "source_reference": build_source_reference(w),
            }
        )

    result = {
        "label": "Weapons",
        "mapping": {
            "category": "system.category",
            "grip_1": "system.grip_1",
            "grip_2": "system.grip_2",
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
