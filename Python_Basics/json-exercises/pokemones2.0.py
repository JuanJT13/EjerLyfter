import json


def read_pokemon(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_new_pokemon_data():
    print("--- REGISTRO DE NUEVO POKÉMON ---")
    name = input("Nombre: ")
    poke_type = input("Tipo: ")
    level = int(input("Nivel: "))
    weight = float(input("Peso (kg): "))

    shiny_input = input("¿Es Shiny? (si/no): ").strip().lower()
    is_shiny = shiny_input in ("si", "sí")

    item_input = input("Objeto equipado (deja en blanco si no tiene): ").strip()
    held_item = item_input if item_input != "" else None

    skills_input = input("Introduce 2 habilidades separadas por coma: ")
    skills = [skill.strip() for skill in skills_input.split(",")]

    print("\n--- Estadísticas ---")
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("Sp. Attack: "))
    sp_defense = int(input("Sp. Defense: "))
    speed = int(input("Speed: "))

    new_pokemon = {
        "name": name,
        "type": poke_type,
        "level": level,
        "weight_kg": weight,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed,
        },
    }

    return new_pokemon


def write_pokemon(file_name, pokemon_list):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(pokemon_list, file, indent=4, ensure_ascii=False)
    print("\n¡Pokémon agregado y guardado con éxito!")


def main():
    archive_pokemon = "pokemon.json"

    pokemon_list = read_pokemon(archive_pokemon)
    nuevo_pokemon = get_new_pokemon_data()
    pokemon_list.append(nuevo_pokemon)
    write_pokemon(archive_pokemon, pokemon_list)


if __name__ == "__main__":
    main()