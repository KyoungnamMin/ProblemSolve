import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

dp = [[0] * N for i in range(N)]
for i in range(1, N):
    for j in range(N - i):
        x = j + i
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + array[j][0] * array[k][1] * array[x][1])

print(dp[0][N - 1])