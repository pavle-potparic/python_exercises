k = int(input())
m = int(input())
i = int(input())
j = int(input())

pozicija = m * (i - 1) + j

broj_punih_ekipa = pozicija // k

resenje = pozicija - (broj_punih_ekipa * k)

if resenje == 0:
    resenje = k

print(resenje)