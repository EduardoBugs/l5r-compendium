from typing import List

from db.db_connection import get_connection
from entities import Boon


def get_boons() -> List[Boon]:
    """Fetch all boons from the database, joining book info."""
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            b.foundry_id,
            b.name,
            b.book,
            b.page,
            b.boon_type,
            b.description,
            bk.babele_key
        FROM l5r_boons b
        LEFT JOIN l5r_books bk ON bk.code = b.book
        ORDER BY b.id;
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    boons = []
    for row in rows:
        (foundry_id, name, book, page, boon_type, description, babele_key) = row
        boons.append(
            Boon(
                id=foundry_id,
                name=name,
                book=book,
                page=page,
                boon_type=boon_type,
                description=description,
                book_reference=babele_key,
            )
        )
    return boons
