broj = int(input())
niz = list(map(int, input().split()))

broj_intervala = 0
suma = 0
dictionary = {0: 1}

for promena in niz:
    suma += promena
    if suma in dictionary:
        broj_intervala += dictionary[suma]
        dictionary[suma] += 1
    else:
        dictionary[suma] = 1

print(broj_intervala)


