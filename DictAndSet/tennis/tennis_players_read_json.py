import json

with open("tennis_players.json", "r") as jsonread:
    loaded_data = json.load(jsonread)
    print(loaded_data)