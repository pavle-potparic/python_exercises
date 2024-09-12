broj = int(input())

biciklisti = list(map(int, input().split(' ')))

min_max = input()

domaci = biciklisti[:4]
gosti = biciklisti[4:]

domaci.sort()

if min_max == 'max':
    resenje = list(filter(lambda x: x > domaci[2], gosti))

    rezultat = len(resenje) // 2

    if rezultat > broj // 4:
        print(1)

    else:
        print(broj // 4 - rezultat)

else:
    resenje = list(filter(lambda y: y < domaci[2], gosti))

    rezultat = len(resenje) // 3

    if rezultat >= broj // 4:
        print(broj // 4)

    else:
        print(1 + rezultat)
