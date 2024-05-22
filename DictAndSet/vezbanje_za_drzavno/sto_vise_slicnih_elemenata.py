import bisect
import math
broj = int(input())
niz = list(map(int, input().split(' ')))
razlika = int(input())
niz.sort()
temp_niz = list(niz)

resenje = 0

for x in range(0, broj):
    pocetak = niz[x]
    temp_niz = list(niz)

    levo = bisect.bisect_right(temp_niz, pocetak + razlika)
    duzina = len(niz[x:levo])

    if resenje < duzina:
        resenje = duzina

print(resenje)