k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

while (start <= end):
    mid = (start + end) // 2
    num = 0
    for i in lan:
        num += i // mid
    if num < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)