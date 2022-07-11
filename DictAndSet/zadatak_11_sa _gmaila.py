brzina = int(input("Koliko se auto krece brzo? "))
duzina_puta = int(input("Kolika je duina puta? "))


def izracunavanje_prelaska_puta(s, v):
    duzina_puta_izrazena_u_satima = v / s
    brisanje_zareza = str(duzina_puta_izrazena_u_satima).replace(".", ":")
    broj_nula_na_kraju = 5 - len(str(brisanje_zareza))
    duzina_puta_izrazena_u_satima = str(brisanje_zareza) + "0" * broj_nula_na_kraju
    return duzina_puta_izrazena_u_satima


pokretanje = izracunavanje_prelaska_puta(brzina, duzina_puta)
print(pokretanje)
