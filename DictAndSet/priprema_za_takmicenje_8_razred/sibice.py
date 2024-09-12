broj = int(input())
niz = list(map(int, input().split(" ")))
stranica = sum(niz) / 4


def pronadji_stranicu(lista, cetvrtina_obima):
    temp_stranica = cetvrtina_obima
    maximum = max(lista)

    if maximum == cetvrtina_obima:
        lista.remove(maximum)
        return True

    else:
        if cetvrtina_obima - maximum in lista:
            lista.remove(maximum)
            lista.remove(cetvrtina_obima - maximum)
            return True

        else:
            while temp_stranica > 1:
                minimum = min(lista)
                temp_stranica -= minimum
                lista.remove(minimum)

            if temp_stranica == 0:
                return True

        return False


if sum(niz) % 4 == 0:
    resenje = 0
    for x in range(0, 4):
        pokretanje = pronadji_stranicu(niz, stranica)
        if not pokretanje:
            print(0)
            break

        else:
            resenje += 1

    if resenje == 4:
        print(1)

else:
    print(0)
