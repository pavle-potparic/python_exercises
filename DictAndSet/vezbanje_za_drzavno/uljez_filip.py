# Učitavanje broja elemenata niza (n) i broja x
n, x = map(int, input().split())
brojevi = list(map(int, input().split(' ')))  # Učitavanje elemenata niza brojevi

# Inicijalizacija niza susx
susx = [0] * (n + 1)

# Popunjavanje niza susx
for i in range(n):
    if brojevi[i] > x:
        susx[i + 1] = susx[i] + 1
    else:
        susx[i + 1] = susx[i]

# Dodavanje broja elemenata manjih od x u susx prolazeći kroz niz unazad
temp = 0
for i in range(n - 1, -1, -1):
    if brojevi[i] < x:
        temp += 1
    susx[i] += temp

# Traženje indeksa sa najmanjom vrednošću u susx
bestpoz = susx.index(min(susx))

# Ispis najbolje pozicije
print(bestpoz)
