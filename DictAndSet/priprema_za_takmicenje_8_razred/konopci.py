broj = int(input())

lista = list(map(int, input().split(' ')))

lista.sort()

drugi_najmanji = lista[1]

for x in range(drugi_najmanji + 1, 1, -1):
    resenje = list(filter(lambda y: y % x == 0, lista))

    if len(resenje) == broj - 1:
        print(x)
        break