godine = int(input())
broj_dana = int(input())

cena_karte = 0

if 5 <= godine < 13:
    cena_karte = 2800

elif 13 < godine < 65:
    cena_karte = 3500

elif godine > 64:
    cena_karte = 3200


if broj_dana > 10:
    resenje = cena_karte * 10
    resenje += cena_karte // 2 * (broj_dana - 10)
    print(resenje)

else:
    print(cena_karte * broj_dana)
