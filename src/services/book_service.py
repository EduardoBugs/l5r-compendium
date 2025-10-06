from typing import List

from db.db_connection import get_connection
from entities import Book


def get_books() -> List[Book]:
    """Fetch all books from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT code, babele_key, name FROM l5r_books ORDER BY name ASC")
    books = [Book(code=row[0], babele_key=row[1], name=row[2]) for row in cursor.fetchall()]
    conn.close()

    return books
