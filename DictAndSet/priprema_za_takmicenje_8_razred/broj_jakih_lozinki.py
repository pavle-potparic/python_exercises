broj = int(input())

full_string = 'QWERTYUIOPASDFGHJKLZXCVBNM'
mali_string = full_string.lower()
full_string += mali_string

lista = list(range(0, 10))
lista = list(map(str, lista))

resenje = 0

for x in range(0, broj):
    lozinka = input()

    if len(lozinka) >= 8:
        if lozinka != lozinka.lower():
            if lozinka != lozinka.upper():
                ima_li_broj = 0
                string = 0
                specijalni_karakter = 0

                for y in lozinka:
                    if y in lista:
                        ima_li_broj = 1

                    elif y in full_string:
                        string = 1

                    else:
                        specijalni_karakter = 1

                if ima_li_broj == 1:
                    if specijalni_karakter == 1:
                        if string == 1:
                            resenje += 1

print(resenje)