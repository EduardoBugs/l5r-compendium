from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base

if TYPE_CHECKING:
    from db.models.book_model import Book


class Weapon(Base):
    __tablename__ = "l5r_weapons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    foundry_id: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    book: Mapped[str] = mapped_column(String, ForeignKey("l5r_books.code"), nullable=False)
    page: Mapped[int | None] = mapped_column(Integer)
    category: Mapped[str | None] = mapped_column(String)
    grip_1: Mapped[str | None] = mapped_column(String)
    grip_2: Mapped[str | None] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(String)

    book_ref: Mapped["Book"] = relationship(back_populates="weapons")

    def __repr__(self) -> str:
        return f"<Weapon(name='{self.name}', category='{self.category}', book='{self.book}')>"
