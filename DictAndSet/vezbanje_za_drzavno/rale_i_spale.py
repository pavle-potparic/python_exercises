broj_rupa = int(input())
koordinate_rupa = input().split(' ')
koordinate_rupa = list(map(int, koordinate_rupa))

broj_zeceva = int(input())
koordinate_zeceva = input().split(' ')
koordinate_zeceva = list(map(int, koordinate_zeceva))

razlika = 0

for x in range(0, broj_zeceva):
    temp_pozicija = []

    for y in range(0, broj_rupa):
        temp_pozicija.append(abs(koordinate_rupa[y] - koordinate_zeceva[x]))

    minimum = min(temp_pozicija)

    if minimum > razlika:
        razlika = minimum


print(razlika)