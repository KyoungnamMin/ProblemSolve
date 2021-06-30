import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dx = [-1, -2, -1, -2, 1, 2, 1, 2]
dy = [-2, -1, 2, 1, -2, -1, 2, 1]

def bfs(nowX, nowY, dstX, dstY):
    queue = deque()
    queue.append((nowX, nowY))
    visited[nowX][nowY] = 1
    while queue:
        x, y = queue.popleft()
        if x == dstX and y == dstY:
            return visited[dstX][dstY] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return 0

for _ in range(T):
    n = int(input())
    nowX, nowY = map(int, input().split())
    dstX, dstY = map(int, input().split())
    visited = [[0] * n for i in range(n)]
    print(bfs(nowX, nowY, dstX, dstY))