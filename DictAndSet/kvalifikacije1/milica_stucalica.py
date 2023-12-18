broj_prekidaca = int(input())
lista_prekidaca = list(map(int, input().split(" ")))
broj_kliktaja = int(input())
kliktaji = list(map(int, input().split(" ")))

resenje = 0

lista = list(lista_prekidaca)

suma = sum(lista_prekidaca)

if suma == 0:
    resenje += 1

for klik in kliktaji:
    if lista[klik] == 1:
        lista[klik] = 0
        suma -= 1

    else:
        lista[klik] = 1
        suma += 1

    if suma == 0:
        resenje += 1

print(resenje)
