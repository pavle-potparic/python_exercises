k = int(input())

mecevi = ""

for x in range(0, pow(2, k)-1):
    mecevi += input() + "/"


lista_igraca = list(range(0, pow(2, k)))

lista_odigranih_meceva = []

for y in lista_igraca:
    lista_odigranih_meceva.append(mecevi.count(str(y)))

finale1 = list(mecevi.split("/"))

max1 = max(lista_odigranih_meceva)
lista_odigranih_meceva[lista_odigranih_meceva.index(max1)] = 0
max2 = max(lista_odigranih_meceva)

igrac1 = lista_igraca.index(lista_odigranih_meceva.index(0))
igrac2 = lista_igraca.index(lista_odigranih_meceva.index(max2))
lista_odigranih_meceva[lista_odigranih_meceva.index(max2)] = 0

if str(igrac1) + " " + str(igrac2) in finale1:
    pobednik = igrac1
    drugi = igrac2

else:
    pobednik = igrac2
    drugi = igrac1

print(pobednik)
print(drugi)

temp_lista = []
temp_max = max(lista_odigranih_meceva)

for z in range(0, pow(2, k)-2):
    if temp_max in lista_odigranih_meceva:
        temp_lista.append(lista_igraca[lista_odigranih_meceva.index(temp_max)])
        lista_odigranih_meceva[lista_odigranih_meceva.index(temp_max)] = 0
    else:
        print(*temp_lista)
        temp_lista = []
        temp_max = max(lista_odigranih_meceva)
        temp_lista.append(lista_igraca[lista_odigranih_meceva.index(temp_max)])
        lista_odigranih_meceva[lista_odigranih_meceva.index(temp_max)] = 0

print(*temp_lista)