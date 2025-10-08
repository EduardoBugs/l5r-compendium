from db.models import Book
from services.base_service import BaseService


class BookService(BaseService[Book]):
    """Service for L5R Book model."""

    def __init__(self):
        super().__init__(Book)
