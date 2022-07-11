lista_pokusaja = [160, 148, 120, 140, 173, 115]


def predjeni_nivoi(vreme_nivoa, vreme_igraca):
    koliko_nivoa_treba_da_se_predje = int(input("Koliko nivoa je podrebno preci? "))
    if koliko_nivoa_treba_da_se_predje * 10 >= vreme_nivoa - 10:
        while koliko_nivoa_treba_da_se_predje * 10 >= vreme_nivoa - 10:
            koliko_nivoa_treba_da_se_predje = int(input("Koliko nivoa je podrebno preci? "))
    nina_nivoi = 0
    mara_nivoi = 0
    ninin_red_da_igra = 1
    for score in vreme_igraca:
        if koliko_nivoa_treba_da_se_predje == 0:
            break
        if ninin_red_da_igra == 1:
            ninin_red_da_igra = 0
            if vreme_nivoa > score:
                vreme_nivoa = vreme_nivoa - 10
                nina_nivoi = nina_nivoi + 1
                koliko_nivoa_treba_da_se_predje -= 1
        else:
            ninin_red_da_igra = 1
            if vreme_nivoa > score:
                vreme_nivoa = vreme_nivoa - 10
                mara_nivoi = mara_nivoi + 1
                koliko_nivoa_treba_da_se_predje -= 1

    print("Ninini predjeni nivoi:", nina_nivoi, "Marini predjeni nivoi: ", mara_nivoi)


predjeni_nivoi(150, lista_pokusaja)
