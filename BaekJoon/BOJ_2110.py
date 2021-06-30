n, c = map(int, input().split())
net = []
for _ in range(n):
    net.append(int(input()))
net.sort()

start = 1
end = net[-1] - net[0]

result = 0
while (start <= end):
    mid = (start + end) // 2
    current = net[0]
    count = 1
    
    for i in range(1, len(net)):
        if net[i] >= current + mid:
            count += 1
            current = net[i]
    if count < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)