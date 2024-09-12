broj, minuti = list(map(int, input().split(' ')))

niz = list(map(int, input().split(" ")))

resenje = []

for x in range(0, broj):
    temp_minuti = int(minuti) - niz[x]
    temp_resenje = 0
    if temp_minuti > -1:
        temp_resenje = 1

        for y in range(x + 1, broj):
            temp_minuti -= niz[y]

            if temp_minuti >= 0:
                temp_resenje += 1

    resenje.append(temp_resenje)

print(max(resenje))