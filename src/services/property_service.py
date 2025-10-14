from db.models.property_model import Property
from services.base_service import BaseService


class PropertyService(BaseService[Property]):
    """Service for handling Property entities."""

    def __init__(self):
        super().__init__(Property)
