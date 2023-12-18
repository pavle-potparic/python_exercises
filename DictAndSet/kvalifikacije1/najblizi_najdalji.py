broj1 = int(input())
broj2 = int(input())
broj3 = int(input())
broj4 = int(input())

lista = [broj1, broj2, broj3, broj4]

lista.sort()

rastojanje1 = lista[1] - lista[0]
rastojanje2 = rastojanje1
temp = lista[2] - lista[1]
if rastojanje2 > temp:
    rastojanje2 = temp

rastojanje3 = temp
rastojanje4 = lista[3] - lista[2]

if rastojanje4 < rastojanje3:
    rastojanje3 = rastojanje4

lista_resenja = [rastojanje1, rastojanje2, rastojanje3, rastojanje4]

max = max(lista_resenja)

max_lista = []

for z in range(0, 4):
    if lista_resenja[z] == max:
        max_lista.append(lista[z])


for x in range(0, len(max_lista)):
    print(max_lista[x])
