broj = int(input())

lista = []

for x in range(0,broj):
    lista.append(int(input()))

temp = 0
resenje = sum(lista[0:7])
for y in range(1, broj-7):
    lista1 = list(lista[y:y+7])
    suma = sum(lista1)

    if suma < resenje:
        resenje = int(suma)
        temp = int(y)

print(temp)
print(resenje)