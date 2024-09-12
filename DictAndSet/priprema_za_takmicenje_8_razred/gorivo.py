pera = int(input())
zika = int(input())
mika = int(input())
gorivo = int(input())

temp = gorivo
gorivo -= pera

if gorivo < 1:
    print("pera")
    gorivo = temp

gorivo -= zika

if gorivo < 1:
    print("zika")
    gorivo = temp


