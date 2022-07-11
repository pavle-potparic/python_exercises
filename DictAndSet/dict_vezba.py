def unesi_igrace():
    igraci = input("Unesi igrace")
    lista_igraca = igraci.split(" ")
    return lista_igraca

def nova_metoda_za_igrace():
    lista_igraca = unesi_igrace()
    for igrac in lista_igraca:
        print("igrac: ", igrac)


nova_metoda_za_igrace()