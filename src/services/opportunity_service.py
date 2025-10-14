from db.models.opportunity_model import Opportunity
from services.base_service import BaseService


class OpportunityService(BaseService[Opportunity]):
    """Service for managing Opportunity entities."""

    def __init__(self):
        super().__init__(Opportunity)
