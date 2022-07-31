class Teniser(object):

    def __init__(self, ime, prezime, kategorija):
        self.ime = ime
        self.prezime = prezime
        self.kategorija = kategorija


djokovic = Teniser("Novak", "Djokovic", "single")
nadal = Teniser("Rafael", "Nadal", "single")
zverev = Teniser("Aleksander", "Zverev", "single")
medvedev = Teniser("Danil", "Medvedev", "single")
pavic = Teniser("Mate", "Pavic", "double")
sabanov = Teniser("Nikola", "Sabanov", "double")
karlovic = Teniser("Ivo", "Karlovic", "double")


tennis_players = [
    djokovic,
    nadal,
    zverev,
    medvedev,
    pavic,
    sabanov,
    karlovic
]

def get_teniser(teniser: Teniser) -> Teniser:
    print(teniser.ime, teniser.prezime, teniser.kategorija)
    return teniser


created_file = "tennis_players_write.txt"

# with open(created_file, "w") as file:
#     for player in tennis_players:
#         print(player.ime, player.prezime, player.kategorija, file=file)
