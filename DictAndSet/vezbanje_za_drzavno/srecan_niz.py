n = int(input())
pocetno = list(map(int, input().split()))

brojevi = pocetno.copy()

while 1 in brojevi:
    brojevi[brojevi.index(1)] = 0

sve_nule = True

for i in brojevi:
    if i != 0:
        sve_nule = False
        break


def nzd():
    a = brojevi.copy()
    delilac = 2
    nzd = 1

    while delilac <= min(a):
        deljivo = True
        for i in a:
            if i % delilac != 0:
                deljivo = False
                break

        if deljivo:
            for i in range(len(a)):
                a[i] = a[i] // delilac
            nzd = nzd * delilac

        else:
            delilac += 1
    return nzd


if sve_nule:
    print(*brojevi)

elif nzd() > 1:
    print(*brojevi)

else:
    brojevi1 = brojevi.copy()
    brojevi2 = brojevi.copy()
    brojevi3 = brojevi.copy()
    brojevi4 = brojevi.copy()
    brojevi5 = brojevi.copy()
    zbir, zbir1, zbir2, zbir3, zbir4, zbir5 = 0, 0, 0, 0, 0, 0

    for i in range(len(brojevi)):
        if brojevi[i] % 2 != 0:
            brojevi[i] = brojevi[i] + 1

    for i in range(len(brojevi1)):
        if brojevi1[i] % 3 != 0:
            if brojevi1[i] % 3 < 3 - (brojevi1[i] % 3):
                brojevi1[i] = brojevi1[i] - (brojevi1[i] % 3)
            else:
                brojevi1[i] = brojevi1[i] + 3 - (brojevi1[i] % 3)

    for i in range(len(brojevi2)):
        if brojevi2[i] % 5 != 0:
            if brojevi2[i] % 5 < 5 - (brojevi2[i] % 5):
                brojevi2[i] = brojevi2[i] - (brojevi2[i] % 5)
            else:
                brojevi2[i] = brojevi2[i] + 5 - (brojevi2[i] % 5)

    for i in range(len(brojevi3)):
        if brojevi3[i] % 7 != 0:
            if brojevi3[i] % 7 < 7 - (brojevi3[i] % 7):
                brojevi3[i] = brojevi3[i] - (brojevi3[i] % 7)
            else:
                brojevi3[i] = brojevi3[i] + 7 - (brojevi3[i] % 7)

    for i in range(len(brojevi4)):
        if brojevi4[i] % 11 != 0:
            if brojevi4[i] % 11 < 11 - (brojevi4[i] % 11):
                brojevi4[i] = brojevi4[i] - (brojevi4[i] % 11)
            else:
                brojevi4[i] = brojevi4[i] + 11 - (brojevi4[i] % 11)

    for i in range(len(brojevi5)):
        if brojevi5[i] % 13 != 0:
            if brojevi5[i] % 13 < 13 - (brojevi5[i] % 13):
                brojevi5[i] = brojevi5[i] - (brojevi5[i] % 13)
            else:
                brojevi5[i] = brojevi5[i] + 13 - (brojevi5[i] % 13)

    for i in range(len(pocetno)):
        zbir += abs(brojevi[i] - pocetno[i])
        zbir1 += abs(brojevi1[i] - pocetno[i])
        zbir2 += abs(brojevi2[i] - pocetno[i])
        zbir3 += abs(brojevi3[i] - pocetno[i])
        zbir4 += abs(brojevi4[i] - pocetno[i])
        zbir5 += abs(brojevi5[i] - pocetno[i])

    if zbir == min(zbir, zbir1, zbir2, zbir3, zbir4, zbir5):
        print(*brojevi)
    elif zbir1 == min(zbir, zbir1, zbir2, zbir3, zbir4, zbir5):
        print(*brojevi1)
    elif zbir2 == min(zbir, zbir1, zbir2, zbir3, zbir4, zbir5):
        print(*brojevi2)
    elif zbir3 == min(zbir, zbir1, zbir2, zbir3, zbir4, zbir5):
        print(*brojevi3)
    elif zbir4 == min(zbir, zbir1, zbir2, zbir3, zbir4, zbir5):
        print(*brojevi4)
    else:
        print(*brojevi5)
