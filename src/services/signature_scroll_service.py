from db.models.signature_scroll_model import SignatureScroll
from services.base_service import BaseService


class SignatureScrollService(BaseService[SignatureScroll]):
    """Service for handling SignatureScroll entities."""

    def __init__(self):
        super().__init__(SignatureScroll)
