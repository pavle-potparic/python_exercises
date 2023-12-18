import math

broj = int(input())


def pronadji_cinioce(broj):
    cinioci = []
    for i in range(1, broj + 1):
        if broj % i == 0:
            cinioci.append(i)

    return cinioci


def pronadji_parove(broj):
    cinioci = pronadji_cinioce(broj)
    parovi = []

    for i in cinioci:
        for j in cinioci:
            if i * j == broj:
                if i <= j:
                    parovi.append((i, j))

    return parovi


svi_proizvodi_brojeva = pronadji_parove(broj)

resenje = 0

for i in range(0, len(svi_proizvodi_brojeva)):
    temp_resenje = math.gcd(svi_proizvodi_brojeva[i][0], svi_proizvodi_brojeva[i][1])
    if resenje < temp_resenje:
        resenje = temp_resenje

print(resenje)