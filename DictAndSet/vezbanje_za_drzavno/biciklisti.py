import bisect

broj = int(input())

svi_biciklisti = list(map(int, input().split(' ')))

domaci = list(svi_biciklisti[0:4])
gosti = list(svi_biciklisti[4:broj])

domaci.sort()
ukupno_vreme_ekipe = domaci[2]
min_max = input()
gosti.sort()

if min_max == 'max':
    resenje = broj//4
else:
    resenje = 1

for x in range(0, (broj-4) // 4):
    for y in range(0, 2):
        gosti.remove(min(gosti))

    if min_max == 'max':
        if min(gosti) > ukupno_vreme_ekipe:
            resenje -= 1
        gosti.remove(min(gosti))
        index = bisect.bisect_right(gosti, ukupno_vreme_ekipe)
        gosti.remove(gosti[index-1])

    else:
        index1 = bisect.bisect_right(gosti, ukupno_vreme_ekipe)
        if gosti[index1-1] < ukupno_vreme_ekipe:
            resenje += 1
        gosti.remove(gosti[index1-1])
        index2 = bisect.bisect_right(gosti, ukupno_vreme_ekipe)
        gosti.remove(gosti[index2-1])

print(resenje)