import sys

# 재귀 한도 늘려주기
sys.setrecursionlimit(100000)

def dfs(x, y):
    global cnt
    arr[x][y] = 0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
            dfs(nx,ny)

T = int(sys.stdin.readline())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    # 배추밭의 가로길이 m: 열, 세로길이 n: 행, 배추 위치 개수 k
    m, n, k = map(int, sys.stdin.readline().split())
    # 배추 밭 arr
    arr = [[0] * m for _ in range(n)]
    # 배추 위치 대입
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    cnt = 0
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt = 0
                dfs(i, j)
                result += 1
    print(result)