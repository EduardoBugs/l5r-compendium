from services.base_service import BaseService
from db.models.item_model import Item


class ItemService(BaseService[Item]):
    """Service for managing Item entities."""

    def __init__(self):
        super().__init__(Item)
