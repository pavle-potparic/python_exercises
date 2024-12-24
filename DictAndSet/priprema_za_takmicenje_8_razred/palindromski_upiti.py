broj_karaktera, broj_upita = list(map(int, input().split(' ')))

rec = list(input())

resenje = []

palindrom = 1

for x in range(broj_upita):
    index, slovo = list(input().split(' '))

    rec[int(index)-1] = slovo

    if broj_karaktera % 2 == 0:
        if rec[0:broj_karaktera//2] == rec[broj_karaktera//2:broj_karaktera]:
            resenje.append('DA')

        else:
            resenje.append('NE')

    else:
        if rec[0:broj_karaktera//2 + 1] == rec[broj_karaktera:broj_karaktera//2 - 1: -1]:
            resenje.append('DA')

        else:
            resenje.append('NE')

print(*resenje, sep='\n')