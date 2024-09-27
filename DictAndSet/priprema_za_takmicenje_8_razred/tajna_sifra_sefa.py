broj = int(input())

niz = list(map(int, input().split(' ')))

temp = list(niz)

niz.sort()

counter = 0

while True:

    lista = [0] + temp
    lista[0] = int(lista[-1])
    lista.pop(-1)

    counter += 1

    if lista == niz:
        break

print(counter)