from db.models import ItemPattern
from services.base_service import BaseService


class ItemPatternService(BaseService[ItemPattern]):
    """Service for L5R ItemPattern model."""

    def __init__(self):
        super().__init__(ItemPattern)
