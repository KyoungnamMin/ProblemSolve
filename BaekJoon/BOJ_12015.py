from bisect import bisect_left

n = int(input())
array = list(map(int, input().split()))

result = []
for x in array:
    k = bisect_left(result, x)
    if len(result) <= k:
        result.append(x)
    else:
        result[k] = x

print(len(result))