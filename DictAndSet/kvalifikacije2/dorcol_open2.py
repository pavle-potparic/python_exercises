k = int(input())

mecevi = ""

pobede = []
porazi = []
for x in range(0, pow(2, k)-1):
    pobeda, poraz = list(map(int, input().split(" ")))
    pobede.append(pobeda)
    porazi.append(poraz)

def sortiraj_bez_duplikata_po_pojavljivanjima(lista):
    broj_pojavljivanja = {}
    for element in lista:
        broj_pojavljivanja[element] = broj_pojavljivanja.get(element, 0) + 1

    sortirana_bez_duplikata = sorted(set(lista), key=lambda x: (-broj_pojavljivanja[x], x))

    return sortirana_bez_duplikata

def unija_bez_duplikata(lista1, lista2):
    set1 = set(lista1)
    filtrirana_lista2 = filter(lambda x: x not in set1, lista2)
    return lista1 + list(filtrirana_lista2)

pobede = sortiraj_bez_duplikata_po_pojavljivanjima(pobede)
porazi = sortiraj_bez_duplikata_po_pojavljivanjima(porazi)

lista = unija_bez_duplikata(pobede, porazi)

print(lista[0])
print(lista[1])
step = 2
for x in range(2, len(lista), step * 2):
    print(*lista[step:step*2])
    step *= 2




