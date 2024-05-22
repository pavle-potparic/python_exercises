redovi, kolone = list(map(int, input().split(" ")))
lista = []
for x in range(0, redovi):
    niz = list(map(int, input().split(" ")))
    resenje = 'da'
    for y in range(0, len(niz)):
        if y % 2 == 0 and niz[y] % 2 == 0:
            pass
        elif y % 2 != 0 and niz[y] % 2 != 0:
            pass
        else:
            resenje = 'ne'

    lista.append(resenje)

print(*lista, sep="\n")

# redovi, brojevi = list(map(int, input().split(' ')))
#
# resenja = []
#
# for x in range(0, redovi):
#     kolone = list(map(int, input().split(' ')))
#     resenje = 'da'
#     for y in range(0, brojevi):
#         if y % 2 == 0:
#             if kolone[y] % 2 != 0:
#                 resenje = 'ne'
#
#                 break
#
#         else:
#             if kolone[y] % 2 == 0:
#                 resenje = 'ne'
#                 break
#
#     resenja.append(resenje)
#
# for z in resenja:
#     print(z)