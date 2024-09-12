broj = int(input())

lista = []

for x in range(0, broj):
    sati = list(input().split(':'))
    if sati[0][0] == '0':
        zamena = int(sati[0][1]) - 9
        if zamena < 0:
            sati[0] = str(zamena+24)

        else:
            sati[0] = '00'

    else:
        zamena = int(sati[0]) - 9

        if zamena < 10:
            sati[0] = '0' + str(zamena)

        else:
            sati[0] = str(zamena)

    lista.append(str(sati[0]) + ':' + sati[1] + ':' + sati[2])

print(*lista, sep='\n')