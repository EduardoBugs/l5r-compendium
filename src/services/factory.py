from typing import Type

from db.models import (
    Armor,
    Bond,
    Book,
    Boon,
    Condition,
    Item,
    ItemPattern,
    Opportunity,
    Peculiarity,
)
from services import (
    ArmorService,
    BondService,
    BookService,
    BoonService,
    ConditionService,
    ItemPatternService,
    ItemService,
    OpportunityService,
    PeculiarityService,
)
from services.base_service import BaseService


class ServiceFactory:
    """Factory class to instantiate services dynamically based on model name."""

    _registry = {
        "books": (Book, BookService),
        "armors": (Armor, ArmorService),
        "bonds": (Bond, BondService),
        "boons": (Boon, BoonService),
        "conditions": (Condition, ConditionService),
        "item_patterns": (ItemPattern, ItemPatternService),
        "items": (Item, ItemService),
        "opportunities": (Opportunity, OpportunityService),
        "peculiarities": (Peculiarity, PeculiarityService),
    }

    @staticmethod
    def get_service(name: str) -> BaseService:
        """
        Retrieve a service instance by key name.

        Args:
            name (str): One of ['books', 'armors', 'bonds', 'boons', 'conditions', 'item_patterns']

        Returns:
            BaseService: Instantiated service.
        """
        entry = ServiceFactory._registry.get(name.lower())
        if not entry:
            raise ValueError(f"❌ Unknown service: {name}")
        _, service_class = entry
        return service_class()

    @staticmethod
    def get_model(name: str) -> Type:
        """Retrieve model class by key name."""
        entry = ServiceFactory._registry.get(name.lower())
        if not entry:
            raise ValueError(f"❌ Unknown model: {name}")
        model_class, _ = entry
        return model_class
