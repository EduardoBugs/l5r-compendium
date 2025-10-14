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
from utils import build_module_structure

from utils import log



def main():

    log.stage("Initializing L5R compendium generation with SQLAlchemy...")

    # Ensure models are bound to metadata (não executa create_all para não alterar o banco)
    log.info("Connecting to database with SQLAlchemy...")
    Base.metadata.bind = engine

    # Create Module Structure
    output_dir = build_module_structure()

    # --- Generators Execution ---
    generate_armors_json(output_dir)
    generate_bonds_json(output_dir)
    generate_boons_json(output_dir)
    generate_conditions_json(output_dir)
    generate_item_patterns_json(output_dir)
    generate_items_json(output_dir)
    generate_opportunities_json(output_dir)
    generate_properties_json(output_dir)
    generate_school_cursus_json(output_dir)
    generate_signature_scrolls_json(output_dir)
    generate_terrains_json(output_dir)
    generate_titles_json(output_dir)
    generate_weapons_json(output_dir)
    generate_peculiarities_json(output_dir)
    generate_techniques_json(output_dir)

    log.info("JSON Generation Complete!")
    log.stage_end()

if __name__ == "__main__":
    main()
