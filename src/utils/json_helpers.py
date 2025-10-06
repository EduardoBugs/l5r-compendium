from entities import BaseSourceEntity


def build_source_reference(entity: BaseSourceEntity) -> dict:
    """
    Build a standardized 'source_reference' dictionary for JSON output
    using any entity that inherits from BaseSourceEntity.

    Args:
        entity (BaseSourceEntity): The entity containing book and page info.

    Returns:
        dict: {"source": str, "page": int | str}
    """
    return {
        "source": entity.book_reference or "",
        "page": entity.page or "",
    }
