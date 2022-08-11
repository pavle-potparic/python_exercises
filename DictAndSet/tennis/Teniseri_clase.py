class Teniseri(object):
    def __init__(self, ime, prezime, kategorija, turnir, trofeji):
        self._ime = ime
        self._prezime = prezime
        self._kategorija = kategorija
        self._turnir = turnir
        self._trofeji = trofeji

    def _get_ime(self):
        return self._ime

    def _set_ime(self, ime):
        self._ime = ime

    def _get_prezime(self):
        return self._prezime

    def _set_prezime(self, prezime):
        self._prezime = prezime

    def _get_kategorija(self):
        return self._kategorija

    def _set_kategorija(self, kategorija):
        self._kategorija = kategorija

    def _get_turnir(self):
        return self._turnir

    def _set_turnir(self, turnir):
        self._turnir = turnir

    @property
    def trofeji(self):
        return self._trofeji

    @trofeji.setter
    def trofeji(self, trofeji):
        self._trofeji = trofeji


    ime = property(_get_ime, _set_ime, None, "Define name of tennis player")
    prezime = property(_get_prezime, _set_prezime)
    kategorija = property(_get_kategorija, _set_kategorija)
    turnir = property(_get_turnir, _set_turnir)

    def __str__(self):
        return "Ime: {0.ime}, Prezime: {0.prezime}, Kategorija: {0.kategorija}, Turnir: {0.turnir}, Trofeji: {0.trofeji}".format(self)





