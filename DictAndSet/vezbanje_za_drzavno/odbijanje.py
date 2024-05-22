visina, sirina, odbij = list(map(int, input().split(" ")))

resenje = (sirina - (sirina // odbij)*odbij) / odbij

if resenje > 0.5:
    if sirina//odbij % 2 == 0:
        print(1)
    else:
        print(-1)

elif resenje < 0.5:
    if sirina//odbij % 2 == 0:
        print(-1)
    else:
        print(1)

else:
    print(0)