import bisect

broj_rupa = int(input())
rupe = list(map(int, input().split(' ')))
rupe.sort()

broj_zeceva = int(input())
zecevi = list(map(int, input().split(' ')))

resenje = 0

for x in zecevi:
    temp = bisect.bisect_right(rupe, x)

    if temp >= broj_rupa:
        index = abs(x - rupe[temp-1])

    else:
        index1 = abs(x - rupe[temp-1])
        index2 = abs(x - rupe[temp])

        index = index1 if index1 < index2 else index2 

    if index > resenje:
        resenje = int(index)

print(resenje)