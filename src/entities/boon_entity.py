from typing import Optional

from pydantic import Field

from entities.base import BaseSourceEntity


class Boon(BaseSourceEntity):
    """Represents a Celestial Boon entity."""

    boon_type: Optional[str] = Field(
        None, description="Type of boon (e.g., 'Blessing', 'Curse', etc.)."
    )
