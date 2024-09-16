broj_drzava = int(input())

drzave = []


for x in range(0, broj_drzava):
    drzave.append(int(input()))

trazena_zemlja = int(input())
zemlja_koja_glasa = int(input())

drzave[trazena_zemlja - 1] += broj_drzava - 1
srbija = drzave[trazena_zemlja - 1]

plus = 0
if drzave[zemlja_koja_glasa - 1] > srbija:
    plus = 1

drzave.remove(drzave[zemlja_koja_glasa - 1])


drzave.sort()

temp = broj_drzava - 2
lista = []

for z in range(0, broj_drzava - 1):
    if z not in lista:
        if drzave[z] + temp > srbija and z != broj_drzava - 2:
            if len(lista) == 0:
                drzave[broj_drzava - 2] += temp
                drzave[z] += 1
                temp -= 1
                lista.append(broj_drzava - 2)
            else:
                najmanja = min(lista) - 1
                if z != najmanja:
                    drzave[najmanja] += temp
                    drzave[z] += broj_drzava - z
                    temp -= 1
                    lista.append(drzave[najmanja])

                else:
                    drzave[z] += temp
                    temp -= 1
        else:
            drzave[z] += temp
            temp -= 1

resenje = list(filter(lambda q: q > srbija, drzave))
print(drzave)
print(len(resenje) + plus)
