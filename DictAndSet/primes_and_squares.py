def svi_prosti_brojevi_do_odredjenog_broja(granica):
    prosti_brojevi = [1]
    for x in range(2, granica):
        prost_broj = 0
        for y in range(2, x):
            if y == x:
                continue
            else:
                if x > y:
                    if x % y == 0:
                        prost_broj = prost_broj + 1
        if prost_broj == 0:
            prosti_brojevi.append(x)
    return set(prosti_brojevi)


def kvadratni_brojevi_do_zadatog_broja(granica):
    lista_kvadratnih_brojeva = []
    for x in range(1, granica):
        if x * x < granica:
            lista_kvadratnih_brojeva.append(x * x)
    return set(lista_kvadratnih_brojeva)


def kubni_brojevi(granica):
    pocetni_broj = 1
    lista_brojeva_na_kvadrat = []
    while pocetni_broj ** 3 < granica:
        lista_brojeva_na_kvadrat.append(pocetni_broj ** 3)
        pocetni_broj = pocetni_broj + 1
    return lista_brojeva_na_kvadrat


def stepenuj_broj(granica, stepen):
    pocetni_broj = 1
    lista_brojeva_na_kvadrat = []
    while pocetni_broj ** stepen < granica:
        lista_brojeva_na_kvadrat.append(pocetni_broj ** stepen)
        pocetni_broj = pocetni_broj + 1
    return lista_brojeva_na_kvadrat


kvadratni_brojevi = stepenuj_broj(100, 2)
kubni_brojevi = stepenuj_broj(100, 3)
broj_na_cetvrtu = stepenuj_broj(100, 4)

#print(kvadratni_brojevi)
#print(kubni_brojevi)
#print(broj_na_cetvrtu)


def slicnosti_i_razlike():
    # pronadji: uniju, razliku, presek, simetricnu uniju
    # napravi posebnu promenljivu koja ce da izvrsi update sa prostim
    # napravi razlicite promenljive koje ce da izvrse razlicite vrste update-a (update.intersection itd)
    svi_prosti_brojevi = svi_prosti_brojevi_do_odredjenog_broja(10)
    brojevi_na_kvadrat = kvadratni_brojevi_do_zadatog_broja(10)
    unija = svi_prosti_brojevi.union(brojevi_na_kvadrat)
    print(unija)
    diff = svi_prosti_brojevi.symmetric_difference(kvadratni_brojevi)
    print(diff)


slicnosti_i_razlike()


"""
1, 2 ,3, 4, 5
kvadratni brojevi
1*1 = 1
2*2 = 4
3*3 = 9
4*4 = 16
5*5 = 25
kubni brojevi
1*1*1 = 1
2*2*2 = 8
3*3*3 = 27
4*4*4 = 64
5*5*5 = 125
brojevi na cetvrtu
1*1*1*1 = 1
2*2*2*2 = 16
3*3*3*3 = 81
4*4*4*4 = 256
5*5*5*5 = 625
"""

"""
kosta 1856 dinara i smanjeno je za 30 %
izracunam koliko je 10% ili 1%
10% = 185,6 dinara  (ima 10 ovakvih delova)
1 % = 18,56 dinara  (ima 100 ovakvih delova)

step 2
popust od 30% iznosi 185,6 *3 = 456,8
cena sa popustom je 1856 - 456,8 = 1399,2
"""

"""
cena je 100 dinara
prvo je smanjena za 10%, pa je onda povecana za 10%
cena sa smanjenjem je 90 dinara
cena sa povecanjem je 99 dinara
"""

"""
cena je 100 dinara
prvo je povecana za 10%, pa je onda smanjena za 10%
cena sa povecanjem je 110 dinara
cena sa smanjenjem je 99 dinara
"""
