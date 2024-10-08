broj, zamene = list(map(int, input().rstrip().split(' ')))
niz = list(map(int, input().split(' ')))

upiti = int(input())

resenja = []

for x in range(0, upiti):
    pocetak, kraj = list(map(int, input().split(' ')))
    prvi_pocetak = pocetak - zamene

    if prvi_pocetak < 0:
        prvi_pocetak = 0

    prvi_kraj = pocetak + zamene
    if prvi_kraj >= len(niz):
        prvi_kraj = len(niz)-1

    drugi_pocetak = kraj - zamene

    if drugi_pocetak < 0:
        drugi_pocetak = 0

    drugi_kraj = kraj + zamene

    if drugi_kraj >= len(niz):
        drugi_kraj = len(niz)-1

    prva_lista = [[niz[i], abs(i - pocetak)] for i in range(prvi_pocetak, prvi_kraj + 1)]

    druga_lista = [[niz[i], abs(i - kraj)] for i in range(drugi_pocetak, drugi_kraj + 1)]

    resenje = -1

    counter1 = 0
    counter2 = 0

    for z in prva_lista:
        for q in druga_lista:
            if z[0] + q[0] > resenje:
                if z[1] + q[1] <= zamene:
                    if niz.index(z[0]) != niz.index(q[0]):
                        resenje = z[0] + q[0]

    resenja.append(resenje)
print(*resenja, sep='\n')
