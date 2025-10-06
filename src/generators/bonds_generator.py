from services.bond_service import get_bonds
from utils import build_source_reference, write_json

OUTPUT_FILENAME = "l5r5e.core-bonds.json"


def _build_bond_description(bond) -> str:
    """
    Build the full HTML description for a bond entry.

    The content includes the base description (inside <blockquote>),
    followed by optional sections for Effects and Ability.
    """
    sections = []
    if bond.description:
        sections.append(f"<blockquote>{bond.description}</blockquote>")
    if bond.effects:
        sections.append(f"<h2>Effects</h2>{bond.effects}")
    if bond.bond_ability:
        sections.append(f"<h2>Ability</h2>{bond.bond_ability}")
    return "<br><br>".join(sections)


def generate_bonds_json(output_dir: str | None = None) -> None:
    """
    Generate a JSON file for all bonds, formatted for FoundryVTT.

    Args:
        output_dir (str): Directory to save the generated JSON file.
    """
    bonds = get_bonds()
    entries = []

    for bond in bonds:
        entries.append(
            {
                "id": bond.id,
                "name": bond.name,
                "description": _build_bond_description(bond),
                "source_reference": build_source_reference(bond),
                "bond_type": bond.bond_type,
            }
        )

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
