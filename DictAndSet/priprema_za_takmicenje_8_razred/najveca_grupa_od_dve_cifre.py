lista = list(input())

lista = list(map(int, lista))

indexi = list(range(0, len(lista)-1))

resenje = list(map(lambda x: int(str(lista[x]) + str(lista[x + 1])), indexi))

print(max(resenje))