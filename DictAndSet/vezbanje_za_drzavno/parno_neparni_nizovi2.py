broj = int(input())
niz = list(map(int, input().split(" ")))

resenje = 'da'

for x in range(0, broj):
    if x % 2 == 0 and niz[x] % 2 == 0:
        pass

    elif x % 2 != 0 and niz[x] % 2 != 0:
        pass

    else:
        resenje = 'ne'

print(resenje)