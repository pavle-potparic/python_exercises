import math


def pronadji_delioce(n):
    rezultat = []
    d = 1
    while d * d < n:
        if n % d == 0:
            rezultat.append(d)
            rezultat.append(n // d)
        d += 1
    if d * d == n:
        rezultat.append(d)
    return sorted(rezultat)


def proveri_period(p, s):
    for i in range(p, len(s)):
        if s[i] != s[i - p]:
            return False
    return True


def period(s):
    delioci = pronadji_delioce(len(s))
    jePeriod = dict()

    for d in delioci:
        jePeriod[d] = False

    jePeriod[len(s)] = True

    rezultat = len(s)

    for i in range(len(delioci) - 2, -1, -1):
        p = delioci[i]

        for j in range(i + 1, len(delioci)):
            if delioci[j] % p == 0:
                pp = delioci[j]
                break

        if not jePeriod[pp]:
            jePeriod[p] = False
        else:
            jePeriod[p] = proveri_period(p, s[0:pp])
            if jePeriod[p]:
                rezultat = p

    return rezultat


def nzd(a, b):
    if b == 0:
        return a
    return nzd(b, a % b)


def nzs(a, b):
    return (a // nzd(a, b)) * b


n = 1
for rec in input().split():
    n = nzs(n, period(rec))
print(n)
