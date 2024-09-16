lista = [[1, 2, 3], [4, 88, 23, 56], [5, 6, 7]]

for x in range(0, len(lista)):
    print(*list(map(lambda z, k=4: z + 2 if z % 2 == 0 else k + 7 + z, lista[x])))
