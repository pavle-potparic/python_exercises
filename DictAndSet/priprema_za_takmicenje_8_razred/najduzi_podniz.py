broj = int(input())

niz = list(map(int, input().split()))

nula_jedan = [i for i, broj in enumerate(niz) if broj % 2 == 0]

resenja = []

for z in range(0, len(nula_jedan) - 2):
    if z == 0:
        if z == len(nula_jedan) - 3:
            resenja.append(nula_jedan[z+2] + 1)

        else:
            resenja.append(nula_jedan[z+2] + 1)

    else:
        if z == len(nula_jedan) - 3 and z != 0:
            resenja.append(nula_jedan[z+2] - nula_jedan[z-1])

        else:
            resenja.append((nula_jedan[z + 3]) - nula_jedan[z-1] - 1)

print(max(resenja))