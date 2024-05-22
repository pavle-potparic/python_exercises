red, kolona, upit = tuple(map(int, input().split(" ")))

sema_matrice = tuple(map(int, input().split(" ")))

max_red = 0

trazeni_redovi = tuple(int(input()) for i in range(upit))


max_red = max(sema_matrice)

if red > max_red:
    red = max_red + 1

matrica = [[0] * kolona for i in range(red)]


def popuni_matricu():
    global sema_matrice, matrica
    for pozicija_kolone in range(0, len(sema_matrice)):
        jedinice = sema_matrice[pozicija_kolone]
        pozicija_reda = 0
        while jedinice > 0:
            matrica[pozicija_reda][pozicija_kolone] = 1
            jedinice -= 1
            pozicija_reda += 1


popuni_matricu()
matrica_nula = tuple(map(lambda x: x.count(0), matrica))


def pronadji_najblizi(nule, lista):
    najblizi = min(lista, key=lambda x: abs(x - nule))
    indeks = lista.index(najblizi)
    if lista[indeks] == nule:
        return indeks
    else:
        korekcija = abs(lista[indeks] - nule)
        return korekcija


for nule in trazeni_redovi:
    print(pronadji_najblizi(nule, matrica_nula))