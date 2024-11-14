broj = int(input())

lista = []

for x in range(0, broj):
    prvi, drugi = map(int, input().split(' '))
    temp_lista = []

    if x == 0:
        lista1 = list(range(prvi, drugi + 1))

    else:
        temp_lista = list(range(prvi, drugi+1))
        if x == 1:
            lista = list(set(lista1).intersection(temp_lista))

        else:
            lista = list(set(lista).intersection(temp_lista))

print(len(lista))