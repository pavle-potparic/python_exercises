broj = int(input())

dictionary = {}

for x in range(0, broj):
    pocetak, kraj = list(input().split(' '))
    dictionary[pocetak] = kraj

kuca = 'Kraljevo'
print(kuca)
for y in range(0, broj):
    print(dictionary[kuca])
    kuca = dictionary[kuca]