n = int(input())
k = int(input())

start = 1
end = k
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(1, n+1):
        total += min(mid//i, n)
    
    if total >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)