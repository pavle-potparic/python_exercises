broj_elemenata = int(input())

niz = list(map(int, input().split(" ")))

lista = []
resenje = 0

for x in range(0, broj_elemenata):
    temp_lista = [niz[x]]
    for y in range(x+1, broj_elemenata):
        temp_lista.append(niz[y])
        if len(temp_lista) == sum(temp_lista):
            if temp_lista in lista:
                pass

            else:
                lista.append(list(temp_lista))
                resenje += 1

print(resenje)


