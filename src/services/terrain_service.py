from db.models.terrain_model import Terrain
from services.base_service import BaseService


class TerrainService(BaseService[Terrain]):
    """Service for handling Terrain entities."""

    def __init__(self):
        super().__init__(Terrain)
