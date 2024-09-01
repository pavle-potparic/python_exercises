dan = int(input())
mesec = int(input())

if 3 <= mesec <= 6:
    if mesec == 3:
        if dan >= 20:
            print("p")
        else:
            print("z")

    elif mesec == 6:
        if dan < 21:
            print("p")

        else:
            print("l")

elif 6 <= mesec <= 9:
    if mesec == 6:
        if dan >= 21:
            print("l")
        else:
            print("p")

    elif mesec == 9:
        if dan < 23:
            print("l")

        else:
            print("j")


elif 9 <= mesec <= 12:
    if mesec == 9:
        if dan >= 23:
            print("j")
        else:
            print("l")

    elif mesec == 12:
        if dan < 21:
            print("j")

        else:
            print("z")

else:
    print("z")
