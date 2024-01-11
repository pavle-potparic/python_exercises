broj_redova = int(input())

lista = []

for x in range(0, broj_redova):
    lista.append(int(input()))

resenje = list(map(lambda y: y // 2, lista))

print(sum(resenje))