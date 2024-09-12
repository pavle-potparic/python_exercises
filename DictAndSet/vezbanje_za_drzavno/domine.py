M = 1000000007
n = int(input())
h = [int(x) for x in input().split()]

dp = [0] * n
dp[n - 1] = 1
for i in range(n - 2, -1, -1):
    for j in range(i + 1, min(n, i + h[i] + 1)):
        dp[i] = (dp[i] + dp[j]) % M
print(dp[0])
