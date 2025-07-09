import requests

url = "https://pokeapi.co/api/v2/pokedex/kanto"

response = requests.get(url)

data = response.json()

print ("Kanto Pokedex")
pokemon_entries = data.get("pokemon_entries", [])
for entry in pokemon_entries:
  entry_num = entry["entry_number"]
  name = entry["pokemon_species"]["name"]
  print(f"{entry_num:03d} - {name.capitalize()}")