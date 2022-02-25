NUM = [1, 2, 3]
LIMIT = 10001

dp = [0] * LIMIT
dp[0] = 1

for k in range(1, 4):
    for i in range(k, LIMIT):
        dp[i] += dp[i - k]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])

"""
N = 3   -> 찾는 숫자

1,2,3 -> 조합할 숫자

dp[N] = N을 조합할 수 있는 경우의 수
dp[n] = dp[n-3] + dp[n-2] + dp[n-1]
"""
