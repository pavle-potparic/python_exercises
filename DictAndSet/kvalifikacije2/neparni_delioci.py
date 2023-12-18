broj = int(input())


def broj_delilaca(n):
    brojac = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            brojac += 1
            if i != n // i:
                brojac += 1
    return brojac


resenje = 0
delioci = 0

while resenje <= broj:
    delioci = broj_delilaca(resenje*broj)

    if delioci % 2 != 0:
        break

    resenje += 1

print(resenje)
