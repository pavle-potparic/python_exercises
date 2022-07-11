tennis_players = [
    "Novak Djokovic - single",
    "Rafael Nadal - single",
    "Aleksander Zverev - single",
    "Danil Medvedev - single",
    "Mate Pavic - double",
    "Nikola Sabanov - double",
    "Ivo Karlovic - double"
]

created_file = "tennis_players_write.txt"

with open(created_file, "w") as file:
    for player in tennis_players:
        print(player, file=file)
