class Kosarkasi:
    def __init__(self, ime, prezime, godine, tim):
        self._ime = ime
        self._prezime = prezime
        self._godine = godine
        self._tim = tim

    def _get_ime(self):
        return self._ime

    def _set_ime(self, ime):
        self._ime = ime

    def _get_prezime(self):
        return self._prezime

    def _set_prezime(self, prezime):
        self._prezime = prezime

    def _get_godine(self):
        return self._godine

    def _set_godine(self, godine):
        if 12 < godine < 14:
            self._godine = godine
        else:
            print('Potrebno je da imate izmedju 12 i 14 godina. ')

    def _get_tim(self):
        return self._tim

    def _set_tim(self, tim):
        self._tim = tim

    ime = property(_get_ime, _set_ime)
    prezime = property(_get_prezime, _set_prezime)
    godine = property(_get_godine, _set_godine)
    tim = property(_get_tim, _set_tim)

    def __str__(self):
        rezultat = "Ime: " + self.ime + " Prezime: " + self.prezime
        return rezultat
