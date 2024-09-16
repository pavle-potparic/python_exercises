ogrlica = list(input())

duzina = len(ogrlica)
broj = duzina // 2

resenje = []

ogrlica2 = ogrlica * 2

lista = [0] * (duzina * 2 + 1)

counter = 0
for z in range(0, duzina * 2+1):
    lista[z] = int(counter)
    if z != duzina * 2:
        if ogrlica2[z] == 'P':
            counter += 1

for x in range(0, duzina):
    if duzina % 2 == 0:
        if x - broj > -1:
            prva_lista_p = lista[x] - lista[x - broj + 1]
        else:
            prva_lista_p = lista[x + duzina] - lista[x + duzina - broj + 1]

        druga_lista_p = lista[broj + x] - lista[x + 1]

    else:
        if x - broj > -1:
            prva_lista_p = lista[x] - lista[x - broj]
        else:
            prva_lista_p = lista[x + duzina] - lista[x + duzina - broj]

        druga_lista_p = lista[broj + x + 1] - lista[x + 1]

    if prva_lista_p > druga_lista_p:
        resenje.append('L')
    elif druga_lista_p > prva_lista_p:
        resenje.append('D')
    else:
        resenje.append('N')

print(*resenje, sep='')
