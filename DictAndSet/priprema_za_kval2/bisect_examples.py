import bisect

# lista = [1, 3, 11, 11, 16, 17]
# left = bisect.bisect_left(lista, 12)
# right = bisect.bisect_right(lista, 12)
#
# print(left)
# print(right)


lista = [30, 35, 35, 35, 35, 40]

ind = lista.index(35)
broj = 36
left = bisect.bisect_left(lista, broj, 0, ind+1)

lista.insert(left, broj)

print(lista)