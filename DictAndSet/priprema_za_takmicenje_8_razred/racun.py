broj_redova, broj_korisnika = list(map(int, input().split(' ')))

korisnici = []

counter = 0

resenje = []

for x in range(0, broj_redova):
    ulaz = list(input().split(' '))

    if ulaz[0] == 'upit':
        if counter == 0:
            if len(korisnici) != broj_korisnika:
                for y in range(0, broj_korisnika - len(korisnici) // 2):
                    korisnici.append('odlogovan')
                    korisnici.append(0)
            counter = 1

        resenje.append(len(list(filter(lambda z: z == int(ulaz[1]) and korisnici.index(z) % 2 == 1, korisnici))))

    else:
        if counter == 1:
            indeks = korisnici.index(ulaz[0])
            korisnici[indeks + 1] += int(ulaz[1])

        else:
            korisnici.append(ulaz[0])
            korisnici.append(int(ulaz[1]))

print(*resenje, sep='\n')