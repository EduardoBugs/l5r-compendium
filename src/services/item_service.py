from db.models.item_model import Item
from services.base_service import BaseService


class ItemService(BaseService[Item]):
    """Service for managing Item entities."""

    def __init__(self):
        super().__init__(Item)
