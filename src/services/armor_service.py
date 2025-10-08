from db.models import Armor
from services.base_service import BaseService


class ArmorService(BaseService[Armor]):
    """Service for L5R Armor model."""

    def __init__(self):
        super().__init__(Armor)
