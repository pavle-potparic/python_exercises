broj = int(input())

lista = []

for x in range(0, broj):
    lista.append(int(input()))

index1 = int(lista.index(max(lista)))
lista.remove(max(lista))

index2 = int(lista.index(max(lista)))

if index1 <= index2:
    index2 += 1

print(index2)
print(max(lista))