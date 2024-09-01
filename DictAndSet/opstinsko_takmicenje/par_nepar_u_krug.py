n = int(input())
niz1 = list(range(1, 2 * n + 1))
neparni_brojevi = list(filter(lambda x: x % 2 != 0, niz1))
parni_brojevi = list(filter(lambda y: y % 2 == 0, niz1))

niz = neparni_brojevi + parni_brojevi

print(*niz)


def pomeri_unazad(niz):
    return niz[1:] + [niz[0]]


parni = list(parni_brojevi)
neparni = list(neparni_brojevi)

for q in range(1, n * n):
    parni = pomeri_unazad(parni)
    if q % n == 0:
        neparni = pomeri_unazad(neparni)
    print(*neparni + parni)
