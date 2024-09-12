redovi, kolone = list(map(int, input().rstrip().split(' ')))
sekunde = int(input().rstrip())

lopte = []
slika = []

while True:
    lopta = input()

    if lopta == '':
        break

    else:
        lopte.append(list(map(int, lopta.rstrip().split(' '))))

for x in range(redovi):
    slika.append(['.'] * kolone)

for osobine_lopte in lopte:
    if 0 <= osobine_lopte[0] + (osobine_lopte[2] * sekunde) < kolone and 0 <= osobine_lopte[1] + (osobine_lopte[3] * sekunde) < redovi:
        slika[osobine_lopte[0] + (osobine_lopte[2] * sekunde)][osobine_lopte[1] + (osobine_lopte[3] * sekunde)] = '#'


for z in slika:
    print(*z, sep='')

