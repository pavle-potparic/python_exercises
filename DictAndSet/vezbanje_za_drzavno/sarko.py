prvo_jagnje = int(input())
drugo_jagnje = int(input())
trece_jagnje = int(input())

lista = [prvo_jagnje, drugo_jagnje, trece_jagnje]
lista.sort()

najmanje = 0
najvise = 0

if lista[2] - lista[1] > 1:
    najmanje += 1
    najvise += lista[2] - lista[1]
    najvise -= 1

if lista[1] - lista[0] > 1:
    najmanje += 1
    najvise += lista[1] - lista[0]
    najvise -= 1

print(najmanje)
print(najvise)