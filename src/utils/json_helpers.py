from typing import Any, Dict


def build_source_reference(entity: Any) -> Dict[str, str | int]:
    """
    Build a standardized 'source_reference' dictionary for JSON output.

    Works with both SQLAlchemy ORM models and Pydantic entities
    that include 'book_ref' or 'book_reference' and 'page' attributes.

    Args:
        entity: ORM or Pydantic entity containing book info and page.

    Returns:
        dict: {"source": str, "page": int | str}
    """
    # Try to get reference from ORM relationship
    if hasattr(entity, "book_ref") and getattr(entity, "book_ref") is not None:
        book_name = getattr(entity.book_ref, "babele_key", "")
        source = f"{book_name}".strip()
    # Fallback for Pydantic-style 'book_reference'
    elif hasattr(entity, "book_reference"):
        source = getattr(entity, "book_reference", "")
    else:
        source = ""

    page = getattr(entity, "page", "") or ""
    return {"source": source, "page": page}
