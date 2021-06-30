import sys
from collections import deque

def bfs():
    global isalreadyRipe
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                isalreadyRipe = False
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

m, n = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tomato = []
queue = deque()
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

if len(queue) == 0:
    print(-1)
    sys.exit(0)

result = -1
isalreadyRipe = True

bfs()

if isalreadyRipe:
    print(0)
    sys.exit(0)

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            sys.exit(0)
        result = max(result, tomato[i][j])

print(result-1)