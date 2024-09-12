lista = [1, 5, 10, 8]
lista1 = []
lista2 = [0, 55, 3, 6, 7]
lista3 = [['Pavle', 'Potparic'], ['Veljko', ''], ['Zoja', 'Potparic'], ['Mama', '']]

print('****** any ******')
print(any(lista))
print(any(lista1))
print(any(lista2))

print('****** all ******')
print(all(lista))
print(all(lista1))
print(all(lista2))

print('*************')

indeksi = all(person[1] for person in lista3)

if indeksi:
    print('Imamo sve vase podatke')

if not indeksi:
    print('Niste uneli sve vase podatke')
