import math
red, kolone = list(map(int, input().rstrip().split(" ")))
sekunde = int(input().rstrip())

linija = list(str('.' * kolone))

lista = []

for x in range(0, red):
    lista.append(list(linija))

while True:
    ulaz = input()
    if ulaz == '':
        break

    lopta = list(map(int, ulaz.rstrip().split(' ')))

    if 0 <= lopta[0] + lopta[2] * sekunde < len(lista) and 0 <= lopta[1] + lopta[3] * sekunde < len(lista[0]):
        lista[lopta[0] + lopta[2] * sekunde][lopta[1] + lopta[3] * sekunde] = "#"


for x in lista:
    print(*x, sep='')