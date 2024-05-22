jedan = int(input())

lista1 = []

for x in range(0, jedan):
    lista1.append(list(map(int, input().split(" "))))

dva = int(input())

lista2 = []

for x in range(0, dva):
    lista2.append(list(map(int, input().split(" "))))

granica = int(input())

lista1.sort(key=lambda k: (k[0], -k[1]), reverse=True)
lista2.sort(key=lambda k: (k[0], -k[1]), reverse=True)

resenje = lista1[0][1] + lista2[0][1]
broj = 1
while resenje > granica:
    resenje 