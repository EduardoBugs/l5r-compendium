import html
from typing import Optional


def build_html_table_from_text(text: Optional[str], header: Optional[str] = None) -> str:
    """
    Converts a multi-line 'pipe-separated' text block into an HTML table.

    Example input:
        "Command | Skill\nMedicine | Skill\n@techgrp[kata|Rank 1 Kata] | Tech. Grp."

    Output:
        <table><tr><td>Command</td><td>Skill</td></tr>...</table>

    Args:
        text (str | None): Input text block.
        header (str | None): Optional header (e.g. 'Rank 1').

    Returns:
        str: HTML string containing <table>...</table> markup.
    """
    if not text:
        return ""

    rows_html = ""
    for line in text.strip().splitlines():
        if "|" in line:
            cols = [html.escape(col.strip()) for col in line.split("|", 1)]
            rows_html += f"<tr><td>{cols[0]}</td><td>{cols[1]}</td></tr>"
        else:
            # Fallback for malformed lines
            rows_html += f"<tr><td colspan='2'>{html.escape(line.strip())}</td></tr>"

    if header:
        header_row = f"<tr><th colspan='2'><h2>{html.escape(header)}</h2></th></tr>"
        rows_html = header_row + rows_html

    return f"<table>{rows_html}</table>"
