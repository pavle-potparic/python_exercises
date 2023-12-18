from decimal import Decimal
import math

n = int(input())
k = int(input())

lista = []

for x in range(0, k):
    lista.append(int(input()))

prosek = float(input())

resenje = prosek * n

resenje1 = round(resenje, 0)

resenje1 = (resenje1 - sum(lista)) / (n - k)

na_dve_decimale = Decimal(str(resenje1))
zaokrugljen = na_dve_decimale.quantize(Decimal('.01'))

print(zaokrugljen)