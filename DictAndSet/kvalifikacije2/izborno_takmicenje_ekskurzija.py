broj_mrava, broj_zelja = list(map(int, input().split(" ")))
zelje = []

for x in range(0, broj_zelja):
    a, b = list(map(int, input().split(" ")))
    zelje.append(a)
    zelje.append(b)

resenje = int(broj_mrava)

for x in range(0, broj_mrava):
    ponavljanje = list(filter(lambda z: z == x, zelje))
    if len(ponavljanje) > 1:
        resenje -= len(ponavljanje)

print(resenje)
