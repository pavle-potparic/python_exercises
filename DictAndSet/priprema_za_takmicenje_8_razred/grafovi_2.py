cvorovi, broj_skupova = list(map(int, input().split(" ")))

skupovi = []


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

    print(prvi_skupovi)
    print(drugi_skupovi)

    zajednicki = set(prvi_skupovi).intersection(set(drugi_skupovi))

    if len(zajednicki) > 0:
        return zajednicki

    return []


resenje = 0

for x in range(0, broj_skupova):
    brojevi = list(map(int, input().split(' ')))
    brojevi.remove(brojevi[0])
    skupovi.append(brojevi)

for pocetni_cvor in range(1, cvorovi):
    for cilj_cvor in range(pocetni_cvor + 1, cvorovi+1):
        skupovi_cilj = set(pronadji_broj(cilj_cvor, skupovi))
        skupovi_pocetak = set(pronadji_broj(pocetni_cvor, skupovi))
        zajednicki_skupovi = skupovi_pocetak.intersection(skupovi_cilj)

        if len(zajednicki_skupovi) == 0:
            pronadjen_put = False
            zajednicki = pronadji_zajednicke_brojeve(skupovi_pocetak, skupovi_cilj, skupovi)
            if len(zajednicki) > 0:
                resenje += 2

            else:
                pass

            print(pocetni_cvor, cilj_cvor)
            print(resenje)
            print('**********')

        else:
            resenje += 1
            print(resenje)

print(resenje)
