broj = int(input())
lista = []
for x in range(0, broj):
    lista.append(int(input()))

resenje = lista[::-1]
print(*resenje, sep='\n')