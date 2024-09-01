broj_redova, broj_elemenata = list(map(int, input().split(" ")))

lista = []
zapremina = 0

for x in range(0, broj_redova):
    red = list(map(int, input().split(" ")))
    zapremina += sum(red)
    lista.append(red)

povrsina = 0
broj_nula = 0

for y in range(0, broj_elemenata):
    najveci = 0
    for z in range(0, broj_redova):
        if najveci < lista[z][y]:
            najveci = lista[z][y]

        if z == 0:
            povrsina += lista[z][y]
            if najveci != lista[z][y]:
                povrsina += najveci - lista[z][y]

        if y == 0 or y == broj_elemenata - 1:
            povrsina += lista[z][y]
            if lista[z][y] != max(lista[z]):
                povrsina += max(lista[z]) - lista[z][y]

        if lista[z][y] == 0:
            broj_nula += 1

    povrsina += najveci

povrsina += broj_redova * broj_elemenata * 2 - broj_nula * 2

print(zapremina, povrsina)