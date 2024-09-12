cena = int(input())
uplata = int(input())

kusur = uplata - cena

lista = [0, 0, 0, 0, 0, 0, 0]

lista2 = [100, 50, 20, 10, 5, 2, 1]

for x in range(0, 7):
    if kusur >= lista2[x]:
        broj = kusur // lista2[x]
        lista[x] += broj
        kusur -= lista2[x] * broj

    if kusur == 0:
        break

lista = lista[::-1]

print(*lista, sep='\n')