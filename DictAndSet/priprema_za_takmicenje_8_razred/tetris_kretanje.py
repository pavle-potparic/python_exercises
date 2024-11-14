redovi, kolone = list(map(int, input().split(' ')))

lista = []

for x in range(0, redovi):
    lista.append(input())

levo = 'da'
desno = 'da'
dole = 'da'

prvi_red = 0
poslednji_red = 0

for y in range(0, redovi):
    if 2 in y:
        prvi_red = y

    else:
        if prvi_red != 0:
            poslednji_red = y
            break
