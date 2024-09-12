def main():
    s = input()
    n = len(s)
    ans = 0

    # Counting changes in adjacent characters
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            ans += 1

    v = [ans] * (n + 1)

    # Processing the string based on specific conditions
    for i in range(1, n - 1):
        if s[i - 1] == s[i + 1]:
            pos = i + 1
            for j in range(1, int(pos**0.5) + 1):
                if pos % j == 0:
                    if s[i] != s[i - 1]:
                        v[j] -= 2
                    else:
                        v[j] += 2

                    if j * j != pos:
                        if s[i] != s[i - 1]:
                            v[pos // j] -= 2
                        else:
                            v[pos // j] += 2

    # Final adjustments
    pos = n
    for j in range(1, int(pos**0.5) + 1):
        if pos % j == 0:
            if s[n - 1] != s[n - 2]:
                v[j] -= 1
            else:
                v[j] += 1

            if j * j != pos:
                if s[n - 1] != s[n - 2]:
                    v[pos // j] -= 1
                else:
                    v[pos // j] += 1

    v[1] = ans
    k = 1
    for i in range(2, n + 1):
        if v[i] < ans:
            ans = v[i]
            k = i

    print(k, ans)

if __name__ == "__main__":
    main()