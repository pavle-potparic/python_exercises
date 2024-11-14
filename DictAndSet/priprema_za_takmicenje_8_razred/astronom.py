broj = int(input())

lista = list(map(int, input().split(' ')))
resenje = 0

for x in range(-1, broj):
    temp = 0
    for y in range(x+1, broj):
        temp += lista[y]

        if temp == 0:
            resenje += 1
            break

print(resenje)

