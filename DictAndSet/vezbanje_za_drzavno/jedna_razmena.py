broj = input()

maksimum = int(max(broj))

count = broj.count(str(maksimum))

if count > 1 or str(maksimum) != broj[0]:
    temp_broj = list(broj[::-1])
    index = temp_broj.index(str(maksimum))
    prvi = temp_broj[-1]
    temp_broj[-1] = maksimum
    temp_broj[index] = prvi
    print(*temp_broj[::-1], sep='')

else:
    temp_broj = list(broj)
    temp_broj.remove(str(maksimum))
    maksimum2 = int(max(temp_broj))
    temp_broj = temp_broj[::-1]
    index = temp_broj.index(str(maksimum2))
    temp_broj.insert(len(temp_broj), maksimum)

    for x in range(len(broj)-1, -1, -1):
        if maksimum2 > int(temp_broj[x]) and index < x:
            drugi = broj[x]
            temp_broj[x] = maksimum2
            temp_broj[index] = drugi
            break

    print(*temp_broj[::-1], sep='')