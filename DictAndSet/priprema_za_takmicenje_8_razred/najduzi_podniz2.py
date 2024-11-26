n = int(input())
elementi = list(map(int, input().split()))

max_duzina = 0
l = 0
d = 0
broj_parnih = 0

while d < n:
    if elementi[d] % 2 == 0:
        broj_parnih += 1
    while broj_parnih > 3:
        if elementi[l] % 2 == 0:
            broj_parnih -= 1
        l += 1
    max_duzina = max(max_duzina, d - l + 1)
    d += 1

print(max_duzina)