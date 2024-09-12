unos = input()

cvorovi, broj_skupova = list(map(int, unos.split(" ")))

skupovi = []

graf = {i: set() for i in range(1, cvorovi + 1)}


def pronadji_broj(broj, lista):
    index = []
    temp = 0
    for z in lista:
        provera = list(filter(lambda k: k == broj, z))
        if len(provera) > 0:
            index.append(temp)
        temp += 1
    return index


def pronadji_zajednicke_brojeve(lista1, lista2, skupovi1):
    prvi_skupovi1 = [skupovi1[p] for p in lista1]
    drugi_skupovi1 = [skupovi1[k] for k in lista2]
    prvi_skupovi = set([broj for podlista in prvi_skupovi1 for broj in podlista])
    drugi_skupovi = [broj for podlista in drugi_skupovi1 for broj in podlista]

    zajednicki = set(prvi_skupovi).intersection(set(drugi_skupovi))
    if len(zajednicki) > 0:
        return zajednicki
    return []


def pronadji_duze_puteve(graf1, pocetni_cvor1, cilj_cvor1):
    red = [(pocetni_cvor1, 0)]
    poseceni = set()

    while len(red) > 0:
        trenutni_cvor, distanca1 = red.pop(0)
        if trenutni_cvor == cilj_cvor1:
            return distanca1

        for pored in graf1.get(trenutni_cvor, []):
            if pored not in poseceni:
                poseceni.add(pored)
                red.append((pored, distanca1 + 1))

    return float('inf')


for x in range(0, broj_skupova):
    brojevi = list(map(int, input().split()[1:]))
    skupovi.append(brojevi)

    for i in brojevi:
        graf[i].update(num for num in brojevi if num != i)


resenje = 0

for pocetni_cvor in range(1, cvorovi + 1):
    for cilj_cvor in range(pocetni_cvor + 1, cvorovi + 1):
        skupovi_cilj = set(pronadji_broj(cilj_cvor, skupovi))
        skupovi_pocetak = set(pronadji_broj(pocetni_cvor, skupovi))
        zajednicki_skupovi = skupovi_pocetak.intersection(skupovi_cilj)

        if len(zajednicki_skupovi) == 0:
            distanca = pronadji_duze_puteve(graf, pocetni_cvor, cilj_cvor)
            resenje += distanca
        else:
            resenje += 1

print(resenje)
