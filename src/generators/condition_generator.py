from services.factory import ServiceFactory
from utils import write_json

OUTPUT_FILENAME = "l5r5e.core-journal-conditions.json"


def generate_conditions_json(output_dir: str | None = None) -> None:
    """Generate JSON for Foundry journal-style condition entries."""
    service = ServiceFactory.get_service("conditions")
    conditions = service.get_all()

    entries = {}
    for condition in conditions:
        book_ref = (
            f"{condition.book_ref.name} p.{condition.page}"
            if condition.book_ref and condition.page
            else ""
        )
        text_html = f"<blockquote>{book_ref}</blockquote><br>{condition.description or ''}"

        entries[condition.name] = {
            "name": condition.name,
            "pages": {
                f"Figure: {condition.name}": {"name": condition.name},
                condition.name: {"name": condition.name, "text": text_html},
            },
        }

    result = {
        "label": "Conditions",
        "mapping": {"text": "text"},
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
