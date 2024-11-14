red, red1 = list(map(int, input().split(' ')))

lista = []

for x in range(0, red):
    lista.append(input())

reci = []

for y in range(0, red1):
    reci.append(input())

resenje = 0

for z in reci:
    for q in range(0, red):
        if z in lista[q]:
            resenje += 1
            break

        temp = list(map(lambda k: lista[k][q], list(range(0, red))))
        print(temp)
        if z in temp:
            resenje += 1
            break

    print(z)
    print(resenje)