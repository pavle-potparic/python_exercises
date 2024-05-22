import math

x_krojac, y_krojac = list(map(int, input().split(" ")))
broj = int(input())

lista = []

for x in range(0, broj):
    if x == 0:
        x_a, y_a = list(map(int, input().split(" ")))

    else:
        lista.append(list(map(int, input().split(" "))))

resenje = 0

for z in range(0, len(lista)):
    if math.sqrt((x_a - lista[z][0]) * (x_a - lista[z][0]) + (y_a - lista[z][1]) * (y_a - lista[z][1])) < math.sqrt((x_krojac - lista[z][0]) * (x_krojac - lista[z][0]) + (y_krojac - lista[z][1]) * (y_krojac - lista[z][1])):
        if math.sqrt((x_a - lista[z][0]) * (x_a - lista[z][0]) + (y_a - lista[z][1]) * (y_a - lista[z][1])) < math.sqrt((x_krojac - x_a) * (x_krojac - x_a) + (y_krojac - y_a) * (y_krojac - y_a)):
            resenje += 1

print(resenje)