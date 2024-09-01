lista = list(range(0, 31))

for broj in range(1, 31):
    resenje = ['fizz buzz' if broj % 15 == 0 else 'fizz' if broj % 3 == 0 else 'buzz' if broj % 5 == 0 else broj]

    print(*resenje)
