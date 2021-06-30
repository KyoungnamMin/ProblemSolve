import sys

n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
apt = []

def dfs(x,y):
    global cnt
    a[x][y] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == '1':
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt = 0
            dfs(i, j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)