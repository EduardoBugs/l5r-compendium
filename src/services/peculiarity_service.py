from services.base_service import BaseService
from db.models.peculiarity_model import Peculiarity


class PeculiarityService(BaseService[Peculiarity]):
    """Service for managing Peculiarity entities."""

    def __init__(self):
        super().__init__(Peculiarity)
