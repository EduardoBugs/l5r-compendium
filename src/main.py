from generators import (
    generate_armors_json,
    generate_bonds_json,
    generate_boons_json,
    generate_conditions_json,
)


def main():
    print("🔧 Iniciando geração de compêndios L5R...")

    generate_armors_json()
    generate_bonds_json()
    generate_boons_json()
    generate_conditions_json()

    print("🎉 Geração concluída!")


if __name__ == "__main__":
    main()
