import math

ulaz = int(input())
resenja = []

for x in range(0, ulaz):
    a, b = list(map(int, input().split(' ')))
    counter = 0
    broj = 2
    lista = []

    while counter != b:

        do_korena = list(range(2, int(math.sqrt(broj))+1))

        provera = list(filter(lambda z: broj % z == 0, do_korena))

        if broj == 2 or broj == 3:
            lista.append(broj)
            counter += 1

        elif len(provera) == 0:
            counter += 1
            lista.append(broj)

        broj += 1

    resenja.append(sum(lista[a - 1:]))

print(*resenja, sep='\n')