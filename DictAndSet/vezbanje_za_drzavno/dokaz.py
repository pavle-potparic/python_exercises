import bisect

n = int(input())
sabirci = [1]
while not n in sabirci:

    p_sabirak = max(sabirci)
    i = len(sabirci) - 1

    while p_sabirak + sabirci[i] > n:
        i -= 1

    d_sabirak = sabirci[i]
    zbir = p_sabirak + d_sabirak
    pozicija = bisect.bisect_left(sabirci, zbir)
    sabirci.insert(pozicija, zbir)
    print(zbir, "=", p_sabirak, "+", d_sabirak, sep="")
