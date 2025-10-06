from typing import Optional

from pydantic import Field

from entities.base import BaseSourceEntity


class Bond(BaseSourceEntity):
    """Represents a Character Bond entity."""

    bond_type: Optional[str] = Field(None, description="Type of bond (e.g. Family, Ally, etc.).")
    effects: Optional[str] = Field(None, description="Effects of the bond.")
    bond_ability: Optional[str] = Field(None, description="Bond's unique ability or feature.")
