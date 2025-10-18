from services.terrain_service import TerrainService
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-journal-terrain-qualities.json"


def generate_terrains_json(output_dir: str | None = None) -> None:
    """Generate JSON for all terrain qualities."""
    service = TerrainService()
    terrains = service.get_all()

    entries = {}
    for terrain in terrains:
        book_ref = (
            f"{terrain.book_ref.name} p.{terrain.page}"
            if terrain.book_ref and terrain.page
            else ""
        )
        text_html = f"<blockquote>{book_ref}</blockquote><br>{terrain.description or ''}"

        entries[terrain.name] = {
            "name": terrain.name,
            "pages": {
                f"Figure: {terrain.name}": {"name": terrain.name},
                terrain.name: {"name": terrain.name, "text": text_html},
            },
        }

    result = {
        "label": "Terrain Qualities",
        "mapping": {
            "text": "text"
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
