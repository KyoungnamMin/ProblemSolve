import sys
from collections import deque

def bfs():
    while queue:
        i = queue.popleft()
        if i == k:
            return visited[i]

        for j in (i+1, i-1, i*2):
            if (0 <= j < MAX) and visited[j] == 0:
                visited[j] = visited[i] + 1
                queue.append(j)

n, k = map(int, sys.stdin.readline().split())
queue = deque()
queue.append(n)
MAX = 100001
visited = [0 for i in range(MAX)]
print(bfs())