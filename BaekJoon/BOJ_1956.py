import sys

input = sys.stdin.readline

V, E = map(int, input().split())
INF = 100000000

s = [[INF] * V for _ in range(V)]

for i in range(E):
    a, b, c = map(int, input().split())
    s[a - 1][b - 1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            if s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

result = INF
for i in range(v):
    result = min(result, s[i][i])

if result == INF:
    print(-1)
else:
    print(result)
