import bisect
broj_takmicara = int(input())
takmicari = list(map(int, input().split()))
takmicari.sort()
razlika = int(input())

resenje = 0

for x in range(0, broj_takmicara):
    index = bisect.bisect_right(takmicari, takmicari[x] + razlika)
    if x != index:
        resenje += abs(index - x - 1)

print(resenje)
