broj = int(input())
transformacija = int(input())

resenje = 0

for x in range(0, transformacija):
    resenje = broj * broj + 1
    broj = resenje

broj = str(broj)

lista = list(broj)
print(lista[-3], lista[-2], lista[-1], sep='')
print(broj)