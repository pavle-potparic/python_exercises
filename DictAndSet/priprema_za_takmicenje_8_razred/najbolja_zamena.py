broj, zamene = list(map(int, input().split(' ')))
niz = list(map(int, input().split(' ')))

upiti = int(input())

resenja = []

for x in range(0, upiti):
    pocetak, kraj = list(map(int, input().split(' ')))
    prvi_pocetak = pocetak - zamene

    if prvi_pocetak < 0:
        prvi_pocetak = 0

    prvi_kraj = pocetak + zamene
    if prvi_kraj > len(niz):
        prvi_kraj = len(niz)-1

    drugi_pocetak = kraj - zamene

    if drugi_pocetak < 0:
        drugi_pocetak = 0

    drugi_kraj = kraj + zamene

    if drugi_kraj > len(niz):
        drugi_kraj = len(niz)-1

    prva_lista = [[niz[i], abs(i - pocetak)] for i in range(prvi_pocetak, prvi_kraj + 1)]

    druga_lista = [[niz[i], abs(i - kraj)] for i in range(drugi_pocetak, drugi_kraj + 1)]

    svi_brojevi = prva_lista + druga_lista

    resenje = -1

    counter = 0
    maks = len(svi_brojevi) - 1

    while counter < maks:
        broj1, udaljenost1 = svi_brojevi[counter]
        broj2, udaljenost2 = svi_brojevi[maks]

        ukupna_udaljenost = udaljenost1 + udaljenost2

        if ukupna_udaljenost <= zamene:
            sabirak = broj1 + broj2
            if sabirak > resenje:
                resenje = sabirak
            counter += 1
        else:
            maks -= 1

    resenja.append(resenje)

print(*resenja, sep='\n')
