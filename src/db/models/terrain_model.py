from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base


class Terrain(Base):
    __tablename__ = "l5r_terrains"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    foundry_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    book: Mapped[str] = mapped_column(String, ForeignKey("l5r_books.code"), nullable=False)
    page: Mapped[int | None] = mapped_column(Integer)
    description: Mapped[str | None] = mapped_column(String)

    book_ref: Mapped["Book"] = relationship(back_populates="terrains")

    def __repr__(self) -> str:
        return f"<Terrain(name='{self.name}', book='{self.book}')>"
