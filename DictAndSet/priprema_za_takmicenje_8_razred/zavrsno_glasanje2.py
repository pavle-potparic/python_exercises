n = int(input())

zemlje = []
brojevi_poena = list(i for i in range(1, n))

for i in range(n):
    zemlje.append(int(input()))

zemlja = int(input()) - 1
glasac = int(input()) - 1

if glasac != zemlja:

    zemlje[zemlja] = zemlje[zemlja] + max(brojevi_poena)
    brojevi_poena.remove(max(brojevi_poena))

poeni = zemlje[zemlja]

for i in range(len(zemlje)):

    if i == glasac or i == zemlja:
        pass

    else:

        if zemlje[i] >= zemlje[zemlja]:

            zemlje[i] = zemlje[i] + max(brojevi_poena)
            brojevi_poena.remove(max(brojevi_poena))

        elif zemlje[i] + min(brojevi_poena) > zemlje[zemlja]:

            zemlje[i] = zemlje[i] + max(brojevi_poena)
            brojevi_poena.remove(max(brojevi_poena))

        else:

            zemlje[i] = zemlje[i] + min(brojevi_poena)
            brojevi_poena.remove(min(brojevi_poena))

zemlje.sort()
zemlje.reverse()

print(zemlje.index(poeni))
