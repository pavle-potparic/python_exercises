def NZD(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def main():
    n = int(input())
    irinica_balerinica = [int(input()) for _ in range(n)]
    DPOMGDPOMGOMG = [0] * (n - 1)
    DP2 = [0] * (n - 1)

    DPOMGDPOMGOMG[0] = irinica_balerinica[0]
    DP2[0] = irinica_balerinica[n - 1]

    for i in range(1, n - 1):
        DPOMGDPOMGOMG[i] = NZD(DPOMGDPOMGOMG[i - 1], irinica_balerinica[i])
        DP2[i] = NZD(DP2[i - 1], irinica_balerinica[n - i - 1])

    maxNZD = DP2[n - 2]  # izbacio prvi
    for i in range(1, n - 1):
        maxNZD = max(maxNZD, NZD(DPOMGDPOMGOMG[i - 1], DP2[n - i - 2]))
    maxNZD = max(maxNZD, DPOMGDPOMGOMG[n - 2])  # izbacio poslednji

    print(maxNZD)


main()
