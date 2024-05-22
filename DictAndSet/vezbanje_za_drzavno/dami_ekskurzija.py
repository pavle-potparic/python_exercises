lista = [1, 3, 7, 6]

L = [['a',1], ['a',2], ['a',3], ['b',1], ['b',2], ['b',3]]
L.sort(key=lambda k: (k[0], -k[1]), reverse=True)

lista1 = lista.sort()
print(lista1)
print(sum(lista))