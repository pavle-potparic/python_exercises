recenica = input()

if "(" in recenica and ")" in recenica:
    otvorena = recenica.index("(")
    recenica = recenica[::-1]
    zatvorena = recenica.index(")")

    recenica = recenica[::-1]

    resenje = len(recenica) - (zatvorena + 1)

    bez_zagrada = list(recenica)

    for x in range(otvorena, zatvorena):
        bez_zagrada.remove(bez_zagrada[otvorena])

    print(*bez_zagrada)
    print(otvorena, zatvorena)

else:
    print(recenica)