from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db import Base, get_session

T = TypeVar("T", bound=Base)


class BaseService(Generic[T]):
    """
    Generic CRUD service for SQLAlchemy models.
    Provides basic ORM operations for derived services.
    """

    def __init__(self, model: Type[T]):
        self.model = model

    def get_all(self, preload: bool = True) -> List[T]:
        """
        Retrieve all records for the model.
        Optionally preloads relationships using selectinload.
        """
        with get_session() as session:
            stmt = select(self.model).order_by(self.model.id)
            if preload:
                stmt = stmt.options(selectinload("*"))
            return session.scalars(stmt).all()

    def get_by_id(self, record_id: int) -> Optional[T]:
        """Fetch a single record by its primary key."""
        with get_session() as session:
            return session.get(self.model, record_id)

    def add(self, obj: T) -> T:
        """Insert a new record and commit."""
        with get_session() as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)
            return obj

    def delete(self, record_id: int) -> bool:
        """Delete a record by ID. Returns True if deleted."""
        with get_session() as session:
            record = session.get(self.model, record_id)
            if not record:
                return False
            session.delete(record)
            session.commit()
            return True
