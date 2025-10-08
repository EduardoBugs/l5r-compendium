from services.terrain_service import TerrainService
from utils import build_source_reference, write_json


OUTPUT_FILENAME = "l5r5e.core-journal-terrain-qualities.json"


def generate_terrains_json(output_dir: str | None = None) -> None:
    """Generate JSON for all terrain qualities."""
    service = TerrainService()
    terrains = service.get_all()

    entries = []
    for t in terrains:
        entries.append({
            "id": t.name,
            "name": t.name,
            "description": f"<blockquote>{t.description or ''}</blockquote>",
            "source_reference": build_source_reference(t),
        })

    result = {
        "label": "Terrain Qualities",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
