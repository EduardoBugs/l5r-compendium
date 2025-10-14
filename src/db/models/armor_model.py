from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base

if TYPE_CHECKING:
    from db.models.book_model import Book


class Armor(Base):
    """ORM model for armor items."""

    __tablename__ = "l5r_armors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    foundry_id: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    book: Mapped[str] = mapped_column(String, ForeignKey("l5r_books.code"), nullable=False)
    page: Mapped[int] = mapped_column(Integer, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)

    # ORM relationship
    book_ref: Mapped["Book"] = relationship(back_populates="armors")

    def __repr__(self) -> str:
        return f"<Armor(name='{self.name}', book='{self.book}')>"
