resenje = input()

lista = []

while resenje != "gotovo":
    lista.append(resenje)
    resenje = input()

kraj = lista[-1]
lista.pop()

join_lista = ", ".join(lista)


if len(join_lista) > 0:
    rezultat = join_lista + " i " + kraj

else:
    rezultat = kraj

print(rezultat)
