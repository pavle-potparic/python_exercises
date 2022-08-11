class CezarovaSifra(object):
    def __init__(self, broj_pomerenih_slova):
        self.broj = broj_pomerenih_slova
        self.abeceda = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.recenica = 'UCIM PROGRAMIRANJE'
        self.sifra = ''
        self.lista_indexa = []
        self.index_slova_u_recenici(self.recenica)
        self.desifrovana_recenica = ''

    def index_slova_u_recenici(self, recenica):
        self.lista_indexa = []
        for slovo in recenica:
            for x in range(0, len(self.abeceda)):
                if slovo == self.abeceda[x]:
                    self.lista_indexa.append(x)

    def sifruj(self):
        #   for slovo in self.recenica:
        #   if slovo in self.abeceda:
        for index in self.lista_indexa:
            if index < len(self.abeceda) - self.broj:
                for x in range(0, len(self.abeceda) - self.broj):
                    if self.abeceda[index] == self.abeceda[x]:
                        self.sifra += self.abeceda[x + self.broj]
            else:
                pocetna_slova = index + self.broj - len(self.abeceda)
                self.sifra += self.abeceda[pocetna_slova]

        return self.sifra

    def desifruj(self):
        self.index_slova_u_recenici(self.sifra)
        for desifrovanje in self.lista_indexa:
            if desifrovanje + 1 > self.broj:
                for x in range(self.broj, len(self.abeceda)):
                    if self.abeceda[desifrovanje] == self.abeceda[x]:
                        self.desifrovana_recenica += self.abeceda[desifrovanje - self.broj]
            else:

                self.desifrovana_recenica += self.abeceda[len(self.abeceda) + desifrovanje - self.broj]

        return self.desifrovana_recenica


test = CezarovaSifra(10)
print(test.sifruj())
print(test.desifruj())

lista_abecednih_slova = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encode(abeceda, rec, modul_sifrovanja):
    sifrat = ""
    for slovo in rec:
        for index in range(0, len(abeceda)):
            if slovo == abeceda[index]:
                sifrat += abeceda[index + modul_sifrovanja]
                break
    return sifrat


sifrovana_rec = encode(lista_abecednih_slova, 'UCIM PROGRAMIRANJE', 10)
print(sifrovana_rec)


def decode(abeceda, rec, modul_desifrovanja):
    text = ''
    temp = abeceda
    length = len(abeceda)
    polovina = temp[:length // 2]

    for slovo in rec:
        for index in range(0, len(polovina)):
            if slovo == temp[index]:
                text += abeceda[index * 2 - modul_desifrovanja]
    return text


def decode_2(abeceda, sifrat, modul_desifrovanja):
    text = ""
    for slovo in sifrat:
        for index in range(len(abeceda)-1, 0, -1):
            if slovo == abeceda[index]:
                text += abeceda[index - modul_desifrovanja]
                break
    return text


print(decode(lista_abecednih_slova, 'EMSWZBYQBKWSBKXTO', 10))
