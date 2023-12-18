prva_stranica = input()
druga_stranica = input()
treca_stranica = input()

cetvorougao = [prva_stranica, druga_stranica, treca_stranica]

a = prva_stranica[0]
b = prva_stranica[1]
c = 0
d = 0

for x in range(0, len(cetvorougao)):
    for y in cetvorougao[x]:
        if c == 0:
            if y != a:
                if y != b:
                    c = y

        else:
            if d == 0:
                if y != a:
                    if y != b:
                        if y != c:
                            d = y

    if d != 0:
        break

if d + a not in cetvorougao:
    if b + c not in cetvorougao:
        temp = c
        c = d
        d = temp

sve_stranice = [a + b, b + c, c + d, d + a]

for z in sve_stranice:
    if z not in cetvorougao:
        print(z)
        break
