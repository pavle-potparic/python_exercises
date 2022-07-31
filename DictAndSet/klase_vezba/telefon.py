class Telefon(object):
    def __init__(self, marka, model, operativni_sistem):
        self.marka = marka
        self._model = model
        self.__operativni_sistem = operativni_sistem

    def prikazi_podatke(self):
        print(self.marka, self._model, self.__operativni_sistem)


xiaomi = Telefon('Xiaomi', 'A2', 'Android')

xiaomi.marka = "iPhone"
xiaomi._model = "13 pro"
xiaomi.__operativni_sistem = "IOS"
xiaomi._Telefon__operativni_sistem = "novi OS"

xiaomi.prikazi_podatke()
print(xiaomi.__dict__)