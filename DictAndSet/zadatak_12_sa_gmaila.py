perina_brzina = float(input("Koliko se Pera brzo krece? "))
mikina_brzina = float(input("Koliko se Mike brzo krece? "))
vreme = int(input("Koliko je sekundi proslo? "))
rastojanje_nakon_odredjenog_vremena = int(input("Koliko je njihovo rastojanje? "))


def odredi_razdaljinu_izmedju_kuca(pera, mika, sekunde, rastojanje):
    pera_brzina = pera * sekunde
    mika_brzina = mika * sekunde
    razdaljina_izmedju_kuca = mika_brzina + rastojanje - pera_brzina
    if pera_brzina > mika_brzina:
        razdaljina_izmedju_kuca = pera_brzina + rastojanje - mika_brzina

    return razdaljina_izmedju_kuca


odredi_razdaljinu = odredi_razdaljinu_izmedju_kuca(perina_brzina, mikina_brzina, vreme,
                                                   rastojanje_nakon_odredjenog_vremena)
print(odredi_razdaljinu)
