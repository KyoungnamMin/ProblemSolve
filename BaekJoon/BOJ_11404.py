import sys

input = sys.stdin.readline

INF = 100000000

n = int(input().strip())
m = int(input().strip())

bus = [[INF] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if bus[a - 1][b - 1] > c:
        bus[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            # 자기 자신으로 오는 경우
            if j == i:
                bus[i][j] = 0

            # k를 거쳐서 가는 것, 원래 값 중 최소 값
            else:
                bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

for i in range(n):
    for j in range(n):
        if bus[i][j] == INF:
            print(0, end=" ")
        else:
            print(bus[i][j], end=" ")
    print()
