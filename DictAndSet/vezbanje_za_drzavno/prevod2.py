broj_reci = int(input())

srpski = []
engleski = []

for x in range(0, broj_reci):
    engleska_rec, srpska_rec = list(input().split(" "))

    engleski.append(engleska_rec)
    srpski.append(srpska_rec)

broj_pitanja = int(input())

srpski_recnik = dict(zip(engleski, srpski))
engleski_recnik = dict(zip(srpski, engleski))

resenja = []

for x in range(0, broj_pitanja):
    jezik, rec = input().split(" ")

    if jezik == "sr":
        if rec in srpski_recnik:
            resenja.append(srpski_recnik[rec])
        else:
            resenja.append("?")

    else:
        if rec in engleski_recnik:
            resenja.append(engleski_recnik[rec])

        else:
            resenja.append("?")

print(*resenja, sep="\n")