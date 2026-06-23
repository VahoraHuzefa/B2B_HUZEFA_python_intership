import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

print("Fetching data from PokeAPI...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"\nPokemon Name: {data['name'].title()}")
    print(f"Weight: {data['weight']} hectograms")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")