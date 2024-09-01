duzina, broj = list(map(int, input().split(' ')))

niz = list(map(int, input().split(' ')))

resenje = 100000000000
index = 1000000

for x in range(0, duzina+1):
    prva_lista = niz[0:x]
    druga_lista = niz[x:duzina]

    levo = list(filter(lambda k: k > broj, prva_lista))
    desno = list(filter(lambda q: q < broj, druga_lista))

    if len(levo) + len(desno) < resenje:
        index = x
        resenje = len(levo) + len(desno)

    if resenje == 0:
        break

print(index)