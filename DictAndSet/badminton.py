def unesi_igrace():
    broj_igraca = int(input("Unesi broj igraca: "))
    igraci = input("Unesi imena igraca: ")
    lista_igraca = igraci.split(" ")

    if len(lista_igraca) != broj_igraca:
        lista_igraca = unesi_igrace()

    return lista_igraca


def vrati_dict_igraca():
    lista_igraca = unesi_igrace()

    dict_igraca = dict(zip(range(1, len(lista_igraca) + 1), lista_igraca))

    return dict_igraca


def unesi_broj_odigranih_meceva():
    broj_meceva = int(input("Unesi broj meceva: "))
    lista_meceva = []

    while broj_meceva > 0:
        mec = input("Unesi podatke o mecu (prvo redni brojevi igraca koji su odigrali, a zatim rezultat): ")
        podaci_o_mecu = mec.split(" ")
        podaci_o_mecu_convert_to_int = [int(podaci_o_mecu[0]), int(podaci_o_mecu[1]), int(podaci_o_mecu[2]),
                                        int(podaci_o_mecu[3])]
        lista_meceva.append(podaci_o_mecu_convert_to_int)
        broj_meceva = broj_meceva - 1

    return lista_meceva


def igraci_sa_najvise_pobeda(dict_igraci, lista_pobeda):
    max_pobeda = max(lista_pobeda)
    max_pobednici = []

    for pozicija in range(0, len(lista_pobeda)):
        if lista_pobeda[pozicija] == max_pobeda:
            podaci_o_pobedniku = [dict_igraci[pozicija + 1], max_pobeda]
            max_pobednici.append(podaci_o_pobedniku)

    return max_pobednici


def prikazi_igrace_sa_najvise_pobeda(dict_igraca, lista_meceva):
    pobede = []
    broj_ponavljanja = 0
    while broj_ponavljanja != len(dict_igraca):
        pobede.append(0)
        broj_ponavljanja = broj_ponavljanja + 1

    for mec in lista_meceva:
        if mec[2] == 2:
            pobede[mec[0] - 1] = pobede[mec[0] - 1] + 1
        else:
            pobede[mec[1] - 1] = pobede[mec[1] - 1] + 1

    return igraci_sa_najvise_pobeda(dict_igraca, pobede)


def prikazi_meceve_koji_trebaju_da_se_odigraju(mec, dict_igraca):
    svi_mecevi = []
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


# Jelena-Ana Ana-Kaca

def neodigrani_mecevi(svi_mecevi, lista_odigranih_meceva):
    for mec in lista_odigranih_meceva:
        kombinacija_meca = [mec[0], mec[1]]
        if mec[0] > mec[1]:
            kombinacija_meca = [mec[1], mec[0]]

        svi_mecevi.remove(kombinacija_meca)

    return svi_mecevi


def generisi_sve_meceve(broj_igraca):
    mecevi = []
    for igrac in range(1, broj_igraca + 1):
        protivnik = igrac + 1
        while protivnik <= broj_igraca:
            mec = [igrac, protivnik]
            mecevi.append(mec)
            protivnik = protivnik + 1

    return mecevi


def odstampaj_meceve_koji_se_nisu_odigrali(dict_igraca, mecevi_koji_se_nisu_odigrali):
    for mec in mecevi_koji_se_nisu_odigrali:
        print(dict_igraca[mec[0]], "-", dict_igraca[mec[1]])


def start_app():
    dict_igraca = vrati_dict_igraca()
    lista_meceva = unesi_broj_odigranih_meceva()
    print("Pobede: ")
    igrac_sa_najvise_pobeda = prikazi_igrace_sa_najvise_pobeda(dict_igraca, lista_meceva)
    print(igrac_sa_najvise_pobeda)
    print("Mecevi: ")
    generisani_mecevi = generisi_sve_meceve(len(dict_igraca))
    mecevi_koji_se_nisu_odigrali = neodigrani_mecevi(generisani_mecevi, lista_meceva)
    odstampaj_meceve_koji_se_nisu_odigrali(dict_igraca, mecevi_koji_se_nisu_odigrali)


# lista_odigranih_meceva = [[1, 2, 2, 1], [3, 2, 0, 2], [1, 4, 2, 0], [4, 2, 1, 2]]
#
# svi_mecevi = svi_mecevi(4)
#

# print(neodigrani_mecevi)

start_app()
