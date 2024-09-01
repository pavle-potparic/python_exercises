n = int(input())
lista = []

for x in range(0, n):
    lista.append(list(map(int, input().split(" "))))

redosled = []

for y in range(0, n):
    redosled.append(int(input()))

for z in range(0, n):
    trenutni_ucenik = redosled[z]
    prosek = sum(lista[trenutni_ucenik - 1]) / len(lista[trenutni_ucenik - 1])
    prosek2 = round(prosek, 2)
    print(*lista[trenutni_ucenik - 1], f"{prosek2:.2f}")