visina, sirina, pomeranje = list(map(int, input().split(' ')))

racun = sirina // pomeranje
udaljenost = sirina - (racun * pomeranje)

resenje = udaljenost / pomeranje

if racun % 2 == 0:

    if resenje == 0.5:
        print(0)

    elif resenje > 0.5:
        print(1)

    else:
        print(-1)


else:
    if resenje == 0.5:
        print(0)
    elif resenje < 0.5:
        print(1)
    else:
        print(-1)