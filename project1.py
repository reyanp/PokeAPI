import requests
import pandas as pd
import sqlalchemy as db

url = "https://pokeapi.co/api/v2/pokedex/kanto"
response = requests.get(url)
data = response.json()

pokemon_entries = data.get("pokemon_entries", [])
rows = [
    {
        "entry_number": entry["entry_number"],
        "name": entry["pokemon_species"]["name"].capitalize()
    }
    for entry in pokemon_entries
]
df = pd.DataFrame.from_dict(rows)

print("Kanto Pokedex (DataFrame):")
print(df.head())

engine = db.create_engine('sqlite:///kanto_pokedex.db')

df.to_sql(
    'kanto_pokemon', 
    con=engine, 
    if_exists='replace', 
    index=False
)

with engine.connect() as connection:
    result = connection.execute(
        db.text("SELECT * FROM kanto_pokemon;")
    ).fetchall()

    df2 = pd.DataFrame(result, columns=df.columns)
    print("\nFetched from SQLite:")
    print(df2.head())
