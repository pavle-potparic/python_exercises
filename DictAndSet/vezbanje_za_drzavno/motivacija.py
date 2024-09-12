lista = []

for x in range(0, 5):
    lista.append(int(input()))

prosek = sum(lista) / 5

if round(prosek - (sum(lista) // 5), 1) >= 0.4:
    print(int(prosek) + 1)

else:
    print(int(prosek))