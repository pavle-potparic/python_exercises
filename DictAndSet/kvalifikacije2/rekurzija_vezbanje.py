lista = [1, 2, 3, 4, 5]

duzina_niz = len(lista) - 1
resenje = 0


def pronadji_sumu(lista, duzina_niz):
    global resenje
    resenje += lista[duzina_niz]
    duzina_niz -= 1

    if duzina_niz == -1:
        return 0

    pronadji_sumu(lista, duzina_niz)


pronadji_sumu(lista, duzina_niz)
print(resenje)
