from bisect import bisect_left

n = int(input())
x = list(map(int, input().split()))

xs = sorted(list(set(x)))

for i in x:
    print(bisect_left(xs, i), end=' ')