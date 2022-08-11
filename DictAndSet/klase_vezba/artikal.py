class Artikal:
    def __init__(self, naziv, cena):
        self.naziv = naziv
        self.cena = cena

    def povecaj_cenu(self, poskupljenje):
        self.cena += self.get_vrednost_od_procenta(poskupljenje)
        return self.cena

    def smanji_cenu(self, popust):
        if self.get_vrednost_od_procenta(popust) > self.get_vrednost_od_procenta(50):
            return 'Nije dozvoljeno smanjiti cenu vise od 50%'
        self.cena -= self.get_vrednost_od_procenta(popust)
        return self.cena

    def get_vrednost_od_procenta(self, procenat):
        return self.cena * procenat / 100

laptop = Artikal('Laptop', 150000)
print(laptop.smanji_cenu(10))
srampac = Artikal('Stampac', 15000)
print(srampac.smanji_cenu(20))
print(srampac.povecaj_cenu(10))
telefon = Artikal('Telefon', 55000)
print(telefon.smanji_cenu(70))
print(telefon.smanji_cenu(50))
# laptop cena 150000
# stampac cena 15000
# telefon cena 55000

# laptop je poskupeo za 10%
# stampac je pojeftinio za 20%, pa je onda poskupeo za 10%
# sok cena, telefon je jeftiniji za 70%
# ok, ako ne moze, onda nek bude jeftiniji za 50%
