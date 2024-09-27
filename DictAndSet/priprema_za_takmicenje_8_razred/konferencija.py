broj_firmi = int(input())
broj_casova = int(input())

niz = list(map(int, input().split(' ')))
temp = 0
lista = []
resenje = 100000000000
odgovor = 'ne moze'
for x in range(0, broj_casova-broj_firmi+1):
    temp = 0
    lista = []
    for y in range(x, broj_casova):
        if niz[y] not in lista:
            lista.append(niz[y])

        temp += 1

        if len(lista) == broj_firmi:
            if resenje > temp:
                resenje = int(temp)
            break

if resenje == 100000000000:
    print(odgovor)

else:
    print(resenje)