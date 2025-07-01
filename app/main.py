import requests


def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"

    response = requests.get(url)

    data = response.json()

    pokemon_summary = {
        "id": data["id"],
        "name": data["name"],
        "sprite": data["sprites"]["front_default"],
        "types": [t["type"]["name"] for t in data["types"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
        "abilities": [a["ability"]["name"] for a in data["abilities"]]
    }

    return pokemon_summary


print(get_pokemon("pikachu"))
