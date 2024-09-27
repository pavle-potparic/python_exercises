def bfs(i, j):
    notvisited[i][j] = False
    if i + 1 < r:
        if notvisited[i + 1][j] and wl[i + 1][j]:
            n[i + 1][j] = n[i][j]
            bfs(i + 1, j)
    if i - 1 >= 0:
        if notvisited[i - 1][j] and wl[i - 1][j]:
            n[i - 1][j] = n[i][j]
            bfs(i - 1, j)
    if j + 1 < c:
        if notvisited[i][j + 1] and wl[i][j + 1]:
            n[i][j + 1] = n[i][j]
            bfs(i, j + 1)
    if j - 1 >= 0:
        if notvisited[i][j - 1] and wl[i][j - 1]:
            n[i][j - 1] = n[i][j]
            bfs(i, j - 1)


r, c = map(int, input().split())
wl = [[False] * c for _ in range(r)]
n = [[-1] * c for _ in range(r)]
notvisited = [[True] * c for _ in range(r)]
cnt = 0

for i in range(r):
    row = input().strip()
    for j in range(c):
        if row[j] == '.':
            wl[i][j] = True
            notvisited[i][j] = True
            n[i][j] = -1
        else:
            wl[i][j] = False
            n[i][j] = -1

for i in range(r):
    if wl[i][0]:
        n[i][0] = 0
    if wl[i][c - 1]:
        n[i][c - 1] = 0

for i in range(c):
    if wl[0][i]:
        n[0][i] = 0
    if wl[r - 1][i]:
        n[r - 1][i] = 0

for i in range(r):
    if wl[i][0] and notvisited[i][0]:
        bfs(i, 0)
    if wl[i][c - 1] and notvisited[i][c - 1]:
        bfs(i, c - 1)

for i in range(c):
    if wl[0][i] and notvisited[0][i]:
        bfs(0, i)
    if wl[r - 1][i] and notvisited[r - 1][i]:
        bfs(r - 1, i)

for i in range(r):
    for j in range(c):
        if wl[i][j]:
            if notvisited[i][j]:
                if n[i][j] == -1:
                    n[i][j] = cnt + 1
                    cnt += 1
                bfs(i, j)

cnts = [0] * cnt
for i in range(r):
    for j in range(c):
        if n[i][j] > 0:
            cnts[n[i][j] - 1] += 1

m = max(cnts, default=0)
print(m)
