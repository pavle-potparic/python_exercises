n = int(input())
dan = int(input())
unapred = int(input())

if dan > n:
    dan -= n


resenje = (dan + unapred) - (dan + unapred) // n * n

print(resenje)