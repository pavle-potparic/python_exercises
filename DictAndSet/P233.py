svi_mecevi = []


def unesi_listu_igraca():
    broj_igraca = int(input("Unesi broj igraca: "))
    igraci = input("Unesi imena igraca: ")
    dictionary = dict(zip(range(1, broj_igraca + 1), igraci.split(" ")))
    return dictionary


def ubaci_igrace():
    dict_igraca = unesi_listu_igraca()
    for kljuc, vrednost in dict_igraca.items():
        for redni_broj, igrac in dict_igraca.items():
            if vrednost == igrac:
                pass
            elif igrac + "-" + vrednost in svi_mecevi:
                pass
            else:
                mec = vrednost + "-" + igrac
                svi_mecevi.append(mec)
    return svi_mecevi


def broj_elemenata(dict_igraca_i_pozicija):
    broj_ponavljanja = 0
    for pozicija, igrac in dict_igraca_i_pozicija.items():
        broj_ponavljanja = broj_ponavljanja + 1

    broj_takmicara = broj_ponavljanja

    print(broj_takmicara)
    return 0


ubacivanje_igraca = unesi_listu_igraca()
pokretanje = broj_elemenata(ubacivanje_igraca)
print(pokretanje)
lista_igraca_i_rezultata = ["1221", "3202", "1420", "4212"]


def rezultat_meca(rezultat_i_igrac):
    for informacije in rezultat_i_igrac:
        if informacije[2] == "2":
            if informacije[0] == "1":
                pass
            elif informacije[0] == "2":
                pass
            elif informacije[0] == "3":
                pass
            elif informacije[0] == "4":
                pass
        else:
            if informacije[1] == "1":
                pass
            elif informacije[1] == "2":
                pass
            elif informacije[1] == "3":
                pass
            elif informacije[1] == "4":
                pass

    print()


rezultat_meca(lista_igraca_i_rezultata)

dict = {1: "jedan", 2: "dva", 3: "tri"}
print(len(dict))