# TODO: napravi klasu Player koji ce da ima dva polja: name i number_of_card
# napravi klasu Transaction i u njoj metodu transaction_card koja ce izvrsiti transakciju kartica izmedju dva playera
# npr ako marko ima 15 kartica, a pera 11 i u transakciji marko da 5 kartica peri, marko ce imati 10, a pera 16 kartica
# ova metoda bi trebala da bude staticka jer ne zavisi od instance vec se transakcija vrsi na nivou klase
# napravi metodu koja ce da prikazuje koliko je ostalo kartica svakom od igraca
# napravi tri instance playera (marko, pera i nemanja) sa pocetnim karticama (20, 14, 16)
# izvrsi 4 poziva transakija
# 1) marko je dao peri 4 kartice (16, 18, 16)
# 2) nemanja je dao peri 8 kartica (16, 26, 8)
# 3) nemanja je dao marku 5 kartica (21, 26, 3)
# 4) nemanja je dao peri 4 kartice, transakcija ne moze da se izvrsi (21, 26, 3)


class Player(object):

    @staticmethod
    def print_all_cards(player_list):
        for player in player_list:
            player.get_cards()
        print(10 * "-")

    @staticmethod
    def transaction(player_list, cards):
        if player_list[1].number_of_card >= cards:
            player_list[0].number_of_card += cards
            player_list[1].number_of_card -= cards

    def __init__(self, name, number_of_card):
        self.name = name
        self.number_of_card = number_of_card

    def get_cards(self):
        print(self.name, self.number_of_card)


class Transaction:
    @staticmethod
    def transaction_card(player1: Player, player2: Player, cards: int):
        if player2.number_of_card >= cards:
            player1.number_of_card += cards
            player2.number_of_card -= cards

    def __init__(self):
        pass


marko = Player('Marko', 20)
pera = Player('Pera', 14)
nemanja = Player('Nemanja', 16)

players = [marko, pera, nemanja]

Transaction.transaction_card(pera, marko, 4)
Player.print_all_cards(players)
Transaction.transaction_card(pera, nemanja, 8)
Player.print_all_cards(players)
Transaction.transaction_card(marko, nemanja, 5)
Player.print_all_cards(players)
Transaction.transaction_card(pera, nemanja, 4)
Player.print_all_cards(players)

# Player.transaction([pera, marko], 4)
# Player.print_all_cards(players)
# Player.transaction([pera, nemanja], 8)
# Player.print_all_cards(players)
# Player.transaction([marko, nemanja], 5)
# Player.print_all_cards(players)
# Player.transaction([pera, nemanja], 4)
# Player.print_all_cards(players)
