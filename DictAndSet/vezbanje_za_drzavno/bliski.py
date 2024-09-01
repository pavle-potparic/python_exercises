from bisect import bisect_right, bisect_left

broj, razlika = list(map(int, input().split(' ')))

prvi_niz = list(map(int, input().split(' ')))
drugi_niz = list(map(int, input().split(' ')))

prvi_niz.sort()
drugi_niz.sort()

rezultat = 0

for x in prvi_niz:
    # Pronalazimo najbliži levi i desni indeks za x - razlika i x + razlika
    levo = bisect_left(drugi_niz, x - razlika)
    desno = bisect_right(drugi_niz, x + razlika - 1)
    # Ako postoji bar jedan element između ova dva indeksa, to znači da x ima bliski broj u drugom nizu
    if desno > levo:
        rezultat += 1

print(rezultat)
