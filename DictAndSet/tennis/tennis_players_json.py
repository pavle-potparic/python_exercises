import json

tennis_players = [
    ["Novak Djokovic", "Serbia", "single"],
    ["Rafael Nadal", "Spain", "single"],
    ["Aleksander Zverev", "Germany", "single"],
    ["Danil Medvedev", "Russia", "single"],
    ["Mate Pavic", "Croatia", "single"],
    ["Nikola Sabanov", "Serbia", "single"],
    ["Ivo Karlovic", "Croatia", "single"]
]

created_file = "tennis_players.json"

with open(created_file, "w", encoding="utf-8") as jsonfile:
    json.dump(tennis_players, jsonfile)