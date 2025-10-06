from typing import List

from db.db_connection import get_connection
from entities.condition_entity import Condition


def get_conditions() -> List[Condition]:
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            c.foundry_id,
            c.name,
            c.book,
            c.page,
            c.description,
            bk.name AS book_name
        FROM l5r_conditions c
        LEFT JOIN l5r_books bk ON bk.code = c.book
        ORDER BY c.id;
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    conditions = []
    for row in rows:
        foundry_id, name, book, page, description, book_name = row

        conditions.append(
            Condition(
                id=foundry_id,
                name=name,
                book=book,
                book_reference=book_name,
                page=page,
                description=description,
            )
        )

    return conditions
