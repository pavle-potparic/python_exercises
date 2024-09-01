import math
def factorial(broj, granica, ponavljanje):
    broj *= ponavljanje+1
    ponavljanje += 1
    if ponavljanje > granica:
        return
    print(broj)
    factorial(broj, granica, ponavljanje)

broj = 1
granica = 10
ponavljanje = 1

factorial(broj, granica, ponavljanje)
print(math.factorial(10))