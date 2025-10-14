from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base

if TYPE_CHECKING:
    from db.models import (
        Armor,
        Bond,
        Boon,
        Condition,
        Item,
        ItemPattern,
        Opportunity,
        Peculiarity,
        Property,
        SchoolCursus,
        SignatureScroll,
        Technique,
        Terrain,
        Title,
        Weapon,
    )


class Book(Base):
    __tablename__ = "l5r_books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    babele_key: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)

    # --- Back-populated relationships ---
    armors: Mapped[list["Armor"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    bonds: Mapped[list["Bond"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    boons: Mapped[list["Boon"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    conditions: Mapped[list["Condition"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    item_patterns: Mapped[list["ItemPattern"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    items: Mapped[list["Item"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    opportunities: Mapped[list["Opportunity"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    peculiarities: Mapped[list["Peculiarity"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    properties: Mapped[list["Property"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    school_cursus: Mapped[list["SchoolCursus"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    signature_scrolls: Mapped[list["SignatureScroll"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    techniques: Mapped[list["Technique"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    terrains: Mapped[list["Terrain"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    titles: Mapped[list["Title"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )
    weapons: Mapped[list["Weapon"]] = relationship(
        back_populates="book_ref", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Book(name='{self.name}', code='{self.code}')>"
