"""
Entities package for L5R compendium data models.

Each entity represents a specific domain object mapped from SQLite tables.
All entities inherit from Pydantic's BaseModel for type validation,
structured serialization, and compatibility with FastAPI or JSON exports.
"""

from entities.armor_entity import Armor
from entities.bond_entity import Bond
from entities.book_entity import Book
from entities.boon_entity import Boon
from entities.condition_entity import Condition

__all__ = ["Armor", "Bond", "Boon", "Book", "Condition"]
