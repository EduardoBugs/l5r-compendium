from typing import List

from db.db_connection import get_connection
from entities import Bond


def get_bonds() -> List[Bond]:
    """Fetch all bonds from the database, joining book info."""
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            b.foundry_id,
            b.name,
            b.bond_type,
            b.book,
            b.page,
            b.description,
            b.effects,
            b.bond_ability,
            bk.babele_key
        FROM l5r_bonds b
        LEFT JOIN l5r_books bk ON bk.code = b.book
        ORDER BY b.id;
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    bonds = []
    for row in rows:
        (
            foundry_id,
            name,
            bond_type,
            book,
            page,
            description,
            effects,
            bond_ability,
            babele_key,
        ) = row

        bonds.append(
            Bond(
                id=foundry_id,
                name=name,
                bond_type=bond_type,
                book=book,
                book_reference=babele_key,
                page=page,
                description=description,
                effects=effects,
                bond_ability=bond_ability,
            )
        )

    return bonds
