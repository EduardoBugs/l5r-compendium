from db.base import Base, engine
from generators import (
    generate_armors_json,
    generate_bonds_json,
    generate_boons_json,
    generate_conditions_json,
    generate_item_patterns_json,
    generate_items_json,
    generate_opportunities_json,
    generate_peculiarities_json,
    generate_properties_json,
    generate_school_cursus_json,
    generate_signature_scrolls_json,
    generate_techniques_json,
    generate_terrains_json,
    generate_titles_json,
    generate_weapons_json,
)


def main():
    print("🔧 Initializing L5R compendium generation with SQLAlchemy...")

    # Ensure models are bound to metadata (não executa create_all para não alterar o banco)
    Base.metadata.bind = engine

    # --- Execução de todos os geradores ---
    generate_armors_json()
    generate_bonds_json()
    generate_boons_json()
    generate_conditions_json()
    generate_item_patterns_json()
    generate_items_json()
    generate_opportunities_json()
    generate_peculiarities_json()
    generate_properties_json()
    generate_school_cursus_json()
    generate_signature_scrolls_json()
    generate_techniques_json()
    generate_terrains_json()
    generate_titles_json()
    generate_weapons_json()

    print("🎉 Geração concluída!")


if __name__ == "__main__":
    main()
