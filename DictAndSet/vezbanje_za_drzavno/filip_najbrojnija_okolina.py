import bisect

n, d = map(int, input().split())
brojevi = list(map(int, input().rstrip().split()))  # Čitamo celu liniju brojeva odjednom
brojevi.sort()

maxokolina = -1
poz = 0

for i in range(n):
    okolina = bisect.bisect_right(brojevi, brojevi[i] + d) - bisect.bisect_left(brojevi, brojevi[i] - d)
    print(bisect.bisect_right(brojevi, brojevi[i] + d) - bisect.bisect_left(brojevi, brojevi[i] - d))
    print('******************')
    print(okolina)
    if okolina > maxokolina:
        maxokolina = okolina
        poz = i

print(brojevi[poz], maxokolina)
