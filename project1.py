import requests

response = requests.get("https://pokeapi.co/api/v2/pokedex/kanto")

print (response.json())