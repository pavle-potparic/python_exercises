def eratostenovo_sito(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:

            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    lista = []

    for p in range(2, num + 1):
        if prime[p]:
            lista.append(p)

    return lista


broj = int(input())

resenje = eratostenovo_sito(broj)

print(resenje[-1])

