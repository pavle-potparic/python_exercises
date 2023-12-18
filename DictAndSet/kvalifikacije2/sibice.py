broj_sibica = int(input())

niz = list(map(int, input().split(" ")))

suma = sum(niz)


def spajanje_sibica(lista, stranice, velicina_stranice):
    lista.sort(reverse=True)
    for x in range(0, len(lista)):
        if velicina_stranice - lista[0] in lista:
            lista.remove(velicina_stranice - lista[0])
            lista.remove(lista[0])
            stranice -= 1
        else:
            razlika = velicina_stranice - lista[0]
            lista.append(razlika)
            lista.sort(reverse=True)
            index = lista.index(razlika)
            lista.remove(razlika)
            for y in range(index, -1, -1):
                if razlika - lista[y] in lista:
                    stranice -= 1
                    lista.remove(x)
                    lista.remove(y)
                    lista.remove(y-1)

        if stranice == 0:
            return 1

    return 0


if suma % 4 != 0:
    print(0)

elif max(niz) > suma / 4:
    print(0)

else:
    stranica = suma // 4
    broj_stranica = 4
    if stranica in niz:
        while stranica in niz:
            niz.remove(stranica)
            broj_stranica -= 1

    print(spajanje_sibica(niz, broj_stranica, stranica))
