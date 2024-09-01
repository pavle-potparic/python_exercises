duzina, trazeni_broj_oscilacija = list(map(int, input().split(' ')))

niz = list(map(float, input().split(' ')))

resenje = 0

if niz[0] > niz[1]:
    veci_manji = False

else:
    veci_manji = True

temp_resenje = 1
povecanje = 0

for x in range(0, duzina - 1):
    if not veci_manji:
        if niz[x] > niz[x + 1]:
            temp_resenje += 1
            povecanje = 1

        else:
            if temp_resenje > resenje:
                resenje = int(temp_resenje)

            temp_resenje = 1
            povecanje = 0


    else:
        if niz[x] < niz[x + 1]:
            temp_resenje += 1
            povecanje = 1

        else:
            if temp_resenje > resenje:
                resenje = int(temp_resenje)

            temp_resenje = 1
            povecanje = 0

    if povecanje == 1:
        veci_manji = not veci_manji

    else:
        if niz[x+1] > niz[x + 2]:
            veci_manji = False
        else:
            veci_manji = True

if temp_resenje > resenje:
    resenje = int(temp_resenje)

if resenje >= trazeni_broj_oscilacija:
    stampanje = 'da'

else:
    stampanje = 'ne'

print(stampanje)
print(resenje)
