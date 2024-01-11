red, kolona = map(int, input().split())
lista = [list(input()) for brojac in range(red)]

start, cilj = (0, 0), (0, 0)
for i in range(red):
    for j in range(kolona):
        if lista[i][j] == 'C':
            cilj = (i, j)
        elif lista[i][j] == 'S':
            start = (i, j)

minimum_start, minimum_cilj = float('inf'), float('inf')

for i in range(red):
    for j in range(kolona):
        if lista[i][j] == 'T':
            minimum_start = min(minimum_start, abs(i - cilj[0]) + abs(j - cilj[1]))
            minimum_cilj = min(minimum_cilj, abs(i - start[0]) + abs(j - start[1]))

resenje = min(minimum_start + minimum_cilj, abs(cilj[0] - start[0]) + abs(cilj[1] - start[1]))
print(resenje)
