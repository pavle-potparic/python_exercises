broj_kuca = int(input())
koordinate_kuca = list(map(int, input().split(" ")))
koordinate_kuca.sort()
broj_predajnika = int(input())
koordinate_predajnika = list(map(int, input().split(" ")))
koordinate_predajnika.sort()


def pronadji_najblizi(broj, lista):
    return abs(broj - min(lista, key=lambda x: abs(x - broj)))


najblizi_brojevi = list(map(lambda x: pronadji_najblizi(x, koordinate_predajnika), koordinate_kuca))

print(max(najblizi_brojevi))
