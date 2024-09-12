a, b = list(map(int, input().split(' ')))

resenje = 0

for x in range(a, b+1):
    z = list(str(x))
    if x < 0:
        z.remove(z[0])

    cifre = list(map(int, z))

    if x != 0 and x % sum(cifre) == 0:
        resenje += 1

print(resenje)