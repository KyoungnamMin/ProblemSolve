N = int(input())
fear = list(map(int, input().split()))

fear.sort()

result = 0
current = 0

for f in fear:
    current += 1
    if current >= f:
        result += 1
        current = 0

print(result)
