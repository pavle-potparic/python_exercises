resenje = 0

for x in range(0, 5):
    broj = int(input())
    if broj > 500:
        temp = broj // 500
        resenje += broj - temp * 500

    else:
        resenje += broj

print(resenje // 500)