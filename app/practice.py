import requests


def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"

    response = requests.get(url)

    data = response.json()

    pokemon_summary = {
        "id": data["id"],
        "name": data["name"],
        "sprite": data["sprites"]["front_default"],
        "types": [type["type"]["name"] for type in data["types"]],
        "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]},
        "abilities": [ability["ability"]["name"] for ability in data["abilities"]]
    }

    return pokemon_summary


print(get_pokemon("charizard"))
