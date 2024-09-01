broj_reci = int(input())

srpski = []
engleski = []

for x in range(0, broj_reci):
    engleska_rec, srpska_rec = list(input().split(" "))

    engleski.append(engleska_rec)
    srpski.append(srpska_rec)

broj_pitanja = int(input())

lista = []

for y in range(0, broj_pitanja):
    jezik, rec = list(input().split(" "))

    if jezik == 'sr':
        if rec in engleski:
            index = engleski.index(rec)
            lista.append(srpski[index])
        else:
            lista.append("?")

    elif jezik == 'en':
        if rec in srpski:
            index = srpski.index(rec)
            lista.append(engleski[index])

        else:
            lista.append("?")

print(*lista, sep="\n")