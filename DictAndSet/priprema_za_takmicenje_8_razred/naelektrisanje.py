from itertools import combinations

broj = int(input())
niz = list(map(int, input().split(' ')))

resenje = 1

for i in range(1, broj + 1):
    for kombinacija in combinations(niz, i):
        if sum(list(kombinacija)) == 0:
            resenje += 1

print(resenje)
