broj = int(input())

lista = []

resenje = 0

for x in range(0, broj):
    red = list(map(int, input().split(' ')))

    provera = list(filter(lambda y: y == 1, red))

    if len(provera) > 1:
        resenje = 1

    lista.append(red)

for z in range(0, broj):
    provera2 = list(filter(lambda k: k[z] == 1, lista))

    if len(provera2) > 1:
        resenje = 1
        break

print(resenje)