komadi = int(input())

armatura = list(map(int, input().split(" ")))

stubovi = int(input())

resenje = 0


def delovi(broj):
    global armatura, stubovi

    rezultat = list(map(lambda x: x // broj, armatura))

    if sum(rezultat) >= stubovi:
        return True

    else:
        return False


while delovi(resenje + 1000000):
    resenje += 1000000

while delovi(resenje + 100000):
    resenje += 100000

while delovi(resenje + 10000):
    resenje += 10000

while delovi(resenje + 1000):
    resenje += 1000

while delovi(resenje + 100):
    resenje += 100

while delovi(resenje + 10):
    resenje += 10

while delovi(resenje + 1):
    resenje += 1

print(resenje)

