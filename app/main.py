import requests


def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"

    response = requests.get(url)

    return response.text


print(get_pokemon("clefairy"))
