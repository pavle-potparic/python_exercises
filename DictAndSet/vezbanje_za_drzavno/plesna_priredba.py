broj = int(input())

lista = list(range(1, broj + 1))

print(*lista, sep=' ')

resenje = []


def raspodela(a, b, lista, delovi, a1, b1):
    if a1 + delovi[1] == b1:
        if a1 == 0:
            return b[::-1] + a[::-1] + lista[b1 + delovi[1]:len(lista)]
        else:
            return lista[0:a1] + b[::-1] + a[::-1] + lista[b1+delovi[1]:len(lista)]

    else:
        return lista[0:a1] + b[::-1] + lista[a1 + delovi[1]:b1] + a[::-1] + lista[b1+delovi[1]:len(lista)]


while True:
    red = input()
    if red == '':
        break
    delovi = list(map(int, red.split()))

    prva_grupa = lista[delovi[0]:delovi[0] + delovi[1]]
    druga_grupa = lista[delovi[2]:delovi[2] + delovi[1]]

    if len(prva_grupa + druga_grupa) != broj:
        lista = raspodela(prva_grupa, druga_grupa, lista, delovi, delovi[0], delovi[2])

    else:
        lista = druga_grupa[::-1] + prva_grupa[::-1]

    print(*lista)
