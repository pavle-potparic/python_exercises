dinar, evro = list(map(int, input().split(" ")))
din_suma, eur_suma = list(map(int, input().split(" ")))

musterije = int(input())

lista = list(map(int, input().split(" ")))

kp = input()

dinar_propusteno = 0
evro_propusteno = 0

for x in range(0, musterije):
    if kp[x] == "K":
        if eur_suma - lista[x] < 0:
            evro_propusteno += 1

        else:
            din_suma += lista[x] * evro
            eur_suma -= lista[x]

    else:
        if din_suma - lista[x] < 0:
            dinar_propusteno += 1

        else:
            din_suma -= lista[x] * dinar
            eur_suma += lista[x]

print(dinar_propusteno, evro_propusteno, din_suma, eur_suma)
