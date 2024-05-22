broj = int(input())
resenje = 0
for x in range(0, broj):
    cena, kodmad = list(map(int, input().split(" ")))
    resenje += cena * kodmad

print(resenje)