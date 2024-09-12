broj = int(input())

lista = list(range(1, broj + 1))
resenje = list(lista)
kraj = []

counter = 0

while True:
    kolona = input()
    if kolona == '':
        break
    delovi = list(map(int, kolona.split(' ')))

    if counter == 0:
        print(*lista)
        counter = 1

    prvi = resenje[delovi[0]:delovi[0] + delovi[1]]
    prvi = prvi[::-1]

    drugi = resenje[delovi[2]:delovi[2] + delovi[1]]
    dva = drugi[::-1]

    resenje[delovi[0]:delovi[0] + delovi[1]] = dva
    resenje[delovi[2]:delovi[2] + delovi[1]] = prvi

    print(*resenje)
