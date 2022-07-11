# 3 T = 150 V : 160 148 120 140 173 115

def predjeni_nivo(min_vreme, ostvareno_vreme):
    if ostvareno_vreme <= min_vreme:
        return True
    return False

def prikazi_rezultate(broj_niova: int, min_vreme: int, ostvarena_vremena: list):
    nina_predjeni_nivo = 0
    mara_predjeni_nivo = 0

    index = 0

    while broj_niova > 0:
        uspesan_pokusaj = predjeni_nivo(min_vreme, ostvarena_vremena[index])
        if uspesan_pokusaj:
            if index % 2 == 0:
                nina_predjeni_nivo += 1
            else:
                mara_predjeni_nivo += 1
            min_vreme -= 10
            broj_niova -= 1

        index += 1

    print("Nina nivoi: ", nina_predjeni_nivo, "Mara nivoi: ", mara_predjeni_nivo)


prikazi_rezultate(3, 150, [160, 148, 120, 140, 173, 115])
