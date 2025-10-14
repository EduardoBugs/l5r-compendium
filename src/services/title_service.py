from db.models.title_model import Title
from services.base_service import BaseService


class TitleService(BaseService[Title]):
    """Service for handling Title entities."""

    def __init__(self):
        super().__init__(Title)
