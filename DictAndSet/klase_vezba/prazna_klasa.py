class Covek(object):
    def __init__(self, ime, pol, broj_godina):
        self.ime = ime
        self.pol = pol
        self.broj_godina = broj_godina


class Sportista(Covek):
    def __init__(self, ime, pol, broj_godina, vrsta_sporta, drzava):
        super().__init__(ime, pol, broj_godina)
        self.vrsta_sporta = vrsta_sporta
        self.drzava = drzava



class Teniser(Sportista):
    def __init__(self, ime, pol, broj_godina, vrsta_sporta, drzava, kategorija, rang):
        super().__init__(ime, pol, broj_godina, vrsta_sporta, drzava)
        self.kategorija = kategorija
        self.rang = rang


class Ucenik(Covek):
    def __init__(self, ime, pol, broj_godina, razred, odeljenje):
        super().__init__(ime, pol, broj_godina)
        self.razred = razred
        self.odeljenje = odeljenje







child_instance = ChildKlasa("child_attribute")
print(child_instance.parent_attribute)

