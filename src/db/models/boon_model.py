from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class Boon(Base):
    """Represents a Celestial Implement Boon."""

    __tablename__ = "l5r_boons"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    foundry_id: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    book: Mapped[str] = mapped_column(String, ForeignKey("l5r_books.code"), nullable=False)
    page: Mapped[int] = mapped_column(Integer, nullable=True)
    boon_type: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)

    # ORM relationship
    book_ref: Mapped["Book"] = relationship(back_populates="boons")

    def __repr__(self) -> str:
        return f"<Boon(name='{self.name}', book='{self.book}')>"