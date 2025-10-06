from typing import Optional

from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    """Base model for all L5R compendium entities."""

    id: str = Field(..., description="Foundry ID or unique identifier of the entity.")
    name: str = Field(..., description="Name of the entity.")
    description: Optional[str] = Field(None, description="Optional description of the entity.")
