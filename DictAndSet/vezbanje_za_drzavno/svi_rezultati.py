def f(x, y):
    global br
    if br >= 1000:
        return
    rez[x + y] = f'{x}:{y}'
    if x + y == n:
        br += 1
        print(*rez)
        return
    if y < b:
        f(x, y + 1)
    if x < a:
        f(x + 1, y)


a, b = input().split()
a, b = int(a), int(b)
n = a + b
br = 0
rez = [''] * (n + 1)
f(0, 0)
print(br)
