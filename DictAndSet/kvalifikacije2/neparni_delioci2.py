import math

broj = int(input())


def broj_delilaca(pocetni_broj):
    counter = 1
    for x in range(1, int(pocetni_broj/2)+1):
        if pocetni_broj % x == 0:
            counter += 1

    return counter

brojac = 0
pocetak = True

while pocetak:
    brojac += 1
    delioci = broj_delilaca(broj * brojac)
    if delioci % 2 == 1:
        pocetak = False

print(brojac)
