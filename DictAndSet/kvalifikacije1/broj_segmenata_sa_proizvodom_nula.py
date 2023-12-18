broj = int(input())

niz = input()

niz = niz.replace(" ", "")

nule = niz.count("0")

resenje = 0
resenje += nule

pozicija = 0

if nule == 1:
    levo = niz.find("0")+1
    desno = broj-levo
    resenje += levo-1
    resenje += levo * desno

elif nule == 0:
    pass

else:
    for x in range(0, nule):
        pozicija = niz.find("0", pozicija, broj)+1
        resenje += pozicija-1

print(resenje)