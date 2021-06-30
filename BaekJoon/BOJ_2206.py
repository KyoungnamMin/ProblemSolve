import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[[0] * m for _ in range(n)] for _ in range(2)]
queue = deque()

def bfs():
    queue.append((0, 0, 0)) # x, y, passing
    visited[0][0][0] = 1 # passing, x, y
    while queue:
        x, y, p = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[p][x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[p][nx][ny]:
                    if not maze[nx][ny]:
                        visited[p][nx][ny] = visited[p][x][y] + 1
                        queue.append((nx, ny, p))
                    elif maze[nx][ny] and not p:
                        visited[1][nx][ny] = visited[p][x][y] + 1
                        queue.append((nx, ny, 1))
    return -1

print(bfs())