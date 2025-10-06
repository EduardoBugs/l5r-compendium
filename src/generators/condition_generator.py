from services.condition_service import get_conditions
from utils import write_json

OUTPUT_FILENAME = "l5r5e.core-journal-conditions.json"


def generate_conditions_json(output_dir: str | None = None) -> None:
    """
    Generate a JSON file for all condition entries, formatted for FoundryVTT journal compendium.
    """

    conditions = get_conditions()

    # Nested structure to match the source JSON format
    entries = {}
    for condition in conditions:
        book_reference = (
            f"{condition.book_reference} p.{condition.page}"
            if condition.book_reference and condition.page
            else ""
        )
        text_html = f"<blockquote>{book_reference}</blockquote><br>{condition.description or ''}"

        entries[condition.name] = {
            "name": condition.name,
            "pages": {
                f"Figure: {condition.name}": {"name": condition.name},
                condition.name: {
                    "name": condition.name,
                    "text": text_html,
                },
            },
        }

    result = {
        "label": "Conditions",
        "mapping": {"text": "text"},
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
