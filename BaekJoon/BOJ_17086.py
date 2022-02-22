from collections import deque

"""
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
"""


def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def bfs(graph):
        dx = [-1, 0, 0, 1, -1, 1, -1, 1]
        dy = [0, 1, -1, 0, -1, 1, 1, -1]
        q = deque()
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    q.append([i, j])

        result = 0
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 0:
                        q.append([nx, ny])
                        graph[nx][ny] = graph[x][y] + 1
                        result = max(result, graph[x][y] + 1)
        return result - 1

    answer = bfs(arr)
    print(answer)


main()
