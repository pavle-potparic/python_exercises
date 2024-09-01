start, cilj = map(int, input().split(" "))

broj_ostrva, broj_mostova = map(int, input().split(" "))

lista = []
indeksi_starta = []

for x in range(0, broj_mostova):
    ostrvo, ostrvo1 = map(int, input().split(" "))
    if ostrvo == start or ostrvo1 == start:
        indeksi_starta.append([ostrvo, ostrvo1])
    lista.append([ostrvo, ostrvo1])

lista.sort(key=lambda k: (k[0], -k[1]), reverse=True)

broj_rusenja = int(input())

rusenje = []

for y in range(0, broj_rusenja):
    most, most1 = map(int, input().split(" "))
    rusenje.append([most, most1])


def pronadji_most_sa_poznatim_krakom(krak, lista1):
    return list(filter(lambda koordinata: koordinata[0] == krak or koordinata[1] == krak, lista1))


def proveri_dolazak_do_cilja(lista):
    global indeksi_starta, start, cilj

    for koordinate in indeksi_starta:
        if koordinate[0] == start:
            krak = koordinate[1]
        else:
            krak = koordinate[0]

        potraga = True

        while potraga:
            pronadjeni_mostovi = pronadji_most_sa_poznatim_krakom(krak, lista)
            if len(pronadjeni_mostovi) == 0:
                print('ne')
                potraga = False

            else:
                da_li_ima_most_do_cilja = pronadji_most_sa_poznatim_krakom(cilj, pronadjeni_mostovi)
                if len(da_li_ima_most_do_cilja) > 0:
                    print('da')
                    potraga = False

                else:
                    if pronadjeni_mostovi[0][0] == krak:
                        krak = pronadjeni_mostovi[0][1]

                    else:
                        krak = pronadjeni_mostovi[0][0]


for x in rusenje:
    lista.remove(x)
    proveri_dolazak_do_cilja(lista)