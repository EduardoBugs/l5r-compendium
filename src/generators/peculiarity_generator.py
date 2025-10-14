import os

from services.peculiarity_service import PeculiarityService
from utils import build_source_reference, write_json

from utils import log

# --- Nome dos arquivos por tipo ---
PECULIARITY_FILE_MAP = {
    "distinction": "l5r5e.core-peculiarities-distinctions.json",
    "passion": "l5r5e.core-peculiarities-passions.json",
    "adversity": "l5r5e.core-peculiarities-adversities.json",
    "anxiety": "l5r5e.core-peculiarities-anxieties.json",
}


def _build_description(p) -> str:
    """Build formatted HTML description block."""
    description = f"<blockquote>{p.description or ''}</blockquote>"
    if p.effects:
        description += f"<br><br><h2>Effects</h2>{p.effects}"
    return description


def generate_peculiarities_json(output_dir: str | None = None) -> None:
    """
    Generate one JSON per peculiarity type (Distinction, Passion, Adversity, Anxiety).
    Uses a static mapping to ensure proper file naming.
    """
    service = PeculiarityService()
    peculiarities = service.get_all()

    # Agrupar por tipo
    grouped = {}
    for p in peculiarities:
        if not p.peculiarity_type:
            continue
        key = p.peculiarity_type.strip().lower()
        grouped.setdefault(key, []).append(p)

    log.stage("Generating Peculiarities")

    for pec_type, items in grouped.items():
        filename = PECULIARITY_FILE_MAP.get(pec_type)
        if not filename:
            print(f"⚠️ Tipo de peculiaridade não mapeado: {pec_type}")
            continue

        entries = []
        for p in items:
            entries.append(
                {
                    "id": p.name,
                    "name": p.name,
                    "types": p.types or "",
                    "description": _build_description(p),
                    "source_reference": build_source_reference(p),
                }
            )

        result = {
            "label": pec_type.capitalize(),
            "mapping": {
                "types": "system.types",
                "description": "system.description",
                "source_reference": "system.source_reference",
            },
            "entries": entries,
        }

        write_json(result, filename, output_dir or os.path.join("output"))

    log.stage_end()
