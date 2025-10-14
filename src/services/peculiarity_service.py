from db.models.peculiarity_model import Peculiarity
from services.base_service import BaseService


class PeculiarityService(BaseService[Peculiarity]):
    """Service for managing Peculiarity entities."""

    def __init__(self):
        super().__init__(Peculiarity)
