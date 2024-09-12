broj = int(input())

niz = list(map(int, input().split(' ')))

k = int(input())

lista = [(niz[x], niz[y]) for x in range(0, broj) for y in range(0, broj) if abs(niz[x] - niz[y]) <= k and x != y]

print(len(lista) // 2)