from services.signature_scroll_service import SignatureScrollService
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-signature-scrolls.json"


def generate_signature_scrolls_json(output_dir: str | None = None) -> None:
    """Generate JSON file for all Signature Scrolls."""
    service = SignatureScrollService()
    scrolls = service.get_all()

    entries = []
    for scroll in scrolls:
        desc_html = ""

        if scroll.description:
            desc_html += f"<blockquote>{scroll.description.strip()}</blockquote>"
        if scroll.requirements:
            desc_html += f"<br><br><h2>Requirements</h2>{scroll.requirements.strip()}"
        if scroll.effects:
            desc_html += f"<br><br><h2>Effects</h2>{scroll.effects.strip()}"

        entries.append(
            {
                "id": scroll.name,
                "name": scroll.name,
                "description": desc_html,
                "source_reference": build_source_reference(scroll),
            }
        )

    result = {
        "label": "Signature Scrolls",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
