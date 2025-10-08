from services.factory import ServiceFactory
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-bonds.json"


def _build_bond_description(bond) -> str:
    """Compose the HTML description of a Bond entry."""
    sections = []
    if bond.description:
        sections.append(f"<blockquote>{bond.description}</blockquote>")
    if bond.effects:
        sections.append(f"<h2>Effects</h2>{bond.effects}")
    if bond.bond_ability:
        sections.append(f"<h2>Ability</h2>{bond.bond_ability}")
    return "<br><br>".join(sections)


def generate_bonds_json(output_dir: str | None = None) -> None:
    """Generate a JSON file for all bond entries using ORM service."""
    service = ServiceFactory.get_service("bonds")
    bonds = service.get_all()

    entries = [
        {
            "id": bond.foundry_id,
            "name": bond.name,
            "description": _build_bond_description(bond),
            "bond_type": bond.bond_type or "",
            "source_reference": build_source_reference(bond),
        }
        for bond in bonds
    ]

    result = {
        "label": "Bonds",
        "mapping": {
            "description": "system.description",
            "source_reference": "system.source_reference",
            "bond_type": "system.bond_type",
        },
        "entries": entries,
    }

    write_json(result, OUTPUT_FILENAME, output_dir)
