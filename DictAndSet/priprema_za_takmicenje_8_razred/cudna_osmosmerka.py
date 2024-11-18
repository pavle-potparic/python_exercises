red, red1 = list(map(int, input().split(' ')))

lista = []

for x in range(0, red):
    lista.append(input())

reci = []

for y in range(0, red1):
    reci.append(input())

resenje = 0

for z in reci:
    for q in range(0, red):
        if z in lista[q] or z in lista[q][::-1]:
            resenje += 1
            break

        temp = ''.join(list(map(lambda k: lista[k][q], list(range(0, red)))))
        temp1 = ''.join(list(list(temp)[::-1]))
        if z in temp or z in temp1:
            resenje += 1
            break

        else:
            mala_dijagonala = ''
            trenutni_red = 0
            for i in range(q, red):
                mala_dijagonala += lista[trenutni_red][i]
                trenutni_red += 1

            if z in mala_dijagonala or z in ''.join(list(mala_dijagonala)[::-1]):
                resenje += 1
                break

            velika_dijagonala = ''
            trenutni_red = 0

            for j in range(q, -1, -1):
                velika_dijagonala += lista[trenutni_red][j]
                trenutni_red += 1

            if z in velika_dijagonala or z in ''.join(list(velika_dijagonala)[::-1]):
                resenje += 1
                break

    print(z)
    print(resenje)