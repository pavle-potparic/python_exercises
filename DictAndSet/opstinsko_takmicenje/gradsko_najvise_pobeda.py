lista = []

for x in range(0, 7):
    pobeda, poraz = input().split(" ")
    lista.append(pobeda)

for covek in lista:
    broj = list(filter(lambda y: y == covek, lista))
    if len(broj) == 3:
        prvi = broj[0]

    if len(broj) == 2:
        drugi = broj[0]

print(prvi)
print(drugi)
