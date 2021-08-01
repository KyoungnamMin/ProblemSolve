from collections import Counter


T = int(input())
for i in range(T):
    N = int(input())
    s = []

    for j in range(N):
        a, b = input().split()
        s.append(b)

    num = 1
    result = Counter(s)
    for key in result:
        num *= result[key] + 1

    print(num - 1)
