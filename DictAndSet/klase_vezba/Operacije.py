class Operacije(object):
    def __init__(self, prvi_broj, drugi_broj):
        self.prvi_broj = prvi_broj
        self.drugi_broj = drugi_broj

    def saberi(self):
        print(self.prvi_broj + self.drugi_broj)

    def oduzmi(self):
        print(self.prvi_broj - self.drugi_broj)

    def pomnozi(self):
        print(self.prvi_broj * self.drugi_broj)

    def podeli(self):
        print(self.prvi_broj // self.drugi_broj)


moja_instanca = Operacije(10, 5)
moja_instanca.saberi()
moja_instanca.oduzmi()
moja_instanca.podeli()
moja_instanca.pomnozi()

moja_druga_instanca = Operacije(20, 2)
moja_druga_instanca.saberi()
moja_druga_instanca.oduzmi()
moja_druga_instanca.podeli()
moja_druga_instanca.pomnozi()