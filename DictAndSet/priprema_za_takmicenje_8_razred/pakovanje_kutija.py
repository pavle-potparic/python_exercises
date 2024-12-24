broj = int(input())

lista = []

for x in range(0, broj):
    dimenzije = list(map(int, input().split(' ')))
    if dimenzije[1] > dimenzije[0]:
        temp = int(dimenzije[0])
        dimenzije[0] = int(dimenzije[1])
        dimenzije[1] = int(temp)

    lista.append(dimenzije)

lista.sort(key=lambda k: (k[2], k[0], k[1]), reverse=True)

resenje = 1

for x1 in range(0, broj):
    resenje = 1
    x = int(x1)
    for y in range(0, broj):
        if x != y:
            if lista[x][0] >= lista[y][0]:
                if lista[x][1] >= lista[y][1]:
                    if lista[x][2] >= lista[y][2]:
                        resenje += 1
                        x = int(y)

                else:
                    if lista[x][0] >= lista[y][1]:
                        if lista[x][1] >= lista[y][0]:
                            if lista[x][2] >= lista[y][2]:
                                resenje += 1
                                x = int(y)

            else:
                if lista[x][0] >= lista[y][1]:
                    if lista[x][1] >= lista[y][0]:
                        if lista[x][2] >= lista[y][2]:
                            resenje += 1
                            x = int(y)

    if x >= broj - resenje:
        break

print(resenje)