import bisect

lista = list(map(int, input().split(' ')))
lista.sort()
prva = lista[0]
druga = lista[1]
treca = lista[2]
cetrvrta = lista[3]

mrav_a, mrav_b = list(map(int, input().split(' ')))
mravi = [mrav_b, mrav_a]
mravi.sort()

mrav_a = int(mravi[0])
mrav_b = int(mravi[1])

slab_mrav = 0

rezultati = []
temp = list(lista)
kraj = 0

for x in range(0, 4):
    if kraj == 1:
        break
    if lista[x] <= mrav_a:
        torba = mrav_a - lista[x]
        temp.remove(lista[x])
        maximum = sum(lista) - lista[x]
        for y in range(0, 4):
            if y == x:
                pass

            else:
                if torba >= lista[y]:
                    maximum -= lista[y]
                    temp.remove(lista[y])
                    if mrav_b >= temp[0] + temp[1]:
                        maximum = 0
                        rezultati.append(maximum)
                        kraj = 1
                        break
                    else:
                        if mrav_b >= temp[1]:
                            maximum -= temp[1]
                            rezultati.append(maximum)
                        else:
                            if mrav_b >= temp[0]:
                                maximum -= temp[0]
                                rezultati.append(maximum)
                    temp.append(lista[y])
                    temp.sort()
                else:
                    if mrav_b >= temp[2] + temp[1]:
                        maximum = temp[0]
                        rezultati.append(maximum)

                    elif temp[1] + temp[0] <= temp[2] + temp[0] <= mrav_b:
                        maximum = temp[1]
                        rezultati.append(maximum)

                    elif temp[2] < temp[1] + temp[0] <= mrav_b:
                        maximum = temp[2]
                        rezultati.append(maximum)

                    else:
                        broj = bisect.bisect_right(temp, mrav_b)
                        vrednost = int(temp[broj-1])
                        temp.remove(temp[broj-1])
                        maximum = sum(temp)
                        rezultati.append(maximum)
                        temp.append(vrednost)

    else:
        if x == 0:
            slab_mrav = 1

            temp = list(lista)

            temp_lista = list(lista)

            for z in lista:
                temp_lista.remove(z)
                resenje = list(map(lambda q: q + z, temp_lista))
                temp_lista.append(z)

                index = bisect.bisect_right(resenje, mrav_b)
                if index > 0:
                    rezultati.append(sum(lista) - resenje[index - 1])

            min_max = 1
            break

    temp = list(lista)

if min(rezultati) < 0:
    print(0)
else:
    print(min(rezultati))

