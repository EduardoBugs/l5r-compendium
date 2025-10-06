from typing import List

from db.db_connection import get_connection
from entities import Armor


def get_armors() -> List[Armor]:
    """Fetch all armors from the database, joining book info."""
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            a.foundry_id,
            a.name,
            a.book,
            a.page,
            a.description,
            bk.babele_key
        FROM l5r_armors a
        LEFT JOIN l5r_books bk ON bk.code = a.book
        ORDER BY a.id;
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    armors: List[Armor] = []
    for row in rows:
        (
            foundry_id,
            name,
            book,
            page,
            description,
            babele_key,
        ) = row

        armors.append(
            Armor(
                id=foundry_id,
                name=name,
                book=book,
                page=page,
                description=description,
                book_reference=babele_key,
            )
        )

    return armors
