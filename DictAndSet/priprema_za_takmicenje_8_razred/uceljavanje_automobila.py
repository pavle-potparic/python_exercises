broj = int(input().rstrip())

lista1 = []

for x in range(0, broj):
    lista1.append(input().rstrip())
    lista1.append('0')


broj2 = int(input())


if broj2 >= broj:
    for y in range(1, 2*broj, 2):
        lista1[y] = input().rstrip()

    for z in range(0, broj2 - broj):
        lista1.append(input().rstrip())

else:
    for y in range(1, 2*broj2, 2):
        lista1[y] = input().rstrip()

    for x in range(0, broj - broj2):
        lista1.remove('0')

print(*lista1, sep='\n')