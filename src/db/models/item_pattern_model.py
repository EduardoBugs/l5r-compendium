from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class ItemPattern(Base):
    """Represents item crafting patterns."""

    __tablename__ = "l5r_item_pattern"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    foundry_id: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    book: Mapped[str] = mapped_column(String, ForeignKey("l5r_books.code"), nullable=False)
    page: Mapped[int] = mapped_column(Integer, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)

    # ORM relationship
    book_ref: Mapped["Book"] = relationship(back_populates="item_patterns")

    def __repr__(self) -> str:
        return f"<ItemPattern(name='{self.name}', book='{self.book}')>"