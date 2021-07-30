import sys
from bisect import bisect_left


input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
dp = []

for num in A:
    idx = bisect_left(dp, num)
    if len(dp) <= idx:
        dp.append(num)
    else:
        dp[idx] = num

print(len(dp))
