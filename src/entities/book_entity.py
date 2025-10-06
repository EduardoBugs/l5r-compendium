from pydantic import BaseModel, Field


class Book(BaseModel):
    """Represents a source book for L5R content (used for cross-referencing)."""

    code: str = Field(..., description="Short code used as book identifier (e.g., 'cr', 'cofw').")
    babele_key: str = Field(
        ..., description="Key used by Foundry's Babele module for localization."
    )
    name: str = Field(..., description="Full display name of the book (e.g., 'Celestial Realms').")
