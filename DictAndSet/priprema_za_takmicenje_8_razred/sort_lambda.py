lista = [[4, 5, 1000], [1, 3, 16], [44, 76, 12], [5, 89, 100]]

lista.sort(key=lambda x: x[1] if x[1] > 10 else x[2], reverse=True)

print(lista)

broj = lambda x: x / 3

print(broj(6))