from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base

if TYPE_CHECKING:
    from db.models.book_model import Book


class SchoolCursus(Base):
    __tablename__ = "l5r_school_cursus"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    foundry_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    book: Mapped[str] = mapped_column(String, ForeignKey("l5r_books.code"), nullable=False)
    page: Mapped[int | None] = mapped_column(Integer)
    rank_1: Mapped[str | None] = mapped_column(String)
    rank_2: Mapped[str | None] = mapped_column(String)
    rank_3: Mapped[str | None] = mapped_column(String)
    rank_4: Mapped[str | None] = mapped_column(String)
    rank_5: Mapped[str | None] = mapped_column(String)

    # ORM relationship
    book_ref: Mapped["Book"] = relationship(back_populates="school_cursus")

    def __repr__(self) -> str:
        return f"<SchoolCursus(name='{self.name}', book='{self.book}')>"
