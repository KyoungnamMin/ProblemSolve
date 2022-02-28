"""
1자리 수
    0~9 - 10개
2자리 수
    00 ~ 09 - 10개
    11 ~ 19 - 9개
        ...
    99 1개
3자리 수

"""
n = int(input())

dp = [1] * 10


for _ in range(n - 1):
    for i in range(1, 10):
        dp[i] = (dp[i] + dp[i - 1]) % 10007

print(sum(dp) % 10007)
