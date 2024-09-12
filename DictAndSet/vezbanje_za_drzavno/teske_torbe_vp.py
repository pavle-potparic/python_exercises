lista = list(map(int, input().split(' ')))
lista.sort()

mrav_a, mrav_b = list(map(int, input().split(' ')))
mravi = [mrav_b, mrav_a]
mravi.sort()

mrav_a = int(mravi[0])
mrav_b = int(mravi[1])

slab_mrav = 0

rezultati = []

def manji_mrav(lista, mrav_a):
    filter_lista = list(filter(lambda y: y <= mrav_a, lista))

    return filter_lista


def uzmi_torbe(lista, putnik):
    pass


print(manji_mrav(lista, mrav_a))