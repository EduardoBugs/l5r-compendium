from db.models import Boon
from services.base_service import BaseService


class BoonService(BaseService[Boon]):
    """Service for L5R Boon model."""

    def __init__(self):
        super().__init__(Boon)
