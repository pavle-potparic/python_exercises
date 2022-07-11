lista = [1, 2, 3, 4, 5, 6, 7]
korisnikov_odgovor = input("Unesi sta hoces da ubacis u listu. ")

if korisnikov_odgovor.isdigit():
    korisnikov_odgovor = int(korisnikov_odgovor)


def append(lista_za_apendovanje, append_parametar):
    appendovana_lista = lista_za_apendovanje + [append_parametar]
    return appendovana_lista


pokretanje = append(lista, korisnikov_odgovor)
print(pokretanje)
