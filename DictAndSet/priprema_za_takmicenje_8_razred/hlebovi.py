broj = int(input())

covek = broj // 2
resenje = 0

for x in range(covek, -1, -1):
    for y in range(0, broj + 1):
        for z in range(0, broj + 1):
            suma = x * 2 + y + z / 2
            broj_ljudi = x + y + z

            if broj_ljudi == broj and suma == broj:
                resenje += 1
                break

            if broj_ljudi > broj:
                break

            if suma > broj:
                break

print(resenje)
