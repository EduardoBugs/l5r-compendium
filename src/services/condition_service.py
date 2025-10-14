from db.models import Condition
from services.base_service import BaseService


class ConditionService(BaseService[Condition]):
    """Service for L5R Condition model."""

    def __init__(self):
        super().__init__(Condition)
