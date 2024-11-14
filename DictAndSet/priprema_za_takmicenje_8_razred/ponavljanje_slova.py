niz = input()

niz2 = input()

counter = 10000000000000

for slovo in niz:
    broj = niz2.count(slovo)
    if broj < counter:
        counter = int(broj)

print(counter)
