broj = int(input())

deo_liste = list("+"*broj)
lista = [deo_liste[:] for _ in range(broj)]

for x in range(0, broj):
    for y in range(0, broj):
        if x == 0 or x == broj-1:
            if y != 0 and y != broj-1:
                lista[x][y] = "-"
        if x != 0 and x != broj-1:
            if y == 0 or y == broj-1:
                lista[x][y] = "|"
        if x != 0 and x != broj-1:
            if y != 0 and y != broj-1:
                lista[x][y] = "."

    print("".join(lista[x]))
