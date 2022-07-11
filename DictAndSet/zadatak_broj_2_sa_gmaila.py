n = int(input("Koliko radnika obavlja posao? "))
s = int(input("Koliko vremena im je bilo potrebno da zavrse zadatak? "))
m = int(input("Koliko se radnika prikljucilo? "))


def podela_posla(trenutni_radnici, broj_sati, dodatni_radnici):
    svi_radnici = trenutni_radnici + dodatni_radnici
    prosecan_ucinak = broj_sati / svi_radnici
    return prosecan_ucinak


radni_dan = podela_posla(n, s, m)
print(radni_dan)
