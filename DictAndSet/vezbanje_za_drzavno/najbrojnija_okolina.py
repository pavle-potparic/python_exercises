import bisect

duzina, razlika = list(map(int, input().split(" ")))

niz = list(map(int, input().rstrip().split(' ')))
niz.sort()
temp_niz = list(niz)

index = 1000000
resenje = 0

for x in range(0, duzina):
    desno = bisect.bisect(temp_niz, niz[x] + razlika)
    levo = bisect.bisect_left(temp_niz, niz[x] - razlika)

    broj_okoline = desno - levo

    if broj_okoline > resenje:
        resenje = broj_okoline
        index = niz[x]

print(index, resenje)
