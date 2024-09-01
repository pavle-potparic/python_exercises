broj , k = list(map(int, input().split(' ')))

niz = list(map(int, input().split(' ')))
resenje = 0
promena = 0
for x in range(0, broj):
    temp = k - niz[x]
    if promena == 0:
        for y in range(x+1, broj):
            if temp - niz[y] >= 0:
                temp -= niz[y]
                promena += 1
            else:
                break

        resenje += 1
    else:
        promena -= 1

print(resenje)