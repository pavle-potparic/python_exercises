broj = int(input())

resenje = ((((broj + 8) * 2) - 10) / 8)

if resenje > 0:
    if float(resenje) == int(resenje):
        print(int(resenje))

    else:
        print("greska")


else:
    print("greska")
