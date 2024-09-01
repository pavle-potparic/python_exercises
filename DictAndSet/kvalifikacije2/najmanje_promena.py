import math
niz = input()

temp_niz = list(niz)
counter = len(niz)
resenje = 0

for i in range(1, len(niz)):
    if niz[i] != niz[i - 1]:
        resenje += 1

lista_resenja = [resenje] * (counter + 1)

for i in range(1, counter - 1):
    if niz[i - 1] == niz[i + 1]:
        index = i + 1
        for j in range(1, int(math.sqrt(index)) + 1):
            if index % j == 0:
                if niz[i] != niz[i - 1]:
                    lista_resenja[j] -= 2
                    if j * j != index:
                        lista_resenja[index // j] -= 2
                else:
                    lista_resenja[j] += 2
                    if j * j != index:
                        lista_resenja[index // j] += 2
index = counter
for x in range(1, int(math.sqrt(index)) + 1):
    if index % x == 0:
        if niz[counter - 1] != niz[counter - 2]:
            lista_resenja[x] -= 1
        else:
            lista_resenja[x] += 1

        if x * x != index:
            if niz[counter - 1] != niz[counter - 2]:
                lista_resenja[index // x] -= 1
            else:
                lista_resenja[index // x] += 1

lista_resenja[1] = resenje
po_koliko_se_preskace_brojeva = 1
for q in range(2, counter + 1):
    if lista_resenja[q] < resenje:
        resenje = lista_resenja[q]
        po_koliko_se_preskace_brojeva = q

print(po_koliko_se_preskace_brojeva, resenje)
