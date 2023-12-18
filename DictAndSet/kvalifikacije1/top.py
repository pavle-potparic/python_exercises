pozicija_topa = input()

broj_pitanja = int(input())

for x in range(0, broj_pitanja):
    pozicija = input()
    if pozicija[0] == pozicija_topa[0]:
        print("DA")

    elif pozicija[1] == pozicija_topa[1]:
        print("DA")

    else:
        print("NE")