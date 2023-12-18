broj_kuca = int(input())
koordinate_kuca = list(map(int, input().split(" ")))
koordinate_kuca.sort()
broj_predajnika = int(input())
koordinate_predajnika = list(map(int, input().split(" ")))
koordinate_predajnika.sort()

min_snaga = 0

for x in koordinate_kuca:

    najmanja_udaljenost = float('inf')
    for predajnik_lokacija in koordinate_predajnika:
        udaljenost = abs(x - predajnik_lokacija)
        if udaljenost < najmanja_udaljenost:
            najmanja_udaljenost = udaljenost
        else:

            break
    if najmanja_udaljenost > min_snaga:
        min_snaga = najmanja_udaljenost


print(min_snaga)