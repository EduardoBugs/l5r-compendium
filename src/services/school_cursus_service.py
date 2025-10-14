from db.models.school_cursus_model import SchoolCursus
from services.base_service import BaseService


class SchoolCursusService(BaseService[SchoolCursus]):
    """Service for handling SchoolCursus entities."""

    def __init__(self):
        super().__init__(SchoolCursus)
