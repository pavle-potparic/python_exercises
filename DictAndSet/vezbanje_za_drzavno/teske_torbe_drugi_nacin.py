def Xabs(n):
    if n < 0:
        return 0
    return n

def main():
    torbe = []
    for i in range(4):
        br = int(input())
        torbe.append(br)

    p1 = int(input())
    p2 = int(input())

    m = 0
    mlevo1 = -1
    mdesno1 = -1
    levo = 0
    desno = 1

    while levo < 3:
        while desno < 4:
            if torbe[levo] + torbe[desno] > m and torbe[levo] + torbe[desno] <= p1:
                m = torbe[levo] + torbe[desno]
                mlevo1 = levo
                mdesno1 = desno
            desno += 1
        levo += 1
        desno = levo + 1

    if mlevo1 == -1:
        for i in range(4):
            if torbe[i] > m and torbe[i] <= p1:
                m = torbe[i]
                mlevo1 = i
                mdesno1 = i

    levo = 0
    desno = 1
    m = 0
    mlevo2 = -1
    mdesno2 = -1

    while levo < 3:
        while desno < 4:
            if torbe[levo] + torbe[desno] > m and torbe[levo] + torbe[desno] <= p2:
                m = torbe[levo] + torbe[desno]
                mlevo2 = levo
                mdesno2 = desno
            desno += 1
        levo += 1
        desno = levo + 1

    if mlevo2 == -1:
        for i in range(4):
            if torbe[i] > m and torbe[i] <= p2:
                m = torbe[i]
                mlevo2 = i
                mdesno2 = i

    z = 0
    for i in range(4):
        if i != mlevo1 and i != mdesno1 and i != mlevo2 and i != mdesno2:
            z += torbe[i]

    print(z)

if __name__ == "__main__":
    main()