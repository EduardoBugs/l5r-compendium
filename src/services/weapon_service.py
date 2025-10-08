from db.models.weapon_model import Weapon
from services.base_service import BaseService


class WeaponService(BaseService[Weapon]):
    """Service for handling Weapon entities."""

    def __init__(self):
        super().__init__(Weapon)
