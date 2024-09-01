trazeni_niz = input()
dati_niz = list(input())

resenje = 0

temp_trazeni_niz = set(trazeni_niz)

for x in temp_trazeni_niz:
    resenje += dati_niz.count(x) - trazeni_niz.count(x)

print(resenje)
