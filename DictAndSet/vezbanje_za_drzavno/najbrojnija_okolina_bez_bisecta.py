duzina, razlika = list(map(int, input().split(' ')))

niz = list(map(int, input().rstrip().split(' ')))
niz.sort()
temp_niz = list(niz)

index = 0
resenje = 0

for x in range(0, duzina):
    temp_niz = list(niz)
    da_li_postoji_desno = 0
    broj = niz[x]
    if broj + razlika in niz:
        desno = niz.index(broj + razlika)
        da_li_postoji_desno = 1
    else:
        temp_niz.append(broj + razlika)
        temp_niz.sort()
        desno = temp_niz.index(broj + razlika)

    if broj - razlika in niz:
        levo = temp_niz.index(broj - razlika)
    else:
        temp_niz.append(broj - razlika)
        temp_niz.sort()
        levo = temp_niz.index(broj - razlika)
    if da_li_postoji_desno == 1:
        okolina = len(niz[levo:desno + 1])
    else:
        okolina = len(niz[levo:desno])
    if okolina > resenje:
        resenje = okolina
        index = broj

print(index, resenje)
