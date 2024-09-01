import bisect

broj = int(input())

lista = []

for x in range(0, broj):
    patike, cena = input().split(' ')
    cena = int(cena)
    lista.append([patike, cena])

kupci = int(input())

lista_resenja = []
lista_indexa = []
for x in range(0, kupci):
    novac = int(input())
    lista.append(['A', novac])
    lista.append(['zzzzz', novac])
    lista.sort(key=lambda k: (k[1], k))
    index = lista.index(['A', novac])
    prethodnik = lista[index - 1][1]

    provera = list(filter(lambda r: r[1] == novac, lista))

    if len(provera) == 2 and index > 0:
        lista.remove(['A', novac])
        lista.append(['A', prethodnik])
        lista.sort(key=lambda k: (k[1], k))
        index = lista.index(['A', prethodnik])

    index1 = lista.index(['zzzzz', novac])
    lista_resenja = []

    if index > index1:
        temp = int(index)
        index = int(index1)
        index1 = int(temp)

    if index1 > 1 and index < broj:
        for y in range(index, index1):
            if y == index + 1:
                standard = lista[y][1]
            if y != index:
                if lista[y][1] == standard:
                    lista_resenja.append(lista[y])
                else:
                    break

    else:
        print('nema')

    if len(lista_resenja) > 0:
        lista_resenja.sort(key=lambda k: k[0], reverse=False)
        for z in lista_resenja:
            print(*z)


