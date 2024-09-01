broj_mrava, broj_zelja = list(map(int, input().split(" ")))

lista = []

broj_podlista = 1

for x in range(0, broj_zelja):
    prvi_mrav, drugi_mrav = list(map(int, input().split(" ")))
    lista.append([prvi_mrav, drugi_mrav])

lista.sort(key=lambda k: (k[0], -k[1]), reverse=True)

used_hotel_rooms = []

prvi = lista[0][0]
drugi = lista[0][1]

sobe = [prvi, drugi]

pocetak = 0

ukupno_mrava = 0

for x in lista:
    if pocetak == 1:
        if x[0] != prvi and x[0] != drugi and x[1] != prvi and x[1] != drugi:
            broj_podlista += 1
            used_hotel_rooms.append(sobe)
            ukupno_mrava += len(sobe)
            prvi = x[0]
            drugi = x[1]
            sobe = [prvi, drugi]

        else:
            if x[0] not in sobe:
                sobe.append(x[0])
            else:
                sobe.append(x[1])
    else:
        pocetak = 1

used_hotel_rooms.append(sobe)
ukupno_mrava += len(sobe)

broj_podlista += broj_mrava - ukupno_mrava

print(broj_podlista)