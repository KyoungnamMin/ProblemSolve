from collections import deque


N, M = map(int, input().split())
board = []
temp = []

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
q = deque()

for i in range(N):
    board.append(list(input().strip()))
    for j in range(M):
        if board[i][j] == "o":
            temp.append((i, j))
q.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))


def bfs():
    while q:
        x1, y1, x2, y2, count = q.popleft()

        # 버튼 10번 넘게 누를 경우
        if count >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if (
                0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M
            ):  # 보드 밖이 아닐 때
                if board[nx1][ny1] == "#":  # 벽일 경우
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                q.append((nx1, ny1, nx2, ny2, count + 1))

            elif not (0 <= nx1 < N and 0 <= ny1 < M) and (
                0 <= nx2 < N and 0 <= ny2 < M
            ):  # coin1 떨어진 경우
                return count + 1
            elif not (0 <= nx2 < N and 0 <= ny2 < M) and (
                0 <= nx1 < N and 0 <= ny1 < M
            ):  # coin2 떨어진 경우
                return count + 1
            else:  # 둘다 떨어진 경우
                continue
    return -1


print(bfs())
