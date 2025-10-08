from services.title_service import TitleService
from utils import build_source_reference, write_json
import html


OUTPUT_FILENAME = "l5r5e.core-titles.json"


def _build_cursus_table(cursus_text: str) -> str:
    """Convert cursus multi-line text into an HTML table."""
    if not cursus_text:
        return ""
    rows = cursus_text.strip().splitlines()
    table = "<table>"
    for r in rows:
        if "|" in r:
            cols = [html.escape(c.strip()) for c in r.split("|", 1)]
            table += f"<tr><td>{cols[0]}</td><td>{cols[1]}</td></tr>"
        else:
            table += f"<tr><td colspan='2'>{html.escape(r.strip())}</td></tr>"
    table += "</table>"
    return table


def _build_description(title) -> str:
    """Build full HTML description for a title entry."""
    desc = f"<blockquote>{title.description or ''}</blockquote>"
    if title.assigned_by:
        desc += f"<br><br><h2>Assign by</h2>{title.assigned_by}"
    if title.modifier:
        desc += f"<br><br><h2>Modifiers</h2>{title.modifier}"
    if title.title_ability:
        desc += f"<br><br><h2>Ability</h2>{title.title_ability}"
    if title.cursus:
        desc += f"<br><br><h2>Curriculum</h2>{_build_cursus_table(title.cursus)}"
    return desc


def generate_titles_json(output_dir: str | None = None) -> None:
    """Generate JSON for all Titles."""
    service = TitleService()
    titles = service.get_all()

    entries = []
    for t in titles:
        entries.append({
            "id": t.name,
            "name": t.name,
            "description": _build_description(t),
            "source_reference": build_source_reference(t),
        })

    result = {
        "label": "Titles",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
