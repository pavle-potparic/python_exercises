n = int(input())

resenje = ((n*n)-n)//n

if isinstance(n/resenje, int):
    while isinstance(n/resenje, int):
        if n % 2 == 0 and resenje % 2 == 0:
            n = n // 2
            resenje = resenje // 2

        if n % 3 == 0 and resenje % 3 == 0:
            n = n // 3
            resenje = resenje // 3

        if n % 5 == 0 and resenje % 5 == 0:
            n = n // 5
            resenje = resenje // 5

        if n % 7 == 0 and resenje % 7 == 0:
            n = n // 7
            resenje = resenje // 7

print(str(n) + "/" + str(resenje))