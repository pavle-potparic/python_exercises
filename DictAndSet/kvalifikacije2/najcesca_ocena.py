n = int(input())
lista = []

for x in range(0, n):
    lista.append(int(input()))

petice = list(filter(lambda y: y >= 90, lista))
cetvorke = list(filter(lambda z: 77 <= z <= 89, lista))
tri = list(filter(lambda z: 64 <= z <= 76, lista))
dva = list(filter(lambda z: 51 <= z <= 63, lista))
kec = list(filter(lambda z: 0 <= z <= 50, lista))

resenje = [len(kec), len(dva), len(tri), len(cetvorke), len(petice)]

maximum = max(resenje)

print(resenje.index(maximum) + 1)