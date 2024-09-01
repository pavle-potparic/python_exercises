trazeni_niz = list(input())
data_slova = list(input())
lista = []
loop = True
resenje = 0
z = 1
while loop:
    for x in range(0, len(trazeni_niz)):
        string = ""
        broj_ispunjenih = len(trazeni_niz)
        for y in range(0, len(data_slova), z):
            if z == 1:
                if data_slova[y] == trazeni_niz[x]:
                    broj_ispunjenih -= 1
                    z = 2
                    x += 1
                    string += data_slova[y]
                    if broj_ispunjenih == 0:
                        x = 0
                        lista.append(string)
                        string = ""
                        break
            else:
                z = 1

        if broj_ispunjenih == 0:
            resenje += 1

        else:
            loop = False
            break

print(resenje)