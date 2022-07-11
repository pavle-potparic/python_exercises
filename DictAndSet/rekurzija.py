def rekurzija(broj: int):
    if(broj < 5):
        broj = rekurzija(broj + 1)

    return broj


def korisnikov_odgovor():
    odgovor = input("Unesite broj veci od 4")
    if(int(odgovor)<5):
        print("niste uneli odgovarajuci broj")
        korisnikov_odgovor()

    print(f"Bravo, uneli ste broj {odgovor}")



# korisnikov_odgovor()

keys = [""] * 10
print(keys[9])