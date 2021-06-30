import sys
from collections import deque

def bfs():
    global isalreadyRipe
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
                isalreadyRipe = False
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append((nx, ny, nz))

m, n, h = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
tomato = [[] for i in range(h)]
queue = deque()
for i in range(h):
    for j in range(n):
        tomato[i].append(list(map(int, sys.stdin.readline().split())))
for height in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[height][i][j] == 1:
                queue.append([i, j, height])

if len(queue) == 0:
    print(-1)
    sys.exit(0)

result = -1
isalreadyRipe = True

bfs()

if isalreadyRipe:
    print(0)
    sys.exit(0)

for height in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[height][i][j] == 0:
                print(-1)
                sys.exit(0)
            result = max(result, tomato[height][i][j])

print(result-1)