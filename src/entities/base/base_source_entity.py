from typing import Optional

from pydantic import Field

from entities.base.base_entity import BaseEntity


class BaseSourceEntity(BaseEntity):
    """Base model for entities that reference a book source."""

    book: str = Field(..., description="Book code where the entity is found.")
    book_reference: Optional[str] = Field(
        None, description="Full book reference (e.g., 'Core Rulebook p.125')."
    )
    page: Optional[int] = Field(None, description="Page number in the source book.")
