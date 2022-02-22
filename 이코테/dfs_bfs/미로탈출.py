def main():
    from collections import deque

    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if arr[nx][ny] == 0:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])
    print(arr[N - 1][M - 1])


main()

"""
5 6
101010
111111
000001
111111
111111
"""
