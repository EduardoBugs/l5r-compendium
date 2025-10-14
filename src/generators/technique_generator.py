import os

from services.technique_service import TechniqueService
from utils import build_source_reference, write_json

from utils import log

def _build_description_html(t):
    html = t.description.strip() if t.description else ""

    if t.activation:
        html += f"<br><br><h2>Activation</h2>{t.activation.strip()}"
    if t.effects:
        html += f"<br><br><h2>Effects</h2>{t.effects.strip()}"
    if t.enhancement_burst:
        html += f"<br><br><h2>Enhancement & Burst Effects</h2>{t.enhancement_burst.strip()}"
    if t.opportunities:
        html += f"<br><br><h2>Opportunities & New Opportunities</h2>{t.opportunities.strip()}"
    if t.magnitude:
        html += f"<br><br><h2>Magnitude</h2>{t.magnitude.strip()}"

    return html


def generate_techniques_json(output_dir: str | None = None):
    """Generate one JSON file per technique type."""
    service = TechniqueService()
    techniques = service.get_all()

    grouped = {}
    for t in techniques:
        if not t.technique_type:
            continue
        grouped.setdefault(t.technique_type.lower(), []).append(t)

    log.stage("Generating Techniques")

    for technique_type, items in grouped.items():
        entries = []
        for t in items:
            entries.append(
                {
                    "id": t.name,
                    "name": t.name,
                    "description": _build_description_html(t),
                    "source_reference": build_source_reference(t),
                }
            )

        result = {
            "label": f"Techniques {technique_type.capitalize()}",
            "mapping": {
                "description": "system.description",
                "source_reference": "system.source_reference",
            },
            "entries": entries,
        }

        filename = f"l5r5e.core-techniques-{technique_type}.json"
        write_json(result, filename, output_dir or os.path.join("output"))

    log.stage_end()