vrednost = int(input())
vrednost_pileta = int(input())
vrednost_paceta = int(input())
vrednost_curica = int(input())
broj_nacina = 0

for broj_pilica in range(0, vrednost // vrednost_pileta + 1):
    for broj_pacica in range(0, vrednost // vrednost_paceta + 1):
        for broj_curica in range(0, vrednost // vrednost_curica + 1):

            if broj_pilica * vrednost_pileta + broj_pacica * vrednost_paceta + broj_curica * vrednost_curica == vrednost:
                broj_nacina += 1

print(broj_nacina)
