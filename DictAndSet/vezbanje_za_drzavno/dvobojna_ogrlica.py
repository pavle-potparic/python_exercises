niz = list(input())
numeracija = list(range(0, len(niz)))

resenje = []

if len(niz) % 2 == 0:
    sredina = ((len(niz) - 1) // 2) + 1
    desno = niz[1: sredina]
    levo = niz[sredina + 1: len(niz)]

    if levo.count('P') > desno.count('P'):
        resenje.append('L')

    elif levo.count('P') < desno.count('P'):
        resenje.append('D')

    else:
        resenje.append('N')

    for x in range(0, len(niz) - 1):
        numeracija.insert(len(niz) - 1, numeracija.pop(0))
        niz.insert(len(niz) - 1, niz.pop(0))
        sredina = ((len(niz) - 1) // 2) + 1
        desno = niz[1: sredina]
        levo = niz[sredina + 1: len(niz)]

        if levo.count('P') > desno.count('P'):
            resenje.append('L')

        elif levo.count('P') < desno.count('P'):
            resenje.append('D')

        else:
            resenje.append('N')

else:
    desno = niz[1: len(niz) // 2 + 1]
    levo = niz[len(niz) // 2 + 1: len(niz)]


    if levo.count('P') > desno.count('P'):
        resenje.append('L')

    elif levo.count('P') < desno.count('P'):
        resenje.append('D')

    else:
        resenje.append('N')

    for x in range(0, len(niz) - 1):
        numeracija.insert(len(niz) - 1, numeracija.pop(0))
        niz.insert(len(niz) - 1, niz.pop(0))
        levo = niz[len(niz) // 2 + 1: len(niz)]
        desno = niz[1: len(niz) // 2 + 1]

        if levo.count('P') > desno.count('P'):
            resenje.append('L')

        elif levo.count('P') < desno.count('P'):
            resenje.append('D')

        else:
            resenje.append('N')

print(*resenje, sep='')
