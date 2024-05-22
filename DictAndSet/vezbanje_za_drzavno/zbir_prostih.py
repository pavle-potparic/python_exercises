def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes(limit):
    primes = []
    number = 2
    while len(primes) < limit:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes


def process_queries(queries, max_b):
    prime_list = generate_primes(max_b)
    results = []
    for a, b in queries:
        sum_primes = sum(prime_list[a - 1:b])
        results.append(sum_primes)
    return results


broj = int(input())
resenje = []
max_b = 0
index = 1
data = []
for _ in range(broj-1):
    if _ < broj//2:
        jedan, dva = list(map(int, input().split(' ')))
        data.append(jedan)
        data.append(dva)
        jedan, dva = list(map(int, input().split(' ')))
        data.append(jedan)
        data.append(dva)
    a, b = int(data[index]), int(data[index + 1])
    resenje.append((a, b))
    max_b = max(max_b, b)
    index += 2

results = process_queries(resenje, max_b)

for result in results:
    print(result)
