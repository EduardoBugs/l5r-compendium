from services.base_service import BaseService
from db.models.opportunity_model import Opportunity


class OpportunityService(BaseService[Opportunity]):
    """Service for managing Opportunity entities."""

    def __init__(self):
        super().__init__(Opportunity)
