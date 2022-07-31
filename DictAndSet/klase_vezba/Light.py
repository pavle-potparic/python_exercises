class Light(object):
    name = 'luster'

    def __init__(self, turn_on):
        self.turn_on = turn_on

    # def on(self):
    #     self.turn_on = True
    #
    # def off(self):
    #     self.turn_on = False

    def switch_toggle(self):
        self.turn_on = not self.turn_on


led = Light(False)
led.switch_toggle()
print(led.turn_on)
led.switch_toggle()
print(led.turn_on)
led.switch_toggle()
print(led.turn_on)
neon = Light(True)
print(Light.name)
print(Light.name)

#
# POTPIS METODE
#
# def ime_meteda(parametar, parameter: list) -> str:
#     parameter.append(10)
#     return "Cao"
#


# TODO: napravi klasu Player koji ce da ima dva polja: name i number_of_card
# napravi metodu transaction_card koja ce izvrsiti transakciju kartica izmedju dva playera
# npr ako marko ima 15 kartica, a pera 11 i u transakciji marko da 5 kartica peri, marko ce imati 10, a pera 16 kartica
# ova metoda bi trebala da bude staticka jer ne zavisi od instance vec se transakcija vrsi na nivou klase
# napravi metodu koja ce da prikazuje koliko je ostalo kartica svakom od igraca
# napravi tri instance playera (marko, pera i nemanja) sa pocetnim karticama (20, 14, 16)
# izvrsi 4 poziva transakija
# 1) marko je dao peri 4 kartice (16, 18, 16)
# 2) nemanja je dao peri 8 kartica (16, 26, 8)
# 3) nemanja je dao marku 5 kartica (21, 26, 3)
# 4) nemanja je dao peri 4 kartice, transakcija ne moze da se izvrsi (21, 26, 3)


