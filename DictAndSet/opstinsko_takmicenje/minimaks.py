prva_cifra = int(input())
druga_cifra = int(input())
treca_cifra = int(input())
cetvrta_cifra = int(input())

lista = [prva_cifra, druga_cifra, treca_cifra, cetvrta_cifra]
lista.sort()

nule = list(filter(lambda x: x == 0, lista))

if len(nule) == 3:
    print(0)

elif len(nule) > 0:
    for x in range(0, len(nule)):
        lista.remove(0)
    string = ''
    string2 = ''
    for x in range(0, len(lista)):
        if x == 0:
            string += str(lista[x])
            string += str(0) * len(nule)
        else:
            string += str(lista[x])
        string2 += str(lista[-(x+1)])

    string2 += str(0) * len(nule)

    print(int(string2) - int(string))

else:
    string = ''
    string2 = ''
    for x in range(0, 4):
        string += str(lista[x])
        string2 += str(lista[-(x+1)])

    print(int(string2) - int(string))