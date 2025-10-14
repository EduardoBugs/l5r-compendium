from typing import Optional

from pydantic import BaseModel


class BaseSourceSchema(BaseModel):
    """Shared fields for entities that come from a book source."""

    id: str
    name: str
    description: Optional[str]
    book: str
    page: Optional[int]
    book_reference: Optional[str]
