broj = list(input().rstrip())

drugi_broj = list(input().rstrip())

iste_cifre = list(filter(lambda x: x in broj, drugi_broj))

resenje = 'da'

if len(iste_cifre) == 0:
    resenje = 'ne'

elif len(iste_cifre) > 1:
    resenje = 'ne'

elif drugi_broj.index(iste_cifre[0]) == broj.index(iste_cifre[0]):
    resenje = 'ne'

print(resenje)