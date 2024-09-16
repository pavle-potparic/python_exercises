ogrlica = list(input())

duzina = len(ogrlica)
broj = duzina // 2

resenje = []

ogrlica2 = ogrlica * 2

broj_p = [0] * (2 * duzina + 1)

for i in range(1, 2 * duzina + 1):
    broj_p[i] = broj_p[i - 1] + (1 if ogrlica2[i - 1] == 'P' else 0)

for x in range(0, duzina):
    if duzina % 2 == 0:
        if x - broj > -1:
            prva_lista_p = broj_p[x] - broj_p[x - broj + 1]
        else:
            prva_lista_p = broj_p[x + duzina] - broj_p[x + duzina - broj + 1]

        druga_lista_p = broj_p[broj + x] - broj_p[x + 1]

    else:
        if x - broj > -1:
            prva_lista_p = broj_p[x] - broj_p[x - broj]
        else:
            prva_lista_p = broj_p[x + duzina] - broj_p[x + duzina - broj]

        druga_lista_p = broj_p[broj + x + 1] - broj_p[x + 1]

    if prva_lista_p > druga_lista_p:
        resenje.append('L')
    elif druga_lista_p > prva_lista_p:
        resenje.append('D')
    else:
        resenje.append('N')
print(broj_p)
print(*resenje, sep='')
