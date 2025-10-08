from db.models import Bond
from services.base_service import BaseService


class BondService(BaseService[Bond]):
    """Service for L5R Bond model."""

    def __init__(self):
        super().__init__(Bond)
