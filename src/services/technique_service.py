from db.models.technique_model import Technique
from services.base_service import BaseService


class TechniqueService(BaseService[Technique]):
    """Service for handling Technique entities."""

    def __init__(self):
        super().__init__(Technique)
