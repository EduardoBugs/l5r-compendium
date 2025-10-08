from services.opportunity_service import OpportunityService
from utils import write_json

OUTPUT_FILENAME = "l5r5e.core-journal-opportunities.json"


def generate_opportunities_json(output_dir: str | None = None) -> None:
    """
    Generate a JSON file for all opportunity entries, formatted for FoundryVTT journal compendium.
    """

    service = OpportunityService()
    opportunities = service.get_all()

    entries = {}
    for opp in opportunities:
        book_reference = (
            f"{opp.book} p.{opp.page}"
            if opp.book and opp.page
            else ""
        )

        text_html = f"<blockquote>{book_reference}</blockquote><br>{opp.description or ''}"

        entries[opp.name] = {
            "name": opp.name,
            "pages": {
                f"Figure: {opp.name}": {"name": opp.name},
                opp.name: {
                    "name": opp.name,
                    "text": text_html,
                },
            },
        }

    result = {
        "label": "Opportunities",
        "mapping": {"text": "text"},
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
