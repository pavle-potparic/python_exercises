import math
broj = int(input())
konopci = list(map(int, input().split(" ")))

konopci.sort()

resenje = []

for x in range(0, broj):
    temp = konopci[x]
    konopci.remove(temp)
    resenje.append(math.gcd(*konopci))
    konopci.append(temp)
    konopci.sort()

print(max(resenje))