from services.school_cursus_service import SchoolCursusService
from utils import write_json, build_html_table_from_text


OUTPUT_FILENAME = "l5r5e.core-journal-school-curriculum.json"


def _build_rank_table(rank_text: str | None, rank_number: int) -> str:
    """Convert a rank_X text block into HTML table rows."""
    if not rank_text:
        return ""

    rows = ""
    for line in rank_text.strip().splitlines():
        if "|" in line:
            left, right = [part.strip() for part in line.split("|", 1)]
            rows += f"<tr><td>{left}</td><td>{right}</td></tr>"
    return f"<tr><th colspan=\"2\"><h2>Rank {rank_number}</h2></th></tr>{rows}"


def _build_cursus_html(cursus) -> str:
    """Build the HTML description for a single school cursus."""
    book_info = f"<blockquote>{cursus.book.title()} Rulebook p.{cursus.page}</blockquote>"
    table_content = "".join(
        _build_rank_table(getattr(cursus, f"rank_{i}"), i) for i in range(1, 6)
    )
    return f"{book_info}<table>{table_content}</table>"


def generate_school_cursus_json(output_dir: str | None = None) -> None:
    """Generate JSON file for all school cursus entries."""
    service = SchoolCursusService()
    cursus_list = service.get_all()

    entries = {}
    for cursus in cursus_list:
        html_content = _build_cursus_html(cursus)
        entries[cursus.name] = {
            "name": cursus.name,
            "pages": {
                f"Figure: {cursus.name}": {"name": cursus.name},
                cursus.name: {"name": cursus.name, "text": html_content},
            },
        }

    result = {
        "label": "School Curriculum",
        "mapping": {"text": "text"},
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
