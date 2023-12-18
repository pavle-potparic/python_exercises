kolone = input()

lista = ["A", "B",  "C", "D", "E", "F",  "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

resenje = 1

for x in range(0, len(kolone)):
    if x != 0 or kolone[x] != "A":
        resenje *= 26 * x + (lista.index(kolone[x]) + 1)

print(resenje)

#ovaj kod saljem cisto da vidim koliko bih bodova dobio