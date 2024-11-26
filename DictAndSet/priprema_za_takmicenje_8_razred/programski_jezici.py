broj = int(input())

dictionary = {}

for x in range(0, broj):
    jezik, ocena = input().split(' ')

    if jezik in dictionary:
        dictionary[jezik][0] += int(ocena)
        dictionary[jezik][1] += 1

    else:
        dictionary[jezik] = [int(ocena), 1]

lista = []

for key, value in dictionary.items():
    zaokruzen_broj = int(value[0] / value[1] * 100) / 100

    if zaokruzen_broj == int(zaokruzen_broj):
        zaokruzen_broj = str(zaokruzen_broj) + '0'

    lista.append([key, zaokruzen_broj])


lista.sort(key=lambda y: y[0])

for kraj in lista:
    print(*kraj)