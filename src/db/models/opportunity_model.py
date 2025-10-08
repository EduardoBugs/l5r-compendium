from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base


class Opportunity(Base):
    __tablename__ = "l5r_opportunities"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    foundry_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    book: Mapped[str] = mapped_column(ForeignKey("l5r_books.code"), nullable=False)
    page: Mapped[int | None] = mapped_column(Integer)
    description: Mapped[str | None] = mapped_column(String)

    # ORM relationship
    book_ref: Mapped["Book"] = relationship(back_populates="opportunities")

    def __repr__(self) -> str:
        return f"<Opportunity(name='{self.name}', book='{self.book}')>"