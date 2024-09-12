broj = int(input())

lista = []

for x in range(broj):
    lista.append(int(input()))

nasa_zemlja = int(input())
bodovi = lista[nasa_zemlja-1]
trenutna_zemlja = int(input())
poeni_trenutna_zemlja = lista[trenutna_zemlja-1]
lista.remove(poeni_trenutna_zemlja)
oduzimanje = 2

if trenutna_zemlja != nasa_zemlja:
    lista[nasa_zemlja-2] += broj-1
    bodovi += broj - 1
    if bodovi <= lista[0] and nasa_zemlja-2 != 0:
        counter = 0
        while lista[counter] >= bodovi:
            lista[counter] += broj - oduzimanje
            oduzimanje += 1
            counter += 1

        if oduzimanje != broj:
            for y in range(broj-2, -1, -1):
                lista[y] += broj - oduzimanje
                oduzimanje += 1

                if oduzimanje == broj:
                    break

    else:
        for x in range(broj-2, -1, -1):
            if x == nasa_zemlja-2:
                pass

            else:
                lista[x] += broj - oduzimanje
                oduzimanje += 1

lista.append(poeni_trenutna_zemlja)
lista.sort(reverse=True)

print(lista.index(bodovi))