from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base

if TYPE_CHECKING:
    from db.models.book_model import Book


class Technique(Base):
    __tablename__ = "l5r_techniques"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    foundry_id: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    book: Mapped[str] = mapped_column(String, ForeignKey("l5r_books.code"), nullable=False)
    page: Mapped[int | None] = mapped_column(Integer)
    technique_type: Mapped[str | None] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(String)
    activation: Mapped[str | None] = mapped_column(String)
    effects: Mapped[str | None] = mapped_column(String)
    enhancement_burst: Mapped[str | None] = mapped_column(String)
    opportunities: Mapped[str | None] = mapped_column(String)
    magnitude: Mapped[str | None] = mapped_column(String)
    form_requirement: Mapped[str | None] = mapped_column(String)

    book_ref: Mapped["Book"] = relationship(back_populates="techniques")

    def __repr__(self):
        return f"<Technique(name='{self.name}', type='{self.technique_type}', book='{self.book}')>"
