import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    page = list(map(int, input().split()))

    dp = [[0] * K for _ in range(K)]

    for i in range(K - 1):
        dp[i][i + 1] = page[i] + page[i + 1]
        for j in range(i + 2, K):
            dp[i][j] = dp[i][j - 1] + page[j]
    for d in range(2, K):
        for i in range(K - d):
            j = i + d
            minimum = [dp[i][k] + dp[k + 1][j] for k in range(i, j)]
            dp[i][j] += min(minimum)

    print(dp[0][K - 1])
